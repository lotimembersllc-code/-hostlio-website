"""v4 SEO/GEO pages: property-type landing pages, comparison page, two guides (TR + EN)."""
from build import btn, icon, url, SIGNUP_URL, SITE, UPDATED, software_schema, LANGMOD
PV4 = {"tr": dict(trial="7 gün ücretsiz dene", demo="Demo iste", plan_h="Hangi plan uygun?", cmp_t='Diğer otel programlarıyla karşılaştırmak için <a href="{c}">otel programı karşılaştırması</a> sayfamıza bakın.', see_pricing="Fiyatları gör"),
       "en": dict(trial="Try it free for 7 days", demo="Book a demo", plan_h="Which plan fits?", cmp_t='To compare with other hotel software, see our <a href="{c}">hotel software comparison</a>.', see_pricing="See pricing"),
       **{l: m.PV4 for l, m in LANGMOD.items()}}

def _img(name, alt, w=720, h=900, eager=False):
    lz = "" if eager else ' loading="lazy"'
    fp = ' fetchpriority="high"' if eager else ""
    return f'<img src="/assets/img/{name}.webp" alt="{alt}" width="{w}" height="{h}"{lz}{fp} decoding="async">'

# ------------------------------------------------------------------ property types
TYPES = {
"tr": [
 dict(key="t-guesthouse", img=("gen-guesthouse", "Masa lambalı, sıcak bir pansiyon odası", 1080, 1350),
  title="Pansiyon Programı: AI Destekli, Aylık 49 $'dan | Hostlio Pro",
  desc="Pansiyonlar için otel programı: misafir mesajlarına 30+ dilde otomatik cevap, Booking.com ve Airbnb senkronu, online check-in. 7 gün ücretsiz deneyin.",
  crumb="Pansiyon programı", h1='Pansiyonlar için <em class="hl">otel programı</em>',
  lead="Tek kişilik ya da küçük bir ekiple işletilen pansiyonlarda gece gelen mesajlar, farklı kanallardaki rezervasyonlar ve check-in aynı kişinin işidir. Hostlio Pro bu yükü azaltır.",
  q="Pansiyon programı nedir?",
  a="Pansiyon programı, 1 ila 10 odalı küçük konaklama işletmelerinin rezervasyonlarını, müsaitliğini ve misafir iletişimini tek yerden yönetmesini sağlayan yazılımdır. Hostlio Pro bu işlevlere, misafir sorularını 30'dan fazla dilde 7/24 yanıtlayan AI asistanı Lio'yu ekler. Starter planı 10 odaya kadar tesisler için aylık 49 $'dır.",
  pains_h="Pansiyonlar en çok hangi sorunlarla uğraşır?",
  pains=[("Gece mesajları","Geç check-in, otopark, kahvaltı soruları gece yarısı gelir. Lio bu soruları misafirin dilinde yanıtlar, siz sabah özetini okursunuz."),
         ("Birden fazla kanal","Booking.com ve Airbnb'de aynı oda satılınca çift rezervasyon olur. Kanal yöneticisi müsaitliği anında eşitler."),
         ("Kimlik ve kayıt","Misafir bilgilerini resepsiyonda tek tek yazmak zaman alır. Online check-in bilgileri varıştan önce toplar."),
         ("Sınırlı bütçe","Komisyonlu yazılımlar doluluk arttıkça pahalanır. Hostlio Pro sabit aylık ücretle çalışır.")],
  plan="Çoğu pansiyon için <strong>Starter</strong> planı yeterlidir: 10 odaya kadar, aylık 1.000 AI mesajı ve WhatsApp AI mesajlaşma. Online check-in ve OTA gelen kutusu mesajlarını (Booking.com, Airbnb, Expedia) da Lio'ya devretmek isterseniz <strong>Pro</strong> planını seçin.",
  faq=[("Pansiyon programı ücretsiz mi?","Hostlio Pro'yu 7 gün ücretsiz deneyebilirsiniz. Sonrasında Starter planı aylık 49 $'dır (ilk 50 müşteriye özel erken kayıt fiyatı)."),
       ("3 odalı bir pansiyon için uygun mu?","Evet. Starter planı 1 tesis ve 10 odaya kadar tesisler için tasarlandı; oda sayısı az olsa da fiyat aynıdır."),
       ("Airbnb ve Booking.com'u birlikte kullanabilir miyim?","Evet. Hostlio Pro, Channex üzerinden iki kanalı ve 100'den fazla başka kanalı aynı takvimde senkronize eder.")]),
 dict(key="t-boutique", img=("gen-boutique-room", "Bugenvilli ve havuzlu butik otel avlusu", 1080, 1350),
  title="Butik Otel Programı: AI Asistan ve Kanal Yöneticisi | Hostlio Pro",
  desc="Butik oteller için otel programı: yabancı misafirlere 30+ dilde kişisel cevap, 100+ OTA senkronu, online check-in ve transfer satışı tek panelde.",
  crumb="Butik otel programı", h1='Butik oteller için <em class="hl">otel programı</em>',
  lead="Butik otelin farkı kişisel ilgidir. Hostlio Pro tekrar eden soruları üstlenir, ekibiniz misafire ayıracak zamanı kazanır.",
  q="Butik otel programı nedir?",
  a="Butik otel programı, genellikle 10 ila 50 odalı, kendine özgü konsepti olan otellerin rezervasyon, kanal ve misafir iletişimini yöneten otel yönetim yazılımıdır (PMS). Hostlio Pro'da AI asistanı Lio misafir mesajlarını otelin kendi bilgileriyle ve misafirin dilinde yanıtlar; kanal yöneticisi 100'den fazla OTA'yı senkronize eder.",
  pains_h="Butik oteller neden ayrı bir yazılıma ihtiyaç duyar?",
  pains=[("Çok dilli misafir","Misafirlerin önemli kısmı yabancıdır. Lio her mesaja misafirin dilinde, otelin tonunda cevap verir."),
         ("Ek gelir","Havalimanı transferi ve tur satışı butik otellerde önemli bir gelir kalemidir. Lio bu teklifleri doğru anda sunar."),
         ("Yoğun OTA trafiği","Booking.com, Expedia ve Airbnb'den gelen rezervasyonlar tek oda rafında, kanal renkleriyle görünür."),
         ("Hızlı check-in","Online check-in ve dijital imza sayesinde misafir lobide form doldurmak yerine hoş geldin içeceğini alır.")],
  plan="10 ila 50 odalı butik oteller için <strong>Pro</strong> planı önerilir: aylık 5.000 AI mesajı, WhatsApp ve OTA gelen kutusu mesajlaşması (Booking.com, Airbnb, Expedia), online check-in, transfer ve tur satışı ve iOS uygulaması.",
  faq=[("Butik otel için en iyi otel programı hangisi?","Seçim oda sayısına, misafir profiline ve bütçeye bağlıdır. Yabancı misafiri çok olan, sabit fiyat isteyen 10–50 odalı oteller için Hostlio Pro'nun AI mesajlaşması ve kanal yöneticisi iyi bir eşleşmedir. Diğer seçenekler için karşılaştırma sayfamıza bakın."),
       ("Hostlio Pro'yu mevcut web sitemle kullanabilir miyim?","Evet. Hostlio Pro mevcut web sitenizin yerine geçmez, onunla birlikte çalışır. Misafir mesajları WhatsApp ve OTA gelen kutularından (Booking.com, Airbnb, Expedia) tek panelde toplanır."),
       ("Kaç kullanıcı ekleyebilirim?","Plan detayları için fiyatlandırma sayfasına bakın veya demo sırasında ekibimize sorun.")]),
 dict(key="t-apart", img=("gen-apart", "Aydınlık, beyaz nevresimli apart daire", 1080, 1350),
  title="Apart Otel Programı: Online Check-in ve Kanal Yönetimi | Hostlio Pro",
  desc="Apart oteller ve kiralık daireler için otel programı: Airbnb ve Booking.com senkronu, online check-in ve dijital imza, 30+ dilde AI misafir mesajları.",
  crumb="Apart otel programı", h1='Apart oteller için <em class="hl">otel programı</em>',
  lead="Resepsiyonu olmayan ya da sınırlı saatlerde çalışan apart otellerde misafir iletişimi ve check-in uzaktan yürür. Hostlio Pro bunun için tasarlandı.",
  q="Apart otel programı nedir?",
  a="Apart otel programı, mutfaklı daire ve suit satan tesislerin rezervasyon, kanal ve misafir süreçlerini yöneten yazılımdır. Hostlio Pro'da misafir, online check-in bağlantısıyla kimlik bilgilerini ve imzasını varıştan önce gönderir; giriş talimatlarıyla ilgili sorular AI asistanı Lio tarafından 30+ dilde yanıtlanır.",
  pains_h="Apart otellerde en çok zaman alan işler nelerdir?",
  pains=[("Uzaktan check-in","Online check-in formu kimlik, refakatçi ve imzayı varıştan önce toplar."),
         ("Giriş talimatları","Anahtar teslimi, Wi-Fi ve otopark soruları tekrar eder. Lio bunları otel bilgilerinizden yanıtlar."),
         ("Kısa dönem kanallar","Airbnb ve Booking.com müsaitliği Channex üzerinden anında eşitlenir."),
         ("Uzun konaklamalar","Oda rafında konaklamayı uzatmak ya da daire değiştirmek sürükle-bırak ile yapılır.")],
  plan="Online check-in Pro ve Growth planlarında vardır, bu yüzden apart oteller için <strong>Pro</strong> planı önerilir. İki tesis işletiyorsanız <strong>Growth</strong> planına bakın.",
  faq=[("Resepsiyonsuz apart otelde Hostlio Pro işe yarar mı?","Evet. Online check-in ve AI mesajlaşma, resepsiyonun yaptığı bilgi toplama ve soru yanıtlama işini uzaktan yapar."),
       ("Airbnb mesajlarını da yanıtlıyor mu?","Pro ve Growth planlarında OTA mesajları, Airbnb dahil, Lio'nun gelen kutusuna düşer."),
       ("Daire sayısı sınırı var mı?","Starter 10, Pro 50, Growth 150 oda veya daireye kadar destekler.")]),
 dict(key="t-hostel", img=("gen-hostel", "Ahşap panelli, ortak alanlı konaklama lobisi", 1080, 1350),
  title="Hostel Programı: Çok Dilli Mesajlar, OTA Senkronu | Hostlio Pro",
  desc="Hosteller için otel programı: Hostelworld, Booking.com ve 100+ kanal senkronu, 30+ dilde AI misafir mesajları ve online check-in. 7 gün ücretsiz.",
  crumb="Hostel programı", h1='Hosteller için <em class="hl">otel programı</em>',
  lead="Hostellerde misafir profili uluslararası, mesaj trafiği yüksek, ekip küçüktür. Hostlio Pro çok dilli soruları üstlenir ve kanalları tek takvimde tutar.",
  q="Hostel programı nedir?",
  a="Hostel programı, yatak ve oda bazlı satış yapan hostellerin rezervasyon, kanal ve misafir iletişimini yöneten yazılımdır. Hostlio Pro, Hostelworld dahil 100'den fazla kanala Channex üzerinden bağlanır ve misafir sorularını AI asistanı Lio ile 30+ dilde yanıtlar.",
  pains_h="Hostellerde öne çıkan ihtiyaçlar nelerdir?",
  pains=[("Çok dilli trafik","Farklı ülkelerden gelen gezginler kendi dillerinde yazar. Lio her dilde cevap verir."),
         ("Hostelworld ve OTA'lar","Hostelworld, Booking.com ve diğer kanallar tek müsaitlikle yönetilir."),
         ("Tur ve transfer","Şehir turu ve havalimanı transferi hostellerde yaygın ek gelirdir; Lio doğru anda sunar."),
         ("Gece vardiyası","Gece gelen sorular sabaha kalmaz; ekip yalnızca karar gerektiren konulara bakar.")],
  plan="Mesaj trafiği yüksek hosteller için aylık 5.000 AI mesajı sunan <strong>Pro</strong> planı önerilir. Yatak bazlı kurulum detaylarını demo sırasında birlikte netleştirelim.",
  faq=[("Hostelworld ile çalışıyor mu?","Evet. Hostelworld, Channex'in bağlı kanalları arasındadır."),
       ("Yatak bazlı (dorm) satış destekleniyor mu?","Kurulumunuza göre değişir; oda ve yatak yapınızı demo sırasında birlikte planlayalım."),
       ("Kaç AI mesajı yeterli olur?","Günde ortalama 150 otomatik yanıt, aylık yaklaşık 4.500 mesaj eder; bu durumda Pro planı uygundur.")]),
],
"en": [
 dict(key="t-guesthouse", img=("gen-guesthouse", "A warm guesthouse room with a desk lamp", 1080, 1350),
  title="Guesthouse Software with an AI Guest Assistant | Hostlio Pro",
  desc="Guesthouse management software: automatic guest replies in 30+ languages, Booking.com and Airbnb sync and online check-in. From $49/month, 7 days free.",
  crumb="Guesthouse software", h1='<em class="hl">Guesthouse software</em> that answers guests for you',
  lead="In a guesthouse, one person handles late-night messages, bookings on several channels and check-in. Hostlio Pro takes load off that person.",
  q="What is guesthouse software?",
  a="Guesthouse software lets small properties with 1 to 10 rooms manage reservations, availability and guest communication in one place. Hostlio Pro adds Lio, an AI assistant that answers guest questions 24/7 in more than 30 languages. The Starter plan costs $49 a month for properties with up to 10 rooms.",
  pains_h="What do guesthouses struggle with most?",
  pains=[("Night messages","Late check-in, parking and breakfast questions arrive at midnight. Lio answers in the guest's language and you read a summary in the morning."),
         ("Several channels","Selling the same room on Booking.com and Airbnb causes double bookings. The channel manager syncs availability instantly."),
         ("ID and registration","Typing guest details at the desk takes time. Online check-in collects them before arrival."),
         ("Tight budget","Commission-based software gets pricier as occupancy grows. Hostlio Pro is a flat monthly fee.")],
  plan="For most guesthouses the <strong>Starter</strong> plan is enough: up to 10 rooms, 1,000 AI messages a month and WhatsApp AI messaging. Choose <strong>Pro</strong> if you also want online check-in and Lio handling OTA inbox messages (Booking.com, Airbnb, Expedia).",
  faq=[("Is there free guesthouse software?","You can try Hostlio Pro free for 7 days. After that, Starter is $49 a month (early-bird price for the first 50 customers)."),
       ("Does it suit a 3-room guesthouse?","Yes. Starter is designed for one property with up to 10 rooms; the price is the same with fewer rooms."),
       ("Can I use Airbnb and Booking.com together?","Yes. Hostlio Pro syncs both, plus 100+ other channels, on one calendar through Channex.")]),
 dict(key="t-boutique", img=("gen-boutique-room", "Boutique hotel courtyard with a pool and bougainvillea", 1080, 1350),
  title="Boutique Hotel Software with AI Guest Messaging | Hostlio Pro",
  desc="Boutique hotel management software: personal replies to international guests in 30+ languages, sync with 100+ OTAs, online check-in and transfer sales.",
  crumb="Boutique hotel software", h1='<em class="hl">Boutique hotel software</em> built around the guest',
  lead="What sets a boutique hotel apart is personal attention. Hostlio Pro takes over repetitive questions so your team has more time for guests.",
  q="What is boutique hotel software?",
  a="Boutique hotel software is a hotel management system (PMS) for hotels with around 10 to 50 rooms and a distinctive concept. In Hostlio Pro, the AI assistant Lio answers guest messages with the hotel's own information and in the guest's language, and the channel manager keeps 100+ OTAs in sync.",
  pains_h="Why do boutique hotels need dedicated software?",
  pains=[("Multilingual guests","Many guests come from abroad. Lio answers each message in the guest's language and your hotel's tone."),
         ("Extra revenue","Airport transfers and tours matter for boutique hotels. Lio offers them at the right moment."),
         ("Heavy OTA traffic","Bookings from Booking.com, Expedia and Airbnb appear on one room rack, colour-coded by channel."),
         ("Fast check-in","With online check-in and a digital signature, guests get a welcome drink instead of a form.")],
  plan="For boutique hotels with 10 to 50 rooms we recommend <strong>Pro</strong>: 5,000 AI messages a month, WhatsApp + OTA inbox messaging (Booking.com, Airbnb, Expedia), online check-in, transfer and tour sales and the iOS app.",
  faq=[("What is the best software for a boutique hotel?","It depends on room count, guest profile and budget. For 10–50 room hotels with many international guests that want flat pricing, Hostlio Pro's AI messaging and channel manager are a good fit. See our comparison page for other options."),
       ("Can I use Hostlio Pro with my existing website?","Yes. Hostlio Pro works alongside your existing website rather than replacing it. Guest messages from WhatsApp and OTA inboxes (Booking.com, Airbnb, Expedia) come together in one dashboard."),
       ("How many users can I add?","See the pricing page for plan details, or ask our team during the demo.")]),
 dict(key="t-apart", img=("gen-apart", "Bright apartment with white bedding", 1080, 1350),
  title="Aparthotel Software: Online Check-in and Channel Sync | Hostlio Pro",
  desc="Aparthotel and serviced apartment software: Airbnb and Booking.com sync, online check-in with digital signature and AI guest messaging in 30+ languages.",
  crumb="Aparthotel software", h1='<em class="hl">Aparthotel software</em> for remote-first operations',
  lead="Aparthotels often have no front desk or limited hours, so guest communication and check-in happen remotely. Hostlio Pro is built for that.",
  q="What is aparthotel software?",
  a="Aparthotel software manages reservations, channels and guest processes for properties that sell apartments and suites with kitchens. In Hostlio Pro, guests send ID details and a signature through an online check-in link before arrival, and the AI assistant Lio answers access questions in 30+ languages.",
  pains_h="What takes the most time in an aparthotel?",
  pains=[("Remote check-in","The online check-in form collects ID, companions and a signature before arrival."),
         ("Access instructions","Key handover, Wi-Fi and parking questions repeat. Lio answers them from your property information."),
         ("Short-stay channels","Airbnb and Booking.com availability syncs instantly through Channex."),
         ("Longer stays","Extending a stay or moving apartments is drag and drop on the room rack.")],
  plan="Online check-in is included in Pro and Growth, so we recommend <strong>Pro</strong> for aparthotels. If you run two properties, look at <strong>Growth</strong>.",
  faq=[("Does Hostlio Pro work for an aparthotel without a front desk?","Yes. Online check-in and AI messaging handle the information gathering and question answering a front desk would do, remotely."),
       ("Does it answer Airbnb messages?","On Pro and Growth, OTA messages, including Airbnb, land in Lio's inbox."),
       ("Is there a unit limit?","Starter supports up to 10, Pro 50 and Growth 150 rooms or units.")]),
 dict(key="t-hostel", img=("gen-hostel", "Lobby with wood panelling and shared seating", 1080, 1350),
  title="Hostel Software: Multilingual Messaging, OTA Sync | Hostlio Pro",
  desc="Hostel management software: Hostelworld, Booking.com and 100+ channel sync, AI guest messaging in 30+ languages and online check-in. 7 days free.",
  crumb="Hostel software", h1='<em class="hl">Hostel software</em> for busy, multilingual inboxes',
  lead="Hostels have international guests, high message volume and small teams. Hostlio Pro handles multilingual questions and keeps channels on one calendar.",
  q="What is hostel software?",
  a="Hostel software manages reservations, channels and guest communication for hostels that sell beds and rooms. Hostlio Pro connects to 100+ channels including Hostelworld through Channex and answers guest questions in 30+ languages with its AI assistant Lio.",
  pains_h="What do hostels need most?",
  pains=[("Multilingual traffic","Travellers write in their own languages. Lio replies in each of them."),
         ("Hostelworld and OTAs","Hostelworld, Booking.com and other channels share one availability."),
         ("Tours and transfers","City tours and airport transfers are common extras in hostels; Lio offers them at the right moment."),
         ("Night shift","Night-time questions don't wait until morning; staff only handle what needs a decision.")],
  plan="For high-volume hostels we recommend <strong>Pro</strong> with 5,000 AI messages a month. Let's plan your bed-based setup together during the demo.",
  faq=[("Does it work with Hostelworld?","Yes. Hostelworld is among Channex's connected channels."),
       ("Is bed-based (dorm) selling supported?","It depends on your setup; let's plan your room and bed structure together during the demo."),
       ("How many AI messages do I need?","About 150 automatic replies a day is roughly 4,500 a month, which fits the Pro plan.")]),
]}

for _l, _m in LANGMOD.items(): TYPES[_l] = _m.types(lambda k, _l=_l: url(k, _l))

def type_page(L, d):
    U = lambda k: url(k, L)
    rows = "".join(f'<div class="row"><h3>{h}</h3><div><p>{p}</p></div></div>' for h,p in d["pains"])
    im = d["img"]; w, h = (im[2], im[3]) if len(im) > 2 else (720, 900)
    pv = PV4[L]; trial, demo, plan_h = pv["trial"], pv["demo"], pv["plan_h"]
    cmp_t = pv["cmp_t"].format(c=U("compare"))
    body = f'''<section class="page-hero"><div class="wrap split"><div><h1>{d["h1"]}</h1><p class="lead">{d["lead"]}</p>
<div class="cta-row">{btn(trial, SIGNUP_URL)}{btn(demo, U("contact"), "ghost")}</div></div>
<div class="hero-img">{_img(im[0], im[1], w, h, eager=True)}</div></div></section>
<section class="white rule"><div class="wrap">
<div class="answer"><h2 style="font-size:var(--t-1);margin-bottom:.4em">{d["q"]}</h2><p>{d["a"]}</p></div>
<h2 style="margin-top:64px">{d["pains_h"]}</h2><div class="rows">{rows}</div>
<h2 style="margin-top:64px">{plan_h}</h2><p class="lead" style="font-size:var(--t-0)">{d["plan"]}</p>
<p>{cmp_t}</p><div class="cta-row">{btn(pv["see_pricing"], U("pricing"), "ghost")}</div>
</div></section>'''
    return {"key": d["key"], "title": d["title"], "desc": d["desc"], "trail": [(d["crumb"], U(d["key"]))],
            "body": body, "faq": d["faq"], "preload_img": f"/assets/img/{im[0]}.webp", "schema": [software_schema(L)]}

# ------------------------------------------------------------------ comparison
CMP_SOURCES = [
 ("Hostlio Pro", "https://hostliopro.com/fiyatlandirma/"),
 ("Cloudbeds", "https://www.cloudbeds.com/pricing/"),
 ("Mews", "https://www.mews.com/en/pricing"),
 ("Little Hotelier", "https://www.littlehotelier.com/pricing/"),
 ("HotelRunner", "https://www.hotelrunner.com/tr/fiyatlandirma"),
]
CMP = {
"tr": dict(
  title="Otel Programı Karşılaştırması 2026: Fiyat, Komisyon, AI | Hostlio Pro",
  desc="Hostlio Pro, Cloudbeds, Mews, Little Hotelier ve HotelRunner karşılaştırması: yayınlanan fiyatlar, başlangıç fiyatı, komisyon, deneme süresi ve AI mesajlaşma.",
  crumb="Otel programı karşılaştırması", h1='Otel programı <em class="hl">karşılaştırması</em> (2026)',
  lead="Bağımsız oteller için beş popüler otel yönetim yazılımını, firmaların kendi fiyatlandırma sayfalarında yayınladığı bilgilere göre karşılaştırdık.",
  q="Hangi otel programı daha uygun?",
  a="Kısa cevap: tek tesisli, 10–150 odalı ve yabancı misafiri çok olan oteller için sabit fiyatlı ve AI mesajlaşması dahil bir yazılım (Hostlio Pro gibi) bütçeyi öngörülebilir kılar. Çok tesisli ve kurumsal ihtiyaçları olan gruplar için Mews veya Cloudbeds gibi teklif bazlı platformlar, Türkiye'de B2B ağı ve yerel destek arayanlar için HotelRunner, SiteMinder ağıyla çalışmak isteyen küçük tesisler için Little Hotelier değerlendirilebilir.",
  cols=["Yazılım","Fiyatlar yayınlanıyor mu?","Başlangıç","Rezervasyon komisyonu","Ücretsiz deneme","AI misafir mesajlaşması"],
  rows=[("Hostlio Pro","Evet","49 $/ay (erken kayıt)","Yok, sabit aylık ücret","7 gün","Tüm planlarda (Lio, 30+ dil)"),
        ("Cloudbeds","Hayır, teklif usulü","Teklif","Booking Engine ve Channel Manager rezervasyonlarından ek komisyon almadığını belirtiyor","Fiyat sayfasında belirtilmiyor","Fiyat sayfasında ayrıca belirtilmiyor"),
        ("Mews","Hayır, teklif usulü","Teklif","Fiyat sayfasında belirtilmiyor","Fiyat sayfasında belirtilmiyor","Advanced planda AI misafir tercih özetleri; mesajlaşma ayrıca belirtilmiyor"),
        ("Little Hotelier","Oda sayısına göre hesaplanıyor","Fiyat hesaplayıcısıyla","Basics planında %1 rezervasyon ücreti","30 gün","Fiyat sayfasında belirtilmiyor"),
        ("HotelRunner","Evet (temel paketler)","19,95 $/ay + %0,75 (Manage)","%0,75 ile %1,25 arası (pakete göre)","Var","Advanced \"Automate\" paketinde")],
  when_h="Hangi durumda hangisi?",
  when=[("Hostlio Pro","Tek tesis ya da iki tesis, 10–150 oda, yabancı misafir trafiği yüksek, sabit aylık bütçe isteyen oteller."),
        ("Cloudbeds ve Mews","Birden fazla tesis, gelir yönetimi ve geniş entegrasyon pazarı gibi kurumsal ihtiyaçları olan gruplar."),
        ("HotelRunner","Türkiye'de yerel destek, B2B satış ağı ve komisyonlu, düşük sabit ücretli model tercih eden tesisler."),
        ("Little Hotelier","SiteMinder altyapısıyla çalışmak isteyen, oda sayısına göre fiyatlandırmayı kabul eden küçük tesisler.")],
  note="Bilgiler 21 Eylül 2026 tarihinde firmaların fiyatlandırma sayfalarından derlenmiştir; fiyat ve paketler değişebilir. Güncel bilgi için her firmanın kendi sayfasını kontrol edin. Hostlio Pro bu karşılaştırmada taraflıdır; tabloyu yalnızca yayınlanmış bilgilere dayandırdık.",
  src_h="Kaynaklar",
  faq=[("Otel programı nedir?","Otel programı (otel yönetim yazılımı, PMS), bir konaklama tesisinin rezervasyonlarını, oda müsaitliğini, satış kanallarını ve misafir bilgilerini tek yerden yönetmesini sağlayan yazılımdır."),
       ("Otel programı fiyatları ne kadar?","Yayınlanmış fiyatlara göre aylık yaklaşık 20 $ ile 150 $ arasında başlayan paketler var; bazı yazılımlar buna rezervasyon başı %0,75–1,25 komisyon ekler, bazıları ise yalnızca teklif verir."),
       ("Komisyonlu mu sabit fiyatlı mı daha avantajlı?","Doluluk ve ortalama oda fiyatı arttıkça komisyonlu modelin maliyeti büyür. Bütçesini sabitlemek isteyen oteller için sabit aylık ücret daha öngörülebilirdir.")]),
"en": dict(
  title="Hotel Software Comparison 2026: Pricing, Fees, AI | Hostlio Pro",
  desc="Hostlio Pro, Cloudbeds, Mews, Little Hotelier and HotelRunner compared: published pricing, starting price, booking fees, free trial and AI guest messaging.",
  crumb="Hotel software comparison", h1='Hotel software <em class="hl">comparison</em> (2026)',
  lead="We compared five popular hotel management systems for independent hotels, using only what each vendor publishes on its own pricing page.",
  q="Which hotel software is right for you?",
  a="Short answer: for single-property hotels with 10–150 rooms and many international guests, flat-priced software with AI messaging included (like Hostlio Pro) keeps the budget predictable. Multi-property groups with enterprise needs may consider quote-based platforms such as Mews or Cloudbeds; properties in Turkey wanting local support and a B2B network may look at HotelRunner; small properties that want the SiteMinder network may consider Little Hotelier.",
  cols=["Software","Published pricing?","Starting at","Booking fee","Free trial","AI guest messaging"],
  rows=[("Hostlio Pro","Yes","$49/month (early bird)","None, flat monthly fee","7 days","All plans (Lio, 30+ languages)"),
        ("Cloudbeds","No, quote-based","Quote","States no added commission on Booking Engine and Channel Manager reservations","Not stated on pricing page","Not separately stated on pricing page"),
        ("Mews","No, quote-based","Quote","Not stated on pricing page","Not stated on pricing page","AI guest-preference summaries on Advanced; messaging not separately stated"),
        ("Little Hotelier","Calculated by room count","Via price calculator","1% booking fee on Basics","30 days","Not stated on pricing page"),
        ("HotelRunner","Yes (core plans)","$19.95/month + 0.75% (Manage)","0.75% to 1.25% depending on plan","Available","In the Advanced \"Automate\" tier")],
  when_h="Which one, when?",
  when=[("Hostlio Pro","One or two properties, 10–150 rooms, heavy international guest traffic and a fixed monthly budget."),
        ("Cloudbeds and Mews","Multi-property groups with enterprise needs such as revenue management and a large integration marketplace."),
        ("HotelRunner","Properties in Turkey that want local support, a B2B sales network and a low fixed fee plus commission."),
        ("Little Hotelier","Small properties that want the SiteMinder infrastructure and accept room-count-based pricing.")],
  note="Information compiled on September 21, 2026 from each vendor's pricing page; prices and plans can change, so check each vendor's page for current details. Hostlio Pro is a party to this comparison; we based the table only on published information.",
  src_h="Sources",
  faq=[("What is hotel management software?","Hotel management software (a PMS) lets a property manage reservations, room availability, sales channels and guest information in one place."),
       ("How much does hotel software cost?","Based on published prices, plans start at roughly $20 to $150 a month; some vendors add a 0.75–1.25% booking fee, and others only give quotes."),
       ("Is a commission or a flat fee better?","As occupancy and average rates rise, commission-based costs grow. A flat monthly fee is more predictable for hotels that want a fixed budget.")]),
}

for _l, _m in LANGMOD.items(): CMP[_l] = _m.cmp(lambda k, _l=_l: url(k, _l))

def compare_page(L):
    d = CMP[L]; U = lambda k: url(k, L)
    head = "".join(f"<th>{c}</th>" for c in d["cols"])
    rows = "".join("<tr>" + f'<th scope="row">{r[0]}</th>' + "".join(f"<td>{c}</td>" for c in r[1:]) + "</tr>" for r in d["rows"])
    when = "".join(f'<div class="row"><h3>{h}</h3><div><p>{p}</p></div></div>' for h,p in d["when"])
    src = "".join(f'<li><a href="{u}" rel="nofollow noopener">{n}</a></li>' for n,u in CMP_SOURCES)
    body = f'''<section class="page-hero"><div class="wrap"><h1>{d["h1"]}</h1><p class="lead">{d["lead"]}</p></div></section>
<section style="padding-top:0"><div class="wrap">
<div class="answer"><h2 style="font-size:var(--t-1);margin-bottom:.4em">{d["q"]}</h2><p>{d["a"]}</p></div>
<div class="table-wrap" style="margin-top:40px"><table><caption class="sr-only">{d["h1"].replace('<em class="hl">','').replace('</em>','')}</caption><thead><tr>{head}</tr></thead><tbody>{rows}</tbody></table></div>
<p class="small muted" style="margin-top:14px">{d["note"]}</p>
<h2 style="margin-top:64px">{d["when_h"]}</h2><div class="rows">{when}</div>
<h2 style="margin-top:48px;font-size:var(--t-1)">{d["src_h"]}</h2><ul>{src}</ul>
</div></section>'''
    return {"key":"compare","title":d["title"],"desc":d["desc"],"trail":[(d["crumb"], U("compare"))],"body":body,"faq":d["faq"]}

# ------------------------------------------------------------------ guides
GUIDES = {
"tr": [
 dict(key="post-overbooking", date="2026-09-21", title="Overbooking nasıl önlenir? Oteller için 6 adım",
  desc="Otellerde overbooking (çift rezervasyon) neden olur ve nasıl önlenir? Kanal yöneticisi, stop-sell, müsaitlik tamponu ve kriz anında yapılacaklar.",
  content='''<div class="answer"><p><strong>Kısa cevap:</strong> Overbooking, aynı oda için satılabilecek olandan fazla rezervasyon alınmasıdır. Bağımsız otellerde en sık sebebi, birden fazla OTA'da müsaitliğin elle güncellenmesidir. Çift yönlü, anlık çalışan bir kanal yöneticisi kullanmak riski büyük ölçüde ortadan kaldırır.</p></div>
<h2>Overbooking neden olur?</h2>
<ul><li>Booking.com, Airbnb ve Expedia'daki müsaitliğin ayrı ayrı, elle güncellenmesi</li><li>Telefon veya walk-in rezervasyonların sisteme geç girilmesi</li><li>İptal ve değişikliklerin bir kanala yansıyıp diğerine yansımaması</li><li>Kanallar arasında gecikmeli (saatlik) senkronizasyon</li></ul>
<h2>6 adımda overbooking'i önleyin</h2>
<ol><li><strong>Tek müsaitlik kaynağı kullanın.</strong> Tüm kanallar müsaitliği tek bir takvimden (PMS) almalı.</li>
<li><strong>Çift yönlü, anlık senkron seçin.</strong> Rezervasyon geldiğinde diğer kanallarda oda saniyeler içinde kapanmalı.</li>
<li><strong>Direkt rezervasyonu hemen girin.</strong> Telefon ve walk-in satışlarını aynı takvime anında işleyin.</li>
<li><strong>Stop-sell ve minimum konaklama kurallarını tek yerden yönetin.</strong> Kanal kanal değiştirmek hata doğurur.</li>
<li><strong>Yoğun dönemlerde küçük bir tampon bırakın.</strong> Son odayı yalnızca direkt kanala açmak riski azaltır.</li>
<li><strong>Kanal eşlemelerini düzenli kontrol edin.</strong> Yeni oda tipi eklediğinizde tüm kanallarda eşleşmeyi doğrulayın.</li></ol>
<h2>Overbooking olursa ne yapılır?</h2>
<p>Misafire hemen ve dürüstçe bilgi verin, eşdeğer ya da daha iyi bir alternatif (yakın otel, oda yükseltme) sunun ve transfer gibi ek maliyetleri üstlenin. Olayın hangi kanaldan ve neden kaynaklandığını kaydedin.</p>
<h2>Hostlio Pro'da nasıl çalışır?</h2>
<p>Hostlio Pro'nun <a href="/kanal-yoneticisi/">kanal yöneticisi</a>, Channex altyapısıyla 100'den fazla kanalda müsaitliği çift yönlü ve anlık senkronize eder. Rezervasyonlar kanal renkleriyle tek oda rafında görünür.</p>''',
  faq=[("Overbooking ne demek?","Overbooking, bir otelin aynı tarih ve oda için satabileceğinden fazla rezervasyon almasıdır; Türkçede çift rezervasyon olarak da bilinir."),
       ("Kanal yöneticisi overbooking'i tamamen önler mi?","Anlık, çift yönlü senkron riski büyük ölçüde azaltır; ancak elle girilmeyen direkt rezervasyonlar ve hatalı oda eşlemeleri yine sorun çıkarabilir.")]),
 dict(key="post-autoreply", date="2026-09-21", title="Booking.com mesajlarına otomatik cevap nasıl verilir?",
  desc="Booking.com misafir mesajlarını otomatik yanıtlamanın üç yolu: hazır şablonlar, planlı mesajlar ve yapay zekâ asistanı. Hangisi ne zaman işe yarar?",
  content='''<div class="answer"><p><strong>Kısa cevap:</strong> Booking.com mesajlarını otomatikleştirmenin üç yolu vardır: extranet'teki hazır mesaj şablonları, rezervasyon aşamasına göre planlanan mesajlar ve misafirin sorusunu anlayıp otel bilgileriyle cevap veren bir yapay zekâ asistanı. Şablonlar standart bilgiler için, AI asistanı ise her misafirin farklı sorusu için uygundur.</p></div>
<h2>1. Hazır mesaj şablonları</h2>
<p>Check-in saati, yol tarifi ve otopark gibi sık sorulan bilgileri şablon olarak kaydedip tek tıkla gönderebilirsiniz. Avantajı basit olmasıdır; dezavantajı, mesajı yine birinin okuyup doğru şablonu seçmesi gerekmesidir.</p>
<h2>2. Planlı mesajlar</h2>
<p>Rezervasyondan hemen sonra, varıştan bir gün önce ya da çıkış günü otomatik gönderilen mesajlar. Misafir soru sormadan bilgilendirilir; ancak misafirin sonradan yazdığı sorulara cevap vermez.</p>
<h2>3. Yapay zekâ asistanı</h2>
<p>Misafirin mesajını okuyup otelin bilgi tabanından, misafirin dilinde cevap üretir. Gece gelen, farklı dillerde yazılan ve şablona uymayan sorular için en etkili yöntemdir. Karar gerektiren mesajları (indirim, şikâyet) personele devretmesi gerekir.</p>
<div class="table-wrap"><table><thead><tr><th>Yöntem</th><th>Ne zaman işe yarar?</th><th>Sınırı</th></tr></thead><tbody>
<tr><td>Hazır şablonlar</td><td>Standart bilgiler</td><td>Birinin okuyup seçmesi gerekir</td></tr>
<tr><td>Planlı mesajlar</td><td>Varış öncesi bilgilendirme</td><td>Gelen sorulara cevap vermez</td></tr>
<tr><td>AI asistanı</td><td>Her saatte, her dilde gelen sorular</td><td>İyi bir bilgi tabanı gerektirir</td></tr></tbody></table></div>
<h2>Cevap süresi neden önemli?</h2>
<p>Misafir rezervasyon öncesi sorusuna hızlı cevap aldığında karar vermesi kolaylaşır; konaklama sırasında hızlı cevap ise memnuniyeti ve yorumları etkiler.</p>
<h2>Hostlio Pro'da nasıl çalışır?</h2>
<p>Pro ve Growth planlarında Booking.com dahil OTA mesajları <a href="/ai-misafir-asistani/">AI asistanı Lio</a>'nun gelen kutusuna düşer. Lio otel bilgilerinizle, misafirin dilinde yanıtlar; emin olmadığı mesajları size bırakır.</p>''',
  faq=[("Booking.com mesajlarına otomatik cevap verilebilir mi?","Evet. Extranet şablonları ve planlı mesajlar Booking.com'un kendi araçlarıdır; soruya özel otomatik cevap için mesajları okuyan bir AI asistanı gerekir."),
       ("AI asistanı yanlış bilgi verir mi?","Yalnızca otelin girdiği bilgilerle çalışan ve emin olmadığında personele devreden bir asistanda risk düşüktür.")]),
],
"en": [
 dict(key="post-overbooking", date="2026-09-21", title="How to prevent overbooking: 6 steps for hotels",
  desc="Why hotels get overbooked and how to prevent it: channel manager, stop-sell rules, availability buffers and what to do when it happens anyway.",
  content='''<div class="answer"><p><strong>Short answer:</strong> Overbooking means accepting more reservations than you can host for the same room and dates. In independent hotels the most common cause is updating availability by hand on several OTAs. A two-way, real-time channel manager removes most of the risk.</p></div>
<h2>Why does overbooking happen?</h2>
<ul><li>Updating availability on Booking.com, Airbnb and Expedia separately, by hand</li><li>Entering phone or walk-in bookings late</li><li>Cancellations and changes reaching one channel but not another</li><li>Delayed (hourly) sync between channels</li></ul>
<h2>Prevent overbooking in 6 steps</h2>
<ol><li><strong>Use one source of availability.</strong> Every channel should read availability from one calendar (your PMS).</li>
<li><strong>Choose two-way, real-time sync.</strong> When a booking arrives, the room should close on other channels within seconds.</li>
<li><strong>Enter direct bookings immediately.</strong> Add phone and walk-in sales to the same calendar right away.</li>
<li><strong>Manage stop-sells and minimum stays in one place.</strong> Changing them channel by channel invites mistakes.</li>
<li><strong>Keep a small buffer in peak periods.</strong> Opening the last room only to your direct channel lowers the risk.</li>
<li><strong>Check channel mappings regularly.</strong> When you add a room type, confirm the mapping on every channel.</li></ol>
<h2>What if it happens anyway?</h2>
<p>Tell the guest promptly and honestly, offer an equal or better alternative (a nearby hotel, an upgrade) and cover extra costs such as transfers. Log which channel caused it and why.</p>
<h2>How it works in Hostlio Pro</h2>
<p>Hostlio Pro's <a href="/en/channel-manager/">channel manager</a> syncs availability two-way and in real time across 100+ channels through Channex. Bookings appear on one room rack, colour-coded by channel.</p>''',
  faq=[("What does overbooking mean?","Overbooking is when a hotel accepts more reservations than it can host for the same room and dates, also called a double booking."),
       ("Does a channel manager fully prevent overbooking?","Real-time two-way sync removes most of the risk; direct bookings that aren't entered and wrong room mappings can still cause problems.")]),
 dict(key="post-autoreply", date="2026-09-21", title="How to auto-reply to Booking.com guest messages",
  desc="Three ways to automate Booking.com guest messages: templates, scheduled messages and an AI assistant. When each one works, and where it falls short.",
  content='''<div class="answer"><p><strong>Short answer:</strong> There are three ways to automate Booking.com messages: saved message templates in the extranet, scheduled messages tied to the booking stage, and an AI assistant that understands the guest's question and answers from your hotel information. Templates suit standard information; an AI assistant suits the questions that differ for every guest.</p></div>
<h2>1. Message templates</h2>
<p>Save frequent answers like check-in time, directions and parking as templates and send them in one click. They're simple, but someone still has to read the message and pick the right template.</p>
<h2>2. Scheduled messages</h2>
<p>Messages sent automatically after booking, a day before arrival or on departure day. Guests are informed before they ask, but these don't answer questions guests write later.</p>
<h2>3. An AI assistant</h2>
<p>It reads the guest's message and writes a reply from your knowledge base in the guest's language. It works best for night-time, multilingual and off-template questions, and it should hand decisions (discounts, complaints) to staff.</p>
<div class="table-wrap"><table><thead><tr><th>Method</th><th>Works best for</th><th>Limit</th></tr></thead><tbody>
<tr><td>Templates</td><td>Standard information</td><td>Someone must read and choose</td></tr>
<tr><td>Scheduled messages</td><td>Pre-arrival information</td><td>Doesn't answer incoming questions</td></tr>
<tr><td>AI assistant</td><td>Questions at any hour, in any language</td><td>Needs a good knowledge base</td></tr></tbody></table></div>
<h2>Why response time matters</h2>
<p>A fast answer before booking makes the guest's decision easier; a fast answer during the stay shapes satisfaction and reviews.</p>
<h2>How it works in Hostlio Pro</h2>
<p>On Pro and Growth, OTA messages including Booking.com land in the inbox of <a href="/en/ai-guest-messaging/">Lio, the AI assistant</a>. Lio answers with your hotel information in the guest's language and leaves what it isn't sure about to you.</p>''',
  faq=[("Can you auto-reply to Booking.com messages?","Yes. Extranet templates and scheduled messages are Booking.com's own tools; question-specific automatic replies need an AI assistant that reads messages."),
       ("Can an AI assistant give wrong information?","The risk is low when the assistant only uses information the hotel provides and hands uncertain questions to staff.")]),
]}

for _l, _m in LANGMOD.items(): GUIDES[_l] = _m.guides(lambda k, _l=_l: url(k, _l))

def guides(L, article):
    return [article({"key": g["key"], "title": g["title"], "date": g["date"], "desc": g["desc"]}, g["content"], g["faq"]) for g in GUIDES[L]]

def pages(L, article):
    return [type_page(L, d) for d in TYPES[L]] + [compare_page(L)] + guides(L, article)
