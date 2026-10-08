#!/usr/bin/env python3
"""Hostlio Pro static site generator. Run: python3 build.py  -> ./dist"""
import json, os, shutil, html, datetime, re
from pathlib import Path

ROOT = Path(__file__).parent
DIST = ROOT / "dist"

# --- asset cache busting -------------------------------------------------
# /assets/* is served with max-age=86400 + stale-while-revalidate=604800, so an
# unversioned style.css can stay stale in a visitor's browser for days after a
# deploy. Every CSS/JS reference therefore carries a content hash.
import hashlib as _hashlib
def asset(rel: str) -> str:
    """Return the asset path with a ?v=<content hash> suffix."""
    p = ROOT / "src" / rel.lstrip("/")
    try:
        return rel + "?v=" + _hashlib.md5(p.read_bytes()).hexdigest()[:8]
    except OSError:
        return rel
SITE = "https://hostliopro.com"          # canonical host used by the current site
SIGNUP_URL = "/signup/"                          # kayıt sayfası; layout()/finish() bunu sayfa diline göre /xx/signup/ yapar (O3)
LOGIN_URL = "https://dashboard.hostliopro.com"   # dashboard login
FORM_ENDPOINT = "https://hook.eu1.make.com/20b5teacqjk8d330goof6adqly5vyuq2"  # Make.com webhook used by the current contact form
WHATSAPP = "12792682488"; WHATSAPP_TXT = "+1 279-268-2488"
PLANS_ENDPOINT = "https://brzetctpyaxognnvjrnd.supabase.co/functions/v1/plans"  # live prices (Supabase edge function)
PLANS_ANON = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJyemV0Y3RweWF4b2dubnZqcm5kIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Nzk2NDk3MzksImV4cCI6MjA5NTIyNTczOX0.3AKfW8oBvcXmpkwMGh972ko22nJmw0rO28fongc-S3U"  # public anon key (already public on the current site)
EMAIL = "hello@hostliopro.com"
# Y5: "Demo iste / Book a demo" düğmeleri. Cal.com veya Calendly linki (20 dk slot) yazılınca tüm düğmeler
# doğrudan takvime gider; boşken iletişim sayfasına gider. Örn. "https://cal.com/hostliopro/demo"
DEMO_URL = ""
UPDATED = "2026-09-23"
# O3: Hakkımızda — kurucu notu ve ekip. Doldurulunca 6 dilde Hakkımızda sayfasına eklenir (boşken hiç görünmez).
# FOUNDER_NOTE = {"name": "Ad Soyad", "role": "Kurucu", "photo": "/assets/img/team-xxx.webp",
#                 "text": {"en": "...", "tr": "...", "es": "...", "it": "...", "pt": "...", "fr": "..."}}
# TEAM = [{"name": "Ad Soyad", "role": {"en": "Product & engineering", "tr": "Ürün ve yazılım", ...}, "photo": "/assets/img/team-yyy.webp"}]
FOUNDER_NOTE = None
TEAM = []
# ---- measurement & entity config (fill in before launch; empty = not rendered)
# GA4 (8 Eki 2026): ölçüm kimliği. "" yapılırsa hiçbir analitik yüklenmez (gtag yok, izin bandı yok, CSP değişmez,
# gizlilik politikası eski metninde kalır). Doluyken analytics_consent.py'deki çerez/analitik metni politikaya eklenir.
GA4_ID = "G-W74GFJQYJ4"  # hostliopro.com GA4 mülkü (8 Eki 2026, sahip oluşturdu; herkese açık kimlik, sır değil)
PLAUSIBLE_DOMAIN = ""  # e.g. "hostliopro.com"
GSC_VERIFY = ""        # Google Search Console HTML-tag token
BING_VERIFY = ""       # Bing Webmaster msvalidate.01 token
INDEXNOW_KEY = "7f3c9a1e5b2d4c8f9e0a6b1d2c3e4f50"
SAME_AS = [           # SEO: yalnız gerçekten yayında olan resmî profiller (8 Ekim 2026'da doğrulandı; geliştirici Loti Members LLC)
    "https://apps.apple.com/us/app/hostlio-pro-hotel-management/id6765888744",
    "https://play.google.com/store/apps/details?id=com.hostlio.hostliopro",
]  # official profiles: LinkedIn, Instagram, YouTube, X, Hotel Tech Report, G2, Capterra...
APP_STORE_URL = ""     # iOS app link
UPDATED_TXT = {"tr": "23 Eylül 2026", "en": "September 23, 2026"}
LANGS = ["tr", "en", "es", "it", "pt", "fr"]
NEW_LANGS = ["es", "it", "pt", "fr"]
LANG_NAME = {"tr": "Türkçe", "en": "English", "es": "Español", "it": "Italiano", "pt": "Português", "fr": "Français"}
LOCALE = {"tr": "tr_TR", "en": "en_US", "es": "es_ES", "it": "it_IT", "pt": "pt_BR", "fr": "fr_FR"}
IN_LANG = {"tr": "tr-TR", "en": "en", "es": "es", "it": "it", "pt": "pt-BR", "fr": "fr"}
# D3: Portekizce içerik Brezilya Portekizcesi ("celular", "notebook"); html lang pt-BR kalır.
# SEO 4.4 (8 Ekim): hreflang bölgesiz "pt" — Google tek Portekizce sürümü hem Brezilya hem Portekiz için kullanır.
HREFLANG = {"tr": "tr", "en": "en", "es": "es", "it": "it", "pt": "pt", "fr": "fr"}
import importlib as _il
import analytics_consent
LANGMOD = {l: _il.import_module("lang_" + l) for l in NEW_LANGS}
for _l, _m in LANGMOD.items(): UPDATED_TXT[_l] = _m.UPDATED_TXT

# ---------------------------------------------------------------- routes
ROUTES = {
    "home":     {"tr": "/",                         "en": "/en/"},
    "ai":       {"tr": "/ai-misafir-asistani/",     "en": "/en/ai-guest-messaging/"},
    "channel":  {"tr": "/kanal-yoneticisi/",        "en": "/en/channel-manager/"},
    "checkin":  {"tr": "/online-check-in/",         "en": "/en/online-check-in/"},
    "features": {"tr": "/ozellikler/",              "en": "/en/features/"},
    "pricing":  {"tr": "/fiyatlandirma/",           "en": "/en/pricing/"},
    "faq":      {"tr": "/sss/",                     "en": "/en/faq/"},
    "about":    {"tr": "/hakkimizda/",              "en": "/en/about/"},
    "contact":  {"tr": "/iletisim/",                "en": "/en/contact/"},
    "blog":     {"tr": "/blog/",                    "en": "/en/blog/"},
    "post-pms": {"tr": "/blog/kucuk-otel-icin-otel-yonetim-yazilimi-secimi/",
                 "en": "/en/blog/choosing-hotel-management-software-small-hotel/"},
    "post-ai":  {"tr": "/blog/otel-misafir-mesajlarini-yapay-zeka-ile-yanitlamak/",
                 "en": "/en/blog/answering-hotel-guest-messages-with-ai/"},
    "post-overbooking": {"tr": "/blog/overbooking-nasil-onlenir/", "en": "/en/blog/how-to-prevent-overbooking/"},
    "post-autoreply":   {"tr": "/blog/booking-com-mesajlarina-otomatik-cevap/", "en": "/en/blog/auto-reply-booking-com-messages/"},
    "t-guesthouse": {"tr": "/pansiyon-programi/",   "en": "/en/guesthouse-software/"},
    "t-boutique":   {"tr": "/butik-otel-programi/", "en": "/en/boutique-hotel-software/"},
    "t-apart":      {"tr": "/apart-otel-programi/", "en": "/en/aparthotel-software/"},
    "t-hostel":     {"tr": "/hostel-programi/",     "en": "/en/hostel-software/"},
    "compare":      {"tr": "/otel-programi-karsilastirma/", "en": "/en/hotel-software-comparison/"},
    "privacy":      {"tr": "/gizlilik-politikasi/", "en": "/privacy/"},
    "terms":        {"tr": "/kullanim-sartlari/",   "en": "/terms/"},
    # tasarim-v2: hesap silme sayfası yeni tasarıma alındı. EN adresi uygulama
    # mağazalarında kayıtlı olabilir: /delete-account (vercel.json → /delete-account/).
    "delacc":       {"tr": "/hesap-silme/", "en": "/delete-account/"},
    # legacy English posts from the previous site (EN only; old URLs 301 → these)
    "post-aifrontdesk": {"en": "/en/blog/hotel-ai-front-desk-guide/"},
    "post-noshows":     {"en": "/en/blog/how-to-reduce-hotel-no-shows/"},
    "post-chains":      {"en": "/en/blog/independent-hotel-vs-chain-technology/"},
    "post-whatsapp":    {"en": "/en/blog/whatsapp-hotel-guest-communication/"},
}
for _k, _v in {'home': ('/es/', '/it/', '/pt/', '/fr/'), 'ai': ('/es/asistente-ia-para-huespedes/', '/it/assistente-ai-ospiti/', '/pt/assistente-ia-para-hospedes/', '/fr/assistant-ia-clients/'), 'channel': ('/es/channel-manager/', '/it/channel-manager/', '/pt/channel-manager/', '/fr/channel-manager/'), 'checkin': ('/es/check-in-online/', '/it/check-in-online/', '/pt/check-in-online/', '/fr/check-in-en-ligne/'), 'features': ('/es/funcionalidades/', '/it/funzionalita/', '/pt/funcionalidades/', '/fr/fonctionnalites/'), 'pricing': ('/es/precios/', '/it/prezzi/', '/pt/precos/', '/fr/tarifs/'), 'faq': ('/es/preguntas-frecuentes/', '/it/domande-frequenti/', '/pt/perguntas-frequentes/', '/fr/faq/'), 'about': ('/es/sobre-nosotros/', '/it/chi-siamo/', '/pt/sobre-nos/', '/fr/a-propos/'), 'contact': ('/es/contacto/', '/it/contatti/', '/pt/contato/', '/fr/contact/'), 'blog': ('/es/blog/', '/it/blog/', '/pt/blog/', '/fr/blog/'), 'post-pms': ('/es/blog/como-elegir-software-de-gestion-hotelera-hotel-pequeno/', '/it/blog/come-scegliere-gestionale-per-hotel-piccolo/', '/pt/blog/como-escolher-sistema-para-hotel-pequeno/', '/fr/blog/choisir-logiciel-gestion-hoteliere-petit-hotel/'), 'post-ai': ('/es/blog/responder-mensajes-de-huespedes-con-ia/', '/it/blog/rispondere-ai-messaggi-degli-ospiti-con-ai/', '/pt/blog/responder-mensagens-de-hospedes-com-ia/', '/fr/blog/repondre-aux-messages-clients-avec-ia/'), 'post-overbooking': ('/es/blog/como-evitar-el-overbooking/', '/it/blog/come-evitare-overbooking/', '/pt/blog/como-evitar-overbooking/', '/fr/blog/comment-eviter-le-surbooking/'), 'post-autoreply': ('/es/blog/respuesta-automatica-mensajes-booking-com/', '/it/blog/risposta-automatica-messaggi-booking-com/', '/pt/blog/resposta-automatica-mensagens-booking-com/', '/fr/blog/reponse-automatique-messages-booking-com/'), 't-guesthouse': ('/es/software-para-hostales/', '/it/gestionale-b-and-b/', '/pt/sistema-para-pousadas/', '/fr/logiciel-chambres-d-hotes/'), 't-boutique': ('/es/software-hotel-boutique/', '/it/gestionale-boutique-hotel/', '/pt/sistema-hotel-boutique/', '/fr/logiciel-hotel-boutique/'), 't-apart': ('/es/software-apartahotel/', '/it/gestionale-residence-aparthotel/', '/pt/sistema-apart-hotel/', '/fr/logiciel-residence-hoteliere/'), 't-hostel': ('/es/software-para-hostels/', '/it/gestionale-ostelli/', '/pt/sistema-para-hostels/', '/fr/logiciel-auberge-de-jeunesse/'), 'compare': ('/es/comparativa-software-hotelero/', '/it/confronto-gestionali-hotel/', '/pt/comparativo-sistemas-para-hotel/', '/fr/comparatif-logiciels-hoteliers/'), 'privacy': ('/es/privacidad/', '/it/privacy/', '/pt/privacidade/', '/fr/confidentialite/'), 'terms': ('/es/terminos/', '/it/termini/', '/pt/termos/', '/fr/conditions/'), 'delacc': ('/es/eliminar-cuenta/', '/it/elimina-account/', '/pt/excluir-conta/', '/fr/supprimer-compte/')}.items():
    ROUTES[_k].update(dict(zip(NEW_LANGS, _v)))
# K4 (Eylül 2026): kök adres artık dil seçmiyor — Türkçe /tr/ altına taşındı; "/" Accept-Language'a göre
# /tr/, /es/, /it/, /pt/, /fr/ ya da /en/'e yönlenir (vercel.json). Eski Türkçe adresler 301 ile /tr/... adresine gider.
# O2: gizlilik, şartlar ve hesap silme İngilizcede de /en/ altında.
OLD_TR = {k: v["tr"] for k, v in ROUTES.items() if "tr" in v}
OLD_EN_ROOT = {k: ROUTES[k]["en"] for k in ("privacy", "terms", "delacc")}
for _k, _v in ROUTES.items():
    if "tr" in _v: _v["tr"] = "/tr" + _v["tr"]
ROUTES["privacy"]["en"] = "/en/privacy/"; ROUTES["terms"]["en"] = "/en/terms/"; ROUTES["delacc"]["en"] = "/en/delete-account/"
# K5 + güçlendirme: Güvenlik ve veri sayfası (6 dil) ve DPA (yalnız İngilizce, esas metin)
ROUTES["security"] = {"tr": "/tr/guvenlik-ve-veri/", "en": "/en/security/", "es": "/es/seguridad/", "it": "/it/sicurezza/", "pt": "/pt/seguranca/", "fr": "/fr/securite/"}
ROUTES["dpa"] = {"en": "/en/dpa/"}
ROUTES["roi"] = {"tr": "/tr/roi-hesaplayici/", "en": "/en/roi-calculator/", "es": "/es/calculadora-roi/", "it": "/it/calcolatore-roi/", "pt": "/pt/calculadora-roi/", "fr": "/fr/calculateur-roi/"}
# S9 (8 Ekim 2026): ücretsiz araçlar (tools_pages.py), karşılaştırmalar (compare_pages.py), TR rehberleri (guides_tr.py).
# Bir sayfa yalnız var olduğu dillerde listelenir; hreflang/sitemap ROUTES'tan türetilir.
ROUTES.update({
 "tools":      {"tr": "/tr/araclar/", "en": "/en/tools/", "es": "/es/herramientas/", "it": "/it/strumenti/", "pt": "/pt/ferramentas/", "fr": "/fr/outils/"},
 "kpi":        {"tr": "/tr/araclar/revpar-adr-doluluk-hesaplama/", "en": "/en/tools/revpar-adr-occupancy-calculator/", "es": "/es/herramientas/calculadora-revpar-adr-ocupacion/",
                "it": "/it/strumenti/calcolo-revpar-adr-occupazione/", "pt": "/pt/ferramentas/calculadora-revpar-adr-ocupacao/", "fr": "/fr/outils/calcul-revpar-adr-taux-occupation/"},
 "commission": {"tr": "/tr/araclar/ota-komisyon-hesaplama/", "en": "/en/tools/ota-commission-calculator/", "es": "/es/herramientas/calculadora-comision-ota/",
                "it": "/it/strumenti/calcolatore-commissioni-ota/", "pt": "/pt/ferramentas/calculadora-comissao-ota/", "fr": "/fr/outils/calculateur-commission-ota/"},
 "cmp-hub":    {"tr": "/tr/karsilastirmalar/", "en": "/en/compare/", "es": "/es/comparativas/", "pt": "/pt/comparativos/", "fr": "/fr/comparatifs/"},
 "vs-hotelrunner": {"tr": "/tr/karsilastirmalar/hostlio-vs-hotelrunner/", "en": "/en/compare/hostlio-vs-hotelrunner/"},
 "vs-elektraweb":  {"tr": "/tr/karsilastirmalar/hostlio-vs-elektraweb/", "en": "/en/compare/hostlio-vs-elektraweb/"},
 "vs-cloudbeds":   {"en": "/en/compare/hostlio-vs-cloudbeds/", "es": "/es/comparativas/hostlio-vs-cloudbeds/", "pt": "/pt/comparativos/hostlio-vs-cloudbeds/"},
 "alt-cloudbeds":  {"en": "/en/compare/cloudbeds-alternatives/", "es": "/es/comparativas/alternativas-a-cloudbeds/", "pt": "/pt/comparativos/alternativas-ao-cloudbeds/"},
 "alt-amenitiz":   {"en": "/en/compare/amenitiz-alternative/", "fr": "/fr/comparatifs/alternative-amenitiz/"},
 "alt-hijiffy":    {"en": "/en/compare/hijiffy-alternative/", "pt": "/pt/comparativos/alternativa-hijiffy/"},
 "whatsapp-tr":    {"tr": "/tr/otel-whatsapp-asistani/"},
 "post-channel-manager": {"tr": "/tr/blog/channel-manager-nedir/"},
 "post-kbs":       {"tr": "/tr/blog/kbs-bildirimi-nasil-yapilir/"},
 "post-prices":    {"tr": "/tr/blog/otel-programi-fiyatlari-2026/"},
 # Tur 2 (8 Ekim 2026): SEO fikri #20 ve #14 (guides_intl.py)
 "post-pms-vs-cm": {"en": "/en/blog/pms-vs-channel-manager/", "it": "/it/blog/channel-manager-cos-e-differenza-pms/",
                    "pt": "/pt/blog/o-que-e-channel-manager-diferenca-pms/", "fr": "/fr/blog/pms-ou-channel-manager-difference/"},
})
ROUTES["post-whatsapp"].update({"es": "/es/blog/whatsapp-para-hoteles/", "it": "/it/blog/whatsapp-per-hotel/", "fr": "/fr/blog/whatsapp-pour-hotels/"})
TOOLS_LABEL = {"tr": "Ücretsiz araçlar", "en": "Free tools", "es": "Herramientas gratis", "it": "Strumenti gratuiti", "pt": "Ferramentas grátis", "fr": "Outils gratuits"}
CMP_LABEL = {"tr": "Karşılaştırmalar", "en": "Comparisons", "es": "Comparativas", "it": "Confronti", "pt": "Comparativos", "fr": "Comparatifs"}
def xdefault(key): return "en" if "en" in ROUTES[key] else langs(key)[0]   # tek dilli (yalnız TR) sayfa x-default'u kendisi
# Q2: mobil menü düğmesinin açık/kapalı etiketi; Q1: footer'daki panel girişi; Q9: footer check-in etiketi
MENU_CLOSE = {"tr": "Menüyü kapat", "en": "Close menu", "es": "Cerrar menú", "it": "Chiudi il menu", "pt": "Fechar menu", "fr": "Fermer le menu"}
FOOT_LOGIN = {"tr": "Panele giriş", "en": "Log in to dashboard", "es": "Acceso al panel", "it": "Accedi al pannello", "pt": "Entrar no painel", "fr": "Connexion au tableau de bord"}
CHECKIN_LABEL = {"tr": "Online check-in", "en": "Online check-in", "es": "Check-in online", "it": "Check-in online", "pt": "Check-in online", "fr": "Check-in en ligne"}
ROI_LABEL = {"tr": "Tasarruf hesaplayıcı", "en": "ROI calculator", "es": "Calculadora de ROI", "it": "Calcolatore ROI", "pt": "Calculadora de ROI", "fr": "Calculateur de ROI"}
def url(key, lang): return ROUTES[key].get(lang) or ROUTES["blog"][lang]
def demo_url(lang): return DEMO_URL or url("contact", lang)
def langs(key): return [l for l in LANGS if l in ROUTES[key]]
def abs_url(key, lang): return SITE + url(key, lang)

UI = {
 "tr": {
   "nav": [("features","Özellikler"),("ai","AI Asistan Lio"),("channel","Kanal Yöneticisi"),("pricing","Fiyatlar"),("blog","Blog")],
   "top": [("pricing","Fiyatlar"),("blog","Blog"),("faq","SSS"),("about","Hakkımızda")],
   "login":"Giriş", "trial":"Ücretsiz dene", "demo":"Demo iste", "menu":"Menüyü aç",
   "skip":"İçeriğe geç", "home":"Ana sayfa", "other":"English", "other_label":"Switch to English",
   "foot_tag":"Bağımsız oteller ve pansiyonlar için yapay zekâ destekli otel programı. Misafir mesajları, kanal yönetimi ve rezervasyon takvimi tek panelde.",
   "foot_product":"Ürün","foot_company":"Şirket","foot_res":"Kaynaklar","foot_sol":"Çözümler","privacy":"Gizlilik Politikası","terms":"Kullanım Şartları","delacc":"Hesap silme","sol":["Butik otel programı","Pansiyon programı","Apart otel programı","Hostel programı","Otel programı karşılaştırması"],
   "foot_about":"Hakkımızda","foot_contact":"İletişim","foot_faq":"Sık sorulan sorular",
   "rights":"Tüm hakları saklıdır.","updated":"Son güncelleme",
   "final_h":"Resepsiyonunuzu bu gece de açık tutun.",
   "final_p":"7 gün ücretsiz deneyin. Deneme bitene kadar ücret alınmaz, istediğiniz zaman iptal edin.",
   "faq_h":"Sık sorulan sorular",
 },
 "en": {
   "nav": [("features","Features"),("ai","Lio AI assistant"),("channel","Channel manager"),("pricing","Pricing"),("blog","Blog")],
   "top": [("pricing","Pricing"),("blog","Blog"),("faq","FAQ"),("about","About")],
   "login":"Log in", "trial":"Try it free", "demo":"Book a demo", "menu":"Open menu",
   "skip":"Skip to content", "home":"Home", "other":"Türkçe", "other_label":"Türkçe'ye geç",
   "foot_tag":"AI-powered hotel management software for independent hotels. Guest messaging, channel management and the reservation calendar in one place.",
   "foot_product":"Product","foot_company":"Company","foot_res":"Resources","foot_sol":"Solutions","privacy":"Privacy Policy","terms":"Terms of Service","delacc":"Delete account","sol":["Boutique hotel software","Guesthouse software","Aparthotel software","Hostel software","Hotel software comparison"],
   "foot_about":"About","foot_contact":"Contact","foot_faq":"FAQ",
   "rights":"All rights reserved.","updated":"Last updated",
   "final_h":"Keep your front desk open tonight, too.",
   "final_p":"Try it free for 7 days. No charge until your trial ends, cancel anytime.",
   "faq_h":"Frequently asked questions",
 },
}

LOGO = ('<svg viewBox="0 0 32 32" aria-hidden="true"><rect width="32" height="32" rx="8" fill="#1B2B4B" stroke="rgba(255,255,255,.18)"/>'
        '<path d="M10.5 8v16M21.5 8v16" stroke="#fff" stroke-width="3.2" stroke-linecap="round"/>'
        '<path d="M10.5 16h11" stroke="#FF6B35" stroke-width="3.2" stroke-linecap="round"/><circle cx="25.2" cy="25.4" r="2.6" fill="#FF6B35"/></svg>')
CHECK = '<svg viewBox="0 0 20 20" fill="none" aria-hidden="true"><path d="M4 10.5l4 4 8-9" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>'

# ---------------------------------------------------------------- schema
def org_schema():
    return {
        "@type": "Organization", "@id": SITE + "/#org", "name": "Hostlio Pro",
        "alternateName": "Hostlio", "legalName": "Loti Members LLC",
        "url": SITE + "/", "logo": SITE + "/assets/logo.png", "email": EMAIL,
        "address": {"@type": "PostalAddress", "streetAddress": "2108 N ST STE N",
                    "addressLocality": "Sacramento", "addressRegion": "CA",
                    "postalCode": "95816", "addressCountry": "US"},
        "telephone": "+1-279-268-2488",
        "contactPoint": {"@type": "ContactPoint", "email": EMAIL, "telephone": "+1-279-268-2488", "contactType": "sales",
                         "availableLanguage": ["English", "Turkish"]},
        **({"sameAs": SAME_AS} if SAME_AS else {}),
    }

def website_schema(lang):
    return {"@type": "WebSite", "@id": SITE + "/#website", "url": SITE + "/", "name": "Hostlio Pro",
            "inLanguage": [IN_LANG[l] for l in LANGS], "publisher": {"@id": SITE + "/#org"}}

# Y2: fiyat/kota/oda limiti TEK KAYNAKTAN (pricing.py). Buradaki liste yalnız eski
# çağıranlar (content_*.py, roi_page.py) için türetilmiş görünüm; rakam YAZMAYIN.
import pricing
PLANS = [{"id": p["id"], "name": p["name"], "price": pricing.monthly(p["id"]), "regular": p["regular_monthly"],
          "annual": pricing.annual(p["id"]), "rooms": p["rooms"], "quota": p["ai_messages"]} for p in pricing.PLANS]

def software_schema(lang, detailed=False):
    desc = {"tr": "Bağımsız oteller için yapay zekâ destekli otel yönetim yazılımı: WhatsApp ve OTA gelen kutularında 30+ dilde 7/24 misafir mesajlaşması, 100+ OTA kanal yöneticisi, rezervasyon takvimi ve online check-in.",
            "en": "AI-powered hotel management software for independent hotels: 24/7 guest messaging on WhatsApp and OTA inboxes in 30+ languages, a channel manager for 100+ OTAs, a reservation calendar and online check-in."}.get(lang, "")
    if lang in LANGMOD: desc = LANGMOD[lang].SOFT_DESC
    s = {"@type": "SoftwareApplication", "@id": SITE + "/#software", "name": "Hostlio Pro",
         "applicationCategory": "BusinessApplication",
         "applicationSubCategory": "Hotel management software (PMS)",
         "operatingSystem": "Web, iOS, Android", "description": desc, "url": abs_url("home", lang),
         "publisher": {"@id": SITE + "/#org"},
         "featureList": {"tr": ["AI misafir asistanı Lio (WhatsApp ve OTA gelen kutuları, 30+ dil)", "Kanal yöneticisi (100+ OTA'ya sertifikalı bağlantı)", "Sürükle-bırak rezervasyon takvimi", "Online check-in: KVKK uyumlu belge tarama (görüntü saklanmaz) ve dijital imza", "Vize için konaklama onayı (PDF)", "Transfer ve tur satışı", "Lio Önerileri: her sabah fiyat ve operasyon önerileri (onayınızla)", "Lio ile WhatsApp'ta rezervasyon ve ek hizmet talebi (onaylı)", "Yorum ve misafir mesajlarından AI içgörüleri", "Doluluk, ADR, RevPAR ve kanal performansı raporları", "iOS ve Android mobil uygulaması"],
                         "en": ["Lio AI guest assistant (WhatsApp and OTA inboxes, 30+ languages)", "Channel manager (certified connections to 100+ OTAs)", "Drag-and-drop reservation calendar", "Online check-in with ID document scanning (no images stored) and digital signature", "Accommodation confirmation for visa applications (PDF)", "Transfer and tour sales", "Lio Suggestions: daily pricing and operations suggestions (approval-based)", "Booking and extra-service requests via Lio on WhatsApp (approval-based)", "AI insights from reviews and guest messages", "Occupancy, ADR, RevPAR and channel performance reports", "iOS and Android mobile app"], **{l: m.SOFT_FEATURES for l, m in LANGMOD.items()}}[lang],
         "offers": {"@type": "AggregateOffer", "priceCurrency": pricing.CURRENCY, "lowPrice": str(min(p["price"] for p in PLANS)), "highPrice": str(max(p["price"] for p in PLANS)), "offerCount": str(len(PLANS))},
         **({"downloadUrl": APP_STORE_URL, "installUrl": APP_STORE_URL} if APP_STORE_URL else {})}
    if detailed:
        s["offers"] = [{"@type": "Offer", "name": p["name"], "price": str(p["price"]), "priceCurrency": pricing.CURRENCY,
                        "url": abs_url("pricing", lang),
                        "priceSpecification": {"@type": "UnitPriceSpecification", "price": str(p["price"]),
                                               "priceCurrency": pricing.CURRENCY, "unitCode": "MON", "billingDuration": 1}}
                       for p in PLANS] + [
                      {"@type": "Offer", "name": p["name"] + " (annual)", "price": str(p["annual"]), "priceCurrency": pricing.CURRENCY,
                        "url": abs_url("pricing", lang),
                        "priceSpecification": {"@type": "UnitPriceSpecification", "price": str(p["annual"]),
                                               "priceCurrency": pricing.CURRENCY, "unitCode": "ANN", "billingDuration": 1}}
                       for p in PLANS]
    return s

def faq_schema(faq):
    return {"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)}} for q, a in faq]}

def crumbs_schema(trail):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + u} for i, (n, u) in enumerate(trail)]}

def strip_tags(s):
    import re
    return html.unescape(re.sub(r"<[^>]+>", "", s)).strip()

# ---------------------------------------------------------------- components
import functools
@functools.lru_cache(None)
def _svg(folder, name):
    return (ROOT / folder / f"{name}.svg").read_text()
def icon(name, cls="ico"):
    s = _svg("icons", name)
    return s.replace("<svg ", f'<svg class="{cls}" aria-hidden="true" focusable="false" ', 1)
def logo(name, label=None):
    import re as _re
    s = _re.sub(r"<title>.*?</title>", "", _svg("logos", name))
    s = s.replace(' role="img"', "")
    if label:
        return s.replace("<svg ", f'<svg role="img" aria-label="{label}" class="lg" ', 1)
    return s.replace("<svg ", '<svg aria-hidden="true" class="lg" ', 1)
ARROW = None
def btn(label, href, kind="primary", extra=""):
    return f'<a class="btn btn-{kind}" href="{href}"{extra}>{label}<span class="bi">{icon("arrow-up-right")}</span></a>'

def faq_block(faq, lang, heading=True, wrap=True):
    items = "".join(f'<details><summary>{html.escape(q)}</summary><div class="a"><p>{a}</p></div></details>' for q, a in faq)
    if not wrap:
        return f'<div class="faq">{items}</div>'
    return (f'<section class="rule" aria-labelledby="faq-h"><div class="wrap faq-wrap"><h2 id="faq-h">{UI[lang]["faq_h"]}</h2>'
            f'<div class="faq">{items}</div></div></section>')

# D6 (WCAG 2.2.2): 10 sn'lik döngü videosu için duraklat/oynat düğmesi (video oynamaya başlayınca görünür)
VIDEO_BTN = {"en": ("Pause video", "Play video"), "tr": ("Videoyu duraklat", "Videoyu oynat"), "es": ("Pausar vídeo", "Reproducir vídeo"),
             "it": ("Metti in pausa il video", "Riproduci il video"), "pt": ("Pausar vídeo", "Reproduzir vídeo"), "fr": ("Mettre la vidéo en pause", "Lire la vidéo")}
def final_cta(lang):
    u = UI[lang]
    return f'''<section><div class="wrap"><div class="final on-dark">
<img src="/assets/img/gen-night-desk.webp" alt="" loading="lazy" width="1080" height="1350">
<video class="final-video" muted loop playsinline preload="none" aria-hidden="true" tabindex="-1" data-webm="/assets/video/night-desk.webm" data-mp4="/assets/video/night-desk.mp4"></video>
<button type="button" class="vid-toggle" hidden aria-pressed="false" data-pause="{VIDEO_BTN[lang][0]}" data-play="{VIDEO_BTN[lang][1]}" aria-label="{VIDEO_BTN[lang][0]}"><span class="vt-pause" aria-hidden="true"></span></button>
<div><h2>{u["final_h"]}</h2><p>{u["final_p"]}</p></div>
<div class="cta-row">{btn(u["trial"], SIGNUP_URL)}{btn(u["demo"], demo_url(lang), "ghost")}</div>
</div></div></section>'''

def crumbs_html(trail, lang):
    lis = []
    for i, (n, u_) in enumerate(trail):
        if i == len(trail) - 1:
            lis.append(f'<li aria-current="page">{html.escape(n)}</li>')
        else:
            lis.append(f'<li><a href="{u_}">{html.escape(n)}</a></li>')
    label = UI[lang]["crumb_label"]
    return f'<nav class="crumbs wrap" aria-label="{label}"><ol>{"".join(lis)}</ol></nav>'

def room_rack(lang):
    days = {"tr": ["Pzt","Sal","Çar","Per","Cum","Cmt","Paz"], "en": ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"], **{l: m.DAYS for l, m in LANGMOD.items()}}[lang]
    dates = [15,16,17,18,19,20,21]
    head = '<div class="h"></div>' + "".join(
        f'<div class="h{" today" if i==2 else ""}">{d}<b class="num">{n}</b></div>' for i,(d,n) in enumerate(zip(days,dates)))
    rows = [
      ("101", [(0,3,"bk","M. Tanaka"),(3,4,"dr","Öztürk")]),
      ("102", [(1,2,"ab","L. Rossi"),(4,3,"ex","J. Miller")]),
      ("103", [(0,5,"ag","N. Hoang")]),
      ("201", [(2,2,"dr","Kaya"),(5,2,"bk","S. Weber")]),
      ("202", [(0,2,"ex","A. Dubois"),(3,3,"bk","K. Sato")]),
      ("203", [(1,4,"ab","E. García")]),
    ]
    body = ""
    for room, bars in rows:
        b = "".join(f'<div class="bar {c}" style="left:calc({s}*100%/7 + 3px);width:calc({l}*100%/7 - 6px)">{html.escape(nm)}</div>' for s,l,c,nm in bars)
        body += f'<div class="rack-row"><div class="rack-room num">{room}</div><div class="rack-lane">{b}</div></div>'
    if lang in LANGMOD: title, sub, legend = LANGMOD[lang].RACK
    else:
      title = {"tr":"Oda rafı","en":"Room rack"}[lang]
      sub = {"tr":"Eylül, 3. hafta","en":"September, week 3"}[lang]
      legend = {"tr":"Rezervasyonlar kanal renkleriyle: Booking.com mavi, Airbnb şeftali, Expedia lila, Agoda kum, direkt rezervasyon yeşil","en":"Bookings colour-coded by channel: Booking.com blue, Airbnb peach, Expedia lilac, Agoda sand, direct green"}[lang]
    return f'''<figure class="ui" role="img" aria-label="{title}. {legend}" style="margin:0"><div class="ui-top">{title}<span>{sub}</span></div>
<div class="rack-grid" aria-hidden="true">{head}{body}</div></figure>'''

def channel_strip(lang):
    return ""

MEGA = {
 "tr": {"btn":"Ürün","cols":[
   ("Misafir",[("ai","sparkle","AI asistan Lio","30+ dilde 7/24 misafir yanıtı"),("checkin","identification-card","Online check-in","Kimlik, refakatçi ve dijital imza")]),
   ("Dağıtım",[("channel","arrows-left-right","Kanal yöneticisi","100+ OTA tek takvimde"),("features","calendar-dots","Oda rafı","Sürükle-bırak rezervasyon takvimi")]),
   ("İşletme",[("features","van","Transfer ve tur satışı","Mesajlaşırken ek gelir"),("features","device-mobile","Mobil uygulama","iOS ve Android, otel dışından yönetim")]),
   ("Tesis tipine göre",[("t-boutique","sparkle","Butik otel programı","10–50 odalı oteller"),("t-guesthouse","users-three","Pansiyon programı","1–10 odalı işletmeler"),("t-apart","calendar-dots","Apart otel programı","Daire ve suitler"),("t-hostel","globe-simple","Hostel programı","Çok dilli gezginler")]),
  ],"feat":("pricing","Planları karşılaştır","Aylık ⟦price:starter⟧'dan başlar, 7 gün ücretsiz")},
 "en": {"btn":"Product","cols":[
   ("Guests",[("ai","sparkle","Lio AI assistant","24/7 guest replies in 30+ languages"),("checkin","identification-card","Online check-in","ID, companions and digital signature")]),
   ("Distribution",[("channel","arrows-left-right","Channel manager","100+ OTAs on one calendar"),("features","calendar-dots","Room rack","Drag-and-drop reservation calendar")]),
   ("Operations",[("features","van","Transfers and tours","Extra revenue while you chat"),("features","device-mobile","Mobile app","iOS and Android, manage on the go")]),
   ("By property",[("t-boutique","sparkle","Boutique hotels","10–50 room hotels"),("t-guesthouse","users-three","Guesthouses","1–10 room properties"),("t-apart","calendar-dots","Aparthotels","Apartments and suites"),("t-hostel","globe-simple","Hostels","Multilingual travellers")]),
  ],"feat":("pricing","Compare plans","From ⟦price:starter⟧ a month, 7 days free")},
}
for _l, _m in LANGMOD.items():
    UI[_l] = _m.UI; MEGA[_l] = _m.MEGA
EXTRA = {
 "tr": dict(bill_m="Aylık", bill_a="Yıllık", save="%20 tasarruf", billed_a="yıllık faturalandırılır", form_ok="Mesajınız bize ulaştı. İş günlerinde genellikle 24 saat içinde dönüş yapıyoruz.", form_err="Gönderilemedi. Lütfen e-posta ya da WhatsApp ile yazın.", resp="İş günlerinde genellikle 24 saat içinde yanıt veriyoruz.", sending="Gönderiliyor…"),
 "en": dict(bill_m="Monthly", bill_a="Annual", save="Save 20%", billed_a="billed annually", form_ok="Thanks, your message reached us. We typically reply within 24 hours on business days.", form_err="Couldn't send. Please email us or write on WhatsApp.", resp="We typically reply within 24 hours on business days.", sending="Sending…"),
 "es": dict(bill_m="Mensual", bill_a="Anual", save="Ahorra 20 %", billed_a="facturado anualmente", form_ok="Gracias, hemos recibido tu mensaje. Solemos responder en 24 horas en días laborables.", form_err="No se pudo enviar. Escríbenos por email o WhatsApp.", resp="Solemos responder en 24 horas en días laborables.", sending="Enviando…"),
 "it": dict(bill_m="Mensile", bill_a="Annuale", save="Risparmi il 20%", billed_a="fatturato annualmente", form_ok="Grazie, abbiamo ricevuto il tuo messaggio. Di solito rispondiamo entro 24 ore nei giorni lavorativi.", form_err="Invio non riuscito. Scrivici via email o WhatsApp.", resp="Di solito rispondiamo entro 24 ore nei giorni lavorativi.", sending="Invio…"),
 "pt": dict(bill_m="Mensal", bill_a="Anual", save="Economize 20%", billed_a="cobrado anualmente", form_ok="Obrigado, recebemos sua mensagem. Costumamos responder em até 24 horas em dias úteis.", form_err="Não foi possível enviar. Escreva para nosso e-mail ou WhatsApp.", resp="Costumamos responder em até 24 horas em dias úteis.", sending="Enviando…"),
 "fr": dict(bill_m="Mensuel", bill_a="Annuel", save="Économisez 20 %", billed_a="facturé annuellement", form_ok="Merci, votre message nous est bien parvenu. Nous répondons généralement sous 24 heures les jours ouvrés.", form_err="L’envoi a échoué. Écrivez-nous par e-mail ou sur WhatsApp.", resp="Nous répondons généralement sous 24 heures les jours ouvrés.", sending="Envoi…"),
}
ANNUAL = {
 "tr": dict(billed_line_m="aylık faturalandırılır", billed_line_a="yılda {at} tek ödeme", annual_line="Yıllık: aylık {am}, yılda {at} tek ödeme", tbl_h="Aylık ve yıllık fiyatlar", tbl_cols=("Plan","Aylık","Yıllık (aylık karşılığı)","Yıllık toplam","Normal aylık fiyat"), tbl_note="Early Bird fiyatları, ABD doları. Yıllık ödemede aylık ödemeye göre %20 tasarruf edersiniz."),
 "en": dict(billed_line_m="billed monthly", billed_line_a="{at} billed yearly", annual_line="Annual: {am}/mo, {at} billed yearly", tbl_h="Monthly and annual prices", tbl_cols=("Plan","Monthly","Annual (per month)","Annual total","Regular monthly price"), tbl_note="Early-bird prices in USD. Annual billing saves 20% compared with paying monthly."),
 "es": dict(billed_line_m="facturado mensualmente", billed_line_a="{at} facturados al año", annual_line="Anual: {am}/mes, {at} facturados al año", tbl_h="Precios mensuales y anuales", tbl_cols=("Plan","Mensual","Anual (por mes)","Total anual","Precio mensual habitual"), tbl_note="Precios de lanzamiento en USD. La facturación anual ahorra un 20 % frente al pago mensual."),
 "it": dict(billed_line_m="fatturato mensilmente", billed_line_a="{at} fatturati all’anno", annual_line="Annuale: {am}/mese, {at} fatturati all’anno", tbl_h="Prezzi mensili e annuali", tbl_cols=("Piano","Mensile","Annuale (al mese)","Totale annuo","Prezzo mensile standard"), tbl_note="Prezzi early bird in USD. Con la fatturazione annuale risparmi il 20% rispetto al pagamento mensile."),
 "pt": dict(billed_line_m="cobrado mensalmente", billed_line_a="{at} cobrados por ano", annual_line="Anual: {am}/mês, {at} cobrados por ano", tbl_h="Preços mensais e anuais", tbl_cols=("Plano","Mensal","Anual (por mês)","Total anual","Preço mensal normal"), tbl_note="Preços early bird em USD. O plano anual economiza 20% em relação ao pagamento mensal."),
 "fr": dict(billed_line_m="facturé mensuellement", billed_line_a="{at} facturés par an", annual_line="Annuel : {am}/mois, {at} facturés par an", tbl_h="Tarifs mensuels et annuels", tbl_cols=("Forfait","Mensuel","Annuel (par mois)","Total annuel","Prix mensuel normal"), tbl_note="Tarifs early bird en USD. La facturation annuelle permet d’économiser 20 % par rapport au paiement mensuel."),
}
for _l in EXTRA: UI[_l].update(EXTRA[_l]); UI[_l].update(ANNUAL[_l])
# Q14: iletişim formu kendi doğrulamasını yapar (novalidate) — çevrili alan mesajları
V_MSG = {"tr": ("Bu alan zorunlu.", "Geçerli bir e-posta adresi girin."),
         "en": ("This field is required.", "Enter a valid email address."),
         "es": ("Este campo es obligatorio.", "Introduce un email válido."),
         "it": ("Questo campo è obbligatorio.", "Inserisci un indirizzo email valido."),
         "pt": ("Este campo é obrigatório.", "Digite um e-mail válido."),
         "fr": ("Ce champ est obligatoire.", "Saisissez une adresse e-mail valide.")}
# Q6: yatay kaydırılan tablo/kart bölgeleri için yedek etiket (önünde başlık yoksa)
TABLE_LABEL = {"tr": "Tablo", "en": "Table", "es": "Tabla", "it": "Tabella", "pt": "Tabela", "fr": "Tableau"}
GEN_ALT = {
 "gen-checkin-phone": {'tr': 'Misafirin telefonunda açık online check-in formu', 'en': 'A guest filling in the online check-in form on a phone', 'es': 'Un huésped completa el check-in online en el móvil', 'it': 'Un ospite compila il check-in online sullo smartphone', 'pt': 'Um hóspede preenchendo o check-in online no celular', 'fr': 'Un client remplit le check-in en ligne sur son téléphone'},
 "gen-owner-laptop": {'tr': 'Dizüstü bilgisayarında otel yazılımlarını karşılaştıran otel sahibi', 'en': 'A hotel owner comparing hotel software on a laptop', 'es': 'Una propietaria compara software hotelero en su portátil', 'it': 'Una titolare confronta gestionali per hotel sul portatile', 'pt': 'Uma dona de hotel comparando sistemas no notebook', 'fr': 'Une propriétaire compare des logiciels hôteliers sur son ordinateur'},
 "gen-reception": {'tr': 'Küçük bir otelin resepsiyon masası ve oda anahtarları', 'en': 'The front desk of a small hotel with room keys', 'es': 'La recepción de un hotel pequeño con las llaves de las habitaciones', 'it': 'La reception di un piccolo hotel con le chiavi delle camere', 'pt': 'A recepção de um pequeno hotel com as chaves dos quartos', 'fr': 'La réception d’un petit hôtel avec les clés des chambres'},
 "brand-phone": {'tr': "Lio'nun cevap ekranını gösteren telefonu tutan el", 'en': "Hand holding a phone showing Lio's reply screen", 'es': 'Mano sosteniendo un móvil con la pantalla de respuesta de Lio', 'it': 'Mano che tiene uno smartphone con la schermata di risposta di Lio', 'pt': 'Mão segurando um celular com a tela de resposta do Lio', 'fr': 'Main tenant un téléphone affichant l’écran de réponse de Lio'},
 "brand-guest-bed": {'tr': 'Otel odasında yatağında telefonundan mesaj yazan misafir', 'en': 'A guest in a hotel bed writing a message on a phone', 'es': 'Un huésped en la cama del hotel escribe un mensaje en el móvil', 'it': 'Un ospite a letto in hotel scrive un messaggio sullo smartphone', 'pt': 'Um hóspede na cama do hotel escrevendo uma mensagem no celular', 'fr': 'Un client allongé dans sa chambre écrit un message sur son téléphone'},
 "gen-terrace-phone": {'tr': 'Otel terasında telefonuna bakan misafir', 'en': 'A guest checking a phone on a hotel terrace', 'es': 'Un huésped mira el móvil en la terraza del hotel', 'it': 'Un ospite guarda lo smartphone sulla terrazza dell’hotel', 'pt': 'Um hóspede olhando o celular no terraço do hotel', 'fr': 'Un client consulte son téléphone sur la terrasse de l’hôtel'},
 "gen-room-dusk": {'tr': 'Akşam ışığında boş bir otel odası', 'en': 'An empty hotel room at dusk', 'es': 'Una habitación de hotel vacía al atardecer', 'it': 'Una camera d’hotel vuota al tramonto', 'pt': 'Um quarto de hotel vazio ao entardecer', 'fr': 'Une chambre d’hôtel vide au crépuscule'},
 "gen-facade": {'tr': 'Bağımsız bir otelin sokak cephesi', 'en': 'The street façade of an independent hotel', 'es': 'La fachada de un hotel independiente', 'it': 'La facciata di un hotel indipendente', 'pt': 'A fachada de um hotel independente', 'fr': 'La façade d’un hôtel indépendant'},
 "gen-arrival": {'tr': 'Valiziyle otele gelen misafir', 'en': 'A guest arriving at a hotel with a suitcase', 'es': 'Un huésped llega al hotel con su maleta', 'it': 'Un ospite arriva in hotel con la valigia', 'pt': 'Um hóspede chegando ao hotel com a mala', 'fr': 'Un client arrive à l’hôtel avec sa valise'},
 "gen-support-call": {"tr":"Dizüstü bilgisayarında görüntülü kurulum görüşmesi yaparken not alan otel işletmecisi","en":"A hotel owner taking notes during a video onboarding call on her laptop","es":"Una propietaria de hotel toma notas durante una videollamada de puesta en marcha en su portátil","it":"Una titolare di hotel prende appunti durante una videochiamata di onboarding sul portatile","pt":"Uma dona de hotel fazendo anotações durante uma videochamada de implantação no notebook","fr":"Une propriétaire d’hôtel prend des notes pendant un appel vidéo de prise en main sur son ordinateur"},
 "gen-team-desk": {"tr":"Küçük bir otelin resepsiyonunda tablete birlikte bakan resepsiyonist ve kat görevlisi","en":"A receptionist and a housekeeper checking a tablet together at a small hotel's front desk","es":"Una recepcionista y una camarera de pisos revisan juntas una tableta en la recepción de un hotel pequeño","it":"Una receptionist e una governante controllano insieme un tablet alla reception di un piccolo hotel","pt":"Uma recepcionista e uma camareira olhando juntas um tablet na recepção de um pequeno hotel","fr":"Une réceptionniste et une femme de chambre consultent ensemble une tablette à la réception d’un petit hôtel"},
 "gen-shutters": {"tr":"Gün doğarken oda panjurlarını denize bakan eski şehre açan otel işletmecisi","en":"A hotel owner opening a room's shutters at sunrise over an old town by the sea","es":"Una propietaria de hotel abre las contraventanas de una habitación al amanecer sobre un casco antiguo junto al mar","it":"Una titolare di hotel apre gli scuri di una camera all’alba sul centro storico affacciato sul mare","pt":"Uma dona de hotel abrindo as venezianas de um quarto ao nascer do sol sobre uma cidade antiga à beira-mar","fr":"Une propriétaire d’hôtel ouvre les volets d’une chambre au lever du soleil sur une vieille ville en bord de mer"},
 "gen-hostel": {"tr":"Akdeniz tarzı bir hostelin ortak alanında sohbet eden iki gezgin, arkada ranzalar","en":"Two travellers chatting in a Mediterranean-style hostel common room, bunk beds in the background","es":"Dos viajeros charlando en la zona común de un hostel mediterráneo, con literas al fondo","it":"Due viaggiatori chiacchierano nell’area comune di un ostello mediterraneo, con i letti a castello sullo sfondo","pt":"Dois viajantes conversando na área comum de um hostel mediterrâneo, com beliches ao fundo","fr":"Deux voyageurs discutent dans l’espace commun d’une auberge méditerranéenne, lits superposés en arrière-plan"},
 "gen-apart": {"tr":"Mutfaklı, deniz manzaralı aydınlık bir apart daire","en":"Bright aparthotel apartment with a kitchenette and a sea view","es":"Apartamento luminoso de apartahotel con cocina y vistas al mar","it":"Appartamento luminoso con angolo cottura e vista mare","pt":"Apartamento claro de apart-hotel com cozinha e vista para o mar","fr":"Appartement lumineux de résidence hôtelière avec kitchenette et vue sur la mer"},
 "gen-guesthouse": {"tr":"Asma altında kurulan pansiyon kahvaltısı, masayı hazırlayan ev sahibi","en":"Guesthouse breakfast under a vine pergola, the host setting the table","es":"Desayuno de hostal bajo una pérgola de parra, con la anfitriona poniendo la mesa","it":"Colazione di un B&B sotto un pergolato, con la padrona di casa che apparecchia","pt":"Café da manhã de pousada sob um caramanchão, com a anfitriã arrumando a mesa","fr":"Petit-déjeuner de chambres d’hôtes sous une treille, l’hôtesse dresse la table"},
 "gen-boutique-room": {"tr":"Taş duvarlı, panjurlu penceresi eski şehre bakan butik otel odası","en":"Boutique hotel room with a stone wall and shuttered window over the old town","es":"Habitación de hotel boutique con pared de piedra y ventana con contraventanas al casco antiguo","it":"Camera di un boutique hotel con muro in pietra e finestra con scuri sul centro storico","pt":"Quarto de hotel boutique com parede de pedra e janela com venezianas para o centro histórico","fr":"Chambre d’hôtel boutique avec mur de pierre et fenêtre à volets sur la vieille ville"},
}
def money(n, lang): return pricing.money(n, lang)   # O9: dile göre tek biçim
def annual_table(lang):
    u = UI[lang]; c = u["tbl_cols"]
    rows = "".join(f'<tr><th scope="row">{p["name"]}</th><td class="num" data-price-m="{p["id"]}">⟦price:{p["id"]}⟧</td><td class="num" data-price-am="{p["id"]}">⟦annual_mo:{p["id"]}⟧</td><td class="num" data-price-a="{p["id"]}">⟦annual:{p["id"]}⟧</td><td class="num" data-eb><s>⟦regular:{p["id"]}⟧</s></td></tr>' for p in PLANS)
    head = "".join(f"<th{' data-eb' if i == len(c) - 1 else ''}>{x}</th>" for i, x in enumerate(c))
    return (f'<div class="annual-table"><h2 id="annual-h" style="font-size:var(--t-1);margin:48px 0 16px">{u["tbl_h"]}</h2><div class="table-wrap"><table aria-labelledby="annual-h"><thead><tr>'
            + head + f'</tr></thead><tbody>{rows}</tbody></table></div><p class="small muted" style="margin-top:10px">{u["tbl_note"]}</p></div>')
UI["tr"]["lang_label"] = "Dil"; UI["en"]["lang_label"] = "Language"
UI["tr"]["crumb_label"] = "Sayfa konumu"; UI["en"]["crumb_label"] = "Breadcrumb"
def mega_html(lang):
    m = MEGA[lang]
    cols = ""
    for h, items in m["cols"]:
        lis = "".join(f'<li><a href="{url(k,lang)}"><span class="mi">{icon(ic)}</span><span><b>{t}</b><span>{d}</span></span></a></li>' for k,ic,t,d in items)
        cols += f'<div><p class="fh">{h}</p><ul>{lis}</ul></div>'
    fk, ft, fd = m["feat"]
    cols += f'<a class="feature" href="{url(fk,lang)}"><b>{ft}</b><span>{fd}</span><span class="bi" style="width:36px;height:36px;border-radius:50%;display:grid;place-items:center;background:rgba(255,255,255,.1)">{icon("arrow-up-right")}</span></a>'
    return f'<div class="mega" id="mega" hidden><div class="wrap mega-grid">{cols}</div></div>'

# ---------------------------------------------------------------- layout
def lang_menu(key, lang):
    items = "".join(
        f'<li><a href="{url(key if l in ROUTES[key] else "home", l)}" hreflang="{HREFLANG[l]}" lang="{IN_LANG[l]}"{CUR if l == lang else ""}>{LANG_NAME[l]}</a></li>'
        for l in LANGS)
    return (f'<div class="lang-wrap"><button type="button" class="lang" aria-expanded="false" aria-controls="lang-menu" aria-label="{UI[lang]["lang_label"]}: {LANG_NAME[lang]}">'
            f'{icon("globe-simple")}{lang.upper()}{icon("caret-down","caret")}</button><ul class="lang-menu" id="lang-menu" hidden>{items}</ul></div>')

# Mağaza rozetleri (8 Ekim 2026): resmî, yerelleştirilmiş rozetler src/assets/badges/ altında (Apple SVG: toolbox.marketingtools.apple.com,
# Google Play PNG: play.google.com/intl/.../badges, saydam kenar kırpıldı, 80 px yükseklik = 2x). Rozetler değiştirilmez; ikisi de 40 px yüksek.
# iOS bağlantısı bölgesiz: App Store ziyaretçiyi kendi ülke mağazasına yönlendirir. Google Play'de hl= yalnız arayüz dilini seçer.
IOS_STORE_URL = "https://apps.apple.com/app/id6765888744"
PLAY_STORE_URL = "https://play.google.com/store/apps/details?id=com.hostlio.hostliopro"
PLAY_HL = {"tr": "tr", "en": "en", "es": "es", "it": "it", "pt": "pt-BR", "fr": "fr"}
STORE_ALT = {  # rozetin üzerindeki metin = erişilebilir ad
    "tr": ("App Store'dan indirin", "Google Play'den indirin"),
    "en": ("Download on the App Store", "Get it on Google Play"),
    "es": ("Consíguelo en el App Store", "Disponible en Google Play"),
    "it": ("Scarica su App Store", "Disponibile su Google Play"),
    "pt": ("Baixar na App Store", "Disponível no Google Play"),
    "fr": ("Télécharger dans l'App Store", "Disponible sur Google Play"),
}
STORE_W = {"tr": 151, "en": 120, "es": 120, "it": 120, "pt": 120, "fr": 127}  # App Store rozeti genişliği (40 px yükseklikte)
STORE_LABEL = {"tr": "Mobil uygulamayı indirin", "en": "Download the mobile app", "es": "Descarga la app móvil",
               "it": "Scarica l'app mobile", "pt": "Baixe o app", "fr": "Télécharger l'application mobile"}
def store_badges(lang, cls=""):
    """App Store + Google Play rozetleri (aynı sekmede açılır, site geleneği: rel=noopener, target yok)."""
    a_alt, g_alt = STORE_ALT[lang]
    return (f'<div class="stores{(" " + cls) if cls else ""}" role="group" aria-label="{STORE_LABEL[lang]}">'
            f'<a href="{IOS_STORE_URL}" rel="noopener"><img src="/assets/badges/app-store-{lang}.svg" alt="{a_alt}" width="{STORE_W[lang]}" height="40" loading="lazy" decoding="async"></a>'
            f'<a href="{PLAY_STORE_URL}&amp;hl={PLAY_HL[lang]}" rel="noopener"><img src="/assets/badges/google-play-{lang}.png" alt="{g_alt}" width="135" height="40" loading="lazy" decoding="async"></a></div>')

SEC_LABEL = {"tr": "Güvenlik ve veri", "en": "Security", "es": "Seguridad", "it": "Sicurezza", "pt": "Segurança", "fr": "Sécurité"}
ABOUT_H = {"tr": ("Kurucudan", "Ekip"), "en": ("A note from the founder", "The team"), "es": ("Una nota del fundador", "El equipo"),
           "it": ("Una nota dal fondatore", "Il team"), "pt": ("Uma nota do fundador", "A equipe"), "fr": ("Le mot du fondateur", "L’équipe")}
def about_people(lang):
    h_note, h_team = ABOUT_H[lang]; out = ""
    if FOUNDER_NOTE:
        f = FOUNDER_NOTE; ph = f'<img src="{f["photo"]}" alt="{html.escape(f["name"])}" width="160" height="160" loading="lazy" style="border-radius:50%;width:96px;height:96px;object-fit:cover">' if f.get("photo") else ""
        out += (f'<section class="rule"><div class="wrap prose"><h2>{h_note}</h2>{ph}<blockquote><p>{f["text"].get(lang) or f["text"]["en"]}</p></blockquote>'
                f'<p><strong>{html.escape(f["name"])}</strong>, {html.escape(f["role"])}</p></div></section>')
    if TEAM:
        def _m(m):
            im = '<img src="%s" alt="%s" width="160" height="160" loading="lazy">' % (m["photo"], html.escape(m["name"])) if m.get("photo") else ""
            return "<li>%s<b>%s</b><span>%s</span></li>" % (im, html.escape(m["name"]), html.escape(m["role"].get(lang) or m["role"]["en"]))
        cards = "".join(_m(m) for m in TEAM)
        out += f'<section class="rule"><div class="wrap"><h2>{h_team}</h2><ul class="team">{cards}</ul></div></section>'
    return out
CUR = ' aria-current="page"'
def label_regions(body, lang):
    """Q6 (axe scrollable-region-focusable): yatay kayabilen tablo kapsayıcıları klavyeyle kaydırılabilir
    bölge olur — tabindex=0, role=region ve önündeki başlıktan (yoksa ilk sütun başlıklarından) etiket."""
    out, pos = [], 0
    for m in re.finditer(r'<div class="table-wrap"((?: style="[^"]*")?)>', body):
        out.append(body[pos:m.start()]); pos = m.end()
        nxt = body[m.end():m.end() + 400]
        lb = re.search(r'<table aria-labelledby="([^"]+)"', nxt)
        if lb:
            attr = f'aria-labelledby="{lb.group(1)}"'
        else:
            hs = re.findall(r"<h[23][^>]*>(.*?)</h[23]>", body[max(0, m.start() - 3000):m.start()], re.S)
            txt = (TABLE_LABEL[lang] + ": " + strip_tags(hs[-1])) if hs and strip_tags(hs[-1]) else ""   # bölüm başlığıyla aynı olmasın (landmark-unique)
            if not txt:
                ths = [strip_tags(x) for x in re.findall(r"<th[^>]*>(.*?)</th>", nxt, re.S)][:3]
                txt = TABLE_LABEL[lang] + (": " + ", ".join(t for t in ths if t) if ths else "")
            attr = f'aria-label="{html.escape(txt, quote=True)}"'
        out.append(f'<div class="table-wrap"{m.group(1)} tabindex="0" role="region" {attr}>')
    out.append(body[pos:])
    return "".join(out)

# S4: iç link — yazılar arasında "İlgili yazılar", ürün/segment sayfalarında "İlgili rehberler".
# Listeler öncelik sırasıdır; o dilde olmayan yazı (eski EN yazıları) atlanır, ilk 3 gösterilir.
RELATED_POSTS = {
    "post-autoreply": ["post-ai", "post-whatsapp", "post-overbooking", "post-pms"],
    "post-ai": ["post-autoreply", "post-pms", "post-whatsapp", "post-overbooking"],
    "post-overbooking": ["post-channel-manager", "post-pms-vs-cm", "post-pms", "post-autoreply", "post-noshows", "post-ai"],
    "post-pms": ["post-prices", "post-channel-manager", "post-pms-vs-cm", "post-overbooking", "post-ai", "post-autoreply"],
    "post-aifrontdesk": ["post-ai", "post-autoreply", "post-whatsapp"],
    "post-noshows": ["post-overbooking", "post-pms", "post-autoreply"],
    "post-chains": ["post-pms", "post-aifrontdesk", "post-overbooking"],
    "post-whatsapp": ["post-ai", "post-autoreply", "post-aifrontdesk", "post-pms"],
    "post-pms-vs-cm": ["post-overbooking", "post-pms", "post-prices", "post-channel-manager", "post-noshows", "post-autoreply"],
    # S9 TR rehberleri (yalnız TR; diğer dillerde liste o dilde olmayan yazıyı zaten atlar)
    "post-channel-manager": ["post-overbooking", "post-prices", "post-pms"],
    "post-kbs": ["post-pms", "post-channel-manager", "post-ai"],
    "post-prices": ["post-pms", "post-channel-manager", "post-overbooking"],
}
RELATED_PRODUCT = {"post-autoreply": "ai", "post-ai": "ai", "post-overbooking": "channel", "post-pms": "pricing",
                   "post-aifrontdesk": "ai", "post-noshows": "channel", "post-chains": "features", "post-whatsapp": "ai",
                   "post-channel-manager": "channel", "post-kbs": "checkin", "post-prices": "pricing", "post-pms-vs-cm": "channel"}
_SEG = ["post-pms", "post-autoreply", "post-overbooking"]
PAGE_GUIDES = {"channel": ["post-channel-manager", "post-pms-vs-cm", "post-overbooking", "post-pms", "post-noshows"], "ai": ["post-whatsapp", "post-autoreply", "post-ai"],
               "checkin": ["post-kbs", "post-pms", "post-ai", "post-noshows"], "pricing": ["post-prices", "post-pms", "post-overbooking", "post-autoreply"],
               "features": _SEG, "compare": ["post-prices", "post-pms", "post-overbooking", "post-autoreply"],
               "t-guesthouse": _SEG, "t-boutique": _SEG, "t-apart": _SEG, "t-hostel": _SEG,
               "kpi": ["post-pms", "post-overbooking", "post-channel-manager"], "commission": ["post-channel-manager", "post-pms-vs-cm", "post-overbooking", "post-pms"]}
# S9: "Ayrıca bakın" satırı — araçlar, karşılaştırmalar ve WhatsApp sayfasına bağlamsal iç link (o dilde olmayan atlanır)
PAGE_EXTRA = {"ai": ["whatsapp-tr", "alt-hijiffy", "roi"], "channel": ["commission", "vs-hotelrunner", "kpi"],
              "pricing": ["cmp-hub", "commission", "kpi"], "features": ["kpi", "commission", "cmp-hub"],
              "compare": ["cmp-hub", "vs-hotelrunner", "vs-elektraweb", "vs-cloudbeds", "alt-cloudbeds", "alt-amenitiz", "alt-hijiffy"],
              "t-boutique": ["kpi", "cmp-hub"], "t-guesthouse": ["kpi", "cmp-hub"], "t-apart": ["kpi", "cmp-hub"], "t-hostel": ["kpi", "cmp-hub"],
              "post-pms": ["cmp-hub", "kpi"], "post-ai": ["whatsapp-tr"], "post-autoreply": ["whatsapp-tr"], "post-whatsapp": ["alt-hijiffy"],
              "post-overbooking": ["commission"], "post-pms-vs-cm": ["commission", "cmp-hub"], "post-noshows": ["kpi"], "post-prices": ["cmp-hub", "kpi"], "post-channel-manager": ["commission"],
              "kpi": ["commission", "roi"], "commission": ["kpi", "roi"]}
SEE_ALSO = {"tr": "Ayrıca bakın", "en": "See also", "es": "Ver también", "it": "Vedi anche", "pt": "Veja também", "fr": "Voir aussi"}
def extra_label(k, lang):
    import tools_pages, compare_pages
    if k == "tools": return TOOLS_LABEL[lang]
    if k == "cmp-hub": return CMP_LABEL[lang]
    if k == "roi": return ROI_LABEL[lang]
    if k == "kpi": return tools_pages.T[lang]["kpi_crumb"]
    if k == "commission": return tools_pages.T[lang]["com_crumb"]
    if k == "whatsapp-tr": return "Otel WhatsApp asistanı"
    return compare_pages.P[k][lang]["crumb"]
def extra_html(key, lang):
    ks = [k for k in PAGE_EXTRA.get(key, []) if lang in ROUTES.get(k, {}) and k != key]
    if not ks: return ""
    return f'<p class="more">{SEE_ALSO[lang]}: ' + " · ".join(f'<a href="{url(k, lang)}">{html.escape(extra_label(k, lang))}</a>' for k in ks) + '</p>'
RELATED_H = {"tr": ("İlgili yazılar", "İlgili rehberler", "Hostlio Pro'da"), "en": ("Related articles", "Related guides", "In Hostlio Pro"),
             "es": ("Artículos relacionados", "Guías relacionadas", "En Hostlio Pro"), "it": ("Articoli correlati", "Guide correlate", "In Hostlio Pro"),
             "pt": ("Artigos relacionados", "Guias relacionados", "No Hostlio Pro"), "fr": ("Articles connexes", "Guides associés", "Dans Hostlio Pro")}
POST_INDEX = {}   # main() doldurur: {dil: {anahtar: (başlık, açıklama)}}
def related_html(key, lang):
    idx = POST_INDEX.get(lang, {})
    if key.startswith("post"): keys, h = RELATED_POSTS.get(key, []), RELATED_H[lang][0]
    elif key in PAGE_GUIDES: keys, h = PAGE_GUIDES[key], RELATED_H[lang][1]
    else: return ""
    keys = [k for k in keys if k in idx and k != key][:3]
    if not keys: return ""
    items = "".join(f'<li><a href="{url(k, lang)}">{html.escape(idx[k][0])}</a><p>{html.escape(idx[k][1])}</p></li>' for k in keys)
    more = ""
    prod = RELATED_PRODUCT.get(key)
    if prod:
        lbl = dict(UI[lang]["nav"]).get(prod) or CHECKIN_LABEL[lang]
        more = f'<p class="more">{RELATED_H[lang][2]}: <a href="{url(prod, lang)}">{lbl}</a></p>'
    return (f'<section class="rule related" aria-labelledby="rel-h"><div class="wrap"><h2 id="rel-h">{h}</h2>'
            f'<ul class="related-list">{items}</ul>{more}{extra_html(key, lang)}</div></section>')

def post_dates(page, lang, body):
    """Yazının görünen "güncelleme" tarihi ve BlogPosting.dateModified sabit UPDATED yerine sayfanın kendi
    tarihini (page_dates.json) gösterir; içerik değişen yazı (ör. S1) gerçekten güncel görünür."""
    mod = page.get("modified", UPDATED)
    for s_ in page.get("schema", []):
        if s_.get("@type") == "BlogPosting": s_["dateModified"] = mod
    mod_mod = __import__("content_" + lang)
    fmt = getattr(mod_mod, "D", None)
    def sub(m):
        return f'<time datetime="{mod}">{mod if m.group(1) == UPDATED else (fmt(mod) if fmt else fmt_date(mod, lang))}</time>'
    return re.sub(r'<time datetime="' + UPDATED + r'">([^<]*)</time>', sub, body)

NOT_FOUND = {"en": ("Page not found | Hostlio Pro", "Page not found", 'The address may have changed. <a href="{home}">Go to the home page</a>.'),
             "tr": ("Sayfa bulunamadı | Hostlio Pro", "Sayfa bulunamadı", 'Adres değişmiş olabilir. <a href="{home}">Ana sayfaya dönün</a>.')}
def layout(page, lang):
    u = UI[lang]
    key = page["key"]
    title = page["title"]
    desc = page["desc"]
    canonical = abs_url(key, lang)
    nav = "".join(
        f'<li><a href="{url(k,lang)}"{CUR if k==key or (k=="blog" and key.startswith("post")) else ""}>{n}</a></li>'
        for k, n in u["top"])
    if page.get("og_type") == "article": page = dict(page, body=post_dates(page, lang, page["body"]))
    graph = [org_schema(), website_schema(lang)]
    webpage = {"@type": "WebPage" if page.get("og_type") != "article" else "WebPage", "@id": canonical + "#webpage",
               "url": canonical, "name": title, "description": desc,
               "inLanguage": IN_LANG[lang], "isPartOf": {"@id": SITE + "/#website"},
               "dateModified": page.get("modified", UPDATED)}
    if page.get("page_type"): webpage["@type"] = page["page_type"]
    graph.append(webpage)
    trail = page.get("trail")
    if trail:
        full = [(u["home"], url("home", lang))] + trail
        graph.append(crumbs_schema(full))
    if page.get("faq"):
        if webpage["@type"] == "FAQPage": webpage["mainEntity"] = faq_schema(page["faq"])["mainEntity"]
        else: graph.append(faq_schema(page["faq"]))
    for s in page.get("schema", []): graph.append(s)
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=None)
    og_img = SITE + "/assets/og-" + lang + ".png"
    locale = LOCALE[lang]
    alt_locales = "".join(f'<meta property="og:locale:alternate" content="{LOCALE[l]}">' for l in langs(key) if l != lang)
    crumbs = crumbs_html([(u["home"], url("home", lang))] + trail, lang) if trail else ""
    body = page["body"]
    if "data-contact-form" in body:
        body = body.replace("data-contact-form", f'data-contact-form data-endpoint="{FORM_ENDPOINT}" data-lang="{lang}" data-ok="{html.escape(u["form_ok"])}" data-err="{html.escape(u["form_err"])}" data-sending="{html.escape(u["sending"])}" data-v-req="{html.escape(V_MSG[lang][0])}" data-v-email="{html.escape(V_MSG[lang][1])}" novalidate', 1)
        body = body.replace('</div>\n<form class="contact"', f'<p><a href="https://wa.me/{WHATSAPP}" rel="noopener">WhatsApp: {WHATSAPP_TXT}</a></p><p class="small muted">{u["resp"]}</p></div>\n<form class="contact"', 1)
        body = contact_form_extras(body, lang)
    if '<div class="plans">' in body:
        toggle = (f'<div class="billing" role="group" aria-label="{u["bill_m"]} / {u["bill_a"]}"><button type="button" class="on" aria-pressed="true" data-bill="m">{u["bill_m"]}</button>'
                  f'<button type="button" aria-pressed="false" data-bill="a">{u["bill_a"]} <span class="save">{u["save"]}</span></button></div>')
        body = body.replace('<div class="plans">', toggle + '<div class="plans" data-plans>')
        for p_ in PLANS:
            # K2: monthly shows only "billed monthly"; annual shows only "$470 billed yearly" (JS swaps them)
            ya = u["billed_line_a"].format(at=f'<span data-at="{p_["id"]}">⟦annual:{p_["id"]}⟧</span>')
            line = f'<span data-bm>{u["billed_line_m"]}</span><span data-ba hidden>{ya}</span>'
            body = re.sub(r'(<h3 id="plan-' + p_["id"] + r'">.*?<div class="price num">.*?</div>)', lambda m: m.group(1) + f'<p class="billed-line num">{line}</p>', body, count=1, flags=re.S)
        if key == "pricing":
            i = body.find('<div class="plans"'); j = body.find('</article></div>', i)
            if j > 0: body = body[:j + 16] + annual_table(lang) + body[j + 16:]
    if key == "about" and (FOUNDER_NOTE or TEAM):
        body += about_people(lang)
    if page.get("faq") and not page.get("faq_inline"):
        body += faq_block(page["faq"], lang)
    body += related_html(key, lang)
    body = label_regions(body, lang)
    upd = u["updated"]
    if key != "home" and not page.get("no_updated"):
        body += f'<p class="wrap small muted updated">{upd}: <time datetime="{page.get("modified", UPDATED)}">{page.get("updated_txt", UPDATED_TXT[lang])}</time></p>'
    if not page.get("no_final"):
        body += final_cta(lang)
    head_extra = ""
    if page.get("preload_img"):
        head_extra += f'<link rel="preload" as="image" href="{page["preload_img"]}" fetchpriority="high">\n'
    if GSC_VERIFY: head_extra += f'<meta name="google-site-verification" content="{GSC_VERIFY}">\n'
    if BING_VERIFY: head_extra += f'<meta name="msvalidate.01" content="{BING_VERIFY}">\n'
    head_extra += analytics_head()
    year = datetime.date.fromisoformat(UPDATED).year
    cmp_li = f'<li><a href="{url("cmp-hub", lang)}">{CMP_LABEL[lang]}</a></li>\n' if lang in ROUTES["cmp-hub"] else ""
    for _n, _a in GEN_ALT.items():
        body = re.sub(r'(<img src="/assets/img/' + _n + r'\.webp" alt=")[^"]*"', lambda m: m.group(1) + html.escape(_a[lang]) + '"', body)
    doc = f'''<!doctype html>
<html class="nojs" lang="{"pt-BR" if lang=="pt" else lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{canonical}">
{"".join(f'<link rel="alternate" hreflang="{HREFLANG[l]}" href="{abs_url(key,l)}">' + chr(10) for l in langs(key))}<link rel="alternate" hreflang="x-default" href="{abs_url(key,xdefault(key))}">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta property="og:type" content="{page.get("og_type","website")}">
<meta property="og:site_name" content="Hostlio Pro">
<meta property="og:locale" content="{locale}">{alt_locales}
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{og_img}">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#1B2B4B">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
{font_preloads(lang, body)}<link rel="stylesheet" href="{asset('/assets/style.css')}">
{head_extra}<script type="application/ld+json">{ld}</script>
</head>
<body>
<a class="skip" href="#main">{u["skip"]}</a>
<header class="site-header"><div class="wrap nav">
<a class="brand" href="{url("home",lang)}" aria-label="Hostlio Pro">{LOGO}<span>Hostlio <span class="pro">Pro</span></span></a>
<ul class="nav-links" id="nav-links">
<li><button type="button" class="mega-btn" aria-expanded="false" aria-controls="mega">{MEGA[lang]["btn"]}{icon("caret-down","caret")}</button>{mega_html(lang)}</li>
{nav}
<li class="nav-login"><a href="{LOGIN_URL}">{u["login"]}{icon("arrow-up-right")}</a></li>
</ul>
<div class="nav-end">
{lang_menu(key, lang)}
<a class="login" href="{LOGIN_URL}">{u["login"]}</a>
{btn(u["trial"], SIGNUP_URL)}
<button type="button" class="menu-toggle" aria-expanded="false" aria-controls="nav-links" aria-label="{u["menu"]}" data-open="{u["menu"]}" data-close="{MENU_CLOSE[lang]}"><span></span></button>
</div></div></header>
<main id="main">
{crumbs}
{body}
</main>
<footer class="site-footer"><div class="wrap">
<div class="foot-grid">
<div><a class="brand" href="{url("home",lang)}">{LOGO}<span>Hostlio <span class="pro">Pro</span></span></a><p class="muted small" style="margin-top:12px">{u["foot_tag"]}</p><p class="small"><a href="mailto:{EMAIL}">{EMAIL}</a><br><a href="https://wa.me/{WHATSAPP}" rel="noopener">WhatsApp {WHATSAPP_TXT}</a></p>{store_badges(lang, "foot-stores")}</div>
<div><p class="fh">{u["foot_product"]}</p><ul>
<li><a href="{url("features",lang)}">{dict(u["nav"])["features"]}</a></li>
<li><a href="{url("ai",lang)}">{dict(u["nav"])["ai"]}</a></li>
<li><a href="{url("channel",lang)}">{dict(u["nav"])["channel"]}</a></li>
<li><a href="{url("checkin",lang)}">{CHECKIN_LABEL[lang]}</a></li>
<li><a href="{url("pricing",lang)}">{dict(u["nav"])["pricing"]}</a></li></ul></div>
<div><p class="fh">{u["foot_sol"]}</p><ul>
<li><a href="{url("t-boutique",lang)}">{u["sol"][0]}</a></li>
<li><a href="{url("t-guesthouse",lang)}">{u["sol"][1]}</a></li>
<li><a href="{url("t-apart",lang)}">{u["sol"][2]}</a></li>
<li><a href="{url("t-hostel",lang)}">{u["sol"][3]}</a></li>
<li><a href="{url("compare",lang)}">{u["sol"][4]}</a></li></ul></div>
<div><p class="fh">{u["foot_res"]}</p><ul>
<li><a href="{url("blog",lang)}">Blog</a></li>
<li><a href="{url("faq",lang)}">{u["foot_faq"]}</a></li>
<li><a href="{url("roi",lang)}">{ROI_LABEL[lang]}</a></li>
<li><a href="{url("tools",lang)}">{TOOLS_LABEL[lang]}</a></li>
{cmp_li}<li><a href="/llms.txt">llms.txt</a></li></ul></div>
<div><p class="fh">{u["foot_company"]}</p><ul>
<li><a href="{url("about",lang)}">{u["foot_about"]}</a></li>
<li><a href="{url("contact",lang)}">{u["foot_contact"]}</a></li>
<li><a href="{url("security",lang)}">{SEC_LABEL[lang]}</a></li>
<li><a href="{LOGIN_URL}">{FOOT_LOGIN[lang]}</a></li></ul></div>
</div>
<div class="foot-bottom"><span>© {year} Hostlio Pro, Loti Members LLC. {u["rights"]}</span><span class="legal"><a href="{url("privacy",lang)}">{u["privacy"]}</a><a href="{url("terms",lang)}">{u["terms"]}</a><a href="{url("delacc",lang)}">{u["delacc"]}</a><a href="{url("dpa","en")}" hreflang="en">DPA</a>{consent_foot(lang)}</span><span>2108 N ST STE N, Sacramento, CA 95816</span></div>
</div></footer>
{pricing_block(lang) if needs_prices(body) else ""}<script src="{asset('/assets/site.js')}" defer></script>
{"".join(f'<script src="{asset(x)}" defer></script>' + chr(10) for x in page.get("scripts", []))}
<script src="{asset('/attribution.js')}" defer></script>
</body>
</html>'''
    return finish(doc, lang)

_LATIN_EXT = re.compile(r"[\u0100-\u0130\u0132-\u0151\u0154-\u02BA]")
def font_preloads(lang, body=None):
    """D7: Türkçe sayfalarda ğ/ş/İ latin-ext dosyasında ⇒ o dosya da önceden yüklenir.
    Q4 (CLS): H1'de italik vurgu (em.hl) varsa italik dosya da önceden yüklenir; yoksa italik metin
    geç gelir ve başlık yeniden sarılıp hero'yu aşağı iter. latin-ext italik yalnız vurgu metni gerektiriyorsa."""
    files = ["instrument-sans-latin-wght-normal.woff2"] + (["instrument-sans-latin-ext-wght-normal.woff2"] if lang == "tr" else [])
    h1 = re.search(r"<h1[^>]*>(.*?)</h1>", body or "", re.S)
    if h1:
        ems = re.findall(r'<em class="hl">(.*?)</em>', h1.group(1), re.S)
        if ems:
            files.append("instrument-sans-latin-wght-italic.woff2")
            if any(_LATIN_EXT.search(html.unescape(e)) for e in ems):
                files.append("instrument-sans-latin-ext-wght-italic.woff2")
    return "".join(f'<link rel="preload" href="/assets/fonts/{f}" as="font" type="font/woff2" crossorigin>\n' for f in files)

def analytics_head():
    """Ölçüm betikleri (boşken hiçbir şey basılmaz). Satır içi betik yok (O4).
    GA4 (8 Eki 2026): yalnız /assets/consent.js basılır — senkron, <head>'de; Consent Mode v2 varsayılanlarını
    (dördü de denied) kurar, izin bandını gösterir ve gtag.js'i YALNIZ "Kabul et"ten sonra yükler.
    Olay adları README "Analitik (GA4)" bölümünde."""
    out = ""
    if PLAUSIBLE_DOMAIN: out += f'<script defer data-domain="{PLAUSIBLE_DOMAIN}" src="https://plausible.io/js/script.js"></script>\n'
    if GA4_ID:
        priv = html.escape(json.dumps({l: url("privacy", l) for l in LANGS}, separators=(",", ":")))
        out += f'<script src="{asset("/assets/consent.js")}" data-ga="{GA4_ID}" data-privacy="{priv}"></script>\n'
    return out

def consent_foot(lang, cls="linkbtn"):
    """Altbilgide "Çerez tercihleri" düğmesi — yalnız GA4_ID doluyken."""
    return analytics_consent.foot_button(lang, cls) if GA4_ID else ""

CONTACT_PRIVACY = {
    "en": 'We use your details only to reply to your request. See our <a href="{p}">Privacy Policy</a>.',
    "tr": 'Bilgilerinizi yalnızca talebinize yanıt vermek için kullanırız. Ayrıntılar: <a href="{p}">Gizlilik Politikası</a>.',
    "es": 'Usamos tus datos solo para responder a tu solicitud. Más información en la <a href="{p}">Política de privacidad</a>.',
    "it": 'Usiamo i tuoi dati solo per rispondere alla tua richiesta. Dettagli nell’<a href="{p}">Informativa sulla privacy</a>.',
    "pt": 'Usamos seus dados apenas para responder à sua solicitação. Saiba mais na <a href="{p}">Política de privacidade</a>.',
    "fr": 'Nous utilisons vos données uniquement pour répondre à votre demande. Voir notre <a href="{p}">Politique de confidentialité</a>.',
}
HONEYPOT = {"en": "Leave this field empty", "tr": "Bu alanı boş bırakın", "es": "Deja este campo vacío", "it": "Lascia vuoto questo campo",
            "pt": "Deixe este campo em branco", "fr": "Laissez ce champ vide"}

def contact_form_extras(body, lang):
    """D9: iletişim formu — toplama noktasında gizlilik bilgilendirmesi, bal küpü (honeypot) alanı ve
    JS'siz yedek. JS yokken form artık Make webhook'una çıplak POST atmıyor (kullanıcı "Accepted"
    sayfasına düşüyordu); e-posta uygulamasını açan mailto: yedeğine gidiyor. JS'li gönderim
    site.js'te (fetch → Make; bal küpü doluysa ya da 3 sn'den hızlı gönderildiyse gönderilmez)."""
    subj = re.search(r'data-subject="([^"]*)"', body)
    subj = subj.group(1) if subj else "Demo request"
    body = body.replace(f' action="{FORM_ENDPOINT}" method="post"',
                        f' action="mailto:{EMAIL}?subject={html.escape(subj)}" method="post" enctype="text/plain"', 1)
    hp = (f'<div class="hp" aria-hidden="true"><label>{HONEYPOT[lang]}<input name="website" tabindex="-1" autocomplete="off"></label></div>\n'
          f'<p class="small muted form-privacy">{CONTACT_PRIVACY[lang].format(p=url("privacy", lang))}</p>\n')
    i = body.find("<form class=\"contact\"")
    j = body.find('<button class="btn btn-primary" type="submit">', i)
    return body[:j] + hp + body[j:] if i > -1 and j > -1 else body

def needs_prices(body):
    return 'data-plans' in body or 'data-price' in body or 'id="roi-form"' in body

def pricing_block(lang):
    """Y2: tarayıcı tarafı fiyat yapılandırması (pricing.py → prices.js). Satır içi JSON veri bloğu
    çalıştırılmaz, dolayısıyla CSP script-src 'self' ile uyumludur."""
    cfg = json.dumps(pricing.js_config(lang, PLANS_ENDPOINT, PLANS_ANON), ensure_ascii=False).replace("</", "<\\/")
    return (f'<script type="application/json" id="hostlio-pricing">{cfg}</script>\n'
            '<script src="' + asset('/assets/prices.js') + '" defer></script>\n')

def signup_url(lang):
    """O3: kayıt sayfasının yönlendirmesiz, dile özgü son adresi."""
    return f"/{lang}/signup/"

def finish(doc, lang):
    """Son geçiş: ⟦fiyat⟧ yer tutucularını dile göre doldur (Y2/O9) ve /signup bağlantılarını
    doğrudan /xx/signup/ adresine çevir (O3: 308 zinciri yok)."""
    doc = re.sub(r'((?:href|action)=")/signup/?(?=[?"])', lambda m: m.group(1) + signup_url(lang), doc)
    return pricing.fill(doc, lang)

# ---------------------------------------------------------------- responsive images
def make_variants():
    """Create 480w copies of every content image for srcset (skipped if Pillow is missing; variants are committed)."""
    try:
        from PIL import Image
    except ImportError:
        import shutil as _sh; _sh.copytree(ROOT / "src/assets/img", DIST / "assets/img", dirs_exist_ok=True); return
    src = ROOT / "src/assets/img"
    for f in src.glob("*.webp"):
        if f.stem.endswith("-480"): continue
        out = src / f"{f.stem}-480.webp"
        if out.exists() and out.stat().st_mtime >= f.stat().st_mtime: continue
        im = Image.open(f)
        if im.width <= 520: continue
        h = round(im.height * 480 / im.width)
        im.resize((480, h), Image.LANCZOS).save(out, "WEBP", quality=60, method=6)
    import shutil as _sh
    _sh.copytree(src, DIST / "assets/img", dirs_exist_ok=True)

IMG_SIZES = "(max-width: 640px) 92vw, (max-width: 1100px) 50vw, 600px"

@functools.lru_cache(None)
def webp_width(path):
    """WebP dosyasının gerçek piksel genişliği (srcset 'w' tanımlayıcısı bunu ister; Pillow gerekmez)."""
    b = Path(path).read_bytes()[:30]
    fmt = b[12:16]
    if fmt == b"VP8 ": return int.from_bytes(b[26:28], "little") & 0x3FFF
    if fmt == b"VP8L": return (int.from_bytes(b[21:23], "little") & 0x3FFF) + 1
    if fmt == b"VP8X": return int.from_bytes(b[24:27], "little") + 1
    return None

def srcset_for(name):
    if not (ROOT / f"src/assets/img/{name}-480.webp").exists(): return None
    w = webp_width(ROOT / f"src/assets/img/{name}.webp") or 880
    return f"/assets/img/{name}-480.webp 480w, /assets/img/{name}.webp {w}w"

def add_srcset(doc):
    import re as _re
    def rep(m):
        tag, name = m.group(0), m.group(1)
        ss = srcset_for(name)
        if "srcset=" in tag or not ss: return tag
        return tag.replace(f'src="/assets/img/{name}.webp"', f'src="/assets/img/{name}.webp" srcset="{ss}" sizes="{IMG_SIZES}"', 1)
    def pre(m):
        # O7: preload, <img> ile AYNI srcset/sizes'ı taşır ⇒ mobil tek dosya indirir
        ss = srcset_for(m.group(1))
        return m.group(0) if not ss else m.group(0).replace(' fetchpriority=', f' imagesrcset="{ss}" imagesizes="{IMG_SIZES}" fetchpriority=', 1)
    doc = _re.sub(r'<link rel="preload" as="image" href="/assets/img/([\w-]+)\.webp" fetchpriority="high">', pre, doc)
    return _re.sub(r'<img [^>]*src="/assets/img/([\w-]+)\.webp"[^>]*>', rep, doc)

# ---------------------------------------------------------------- build
def write(path, content):
    p = DIST / path.lstrip("/")
    if path.endswith("/"): p = p / "index.html"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")

# Y3: yedek yol YALNIZ python3 hiç yoksa devreye girer. python3 varsa build.py ya da check.py'nin
# her hatası deploy'u düşürür (eskiden `python3 build.py || test -f dist/en/index.html` yarım
# kalmış bir build'i başarılı sayabiliyordu).
BUILD_COMMAND = ('if command -v python3 >/dev/null 2>&1; then python3 build.py && python3 scripts/check.py; '
                 'else echo "python3 yok, depodaki dist kullanılıyor" && test -f dist/en/index.html && test -f dist/sitemap.xml; fi')

def csp():
    """O4: Content-Security-Policy — yalnız gerçekten kullanılan kökenler. Satır içi betik ve on*
    özniteliği yok (scripts/check.py bunu denetler), bu yüzden script-src 'self' zorunlu modda.
    style-src 'unsafe-inline': şablonlardaki style="" öznitelikleri için (betik çalıştırmaz)."""
    supa = PLANS_ENDPOINT.split("/functions/")[0]           # plans + signup-checkout
    make = "/".join(FORM_ENDPOINT.split("/")[:3])           # iletişim formu (fetch)
    script, connect = ["'self'"], ["'self'", supa, make]
    if PLAUSIBLE_DOMAIN: script.append("https://plausible.io"); connect.append("https://plausible.io")
    img = ["'self'", "data:"]
    if GA4_ID:   # Google'ın GA4 için belgelediği kökenler (developers.google.com/tag-platform/security/guides/csp)
        ga = ["https://*.google-analytics.com", "https://*.analytics.google.com", "https://*.googletagmanager.com"]
        script.append("https://*.googletagmanager.com"); connect += ga; img += ga
    return "; ".join([
        "default-src 'self'", "script-src " + " ".join(script), "style-src 'self' 'unsafe-inline'",
        "img-src " + " ".join(img),
        "font-src 'self'", "media-src 'self'", "connect-src " + " ".join(connect),
        "form-action 'self' mailto:", "frame-ancestors 'self'", "base-uri 'self'", "object-src 'none'",
        "upgrade-insecure-requests"])

# ---------------------------------------------------------------- D4: sayfa başına tarih
# Her sayfanın dateModified / "Son güncelleme" / sitemap lastmod değeri kendi içeriğinin özetinden
# gelir: page_dates.json (depoda) {url: {"h": özet, "d": tarih}}. İçerik değişmediyse tarih korunur,
# değiştiyse build günü yazılır. Böylece global UPDATED değişince 149 sayfa birden "güncellenmiş" görünmez.
DATES_FILE = ROOT / "page_dates.json"
MONTHS = {
    "en": "January February March April May June July August September October November December".split(),
    "tr": "Ocak Şubat Mart Nisan Mayıs Haziran Temmuz Ağustos Eylül Ekim Kasım Aralık".split(),
    "es": "enero febrero marzo abril mayo junio julio agosto septiembre octubre noviembre diciembre".split(),
    "it": "gennaio febbraio marzo aprile maggio giugno luglio agosto settembre ottobre novembre dicembre".split(),
    "pt": "janeiro fevereiro março abril maio junho julho agosto setembro outubro novembro dezembro".split(),
    "fr": "janvier février mars avril mai juin juillet août septembre octobre novembre décembre".split(),
}
def fmt_date(iso, lang):
    d = datetime.date.fromisoformat(iso); m = MONTHS[lang][d.month - 1]
    return {"en": f"{m.capitalize()} {d.day}, {d.year}", "es": f"{d.day} de {m} de {d.year}", "pt": f"{d.day} de {m} de {d.year}"}.get(lang, f"{d.day} {m} {d.year}")

def content_hash(p, lang):
    """Sayfanın kendi içeriği (başlık, açıklama, gövde, SSS); kayıt bağlantısı biçimi normalize edilir."""
    raw = json.dumps([p.get("title"), p.get("desc"), p.get("body"), p.get("faq")], ensure_ascii=False, sort_keys=True)
    raw = re.sub(r"/signup/?", "/signup", pricing.fill(raw, lang))
    return _hashlib.md5(raw.encode("utf-8")).hexdigest()[:12]

def assign_dates(pages, today=None):
    today = today or datetime.date.today().isoformat()
    try: old = json.loads(DATES_FILE.read_text())
    except (OSError, ValueError): old = {}
    new = {}
    for lang, plist in pages.items():
        for p in plist:
            u, h = url(p["key"], lang), content_hash(p, lang)
            d = old[u]["d"] if u in old and old[u]["h"] == h else today
            new[u] = {"h": h, "d": d}
            if "modified" not in p: p["modified"] = d; p["updated_txt"] = fmt_date(d, lang)
    DATES_FILE.write_text(json.dumps(new, ensure_ascii=False, indent=0, sort_keys=True) + "\n", encoding="utf-8")
    return {u: v["d"] for u, v in new.items()}

def lang_redirects():
    """K4/O2: kök dil yönlendirmesi + eski Türkçe ve kök İngilizce adreslerden 301."""
    r = []
    def both(src, dst, perm=True):
        base = src.rstrip("/")
        for s_ in ([base, base + "/"] if base else ["/"]):
            r.append({"source": s_, "destination": dst, "permanent": perm})
    # "/" — tarayıcı diline göre (geçici yönlendirme, dile göre değiştiği için). Varsayılan İngilizce.
    for l in ["tr", "es", "it", "pt", "fr"]:
        r.append({"source": "/", "has": [{"type": "header", "key": "accept-language", "value": f"^{l}([-_,;].*)?$"}],
                  "destination": url("home", l), "permanent": False})
    r.append({"source": "/", "destination": url("home", "en"), "permanent": False})
    for k, old in OLD_TR.items():
        if old != "/": both(old, url(k, "tr"))
    for k, old in OLD_EN_ROOT.items():
        both(old, url(k, "en"))
    # O1: /es/pricing/ gibi İngilizce adres tahminleri yerelleştirilmiş sayfaya gitsin
    for l in ["tr", "es", "it", "pt", "fr"]:
        for k, slug in [("pricing", "pricing"), ("faq", "faq"), ("features", "features"), ("contact", "contact"), ("about", "about"), ("security", "security")]:
            if url(k, l) != f"/{l}/{slug}/": both(f"/{l}/{slug}", url(k, l))
    # O3: kayıt sayfası her dilde kendi adresinde (/xx/signup/); /signup/ dil algılayan giriş noktası
    # (Stripe dönüşü ve eski bağlantılar). D1: cleanUrls kapalı ⇒ eski .html adresleri açıkça yönlenir.
    for old, new in [("/signup.html", "/signup/"), ("/index.html", "/"), ("/privacy.html", url("privacy", "en")),
                     ("/terms.html", url("terms", "en")), ("/blog/index.html", url("blog", "en"))]:
        r.append({"source": old, "destination": new, "permanent": True})
    return r

def main():
    import importlib
    if DIST.exists(): shutil.rmtree(DIST)
    shutil.copytree(ROOT / "src", DIST)
    # root vercel.json (used when the repo itself is deployed on Vercel): same headers/redirects + build settings
    vc = json.loads((ROOT / "src/vercel.json").read_text())
    vc["redirects"] = vc.get("redirects", []) + lang_redirects()
    for h in vc["headers"]:
        if h["source"] == "/(.*)": h["headers"].append({"key": "Content-Security-Policy", "value": csp()})
    (DIST / "vercel.json").write_text(json.dumps(vc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    vc = {"buildCommand": BUILD_COMMAND, "outputDirectory": "dist", **vc}
    (ROOT / "vercel.json").write_text(json.dumps(vc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    import tools_pages, compare_pages, guides_tr, sys as _sys_
    _B = _sys_.modules[__name__]
    import guides_intl
    pages = {l: importlib.import_module("content_" + l).pages() + tools_pages.pages(l, _B) + compare_pages.pages(l, _B) + guides_intl.pages(l, url)
                + (guides_tr.pages(_B) if l == "tr" else []) for l in LANGS}
    if GA4_ID:   # GA4 açıkken gizlilik politikasının çerez bölümüne analitik paragrafı (analytics_consent.py)
        for l, plist in pages.items():
            for p in plist:
                if p["key"] == "privacy": p["body"] = analytics_consent.privacy_patch(p["body"], l)
    page_dates = assign_dates(pages)
    for lang, plist in pages.items():
        POST_INDEX[lang] = {p["key"]: (pricing.fill(p["title"], lang), pricing.fill(p["desc"], lang)) for p in plist if p["key"].startswith("post")}
    make_variants()
    for lang, plist in pages.items():
        for p in plist:
            write(url(p["key"], lang), add_srcset(layout(p, lang)))
    # llms-full.txt: plain-text version of every page for AI systems
    import re as _re
    full = ["# Hostlio Pro full content", f"Last updated: {UPDATED}", ""]
    for lang, plist in pages.items():
        for p in plist:
            txt = _re.sub(r"<(script|style|svg)[^>]*>.*?</\1>", " ", p["body"], flags=_re.S)
            txt = _re.sub(r"<(h[1-3])[^>]*>", "\n## ", txt)
            txt = _re.sub(r"<li[^>]*>", "\n- ", txt)
            txt = _re.sub(r"</(p|div|h[1-3]|section|tr|details)>", "\n", txt)
            txt = html.unescape(_re.sub(r"<[^>]+>", " ", txt))
            txt = "\n".join(_re.sub(r"[ \t]+", " ", l).strip() for l in txt.splitlines())
            txt = _re.sub(r"\n{3,}", "\n\n", txt).strip()
            full.append(pricing.fill(f"---\n# {p['title']}\nURL: {abs_url(p['key'], lang)}\n\n{txt}\n", lang))
            for q, a in p.get("faq", []): full.append(pricing.fill(f"Q: {q}\nA: {strip_tags(a)}\n", lang))
    (DIST / "llms-full.txt").write_text("\n".join(full), encoding="utf-8")
    if INDEXNOW_KEY: (DIST / f"{INDEXNOW_KEY}.txt").write_text(INDEXNOW_KEY, encoding="utf-8")
    # sitemap with hreflang alternates
    items = []
    lastmod = {SITE + u: page_dates[u] for u in page_dates}
    for lang, plist in pages.items():   # açık "modified" taşıyan sayfalar (hukuki metinler) kendi tarihleriyle
        for p in plist: lastmod[abs_url(p["key"], lang)] = p.get("modified", lastmod.get(abs_url(p["key"], lang)))
    for key in ROUTES:
        for lang in langs(key):
            alts = "".join(f'<xhtml:link rel="alternate" hreflang="{HREFLANG[l]}" href="{abs_url(key,l)}"/>' for l in langs(key))
            alts += f'<xhtml:link rel="alternate" hreflang="x-default" href="{abs_url(key,xdefault(key))}"/>'
            items.append(f'<url><loc>{abs_url(key,lang)}</loc><lastmod>{lastmod.get(abs_url(key,lang), UPDATED)}</lastmod>{alts}</url>')
    (DIST / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
        + "\n".join(items) + "\n</urlset>\n", encoding="utf-8")
    # llms.txt (GEO: plain-language index for AI answer engines)
    bykey = {l: {p["key"]: p for p in pages[l]} for l in LANGS}
    SEC = {"en": "English pages", "tr": "Türkçe sayfalar", "es": "Páginas en español", "it": "Pagine in italiano", "pt": "Páginas em português", "fr": "Pages en français"}
    def line(k, lang, src): return pricing.fill(f'- [{src[k]["title"].split(" | ")[0]}]({abs_url(k,lang)}): {src[k]["desc"]}', lang)
    llms = f"""# Hostlio Pro

> Hostlio Pro (also called "Hostlio") is AI-powered hotel management software (PMS) for independent hotels, boutique hotels, guesthouses, aparthotels and hostels with roughly 1–150 rooms. It combines Lio, an AI guest-messaging assistant that replies 24/7 in 30+ languages on WhatsApp and OTA inboxes (Booking.com, Airbnb, Expedia), a channel manager with certified connections to 100+ OTAs, a drag-and-drop room rack calendar, online check-in with on-device ID document scanning (no document images stored) and digital signature, an accommodation confirmation letter for visa applications (PDF), transfer and tour sales, and a mobile app for iOS and Android. Operated by Loti Members LLC (Sacramento, CA, USA). Used by independent hotels in 20+ countries.

## Key facts
- Pricing (USD/month, early-bird for first 50 customers, locked in while subscribed): Starter ⟦price:starter⟧ (regular ⟦regular:starter⟧), Pro ⟦price:pro⟧ (regular ⟦regular:pro⟧), Growth ⟦price:growth⟧ (regular ⟦regular:growth⟧).
- Starter: 1 property, up to 10 rooms, 3 users, ⟦quota:starter⟧ AI messages/month, 100+ OTA sync, WhatsApp AI messaging, Lio Suggestions, room rack, visa accommodation confirmation (PDF), iOS and Android mobile app (the app is included in every plan).
- Pro: 1 property, up to 50 rooms, 8 users, ⟦quota:pro⟧ AI messages/month, adds OTA inbox messaging (Booking.com, Airbnb, Expedia), booking and extra-service requests via Lio on WhatsApp, AI insights from reviews and guest messages, optional weekly AI summary, online check-in, transfer & tour sales.
- Online check-in (Pro and Growth): the guest scans the machine-readable zone (MRZ) of a passport or ID card with their own phone; reading happens entirely in the browser and only the extracted fields (name, document number or Turkish T.C. identity number, nationality, date of birth, expiry date) and the digital signature are saved. No ID or passport images are uploaded or stored, in line with KVKK principle decision 2025/2120. Staff can scan at the desk with the mobile app (on-device Google ML Kit text recognition). Documents without an MRZ are entered manually.
- Growth: up to 2 properties, 150 rooms, 20 users, ⟦quota:growth⟧ AI messages/month, weekly AI summary, priority sync, priority support, onboarding call, white-label.
- Free trial: 7 days; a payment card is collected at signup, no charge until the trial ends, cancel anytime.
- Annual billing: 20% off — Starter ⟦annual_mo:starter⟧/mo (⟦annual:starter⟧/year), Pro ⟦annual_mo:pro⟧/mo (⟦annual:pro⟧/year), Growth ⟦annual_mo:growth⟧/mo (⟦annual:growth⟧/year), early-bird.
- Setup: the account is ready in minutes; channels are usually connected the same day (add rooms, authorise the connection in each OTA extranet, map rooms).
- Starter syncs OTA reservations but does not reply to OTA guest messages; OTA inbox messaging starts from Pro.
- Lio Suggestions (all plans): every morning Lio suggests actions on pricing, operations (e.g. rooms waiting to be cleaned, pending requests), setup gaps and revenue opportunities. Nothing changes without the hotelier's approval; rate changes stay within limits the hotelier sets.
- Booking requests (Pro and Growth): on WhatsApp Lio collects dates, guests and room preference and quotes a price from the hotel's own rates and availability; the request becomes a reservation only after the hotelier approves it. Lio does not confirm bookings on its own.
- Also available on all plans (web dashboard): Today screen (arrivals, departures, rooms to clean, pending messages and drafts); analytics (occupancy, ADR, RevPAR, revenue, cancellations/no-shows, 30/60/90-day forward view with pickup, channel gross/commission/net) with Excel export, PDF print and weekly/monthly email reports; staff roles and permissions (6 roles: owner, manager, front desk, housekeeping, accounting, viewer; users 3/8/20 by plan) and a field-level activity log (365 days, CSV); housekeeping statuses and printable list; maintenance reports with photos, where taking a room out of order lowers OTA availability automatically; rate grid with min/max stay, CTA, CTD, stop sell, date-range bulk edit and weekend pricing; reservation import from CSV/Excel; notification center (90 days).
- Pro and Growth: optional automatic email with the guest's check-in link, per booking source. Growth: 'All properties' overview, property switcher, settings copied to the second property, shared AI quota.
- Not offered: bed-level (dorm) inventory, direct submission to government guest registers (KBS, SES.Hospedajes, Alloggiati).
- Channels include Booking.com, Airbnb, Expedia, Agoda, Trip.com, Hotels.com, Hotelbeds, Hostelworld, Google Hotels.
- Languages: website in English, Turkish, Spanish, Italian, Portuguese and French; dashboard, mobile app and guest check-in form in the same 6 languages; support in English and Turkish; guest replies in 30+ languages.
- Contact: {EMAIL}, WhatsApp {WHATSAPP_TXT}
- Last updated: {UPDATED}

""" + "\n\n".join(f"## {SEC[l]}\n" + "\n".join(line(k, l, bykey[l]) for k in ROUTES if l in ROUTES[k]) for l in ["en","tr","es","it","pt","fr"]) + "\n"
    (DIST / "llms.txt").write_text(pricing.fill(llms, "en"), encoding="utf-8")
    # ödeme/kayıt sayfası — kendi odaklı düzeniyle (signup_page.py)
    import signup_page, sys as _sys
    write("/signup/", signup_page.render(_sys.modules[__name__]))
    for l in LANGS:
        write(signup_url(l), signup_page.render(_sys.modules[__name__], l))
    # 404
    # Q13/D6: Vercel bulunmayan her adreste /404.html'i 404 koduyla döner; dile göre ayrı dosya
    # verilemez. Bu yüzden 404 sayfası 6 dilin metnini taşır, site.js adresin dil önekine (yoksa
    # tarayıcı diline) göre doğru bloğu gösterir. JS yoksa İngilizce görünür. "Son güncelleme" yok.
    nfs = dict(NOT_FOUND)
    for l, m in LANGMOD.items(): nfs[l] = (m.NOTFOUND[0], m.NOTFOUND[2], m.NOTFOUND[3])
    links = '<p class="nf-langs">' + " · ".join(f'<a href="{url("home",l)}" lang="{IN_LANG[l]}" hreflang="{HREFLANG[l]}">{LANG_NAME[l]}</a>' for l in LANGS) + '</p>'
    blocks = "".join(f'<div data-nf="{l}" lang="{IN_LANG[l]}" data-title="{html.escape(nfs[l][0])}"{"" if l == "en" else " hidden"}><h1>{nfs[l][1]}</h1><p class="lead">{nfs[l][2].format(home=url("home", l))}</p></div>' for l in ["en"] + [x for x in LANGS if x != "en"])
    nf = {"key":"home","title":nfs["en"][0],"desc":"The page you are looking for may have moved or been removed.","no_final":True,"no_updated":True,
          "body":f'<section class="page-hero"><div class="wrap">{blocks}{links}</div></section>'}
    (DIST / "404.html").write_text(re.sub(r'<meta property="og:url"[^>]*>\n?', '', re.sub(r'<link rel="(alternate|canonical)"[^>]*>\n?', '', layout(nf, "en"))).replace('<meta name="robots" content="index,follow,max-image-preview:large">','<meta name="robots" content="noindex">'), encoding="utf-8")
    print("built", sum(len(v) for v in pages.values()), "pages")

if __name__ == "__main__":
    main()
