#!/usr/bin/env python3
"""Hostlio Pro static site generator. Run: python3 build.py  -> ./dist"""
import json, os, shutil, html, datetime, re
from pathlib import Path

ROOT = Path(__file__).parent
DIST = ROOT / "dist"
SITE = "https://hostliopro.com"          # canonical host used by the current site
SIGNUP_URL = "/signup"                           # existing sign-up page (src/signup.html, from the current site)
LOGIN_URL = "https://dashboard.hostliopro.com"   # dashboard login
FORM_ENDPOINT = "https://hook.eu1.make.com/20b5teacqjk8d330goof6adqly5vyuq2"  # Make.com webhook used by the current contact form
WHATSAPP = "13413414479"; WHATSAPP_TXT = "+1 341 341 4479"
PLANS_ENDPOINT = "https://brzetctpyaxognnvjrnd.supabase.co/functions/v1/plans"  # live prices (Supabase edge function)
PLANS_ANON = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJyemV0Y3RweWF4b2dubnZqcm5kIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Nzk2NDk3MzksImV4cCI6MjA5NTIyNTczOX0.3AKfW8oBvcXmpkwMGh972ko22nJmw0rO28fongc-S3U"  # public anon key (already public on the current site)
EMAIL = "hello@hostliopro.com"
UPDATED = "2026-09-21"
# ---- measurement & entity config (fill in before launch; empty = not rendered)
GA4_ID = ""            # e.g. "G-XXXXXXX"
PLAUSIBLE_DOMAIN = ""  # e.g. "hostliopro.com"
GSC_VERIFY = ""        # Google Search Console HTML-tag token
BING_VERIFY = ""       # Bing Webmaster msvalidate.01 token
INDEXNOW_KEY = "7f3c9a1e5b2d4c8f9e0a6b1d2c3e4f50"
SAME_AS = []           # official profiles: LinkedIn, Instagram, YouTube, X, Hotel Tech Report, G2, Capterra...
APP_STORE_URL = ""     # iOS app link
UPDATED_TXT = {"tr": "21 Eylül 2026", "en": "September 21, 2026"}
LANGS = ["tr", "en", "es", "it", "pt", "fr"]
NEW_LANGS = ["es", "it", "pt", "fr"]
LANG_NAME = {"tr": "Türkçe", "en": "English", "es": "Español", "it": "Italiano", "pt": "Português", "fr": "Français"}
LOCALE = {"tr": "tr_TR", "en": "en_US", "es": "es_ES", "it": "it_IT", "pt": "pt_BR", "fr": "fr_FR"}
IN_LANG = {"tr": "tr-TR", "en": "en", "es": "es", "it": "it", "pt": "pt", "fr": "fr"}
import importlib as _il
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
    # legacy English posts from the previous site (EN only; old URLs 301 → these)
    "post-aifrontdesk": {"en": "/en/blog/hotel-ai-front-desk-guide/"},
    "post-noshows":     {"en": "/en/blog/how-to-reduce-hotel-no-shows/"},
    "post-chains":      {"en": "/en/blog/independent-hotel-vs-chain-technology/"},
    "post-whatsapp":    {"en": "/en/blog/whatsapp-hotel-guest-communication/"},
}
for _k, _v in {'home': ('/es/', '/it/', '/pt/', '/fr/'), 'ai': ('/es/asistente-ia-para-huespedes/', '/it/assistente-ai-ospiti/', '/pt/assistente-ia-para-hospedes/', '/fr/assistant-ia-clients/'), 'channel': ('/es/channel-manager/', '/it/channel-manager/', '/pt/channel-manager/', '/fr/channel-manager/'), 'checkin': ('/es/check-in-online/', '/it/check-in-online/', '/pt/check-in-online/', '/fr/check-in-en-ligne/'), 'features': ('/es/funcionalidades/', '/it/funzionalita/', '/pt/funcionalidades/', '/fr/fonctionnalites/'), 'pricing': ('/es/precios/', '/it/prezzi/', '/pt/precos/', '/fr/tarifs/'), 'faq': ('/es/preguntas-frecuentes/', '/it/domande-frequenti/', '/pt/perguntas-frequentes/', '/fr/faq/'), 'about': ('/es/sobre-nosotros/', '/it/chi-siamo/', '/pt/sobre-nos/', '/fr/a-propos/'), 'contact': ('/es/contacto/', '/it/contatti/', '/pt/contato/', '/fr/contact/'), 'blog': ('/es/blog/', '/it/blog/', '/pt/blog/', '/fr/blog/'), 'post-pms': ('/es/blog/como-elegir-software-de-gestion-hotelera-hotel-pequeno/', '/it/blog/come-scegliere-gestionale-per-hotel-piccolo/', '/pt/blog/como-escolher-sistema-para-hotel-pequeno/', '/fr/blog/choisir-logiciel-gestion-hoteliere-petit-hotel/'), 'post-ai': ('/es/blog/responder-mensajes-de-huespedes-con-ia/', '/it/blog/rispondere-ai-messaggi-degli-ospiti-con-ai/', '/pt/blog/responder-mensagens-de-hospedes-com-ia/', '/fr/blog/repondre-aux-messages-clients-avec-ia/'), 'post-overbooking': ('/es/blog/como-evitar-el-overbooking/', '/it/blog/come-evitare-overbooking/', '/pt/blog/como-evitar-overbooking/', '/fr/blog/comment-eviter-le-surbooking/'), 'post-autoreply': ('/es/blog/respuesta-automatica-mensajes-booking-com/', '/it/blog/risposta-automatica-messaggi-booking-com/', '/pt/blog/resposta-automatica-mensagens-booking-com/', '/fr/blog/reponse-automatique-messages-booking-com/'), 't-guesthouse': ('/es/software-para-hostales/', '/it/gestionale-b-and-b/', '/pt/sistema-para-pousadas/', '/fr/logiciel-chambres-d-hotes/'), 't-boutique': ('/es/software-hotel-boutique/', '/it/gestionale-boutique-hotel/', '/pt/sistema-hotel-boutique/', '/fr/logiciel-hotel-boutique/'), 't-apart': ('/es/software-apartahotel/', '/it/gestionale-residence-aparthotel/', '/pt/sistema-apart-hotel/', '/fr/logiciel-residence-hoteliere/'), 't-hostel': ('/es/software-para-hostels/', '/it/gestionale-ostelli/', '/pt/sistema-para-hostels/', '/fr/logiciel-auberge-de-jeunesse/'), 'compare': ('/es/comparativa-software-hotelero/', '/it/confronto-gestionali-hotel/', '/pt/comparativo-sistemas-para-hotel/', '/fr/comparatif-logiciels-hoteliers/'), 'privacy': ('/es/privacidad/', '/it/privacy/', '/pt/privacidade/', '/fr/confidentialite/'), 'terms': ('/es/terminos/', '/it/termini/', '/pt/termos/', '/fr/conditions/')}.items():
    ROUTES[_k].update(dict(zip(NEW_LANGS, _v)))
def url(key, lang): return ROUTES[key].get(lang) or ROUTES["blog"][lang]
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
        "telephone": "+1-341-341-4479",
        "contactPoint": {"@type": "ContactPoint", "email": EMAIL, "telephone": "+1-341-341-4479", "contactType": "sales",
                         "availableLanguage": ["English", "Turkish"]},
        **({"sameAs": SAME_AS} if SAME_AS else {}),
    }

def website_schema(lang):
    return {"@type": "WebSite", "@id": SITE + "/#website", "url": SITE + "/", "name": "Hostlio Pro",
            "inLanguage": [IN_LANG[l] for l in LANGS], "publisher": {"@id": SITE + "/#org"}}

PLANS = [
  {"id":"starter","name":"Starter","price":49,"regular":59,"annual":470},
  {"id":"pro","name":"Pro","price":89,"regular":109,"annual":854},
  {"id":"growth","name":"Growth","price":149,"regular":189,"annual":1430},
]

def software_schema(lang, detailed=False):
    desc = {"tr": "Bağımsız oteller için yapay zekâ destekli otel yönetim yazılımı: WhatsApp ve OTA gelen kutularında 30+ dilde 7/24 misafir mesajlaşması, 100+ OTA kanal yöneticisi, rezervasyon takvimi ve online check-in.",
            "en": "AI-powered hotel management software for independent hotels: 24/7 guest messaging on WhatsApp and OTA inboxes in 30+ languages, a channel manager for 100+ OTAs, a reservation calendar and online check-in."}.get(lang, "")
    if lang in LANGMOD: desc = LANGMOD[lang].SOFT_DESC
    s = {"@type": "SoftwareApplication", "@id": SITE + "/#software", "name": "Hostlio Pro",
         "applicationCategory": "BusinessApplication",
         "applicationSubCategory": "Hotel management software (PMS)",
         "operatingSystem": "Web, iOS", "description": desc, "url": abs_url("home", lang),
         "publisher": {"@id": SITE + "/#org"},
         "featureList": {"tr": ["AI misafir asistanı Lio (WhatsApp ve OTA gelen kutuları, 30+ dil)", "Kanal yöneticisi (100+ OTA, Channex)", "Sürükle-bırak rezervasyon takvimi", "Online check-in ve dijital imza", "Otomatik PDF vize formları", "Transfer ve tur satışı", "Çevrimdışı çalışan mobil uygulama"],
                         "en": ["Lio AI guest assistant (WhatsApp and OTA inboxes, 30+ languages)", "Channel manager (100+ OTAs via Channex)", "Drag-and-drop reservation calendar", "Online check-in with digital signature", "Automatic PDF visa forms", "Transfer and tour sales", "Offline-capable mobile app"], **{l: m.SOFT_FEATURES for l, m in LANGMOD.items()}}[lang],
         "offers": {"@type": "AggregateOffer", "priceCurrency": "USD", "lowPrice": "49", "highPrice": "149", "offerCount": "3"},
         **({"downloadUrl": APP_STORE_URL, "installUrl": APP_STORE_URL} if APP_STORE_URL else {})}
    if detailed:
        s["offers"] = [{"@type": "Offer", "name": p["name"], "price": str(p["price"]), "priceCurrency": "USD",
                        "url": abs_url("pricing", lang),
                        "priceSpecification": {"@type": "UnitPriceSpecification", "price": str(p["price"]),
                                               "priceCurrency": "USD", "unitCode": "MON", "billingDuration": 1}}
                       for p in PLANS] + [
                      {"@type": "Offer", "name": p["name"] + " (annual)", "price": str(p["annual"]), "priceCurrency": "USD",
                        "url": abs_url("pricing", lang),
                        "priceSpecification": {"@type": "UnitPriceSpecification", "price": str(p["annual"]),
                                               "priceCurrency": "USD", "unitCode": "ANN", "billingDuration": 1}}
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

def final_cta(lang):
    u = UI[lang]
    return f'''<section><div class="wrap"><div class="final on-dark">
<img src="/assets/img/gen-night-desk.webp" alt="" loading="lazy" width="1080" height="1350">
<video class="final-video" muted loop playsinline preload="none" aria-hidden="true" tabindex="-1" data-webm="/assets/video/night-desk.webm" data-mp4="/assets/video/night-desk.mp4"></video>
<div><h2>{u["final_h"]}</h2><p>{u["final_p"]}</p></div>
<div class="cta-row">{btn(u["trial"], SIGNUP_URL)}{btn(u["demo"], url("contact",lang), "ghost")}</div>
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
   ("İşletme",[("features","van","Transfer ve tur satışı","Mesajlaşırken ek gelir"),("features","device-mobile","Mobil uygulama","Çevrimdışı da çalışan iOS")]),
   ("Tesis tipine göre",[("t-boutique","sparkle","Butik otel programı","10–50 odalı oteller"),("t-guesthouse","users-three","Pansiyon programı","1–10 odalı işletmeler"),("t-apart","calendar-dots","Apart otel programı","Daire ve suitler"),("t-hostel","globe-simple","Hostel programı","Yatak bazlı satış")]),
  ],"feat":("pricing","Planları karşılaştır","Aylık 49 $'dan başlar, 7 gün ücretsiz")},
 "en": {"btn":"Product","cols":[
   ("Guests",[("ai","sparkle","Lio AI assistant","24/7 guest replies in 30+ languages"),("checkin","identification-card","Online check-in","ID, companions and digital signature")]),
   ("Distribution",[("channel","arrows-left-right","Channel manager","100+ OTAs on one calendar"),("features","calendar-dots","Room rack","Drag-and-drop reservation calendar")]),
   ("Operations",[("features","van","Transfers and tours","Extra revenue while you chat"),("features","device-mobile","Mobile app","iOS that works offline too")]),
   ("By property",[("t-boutique","sparkle","Boutique hotels","10–50 room hotels"),("t-guesthouse","users-three","Guesthouses","1–10 room properties"),("t-apart","calendar-dots","Aparthotels","Apartments and suites"),("t-hostel","globe-simple","Hostels","Bed-based selling")]),
  ],"feat":("pricing","Compare plans","From $49 a month, 7 days free")},
}
for _l, _m in LANGMOD.items():
    UI[_l] = _m.UI; MEGA[_l] = _m.MEGA
EXTRA = {
 "tr": dict(bill_m="Aylık", bill_a="Yıllık", save="%20 tasarruf", billed_a="yıllık faturalandırılır", form_ok="Mesajınız bize ulaştı. İş günlerinde genellikle 24 saat içinde dönüş yapıyoruz.", form_err="Gönderilemedi. Lütfen e-posta ya da WhatsApp ile yazın.", resp="İş günlerinde genellikle 24 saat içinde yanıt veriyoruz.", sending="Gönderiliyor…"),
 "en": dict(bill_m="Monthly", bill_a="Annual", save="Save 20%", billed_a="billed annually", form_ok="Thanks, your message reached us. We typically reply within 24 hours on business days.", form_err="Couldn't send. Please email us or write on WhatsApp.", resp="We typically reply within 24 hours on business days.", sending="Sending…"),
 "es": dict(bill_m="Mensual", bill_a="Anual", save="Ahorra 20 %", billed_a="facturado anualmente", form_ok="Gracias, hemos recibido tu mensaje. Solemos responder en 24 horas en días laborables.", form_err="No se pudo enviar. Escríbenos por email o WhatsApp.", resp="Solemos responder en 24 horas en días laborables.", sending="Enviando…"),
 "it": dict(bill_m="Mensile", bill_a="Annuale", save="Risparmi il 20%", billed_a="fatturato annualmente", form_ok="Grazie, abbiamo ricevuto il tuo messaggio. Di solito rispondiamo entro 24 ore nei giorni lavorativi.", form_err="Invio non riuscito. Scrivici via email o WhatsApp.", resp="Di solito rispondiamo entro 24 ore nei giorni lavorativi.", sending="Invio…"),
 "pt": dict(bill_m="Mensal", bill_a="Anual", save="Economize 20%", billed_a="cobrado anualmente", form_ok="Obrigado, recebemos sua mensagem. Costumamos responder em até 24 horas em dias úteis.", form_err="Não foi possível enviar. Escreva para nosso e-mail ou WhatsApp.", resp="Costumamos responder em até 24 horas em dias úteis.", sending="Enviando…"),
 "fr": dict(bill_m="Mensuel", bill_a="Annuel", save="Économisez 20 %", billed_a="facturé annuellement", form_ok="Merci, votre message nous est bien parvenu. Nous répondons généralement sous 24 heures les jours ouvrés.", form_err="L’envoi a échoué. Écrivez-nous par e-mail ou sur WhatsApp.", resp="Nous répondons généralement sous 24 heures les jours ouvrés.", sending="Envoi…"),
}
ANNUAL = {
 "tr": dict(annual_line="Yıllık: aylık {am}, yılda {at} tek ödeme", tbl_h="Aylık ve yıllık fiyatlar", tbl_cols=("Plan","Aylık","Yıllık (aylık karşılığı)","Yıllık toplam","Normal aylık fiyat"), tbl_note="Early Bird fiyatları, ABD doları. Yıllık ödemede aylık ödemeye göre %20 tasarruf edersiniz."),
 "en": dict(annual_line="Annual: {am}/mo, {at} billed yearly", tbl_h="Monthly and annual prices", tbl_cols=("Plan","Monthly","Annual (per month)","Annual total","Regular monthly price"), tbl_note="Early-bird prices in USD. Annual billing saves 20% compared with paying monthly."),
 "es": dict(annual_line="Anual: {am}/mes, {at} facturados al año", tbl_h="Precios mensuales y anuales", tbl_cols=("Plan","Mensual","Anual (por mes)","Total anual","Precio mensual habitual"), tbl_note="Precios de lanzamiento en USD. La facturación anual ahorra un 20 % frente al pago mensual."),
 "it": dict(annual_line="Annuale: {am}/mese, {at} fatturati all’anno", tbl_h="Prezzi mensili e annuali", tbl_cols=("Piano","Mensile","Annuale (al mese)","Totale annuo","Prezzo mensile standard"), tbl_note="Prezzi early bird in USD. Con la fatturazione annuale risparmi il 20% rispetto al pagamento mensile."),
 "pt": dict(annual_line="Anual: {am}/mês, {at} cobrados por ano", tbl_h="Preços mensais e anuais", tbl_cols=("Plano","Mensal","Anual (por mês)","Total anual","Preço mensal normal"), tbl_note="Preços early bird em USD. O plano anual economiza 20% em relação ao pagamento mensal."),
 "fr": dict(annual_line="Annuel : {am}/mois, {at} facturés par an", tbl_h="Tarifs mensuels et annuels", tbl_cols=("Forfait","Mensuel","Annuel (par mois)","Total annuel","Prix mensuel normal"), tbl_note="Tarifs early bird en USD. La facturation annuelle permet d’économiser 20 % par rapport au paiement mensuel."),
}
for _l in EXTRA: UI[_l].update(EXTRA[_l]); UI[_l].update(ANNUAL[_l])
GEN_ALT = {
 "gen-support-call": {"tr":"Dizüstü bilgisayarında görüntülü kurulum görüşmesi yaparken not alan otel işletmecisi","en":"A hotel owner taking notes during a video onboarding call on her laptop","es":"Una propietaria de hotel toma notas durante una videollamada de puesta en marcha en su portátil","it":"Una titolare di hotel prende appunti durante una videochiamata di onboarding sul portatile","pt":"Uma dona de hotel fazendo anotações durante uma videochamada de implantação no notebook","fr":"Une propriétaire d’hôtel prend des notes pendant un appel vidéo de prise en main sur son ordinateur"},
 "gen-team-desk": {"tr":"Küçük bir otelin resepsiyonunda tablete birlikte bakan resepsiyonist ve kat görevlisi","en":"A receptionist and a housekeeper checking a tablet together at a small hotel's front desk","es":"Una recepcionista y una camarera de pisos revisan juntas una tableta en la recepción de un hotel pequeño","it":"Una receptionist e una governante controllano insieme un tablet alla reception di un piccolo hotel","pt":"Uma recepcionista e uma camareira olhando juntas um tablet na recepção de um pequeno hotel","fr":"Une réceptionniste et une femme de chambre consultent ensemble une tablette à la réception d’un petit hôtel"},
 "gen-shutters": {"tr":"Gün doğarken oda panjurlarını denize bakan eski şehre açan otel işletmecisi","en":"A hotel owner opening a room's shutters at sunrise over an old town by the sea","es":"Una propietaria de hotel abre las contraventanas de una habitación al amanecer sobre un casco antiguo junto al mar","it":"Una titolare di hotel apre gli scuri di una camera all’alba sul centro storico affacciato sul mare","pt":"Uma dona de hotel abrindo as venezianas de um quarto ao nascer do sol sobre uma cidade antiga à beira-mar","fr":"Une propriétaire d’hôtel ouvre les volets d’une chambre au lever du soleil sur une vieille ville en bord de mer"},
 "gen-hostel": {"tr":"Akdeniz tarzı bir hostelin ortak alanında sohbet eden iki gezgin, arkada ranzalar","en":"Two travellers chatting in a Mediterranean-style hostel common room, bunk beds in the background","es":"Dos viajeros charlando en la zona común de un hostel mediterráneo, con literas al fondo","it":"Due viaggiatori chiacchierano nell’area comune di un ostello mediterraneo, con i letti a castello sullo sfondo","pt":"Dois viajantes conversando na área comum de um hostel mediterrâneo, com beliches ao fundo","fr":"Deux voyageurs discutent dans l’espace commun d’une auberge méditerranéenne, lits superposés en arrière-plan"},
 "gen-apart": {"tr":"Mutfaklı, deniz manzaralı aydınlık bir apart daire","en":"Bright aparthotel apartment with a kitchenette and a sea view","es":"Apartamento luminoso de apartahotel con cocina y vistas al mar","it":"Appartamento luminoso con angolo cottura e vista mare","pt":"Apartamento claro de apart-hotel com cozinha e vista para o mar","fr":"Appartement lumineux de résidence hôtelière avec kitchenette et vue sur la mer"},
 "gen-guesthouse": {"tr":"Asma altında kurulan pansiyon kahvaltısı, masayı hazırlayan ev sahibi","en":"Guesthouse breakfast under a vine pergola, the host setting the table","es":"Desayuno de hostal bajo una pérgola de parra, con la anfitriona poniendo la mesa","it":"Colazione di un B&B sotto un pergolato, con la padrona di casa che apparecchia","pt":"Café da manhã de pousada sob um caramanchão, com a anfitriã arrumando a mesa","fr":"Petit-déjeuner de chambres d’hôtes sous une treille, l’hôtesse dresse la table"},
 "gen-boutique-room": {"tr":"Taş duvarlı, panjurlu penceresi eski şehre bakan butik otel odası","en":"Boutique hotel room with a stone wall and shuttered window over the old town","es":"Habitación de hotel boutique con pared de piedra y ventana con contraventanas al casco antiguo","it":"Camera di un boutique hotel con muro in pietra e finestra con scuri sul centro storico","pt":"Quarto de hotel boutique com parede de pedra e janela com venezianas para o centro histórico","fr":"Chambre d’hôtel boutique avec mur de pierre et fenêtre à volets sur la vieille ville"},
}
def money(n): return "$" + f"{n:,}"
def annual_table(lang):
    u = UI[lang]; c = u["tbl_cols"]
    rows = "".join(f'<tr><th scope="row">{p["name"]}</th><td class="num">{money(p["price"])}</td><td class="num">{money(round(p["annual"]/12))}</td><td class="num">{money(p["annual"])}</td><td class="num"><s>{money(p["regular"])}</s></td></tr>' for p in PLANS)
    return (f'<div class="annual-table"><h2 id="annual-h" style="font-size:var(--t-1);margin:48px 0 16px">{u["tbl_h"]}</h2><div class="table-wrap"><table aria-labelledby="annual-h"><thead><tr>'
            + "".join(f"<th>{x}</th>" for x in c) + f'</tr></thead><tbody>{rows}</tbody></table></div><p class="small muted" style="margin-top:10px">{u["tbl_note"]}</p></div>')
UI["tr"]["lang_label"] = "Dil"; UI["en"]["lang_label"] = "Language"
UI["tr"]["crumb_label"] = "Sayfa konumu"; UI["en"]["crumb_label"] = "Breadcrumb"
def mega_html(lang):
    m = MEGA[lang]
    cols = ""
    for h, items in m["cols"]:
        lis = "".join(f'<li><a href="{url(k,lang)}"><span class="mi">{icon(ic)}</span><span><b>{t}</b><span>{d}</span></span></a></li>' for k,ic,t,d in items)
        cols += f'<div><h2>{h}</h2><ul>{lis}</ul></div>'
    fk, ft, fd = m["feat"]
    cols += f'<a class="feature" href="{url(fk,lang)}"><b>{ft}</b><span>{fd}</span><span class="bi" style="width:36px;height:36px;border-radius:50%;display:grid;place-items:center;background:rgba(255,255,255,.1)">{icon("arrow-up-right")}</span></a>'
    return f'<div class="mega" id="mega" hidden><div class="wrap mega-grid">{cols}</div></div>'

# ---------------------------------------------------------------- layout
def lang_menu(key, lang):
    items = "".join(
        f'<li><a href="{url(key if l in ROUTES[key] else "home", l)}" hreflang="{l}" lang="{l}"{CUR if l == lang else ""}>{LANG_NAME[l]}</a></li>'
        for l in LANGS)
    return (f'<div class="lang-wrap"><button type="button" class="lang" aria-expanded="false" aria-controls="lang-menu" aria-label="{UI[lang]["lang_label"]}: {LANG_NAME[lang]}">'
            f'{icon("globe-simple")}{lang.upper()}{icon("caret-down","caret")}</button><ul class="lang-menu" id="lang-menu" hidden>{items}</ul></div>')

CUR = ' aria-current="page"'
def layout(page, lang):
    u = UI[lang]
    key = page["key"]
    title = page["title"]
    desc = page["desc"]
    canonical = abs_url(key, lang)
    nav = "".join(
        f'<li><a href="{url(k,lang)}"{CUR if k==key or (k=="blog" and key.startswith("post")) else ""}>{n}</a></li>'
        for k, n in u["top"])
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
        body = body.replace("data-contact-form", f'data-contact-form data-endpoint="{FORM_ENDPOINT}" data-lang="{lang}" data-ok="{html.escape(u["form_ok"])}" data-err="{html.escape(u["form_err"])}" data-sending="{html.escape(u["sending"])}"', 1)
        body = body.replace('</div>\n<form class="contact"', f'<p><a href="https://wa.me/{WHATSAPP}" rel="noopener">WhatsApp: {WHATSAPP_TXT}</a></p><p class="small muted">{u["resp"]}</p></div>\n<form class="contact"', 1)
    if '<div class="plans">' in body:
        toggle = (f'<div class="billing" role="group" aria-label="{u["bill_m"]} / {u["bill_a"]}"><button type="button" class="on" aria-pressed="true" data-bill="m">{u["bill_m"]}</button>'
                  f'<button type="button" aria-pressed="false" data-bill="a">{u["bill_a"]} <span class="save">{u["save"]}</span></button></div>')
        body = body.replace('<div class="plans">', toggle + f'<div class="plans" data-plans-endpoint="{PLANS_ENDPOINT}" data-anon="{PLANS_ANON}" data-billed="{html.escape(u["billed_a"])}">')
        for p_ in PLANS:
            line = u["annual_line"].format(am=f'<b data-am>{money(round(p_["annual"]/12))}</b>', at=f'<span data-at>{money(p_["annual"])}</span>')
            body = re.sub(r'(<h3 id="plan-' + p_["id"] + r'">.*?<div class="price num">.*?</div>)', lambda m: m.group(1) + f'<p class="annual-line num">{line}</p>', body, count=1, flags=re.S)
        if key == "pricing":
            i = body.find('<div class="plans"'); j = body.find('</article></div>', i)
            if j > 0: body = body[:j + 16] + annual_table(lang) + body[j + 16:]
    if page.get("faq") and not page.get("faq_inline"):
        body += faq_block(page["faq"], lang)
    upd = u["updated"]
    body += f'<p class="wrap small muted updated">{upd}: <time datetime="{page.get("modified", UPDATED)}">{page.get("updated_txt", UPDATED_TXT[lang])}</time></p>'
    if not page.get("no_final"):
        body += final_cta(lang)
    head_extra = ""
    if page.get("preload_img"):
        head_extra += f'<link rel="preload" as="image" href="{page["preload_img"]}" fetchpriority="high">\n'
    if GSC_VERIFY: head_extra += f'<meta name="google-site-verification" content="{GSC_VERIFY}">\n'
    if BING_VERIFY: head_extra += f'<meta name="msvalidate.01" content="{BING_VERIFY}">\n'
    if PLAUSIBLE_DOMAIN: head_extra += f'<script defer data-domain="{PLAUSIBLE_DOMAIN}" src="https://plausible.io/js/script.js"></script>\n'
    if GA4_ID: head_extra += f'<script async src="https://www.googletagmanager.com/gtag/js?id={GA4_ID}"></script><script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments)}}gtag("js",new Date());gtag("config","{GA4_ID}");</script>\n'
    year = datetime.date.fromisoformat(UPDATED).year
    for _n, _a in GEN_ALT.items():
        body = re.sub(r'(<img src="/assets/img/' + _n + r'\.webp" alt=")[^"]*"', lambda m: m.group(1) + html.escape(_a[lang]) + '"', body)
    return f'''<!doctype html>
<html class="nojs" lang="{"pt-BR" if lang=="pt" else lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{canonical}">
{"".join(f'<link rel="alternate" hreflang="{l}" href="{abs_url(key,l)}">' + chr(10) for l in langs(key)) if len(langs(key))>1 else ""}{f'<link rel="alternate" hreflang="x-default" href="{abs_url(key,"en")}">' if len(langs(key))>1 else ""}
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
<link rel="preload" href="/assets/fonts/instrument-sans-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/style.css">
{head_extra}<script type="application/ld+json">{ld}</script>
</head>
<body>
<a class="skip" href="#main">{u["skip"]}</a>
<header class="site-header"><div class="wrap nav">
<a class="brand" href="{url("home",lang)}" aria-label="Hostlio Pro">{LOGO}<span>Hostlio <span class="pro">Pro</span></span></a>
<ul class="nav-links" id="nav-links">
<li><button type="button" class="mega-btn" aria-expanded="false" aria-controls="mega">{MEGA[lang]["btn"]}{icon("caret-down","caret")}</button>{mega_html(lang)}</li>
{nav}
</ul>
<div class="nav-end">
{lang_menu(key, lang)}
<a class="login" href="{LOGIN_URL}">{u["login"]}</a>
{btn(u["trial"], SIGNUP_URL)}
<button class="menu-toggle" aria-expanded="false" aria-controls="nav-links" aria-label="{u["menu"]}"><span></span></button>
</div></div></header>
<main id="main">
{crumbs}
{body}
</main>
<footer class="site-footer"><div class="wrap">
<div class="foot-grid">
<div><a class="brand" href="{url("home",lang)}">{LOGO}<span>Hostlio <span class="pro">Pro</span></span></a><p class="muted small" style="margin-top:12px">{u["foot_tag"]}</p><p class="small"><a href="mailto:{EMAIL}">{EMAIL}</a><br><a href="https://wa.me/{WHATSAPP}" rel="noopener">WhatsApp {WHATSAPP_TXT}</a></p></div>
<div><h2>{u["foot_product"]}</h2><ul>
<li><a href="{url("features",lang)}">{dict(u["nav"])["features"]}</a></li>
<li><a href="{url("ai",lang)}">{dict(u["nav"])["ai"]}</a></li>
<li><a href="{url("channel",lang)}">{dict(u["nav"])["channel"]}</a></li>
<li><a href="{url("checkin",lang)}">Online check-in</a></li>
<li><a href="{url("pricing",lang)}">{dict(u["nav"])["pricing"]}</a></li></ul></div>
<div><h2>{u["foot_sol"]}</h2><ul>
<li><a href="{url("t-boutique",lang)}">{u["sol"][0]}</a></li>
<li><a href="{url("t-guesthouse",lang)}">{u["sol"][1]}</a></li>
<li><a href="{url("t-apart",lang)}">{u["sol"][2]}</a></li>
<li><a href="{url("t-hostel",lang)}">{u["sol"][3]}</a></li>
<li><a href="{url("compare",lang)}">{u["sol"][4]}</a></li></ul></div>
<div><h2>{u["foot_res"]}</h2><ul>
<li><a href="{url("blog",lang)}">Blog</a></li>
<li><a href="{url("faq",lang)}">{u["foot_faq"]}</a></li>
<li><a href="/llms.txt">llms.txt</a></li></ul></div>
<div><h2>{u["foot_company"]}</h2><ul>
<li><a href="{url("about",lang)}">{u["foot_about"]}</a></li>
<li><a href="{url("contact",lang)}">{u["foot_contact"]}</a></li></ul></div>
</div>
<div class="foot-bottom"><span>© {year} Hostlio Pro, Loti Members LLC. {u["rights"]}</span><span class="legal"><a href="{url("privacy",lang)}">{u["privacy"]}</a><a href="{url("terms",lang)}">{u["terms"]}</a><a href="/delete-account">{u["delacc"]}</a></span><span>2108 N ST STE N, Sacramento, CA 95816</span></div>
</div></footer>
<script src="/assets/site.js" defer></script>
<script src="/attribution.js" defer></script>
</body>
</html>'''

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

def add_srcset(doc):
    import re as _re
    def rep(m):
        tag, name = m.group(0), m.group(1)
        if "srcset=" in tag or not (ROOT / f"src/assets/img/{name}-480.webp").exists(): return tag
        w = _re.search(r'width="(\d+)"', tag); w = w.group(1) if w else "720"
        return tag.replace(f'src="/assets/img/{name}.webp"', f'src="/assets/img/{name}.webp" srcset="/assets/img/{name}-480.webp 480w, /assets/img/{name}.webp {w}w" sizes="(max-width: 640px) 92vw, (max-width: 1100px) 50vw, 600px"', 1)
    return _re.sub(r'<img [^>]*src="/assets/img/([\w-]+)\.webp"[^>]*>', rep, doc)

# ---------------------------------------------------------------- build
def write(path, content):
    p = DIST / path.lstrip("/")
    if path.endswith("/"): p = p / "index.html"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")

def main():
    import importlib
    if DIST.exists(): shutil.rmtree(DIST)
    shutil.copytree(ROOT / "src", DIST)
    # root vercel.json (used when the repo itself is deployed on Vercel): same headers/redirects + build settings
    vc = json.loads((ROOT / "src/vercel.json").read_text())
    vc = {"buildCommand": "python3 build.py || (echo \"python yok, depodaki dist kullanılıyor\" && test -f dist/index.html)", "outputDirectory": "dist", **vc}
    (ROOT / "vercel.json").write_text(json.dumps(vc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    pages = {l: importlib.import_module("content_" + l).pages() for l in LANGS}
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
            full.append(f"---\n# {p['title']}\nURL: {abs_url(p['key'], lang)}\n\n{txt}\n")
            for q, a in p.get("faq", []): full.append(f"Q: {q}\nA: {strip_tags(a)}\n")
    (DIST / "llms-full.txt").write_text("\n".join(full), encoding="utf-8")
    if INDEXNOW_KEY: (DIST / f"{INDEXNOW_KEY}.txt").write_text(INDEXNOW_KEY, encoding="utf-8")
    # sitemap with hreflang alternates
    items = []
    for key in ROUTES:
        for lang in langs(key):
            alts = "".join(f'<xhtml:link rel="alternate" hreflang="{l}" href="{abs_url(key,l)}"/>' for l in langs(key)) if len(langs(key)) > 1 else ""
            if alts: alts += f'<xhtml:link rel="alternate" hreflang="x-default" href="{abs_url(key,"en")}"/>'
            items.append(f'<url><loc>{abs_url(key,lang)}</loc><lastmod>{UPDATED}</lastmod>{alts}</url>')
    (DIST / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
        + "\n".join(items) + "\n</urlset>\n", encoding="utf-8")
    # llms.txt (GEO: plain-language index for AI answer engines)
    bykey = {l: {p["key"]: p for p in pages[l]} for l in LANGS}
    SEC = {"en": "English pages", "tr": "Türkçe sayfalar", "es": "Páginas en español", "it": "Pagine in italiano", "pt": "Páginas em português", "fr": "Pages en français"}
    def line(k, lang, src): return f'- [{src[k]["title"].split(" | ")[0]}]({abs_url(k,lang)}): {src[k]["desc"]}'
    llms = f"""# Hostlio Pro

> Hostlio Pro (also called "Hostlio") is AI-powered hotel management software (PMS) for independent hotels, boutique hotels, guesthouses, aparthotels and hostels with roughly 10–150 rooms. It combines Lio, an AI guest-messaging assistant that replies 24/7 in 30+ languages on WhatsApp and OTA inboxes (Booking.com, Airbnb, Expedia), a channel manager connected to 100+ OTAs via Channex, a drag-and-drop room rack calendar, online check-in with digital signature, automatic PDF visa forms, transfer and tour sales, and an offline-capable iOS app. Operated by Loti Members LLC (Sacramento, CA, USA). Used by independent hotels in 20+ countries.

## Key facts
- Pricing (USD/month, early-bird for first 50 customers, locked in while subscribed): Starter $49 (regular $59), Pro $89 (regular $109), Growth $149 (regular $189).
- Starter: 1 property, up to 10 rooms, 1,000 AI messages/month, 100+ OTA sync, WhatsApp AI messaging, room rack, PDF visa forms.
- Pro: 1 property, up to 50 rooms, 5,000 AI messages/month, adds OTA inbox messaging (Booking.com, Airbnb, Expedia), online check-in, transfer & tour sales, mobile app.
- Growth: up to 2 properties, 150 rooms, 12,000 AI messages/month, priority sync, priority support, onboarding call, white-label.
- Free trial: 7 days; a payment card is collected at signup, no charge until the trial ends, cancel anytime.
- Annual billing: 20% off — Starter $39/mo ($470/year), Pro $71/mo ($854/year), Growth $119/mo ($1,430/year), early-bird.
- Setup: most hotels are running in about 30 minutes (connect channels, import rooms, configure the AI assistant).
- Starter syncs OTA reservations but does not reply to OTA guest messages; OTA inbox messaging starts from Pro.
- Channels include Booking.com, Airbnb, Expedia, Agoda, Trip.com, Hotels.com, Hotelbeds, Hostelworld, Google Hotels.
- Languages: website in English, Turkish, Spanish, Italian, Portuguese and French; support in English and Turkish; guest replies in 30+ languages.
- Contact: {EMAIL}, WhatsApp {WHATSAPP_TXT}
- Last updated: {UPDATED}

""" + "\n\n".join(f"## {SEC[l]}\n" + "\n".join(line(k, l, bykey[l]) for k in ROUTES if l in ROUTES[k]) for l in ["en","tr","es","it","pt","fr"]) + "\n"
    (DIST / "llms.txt").write_text(llms, encoding="utf-8")
    # 404
    nf = {"key":"home","title":"Sayfa bulunamadı | Hostlio Pro","desc":"Aradığınız sayfa taşınmış ya da kaldırılmış olabilir.","no_final":True,
          "body":f'<section class="page-hero"><div class="wrap"><h1>Bu sayfa bulunamadı</h1><p class="lead">Adres değişmiş olabilir. <a href="/">Ana sayfaya dönün</a>.</p><p>'+" · ".join(f'<a href="{url("home",l)}" lang="{l}">{LANG_NAME[l]}</a>' for l in LANGS)+'</p></div></section>'}
    (DIST / "404.html").write_text(re.sub(r'<link rel="(alternate|canonical)"[^>]*>\n?', '', layout(nf, "tr")).replace('<meta name="robots" content="index,follow,max-image-preview:large">','<meta name="robots" content="noindex">'), encoding="utf-8")
    print("built", sum(len(v) for v in pages.values()), "pages")

if __name__ == "__main__":
    main()
