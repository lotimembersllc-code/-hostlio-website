"""Home page (v3, brand visuals) shared by TR and EN."""
from build import icon, logo, btn, room_rack, url, SIGNUP_URL, EMAIL, software_schema, LANGMOD

IMG = "/assets/img/"
TI = ' tabindex="-1"'
HID = " hidden"

T = {
"tr": dict(
  title="Hostlio Pro | AI Destekli Otel Programı ve Kanal Yöneticisi",
  desc="Otel programı Hostlio Pro: AI asistan Lio misafir mesajlarını 30+ dilde 7/24 yanıtlar, kanal yöneticisi 100+ OTA'yı senkronize eder. 7 gün ücretsiz deneyin.",
  h1='Oteliniz uyurken <em class="hl">Lio</em> cevap verir',
  lead="Bağımsız oteller ve pansiyonlar için yapay zekâ destekli otel programı. Rezervasyonlar, 100+ kanal ve misafir mesajları tek panelde, 30+ dilde.",
  try_="Ücretsiz dene", demo="Demo iste", via="Sertifikalı bağlantılar:", more="ve 100+ kanal",
  coll_alt1="Bugenvilli ve havuzlu, gün batımında butik otel avlusu", coll_alt2="Kahvesini içerek gülümseyen otel işletmecisi",
  chip1=("Oda 202 satıldı","Booking.com, 21:40"), chip2="Airbnb ve Expedia'da kapandı",
  bub_h=("Lio","AI resepsiyonist, çevrimiçi"), bub_in="Hallo! Ist ein später Check-in möglich?", bub_out="Natürlich! Unsere Rezeption ist rund um die Uhr besetzt.", bub_note="Almanca yanıtlandı, 4 sn",
  pick_h="Neyle başlamak istersiniz?", pick_p="Seçimlerinize göre hesabınızı hazırlayalım.", pick_none="İstediğiniz kadar seçebilirsiniz.", pick_some="{n} modül seçildi, 7 gün ücretsiz deneyin.", pick_btn="Başla", pick_name="ilgi",
  tiles=[("ai","sparkle","t-peach","AI asistan Lio","Misafir mesajlarına 30+ dilde yanıt"),("channel","arrows-left-right","t-lilac","Kanal yöneticisi","100+ OTA ile anlık senkron"),("rack","calendar-dots","t-sand","Oda rafı","Sürükle-bırak rezervasyon takvimi"),("checkin","identification-card","t-peach","Online check-in","Kimlik ve imza varıştan önce"),("upsell","van","t-lilac","Transfer ve tur","Mesajlaşırken ek gelir"),("mobile","device-mobile","t-sand","Mobil uygulama","Otel dışından yönetim")],
  story_h='Gece <em class="hl">02:14</em>, bir misafir yazıyor',
  story_p="Siz uyurken olan biten, üç karede.",
  story=[("brand-night","Uyuyan otel işletmecisi ve komodinde yanan telefon","02:14","Misafir mesaj atar","Almanya'dan gelen misafir geç check-in'i soruyor. Siz derin uykudasınız."),
         ("brand-phone","Elde tutulan telefonda turuncu Lio yanıt ekranı","02:14","Lio anında cevaplar","Otelinizin bilgileriyle, misafirin kendi dilinde. Gerekiyorsa size not bırakır."),
         ("brand-hotelier","Sabah lobide kahvesiyle yürüyen otel işletmecisi","08:30","Sabah her şey hazır","Yazışma Türkçe çevirisiyle panelinizde. Misafir memnun, siz dinlenmiş.")],
  story_chip="Lio yanıtladı",
  tour_h='Otelinizin gününü <em class="hl">tek ekrandan</em> yönetin', tour_p="Misafir mesajı, rezervasyon, kanal ve check-in birbirine bağlı çalışır.", tour_label="Ürün turu",
  tabs=["Mesajlar","Takvim","Kanallar","Check-in"],
  st=[("Tüm misafir mesajları tek gelen kutusunda","WhatsApp ve OTA gelen kutusu mesajları (Booking.com, Airbnb, Expedia) bir arada. Lio otelinizin bilgileriyle cevaplar, siz sadece gerekeni görürsünüz.",["30+ dilde otomatik yanıt","Her mesajın yanında rezervasyon bilgisi","Emin olmadığı soruyu size devreder"],"ai","Lio nasıl çalışır"),
      ("Oda rafında haftanın tamamı","Her rezervasyonu kanal rengiyle görün. Oda değiştirmek, konaklamayı uzatmak ya da blokaj koymak tek hareket.",["Sürükle-bırak oda değişikliği","Kanal renkleriyle rezervasyonlar","Web ve iOS'ta aynı takvim"],"features","Tüm özellikler"),
      ("100+ kanal, tek müsaitlik","Sertifikalı kanal bağlantılarıyla çift yönlü senkron. Bir kanalda satılan oda diğerlerinde anında kapanır.",["Fiyat ve kısıtlamalar tek ekrandan","Yeni rezervasyon ve iptaller otomatik","Overbooking riski yok"],"channel","Kanal yöneticisi"),
      ("Check-in varıştan önce biter","Misafir güvenli bağlantıdan kimlik bilgilerini, refakatçilerini ve imzasını telefonundan gönderir.",["Uygulama indirmeden, tarayıcıda","Refakatçi misafirler tek formda","Dijital imza ve açık rıza"],"checkin","Online check-in")],
  inbox_top=("Gelen kutusu","12 açık konuşma"), inbox_note="Çeviri: Check-in 14:00'te, bavullarınızı hemen alabiliriz.",
  chan_top=("Bağlı kanallar","Son senkron: şimdi"), sync="Senkron",
  ci_top=("Online check-in","Oda 202"), ci_f=[("Ad soyad","Keiko Sato"),("Uyruk","Japonya"),("Refakatçi","1 misafir eklendi")], ci_sig="İmza",
  bento_h='Bir otelin ihtiyacı olan <em class="hl">her şey</em>', bento_p="Her modül birbirine bağlı; ayrı ayrı araç, ayrı ayrı şifre yok.",
  b_lio=("AI asistan Lio","Misafir sorularının çoğunu siz görmeden kapatır, kalanını size özetler.","Is breakfast included?","Yes, from 7:30 to 10:30 on the terrace."),
  b_chan=("Kanal yöneticisi","100+ satış kanalı, tek müsaitlik."),
  b_rack=("Oda rafı","Sürükle-bırak rezervasyon takvimi."),
  b_ci=("Online check-in","Kimlik, refakatçi ve dijital imza varıştan önce."),
  b_pdf=("PDF vize formları","Konaklama ve davet belgeleri tek tıkla.","Konaklama belgesi","PDF"),
  b_tr=("Transfer ve tur satışı","Lio doğru anda teklif eder, siz kazanırsınız.","Havalimanı transferi","+35 €"),
  b_lang=("30+ dil","Misafir hangi dilde yazarsa o dilde cevap."),
  b_mob=("Mobil uygulama","iOS'ta rezervasyon, mesaj ve check-in; internet yokken de."),
  types_h='Her <em class="hl">tesis tipine</em> uygun', types_p="1 ila 150 odalı bağımsız tesisler için tasarlandı.",
  types=[("brand-courtyard","Havuzlu, bugenvilli butik otel avlusu","Butik otel","10–50 oda","Yabancı misafiri çok, her mesaj kişisel."),
         ("gen-hostel","Ahşap panelli, ortak alanlı konaklama lobisi","Hostel","Yatak ve oda","Çok dilli gezginler, yoğun mesaj trafiği."),
         ("gen-guesthouse","Masa lambalı sıcak pansiyon odası","Pansiyon","1–10 oda","Tek kişilik ekip için gece vardiyası."),
         ("gen-apart","Aydınlık beyaz nevresimli apart daire","Apart otel","10–40 daire","Varıştan önce online check-in.")],
  plans_h="Otelinizin büyüklüğüne göre plan", plans_p="Sabit aylık ücret, uzun süreli sözleşme yok. Tüm planlar 7 gün ücretsiz.",
  early="İlk 50 müşteriye %20 indirim, abonelik boyunca sabit", tax='Fiyatlara vergi dahil değildir. <a href="{p}">Planları detaylı karşılaştırın</a>.',
  ai_h='Lio: resepsiyonunuzun <em class="hl">gece vardiyası</em>', ai_p="Otelinizin bilgileriyle çalışan yapay zekâ asistanı. Misafire cevap verir, satış yapar, gerekeni size bırakır.",
  ai_wide=("Misafirin dilinde cevap","Japonca soru Japonca, Arapça soru Arapça yanıtlanır. Siz yazışmayı Türkçe okursunuz."),
  ai_cards=[("van","Satış yapar","Havalimanı transferi ve turu doğru anda önerir, talebi size iletir."),("hand-arrow-up","Gerekeni size bırakır","İndirim, şikâyet ya da özel istek gibi karar gerektiren mesajları personele iletir."),("calendar-dots","Rezervasyonu tanır","Misafir rezervasyonla eşleştiğinde oda, tarih ve rezervasyon bilgilerini cevaba katar.")],
  ai_photo=("brand-guest-phone","Pencere kenarında telefonundan mesaj yazan misafir","WhatsApp ve OTA'larda","WhatsApp, Booking.com, Airbnb ve Expedia."),
  ai_btn="Lio'yu inceleyin",
  answer="<strong>Hostlio Pro nedir?</strong> Hostlio Pro, 1 ila 150 odalı bağımsız oteller ve pansiyonlar için bulut tabanlı bir otel programıdır (PMS). Misafir iletişimini yapay zekâya devreder, OTA rezervasyonlarını tek takvimde toplar, check-in'i misafirin telefonuna taşır. Web'den ve iOS uygulamasından yönetilir, 20'den fazla ülkede kullanılır.",
  stats=[("30+","dilde misafir yanıtı"),("100+","OTA ve satış kanalı"),("20+","ülkede bağımsız oteller"),("7 gün","ücretsiz deneme, taahhüt yok")],
  sup_h="Yanınızda bir ekip var",
  sup=[("rocket-launch","t-peach","Dakikalar içinde hesap, aynı gün kanal","Hesabınız dakikalar içinde hazır; oda tiplerini girip kanalları aynı gün bağlayın. Growth planında birebir kurulum görüşmesi dahil."),
       ("lifebuoy","t-lilac","Türkçe ve İngilizce destek",'Takıldığınız yerde ekibe <a href="mailto:{e}">{e}</a> adresinden ulaşın.'),
       ("book-open-text","t-sand","Rehberler",'Otel yönetimi ve dağıtım üzerine <a href="{b}">blog yazıları</a> ve <a href="{f}">sık sorulan sorular</a>.')],
  sup_img=("gen-support-call","Dizüstü bilgisayarında rezervasyonlara bakan otel işletmecisi"),
),
"en": dict(
  title="Hostlio Pro | AI Hotel Management Software for Independent Hotels",
  desc="Hostlio Pro hotel management software: the Lio AI assistant answers guest messages 24/7 in 30+ languages, and the channel manager syncs 100+ OTAs. Free 7-day trial.",
  h1='While your hotel sleeps, <em class="hl">Lio</em> replies',
  lead="AI-powered hotel management software for independent hotels and guesthouses. Reservations, 100+ channels and guest messages in one place, in 30+ languages.",
  try_="Try it free", demo="Book a demo", via="Certified connections to:", more="and 100+ more",
  coll_alt1="Boutique hotel courtyard with bougainvillea and a pool at sunset", coll_alt2="Smiling hotel owner holding a cup of coffee",
  chip1=("Room 202 sold","Booking.com, 21:40"), chip2="Closed on Airbnb and Expedia",
  bub_h=("Lio","AI receptionist, online"), bub_in="Hallo! Ist ein später Check-in möglich?", bub_out="Natürlich! Unsere Rezeption ist rund um die Uhr besetzt.", bub_note="Answered in German, 4 sec",
  pick_h="What would you like to start with?", pick_p="Pick what matters and we set up your account around it.", pick_none="Pick as many as you like.", pick_some="{n} selected, try them free for 7 days.", pick_btn="Get started", pick_name="interest",
  tiles=[("ai","sparkle","t-peach","Lio AI assistant","Guest replies in 30+ languages"),("channel","arrows-left-right","t-lilac","Channel manager","Real-time sync with 100+ OTAs"),("rack","calendar-dots","t-sand","Room rack","Drag-and-drop reservation calendar"),("checkin","identification-card","t-peach","Online check-in","ID and signature before arrival"),("upsell","van","t-lilac","Transfers and tours","Extra revenue while you chat"),("mobile","device-mobile","t-sand","Mobile app","Run the hotel from anywhere")],
  story_h='<em class="hl">2:14 am</em>, a guest is writing',
  story_p="What happens while you sleep, in three frames.",
  story=[("brand-night","Hotel owner asleep with a phone lighting up on the nightstand","02:14","A guest messages","A guest from Germany asks about late check-in. You're fast asleep."),
         ("brand-phone","Hand holding a phone showing Lio's orange reply screen","02:14","Lio replies instantly","With your hotel's information, in the guest's own language. It leaves you a note if needed."),
         ("brand-hotelier","Hotel owner walking through the lobby with a morning coffee","08:30","Morning, all sorted","The conversation waits in your dashboard, translated. A happy guest and a rested you.")],
  story_chip="Lio replied",
  tour_h='Run your hotel\'s day <em class="hl">from one screen</em>', tour_p="Guest messages, reservations, channels and check-in work together.", tour_label="Product tour",
  tabs=["Messages","Calendar","Channels","Check-in"],
  st=[("Every guest message in one inbox","WhatsApp and OTA inbox messages (Booking.com, Airbnb, Expedia) together. Lio answers with your hotel's information, and you only see what needs you.",["Automatic replies in 30+ languages","Reservation details beside every message","Hands over what it isn't sure about"],"ai","How Lio works"),
      ("Your whole week on the room rack","See every booking in its channel colour. Moving rooms, extending stays or blocking dates takes one gesture.",["Drag-and-drop room moves","Bookings colour-coded by channel","The same calendar on web and iOS"],"features","All features"),
      ("100+ channels, one availability","Two-way sync over certified channel connections. A room sold on one channel closes on the others instantly.",["Rates and restrictions from one screen","New bookings and cancellations flow in","No overbooking risk"],"channel","Channel manager"),
      ("Check-in is done before arrival","Guests send ID details, companions and a signature from their phone through a secure link.",["In the browser, no app download","Companions in a single form","Digital signature and consent"],"checkin","Online check-in")],
  inbox_top=("Inbox","12 open conversations"), inbox_note="Translation: Check-in is from 2 pm, we can hold your luggage.",
  chan_top=("Connected channels","Last sync: just now"), sync="In sync",
  ci_top=("Online check-in","Room 202"), ci_f=[("Full name","Keiko Sato"),("Nationality","Japan"),("Companions","1 guest added")], ci_sig="Signature",
  bento_h='<em class="hl">Everything</em> a hotel needs', bento_p="Every module is connected: no separate tools, no separate passwords.",
  b_lio=("Lio AI assistant","Closes most guest questions before you see them and summarises the rest.","Is breakfast included?","Yes, from 7:30 to 10:30 on the terrace."),
  b_chan=("Channel manager","100+ sales channels, one availability."),
  b_rack=("Room rack","Drag-and-drop reservation calendar."),
  b_ci=("Online check-in","ID, companions and digital signature before arrival."),
  b_pdf=("PDF visa forms","Accommodation and invitation letters in one click.","Accommodation letter","PDF"),
  b_tr=("Transfer and tour sales","Lio offers them at the right moment; you earn more.","Airport transfer","+€35"),
  b_lang=("30+ languages","Whatever language the guest writes in, that's the reply."),
  b_mob=("Mobile app","Bookings, messages and check-ins on iOS, even offline."),
  types_h='Built for <em class="hl">every kind of property</em>', types_p="Designed for independent properties with 1 to 150 rooms.",
  types=[("brand-courtyard","Boutique hotel courtyard with a pool and bougainvillea","Boutique hotel","10–50 rooms","Many international guests, every message personal."),
         ("gen-hostel","Lobby with wood panelling and shared seating","Hostel","Beds and rooms","Multilingual travellers, busy inboxes."),
         ("gen-guesthouse","Warm guesthouse room with a desk lamp","Guesthouse","1–10 rooms","A night shift for a one-person team."),
         ("gen-apart","Bright apartment with white bedding","Aparthotel","10–40 units","Online check-in before arrival.")],
  plans_h="A plan for your hotel's size", plans_p="A flat monthly fee, no long-term contract. Every plan is free for 7 days.",
  early="20% off for the first 50 customers, locked in for life", tax='Prices exclude taxes. <a href="{p}">Compare plans in detail</a>.',
  ai_h='Lio, your front desk\'s <em class="hl">night shift</em>', ai_p="An AI assistant that works from your hotel's information. It answers guests, sells extras and leaves the rest to you.",
  ai_wide=("Replies in the guest's language","A Japanese question gets a Japanese answer, an Arabic one an Arabic answer. You read the conversation in your own language."),
  ai_cards=[("van","Sells for you","Suggests airport transfers and tours at the right moment and passes the request to you."),("hand-arrow-up","Knows when to hand over","Messages that need a decision, like discounts, complaints or special requests, go to your staff."),("calendar-dots","Knows the booking","When the guest is matched to a reservation, replies use the room, dates and booking details.")],
  ai_photo=("brand-guest-phone","Guest by a window typing a message on her phone","On WhatsApp and OTAs","WhatsApp, Booking.com, Airbnb and Expedia."),
  ai_btn="Explore Lio",
  answer="<strong>What is Hostlio Pro?</strong> Hostlio Pro is cloud hotel management software (a PMS) for independent hotels and guesthouses with 1 to 150 rooms. It hands guest communication to AI, pulls OTA bookings into one calendar and moves check-in to the guest's phone. Managed from the web and an iOS app, used in 20+ countries.",
  stats=[("30+","languages answered"),("100+","OTAs and sales channels"),("20+","countries with Hostlio Pro hotels"),("7 days","free trial, no commitment")],
  sup_h="A team behind you",
  sup=[("rocket-launch","t-peach","Ready in minutes, live the same day","Your account is ready in minutes; add room types and connect channels the same day. Growth includes a one-to-one onboarding call."),
       ("lifebuoy","t-lilac","Support in English and Turkish",'Stuck on something? Reach the team at <a href="mailto:{e}">{e}</a>.'),
       ("book-open-text","t-sand","Guides",'<a href="{b}">Blog posts</a> on hotel management and distribution, plus <a href="{f}">frequently asked questions</a>.')],
  sup_img=("gen-support-call","Hotel owner checking bookings on a laptop"),
),
}

def img(name, alt, w=720, h=900, lazy=True):
    lz = ' loading="lazy"' if lazy else ""
    return f'<img src="{IMG}{name}.webp" alt="{alt}" width="{w}" height="{h}"{lz} decoding="async">'

for _l, _m in LANGMOD.items(): T[_l] = _m.HOME

SUPCARD = {
 "tr": dict(h="Hostlio Pro destek", sub="Genellikle 24 saat içinde yanıt", q="Booking.com'u nasıl bağlarım?", a="Kanallar bölümünden Booking.com'u seçip bir kez yetkilendirin. Rezervasyonlar otomatik senkronize olur.", chip="Kanal bağlandı"),
 "en": dict(h="Hostlio Pro support", sub="Usually replies within 24 hours", q="How do I connect Booking.com?", a="Pick Booking.com under Channels and authorise it once. Reservations then sync automatically.", chip="Channel connected"),
 "es": dict(h="Soporte de Hostlio Pro", sub="Suele responder en 24 horas", q="¿Cómo conecto Booking.com?", a="Elige Booking.com en Canales y autorízalo una vez. Las reservas se sincronizan automáticamente.", chip="Canal conectado"),
 "it": dict(h="Supporto Hostlio Pro", sub="Di solito risponde entro 24 ore", q="Come collego Booking.com?", a="Scegli Booking.com in Canali e autorizzalo una volta. Le prenotazioni si sincronizzano in automatico.", chip="Canale collegato"),
 "pt": dict(h="Suporte Hostlio Pro", sub="Costuma responder em até 24 horas", q="Como conecto o Booking.com?", a="Escolha o Booking.com em Canais e autorize uma vez. As reservas são sincronizadas automaticamente.", chip="Canal conectado"),
 "fr": dict(h="Support Hostlio Pro", sub="Répond généralement sous 24 heures", q="Comment connecter Booking.com ?", a="Choisissez Booking.com dans Canaux et autorisez-le une seule fois. Les réservations se synchronisent ensuite automatiquement.", chip="Canal connecté"),
}

def home(L, plans_html, FAQ_CORE):
    t = T[L]; U = lambda k: url(k, L)
    chk = lambda items: "<ul>" + "".join(f"<li>{icon('check')}<span>{x}</span></li>" for x in items) + "</ul>"
    more = lambda k, s: f'<a class="more" href="{U(k)}">{s}{icon("arrow-up-right")}</a>'
    partners = "".join(logo(n, lbl) for n, lbl in [("bookingdotcom","Booking.com"),("airbnb","Airbnb"),("expedia","Expedia"),("tripdotcom","Trip.com"),("hotelsdotcom","Hotels.com"),("google","Google Hotels")])

    hero_img = img("brand-courtyard", t["coll_alt1"], 880, 804, lazy=False).replace("<img ", '<img fetchpriority="high" ', 1)
    hero = f'''<section class="hero"><div class="wrap hero-split">
<div><h1>{t["h1"]}</h1><p class="lead">{t["lead"]}</p>
<div class="cta-row">{btn(t["try_"], SIGNUP_URL)}{btn(t["demo"], __import__("build").demo_url(L), "ghost")}</div>
<div class="partners"><span>{t["via"]}</span><span class="logos">{partners}</span><span>{t["more"]}</span></div></div>
<div class="collage">
<div class="c-main">{hero_img}</div>
<div class="c-side">{img("brand-host-coffee", t["coll_alt2"], 658, 921, lazy=False)}</div>
<span class="chip" style="top:18px;left:18px" aria-hidden="true">{logo("bookingdotcom")}<span>{t["chip1"][0]}<small>{t["chip1"][1]}</small></span></span>
<span class="chip" style="top:76px;left:18px" aria-hidden="true">{icon("check")}{t["chip2"]}</span>
<div class="bubble" aria-hidden="true"><div class="bh"><i>L</i><span>{t["bub_h"][0]}<small><span class="dot-live"></span>{t["bub_h"][1]}</small></span></div>
<div class="msg in" lang="de">{t["bub_in"]}</div><div class="msg out" lang="de">{t["bub_out"]}<small lang="{L}">{t["bub_note"]}</small></div></div>
</div></div></section>'''

    tiles = "".join(f'''<label class="tile"><input type="checkbox" name="{t["pick_name"]}" value="{v}"><span class="box">{icon("check")}</span>
<span class="ti {c}">{icon(ic)}</span><span><b>{a}</b><small>{d}</small></span></label>''' for v,ic,c,a,d in t["tiles"])
    picker = f'''<section style="padding-top:0"><div class="wrap"><div class="shell"><form class="core picker" data-picker action="{SIGNUP_URL}" method="get">
<div class="picker-head"><h2>{t["pick_h"]}</h2><p>{t["pick_p"]}</p></div><div class="tiles">{tiles}</div>
<div class="picker-foot"><p data-count data-none="{t["pick_none"]}" data-some="{t["pick_some"]}">{t["pick_none"]}</p>
<button class="btn btn-primary" type="submit">{t["pick_btn"]}<span class="bi">{icon("arrow-up-right")}</span></button></div></form></div></div></section>'''

    st = ""
    for i,(im,alt,tm,h,p) in enumerate(t["story"]):
        chip = f'<span class="chip" aria-hidden="true">{icon("sparkle")}{t["story_chip"]}</span>' if i == 1 else ""
        st += f'<article>{img(im, alt)}<span class="time">{tm}</span>{chip}<div class="txt"><h3>{h}</h3><p>{p}</p></div></article>'
    story = f'''<section class="white rule"><div class="wrap"><div class="section-head rv"><h2>{t["story_h"]}</h2><p>{t["story_p"]}</p></div>
<div class="story">{st}</div></div></section>'''

    inbox = f'''<div class="ui"><div class="ui-top">{t["inbox_top"][0]}<span>{t["inbox_top"][1]}</span></div><div class="inbox" aria-hidden="true">
<div class="inbox-list"><div class="on"><i>KS</i><span><b>Keiko Sato</b><span>Booking.com</span></span></div><div><i>LR</i><span><b>Luca Rossi</b><span>Airbnb</span></span></div><div><i>AD</i><span><b>Amélie Dubois</b><span>WhatsApp</span></span></div><div><i>MA</i><span><b>Mona Al-Sayed</b><span>Expedia</span></span></div></div>
<div class="ui-body thread"><div class="msg in" lang="ja">チェックインは何時ですか？<small>Keiko, 03:12</small></div>
<div class="msg out" lang="ja">チェックインは14:00からです。お荷物は到着後すぐにお預かりできます。<small>Lio, 03:12</small></div>
<div class="msg note">{t["inbox_note"]}</div></div></div></div>'''
    chans = "".join(f'<div><span class="nm">{logo(n)}{lbl}</span><span class="pill">{t["sync"]}</span></div>' for n,lbl in [("bookingdotcom","Booking.com"),("airbnb","Airbnb"),("expedia","Expedia"),("tripdotcom","Trip.com"),("google","Google Hotels")])
    chan_ui = f'<div class="ui"><div class="ui-top">{t["chan_top"][0]}<span>{t["chan_top"][1]}</span></div><div class="ui-body chan-list" aria-hidden="true">{chans}</div></div>'
    sig = '<svg viewBox="0 0 120 40" fill="none" aria-hidden="true"><path d="M4 30c10-18 18-22 20-12s-6 14 2 6 14-20 18-12-4 16 4 10 12-12 18-6 6 8 14 2 10-8 16-6" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>'
    fields = "".join(f'<div class="field"><span>{a}</span><div>{b}</div></div>' for a,b in t["ci_f"])
    ci_ui = f'<div class="ui"><div class="ui-top">{t["ci_top"][0]}<span>{t["ci_top"][1]}</span></div><div class="ui-body" aria-hidden="true">{fields}<div class="field"><span>{t["ci_sig"]}</span><div class="sig">{sig}</div></div></div></div>'
    visuals = [inbox, room_rack(L), chan_ui, ci_ui]
    grads = ["g-lilac","g-sky","g-mint","g-peach"]; icons_ = ["chats-circle","calendar-dots","arrows-left-right","identification-card"]; ids = "mtkc"
    tabs = "".join(f'<button class="tab" role="tab" id="tab-{ids[i]}" aria-controls="st-{ids[i]}" aria-selected="{"true" if i==0 else "false"}"{"" if i==0 else TI}>{icon(icons_[i])}{t["tabs"][i]}</button>' for i in range(4))
    stages = "".join(f'<div class="stage {grads[i]}" role="tabpanel" id="st-{ids[i]}" aria-labelledby="tab-{ids[i]}"{"" if i==0 else HID}><div><h3>{h}</h3><p>{p}</p>{chk(li)}{more(k,m)}</div>{visuals[i]}</div>' for i,(h,p,li,k,m) in enumerate(t["st"]))
    tour = f'''<section><div class="wrap"><div class="section-head center rv"><h2>{t["tour_h"]}</h2><p>{t["tour_p"]}</p></div>
<div class="tabs" role="tablist" aria-label="{t["tour_label"]}" style="justify-content:center">{tabs}</div>{stages}</div></section>'''

    lio, chan, rack, ci, pdf, tr, lang, mob = t["b_lio"], t["b_chan"], t["b_rack"], t["b_ci"], t["b_pdf"], t["b_tr"], t["b_lang"], t["b_mob"]
    logos6 = "".join(f"<span>{logo(n)}</span>" for n in ["bookingdotcom","airbnb","expedia","tripdotcom","hotelsdotcom","google"])
    bento = f'''<section class="white rule"><div class="wrap"><div class="section-head rv"><h2>{t["bento_h"]}</h2><p>{t["bento_p"]}</p></div>
<div class="bento">
<a class="card photo span8" href="{U("ai")}">{img("brand-guest-bed","",1200,675)}<div class="float" aria-hidden="true"><span class="chip" lang="en">{logo("whatsapp")}{lio[2]}</span><span class="chip" lang="en">{icon("sparkle")}{lio[3]}</span></div><div class="txt"><h3>{lio[0]}</h3><p>{lio[1]}</p></div></a>
<a class="card navy" href="{U("channel")}"><span class="ci">{icon("arrows-left-right")}</span><h3>{chan[0]}</h3><p>{chan[1]}</p><div class="vis logo-grid" aria-hidden="true">{logos6}</div></a>
<a class="card" href="{U("features")}"><span class="ci">{icon("calendar-dots")}</span><h3>{rack[0]}</h3><p>{rack[1]}</p><div class="vis mini-rack" aria-hidden="true"><div style="background:#1B2B4B;color:#fff;width:78%">K. Sato</div><div style="background:var(--orange);color:var(--ink);width:56%;margin-left:30%">Öztürk</div><div style="background:var(--peach);color:var(--peach-ink);width:64%;margin-left:12%">L. Rossi</div></div></a>
<a class="card" href="{U("checkin")}"><span class="ci">{icon("identification-card")}</span><h3>{ci[0]}</h3><p>{ci[1]}</p><div class="vis sig" aria-hidden="true">{sig}</div></a>
<a class="card" href="{U("features")}"><span class="ci">{icon("file-pdf")}</span><h3>{pdf[0]}</h3><p>{pdf[1]}</p><div class="vis pdf" aria-hidden="true"><div class="ph">{pdf[2]}<span>{pdf[3]}</span></div><i class="m"></i><i></i><i class="s"></i></div></a>
<a class="card peach" href="{U("features")}"><span class="ci">{icon("van")}</span><h3>{tr[0]}</h3><p>{tr[1]}</p><div class="vis price-chip" aria-hidden="true">{tr[2]}<b>{tr[3]}</b></div></a>
<a class="card" href="{U("ai")}"><span class="ci">{icon("translate")}</span><h3>{lang[0]}</h3><p>{lang[1]}</p><div class="vis langs" aria-hidden="true"><span>Türkçe</span><span>English</span><span lang="de">Deutsch</span><span lang="ar">العربية</span><span lang="ru">Русский</span><span lang="ja">日本語</span><span lang="zh">中文</span><span lang="fr">Français</span></div></a>
<a class="card photo" href="{U("features")}">{img("brand-phone","")}<div class="txt"><h3>{mob[0]}</h3><p>{mob[1]}</p></div></a>
</div></div></section>'''

    tkeys = ["t-boutique","t-hostel","t-guesthouse","t-apart"]
    types = "".join(f'<a class="type" href="{U(tkeys[i])}">{img(im, alt)}<span class="tag">{tag}</span><div class="txt"><h3>{h}</h3><p>{p}</p></div></a>' for i,(im,alt,h,tag,p) in enumerate(t["types"]))
    types_sec = f'''<section><div class="wrap"><div class="section-head rv"><h2>{t["types_h"]}</h2><p>{t["types_p"]}</p></div><div class="types">{types}</div></div></section>'''

    plans = f'''<section class="white rule"><div class="wrap"><div class="section-head rv"><h2>{t["plans_h"]}</h2><p>{t["plans_p"]}</p></div>
<span class="billing-note">{icon("sparkle")}{t["early"]}</span>{plans_html()}
<p class="small muted" style="margin-top:18px">{t["tax"].format(p=U("pricing"))}</p></div></section>'''

    aw, ap = t["ai_wide"], t["ai_photo"]
    cards = "".join(f'<article class="ai-card"><span class="ai">{icon(ic)}</span><h3>{h}</h3><p>{p}</p></article>' for ic,h,p in t["ai_cards"])
    ai = f'''<section class="dark"><div class="wrap"><div class="section-head rv"><h2>{t["ai_h"]}</h2><p>{t["ai_p"]}</p></div>
<div class="ai-grid">
<article class="ai-card wide"><span class="ai">{icon("translate")}</span><h3>{aw[0]}</h3><p>{aw[1]}</p>
<div class="thread" aria-hidden="true"><div class="msg in" lang="ar" dir="rtl">هل الإفطار مشمول في الحجز؟</div><div class="msg out" lang="ar" dir="rtl">نعم، الإفطار مشمول ويُقدَّم من 7:30 حتى 10:30.</div></div></article>
<article class="ai-card card photo ai-photo">{img(ap[0], ap[1])}<div class="txt"><h3>{ap[2]}</h3><p>{ap[3]}</p></div></article>
{cards}</div>
<div class="cta-row">{btn(t["ai_btn"], U("ai"))}</div></div></section>'''

    stats = "".join(f'<div><b class="num">{a}</b><span>{b}</span></div>' for a,b in t["stats"])
    stats_sec = f'''<section><div class="wrap"><div class="answer rv" style="margin-bottom:48px"><p>{t["answer"]}</p></div><div class="stats">{stats}</div></div></section>'''

    sc = SUPCARD[L]
    sup = "".join(f'<article><span class="ai {c}">{icon(ic)}</span><h3>{h}</h3><p>{p.format(e=EMAIL, b=U("blog"), f=U("faq"))}</p></article>' for ic,c,h,p in t["sup"])
    support = f'''<section class="white rule"><div class="wrap split" style="align-items:stretch"><div><div class="section-head rv"><h2>{t["sup_h"]}</h2></div><div class="support" style="grid-template-columns:1fr">{sup}</div></div>
<div class="sup-media"><div class="hero-img" style="aspect-ratio:auto;min-height:420px;height:100%">{img(t["sup_img"][0], t["sup_img"][1], 1080, 1350)}</div>
<span class="chip sup-chip" aria-hidden="true">{icon("check")}{sc["chip"]}</span>
<div class="bubble sup-bubble" aria-hidden="true"><div class="bh"><i>H</i><span>{sc["h"]}<small>{sc["sub"]}</small></span></div>
<div class="msg in">{sc["q"]}</div><div class="msg out">{sc["a"]}</div></div></div></div></section>'''

    body = hero + picker + story + tour + bento + types_sec + plans + ai + stats_sec + support
    return {"key":"home","title":t["title"],"desc":t["desc"],"body":body,"preload_img":"/assets/img/brand-courtyard.webp","faq":FAQ_CORE,"schema":[software_schema(L)]}
