from build import btn, icon, logo, url, room_rack, channel_strip, faq_block, SIGNUP_URL, EMAIL, UPDATED, CHECK, software_schema, SITE, PLANS
L = "tr"
def U(k): return url(k, L)

# ------------------------------------------------------------ shared facts
PLAN_TXT = {
 "starter": ("Küçük pansiyon ve butik oteller için", ["1 tesis, 10 odaya kadar","Aylık 1.000 AI mesajı","100+ OTA ile kanal senkronizasyonu","WhatsApp AI mesajlaşma","Oda rafı (rezervasyon takvimi)","Otomatik PDF vize formları"]),
 "pro":     ("Tek tesisli, büyüyen oteller için", ["1 tesis, 50 odaya kadar","Aylık 5.000 AI mesajı","Starter'daki her şey","WhatsApp + OTA gelen kutusu mesajlaşması (Booking.com, Airbnb, Expedia)","Online check-in ve dijital imza","Transfer ve tur satışı","Mobil uygulama"]),
 "growth":  ("İki tesis işleten ekipler için", ["2 tesise kadar, 150 odaya kadar","Aylık 12.000 AI mesajı","Pro'daki her şey","Öncelikli kanal senkronizasyonu","Öncelikli destek (ertesi iş günü)","Birebir kurulum görüşmesi","White-label seçenekleri"]),
}

def plans_html():
    out = []
    for p in PLANS:
        for_, feats = PLAN_TXT[p["id"]]
        pop = p["id"] == "pro"
        lis = "".join(f"<li>{CHECK}<span>{f}</span></li>" for f in feats)
        out.append(f'''<article class="plan{" pop" if pop else ""}" aria-labelledby="plan-{p["id"]}">
{'<span class="tag">En çok tercih edilen</span>' if pop else ""}
<h3 id="plan-{p["id"]}">{p["name"]}</h3><p class="for">{for_}</p>
<div class="price num"><b>${p["price"]}</b><span class="muted">/ ay</span></div>
<p class="small muted num" style="margin:0">Erken kayıt fiyatı (normali <s>${p["regular"]}</s>)</p>
<ul>{lis}</ul>
{btn(p["name"]+" ile başla", SIGNUP_URL+"?plan="+p["id"], "primary" if pop else "ghost")}
</article>''')
    return '<div class="plans">' + "".join(out) + "</div>"

FAQ_CORE = [
 ("Otel programı nedir?", "Otel programı (otel yönetim yazılımı, PMS), bir konaklama tesisinin rezervasyonlarını, oda müsaitliğini, satış kanallarını ve misafir bilgilerini tek yerden yönetmesini sağlayan yazılımdır. Hostlio Pro bu işlevlere misafir mesajlarını 30+ dilde yanıtlayan yapay zekâ asistanı Lio'yu ekler."),
 ("Hostlio Pro nedir?", "Hostlio Pro, bağımsız oteller, butik oteller ve pansiyonlar için geliştirilmiş yapay zekâ destekli bir otel yönetim yazılımıdır (PMS). Misafir mesajlarını 30'dan fazla dilde 7/24 yanıtlayan AI asistanı Lio'yu, 100+ OTA'ya bağlanan kanal yöneticisini, sürükle-bırak rezervasyon takvimini ve online check-in'i tek panelde birleştirir."),
 ("Hostlio Pro'nun fiyatı ne kadar?", "Üç plan var: Starter aylık 49 $, Pro aylık 89 $, Growth aylık 149 $. Bu fiyatlar ilk 50 müşteriye özel %20 erken kayıt indirimini içerir ve abonelik sürdüğü sürece sabit kalır. Normal fiyatlar sırasıyla 59 $, 109 $ ve 189 $'dır."),
 ("Ücretsiz deneme var mı?", "Evet. Tüm planlar 7 gün ücretsiz denenebilir. Kayıt sırasında ödeme kartı alınır, ancak deneme süresi bitene kadar hiçbir ücret çekilmez. Uzun süreli sözleşme yoktur, istediğiniz zaman iptal edebilirsiniz."),
 ("Hangi OTA'larla çalışıyor?", "Hostlio Pro, Channex altyapısı üzerinden Booking.com, Airbnb, Expedia, Agoda, Trip.com, Hotels.com, Hotelbeds, Hostelworld ve Google Hotels dahil 100'den fazla kanala bağlanır. Müsaitlik, fiyat ve rezervasyonlar tüm kanallarda eşzamanlı güncellenir."),
 ("AI asistan Lio hangi dillerde yanıt veriyor?", "Lio, Türkçe, İngilizce, Arapça, Rusça, Almanca, Japonca ve Çince dahil 30'dan fazla dilde yanıt verir. Misafir hangi dilde yazarsa o dilde cevaplar; siz panelde Türkçe çevirisini görürsünüz."),
]

# ------------------------------------------------------------ pages
def home():
    import home_v3
    return home_v3.home(L, plans_html, FAQ_CORE)

def ai():
    body = f'''
<section class="page-hero"><div class="wrap split">
<div><h1>AI misafir asistanı Lio</h1>
<p class="lead">Lio, otelinizin bilgileriyle eğitilen bir yapay zekâ asistanıdır. Misafir mesajlarını WhatsApp'ta ve OTA gelen kutuları (Booking.com, Airbnb, Expedia) içinde 30+ dilde, günün her saatinde yanıtlar.</p>
<div class="cta-row">{btn("Lio'yu 7 gün ücretsiz dene", SIGNUP_URL)}</div></div>
<div class="panel typing"><p class="panel-title">WhatsApp, 02:47</p>
<div class="msg in" style="background:var(--bg)" lang="en">Hi! Our flight lands at 1 am. Can someone pick us up and is late check-in ok?</div>
<div class="msg out">Of course! Our airport transfer is €35 for up to 3 guests. Shall I book it for your 1 am arrival? Late check-in is no problem, the night desk will be waiting.<small>Lio, İngilizce</small></div>
<p class="small muted" style="margin:10px 0 0">Transfer rezervasyonu oluşturuldu, ödeme bağlantısı gönderildi.</p></div>
</div></section>

<section class="white rule"><div class="wrap">
<div class="answer"><p><strong>Otelde AI misafir asistanı nedir?</strong> Misafirlerin rezervasyon öncesi ve sonrası sorduğu soruları, otelin kendi bilgilerini kullanarak otomatik yanıtlayan yazılımdır. Lio, cevaplayamadığı ya da insan kararı gereken mesajları (indirim talebi, şikâyet, özel istek) personele iletir.</p></div>
<h2 style="margin-top:64px">Lio neler yapar</h2><div class="rows">
<div class="row"><h3>Tek gelen kutusu</h3><div><p>WhatsApp ve OTA gelen kutusu mesajları (Booking.com, Airbnb, Expedia) tek ekranda toplanır. Hangi misafirin hangi rezervasyona ait olduğunu Lio otomatik eşler.</p></div></div>
<div class="row"><h3>30+ dil, otomatik çeviri</h3><div><p>Misafir Japonca yazar, Lio Japonca cevaplar; siz yazışmayı Türkçe görürsünüz. Manuel cevap yazarken de mesajınız misafirin diline çevrilir.</p></div></div>
<div class="row"><h3>Otelinize özel bilgi</h3><div><p>Check-in/check-out saatleri, otopark, evcil hayvan kuralları, kahvaltı saatleri, yakın ulaşım, oda özellikleri. Bu bilgileri bir kez girersiniz, Lio her cevapta tutarlı kullanır.</p></div></div>
<div class="row"><h3>Satış yapan asistan</h3><div><p>Lio sadece soru yanıtlamaz: havalimanı transferi, şehir turu ve ek hizmet tekliflerini uygun anda sunar, rezervasyonu oluşturur.</p></div></div>
<div class="row"><h3>Kontrol sizde</h3><div><p>İlk günlerde Lio'nun cevaplarını göndermeden önce onaylayabilirsiniz. Hangi konuları kendisi kapatacağını, hangilerini size devredeceğini siz belirlersiniz.</p></div></div>
</div></div></section>

<section><div class="wrap">
<div class="section-head"><h2>Planlara göre AI mesaj kotası</h2><p>Bir mesaj, Lio'nun misafire gönderdiği tek bir yanıttır.</p></div>
<div class="table-wrap"><table><thead><tr><th>Plan</th><th class="c">Aylık AI mesajı</th><th>Mesaj kanalları</th></tr></thead><tbody>
<tr><th>Starter</th><td class="c num">1.000</td><td>WhatsApp</td></tr>
<tr><th>Pro</th><td class="c num">5.000</td><td>WhatsApp + OTA gelen kutuları (Booking.com, Airbnb, Expedia)</td></tr>
<tr><th>Growth</th><td class="c num">12.000</td><td>WhatsApp + OTA gelen kutuları (Booking.com, Airbnb, Expedia)</td></tr>
</tbody></table></div>
</div></section>
'''
    faq = [
     ("Lio yanlış bilgi verirse ne olur?", "Lio yalnızca sizin girdiğiniz otel bilgilerini ve rezervasyon verilerini kullanır. Emin olmadığı sorularda tahmin yürütmek yerine mesajı size iletir. Dilerseniz tüm cevapları gönderilmeden önce onaylayabilirsiniz."),
     ("Booking.com ve Airbnb mesajlarını da yanıtlıyor mu?", "Evet. Pro ve Growth planlarında OTA mesajları da Lio'nun gelen kutusuna düşer ve aynı şekilde yanıtlanır."),
     ("Mesaj kotası dolarsa ne olur?", "Kotanız dolduğunda mesajlar gelmeye devam eder ve panelde görünür; yalnızca otomatik yanıt durur. Üst plana geçerek kotanızı artırabilirsiniz."),
     FAQ_CORE[5],
    ]
    return {"key":"ai","title":"AI Misafir Asistanı Lio: 30+ Dilde Otel Mesajları | Hostlio Pro",
            "desc":"Hostlio Pro'nun AI asistanı Lio, otel misafirlerinin WhatsApp ve OTA gelen kutusu mesajlarını 30+ dilde 7/24 yanıtlar, transfer ve tur satar. Nasıl çalıştığını görün.",
            "trail":[("AI asistan Lio", U("ai"))],"body":body,"faq":faq}

def channel():
    body = f'''
<section class="page-hero"><div class="wrap split">
<div><h1>100+ OTA için kanal yöneticisi</h1>
<p class="lead">Booking.com, Airbnb, Expedia, Agoda ve 100'den fazla kanaldaki müsaitlik, fiyat ve rezervasyonlarınızı tek takvimden yönetin. Hostlio Pro sertifikalı bağlantılarla çift yönlü, anlık senkronizasyon yapar.</p>
<div class="cta-row">{btn("7 gün ücretsiz dene", SIGNUP_URL)}</div></div>
<div class="panel"><p class="panel-title">Bağlı kanallar</p><div class="chan-list">
<div><span>Booking.com</span><span class="pill">Senkron</span></div>
<div><span>Airbnb</span><span class="pill">Senkron</span></div>
<div><span>Expedia</span><span class="pill">Senkron</span></div>
<div><span>Agoda</span><span class="pill">Senkron</span></div>
<div><span>Google Hotels</span><span class="pill">Senkron</span></div>
</div></div>
</div></section>
<section class="white rule"><div class="wrap">
<div class="answer"><p><strong>Kanal yöneticisi (channel manager) nedir?</strong> Bir otelin odalarını birden fazla online satış kanalında aynı anda satarken müsaitlik ve fiyatları otomatik eşitleyen yazılımdır. Bir kanalda oda satıldığında diğer tüm kanallarda o oda anında kapanır, böylece çift rezervasyon (overbooking) önlenir.</p></div>
<h2 style="margin-top:64px">Kanal yöneticisinin sağladıkları</h2><div class="rows">
<div class="row"><h3>Çift yönlü senkronizasyon</h3><div><p>Yeni rezervasyon, değişiklik ve iptaller oda rafına otomatik düşer. Takvimde yaptığınız değişiklik de tüm kanallara gider.</p></div></div>
<div class="row"><h3>Fiyat ve kısıtlama yönetimi</h3><div><p>Oda tipi bazında fiyat, minimum konaklama ve satış kapatma gibi kısıtlamaları tek ekrandan tüm kanallara gönderin.</p></div></div>
<div class="row"><h3>Kanal renkleriyle oda rafı</h3><div><p>Hangi rezervasyonun hangi kanaldan geldiğini renkten anlarsınız. Oda değişikliği sürükle-bırak ile yapılır.</p></div></div>
<div class="row"><h3>Mesajlarla entegre</h3><div><p>OTA'dan gelen rezervasyonun misafir mesajları da Lio'nun gelen kutusuna bağlanır; kim, hangi oda, hangi tarih bilgisi her yazışmanın yanındadır.</p></div></div>
</div></div></section>
<section><div class="wrap"><div class="section-head"><h2>Desteklenen başlıca kanallar</h2><p>Liste sertifikalı bağlantı ağımıza göre güncellenir; burada olmayan bir kanal için bize yazın.</p></div>
<div class="table-wrap"><table><thead><tr><th>Kanal</th><th>Tür</th></tr></thead><tbody>
<tr><th>Booking.com</th><td>OTA</td></tr><tr><th>Airbnb</th><td>Kısa dönem kiralama</td></tr><tr><th>Expedia, Hotels.com</th><td>OTA</td></tr>
<tr><th>Agoda, Trip.com</th><td>OTA (Asya ağırlıklı)</td></tr><tr><th>Hotelbeds</th><td>Toptancı (bedbank)</td></tr><tr><th>Hostelworld</th><td>Hostel pazaryeri</td></tr><tr><th>Google Hotels</th><td>Metasearch</td></tr>
</tbody></table></div></div></section>
'''
    faq = [FAQ_CORE[4],
     ("Kanal yöneticisi tüm planlarda var mı?", "Evet. Starter, Pro ve Growth planlarının tamamında 100+ OTA ile kanal senkronizasyonu bulunur. Growth planında senkronizasyon önceliklidir."),
     ("Mevcut kanal yöneticimden geçiş zor mu?", "Hayır. Oda tiplerinizi Hostlio Pro'da oluşturup OTA hesaplarınızı Channex üzerinden eşlemeniz yeterli. Geçiş sırasında kurulum ekibimiz size eşlik eder."),
    ]
    return {"key":"channel","title":"Otel Kanal Yöneticisi: 100+ OTA Tek Takvimde | Hostlio Pro",
            "desc":"Hostlio Pro kanal yöneticisi Booking.com, Airbnb, Expedia, Agoda dahil 100+ OTA'da müsaitlik ve fiyatı anlık senkronize eder, overbooking'i önler.",
            "trail":[("Kanal yöneticisi", U("channel"))],"body":body,"faq":faq}

def checkin():
    body = f'''
<section class="page-hero"><div class="wrap split">
<div><h1>Online check&#8209;in ve dijital imza</h1>
<p class="lead">Misafir, varıştan önce telefonundan kimlik bilgilerini, refakatçilerini ve imzasını gönderir. Resepsiyonda anahtar teslimi birkaç dakikaya iner.</p>
<div class="cta-row">{btn("Pro ile 7 gün ücretsiz dene", SIGNUP_URL+"?plan=pro")}</div></div>
<div class="panel"><p class="panel-title">Online check-in, Oda 202</p>
<div class="field"><span>Ad soyad</span><div>Keiko Sato</div></div>
<div class="field"><span>Uyruk</span><div>Japonya</div></div>
<div class="field"><span>Refakatçi</span><div>1 misafir eklendi</div></div>
<div class="field"><span>İmza</span><div class="sig">Dijital imza alındı</div></div>
</div>
</div></section>
<section class="white rule"><div class="wrap">
<div class="answer"><p><strong>Online check-in nasıl çalışır?</strong> Hostlio Pro, rezervasyon sahibine kişiye özel, süreli ve güvenli bir bağlantı gönderir. Misafir bu bağlantıdan kimlik bilgilerini girer, kimlik fotoğrafını ekler, varsa refakatçileri ekler ve formu dijital olarak imzalar. Bilgiler doğrudan rezervasyona kaydedilir.</p></div>
<h2 style="margin-top:64px">Online check-in özellikleri</h2><div class="rows">
<div class="row"><h3>Güvenli bağlantı</h3><div><p>Her rezervasyona özel, token tabanlı bağlantı. Bağlantı yalnızca o rezervasyonun formunu açar.</p></div></div>
<div class="row"><h3>Refakatçi misafirler</h3><div><p>Aynı odada kalan tüm misafirler tek formda eklenir. Resepsiyonda tek tek bilgi yazmaya gerek kalmaz.</p></div></div>
<div class="row"><h3>Dijital imza ve onay</h3><div><p>Misafir otel kurallarını ve kişisel veri onayını ekranda imzalar. İmzalı kayıt rezervasyonda saklanır.</p></div></div>
<div class="row"><h3>Kişisel verilere saygı</h3><div><p>Misafir verileri talep üzerine silinebilir. Açık rıza metni formun parçasıdır.</p></div></div>
<div class="row"><h3>Resmî bildirim için dışa aktarma</h3><div><p>Toplanan misafir bilgileri, yasal konaklama bildirimlerinizde kullanabileceğiniz formatta dışa aktarılır.</p></div></div>
</div></div></section>
<section class="dark on-dark"><div class="wrap"><div class="section-head"><h2>Misafir tarafında üç adım</h2></div>
<ol class="steps"><li><h3>Bağlantıyı açar</h3><p>Rezervasyon onayından sonra gelen kişisel bağlantıyı açar (otomatik e-postayla gönderilir ya da otel paylaşır).</p></li>
<li><h3>Bilgileri doldurur</h3><p>Kimlik bilgilerini ve fotoğrafını ekler, refakatçileri girer.</p></li>
<li><h3>İmzalar</h3><p>Otel kurallarını onaylayıp ekranda imzalar. Resepsiyona sadece anahtar almaya gelir.</p></li></ol>
</div></section>
'''
    faq = [("Online check-in hangi planda var?", "Online check-in ve dijital imza Pro ve Growth planlarına dahildir."),
           ("Misafirin uygulama indirmesi gerekiyor mu?", "Hayır. Check-in formu tarayıcıda açılır; herhangi bir uygulama indirmek gerekmez."),
           ("Misafir bağlantıyı doldurmazsa ne olur?", "Klasik check-in'e devam edebilirsiniz. Resepsiyonda bilgileri Hostlio Pro mobil uygulamasından da girebilirsiniz.")]
    return {"key":"checkin","title":"Otel Online Check-in ve Dijital İmza Yazılımı | Hostlio Pro",
            "desc":"Hostlio Pro online check-in ile misafirler varıştan önce kimlik bilgilerini, refakatçilerini ve dijital imzasını telefondan gönderir. Resepsiyonda kuyruk olmaz.",
            "trail":[("Online check-in", U("checkin"))],"body":body,"faq":faq}

def features():
    body = f'''
<section class="page-hero"><div class="wrap split"><div><h1>Hostlio Pro'nun tüm özellikleri</h1>
<p class="lead">Bağımsız bir otelin günlük işleri için gereken modüller: misafir iletişimi, dağıtım, rezervasyon, check-in ve ek gelir.</p></div><div class="hero-img"><img src="/assets/img/gen-team-desk.webp" alt="" width="1080" height="1350"></div></div></section>
<section class="white rule"><div class="wrap"><h2 class="sr-only">Modüller</h2><div class="rows">
<div class="row"><h3>AI asistan Lio</h3><div><p>30+ dilde, 7/24 misafir yanıtı. WhatsApp ve OTA gelen kutusu mesajları (Booking.com, Airbnb, Expedia) tek gelen kutusunda.</p><a href="{U("ai")}">Lio hakkında daha fazlası</a></div></div>
<div class="row"><h3>Kanal yöneticisi</h3><div><p>100+ OTA'da sertifikalı bağlantılarla müsaitlik, fiyat ve rezervasyon senkronizasyonu.</p><a href="{U("channel")}">Kanal yöneticisi</a></div></div>
<div class="row"><h3>Oda rafı (room rack)</h3><div><p>Sürükle-bırak rezervasyon takvimi. Oda değişikliği, konaklama uzatma ve blokaj tek hareketle.</p></div></div>
<div class="row"><h3>Online check-in</h3><div><p>Güvenli bağlantı, refakatçi misafirler, kimlik fotoğrafı ve dijital imza.</p><a href="{U("checkin")}">Online check-in</a></div></div>
<div class="row"><h3>Otomatik PDF vize formları</h3><div><p>Vize başvurusu için otel davet ve konaklama belgelerini rezervasyon bilgilerinden tek tıkla PDF olarak üretin.</p></div></div>
<div class="row"><h3>Transfer ve tur satışı</h3><div><p>Lio mesajlaşma sırasında havalimanı transferi ve tur önerir, talebi ekibinize iletir.</p></div></div>
<div class="row"><h3>Mobil uygulama</h3><div><p>iOS uygulamasıyla rezervasyonları, mesajları ve check-in'leri otelin dışından yönetin. İnternet kesildiğinde de çalışır, bağlantı gelince senkronize olur.</p></div></div>
</div></div></section>
<section><div class="wrap"><div class="section-head"><h2>Planlara göre özellikler</h2></div>
<div class="table-wrap"><table><thead><tr><th>Özellik</th><th class="c">Starter</th><th class="c">Pro</th><th class="c">Growth</th></tr></thead><tbody>
<tr><th>Tesis sayısı</th><td class="c">1</td><td class="c">1</td><td class="c">2</td></tr>
<tr><th>Oda limiti</th><td class="c num">10</td><td class="c num">50</td><td class="c num">150</td></tr>
<tr><th>Aylık AI mesajı</th><td class="c num">1.000</td><td class="c num">5.000</td><td class="c num">12.000</td></tr>
<tr><th>100+ OTA kanal senkronizasyonu</th><td class="c">Var</td><td class="c">Var</td><td class="c">Öncelikli</td></tr>
<tr><th>WhatsApp AI mesajlaşma</th><td class="c">Var</td><td class="c">Var</td><td class="c">Var</td></tr>
<tr><th>OTA gelen kutusu mesajlaşması (Booking.com, Airbnb, Expedia)</th><td class="c">Yok</td><td class="c">Var</td><td class="c">Var</td></tr>
<tr><th>Oda rafı takvimi</th><td class="c">Var</td><td class="c">Var</td><td class="c">Var</td></tr>
<tr><th>PDF vize formları</th><td class="c">Var</td><td class="c">Var</td><td class="c">Var</td></tr>
<tr><th>Online check-in ve dijital imza</th><td class="c">Yok</td><td class="c">Var</td><td class="c">Var</td></tr>
<tr><th>Transfer ve tur satışı</th><td class="c">Yok</td><td class="c">Var</td><td class="c">Var</td></tr>
<tr><th>iOS mobil uygulama</th><td class="c">Yok</td><td class="c">Var</td><td class="c">Var</td></tr>
<tr><th>Öncelikli destek ve kurulum görüşmesi</th><td class="c">Yok</td><td class="c">Yok</td><td class="c">Var</td></tr>
<tr><th>White-label</th><td class="c">Yok</td><td class="c">Yok</td><td class="c">Var</td></tr>
</tbody></table></div></div></section>
'''
    return {"key":"features","title":"Otel Programı Özellikleri: AI, Kanal Yöneticisi | Hostlio Pro",
            "desc":"Hostlio Pro özellikleri: AI misafir asistanı, 100+ OTA kanal yöneticisi, sürükle-bırak oda rafı, online check-in, PDF vize formları, transfer satışı ve mobil uygulama.",
            "trail":[("Özellikler", U("features"))],"body":body,"faq":[FAQ_CORE[0], FAQ_CORE[1], FAQ_CORE[4]]}

def pricing():
    body = f'''
<section class="page-hero"><div class="wrap"><h1>Hostlio Pro fiyatları</h1>
<p class="lead">Sabit aylık ücret. Rezervasyon başına komisyon yok, kurulum ücreti yok. Tüm planları 7 gün ücretsiz deneyebilirsiniz.</p></div></section>
<section style="padding-top:0"><div class="wrap"><h2 class="sr-only">Planlar</h2>
<span class="billing-note">İlk 50 müşteriye %20 indirim, abonelik boyunca sabit</span>
{plans_html()}
<p class="small muted" style="margin-top:18px">Fiyatlar ABD doları cinsindendir, vergiler hariçtir. Son güncelleme: <time datetime="{UPDATED}">21 Eylül 2026</time>.</p>
</div></section>
<section class="white rule"><div class="wrap">
<div class="section-head"><h2>Hangi plan size uygun?</h2></div>
<div class="rows">
<div class="row"><h3>Starter</h3><div><p>10 odaya kadar pansiyon ve butik oteller. Mesaj trafiği ayda 1.000 yanıtı geçmeyen, kanal senkronizasyonu ve AI yanıtla başlamak isteyen işletmeler.</p></div></div>
<div class="row"><h3>Pro</h3><div><p>11–50 odalı oteller. OTA mesajlarını da Lio'ya devretmek, online check-in kullanmak ve transfer/tur satmak isteyenler için.</p></div></div>
<div class="row"><h3>Growth</h3><div><p>İki tesis veya 150 odaya kadar kapasite. Öncelikli destek, birebir kurulum ve kendi markanızla (white-label) kullanım gerektiğinde.</p></div></div>
</div></div></section>
'''
    faq = [FAQ_CORE[2], FAQ_CORE[3],
      ("Rezervasyon başına komisyon alıyor musunuz?", "Hayır. Hostlio Pro sabit aylık abonelikle çalışır; rezervasyon değerinden yüzde almaz."),
      ("Yıllık ödeme seçeneği var mı?", "Evet. Abonelikler aylık veya yıllık peşin faturalandırılır; yıllık planlarda %20 indirim uygulanır (Kullanım Şartları, 3. madde)."),
      ("Plan değiştirebilir miyim?", "Evet. İstediğiniz zaman üst veya alt plana geçebilirsiniz; değişiklik bir sonraki fatura döneminde yansır."),
      ("Erken kayıt indirimi ne kadar sürer?", "İndirim ilk 50 müşteri için geçerlidir ve aboneliğiniz devam ettiği sürece fiyatınız sabit kalır.")]
    return {"key":"pricing","title":"Otel Yazılımı Fiyatları: Aylık 49 $'dan Başlar | Hostlio Pro",
            "desc":"Hostlio Pro fiyatları: Starter 49 $, Pro 89 $, Growth 149 $/ay. Komisyon yok, kurulum ücreti yok, 7 gün ücretsiz deneme. Planları karşılaştırın.",
            "trail":[("Fiyatlandırma", U("pricing"))],"body":body,"faq":faq,"schema":[software_schema(L, detailed=True)]}

FAQ_ALL = FAQ_CORE + [
 ("Hostlio Pro hangi otel tiplerine uygun?", "Butik oteller, şehir otelleri, pansiyonlar, apart oteller ve hosteller gibi 1 ila 150 odalı bağımsız tesisler için tasarlandı."),
 ("Mobil uygulama var mı?", "Evet. Pro ve Growth planlarında iOS uygulaması bulunur. Uygulama internet bağlantısı olmadan da çalışır ve bağlantı geldiğinde verileri senkronize eder."),
 ("Online check-in nasıl çalışıyor?", "Misafire kişiye özel güvenli bir bağlantı gönderilir. Misafir kimlik bilgilerini, refakatçilerini ve dijital imzasını varıştan önce telefonundan gönderir. Pro ve Growth planlarında vardır."),
 ("PDF vize formu özelliği ne işe yarar?", "Vizeye ihtiyaç duyan misafirler için otel konaklama ve davet belgelerini rezervasyon bilgilerinden otomatik olarak PDF'e dönüştürür."),
 ("Verilerim güvende mi?", "Veriler şifreli bağlantı üzerinden iletilir ve her otelin verisi satır düzeyinde erişim kurallarıyla diğer tesislerden ayrılır. Misafir verileri talep üzerine silinebilir."),
 ("Kurulum ne kadar sürer?", "Hesabınız dakikalar içinde hazır olur. Çoğu otel kanallarını aynı gün bağlar: oda tiplerini ve odaları girin, her OTA'nın extranet'inde bağlantıyı yetkilendirin ve odaları eşleyin. Growth planında birebir kurulum görüşmesi dahildir."),
 ("Türkçe destek veriyor musunuz?", "Evet. Panel ve destek Türkçe ve İngilizce sunulur. Bize " + EMAIL + " adresinden ulaşabilirsiniz."),
]

def faq_page():
    body = f'''<section class="page-hero"><div class="wrap"><h1>Sık sorulan sorular</h1>
<p class="lead">Hostlio Pro'nun özellikleri, fiyatları ve kurulumu hakkında en çok sorulanlar. Cevabını bulamadığınız soru için <a href="{U("contact")}">bize yazın</a>.</p></div></section>
<section style="padding-top:0"><div class="wrap">{faq_block(FAQ_ALL, L, heading=False, wrap=False)}</div></section>'''
    return {"key":"faq","title":"Hostlio Pro Hakkında Sık Sorulan Sorular (SSS)",
            "desc":"Hostlio Pro otel yönetim yazılımı hakkında sık sorulan sorular: fiyatlar, ücretsiz deneme, OTA entegrasyonları, AI asistan Lio, online check-in ve güvenlik.",
            "trail":[("SSS", U("faq"))],"body":body,"faq":FAQ_ALL,"faq_inline":True,"page_type":"FAQPage"}

def about():
    body = f'''<section class="page-hero"><div class="wrap split"><div><h1>Hostlio Pro'yu neden yaptık</h1>
<p class="lead">Küçük otellerde resepsiyon, satış ve misafir iletişimi çoğu zaman aynı kişinin omzundadır. Hostlio Pro, bu kişinin gece mesajlara, gündüz kanal ekranlarına gömülmemesi için var.</p></div><div class="hero-img"><img src="/assets/img/gen-shutters.webp" alt="" width="1080" height="1350"></div></div></section>
<section class="white rule"><div class="wrap split">
<div class="prose"><h2>Ne yapıyoruz</h2>
<p>Hostlio Pro, bağımsız oteller için yapay zekâ destekli bir otel yönetim yazılımıdır. Misafir iletişimini AI asistanımız Lio'ya devrediyor, OTA dağıtımını tek takvimde topluyor ve check-in'i misafirin telefonuna taşıyoruz.</p>
<h2>Nasıl çalışıyoruz</h2>
<ul><li>Fiyatlarımızı açıkça yayınlıyoruz, komisyon almıyoruz.</li><li>Yazılımı otelcilerin gerçek günlük işlerinden yola çıkarak geliştiriyoruz.</li><li>Uzun sözleşme istemiyoruz; müşterimiz, memnun kaldığı için kalır.</li></ul></div>
<div class="panel"><p class="panel-title">Şirket bilgileri</p><dl class="list-kv">
<dt>Ürün</dt><dd>Hostlio Pro (Hostlio Pro)</dd><dt>Şirket</dt><dd>Loti Members LLC</dd>
<dt>Adres</dt><dd>2108 N ST STE N, Sacramento, CA 95816, ABD</dd><dt>E-posta</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd>
<dt>Kullanım</dt><dd>20+ ülkede bağımsız oteller</dd></dl></div>
</div></section>'''
    return {"key":"about","title":"Hakkımızda | Hostlio Pro","desc":"Hostlio Pro, bağımsız oteller için yapay zekâ destekli otel yönetim yazılımı geliştirir. Loti Members LLC bünyesinde, 20+ ülkede kullanılıyor.",
            "trail":[("Hakkımızda", U("about"))],"body":body,"page_type":"AboutPage"}

def contact():
    from build import FORM_ENDPOINT
    act = f' action="{FORM_ENDPOINT}" method="post"' if FORM_ENDPOINT else ""
    body = f'''<section class="page-hero"><div class="wrap split" style="align-items:start">
<div><h1>Demo isteyin ya da bize yazın</h1>
<p class="lead">Otelinizi ve kullandığınız kanalları kısaca anlatın; 30 dakikalık bir görüşmede Hostlio Pro'yu kendi odalarınızla gösterelim.</p>
<p>Doğrudan e-posta: <a href="mailto:{EMAIL}">{EMAIL}</a></p></div>
<form class="contact" data-contact-form data-mail="{EMAIL}" data-subject="Demo talebi" data-sent="E-posta uygulamanız açıldı. Göndere bastığınızda talebiniz bize ulaşır."{act}>
<label>Ad soyad<input name="name" autocomplete="name" required></label>
<label>E-posta<input type="email" name="email" autocomplete="email" required></label>
<label>Otel adı<input name="hotel" autocomplete="organization" required></label>
<label>Oda sayısı<select name="rooms"><option>1–10</option><option>11–50</option><option>51–150</option><option>150+</option></select></label>
<label>Ülke / şehir<input name="country" autocomplete="country-name"></label>
<label>Mesajınız <span class="hint">Kullandığınız kanallar, mevcut yazılımınız</span><textarea name="message" rows="4"></textarea></label>
<button class="btn btn-primary" type="submit">Demo talebini gönder</button>
<p class="form-status" role="status" aria-live="polite"></p>
</form></div></section>'''
    return {"key":"contact","title":"İletişim ve Demo Talebi | Hostlio Pro","desc":"Hostlio Pro ekibiyle iletişime geçin veya otelinize özel 30 dakikalık ücretsiz demo isteyin. Türkçe ve İngilizce destek, e-posta: " + EMAIL,
            "trail":[("İletişim", U("contact"))],"body":body,"page_type":"ContactPage","no_final":True}

POSTS = [
 {"key":"post-overbooking","title":"Overbooking nasıl önlenir? Oteller için 6 adım","date":"2026-09-21","desc":"Otellerde overbooking (çift rezervasyon) neden olur ve nasıl önlenir? Kanal yöneticisi, stop-sell, müsaitlik tamponu ve kriz anında yapılacaklar."},
 {"key":"post-autoreply","title":"Booking.com mesajlarına otomatik cevap nasıl verilir?","date":"2026-09-21","desc":"Booking.com misafir mesajlarını otomatik yanıtlamanın üç yolu: hazır şablonlar, planlı mesajlar ve yapay zekâ asistanı."},
 {"key":"post-ai","title":"Otel misafir mesajlarını yapay zekâ ile yanıtlamak: pratik rehber","date":"2026-09-18",
  "desc":"Otel misafir mesajlarını yapay zekâ ile yanıtlamanın avantajları, riskleri ve kurulum adımları. Hangi sorular otomatikleşir, hangileri insanda kalmalı?"},
 {"key":"post-pms","title":"Küçük otel için otel programı (PMS) nasıl seçilir?","date":"2026-09-10",
  "desc":"Küçük ve butik oteller için PMS seçerken bakılması gereken 7 kriter: kanal yöneticisi, fiyat modeli, misafir iletişimi, mobil erişim ve daha fazlası."},
]

def blog():
    items = "".join(f'<article><h2><a href="{U(p["key"])}">{p["title"]}</a></h2><p class="meta"><time datetime="{p["date"]}">{p["date"]}</time></p><p>{p["desc"]}</p></article>' for p in POSTS)
    body = f'<section class="page-hero"><div class="wrap"><h1>Otelciler için blog</h1><p class="lead">Bağımsız otel işletmeciliği, dağıtım ve misafir iletişimi üzerine pratik yazılar.</p></div></section><section style="padding-top:0"><div class="wrap post-list">{items}</div></section>'
    return {"key":"blog","title":"Blog: Bağımsız Oteller için Rehberler | Hostlio Pro","desc":"Otel yönetimi, kanal yönetimi, OTA dağıtımı ve AI ile misafir iletişimi üzerine bağımsız otelcilere yönelik pratik rehberler.",
            "trail":[("Blog", U("blog"))],"body":body,"page_type":"CollectionPage"}

COVERS={"post-ai":("gen-checkin-phone",1080,1350),"post-pms":("gen-owner-laptop",1080,1350),"post-overbooking":("gen-reception",1080,1350),"post-autoreply":("gen-night-desk",1080,1350)}
def article(meta, content, faq=None):
    art = {"@type":"BlogPosting","headline":meta["title"],"description":meta["desc"],"datePublished":meta["date"],"inLanguage":"tr-TR","author":{"@type":"Organization","name":"Hostlio Pro ürün ekibi","url":SITE+"/hakkimizda/"},"dateModified":UPDATED,"publisher":{"@id":SITE+"/#org"},
           "mainEntityOfPage":SITE+U(meta["key"]),"image":SITE+"/assets/img/"+COVERS[meta["key"]][0]+".webp"}
    body = f'<article><section class="page-hero"><div class="wrap"><h1 style="max-width:22ch">{meta["title"]}</h1><p class="meta">Yazan: <a href="/tr/hakkimizda/">Hostlio Pro ürün ekibi</a>, otel yazılımı geliştiren ekip. Yayın: <time datetime="{meta["date"]}">{meta["date"]}</time>, güncelleme: <time datetime="{UPDATED}">{UPDATED}</time></p></div></section><section style="padding-top:0"><div class="wrap"><figure class="post-cover"><img src="/assets/img/{COVERS[meta["key"]][0]}.webp" alt="" width="{COVERS[meta["key"]][1]}" height="{COVERS[meta["key"]][2]}"></figure><div class="prose">{content}</div></div></section></article>'
    return {"key":meta["key"],"title":meta["title"],"desc":meta["desc"],"og_type":"article",
            "trail":[("Blog",U("blog")),(meta["title"],U(meta["key"]))],"body":body,"schema":[art],"faq":faq or []}

def post_ai():
    c = f'''
<div class="answer"><p><strong>Kısa cevap:</strong> Otel mesajlarının büyük kısmı tekrar eden sorulardır (check-in saati, otopark, transfer, kahvaltı). Bu soruları otelin kendi bilgileriyle eğitilmiş bir yapay zekâ asistanına bırakmak, misafire saniyeler içinde kendi dilinde cevap verir; indirim, şikâyet ve özel talepler ise personelde kalmalıdır.</p></div>
<h2>Otellere en çok hangi sorular geliyor?</h2>
<p>Bağımsız otellerde gelen mesajların çoğu birkaç konu etrafında toplanır:</p>
<ul><li>Check-in ve check-out saatleri, erken giriş ya da geç çıkış</li><li>Havalimanı transferi ve ulaşım</li><li>Otopark, kahvaltı, evcil hayvan kuralları</li><li>Bagaj bırakma, oda özellikleri, yakın çevre</li><li>Rezervasyon değişikliği ve fatura talepleri</li></ul>
<p>Bu soruların cevabı otelde zaten yazılıdır; sorun, cevabın doğru dilde ve doğru saatte verilmesidir.</p>
<h2>Yapay zekâ neyi otomatikleştirmeli, neyi otomatikleştirmemeli?</h2>
<p>İyi bir kurulumda asistan bilgi sorularını kapatır, karar gerektiren konuları personele devreder.</p>
<div class="table-wrap"><table><thead><tr><th>AI yanıtlasın</th><th>Personele devredilsin</th></tr></thead><tbody>
<tr><td>Saatler, kurallar, olanaklar</td><td>İndirim ve fiyat pazarlığı</td></tr><tr><td>Yol tarifi, transfer bilgisi</td><td>Şikâyet ve tazminat talepleri</td></tr><tr><td>Transfer ve tur satışı</td><td>Tıbbi veya güvenlikle ilgili durumlar</td></tr><tr><td>Rezervasyon detaylarını hatırlatma</td><td>Grup ve özel etkinlik talepleri</td></tr></tbody></table></div>
<h2>Adım adım kurulum</h2>
<ol><li><strong>Otel bilgi tabanını yazın.</strong> Saatler, kurallar, olanaklar ve sık sorulan sorular. Ne kadar net olursa cevaplar o kadar tutarlı olur.</li>
<li><strong>Kanalları bağlayın.</strong> WhatsApp ve OTA gelen kutusu mesajlarını tek gelen kutusunda toplayın.</li>
<li><strong>Onay modunda başlayın.</strong> İlk hafta asistanın cevaplarını göndermeden önce okuyun ve düzeltin.</li>
<li><strong>Devir kurallarını belirleyin.</strong> Hangi konuların size geleceğini tanımlayın.</li>
<li><strong>Otomatik moda geçin.</strong> Cevaplar tutarlı hale geldiğinde bilgi sorularını tamamen asistana bırakın.</li></ol>
<h2>Çok dilli iletişim neden önemli?</h2>
<p>Misafir kendi dilinde yazdığında daha fazla detay verir ve cevaba daha çok güvenir. 30+ dilde yanıt veren bir asistan, resepsiyonda o dili bilen biri olmasa da bu güveni sağlar. Yazışmayı siz kendi dilinizde okursunuz.</p>
<h2>Hostlio Pro'da nasıl çalışır?</h2>
<p>Hostlio Pro'nun AI asistanı <a href="{U("ai")}">Lio</a>, otel bilgilerinizi ve rezervasyon verilerini kullanarak WhatsApp ve OTA gelen kutusu mesajlarını (Booking.com, Airbnb, Expedia) 30+ dilde yanıtlar. Planlara göre aylık 1.000 ile 12.000 AI mesajı arasında kota bulunur; detaylar <a href="{U("pricing")}">fiyatlandırma sayfasında</a>.</p>'''
    faq = [("Yapay zekâ misafire yanlış bilgi verebilir mi?", "Asistan yalnızca otelin girdiği bilgilerle çalıştığında ve emin olmadığı sorularda personele devrettiğinde bu risk en aza iner. İlk günlerde onay modunda kullanmak önerilir."),
           ("Misafirler yapay zekâyla konuştuğunu anlar mı?", "Cevaplar otelin adına ve tonunda yazılır. Şeffaflık için otel, asistanın bir AI olduğunu karşılama mesajında belirtebilir.")]
    return article(next(p for p in POSTS if p["key"]=="post-ai"), c, faq)

def post_pms():
    c = f'''
<div class="answer"><p><strong>Kısa cevap:</strong> Küçük bir otel için doğru PMS; entegre kanal yöneticisi olan, sabit ve şeffaf fiyatlı, misafir mesajlarını tek yerde toplayan, mobilden yönetilebilen ve aynı gün kurulabilen yazılımdır. Yüzlerce özelliği olan kurumsal sistemler küçük ekipte kullanılmadan kalır.</p></div>
<h2>1. Entegre kanal yöneticisi</h2>
<p>Booking.com, Airbnb ve Expedia'da aynı anda satış yapıyorsanız müsaitliğin anında eşitlenmesi şarttır. Ayrı bir kanal yöneticisi ek maliyet ve ek ekran demektir. PMS'in kanal yöneticisini içermesi ve bağlandığı kanal sayısı ilk bakılacak şeydir.</p>
<h2>2. Fiyat modeli</h2>
<p>Bazı yazılımlar aylık ücretin yanında rezervasyon değerinden yüzde alır. Doluluk arttıkça maliyet de artar. Sabit aylık fiyatlı bir model bütçeyi öngörülebilir kılar. Fiyatını web sitesinde yayınlamayan yazılımlarda teklif sürecine hazırlıklı olun.</p>
<h2>3. Misafir iletişimi</h2>
<p>Mesajlar WhatsApp ve farklı OTA gelen kutularına dağılmışsa cevap süresi uzar. Tek gelen kutusu ve otomatik yanıt, küçük ekipte en büyük zaman kazancıdır.</p>
<h2>4. Oda rafının kullanımı</h2>
<p>Resepsiyonun en çok baktığı ekran rezervasyon takvimidir. Sürükle-bırakla oda değiştirme ve rezervasyonun kanalını bir bakışta görme, günlük işi hızlandırır.</p>
<h2>5. Mobil erişim</h2>
<p>Otel sahibi çoğu zaman otelin dışındadır. Mobil uygulama, özellikle internet kesintisinde çalışabiliyorsa, gerçek bir ihtiyaçtır.</p>
<h2>6. Online check-in</h2>
<p>Misafir bilgilerinin varıştan önce toplanması hem resepsiyonda zaman kazandırır hem de yasal bildirimleri kolaylaştırır.</p>
<h2>7. Kurulum ve destek</h2>
<p>Küçük bir otel haftalarca süren bir kurulum projesini kaldıramaz. Aynı gün kullanılabilen, kendi dilinizde destek veren bir yazılım seçin ve deneme süresini gerçek rezervasyonlarla test edin.</p>
<h2>Kontrol listesi</h2>
<div class="table-wrap"><table><thead><tr><th>Kriter</th><th>Sorulacak soru</th></tr></thead><tbody>
<tr><td>Kanal yöneticisi</td><td>Dahil mi, kaç kanala bağlanıyor?</td></tr><tr><td>Fiyat</td><td>Sabit mi, komisyon var mı, fiyat açık mı?</td></tr>
<tr><td>Mesajlaşma</td><td>WhatsApp ve OTA mesajları tek yerde mi, otomatik yanıt var mı?</td></tr><tr><td>Mobil</td><td>Uygulama var mı, çevrimdışı çalışıyor mu?</td></tr>
<tr><td>Check-in</td><td>Online check-in ve dijital imza var mı?</td></tr><tr><td>Deneme</td><td>Ücretsiz deneme ve taahhütsüz iptal var mı?</td></tr></tbody></table></div>
<p>Hostlio Pro bu kriterlere göre tasarlandı: <a href="{U("features")}">özellikleri</a> ve <a href="{U("pricing")}">fiyatları</a> inceleyebilirsiniz.</p>'''
    faq = [("Küçük bir otel için PMS gerekli mi?", "Birden fazla OTA'da satış yapıyor ve günde onlarca mesaj alıyorsanız evet. Excel ve ayrı OTA panelleriyle çalışmak overbooking ve geciken cevap riskini artırır."),
           ("PMS ile kanal yöneticisi arasındaki fark nedir?", "PMS otelin iç operasyonunu (rezervasyon, oda, misafir) yönetir; kanal yöneticisi ise müsaitlik ve fiyatı OTA'lara dağıtır. Hostlio Pro gibi yazılımlar ikisini tek panelde birleştirir.")]
    return article(next(p for p in POSTS if p["key"]=="post-pms"), c, faq)

def pages():
    import pages_v4
    return [home(), ai(), channel(), checkin(), features(), pricing(), faq_page(), about(), contact(), blog(), post_ai(), post_pms()] + pages_v4.pages(L, article) + __import__("legal_v5").pages(L, article)
