"""TEK FİYAT KAYNAĞI — sitenin bütün fiyat, kota ve oda limiti rakamları buradan gelir.

Kim okuyor:
  - build.py (plan kartları, yıllık tablo, JSON-LD offers, llms.txt, MEGA menü)
  - content_*.py / lang_*.py / pages_v4.py metinleri: rakam yerine ⟦price:starter⟧ gibi
    yer tutucular yazar; build `fill()` ile sayfanın diline göre biçimlendirir.
  - signup_page.py, roi_page.py ve tarayıcıdaki /assets/prices.js (sayfaya gömülen
    <script type="application/json" id="hostlio-pricing"> bloğu: js_config()).

Canlı kaynak: Supabase `plans` uç noktası (Stripe'tan okur). Fiyat ve ödeme sayfası
yüklenince oradan tazelenir; early_bird=false gelirse "ilk 50 müşteri" metinleri gizlenir
ve normal fiyat gösterilir. Buradaki değerler JS'siz ziyaretçi, arama motoru ve
llms.txt içindir — Stripe'ta fiyat değişirse burayı da güncelleyip yeniden derleyin.
Doğrulama: `python3 scripts/check.py --live-prices` canlı `plans` yanıtıyla karşılaştırır.

Backend karşılıkları (hostlio-mobile-main/supabase/functions):
  EARLY_BIRD, DENEME_GUN, PLAN_OZELLIKLERI.aylikMesaj  → _shared/planConfig.ts
  ROOM_LIMITS                                          → signup-checkout/index.ts
"""
import re

EARLY_BIRD = True          # planConfig.ts EARLY_BIRD ile aynı olmalı
CURRENCY = "USD"
TRIAL_DAYS = 7             # planConfig.ts DENEME_GUN
ANNUAL_DISCOUNT_PCT = 20   # yıllık ödeme indirimi (metinlerde "%20")
EARLY_BIRD_SEATS = 50      # "ilk 50 müşteri"

# eb_* = Early Bird (bugün canlı), regular_* = normal fiyat.
# regular_annual Stripe'ta var (starter_annual …) ama sitede hiç gösterilmedi ve
# doğrulanmadı ⇒ None. EARLY_BIRD=False yapmadan önce Stripe'tan okuyup doldurun
# (build None görürse durur).
PLANS = [
    {"id": "starter", "name": "Starter", "eb_monthly": 49,  "eb_annual": 470,  "regular_monthly": 59,  "regular_annual": None,
     "properties": 1, "rooms": 10,  "ai_messages": 1000},
    {"id": "pro",     "name": "Pro",     "eb_monthly": 89,  "eb_annual": 854,  "regular_monthly": 109, "regular_annual": None,
     "properties": 1, "rooms": 50,  "ai_messages": 5000},
    {"id": "growth",  "name": "Growth",  "eb_monthly": 149, "eb_annual": 1430, "regular_monthly": 189, "regular_annual": None,
     "properties": 2, "rooms": 150, "ai_messages": 12000},
]
BY_ID = {p["id"]: p for p in PLANS}


def monthly(pid):
    p = BY_ID[pid]
    return p["eb_monthly"] if EARLY_BIRD else p["regular_monthly"]


def annual(pid):
    p = BY_ID[pid]
    v = p["eb_annual"] if EARLY_BIRD else p["regular_annual"]
    if v is None:
        raise SystemExit(f"pricing.py: {pid} için normal yıllık fiyat (regular_annual) boş — EARLY_BIRD=False öncesi Stripe'tan doldurun.")
    return v


def annual_per_month(pid):
    return round(annual(pid) / 12)


def regular(pid):
    return BY_ID[pid]["regular_monthly"]


# ---------------------------------------------------------------- biçim (O9)
# Dil başına TEK biçim: sembol yeri, binlik ayıracı. Aynı tablo prices.js'e gider,
# böylece sunucuda yazılan "1.430 $" ile tarayıcının yazdığı birebir aynıdır.
NBSP, NNBSP = " ", " "
FORMAT = {
    "en": {"pre": "$",          "post": "",        "group": ","},
    "tr": {"pre": "",           "post": NBSP + "$", "group": "."},
    "es": {"pre": "",           "post": NBSP + "$", "group": "."},
    "it": {"pre": "",           "post": NBSP + "$", "group": "."},
    "pt": {"pre": "US$" + NBSP, "post": "",        "group": "."},
    "fr": {"pre": "",           "post": NBSP + "$", "group": NNBSP},
}


def number(n, lang):
    s = f"{int(n):,}"
    return s.replace(",", FORMAT.get(lang, FORMAT["en"])["group"])


def money(n, lang):
    f = FORMAT.get(lang, FORMAT["en"])
    return f["pre"] + number(n, lang) + f["post"]


# ---------------------------------------------------------------- yer tutucular
# Metinlerde: ⟦price:starter⟧ aktif aylık · ⟦annual:pro⟧ yıllık toplam ·
# ⟦annual_mo:growth⟧ yıllığın aylık karşılığı · ⟦regular:starter⟧ normal aylık ·
# ⟦quota:pro⟧ aylık AI mesajı · ⟦rooms:growth⟧ oda limiti · ⟦trial⟧ deneme günü.
TOKEN = re.compile(r"⟦(\w+)(?::(\w+))?⟧")


def _tok(kind, pid, lang):
    if kind == "price": return money(monthly(pid), lang)
    if kind == "annual": return money(annual(pid), lang)
    if kind == "annual_mo": return money(annual_per_month(pid), lang)
    if kind == "regular": return money(regular(pid), lang)
    if kind == "quota": return number(BY_ID[pid]["ai_messages"], lang)
    if kind == "rooms": return number(BY_ID[pid]["rooms"], lang)
    if kind == "trial": return str(TRIAL_DAYS)
    raise KeyError(kind)


def fill(text, lang):
    """Metindeki bütün ⟦…⟧ yer tutucularını sayfanın diline göre doldurur."""
    return TOKEN.sub(lambda m: _tok(m.group(1), m.group(2), lang), text)


def js_config(lang, endpoint, anon):
    """Tarayıcıya giden yapılandırma (prices.js). Tek kaynak: bu dosya."""
    return {
        "lang": lang, "endpoint": endpoint, "anon": anon, "early_bird": EARLY_BIRD,
        "fmt": FORMAT,
        "plans": {p["id"]: {"name": p["name"], "m": monthly(p["id"]), "a": annual(p["id"]),
                            "r": p["regular_monthly"], "rooms": p["rooms"], "quota": p["ai_messages"]}
                  for p in PLANS},
    }
