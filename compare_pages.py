"""Karşılaştırma merkezi ve "Hostlio vs X" / "X alternatifleri" sayfaları (SEO raporu bölüm 8, #8–#12).

DÜRÜSTLÜK KURALI: rakip hakkındaki her bilgi rakibin RESMİ sayfasında 8 Ekim 2026'da doğrulandı; kaynak URL'leri
SRC'de, sayfada "Kaynaklar" listesinde ve scratchpad/site_karsi.md'de. Doğrulanamayan bilgi YAZILMAZ.
Rakip fiyatı/özelliği değişince: SRC tarihini ve ilgili hücreyi birlikte güncelleyin (3 ayda bir kontrol).
Hostlio tarafı yalnız canlı özellikler (WEB_SITE_DUZELTMELER.md §2–4); fiyatlar ⟦token⟧ (pricing.py).
"""
import html
import pricing

CHECKED = "2026-10-08"
SRC = {
    "hr_en": ("HotelRunner: Pricing", "https://hotelrunner.com/en/pricing/"),
    "hr_tr": ("HotelRunner: Fiyatlandırma", "https://hotelrunner.com/tr/fiyatlandirma/"),
    "hr_cm": ("HotelRunner: Channel manager", "https://hotelrunner.com/en/products/channel-manager/"),
    "cb_pr": ("Cloudbeds: Pricing", "https://www.cloudbeds.com/pricing/"),
    "cb_home": ("Cloudbeds: Home", "https://www.cloudbeds.com/"),
    "cb_ge": ("Cloudbeds: Guest engagement", "https://www.cloudbeds.com/guest-engagement-software/"),
    "am_en": ("Amenitiz: Pricing", "https://amenitiz.com/en/pricing"),
    "am_fr": ("Amenitiz : Nos tarifs", "https://amenitiz.com/fr/nos-tarifs"),
    "am_cm": ("Amenitiz: Channel manager", "https://amenitiz.com/en/product/channel-manager"),
    "hj_pr": ("HiJiffy: Plans and pricing", "https://www.hijiffy.com/plans-and-pricing"),
    "hj_home": ("HiJiffy: Home", "https://www.hijiffy.com/"),
    "sv_pr": ("Sirvoy: Pricing", "https://sirvoy.com/pricing"),
    "b24_pr": ("Beds24: Pricing", "https://beds24.com/pricing.html"),
    "ev_pr": ("eviivo: Pricing", "https://eviivo.com/pricing/"),
}

# HotelRunner Essential Sell: aylık gerçekleşen rezervasyon geliri × %1,25, asgari $29,95 (resmi SSS formülü)
def hr_sell_fee(revenue): return max(29.95, revenue * 0.0125)
BREAK_EVEN_PRO = round(pricing.monthly("pro") / 0.0125)          # Pro aylık ücreti = Sell ücreti olduğu gelir
BREAK_EVEN_STARTER = round(pricing.monthly("starter") / 0.0125)
HR_EXAMPLES = [2000, 5000, 10000, 20000]

C = {
"tr": dict(col_f="", col_h="Hostlio Pro", checked="8 Ekim 2026'da kontrol edildi", src_h="Kaynaklar", asof="Ekim 2026 itibarıyla",
  note="Rakip bilgileri yalnızca firmaların kendi resmî sayfalarından alınmıştır ve {d} tarihinde kontrol edilmiştir; fiyat ve paketler değişebilir. Hostlio Pro bu karşılaştırmada taraftır. Bir bilgiyi doğrulayamadığımızda tabloya yazmadık. Hata görürseniz <a href=\"{contact}\">bize yazın</a>, düzeltelim.",
  trial="7 gün ücretsiz dene", pricing="Planları gör", more_h="Diğer karşılaştırmalar", fit_h="Hostlio Pro nerede öne çıkar?", switch_h="Hostlio Pro'ya geçiş nasıl olur?",
  hub_link="Tüm karşılaştırmalar", tools="Ücretsiz otel hesaplayıcıları"),
"en": dict(col_f="", col_h="Hostlio Pro", checked="Checked on October 8, 2026", src_h="Sources", asof="As of October 2026",
  note="Competitor information comes only from each company's own official pages and was checked on {d}; prices and plans can change. Hostlio Pro is a party to this comparison. Where we couldn't verify something, we left it out. Spotted a mistake? <a href=\"{contact}\">Tell us</a> and we'll fix it.",
  trial="Try it free for 7 days", pricing="See plans", more_h="More comparisons", fit_h="Where Hostlio Pro fits", switch_h="How switching to Hostlio Pro works",
  hub_link="All comparisons", tools="Free hotel calculators"),
"es": dict(col_f="", col_h="Hostlio Pro", checked="Comprobado el 8 de octubre de 2026", src_h="Fuentes", asof="A octubre de 2026",
  note="La información de la competencia procede solo de las páginas oficiales de cada empresa y se comprobó el {d}; los precios y planes pueden cambiar. Hostlio Pro es parte interesada en esta comparativa. Lo que no pudimos verificar, no lo incluimos. ¿Ves un error? <a href=\"{contact}\">Escríbenos</a> y lo corregimos.",
  trial="Pruébalo gratis 7 días", pricing="Ver planes", more_h="Más comparativas", fit_h="Dónde encaja Hostlio Pro", switch_h="Cómo es el cambio a Hostlio Pro",
  hub_link="Todas las comparativas", tools="Calculadoras hoteleras gratis"),
"pt": dict(col_f="", col_h="Hostlio Pro", checked="Verificado em 8 de outubro de 2026", src_h="Fontes", asof="Em outubro de 2026",
  note="As informações sobre concorrentes vêm apenas das páginas oficiais de cada empresa e foram verificadas em {d}; preços e planos podem mudar. O Hostlio Pro é parte interessada nesta comparação. O que não conseguimos confirmar, deixamos de fora. Viu um erro? <a href=\"{contact}\">Fale com a gente</a> e corrigimos.",
  trial="Teste grátis por 7 dias", pricing="Ver planos", more_h="Mais comparativos", fit_h="Onde o Hostlio Pro se encaixa", switch_h="Como é a migração para o Hostlio Pro",
  hub_link="Todos os comparativos", tools="Calculadoras gratuitas para hotéis"),
"fr": dict(col_f="", col_h="Hostlio Pro", checked="Vérifié le 8 octobre 2026", src_h="Sources", asof="En octobre 2026",
  note="Les informations sur les concurrents proviennent uniquement de leurs pages officielles et ont été vérifiées le {d} ; prix et offres peuvent changer. Hostlio Pro est partie prenante de ce comparatif. Ce que nous n’avons pas pu vérifier n’y figure pas. Vous voyez une erreur ? <a href=\"{contact}\">Écrivez-nous</a>, nous la corrigerons.",
  trial="Essai gratuit de 7 jours", pricing="Voir les forfaits", more_h="Autres comparatifs", fit_h="Où Hostlio Pro se distingue", switch_h="Passer à Hostlio Pro : comment ça se passe",
  hub_link="Tous les comparatifs", tools="Calculateurs gratuits pour hôtels"),
}
SRC_ONE = {"tr": "kaynak", "en": "source", "es": "fuente", "pt": "fonte", "fr": "source"}
DATE_TXT = {"tr": "8 Ekim 2026", "en": "October 8, 2026", "es": "8 de octubre de 2026", "pt": "8 de outubro de 2026", "fr": "8 octobre 2026"}

# Hostlio Pro tarafı (yalnız canlı özellikler)
HL = {
"tr": dict(price="Sabit aylık ücret: Starter ⟦price:starter⟧, Pro ⟦price:pro⟧, Growth ⟦price:growth⟧ (USD, erken kayıt fiyatı); yıllık ödemede %20 indirim",
  fee="Hostlio rezervasyon başına ücret ya da gelir yüzdesi almaz", trial="7 gün (kart kayıtta alınır, deneme bitene kadar ücret çekilmez)",
  ai="AI asistan Lio tüm planlarda WhatsApp'ta; Pro ve Growth'ta Booking.com, Airbnb ve Expedia gelen kutuları da", wa="Tüm planlarda (Lio)",
  cm="Tüm planlarda, 100+ OTA'ya sertifikalı bağlantı", rooms="Starter 10, Pro 50, Growth 150 oda (Growth: 2 tesis)", users="Starter 3, Pro 8, Growth 20 kullanıcı",
  checkin="Pro ve Growth'ta: kimlik/pasaport MRZ okuma, dijital imza", be="Yok; Hostlio Pro PMS, kanal yöneticisi ve AI mesajlaşmaya odaklanır",
  pay="Yok; ödeme tahsilatı yapılmaz", lang="Panel 6 dilde; destek Türkçe ve İngilizce", analytics="Doluluk, ADR, RevPAR; kanal bazında brüt, komisyon ve net gelir"),
"en": dict(price="Flat monthly fee: Starter ⟦price:starter⟧, Pro ⟦price:pro⟧, Growth ⟦price:growth⟧ (USD, early-bird); 20% off with annual billing",
  fee="No per-booking fee or revenue percentage from Hostlio", trial="7 days (card at signup, no charge until the trial ends)",
  ai="Lio AI assistant on WhatsApp on every plan; Booking.com, Airbnb and Expedia inboxes too on Pro and Growth", wa="All plans (Lio)",
  cm="All plans, certified connections to 100+ OTAs", rooms="Starter 10, Pro 50, Growth 150 rooms (Growth: 2 properties)", users="Starter 3, Pro 8, Growth 20 users",
  checkin="Pro and Growth: ID/passport MRZ reading, digital signature", be="Not included; Hostlio Pro focuses on PMS, channel manager and AI messaging",
  pay="Not included; no payment collection", lang="Dashboard in 6 languages; support in English and Turkish", analytics="Occupancy, ADR, RevPAR; gross, commission and net revenue per channel"),
"es": dict(price="Cuota mensual fija: Starter ⟦price:starter⟧, Pro ⟦price:pro⟧, Growth ⟦price:growth⟧ (USD, precio de lanzamiento); 20 % de descuento en pago anual",
  fee="Hostlio no cobra por reserva ni un porcentaje de ingresos", trial="7 días (tarjeta al registrarse, sin cargo hasta que termina la prueba)",
  ai="El asistente IA Lio en WhatsApp en todos los planes; en Pro y Growth también las bandejas de Booking.com, Airbnb y Expedia", wa="Todos los planes (Lio)",
  cm="Todos los planes, conexiones certificadas con más de 100 OTAs", rooms="Starter 10, Pro 50, Growth 150 habitaciones (Growth: 2 alojamientos)", users="Starter 3, Pro 8, Growth 20 usuarios",
  checkin="Pro y Growth: lectura MRZ de DNI/pasaporte, firma digital", be="No incluido; Hostlio Pro se centra en PMS, channel manager y mensajería con IA",
  pay="No incluido; no cobra pagos", lang="Panel en 6 idiomas (incluido español); soporte en inglés y turco", analytics="Ocupación, ADR, RevPAR; ingresos brutos, comisión y netos por canal"),
"pt": dict(price="Mensalidade fixa: Starter ⟦price:starter⟧, Pro ⟦price:pro⟧, Growth ⟦price:growth⟧ (USD, preço early bird); 20% de desconto no plano anual",
  fee="O Hostlio não cobra por reserva nem percentual da receita", trial="7 dias (cartão no cadastro, sem cobrança até o fim do teste)",
  ai="Assistente de IA Lio no WhatsApp em todos os planos; no Pro e no Growth também as caixas de entrada do Booking.com, Airbnb e Expedia", wa="Todos os planos (Lio)",
  cm="Todos os planos, conexões certificadas com mais de 100 OTAs", rooms="Starter 10, Pro 50, Growth 150 quartos (Growth: 2 propriedades)", users="Starter 3, Pro 8, Growth 20 usuários",
  checkin="Pro e Growth: leitura MRZ de documento/passaporte, assinatura digital", be="Não incluído; o Hostlio Pro se concentra em PMS, channel manager e mensagens com IA",
  pay="Não incluído; não processa pagamentos", lang="Painel em 6 idiomas (inclui português); suporte em inglês e turco", analytics="Ocupação, ADR, RevPAR; receita bruta, comissão e líquida por canal"),
"fr": dict(price="Abonnement mensuel fixe : Starter ⟦price:starter⟧, Pro ⟦price:pro⟧, Growth ⟦price:growth⟧ (USD, tarif early bird) ; −20 % en paiement annuel",
  fee="Aucun frais par réservation ni pourcentage du chiffre d’affaires", trial="7 jours (carte à l’inscription, aucun prélèvement avant la fin de l’essai)",
  ai="L’assistant IA Lio sur WhatsApp dans tous les forfaits ; en Pro et Growth, aussi les messageries Booking.com, Airbnb et Expedia", wa="Tous les forfaits (Lio)",
  cm="Tous les forfaits, connexions certifiées à plus de 100 OTA", rooms="Starter 10, Pro 50, Growth 150 chambres (Growth : 2 établissements)", users="Starter 3, Pro 8, Growth 20 utilisateurs",
  checkin="Pro et Growth : lecture MRZ de la pièce d’identité/du passeport, signature numérique", be="Non inclus ; Hostlio Pro se concentre sur le PMS, le channel manager et la messagerie IA",
  pay="Non inclus ; pas d’encaissement", lang="Tableau de bord en 6 langues (dont le français) ; support en anglais et en turc", analytics="Taux d’occupation, ADR, RevPAR ; revenu brut, commission et net par canal"),
}

def _usd(n, lang):
    """HotelRunner örnekleri USD; 2 ondalık gerekiyorsa yaz."""
    s = f"{n:,.2f}" if not float(n).is_integer() else f"{int(n):,}"
    if lang == "en": return "$" + s
    if lang == "fr": return s.replace(",", " ").replace(".", ",") + " $"
    s = s.replace(",", "X").replace(".", ",").replace("X", ".")
    return ("$" + s) if lang in ("tr", "pt") else (s + " $")

def hr_table(lang):
    hd = {"tr": ("Aylık rezervasyon geliri", "HotelRunner Essential Sell (%1,25, asgari $29,95)", "Hostlio Pro"),
          "en": ("Monthly booking revenue", "HotelRunner Essential Sell (1.25%, min. $29.95)", "Hostlio Pro")}[lang]
    rows = "".join(f'<tr><th scope="row" class="num">{_usd(r, lang)}</th><td class="num">{_usd(round(hr_sell_fee(r), 2), lang)}</td><td class="num">⟦price:pro⟧</td></tr>' for r in HR_EXAMPLES)
    return (f'<div class="table-wrap" style="margin-top:16px"><table><thead><tr>{"".join(f"<th>{h}</th>" for h in hd)}</tr></thead><tbody>{rows}</tbody></table></div>')

# ---------------------------------------------------------------- page content
P = {}

P["vs-hotelrunner"] = {
"tr": dict(
  card="Hostlio Pro ile HotelRunner: sabit aylık ücret mi, gelir yüzdesi mi?",
  title="Hostlio Pro vs HotelRunner (2026): Fiyat, AI | Hostlio Pro",
  desc="Hostlio Pro ve HotelRunner karşılaştırması: sabit aylık ücret ile rezervasyon gelirinden yüzde, AI misafir mesajlaşması, WhatsApp ve hangisi kime uygun.",
  crumb="Hostlio Pro vs HotelRunner", h1='Hostlio Pro vs <em class="hl">HotelRunner</em>',
  lead="İkisi de bağımsız tesisler için bulut tabanlı yazılım. En büyük fark ödeme modelinde: Hostlio Pro sabit aylık ücret alır, HotelRunner'ın Essential planları ise asgari aylık ücretle birlikte rezervasyon gelirinin bir yüzdesini alır. Aşağıdaki karşılaştırma her iki firmanın yayınladığı bilgilere dayanır.",
  answer="<strong>Kısa cevap:</strong> Sabit, gelirle büyümeyen bir aylık ücret ve her planda misafirlere WhatsApp'tan cevap veren bir AI asistan istiyorsanız Hostlio Pro uygundur. Aynı platformda rezervasyon motoru ve web sitesi, online ödeme tahsilatı ya da acente (B2B) dağıtımı istiyorsanız veya çok kullanıcılı büyük bir tesis işletiyorsanız HotelRunner daha uygun olabilir.",
  rows=[("Fiyat modeli", "price", "Essential planlar: tüm kanallardan gelen aylık gerçekleşen rezervasyon gelirinin yüzdesi, asgari aylık ücretle"),
        ("Yayınlanan fiyatlar", "Evet, fiyatlandırma sayfasında", "Essential Manage aylık %0,75 (asgari $19,95), Sell %1,25 (asgari $29,95), Complete %1 (asgari $39,95). Advanced ve Elite: satış ekibiyle görüşme"),
        ("Rezervasyon başı ücret", "fee", "Essential planlarda gelir yüzdesi (yukarıda)"),
        ("Kanal yöneticisi", "cm", "Sell ve Complete planlarında; \"150+ kanal\""),
        ("Rezervasyon motoru ve web sitesi", "be", "Sell ve Complete planlarında"),
        ("AI misafir mesajlaşması", "ai", "Konuşma yöneticisi, AI asistan ve AI çeviri, Advanced planlardaki Misafir İlişkileri Yönetimi'nde listeleniyor (fiyat satış ekibinden)"),
        ("WhatsApp ile misafir mesajlaşması", "wa", "İncelediğimiz fiyat ve ürün sayfalarında belirtilmiyor"),
        ("Oda ve kullanıcı", "Oda: Starter 10, Pro 50, Growth 150. Kullanıcı: 3 / 8 / 20", "Essential planlarda sınırsız oda ve sınırsız kullanıcı"),
        ("Ücretsiz deneme", "trial", "\"Ücretsiz deneyin\" seçeneği var; süresi fiyat sayfasında belirtilmiyor"),
        ("Destek", "Türkçe ve İngilizce", "Tüm planlarda mesaj, e-posta ve telefon desteği")],
  srcs=["hr_tr", "hr_en", "hr_cm"],
  calc_h="Hangisi daha ekonomik? Gelire göre örnek hesap",
  calc_p="HotelRunner'ın SSS'sinde yayınlanan formüle göre Essential Sell planında aylık ücret, tüm kanallardan gerçekleşen rezervasyon gelirinin %1,25'idir; bu tutar $29,95'in altında kalırsa asgari ücret ödenir. Hostlio Pro planı ise gelirden bağımsız olarak sabittir. Aşağıdaki rakamlar bizim hesabımızdır; OTA komisyonları ve vergiler hariçtir, iki ürünün kapsamı da aynı değildir.",
  calc_after=f"Bu formüle göre aylık rezervasyon geliriniz yaklaşık {_usd(BREAK_EVEN_PRO, 'tr')}'ın altındaysa Essential Sell ücreti Hostlio Pro'dan düşük, üstündeyse yüksek olur. Starter için bu eşik yaklaşık {_usd(BREAK_EVEN_STARTER, 'tr')}'dır.",
  fit=[("Bütçe sezonla büyümez", "Yüksek sezonda geliriniz artsa da Hostlio Pro'nun aylık ücreti değişmez. Kanal yöneticisi, oda rafı ve AI asistan aynı pakette."),
       ("Her planda WhatsApp'ta AI asistan", "Lio, misafir sorularını otelinizin bilgileriyle ve misafirin dilinde yanıtlar; indirim, şikâyet gibi karar gerektiren mesajları size bırakır. Pro ve Growth'ta OTA gelen kutuları da Lio'ya bağlanır ve Lio WhatsApp'ta rezervasyon talebi toplar, talep sizin onayınızla rezervasyona dönüşür."),
       ("Her sabah öneri, net rakamlar", "Lio Önerileri her sabah fiyat ve operasyon önerisi getirir; onayınız olmadan hiçbir şey değişmez. Analiz ekranı doluluk, ADR, RevPAR ile kanal bazında brüt, komisyon ve net geliri gösterir."),
       ("Kolay geçiş", "Mevcut rezervasyonlarınızı CSV ya da Excel dosyasıyla içeri aktarırsınız; kurulum sihirbazı eksik bilgileri işaretler.")],
  better_h="HotelRunner hangi durumda daha uygun?",
  better=[("Rezervasyon motoru ve web sitesi gerekiyorsa", "HotelRunner'ın Sell planı kanal yöneticisinin yanında rezervasyon motoru, web sitesi, merkezi rezervasyon sistemi ve meta arama içerir. Hostlio Pro bunları sunmaz."),
          ("Ödemeyi platformda almak istiyorsanız", "HotelRunner online ödeme ve ödeme bağlantısı gibi ödeme özelliklerini listeler. Hostlio Pro ödeme tahsil etmez."),
          ("Çok kullanıcılı, çok odalı tesisler", "Essential planlarda oda ve kullanıcı sınırı yoktur; Hostlio Pro'da Growth planı 150 oda ve 20 kullanıcıyla sınırlıdır."),
          ("Acente (B2B) satışı önemliyse", "HotelRunner acente ağı ve sözleşme yönetimi gibi B2B araçları sunar."),
          ("Rezervasyon geliriniz düşükse", f"Aylık geliri yaklaşık {_usd(BREAK_EVEN_STARTER, 'tr')}'ın altında kalan küçük bir tesis için yüzdeye dayalı model daha ucuza gelebilir.")],
  switch=["7 günlük denemeyi başlatın; oda tiplerinizi ve fiyatlarınızı girin.", "Mevcut rezervasyonlarınızı CSV ya da Excel dosyasıyla aktarın (sütun eşleme ve mükerrer kontrolü dahil).",
          "Kanallarınızı Hostlio Pro'ya bağlayın. Müsaitliğin tek sistemden güncellenmesi için eski kanal yöneticisinden çıkış saatini önceden planlayın.",
          "Lio'nun otel bilgilerini doldurun ve \"Lio'yu dene\" ile birkaç misafir sorusu deneyin."],
  faq=[("HotelRunner komisyonlu mu çalışıyor?", "HotelRunner'ın fiyatlandırma sayfasına göre Essential planlarda aylık ücret, tüm kanallardan gerçekleşen rezervasyon gelirinin bir yüzdesidir (%0,75–%1,25) ve her planın asgari aylık tutarı vardır ($19,95–$39,95). Advanced ve Elite planlarının fiyatı satış ekibinden alınır."),
       ("Hostlio Pro komisyon alıyor mu?", "Hayır. Hostlio Pro sabit aylık ücretlidir ve rezervasyon başına ücret ya da gelir yüzdesi almaz. OTA'ların kendi komisyonları her iki durumda da ayrıca geçerlidir."),
       ("Hangisi daha ucuz?", f"Gelirinize bağlı. HotelRunner'ın yayınladığı formüle göre Essential Sell ücreti, aylık rezervasyon geliri yaklaşık {_usd(BREAK_EVEN_PRO, 'tr')} olduğunda Hostlio Pro planının aylık ücretine (⟦price:pro⟧) eşit olur; bunun üstünde HotelRunner, altında Hostlio Pro daha pahalıdır. Kapsamlar farklı olduğu için yalnızca fiyata bakmayın."),
       ("HotelRunner'dan Hostlio Pro'ya rezervasyonlarımı taşıyabilir miyim?", "Evet. Rezervasyonlarınızı CSV ya da Excel dosyası olarak dışa aktarıp Hostlio Pro'ya içe aktarabilirsiniz; içe aktarma sütun eşleme, tarih biçimi seçimi ve mükerrer kayıt kontrolü içerir.")]),
"en": dict(
  card="Hostlio Pro vs HotelRunner: flat monthly fee or a share of revenue?",
  title="Hostlio Pro vs HotelRunner (2026): Pricing, AI | Hostlio Pro",
  desc="Hostlio Pro vs HotelRunner: a flat monthly fee vs a percentage of booking revenue, AI guest messaging, WhatsApp and which one fits your property.",
  crumb="Hostlio Pro vs HotelRunner", h1='Hostlio Pro vs <em class="hl">HotelRunner</em>',
  lead="Both are cloud software for independent properties. The biggest difference is how you pay: Hostlio Pro charges a flat monthly fee, while HotelRunner's Essential plans charge a percentage of booking revenue with a monthly minimum. This comparison is based on what each company publishes.",
  answer="<strong>Short answer:</strong> choose Hostlio Pro if you want a fixed monthly price that doesn't grow with revenue and an AI assistant that answers guests on WhatsApp on every plan. HotelRunner may fit better if you need a booking engine and website, online payment collection or travel-agency (B2B) distribution in the same platform, or run a large property with many users.",
  rows=[("Pricing model", "price", "Essential plans: a percentage of monthly realized booking revenue from all channels, with a monthly minimum"),
        ("Published prices", "Yes, on the pricing page", "Essential Manage 0.75% a month (min. $19.95), Sell 1.25% (min. $29.95), Complete 1% (min. $39.95). Advanced and Elite: talk to sales"),
        ("Per-booking fees", "fee", "Revenue percentage on Essential plans (above)"),
        ("Channel manager", "cm", "On Sell and Complete; \"150+ channels\""),
        ("Booking engine and website", "be", "On Sell and Complete"),
        ("AI guest messaging", "ai", "Conversation manager, AI assistant and AI translation are listed under Guest Relationship Management in the Advanced plans (priced by sales)"),
        ("WhatsApp guest messaging", "wa", "Not stated on the pricing and product pages we checked"),
        ("Rooms and users", "Rooms: Starter 10, Pro 50, Growth 150. Users: 3 / 8 / 20", "Unlimited rooms and unlimited users on Essential plans"),
        ("Free trial", "trial", "\"Start free trial\" offered; length not stated on the pricing page"),
        ("Support", "English and Turkish", "Chat, email and phone support on all plans")],
  srcs=["hr_en", "hr_tr", "hr_cm"],
  calc_h="Which costs less? A worked example by revenue",
  calc_p="Under the formula in HotelRunner's pricing FAQ, the Essential Sell fee is 1.25% of monthly realized booking revenue from all channels, with $29.95 as the minimum. Hostlio Pro's plan price is fixed whatever your revenue. The numbers below are our own calculation; they exclude OTA commissions and taxes, and the two products don't cover exactly the same features.",
  calc_after=f"By this formula, below roughly {_usd(BREAK_EVEN_PRO, 'en')} of monthly booking revenue the Essential Sell fee is lower than Hostlio Pro's; above it, higher. For Starter the threshold is about {_usd(BREAK_EVEN_STARTER, 'en')}.",
  fit=[("A budget that doesn't grow with the season", "Your Hostlio Pro fee stays the same in high season. The channel manager, room rack and AI assistant come in one package."),
       ("An AI assistant on WhatsApp on every plan", "Lio answers guest questions with your hotel's information in the guest's language and leaves decisions such as discounts or complaints to you. On Pro and Growth, OTA inboxes are connected too, and Lio collects booking requests on WhatsApp that become reservations once you approve them."),
       ("Daily suggestions and clear numbers", "Lio Suggestions bring pricing and operations ideas every morning; nothing changes without your approval. Analytics shows occupancy, ADR, RevPAR and gross, commission and net revenue per channel."),
       ("An easy move", "Import your existing reservations from a CSV or Excel file; the setup wizard flags anything missing.")],
  better_h="When HotelRunner is a better fit",
  better=[("You need a booking engine and website", "HotelRunner's Sell plan includes a booking engine, website, central reservation system and metasearch next to the channel manager. Hostlio Pro doesn't offer these."),
          ("You want to collect payments in the platform", "HotelRunner lists online payment processing and payment links. Hostlio Pro doesn't collect payments."),
          ("Large teams and many rooms", "Essential plans have no room or user limit; Hostlio Pro's Growth plan stops at 150 rooms and 20 users."),
          ("Travel-agency (B2B) sales matter to you", "HotelRunner offers B2B tools such as agency networking and contracting."),
          ("Your booking revenue is low", f"For a small property earning under roughly {_usd(BREAK_EVEN_STARTER, 'en')} a month, a percentage-based plan can cost less.")],
  switch=["Start the 7-day trial and add your room types and rates.", "Import your existing reservations from CSV or Excel (with column mapping and duplicate checks).",
          "Connect your channels to Hostlio Pro. Plan the cut-over time with your old channel manager so availability is updated from one system only.",
          "Fill in Lio's hotel information and use \"Try Lio\" to test a few guest questions."],
  faq=[("Is HotelRunner commission-based?", "According to HotelRunner's pricing page, Essential plans charge a percentage (0.75%–1.25%) of monthly realized booking revenue from all channels, and each plan has a monthly minimum ($19.95–$39.95). Advanced and Elite plans are priced by the sales team."),
       ("Does Hostlio Pro charge a commission?", "No. Hostlio Pro is a flat monthly fee with no per-booking fee or revenue percentage. OTAs charge their own commission either way."),
       ("Which one is cheaper?", f"It depends on your revenue. By HotelRunner's published formula, the Essential Sell fee equals Hostlio Pro's monthly price (⟦price:pro⟧) at about {_usd(BREAK_EVEN_PRO, 'en')} of monthly booking revenue; above that HotelRunner costs more, below it Hostlio Pro does. The products differ in scope, so don't compare on price alone."),
       ("Can I move my reservations from HotelRunner?", "Yes. Export your reservations as a CSV or Excel file and import them into Hostlio Pro; the import supports column mapping, date-format selection and duplicate checks.")]),
}

P["vs-cloudbeds"] = {
"en": dict(
  card="Hostlio Pro vs Cloudbeds: published price vs quote, AI messaging",
  title="Hostlio Pro vs Cloudbeds (2026): Pricing, AI, Fit | Hostlio Pro",
  desc="Hostlio Pro vs Cloudbeds compared: published flat pricing vs quote-based plans, AI guest messaging and WhatsApp, and when each one is the better fit.",
  crumb="Hostlio Pro vs Cloudbeds", h1='Hostlio Pro vs <em class="hl">Cloudbeds</em>',
  lead="Cloudbeds is a broad hospitality platform for properties of every size; Hostlio Pro is a focused PMS, channel manager and AI guest assistant for independent properties of roughly 1–150 rooms. Here is how they compare, using only what each company publishes.",
  answer="<strong>Short answer:</strong> Hostlio Pro fits small and mid-sized independent properties that want to see the price before a sales call and have an AI assistant on WhatsApp in every plan. Cloudbeds fits properties that need a booking engine, integrated payments, a large integration marketplace or multi-property scale, and are happy to get a quote.",
  rows=[("Pricing", "price", "Quote-based: Flex, One, Experience and Enterprise plans all show \"Request a quote\""),
        ("Booking fees", "fee", "States it doesn't charge added commission on reservations made through its Booking Engine or Channel Manager; metasearch commissions apply after the stay"),
        ("Channel manager", "cm", "In the One plan and above (Flex lets you bring your own channel manager)"),
        ("Booking engine and payments", "be", "Booking Engine in One and above; Payments included with all plans"),
        ("AI guest messaging and WhatsApp", "ai", "AI chatbot and a unified inbox covering WhatsApp, SMS, email and OTA messages; on the pricing page Guest Experience is listed in the Experience plan"),
        ("Integrations", "Channel connections through Channex; Booking.com, Airbnb and Expedia inboxes", "\"400+ integration partners\" (pricing page)"),
        ("Free trial", "trial", "Not mentioned on the pricing page; demo offered"),
        ("Onboarding and support", "Setup wizard, CSV/Excel import; support in English and Turkish", "Self-serve or with an onboarding coach; 24/7 support")],
  srcs=["cb_pr", "cb_home", "cb_ge"],
  fit=[("You see the price up front", "Plans start at ⟦price:starter⟧ a month and are listed on the pricing page; you can start a 7-day trial without a sales call."),
       ("AI in every plan", "Lio answers guests on WhatsApp on every plan, with your hotel's information and in the guest's language. Pro and Growth add Booking.com, Airbnb and Expedia inboxes and booking requests that you approve."),
       ("Built for 1–150 rooms", "One calendar, a channel manager, online check-in (Pro and Growth), analytics with occupancy, ADR and RevPAR, and staff roles, without modules to assemble."),
       ("Easy to switch", "Import reservations from CSV or Excel; the setup wizard shows what's missing before you go live.")],
  better_h="When Cloudbeds is a better fit",
  better=[("You need a booking engine and payments", "Cloudbeds includes a Booking Engine (One and above) and Payments. Hostlio Pro offers neither a booking engine nor payment collection."),
          ("You rely on many third-party tools", "Cloudbeds lists 400+ integration partners in its marketplace."),
          ("You run a large portfolio", "Cloudbeds says it serves businesses of every size up to enterprise portfolios; Hostlio Pro's largest plan covers 2 properties and 150 rooms."),
          ("You want round-the-clock support", "Cloudbeds offers 24/7 support after onboarding. Hostlio Pro support is in English and Turkish, typically within 24 hours on business days.")],
  switch=["Start the 7-day trial and add your room types and rates.", "Export your reservations from Cloudbeds and import them as CSV or Excel.",
          "Connect your OTAs to Hostlio Pro; plan the cut-over so availability is sent from one system only.", "Fill in Lio's hotel information and test it with \"Try Lio\"."],
  faq=[("How much does Cloudbeds cost?", "Cloudbeds doesn't publish prices. Its pricing page lists four plans (Flex, One, Experience, Enterprise), each with \"Request a quote\"."),
       ("Does Cloudbeds include WhatsApp messaging?", "Cloudbeds' site describes a unified inbox that includes WhatsApp and an AI chatbot that can work via WhatsApp or SMS. On the pricing page, Guest Experience is listed in the Experience plan."),
       ("Is Hostlio Pro a full Cloudbeds replacement?", "For the PMS, channel manager and guest messaging, yes for many small properties. If you need a booking engine, payment processing or a large integration marketplace, Cloudbeds covers more."),
       ("How long does switching take?", "The account is ready in minutes and channels are usually connected the same day. Reservations can be imported from a CSV or Excel file.")]),
"es": dict(
  card="Hostlio Pro vs Cloudbeds: precio publicado o presupuesto, IA incluida",
  title="Hostlio Pro vs Cloudbeds (2026): precios e IA | Hostlio Pro",
  desc="Hostlio Pro frente a Cloudbeds: precio fijo publicado o planes con presupuesto, mensajería con IA y WhatsApp, y cuándo encaja mejor cada uno.",
  crumb="Hostlio Pro vs Cloudbeds", h1='Hostlio Pro vs <em class="hl">Cloudbeds</em>',
  lead="Cloudbeds es una plataforma hotelera amplia para alojamientos de cualquier tamaño; Hostlio Pro es un PMS, channel manager y asistente de IA centrado en alojamientos independientes de 1 a 150 habitaciones aproximadamente. Así se comparan, solo con lo que publica cada empresa.",
  answer="<strong>Respuesta corta:</strong> Hostlio Pro encaja con alojamientos independientes pequeños y medianos que quieren ver el precio antes de hablar con ventas y tener un asistente de IA en WhatsApp en todos los planes. Cloudbeds encaja con quien necesita motor de reservas, pagos integrados, un gran marketplace de integraciones o escala multipropiedad, y no le importa pedir presupuesto.",
  rows=[("Precio", "price", "Con presupuesto: los planes Flex, One, Experience y Enterprise muestran \"Request a quote\""),
        ("Comisiones", "fee", "Indica que no cobra comisión añadida por las reservas de su Booking Engine o Channel Manager; en metabuscadores cobra comisión tras la estancia"),
        ("Channel manager", "cm", "En el plan One y superiores (en Flex puedes usar tu propio channel manager)"),
        ("Motor de reservas y pagos", "be", "Booking Engine en One y superiores; Payments incluido en todos los planes"),
        ("Mensajería con IA y WhatsApp", "ai", "Chatbot con IA y bandeja unificada con WhatsApp, SMS, email y mensajes de OTAs; en la página de precios Guest Experience figura en el plan Experience"),
        ("Integraciones", "Conexiones de canal mediante Channex; bandejas de Booking.com, Airbnb y Expedia", "\"400+ integration partners\" (página de precios)"),
        ("Prueba gratis", "trial", "No se menciona en la página de precios; ofrece demo"),
        ("Puesta en marcha y soporte", "Asistente de configuración e importación CSV/Excel; soporte en inglés y turco", "Autoservicio o con un coach de onboarding; soporte 24/7")],
  srcs=["cb_pr", "cb_home", "cb_ge"],
  fit=[("Ves el precio desde el principio", "Los planes empiezan en ⟦price:starter⟧ al mes y están en la página de precios; puedes empezar una prueba de 7 días sin llamada comercial."),
       ("IA en todos los planes", "Lio responde a los huéspedes por WhatsApp en todos los planes, con la información de tu hotel y en su idioma. Pro y Growth añaden las bandejas de Booking.com, Airbnb y Expedia y solicitudes de reserva que tú apruebas."),
       ("Pensado para 1–150 habitaciones", "Un calendario, channel manager, check-in online (Pro y Growth), análisis con ocupación, ADR y RevPAR y roles de equipo, sin módulos que montar."),
       ("Cambio sencillo", "Importa reservas desde CSV o Excel; el asistente de configuración te muestra lo que falta antes de empezar.")],
  better_h="Cuándo encaja mejor Cloudbeds",
  better=[("Necesitas motor de reservas y pagos", "Cloudbeds incluye Booking Engine (One y superiores) y Payments. Hostlio Pro no ofrece motor de reservas ni cobro de pagos."),
          ("Usas muchas herramientas de terceros", "Cloudbeds anuncia más de 400 socios de integración en su marketplace."),
          ("Gestionas una cartera grande", "Cloudbeds dice atender a negocios de cualquier tamaño, hasta carteras enterprise; el plan mayor de Hostlio Pro cubre 2 alojamientos y 150 habitaciones."),
          ("Quieres soporte 24/7 en tu idioma", "Cloudbeds ofrece soporte 24/7 tras el onboarding. El soporte de Hostlio Pro es en inglés y turco, aunque el panel está en español.")],
  switch=["Empieza la prueba de 7 días y añade tus tipos de habitación y tarifas.", "Exporta tus reservas de Cloudbeds e impórtalas en CSV o Excel.",
          "Conecta tus OTAs a Hostlio Pro y planifica el cambio para que la disponibilidad salga de un solo sistema.", "Completa la información del hotel para Lio y pruébalo con \"Probar Lio\"."],
  faq=[("¿Cuánto cuesta Cloudbeds?", "Cloudbeds no publica precios. Su página de precios muestra cuatro planes (Flex, One, Experience, Enterprise), todos con \"Request a quote\"."),
       ("¿Cloudbeds incluye WhatsApp?", "La web de Cloudbeds describe una bandeja unificada que incluye WhatsApp y un chatbot con IA que puede funcionar por WhatsApp o SMS. En la página de precios, Guest Experience figura en el plan Experience."),
       ("¿Hostlio Pro sustituye por completo a Cloudbeds?", "Para PMS, channel manager y mensajería con huéspedes, sí en muchos alojamientos pequeños. Si necesitas motor de reservas, cobro de pagos o un gran marketplace de integraciones, Cloudbeds cubre más."),
       ("¿Cuánto tarda el cambio?", "La cuenta está lista en minutos y los canales suelen conectarse el mismo día. Las reservas se pueden importar desde un archivo CSV o Excel.")]),
"pt": dict(
  card="Hostlio Pro vs Cloudbeds: preço publicado ou orçamento, IA incluída",
  title="Hostlio Pro vs Cloudbeds (2026): preços e IA | Hostlio Pro",
  desc="Hostlio Pro x Cloudbeds: preço fixo publicado ou planos sob orçamento, mensagens com IA e WhatsApp, e quando cada um é a melhor escolha.",
  crumb="Hostlio Pro vs Cloudbeds", h1='Hostlio Pro vs <em class="hl">Cloudbeds</em>',
  lead="A Cloudbeds é uma plataforma ampla para hospedagens de todos os portes; o Hostlio Pro é um PMS, channel manager e assistente de IA focado em hotéis independentes de cerca de 1 a 150 quartos. Veja a comparação, só com o que cada empresa publica.",
  answer="<strong>Resposta curta:</strong> o Hostlio Pro serve para hotéis e pousadas independentes de pequeno e médio porte que querem ver o preço antes de falar com vendas e ter um assistente de IA no WhatsApp em todos os planos. A Cloudbeds serve para quem precisa de motor de reservas, pagamentos integrados, um grande marketplace de integrações ou escala multipropriedade, e aceita pedir orçamento.",
  rows=[("Preço", "price", "Sob orçamento: os planos Flex, One, Experience e Enterprise mostram \"Request a quote\""),
        ("Comissões", "fee", "Informa que não cobra comissão adicional nas reservas do seu Booking Engine ou Channel Manager; em metabuscadores cobra comissão após a estadia"),
        ("Channel manager", "cm", "No plano One e acima (no Flex você usa seu próprio channel manager)"),
        ("Motor de reservas e pagamentos", "be", "Booking Engine no One e acima; Payments incluído em todos os planos"),
        ("Mensagens com IA e WhatsApp", "ai", "Chatbot com IA e caixa de entrada unificada com WhatsApp, SMS, e-mail e mensagens de OTAs; na página de preços, Guest Experience aparece no plano Experience"),
        ("Integrações", "Conexões de canal via Channex; caixas de entrada do Booking.com, Airbnb e Expedia", "\"400+ integration partners\" (página de preços)"),
        ("Teste grátis", "trial", "Não mencionado na página de preços; oferece demonstração"),
        ("Implantação e suporte", "Assistente de configuração e importação CSV/Excel; suporte em inglês e turco", "Autoatendimento ou com um coach de onboarding; suporte 24/7")],
  srcs=["cb_pr", "cb_home", "cb_ge"],
  fit=[("Você vê o preço logo de início", "Os planos começam em ⟦price:starter⟧ por mês e estão na página de preços; dá para iniciar um teste de 7 dias sem ligação de vendas."),
       ("IA em todos os planos", "A Lio responde hóspedes no WhatsApp em todos os planos, com as informações do seu hotel e no idioma do hóspede. Pro e Growth incluem as caixas de entrada do Booking.com, Airbnb e Expedia e pedidos de reserva que você aprova."),
       ("Feito para 1–150 quartos", "Um calendário, channel manager, check-in online (Pro e Growth), análises com ocupação, ADR e RevPAR e perfis de equipe, sem módulos para montar."),
       ("Migração simples", "Importe reservas de um arquivo CSV ou Excel; o assistente de configuração mostra o que falta antes de começar.")],
  better_h="Quando a Cloudbeds é a melhor escolha",
  better=[("Você precisa de motor de reservas e pagamentos", "A Cloudbeds inclui Booking Engine (One e acima) e Payments. O Hostlio Pro não oferece motor de reservas nem processamento de pagamentos."),
          ("Você usa muitas ferramentas de terceiros", "A Cloudbeds anuncia mais de 400 parceiros de integração no marketplace."),
          ("Você administra um portfólio grande", "A Cloudbeds diz atender negócios de todos os portes, até portfólios enterprise; o maior plano do Hostlio Pro cobre 2 propriedades e 150 quartos."),
          ("Você quer suporte 24/7", "A Cloudbeds oferece suporte 24/7 após o onboarding. O suporte do Hostlio Pro é em inglês e turco, embora o painel esteja em português.")],
  switch=["Comece o teste de 7 dias e cadastre seus tipos de quarto e tarifas.", "Exporte suas reservas da Cloudbeds e importe em CSV ou Excel.",
          "Conecte suas OTAs ao Hostlio Pro e planeje a troca para que a disponibilidade saia de um só sistema.", "Preencha as informações do hotel para a Lio e teste com \"Testar a Lio\"."],
  faq=[("Quanto custa a Cloudbeds?", "A Cloudbeds não publica preços. A página de preços mostra quatro planos (Flex, One, Experience, Enterprise), todos com \"Request a quote\"."),
       ("A Cloudbeds tem WhatsApp?", "O site da Cloudbeds descreve uma caixa de entrada unificada que inclui WhatsApp e um chatbot com IA que funciona via WhatsApp ou SMS. Na página de preços, Guest Experience aparece no plano Experience."),
       ("O Hostlio Pro substitui totalmente a Cloudbeds?", "Para PMS, channel manager e mensagens com hóspedes, sim, em muitos hotéis pequenos. Se você precisa de motor de reservas, pagamentos ou de um grande marketplace de integrações, a Cloudbeds cobre mais."),
       ("Quanto tempo leva a migração?", "A conta fica pronta em minutos e os canais costumam ser conectados no mesmo dia. As reservas podem ser importadas de um arquivo CSV ou Excel.")]),
}

# Alternatifler listesi: yalnız resmî fiyat sayfasında doğrulanan ürünler
ALTS = {
"en": [("Hostlio Pro", "Flat monthly fee", "⟦price:starter⟧/month (Starter, early-bird)", "7 days", "Independent properties of 1–150 rooms that want an AI assistant on WhatsApp included", None),
       ("HotelRunner", "% of booking revenue with a monthly minimum (Essential)", "0.75% a month, min. $19.95 (Essential Manage)", "Offered; length not stated", "Properties that want a booking engine, website and payments in one platform", "hr_en"),
       ("Amenitiz", "Quote based on number of rooms", "Not published", "Not offered; free demo", "Independent hotels and B&Bs in Europe wanting an all-in-one system with website builder", "am_en"),
       ("Sirvoy", "Flat monthly fee by room tier", "Up to 10 rooms: €22 (Starter) or €79 (Pro, with channel manager) a month, monthly billing", "14 days", "Small hotels and B&Bs wanting a simple, published price", "sv_pr"),
       ("Beds24", "Pay as you go: base + per room + per channel link", "From €15.50/month", "Free trial available", "Budget-minded properties comfortable configuring a flexible system", "b24_pr"),
       ("eviivo", "From-price plus a per-booking fee", "From $50/month (single property, excl. taxes) + $0.50 per confirmed booking", "14 days (single property)", "Small accommodation businesses wanting an all-in-one system", "ev_pr")],
"es": [("Hostlio Pro", "Cuota mensual fija", "⟦price:starter⟧/mes (Starter, lanzamiento)", "7 días", "Alojamientos independientes de 1–150 habitaciones que quieren un asistente de IA en WhatsApp incluido", None),
       ("HotelRunner", "% de los ingresos por reservas con mínimo mensual (Essential)", "0,75 % al mes, mínimo 19,95 $ (Essential Manage)", "Disponible; duración no indicada", "Alojamientos que quieren motor de reservas, web y pagos en una plataforma", "hr_en"),
       ("Amenitiz", "Presupuesto según número de habitaciones", "No publicado", "No ofrece; demo gratuita", "Hoteles independientes y B&B en Europa que buscan un todo en uno con creador de webs", "am_en"),
       ("Sirvoy", "Cuota mensual fija por tramo de habitaciones", "Hasta 10 habitaciones: 22 € (Starter) o 79 € (Pro, con channel manager) al mes, pago mensual", "14 días", "Hoteles pequeños y B&B que quieren un precio sencillo y publicado", "sv_pr"),
       ("Beds24", "Pago por uso: base + por habitación + por conexión de canal", "Desde 15,50 €/mes", "Prueba gratuita disponible", "Alojamientos con presupuesto ajustado que no temen configurar un sistema flexible", "b24_pr"),
       ("eviivo", "Precio desde + tarifa por reserva", "Desde 50 $/mes (un alojamiento, sin impuestos) + 0,50 $ por reserva confirmada", "14 días (un alojamiento)", "Pequeños alojamientos que quieren un sistema todo en uno", "ev_pr")],
"pt": [("Hostlio Pro", "Mensalidade fixa", "⟦price:starter⟧/mês (Starter, early bird)", "7 dias", "Hotéis independentes de 1–150 quartos que querem um assistente de IA no WhatsApp incluído", None),
       ("HotelRunner", "% da receita de reservas com mínimo mensal (Essential)", "0,75% ao mês, mínimo US$ 19,95 (Essential Manage)", "Disponível; duração não informada", "Hotéis que querem motor de reservas, site e pagamentos numa só plataforma", "hr_en"),
       ("Amenitiz", "Orçamento conforme o número de quartos", "Não publicado", "Não oferece; demonstração gratuita", "Hotéis independentes e B&Bs na Europa que buscam um sistema completo com criador de sites", "am_en"),
       ("Sirvoy", "Mensalidade fixa por faixa de quartos", "Até 10 quartos: € 22 (Starter) ou € 79 (Pro, com channel manager) por mês, cobrança mensal", "14 dias", "Hotéis pequenos e B&Bs que querem um preço simples e publicado", "sv_pr"),
       ("Beds24", "Pague pelo uso: base + por quarto + por conexão de canal", "A partir de € 15,50/mês", "Teste grátis disponível", "Hospedagens com orçamento apertado que não se importam em configurar um sistema flexível", "b24_pr"),
       ("eviivo", "Preço a partir de + taxa por reserva", "A partir de US$ 50/mês (uma propriedade, sem impostos) + US$ 0,50 por reserva confirmada", "14 dias (uma propriedade)", "Pequenas hospedagens que querem um sistema completo", "ev_pr")],
}
ALT_COLS = {"en": ("Software", "Pricing model", "Published starting price", "Free trial (as stated)", "Often a good fit for", "Source"),
            "es": ("Software", "Modelo de precio", "Precio de partida publicado", "Prueba gratis (según la web)", "Suele encajar con", "Fuente"),
            "pt": ("Software", "Modelo de preço", "Preço inicial publicado", "Teste grátis (segundo o site)", "Costuma servir para", "Fonte")}

P["alt-cloudbeds"] = {
"en": dict(
  card="Cloudbeds alternatives for small hotels, with published prices",
  title="Cloudbeds Alternatives for Small Hotels (2026) | Hostlio Pro",
  desc="Cloudbeds alternatives for small and independent hotels: pricing models and published starting prices from official pages, plus how to choose. Checked Oct 2026.",
  crumb="Cloudbeds alternatives", h1='Cloudbeds <em class="hl">alternatives</em> for small hotels',
  lead="Cloudbeds publishes no prices and asks for a quote. If you'd rather compare published prices first, here are alternatives whose pricing we could verify on their own websites, including Hostlio Pro (our product).",
  answer="<strong>Short answer:</strong> for a small independent property, the main questions are how you pay (flat fee, per room or a share of revenue), whether the channel manager is included, and whether guest messaging is part of the plan. Hostlio Pro, Sirvoy and Beds24 publish flat or usage-based prices; HotelRunner charges a share of booking revenue; Amenitiz, like Cloudbeds, gives quotes.",
  cb_h="What Cloudbeds offers, in its own words",
  cb=["Four plans, Flex, One, Experience and Enterprise, all priced by quote.", "No added commission on reservations made through its Booking Engine or Channel Manager.",
      "Guest messaging with an AI chatbot and a unified inbox that includes WhatsApp, listed under Guest Experience in the Experience plan.", "\"400+ integration partners\", onboarding self-serve or with a coach, and 24/7 support."],
  why_h="Why small properties compare alternatives",
  why=["They want to see a price before booking a sales demo.", "They run 1–50 rooms and need fewer modules.", "They want guest messaging included rather than in a higher plan."],
  choose_h="How to choose",
  choose=["Write down your monthly booking revenue and room count, then work out the yearly cost under each pricing model.", "Check that the channel manager covers the OTAs you sell on.",
          "Decide whether you need a booking engine and payment collection in the same tool.", "Ask how guest messages from WhatsApp and OTA inboxes are handled, and in which plan.", "Use the free trial with your real rooms and rates before switching."],
  srcs=["cb_pr", "cb_ge", "hr_en", "am_en", "sv_pr", "b24_pr", "ev_pr"],
  faq=[("Is there a cheaper alternative to Cloudbeds?", "Cloudbeds doesn't publish prices, so a direct comparison needs a quote. Among alternatives with published prices, Beds24 starts from €15.50 a month, Sirvoy from €22 a month for up to 10 rooms (Starter), and Hostlio Pro from ⟦price:starter⟧ a month."),
       ("Which Cloudbeds alternative includes AI guest messaging?", "Hostlio Pro includes its AI assistant Lio on WhatsApp in every plan, and adds Booking.com, Airbnb and Expedia inboxes on Pro and Growth. For other products, check the plan details on their websites."),
       ("Can I move my data from Cloudbeds?", "Most systems let you export reservations. Hostlio Pro imports reservations from CSV or Excel files with column mapping and duplicate checks.")]),
"es": dict(
  card="Alternativas a Cloudbeds para hoteles pequeños, con precios publicados",
  title="Alternativas a Cloudbeds para hoteles pequeños | Hostlio Pro",
  desc="Alternativas a Cloudbeds para hoteles pequeños e independientes: modelos de precio y precios de partida publicados en webs oficiales, y cómo elegir.",
  crumb="Alternativas a Cloudbeds", h1='<em class="hl">Alternativas</em> a Cloudbeds para hoteles pequeños',
  lead="Cloudbeds no publica precios y trabaja con presupuesto. Si prefieres comparar primero precios publicados, estas son alternativas cuyos precios pudimos verificar en sus propias webs, incluido Hostlio Pro (nuestro producto).",
  answer="<strong>Respuesta corta:</strong> en un alojamiento pequeño e independiente, las preguntas clave son cómo pagas (cuota fija, por habitación o un porcentaje de ingresos), si el channel manager está incluido y si la mensajería con huéspedes forma parte del plan. Hostlio Pro, Sirvoy y Beds24 publican precios fijos o por uso; HotelRunner cobra un porcentaje de los ingresos por reservas; Amenitiz, como Cloudbeds, da presupuesto.",
  cb_h="Qué ofrece Cloudbeds, según su web",
  cb=["Cuatro planes, Flex, One, Experience y Enterprise, todos con presupuesto.", "Sin comisión añadida por las reservas de su Booking Engine o Channel Manager.",
      "Mensajería con chatbot de IA y bandeja unificada que incluye WhatsApp, dentro de Guest Experience en el plan Experience.", "\"400+ integration partners\", onboarding autoservicio o con coach, y soporte 24/7."],
  why_h="Por qué los alojamientos pequeños comparan alternativas",
  why=["Quieren ver un precio antes de reservar una demo comercial.", "Tienen 1–50 habitaciones y necesitan menos módulos.", "Quieren la mensajería con huéspedes incluida y no en un plan superior."],
  choose_h="Cómo elegir",
  choose=["Anota tus ingresos mensuales por reservas y tus habitaciones, y calcula el coste anual con cada modelo de precio.", "Comprueba que el channel manager cubre las OTAs en las que vendes.",
          "Decide si necesitas motor de reservas y cobro de pagos en la misma herramienta.", "Pregunta cómo se gestionan los mensajes de WhatsApp y de las bandejas de las OTAs, y en qué plan.", "Usa la prueba gratuita con tus habitaciones y tarifas reales antes de cambiar."],
  srcs=["cb_pr", "cb_ge", "hr_en", "am_en", "sv_pr", "b24_pr", "ev_pr"],
  faq=[("¿Hay una alternativa más barata a Cloudbeds?", "Cloudbeds no publica precios, así que una comparación directa requiere presupuesto. Entre las alternativas con precio publicado, Beds24 empieza en 15,50 € al mes, Sirvoy en 22 € al mes hasta 10 habitaciones (Starter) y Hostlio Pro en ⟦price:starter⟧ al mes."),
       ("¿Qué alternativa a Cloudbeds incluye mensajería con IA?", "Hostlio Pro incluye su asistente de IA Lio en WhatsApp en todos los planes y añade las bandejas de Booking.com, Airbnb y Expedia en Pro y Growth. Para otros productos, revisa los detalles de sus planes en sus webs."),
       ("¿Puedo llevarme mis datos de Cloudbeds?", "La mayoría de sistemas permite exportar reservas. Hostlio Pro importa reservas desde archivos CSV o Excel con asignación de columnas y control de duplicados.")]),
"pt": dict(
  card="Alternativas à Cloudbeds para hotéis pequenos, com preços publicados",
  title="Alternativas à Cloudbeds para hotéis pequenos | Hostlio Pro",
  desc="Alternativas à Cloudbeds para hotéis e pousadas independentes: modelos de preço e preços iniciais publicados nos sites oficiais, e como escolher.",
  crumb="Alternativas à Cloudbeds", h1='<em class="hl">Alternativas</em> à Cloudbeds para hotéis pequenos',
  lead="A Cloudbeds não publica preços e trabalha com orçamento. Se você prefere comparar preços publicados primeiro, estas são alternativas cujos preços conseguimos confirmar nos próprios sites, incluindo o Hostlio Pro (nosso produto).",
  answer="<strong>Resposta curta:</strong> para um hotel pequeno e independente, as perguntas principais são como você paga (mensalidade fixa, por quarto ou percentual da receita), se o channel manager está incluído e se as mensagens com hóspedes fazem parte do plano. Hostlio Pro, Sirvoy e Beds24 publicam preços fixos ou por uso; a HotelRunner cobra um percentual da receita de reservas; a Amenitiz, como a Cloudbeds, trabalha com orçamento.",
  cb_h="O que a Cloudbeds oferece, segundo o próprio site",
  cb=["Quatro planos, Flex, One, Experience e Enterprise, todos sob orçamento.", "Sem comissão adicional nas reservas do seu Booking Engine ou Channel Manager.",
      "Mensagens com chatbot de IA e caixa de entrada unificada que inclui WhatsApp, dentro de Guest Experience no plano Experience.", "\"400+ integration partners\", onboarding por autoatendimento ou com coach, e suporte 24/7."],
  why_h="Por que hotéis pequenos comparam alternativas",
  why=["Querem ver um preço antes de agendar uma demonstração de vendas.", "Têm 1–50 quartos e precisam de menos módulos.", "Querem as mensagens com hóspedes incluídas, não num plano superior."],
  choose_h="Como escolher",
  choose=["Anote sua receita mensal de reservas e o número de quartos e calcule o custo anual em cada modelo de preço.", "Confira se o channel manager cobre as OTAs em que você vende.",
          "Decida se precisa de motor de reservas e de processamento de pagamentos na mesma ferramenta.", "Pergunte como são tratadas as mensagens do WhatsApp e das caixas de entrada das OTAs, e em qual plano.", "Use o teste grátis com seus quartos e tarifas reais antes de migrar."],
  srcs=["cb_pr", "cb_ge", "hr_en", "am_en", "sv_pr", "b24_pr", "ev_pr"],
  faq=[("Existe uma alternativa mais barata à Cloudbeds?", "A Cloudbeds não publica preços, então uma comparação direta exige orçamento. Entre as alternativas com preço publicado, a Beds24 começa em € 15,50 por mês, a Sirvoy em € 22 por mês para até 10 quartos (Starter) e o Hostlio Pro em ⟦price:starter⟧ por mês."),
       ("Qual alternativa à Cloudbeds inclui mensagens com IA?", "O Hostlio Pro inclui a assistente de IA Lio no WhatsApp em todos os planos e acrescenta as caixas de entrada do Booking.com, Airbnb e Expedia no Pro e no Growth. Para outros produtos, confira os detalhes dos planos nos sites deles."),
       ("Consigo levar meus dados da Cloudbeds?", "A maioria dos sistemas permite exportar reservas. O Hostlio Pro importa reservas de arquivos CSV ou Excel, com mapeamento de colunas e controle de duplicados.")]),
}

P["alt-amenitiz"] = {
"en": dict(
  card="Amenitiz alternative: published pricing and AI messaging on WhatsApp",
  title="Amenitiz Alternative: Hostlio Pro Compared (2026) | Hostlio Pro",
  desc="Looking for an Amenitiz alternative? Compare quote-based Amenitiz with Hostlio Pro's published pricing, AI guest messaging on WhatsApp and when each fits.",
  crumb="Amenitiz alternative", h1='An <em class="hl">Amenitiz</em> alternative with published pricing',
  lead="Amenitiz is an all-in-one system for independent hotels and B&Bs in Europe, priced by quote. Hostlio Pro is a PMS, channel manager and AI guest assistant with prices on its website. Here is an honest side-by-side, based on each company's own pages.",
  answer="<strong>Short answer:</strong> Hostlio Pro suits properties that want to see the price up front and have an AI assistant answering on WhatsApp in every plan. Amenitiz suits properties that want a website builder, booking engine and integrated payments in one subscription, with support in their own language.",
  rows=[("Pricing", "price", "Not published: personalised quote based on number of rooms; monthly or annual (extra discount)"),
        ("Booking fees", "fee", "No commission on direct bookings and no per-reservation fees; AmenitizPay transactions 1.5% + €0.25"),
        ("Channel manager", "cm", "Core plan: channel manager with unlimited OTA connections (\"150+ OTAs\")"),
        ("Website, booking engine and payments", "be", "Booking engine and AmenitizPay in Core; website builder as Presence/Ultimate+ or the Advanced Website add-on"),
        ("Guest messaging and WhatsApp", "ai", "Core: automated guest emails and a unified guest inbox. \"Guest messaging + WhatsApp\" is in Advanced (labelled \"live in June\" on the pricing page)"),
        ("Free trial", "trial", "Not offered; free demo, and \"Live in 30 days or your first month is on us\""),
        ("Support languages", "English and Turkish (dashboard in 6 languages)", "English, French, Italian, Spanish or Portuguese on every plan")],
  srcs=["am_en", "am_fr", "am_cm"],
  fit=[("Price before the demo", "Plans and prices are on the pricing page, from ⟦price:starter⟧ a month, with a 7-day trial."),
       ("WhatsApp AI from the first plan", "Lio answers guests on WhatsApp on every plan, with your hotel's information and in the guest's language; Pro and Growth add Booking.com, Airbnb and Expedia inboxes."),
       ("Daily suggestions", "Every morning Lio suggests pricing and operations actions; nothing changes without your approval."),
       ("Numbers per channel", "Analytics shows occupancy, ADR, RevPAR and what each channel leaves you after commission.")],
  better_h="When Amenitiz is a better fit",
  better=[("You want a website and booking engine in the same subscription", "Amenitiz includes a booking engine and offers website building; Hostlio Pro doesn't."),
          ("You want to take payments", "AmenitizPay is integrated; Hostlio Pro doesn't collect payments."),
          ("You want support in French, Italian, Spanish or Portuguese", "Amenitiz offers native-language support on every plan; Hostlio Pro support is in English and Turkish."),
          ("You want a dedicated account manager", "Amenitiz lists a dedicated account manager in its Advanced plan.")],
  others_h="Other alternatives with published prices",
  others=[("Sirvoy", "Flat monthly fee by room tier, e.g. up to 10 rooms €22 (Starter) or €79 (Pro, with channel manager), 14-day trial.", "sv_pr"),
          ("Beds24", "Pay as you go from €15.50 a month: base fee, per room and per channel link.", "b24_pr")],
  switch=["Start the 7-day trial and add your room types and rates.", "Import your reservations from a CSV or Excel export.", "Connect your OTAs and plan the cut-over so availability is sent from one system only.", "Fill in Lio's hotel information and test it with \"Try Lio\"."],
  faq=[("How much does Amenitiz cost?", "Amenitiz doesn't publish prices. Its pricing page offers a personalised quote based on the number of rooms, with monthly or annual billing."),
       ("Does Amenitiz include WhatsApp?", "On Amenitiz's pricing page, \"Guest messaging + WhatsApp\" is listed in the Advanced plan, not in Core, and is labelled \"live in June\"."),
       ("Is Hostlio Pro available in French, Spanish, Italian and Portuguese?", "The dashboard, mobile app and guest check-in form are available in English, Turkish, Spanish, French, Italian and Portuguese. Support is in English and Turkish.")]),
"fr": dict(
  card="Alternative à Amenitiz : tarifs publics et IA sur WhatsApp",
  title="Alternative à Amenitiz : Hostlio Pro comparé (2026) | Hostlio Pro",
  desc="Vous cherchez une alternative à Amenitiz ? Comparez Amenitiz (sur devis) et Hostlio Pro : tarifs publics, IA sur WhatsApp et cas où chacun convient.",
  crumb="Alternative à Amenitiz", h1='Une alternative à <em class="hl">Amenitiz</em> avec des tarifs publics',
  lead="Amenitiz est une solution tout-en-un pour hôtels indépendants et chambres d’hôtes en Europe, sur devis. Hostlio Pro est un PMS, un channel manager et un assistant IA pour les clients, avec des tarifs affichés sur son site. Voici une comparaison honnête, fondée sur les pages officielles de chacun.",
  answer="<strong>En bref :</strong> Hostlio Pro convient aux établissements qui veulent connaître le prix d’emblée et disposer d’un assistant IA qui répond sur WhatsApp dans tous les forfaits. Amenitiz convient à ceux qui veulent un créateur de site, un moteur de réservation et l’encaissement des paiements dans un seul abonnement, avec un support dans leur langue.",
  rows=[("Tarifs", "price", "Non publiés : devis personnalisé selon le nombre de chambres ; paiement mensuel ou annuel (remise supplémentaire)"),
        ("Commissions", "fee", "Aucune commission sur les réservations directes ni frais par réservation ; transactions AmenitizPay 1,5 % + 0,25 €"),
        ("Channel manager", "cm", "Offre Core : channel manager avec connexions OTA illimitées (« 150+ OTAs »)"),
        ("Site, moteur de réservation et paiements", "be", "Moteur de réservation et AmenitizPay dans Core ; création de site via Presence/Ultimate+ ou l’option Advanced Website"),
        ("Messagerie clients et WhatsApp", "ai", "Core : e-mails automatiques et messagerie client unifiée. « Messagerie client + WhatsApp » dans l’offre Advanced (mention « disponible en juin » sur la page tarifs)"),
        ("Essai gratuit", "trial", "Non proposé ; démo gratuite et « mise en ligne en 30 jours ou premier mois offert »"),
        ("Langues du support", "Anglais et turc (tableau de bord en 6 langues)", "Anglais, français, italien, espagnol ou portugais dans toutes les offres")],
  srcs=["am_fr", "am_en", "am_cm"],
  fit=[("Le prix avant la démo", "Les forfaits et leurs prix sont sur la page tarifs, dès ⟦price:starter⟧ par mois, avec un essai de 7 jours."),
       ("L’IA sur WhatsApp dès le premier forfait", "Lio répond aux clients sur WhatsApp dans tous les forfaits, avec les informations de votre hôtel et dans la langue du client ; Pro et Growth ajoutent les messageries Booking.com, Airbnb et Expedia."),
       ("Des suggestions chaque matin", "Chaque matin, Lio propose des actions sur les prix et l’exploitation ; rien ne change sans votre accord."),
       ("Les chiffres par canal", "L’écran Analyse affiche taux d’occupation, ADR, RevPAR et ce que chaque canal vous laisse après commission.")],
  better_h="Quand Amenitiz convient mieux",
  better=[("Vous voulez site et moteur de réservation dans le même abonnement", "Amenitiz inclut un moteur de réservation et propose la création de site ; pas Hostlio Pro."),
          ("Vous voulez encaisser les paiements", "AmenitizPay est intégré ; Hostlio Pro n’encaisse pas de paiements."),
          ("Vous voulez un support en français", "Amenitiz propose un support dans votre langue dans toutes ses offres ; le support Hostlio Pro est en anglais et en turc, même si le tableau de bord est en français."),
          ("Vous voulez un interlocuteur dédié", "Amenitiz mentionne un account manager dédié dans son offre Advanced.")],
  others_h="Autres alternatives aux tarifs publics",
  others=[("Sirvoy", "Abonnement mensuel fixe par tranche de chambres, par ex. jusqu’à 10 chambres 22 € (Starter) ou 79 € (Pro, avec channel manager), essai de 14 jours.", "sv_pr"),
          ("Beds24", "Paiement à l’usage dès 15,50 € par mois : forfait de base, par chambre et par connexion de canal.", "b24_pr")],
  switch=["Démarrez l’essai de 7 jours et saisissez vos types de chambres et vos tarifs.", "Importez vos réservations depuis un export CSV ou Excel.", "Connectez vos OTA et planifiez la bascule pour que les disponibilités partent d’un seul système.", "Renseignez les informations de l’hôtel pour Lio et testez-le avec « Essayer Lio »."],
  faq=[("Combien coûte Amenitiz ?", "Amenitiz ne publie pas ses prix. Sa page tarifs propose un devis personnalisé selon le nombre de chambres, en paiement mensuel ou annuel."),
       ("Amenitiz inclut-il WhatsApp ?", "Sur la page tarifs d’Amenitiz, « Messagerie client + WhatsApp » figure dans l’offre Advanced, pas dans Core, avec la mention « disponible en juin »."),
       ("Hostlio Pro est-il disponible en français ?", "Oui : le tableau de bord, l’application mobile et le formulaire de check-in client existent en français (ainsi qu’en anglais, turc, espagnol, italien et portugais). Le support est en anglais et en turc.")]),
}

P["alt-hijiffy"] = {
"en": dict(
  card="HiJiffy alternative: AI guest messaging with the PMS included",
  title="HiJiffy Alternative: AI Messaging with PMS Included | Hostlio Pro",
  desc="HiJiffy alternative for small hotels: compare HiJiffy's guest-messaging plans with Hostlio Pro, where PMS, channel manager and WhatsApp AI come in one price.",
  crumb="HiJiffy alternative", h1='A <em class="hl">HiJiffy</em> alternative with the PMS included',
  lead="HiJiffy is a guest-communication and AI layer that works on top of your existing PMS. Hostlio Pro is the PMS and channel manager itself, with an AI guest assistant built in. They solve overlapping problems in different ways, so the right choice depends on what you already use.",
  answer="<strong>Short answer:</strong> if you're happy with your PMS and want a messaging layer across website chat, social channels and WhatsApp, HiJiffy is built for that. If you're a small independent property that wants the PMS, channel manager and an AI assistant on WhatsApp in one subscription, Hostlio Pro covers all three, with WhatsApp on every plan.",
  rows=[("What it is", "PMS + channel manager + AI guest assistant (Lio)", "A guest-communication and AI layer that integrates with PMSs, booking engines and CRMs"),
        ("Pricing", "price", "Per property, \"starting at\" by room count: Basic €99, Pro €159, Premium €319 a month with yearly billing (€105 / €170 / €350 monthly), plus a setup fee of €99 / €399 / €599 for each 5 properties; Enterprise by quote"),
        ("WhatsApp", "wa", "From the Premium plan; Pro covers website, Facebook, Instagram and Telegram"),
        ("OTA messaging", "Booking.com, Airbnb and Expedia inboxes on Pro and Growth", "Its site says it centralises OTA native messaging including Booking.com, Expedia and Airbnb"),
        ("PMS and channel manager", "cm", "Not a PMS or channel manager; PMS integration from Premium"),
        ("Free trial", "trial", "Not mentioned; subscribe or book a demo")],
  srcs=["hj_pr", "hj_home"],
  fit=[("One subscription instead of two", "Reservations, the room rack, the channel manager and Lio sit in one product, so Lio answers with live availability and your own rates."),
       ("WhatsApp on every plan", "Lio answers on WhatsApp from Starter (⟦price:starter⟧ a month), in the guest's language; it hands decisions to you."),
       ("Booking requests you approve", "On Pro and Growth, Lio collects dates, guests and room preference on WhatsApp and quotes from your rates; the request becomes a reservation once you approve it."),
       ("Online check-in", "Pro and Growth include online check-in with ID/passport MRZ reading and a digital signature.")],
  better_h="When HiJiffy is a better fit",
  better=[("You want to keep your current PMS", "HiJiffy is designed to sit on top of existing hotel systems. Hostlio Pro replaces the PMS and channel manager."),
          ("You need website chat and social channels", "HiJiffy covers website chat, Facebook, Instagram and Telegram. Hostlio Pro's Lio works on WhatsApp and OTA inboxes."),
          ("You run a large hotel or a group", "HiJiffy offers Enterprise plans with custom integrations and Power BI; Hostlio Pro's largest plan covers 2 properties and 150 rooms.")],
  switch=["Start the 7-day trial and add your room types and rates.", "Import your reservations from a CSV or Excel export of your current PMS.", "Connect your OTAs and your WhatsApp number.", "Fill in Lio's hotel information and test it with \"Try Lio\"."],
  faq=[("How much does HiJiffy cost?", "HiJiffy's pricing page lists per-property \"starting at\" prices that depend on room count: Basic €99, Pro €159 and Premium €319 a month with yearly billing, or €105, €170 and €350 billed monthly, plus a setup fee. Enterprise is by quote."),
       ("Which HiJiffy plan includes WhatsApp?", "According to HiJiffy's pricing page, WhatsApp is part of the Premium plan; the Pro plan's channels are website, Facebook, Instagram and Telegram."),
       ("Is Hostlio Pro only a chatbot?", "No. Hostlio Pro is a PMS and channel manager with an AI assistant built in, so it also handles reservations, availability on 100+ OTAs and online check-in.")]),
"pt": dict(
  card="Alternativa à HiJiffy: mensagens com IA e PMS incluído",
  title="Alternativa à HiJiffy com PMS incluído | Hostlio Pro",
  desc="Alternativa à HiJiffy para hotéis pequenos: compare os planos de mensagens da HiJiffy com o Hostlio Pro, que inclui PMS, channel manager e IA no WhatsApp.",
  crumb="Alternativa à HiJiffy", h1='Uma alternativa à <em class="hl">HiJiffy</em> com o PMS incluído',
  lead="A HiJiffy é uma camada de comunicação com hóspedes e IA que funciona sobre o PMS que você já usa. O Hostlio Pro é o próprio PMS e channel manager, com um assistente de IA embutido. Os dois resolvem problemas parecidos de formas diferentes; a escolha depende do que você já tem.",
  answer="<strong>Resposta curta:</strong> se você está satisfeito com seu PMS e quer uma camada de mensagens para chat do site, redes sociais e WhatsApp, a HiJiffy foi feita para isso. Se você tem um hotel ou pousada independente e quer PMS, channel manager e um assistente de IA no WhatsApp numa só assinatura, o Hostlio Pro cobre os três, com WhatsApp em todos os planos.",
  rows=[("O que é", "PMS + channel manager + assistente de IA (Lio)", "Uma camada de comunicação com hóspedes e IA que se integra a PMSs, motores de reserva e CRMs"),
        ("Preço", "price", "Por propriedade, \"a partir de\" conforme o número de quartos: Basic € 99, Pro € 159, Premium € 319 por mês no plano anual (€ 105 / € 170 / € 350 no mensal), mais taxa de implantação de € 99 / € 399 / € 599 a cada 5 propriedades; Enterprise sob orçamento"),
        ("WhatsApp", "wa", "A partir do plano Premium; o Pro cobre site, Facebook, Instagram e Telegram"),
        ("Mensagens das OTAs", "Caixas de entrada do Booking.com, Airbnb e Expedia no Pro e no Growth", "O site informa que centraliza as mensagens nativas das OTAs, incluindo Booking.com, Expedia e Airbnb"),
        ("PMS e channel manager", "cm", "Não é PMS nem channel manager; integração com PMS a partir do Premium"),
        ("Teste grátis", "trial", "Não mencionado; assinar ou agendar demonstração")],
  srcs=["hj_pr", "hj_home"],
  fit=[("Uma assinatura em vez de duas", "Reservas, mapa de quartos, channel manager e Lio ficam no mesmo produto, então a Lio responde com a disponibilidade real e as suas tarifas."),
       ("WhatsApp em todos os planos", "A Lio responde no WhatsApp desde o Starter (⟦price:starter⟧ por mês), no idioma do hóspede, e passa as decisões para você."),
       ("Pedidos de reserva com sua aprovação", "No Pro e no Growth, a Lio coleta datas, número de hóspedes e preferência de quarto no WhatsApp e informa o preço pelas suas tarifas; o pedido vira reserva quando você aprova."),
       ("Check-in online", "Pro e Growth incluem check-in online com leitura MRZ de documento/passaporte e assinatura digital.")],
  better_h="Quando a HiJiffy é a melhor escolha",
  better=[("Você quer manter seu PMS atual", "A HiJiffy foi feita para funcionar sobre os sistemas do hotel. O Hostlio Pro substitui o PMS e o channel manager."),
          ("Você precisa de chat no site e redes sociais", "A HiJiffy cobre chat do site, Facebook, Instagram e Telegram. A Lio do Hostlio Pro funciona no WhatsApp e nas caixas de entrada das OTAs."),
          ("Você administra um hotel grande ou uma rede", "A HiJiffy oferece planos Enterprise com integrações sob medida e Power BI; o maior plano do Hostlio Pro cobre 2 propriedades e 150 quartos.")],
  switch=["Comece o teste de 7 dias e cadastre seus tipos de quarto e tarifas.", "Importe suas reservas de um arquivo CSV ou Excel exportado do seu PMS atual.", "Conecte suas OTAs e seu número de WhatsApp.", "Preencha as informações do hotel para a Lio e teste com \"Testar a Lio\"."],
  faq=[("Quanto custa a HiJiffy?", "A página de preços da HiJiffy mostra preços \"a partir de\" por propriedade, que dependem do número de quartos: Basic € 99, Pro € 159 e Premium € 319 por mês no plano anual, ou € 105, € 170 e € 350 no mensal, mais taxa de implantação. O Enterprise é sob orçamento."),
       ("Qual plano da HiJiffy inclui WhatsApp?", "Segundo a página de preços da HiJiffy, o WhatsApp faz parte do plano Premium; os canais do plano Pro são site, Facebook, Instagram e Telegram."),
       ("O Hostlio Pro é só um chatbot?", "Não. O Hostlio Pro é um PMS e channel manager com assistente de IA embutido; também cuida das reservas, da disponibilidade em mais de 100 OTAs e do check-in online.")]),
}

HUB = {
"tr": dict(title="Otel Programı Karşılaştırmaları | Hostlio Pro",
  desc="Hostlio Pro'yu HotelRunner ve diğer otel programlarıyla karşılaştırın: fiyat modeli, AI misafir mesajlaşması ve hangisi kime uygun. Resmî kaynaklı, tarihli.",
  crumb="Karşılaştırmalar", h1='Otel programı <em class="hl">karşılaştırmaları</em>',
  lead="Her karşılaştırma yalnızca firmaların kendi resmî sayfalarında yayınladığı bilgilere dayanır ve tarihlidir. Rakibin daha uygun olduğu durumları da yazıyoruz.",
  general="Genel karşılaştırma: Hostlio Pro, Cloudbeds, Mews, Little Hotelier ve HotelRunner", prices="Otel programı fiyatları 2026"),
"en": dict(title="Hotel Software Comparisons & Alternatives | Hostlio Pro",
  desc="Compare Hostlio Pro with HotelRunner, Cloudbeds, Amenitiz and HiJiffy: pricing models, AI guest messaging and when each one fits. Sourced and dated.",
  crumb="Comparisons", h1='Hotel software <em class="hl">comparisons</em>',
  lead="Every comparison uses only what each company publishes on its own official pages, and is dated. We also say when the other product is the better fit.",
  general="Overview: Hostlio Pro, Cloudbeds, Mews, Little Hotelier and HotelRunner"),
"es": dict(title="Comparativas de software hotelero | Hostlio Pro",
  desc="Compara Hostlio Pro con Cloudbeds y otras alternativas: modelos de precio, mensajería con IA y cuándo encaja cada uno. Con fuentes oficiales y fecha.",
  crumb="Comparativas", h1='Comparativas de <em class="hl">software hotelero</em>',
  lead="Cada comparativa usa solo lo que cada empresa publica en sus páginas oficiales y lleva fecha. También explicamos cuándo encaja mejor el otro producto.",
  general="Visión general: Hostlio Pro, Cloudbeds, Mews, Little Hotelier y HotelRunner"),
"pt": dict(title="Comparativos de sistemas para hotel | Hostlio Pro",
  desc="Compare o Hostlio Pro com Cloudbeds, HiJiffy e outras alternativas: modelos de preço, mensagens com IA e quando cada um serve. Com fontes oficiais e data.",
  crumb="Comparativos", h1='Comparativos de <em class="hl">sistemas para hotel</em>',
  lead="Cada comparativo usa só o que cada empresa publica nas próprias páginas oficiais e tem data. Também dizemos quando o outro produto é a melhor escolha.",
  general="Visão geral: Hostlio Pro, Cloudbeds, Mews, Little Hotelier e HotelRunner"),
"fr": dict(title="Comparatifs de logiciels hôteliers | Hostlio Pro",
  desc="Comparez Hostlio Pro à Amenitiz et à d’autres logiciels hôteliers : modèles de prix, messagerie IA et cas où chacun convient. Sources officielles, datées.",
  crumb="Comparatifs", h1='Comparatifs de <em class="hl">logiciels hôteliers</em>',
  lead="Chaque comparatif s’appuie uniquement sur ce que chaque entreprise publie sur ses pages officielles, et il est daté. Nous indiquons aussi quand l’autre produit convient mieux.",
  general="Vue d’ensemble : Hostlio Pro, Cloudbeds, Mews, Little Hotelier et HotelRunner"),
}
HUB_KEYS = ["vs-hotelrunner", "vs-cloudbeds", "alt-cloudbeds", "alt-amenitiz", "alt-hijiffy"]

# ---------------------------------------------------------------- rendering
def _plain(s): return s.replace('<em class="hl">', "").replace("</em>", "")

def _sources(lang, keys):
    c = C[lang]
    lis = "".join(f'<li><a href="{SRC[k][1]}" rel="nofollow noopener">{html.escape(SRC[k][0])}</a> <span class="small muted">({c["checked"]})</span></li>' for k in keys)
    return f'<h2 style="margin-top:48px;font-size:var(--t-1)">{c["src_h"]}</h2><ul>{lis}</ul>'

def _rows(items): return "".join(f'<div class="row"><h3>{h}</h3><div><p>{p}</p></div></div>' for h, p in items)

def _more(key, lang, B):
    c = C[lang]
    ks = [k for k in HUB_KEYS if k != key and lang in B.ROUTES[k]]
    lis = "".join(f'<li><a href="{B.url(k, lang)}">{html.escape(P[k][lang]["card"])}</a></li>' for k in ks)
    lis += f'<li><a href="{B.url("compare", lang)}">{html.escape(HUB[lang]["general"])}</a></li>'
    return (f'<h2 style="margin-top:48px;font-size:var(--t-1)">{c["more_h"]}</h2><ul>{lis}</ul>'
            f'<p><a href="{B.url("cmp-hub", lang)}">{c["hub_link"]}</a> · <a href="{B.url("tools", lang)}">{c["tools"]}</a></p>')

def _cta(lang, B):
    c = C[lang]
    return f'<div class="cta-row" style="margin-top:28px">{B.btn(c["trial"], B.SIGNUP_URL)}{B.btn(c["pricing"], B.url("pricing", lang), "ghost")}</div>'

def _note(lang, B):
    return f'<p class="small muted" style="margin-top:14px">{C[lang]["note"].format(d=DATE_TXT[lang], contact=B.url("contact", lang))}</p>'

def vs_page(key, lang, B):
    d = P[key][lang]; c = C[lang]; h = HL[lang]
    rows = "".join(f'<tr><th scope="row">{lbl}</th><td>{h.get(hv, hv)}</td><td>{cv}</td></tr>' for lbl, hv, cv in d["rows"])
    compname = {"vs-hotelrunner": "HotelRunner", "vs-cloudbeds": "Cloudbeds", "alt-amenitiz": "Amenitiz", "alt-hijiffy": "HiJiffy"}[key]
    table = (f'<div class="table-wrap" style="margin-top:40px"><table><caption class="sr-only">{html.escape(_plain(d["h1"]))}, {c["asof"]}</caption>'
             f'<thead><tr><th>{c["asof"]}</th><th>Hostlio Pro</th><th>{compname}</th></tr></thead><tbody>{rows}</tbody></table></div>')
    calc = ""
    if key == "vs-hotelrunner":
        calc = f'<h2 style="margin-top:64px">{d["calc_h"]}</h2><p style="max-width:75ch">{d["calc_p"]}</p>{hr_table(lang)}<p style="max-width:75ch;margin-top:14px">{d["calc_after"]}</p>'
    others = ""
    if d.get("others"):
        lis = "".join(f'<li><strong>{n}</strong>: {t} <a href="{SRC[s][1]}" rel="nofollow noopener" class="small">({SRC_ONE[lang]})</a></li>' for n, t, s in d["others"])
        others = f'<h2 style="margin-top:48px;font-size:var(--t-1)">{d["others_h"]}</h2><ul>{lis}</ul>'
    body = f'''<section class="page-hero"><div class="wrap"><h1>{d["h1"]}</h1><p class="lead">{d["lead"]}</p>{_cta(lang, B)}</div></section>
<section style="padding-top:0"><div class="wrap">
<div class="answer"><p>{d["answer"]}</p></div>
{table}{_note(lang, B)}
{calc}
<h2 style="margin-top:64px">{c["fit_h"]}</h2><div class="rows">{_rows(d["fit"])}</div>
<h2 style="margin-top:64px">{d["better_h"]}</h2><div class="rows">{_rows(d["better"])}</div>
{others}
<h2 style="margin-top:64px">{c["switch_h"]}</h2><div class="prose"><ol>{"".join(f"<li>{s}</li>" for s in d["switch"])}</ol></div>
{_cta(lang, B)}
{_sources(lang, d["srcs"])}
{_more(key, lang, B)}
</div></section>'''
    return body

def alt_page(key, lang, B):
    d = P[key][lang]; c = C[lang]
    cols = ALT_COLS[lang]
    rows = "".join(f'<tr><th scope="row">{n}</th><td>{m}</td><td>{p}</td><td>{t}</td><td>{f}</td><td>'
                   + (f'<a href="{SRC[s][1]}" rel="nofollow noopener">{html.escape(SRC[s][0].split(":")[0])}</a>' if s else f'<a href="{B.url("pricing", lang)}">Hostlio Pro</a>') + '</td></tr>'
                   for n, m, p, t, f, s in ALTS[lang])
    table = (f'<div class="table-wrap" style="margin-top:24px"><table><caption class="sr-only">{html.escape(_plain(d["h1"]))}, {c["asof"]}</caption>'
             f'<thead><tr>{"".join(f"<th>{x}</th>" for x in cols)}</tr></thead><tbody>{rows}</tbody></table></div>')
    ul = lambda xs: "<ul>" + "".join(f"<li>{x}</li>" for x in xs) + "</ul>"
    body = f'''<section class="page-hero"><div class="wrap"><h1>{d["h1"]}</h1><p class="lead">{d["lead"]}</p>{_cta(lang, B)}</div></section>
<section style="padding-top:0"><div class="wrap">
<div class="answer"><p>{d["answer"]}</p></div>
<h2 style="margin-top:56px">{c["asof"]}</h2>{table}{_note(lang, B)}
<div class="prose">
<h2>{d["cb_h"]}</h2>{ul(d["cb"])}
<h2>{d["why_h"]}</h2>{ul(d["why"])}
<h2>{d["choose_h"]}</h2><ol>{"".join(f"<li>{x}</li>" for x in d["choose"])}</ol>
</div>
{_cta(lang, B)}
{_sources(lang, d["srcs"])}
{_more(key, lang, B)}
</div></section>'''
    return body

def hub_page(lang, B):
    d = HUB[lang]
    ks = [k for k in HUB_KEYS if lang in B.ROUTES[k]]
    cards = [(B.url(k, lang), P[k][lang]["card"], P[k][lang]["desc"]) for k in ks]
    gen = B.url("compare", lang)
    cards.append((gen, d["general"], ""))
    if lang == "tr" and "post-prices" in B.ROUTES: cards.append((B.url("post-prices", "tr"), d["prices"], ""))
    items = "".join(f'<li><a href="{u}">{html.escape(t)}</a>' + (f'<p>{html.escape(pricing.fill(ds, lang))}</p>' if ds else "") + '</li>' for u, t, ds in cards)
    body = f'''<section class="page-hero"><div class="wrap"><h1>{d["h1"]}</h1><p class="lead">{d["lead"]}</p></div></section>
<section style="padding-top:0" class="related"><div class="wrap"><ul class="related-list">{items}</ul>
<p class="small muted" style="margin-top:16px"><a href="{B.url("tools", lang)}">{C[lang]["tools"]}</a></p></div></section>'''
    return {"key": "cmp-hub", "title": d["title"], "desc": d["desc"], "trail": [(d["crumb"], B.url("cmp-hub", lang))], "body": body, "page_type": "CollectionPage"}

def pages(lang, B):
    out = []
    if lang in B.ROUTES["cmp-hub"]: out.append(hub_page(lang, B))
    for key in HUB_KEYS:
        if lang not in B.ROUTES[key]: continue
        d = P[key][lang]
        body = vs_page(key, lang, B) if "rows" in d else alt_page(key, lang, B)
        out.append({"key": key, "title": d["title"], "desc": d["desc"], "body": body, "faq": d["faq"],
                    "trail": [(HUB[lang]["crumb"], B.url("cmp-hub", lang)), (d["crumb"], B.url(key, lang))]})
    return out
