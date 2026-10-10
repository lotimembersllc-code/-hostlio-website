"""Türkçe içerik paketi (SEO raporu bölüm 8: #4, #5, #6, #13). Yalnız TR.
- post-channel-manager: "Channel manager nedir?" rehberi
- post-kbs: "KBS bildirimi nasıl yapılır?" (resmî kaynaklar 8 Ekim 2026'da doğrulandı; Hostlio yalnız CSV dışa aktarır,
  KBS'ye OTOMATİK BİLDİRİM YAPMAZ — metin bunu açıkça söyler)
- post-prices: "Otel programı fiyatları 2026" (rakip fiyatları resmî fiyat sayfalarından, 8 Ekim 2026)
- whatsapp-tr: "Otel WhatsApp asistanı" landing'i (Lio — yalnız canlı yetenekler)
Blog listesi için content_tr.POSTS ve COVERS'a da kayıt eklendi.
"""
import html

SRC_DATE = "8 Ekim 2026"

def _src(items):
    lis = "".join(f'<li><a href="{u}" rel="nofollow noopener">{html.escape(n)}</a></li>' for n, u in items)
    return f'<h2>Kaynaklar</h2><p class="small muted">Tüm kaynaklara {SRC_DATE} tarihinde erişildi.</p><ul>{lis}</ul>'

def _tbl(head, rows, cls="", hl_col=None):
    """hl_col: vurgulanacak sütun (Hostlio Pro); ilk hücresi "Hostlio Pro" olan satır da vurgulanır (style.css table.cmp)."""
    hc = lambda i: ' class="hl"' if i == hl_col else ""
    h = "".join(f'<th scope="col"{hc(i)}>{x}</th>' for i, x in enumerate(head))
    b = "".join(("<tr class=\"hl\">" if r[0] == "Hostlio Pro" else "<tr>") + f'<th scope="row">{r[0]}</th>'
                + "".join(f"<td{hc(i)}>{c}</td>" for i, c in enumerate(r[1:], 1)) + "</tr>" for r in rows)
    return f'<div class="table-wrap"><table class="cmp"><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table></div>'

# ------------------------------------------------------------------ channel manager nedir
def channel_manager(U):
    c = f'''<div class="answer"><p><strong>Kısa cevap:</strong> Channel manager (kanal yöneticisi), otelinizin müsaitliğini, fiyatlarını ve satış kısıtlamalarını Booking.com, Airbnb, Expedia gibi tüm online satış kanallarına tek yerden gönderen ve bu kanallardan gelen rezervasyonları tek takvimde toplayan yazılımdır. Bir kanaldan rezervasyon geldiğinde o oda diğer kanallarda da otomatik kapanır; böylece overbooking riski azalır ve her kanalın extranet'ine ayrı ayrı girmeniz gerekmez.</p></div>
<h2>Channel manager nasıl çalışır?</h2>
<p>Kanal yöneticisinin işi iki yönlü bir veri akışıdır:</p>
<ul><li><strong>Otelden kanallara:</strong> müsaitlik (kaç oda satılabilir), fiyat ve kısıtlamalar. Sektörde buna kısaca ARI (availability, rates, inventory) denir. Kısıtlamalar; minimum ve maksimum konaklama, girişe kapalı (CTA), çıkışa kapalı (CTD) ve satışa kapama (stop-sell) gibi kurallardır.</li>
<li><strong>Kanallardan otele:</strong> yeni rezervasyonlar, değişiklikler ve iptaller. Bunlar takviminize düşer ve müsaitlik yeniden hesaplanıp tüm kanallara gönderilir.</li></ul>
<p>Örnek: 8 odalı bir pansiyonda son boş oda Airbnb'den satıldı. Kanal yöneticisi rezervasyonu alır, o tarihte müsaitliği sıfıra indirir ve Booking.com ile Expedia'ya da “0 oda” gönderir. Siz hiçbir extranet'e girmeden oda tüm kanallarda kapanmış olur.</p>
<h2>Channel manager ile PMS arasındaki fark</h2>
{_tbl(["Konu", "Channel manager", "PMS (otel programı)"], [
  ("Ana görevi", "Satış kanallarıyla müsaitlik, fiyat ve rezervasyon alışverişi", "Otelin günlük işleyişi: rezervasyon takvimi, oda durumu, misafir kayıtları, raporlar"),
  ("Kimlerle konuşur", "OTA'lar ve diğer satış kanalları", "Resepsiyon, kat hizmetleri, yönetim"),
  ("Tek başına yeterli mi", "Çoğu zaman bir PMS ya da takvimle birlikte kullanılır", "Kanal bağlantısı yoksa müsaitliği kanallara elle girmeniz gerekir")])}
<p>Küçük otellerde ikisini ayrı ayrı almak yerine kanal yöneticisi PMS'e yerleşik bir sistem seçmek, iki yazılım arasındaki senkron sorunlarını ortadan kaldırır. Ayrıntılı seçim kriterleri için <a href="{U("post-pms")}">küçük otel için otel programı seçimi</a> rehberine bakın.</p>
<h2>Neden gerekli?</h2>
<ul><li><strong>Overbooking riskini azaltır.</strong> Elle güncellemede iki kanal aynı odayı aynı anda satabilir. Nasıl önleneceğini <a href="{U("post-overbooking")}">overbooking rehberinde</a> anlattık.</li>
<li><strong>Zaman kazandırır.</strong> Sezon fiyatını bir kez girersiniz, tüm kanallara gider.</li>
<li><strong>Fiyatlarınız tutarlı kalır.</strong> Bir kanalı güncelleyip diğerini unutma ihtimali ortadan kalkar.</li>
<li><strong>Daha fazla kanalda görünmenizi kolaylaştırır.</strong> Yeni bir kanal eklemek, ayrı bir takvimi yönetmek anlamına gelmez.</li></ul>
<h2>Kanal yöneticisi fiyat modelleri</h2>
<p>Yazılımlar kanal yöneticisini farklı şekillerde fiyatlandırır. Firmaların kendi sayfalarında yayınladığı örnekler ({SRC_DATE}):</p>
<ul><li><strong>Sabit aylık ücret:</strong> Oda sayısından ya da gelirden bağımsız tek fiyat. Hostlio Pro'da kanal yöneticisi tüm planlara dahildir (aylık ⟦price:starter⟧'dan).</li>
<li><strong>Oda kademesine göre:</strong> Örneğin Sirvoy'da 10 odaya kadar Pro planı aylık 79 €; kanal yöneticisi bu yazılımda yalnızca Pro planında yer alıyor.</li>
<li><strong>Oda ve kanal başına:</strong> Beds24 taban ücret, oda başı ücret ve kanal bağlantısı başına ücret alıyor (aylık 15,50 €'dan başlıyor).</li>
<li><strong>Gelir yüzdesi:</strong> HotelRunner'ın Essential planları aylık rezervasyon gelirinin %0,75–%1,25'ini alıyor, her planın asgari aylık tutarı var.</li></ul>
<p>Rakamların tamamı ve kaynakları için <a href="{U("post-prices")}">otel programı fiyatları 2026</a> rehberine bakın.</p>
<h2>Channel manager seçerken 7 soru</h2>
<ol><li>Sattığım tüm kanallara (Booking.com, Airbnb, Expedia, Agoda…) sertifikalı bağlantısı var mı?</li>
<li>Senkron anlık mı, yoksa belirli aralıklarla mı yapılıyor?</li>
<li>Fiyat ve kısıtlamaları (min. konaklama, CTA, CTD, stop-sell) tarih aralığına toplu girebiliyor muyum?</li>
<li>PMS'e yerleşik mi, yoksa ayrı bir sistemle mi entegre?</li>
<li>Fiyat modeli ne: sabit, oda başı, rezervasyon başı ya da gelir yüzdesi? Yüksek sezonda maliyet nasıl değişir?</li>
<li>Oda eşlemesini kim yapıyor; kurulumda destek var mı, hangi dilde?</li>
<li>Gerçek oda ve fiyatlarımla deneyebileceğim ücretsiz bir deneme süresi var mı?</li></ol>
<h2>Kurulum nasıl yapılır?</h2>
<ol><li>Oda tiplerinizi ve fiyat planlarınızı yazılıma girin.</li>
<li>Her kanalın extranet'inde kanal yöneticisi bağlantısını yetkilendirin.</li>
<li>Kanaldaki oda ve fiyat planlarını yazılımdakilerle eşleyin.</li>
<li>Bir test tarihinde müsaitliği değiştirip tüm kanallara yansıdığını kontrol edin.</li>
<li>Eski sistemden geçiyorsanız kesin bir geçiş saati belirleyin; müsaitlik aynı anda iki sistemden güncellenmesin.</li></ol>
<h2>Hostlio Pro'da kanal yöneticisi</h2>
<p>Hostlio Pro'nun <a href="{U("channel")}">kanal yöneticisi</a> tüm planlara dahildir ve sertifikalı bağlantılarla 100'den fazla kanala (Booking.com, Airbnb, Expedia, Agoda, Trip.com, Hotels.com, Hotelbeds, Hostelworld, Google Hotels ve diğerleri) bağlanır. Oda tipi ve fiyat planı ızgarasında fiyat, minimum ve maksimum konaklama, girişe ve çıkışa kapalı ve satışa kapama kurallarını tarih aralığına toplu girersiniz. Arızalı bir odayı “satış dışı” yaptığınızda oda OTA müsaitliğinden de otomatik düşer. Analiz ekranı her kanalın brüt gelirini, komisyonunu ve net gelirini gösterir; komisyon sonrası tabloyu kendiniz görmek için <a href="{U("commission")}">OTA komisyon hesaplayıcısını</a> da kullanabilirsiniz.</p>'''
    faq = [("Channel manager ne iş yapar?", "Müsaitliğinizi, fiyatlarınızı ve kısıtlamalarınızı tüm online satış kanallarına tek yerden gönderir ve kanallardan gelen rezervasyonları tek takvimde toplar. Bir kanaldan gelen rezervasyon, odayı diğer kanallarda da otomatik kapatır."),
           ("Kanal yöneticisi ile otel programı (PMS) aynı şey mi?", "Hayır. PMS otelin günlük işleyişini (rezervasyon takvimi, oda durumu, misafir kayıtları) yönetir; kanal yöneticisi ise satış kanallarıyla veri alışverişi yapar. Birçok yazılımda ikisi tek pakette sunulur."),
           ("Ücretsiz channel manager var mı?", "Bazı yazılımların ücretsiz planı vardır, ancak kanal yöneticisi her planda olmayabilir. Örneğin Sirvoy'un fiyat sayfasında kanal yöneticisi yalnızca Pro planında yer alıyor. Planın neleri kapsadığını mutlaka kontrol edin."),
           ("Booking.com ve Airbnb'yi aynı anda nasıl senkron tutarım?", "İki kanalı da aynı kanal yöneticisine bağlarsınız. Müsaitlik tek takvimden yönetilir; bir kanaldan rezervasyon geldiğinde diğer kanaldaki müsaitlik otomatik güncellenir.")]
    return c, faq

# ------------------------------------------------------------------ KBS
KBS_SRC = [
 ("1774 sayılı Kimlik Bildirme Kanunu (mevzuat.gov.tr)", "https://www.mevzuat.gov.tr/MevzuatMetin/1.5.1774.pdf"),
 ("Kimlik Bildirme Kanununun Uygulanması ile İlgili Yönetmelik (mevzuat.gov.tr)", "https://www.mevzuat.gov.tr/File/GeneratePdf?mevzuatNo=9484&mevzuatTur=KurumVeKurulusYonetmeligi&mevzuatTertip=5"),
 ("Konutların Turizm Amaçlı Kiralanması Yönetmeliği (mevzuat.gov.tr)", "https://mevzuat.gov.tr/MevzuatMetin/yonetmelik/7.5.40522.pdf"),
 ("7565 sayılı Kanun, Resmî Gazete 5 Aralık 2025", "https://www.resmigazete.gov.tr/eskiler/2025/12/20251205-6.htm"),
 ("Emniyet Genel Müdürlüğü: Kimlik Bildirim Sistemi", "https://www.egm.gov.tr/kimlik-bildirim-sistemi"),
 ("EGM Asayiş Daire Başkanlığı: KBS", "https://www.asayis.pol.tr/kmlkbldrmsstm"),
 ("EGMSEC iki faktörlü doğrulama kılavuzu (KBS)", "https://m.egm.gov.tr/EGMSEC/KBS-K%C4%B1lavuz.pdf"),
 ("Kocaeli İl Emniyet Müdürlüğü: KBS projesi", "https://www.kocaeli.pol.tr/kimlik-bildirim-sistemi-kbs-projesi"),
 ("Jandarma Genel Komutanlığı: Kimlik Bildirim Sistemi", "https://www.jandarma.gov.tr/kimlik-bildirim-sistemi"),
 ("Jandarma KBS Tesis 2 uygulama dokümanı", "https://www.jandarma.gov.tr/kurumlar/jandarma.gov.tr/Jandarma/Uygulamalar/KBS/KBS_Tesis_2_Uygulama_TD.pdf"),
 ("Jandarma KBS Tesis 2 geçiş işlemleri", "https://www.jandarma.gov.tr/kurumlar/jandarma.gov.tr/Jandarma/Uygulamalar/KBS/KBS_Tesis_2_Gecis_Islemleri.pdf"),
 ("Jandarma KBS web servis tanım dokümanı", "https://www.jandarma.gov.tr/kurumlar/jandarma.gov.tr/Jandarma/Uygulamalar/KBS/KBS_Tesis_2_WebServis_TD.pdf"),
 ("e-Devlet: Jandarma Kimlik Bildirim Sistemi", "https://www.turkiye.gov.tr/jandarma-kimlik-bildirim-sistemi"),
 ("5326 sayılı Kabahatler Kanunu (mevzuat.gov.tr)", "https://www.mevzuat.gov.tr/MevzuatMetin/1.5.5326.pdf"),
]

def kbs(U):
    c = f'''<div class="answer"><p><strong>Kısa cevap:</strong> KBS (Kimlik Bildirim Sistemi), konaklama tesislerinin misafirlerinin ve çalışanlarının kimlik bilgilerini kolluğa elektronik ortamda bildirdiği sistemdir. 1774 sayılı Kimlik Bildirme Kanunu'na göre bildirim <strong>anlık</strong> yapılmalıdır. Tesisiniz polis bölgesindeyse Emniyet'in <code>kbs.egm.gov.tr</code> adresini, jandarma bölgesindeyse e-Devlet üzerinden Jandarma KBS'yi kullanırsınız. Kayıt için bağlı olduğunuz polis birimine ya da jandarma karakoluna başvurursunuz.</p></div>
<p class="small muted">Bu yazı genel bilgilendirme amaçlıdır, hukuki danışmanlık değildir. Bilgiler {SRC_DATE} tarihinde resmî kaynaklardan derlendi; uygulama ilden ile değişebilir. Güncel şartları bağlı olduğunuz polis birimine ya da jandarma karakoluna sorun.</p>
<h2>KBS bildirimi kimler için zorunlu?</h2>
<p>1774 sayılı Kanun'un 2. maddesi otel, motel, han, pansiyon, bekâr odaları, günübirlik kiralanan evler, kamp, kamping, tatil köyü, marinalar ve <em>benzeri her türlü</em> özel veya resmî konaklama yerinin sorumlu işleticisini, yerli ya da yabancı herkesin kimlik ve geliş-ayrılış kayıtlarını tutmakla yükümlü kılar. Kanun'un ek 1. maddesi bu kayıtların bilgisayarda günü gününe tutulmasını ve kolluğa <em>anlık olarak</em> bildirilmesini zorunlu tutar; KBS'nin dayanağı bu maddedir.</p>
<p>Uygulama yönetmeliği apart otelleri de konaklama işletmeleri arasında sayar. Turizm amaçlı kiralanan konutlar için Kültür ve Turizm Bakanlığı yönetmeliği de izin belgesi sahibinin 1774 sayılı Kanun'daki yükümlülükleri yerine getirmesini şart koşar.</p>
<h2>Emniyet KBS mi, Jandarma KBS mi?</h2>
{_tbl(["Konu", "Polis bölgesi (Emniyet)", "Jandarma bölgesi"], [
  ("Sistem", "Emniyet Genel Müdürlüğü KBS (2017'den beri)", "Jandarma KBS (“KBS Tesis 2”)"),
  ("Adres", "kbs.egm.gov.tr", "e-Devlet: turkiye.gov.tr/jandarma-kimlik-bildirim-sistemi ya da jandarma.gov.tr/kbs"),
  ("Giriş", "Kullanıcı adı, parola ve EGMSEC uygulamasından alınan tek kullanımlık şifre", "Tesis yetkilisinin e-Devlet girişiyle"),
  ("Başvuru yeri", "Tesisin bağlı olduğu güvenlik birimi (polis)", "Tesisten sorumlu Jandarma Karakol Komutanlığı")])}
<p>Tesisinizin hangi bölgede olduğunu gösteren resmî bir çevrimiçi sorgu bulamadık; emin değilseniz en yakın polis merkezine ya da jandarma karakoluna sorun.</p>
<h2>KBS'ye kayıt: adım adım</h2>
<h3>Polis bölgesindeki tesisler</h3>
<ol><li>Tesis yetkilisi, tesisin bağlı olduğu güvenlik birimine başvurarak kayıt yaptırır (EGM Asayiş Daire Başkanlığı).</li>
<li>İstenen belgeler ilden ile değişebilir. Örneğin Kocaeli İl Emniyet Müdürlüğü gerçek kişiler için işyeri açma ve çalıştırma ruhsatı, vergi levhası, nüfus cüzdanı fotokopisi, dilekçe, KBS kullanıcı bilgi formu ve turizm işletme ya da konut izin belgesi istiyor; şirketlerde ticaret sicil gazetesi ve imza beyannamesi de ekleniyor.</li>
<li>Aynı il müdürlüğünün açıklamasına göre parola kayıtta bildirilen e-posta adresine gelir, kullanıcı adı e-posta adresidir ve sabit IP adresi tanımlanmayan tesis sisteme giremez.</li>
<li>Girişte telefonunuza kuracağınız EGMSEC uygulamasının ürettiği tek kullanımlık şifre de istenir.</li></ol>
<h3>Jandarma bölgesindeki tesisler</h3>
<ol><li>Tesis yetkilisi geçiş/bildirim formunu doldurarak tesisten sorumlu Jandarma Karakol Komutanlığına başvurur. Formda tesis bilgileri, adres kodu, koordinat ve yetkili kullanıcının T.C. kimlik numarası gibi alanlar bulunur.</li>
<li>Yetki karakol tarafından tanımlanır; sonra tesis yetkilisi e-Devlet şifresiyle sisteme girer.</li>
<li>Tesis yetkilisi kendi altına konaklayan, personel ya da her ikisini bildirebilecek başka kullanıcılar ekleyebilir; her kullanıcı kendi e-Devlet şifresiyle girer.</li></ol>
<h2>Misafir bildirimi nasıl yapılır?</h2>
<p>Jandarma KBS dokümanına göre:</p>
<ul><li><strong>T.C. vatandaşı:</strong> T.C. kimlik numarası, oda numarası ve giriş tarihi girilir; varsa araç plakası ve telefon eklenir. Ad, soyad gibi bilgiler kontrol için nüfus kayıtlarından ekrana gelir.</li>
<li><strong>Yabancı kimlik numarası olan yabancı:</strong> Yabancı kimlik numarası, ülke, oda numarası ve giriş tarihi girilir.</li>
<li><strong>Diğer yabancı misafirler:</strong> Kimlik bilgilerinin tamamı elle girilir; pasaport numarası “Belge Seri No” alanına yazılır ve ülke seçilir. Jandarma'nın duyurusuna göre yabancı turistler için ana adı, baba adı, medeni hal ve cinsiyet bildirme zorunluluğu kaldırılmıştır.</li>
<li><strong>Çıkış:</strong> Misafir ayrıldığında çıkış kaydı yapılır. Kocaeli İl Emniyet Müdürlüğü'nün tesislere yönelik notunda çıkışın “çıkış anında” yapılması isteniyor.</li></ul>
<p>Emniyet KBS ekranındaki alanlar oturum açmadan görülemediği için yabancı misafirde hangi alanların zorunlu olduğunu ekranınızdan kontrol edin.</p>
<h2>Bildirim süresi: “anlık” ne demek?</h2>
<p>Kanun ve yönetmelik misafir bildirimi için saat cinsinden bir süre vermez; ölçüt <strong>anlık</strong> bildirimdir. Jandarma sistemi teknik aksaklıklar nedeniyle giriş kaydının 72 saat, çıkışın üç gün geriye dönük girilmesine izin verir; bu bir yasal süre değil, sistemin teknik toleransıdır. Çalışanların işe giriş ve ayrılışı ise Kanun'un 4. maddesine göre <strong>24 saat</strong> içinde bildirilir.</p>
<h2>KBS bildirimi yapılmazsa ceza nedir?</h2>
<ul><li>Kanun'un ek 1. maddesine göre kolluk terminaline bağlanmayan tesise 10.000 TL, anlık veri göndermeyen ya da gerçeğe aykırı kayıt tutan tesise 5.000 TL idari para cezası verilir. Bu tutarlar Kanun'daki nominal tutarlardır; Kabahatler Kanunu gereği her yıl yeniden değerleme oranıyla artırılır.</li>
<li>Kocaeli İl Emniyet Müdürlüğü'nün 2026 bilgilendirmesinde bu tutarlar 2026 yılı için 170.903 TL (sisteme dahil olmadan faaliyet) ve 85.437 TL (anlık bildirim yapmama ya da gerçeğe aykırı kayıt) olarak veriliyor. Ulusal düzeyde yayınlanmış resmî bir 2026 tablosu bulamadık.</li>
<li>5 Aralık 2025'te yürürlüğe giren 7565 sayılı Kanun'la, aynı takvim yılında tekrarında son cezanın iki katı uygulanması ve dördüncü kez işlenmesinde işletme ruhsatının iptali hükme bağlandı.</li></ul>
<h2>Sık yapılan hatalar</h2>
<ul><li>Misafiri kayıt yapılmadan odaya çıkarmak.</li>
<li>Çıkış kaydını günler sonra toplu yapmak.</li>
<li>Grup ya da aile konaklamalarında bireylerden birini eksik bırakmak.</li>
<li>Yabancı misafirde pasaport numarasını yanlış alana ya da eksik yazmak.</li>
<li>Yeni çalışanı 24 saat içinde bildirmemek.</li></ul>
<h2>Online check-in ile bilgileri önceden toplamak</h2>
<p>Resepsiyondaki yükü azaltmanın bir yolu, misafir bilgilerini varıştan önce toplamaktır. Hostlio Pro'nun <a href="{U("checkin")}">online check-in</a> özelliğinde (Pro ve Growth planları) misafir pasaportunun ya da kimlik kartının makinece okunabilir bölgesini (MRZ) kendi telefonuyla okutur; okuma tarayıcıda yapılır ve yalnızca çıkarılan alanlar ile dijital imza kaydedilir, belge görüntüsü saklanmaz.</p>
<p>Hostlio Pro panelindeki <strong>KBS dışa aktarma</strong>, seçtiğiniz tarih aralığındaki misafirleri (iptal edilen rezervasyonlar hariç) ad soyad, belge tipi, belge numarası, uyruk, doğum tarihi, giriş tarihi ve kayıt zamanıyla tek bir CSV dosyasında toplar.</p>
<div class="answer"><p><strong>Önemli:</strong> Hostlio Pro KBS'ye bağlanmaz ve KBS'ye <strong>otomatik bildirim yapmaz</strong>. CSV dosyası, bildirimi kendi KBS ekranınızdan yaparken bilgileri tek yerde görmeniz içindir; bildirimi yapmak ve süresine uymak tesisin sorumluluğundadır.</p></div>'''
    c += _src(KBS_SRC)
    faq = [("KBS bildirimi ne zaman yapılır?", "1774 sayılı Kanun'un ek 1. maddesine göre misafir bilgileri kolluğa anlık olarak bildirilir; mevzuatta saat cinsinden ayrı bir süre yoktur. Çalışanlar ise 24 saat içinde bildirilir."),
           ("KBS'ye nasıl kayıt olunur?", "Polis bölgesindeki tesisler bağlı oldukları güvenlik birimine, jandarma bölgesindeki tesisler sorumlu Jandarma Karakol Komutanlığına başvurur. İstenen belgeler ilden ile değişebilir; başvurmadan önce ilgili birime sorun."),
           ("Yabancı misafir KBS'ye nasıl bildirilir?", "Jandarma KBS'de yabancı kimlik numarası olmayan misafirin kimlik bilgileri elle girilir, pasaport numarası “Belge Seri No” alanına yazılır ve ülke seçilir. Emniyet KBS'de zorunlu alanları kendi ekranınızdan kontrol edin."),
           ("Hostlio Pro KBS'ye otomatik bildirim yapıyor mu?", "Hayır. Hostlio Pro, online check-in ile toplanan bilgileri tarih aralığına göre CSV olarak dışa aktarır. KBS'ye bağlanmaz ve bildirim göndermez; bildirimi KBS ekranınızdan siz yaparsınız."),
           ("KBS bildirimi yapılmazsa ceza var mı?", "Evet. Kanun'un ek 1. maddesi sisteme bağlanmayan ve anlık bildirim yapmayan tesislere idari para cezası öngörür; tutarlar her yıl yeniden değerleme oranıyla artar. Aynı yıl içinde dördüncü kez tekrarında işletme ruhsatı iptal edilir.")]
    return c, faq

# ------------------------------------------------------------------ otel programı fiyatları 2026
PRICE_SRC = [
 ("HMS Otel: Fiyat listesi", "https://www.hmsotel.com/fiyat-listesi/"),
 ("HotelRunner: Fiyatlandırma", "https://hotelrunner.com/tr/fiyatlandirma/"),
 ("AKINSOFT: WOLVOX Otel Programı", "https://www.akinsoft.com.tr/programlar/detay/wolvox-otel-programi--who9"),
 ("Sirvoy: Pricing", "https://sirvoy.com/pricing"),
 ("Beds24: Pricing", "https://beds24.com/pricing.html"),
 ("eviivo: Pricing", "https://eviivo.com/pricing/"),
 ("Elektraweb: Fiyat listesi (teklif formu)", "https://www.elektraweb.com/elektraweb-fiyat-listesi/"),
 ("Sistem Otel", "https://www.sistemotel.com/"),
 ("Cloudbeds: Pricing", "https://www.cloudbeds.com/pricing/"),
 ("Amenitiz: Pricing", "https://amenitiz.com/en/pricing"),
]
def b24(rooms, types, channels): return 12.90 + 2.60 * rooms + 0.55 * types * channels

def prices(U):
    from build import btn, SIGNUP_URL
    cta = btn("7 gün ücretsiz dene", SIGNUP_URL) + btn("Planları gör", U("pricing"), "ghost")
    def eur(x): return f"{x:,.2f} €".replace(",", "X").replace(".", ",").replace("X", ".").replace(",00 €", " €")
    rows = [
      ("Hostlio Pro", "Sabit aylık ücret (plan)", "Starter ⟦price:starter⟧, Pro ⟦price:pro⟧, Growth ⟦price:growth⟧ / ay (USD, erken kayıt); yıllıkta %20 indirim", "PMS, kanal yöneticisi ve AI asistan Lio tüm planlarda; oda sınırı 10 / 50 / 150"),
      ("HMS Otel", "Oda aralığına göre sabit paket", "1–10 oda 88 €, 11–20 oda 100 €, 21–30 oda 112 €, 31–40 oda 124 €, 41–50 oda 136 € / ay; 51+ oda teklifle", "Kurulum, uzaktan eğitim ve teknik destek için ek ücret alınmıyor; misafir ilişkileri modülü (SMS/e-posta) ayrıca ücretli"),
      ("HotelRunner", "Rezervasyon gelirinden yüzde + asgari ücret", "Essential Manage %0,75 (asgari 19,95 $), Sell %1,25 (asgari 29,95 $), Complete %1 (asgari 39,95 $) / ay", "Yüzde, tüm kanallardan gerçekleşen aylık rezervasyon gelirine uygulanıyor; Advanced ve Elite teklifle"),
      ("AKINSOFT WOLVOX Otel", "Tek seferlik lisans", "Otel Yönetimi 1 (50 oda dahil): liste fiyatı 102.950 ₺, KDV hariç", "Ekim 2026'da süreli kampanya indirimi uygulanıyor (sayfaya göre 27 Ekim 2026'ya kadar)"),
      ("Sirvoy", "Oda kademesine göre sabit aylık", "10 odaya kadar: Starter 22 €, Pro 79 € / ay (aylık ödeme); 1 oda için ücretsiz plan", "Kanal yöneticisi yalnızca Pro planında; 14 gün deneme"),
      ("Beds24", "Kullandıkça öde", "Taban 12,90 € + oda başı 2,60 € + oda tipi başına kanal bağlantısı 0,55 € / ay; “15,50 €'dan başlayan”", "Kurulum ücreti ve taahhüt yok"),
      ("eviivo", "“Başlayan” fiyat + rezervasyon başı ücret", "Tek tesis 50 $'dan başlayan / ay, vergiler hariç; onaylanan rezervasyon başına 0,50 $", "10 odanın üzerinde hacim fiyatı teklifle; 14 gün ücretsiz"),
      ("Elektraweb, Sistem Otel", "Teklif", "Yayınlanmıyor", "Fiyat sayfaları teklif formuna yönlendiriyor"),
      ("Cloudbeds, Amenitiz", "Teklif", "Yayınlanmıyor", "Fiyat sayfalarında teklif isteniyor")]
    ex = [(10, 2, 3), (25, 3, 3), (50, 4, 4)]
    hms = {10: "88 €", 25: "112 €", 50: "136 €"}
    sv = {10: "79 € (Pro, 10 odaya kadar)", 25: "149 € (Pro, 50 odaya kadar)", 50: "149 € (Pro, 50 odaya kadar)"}
    hl = {10: "⟦price:starter⟧ (Starter) ya da ⟦price:pro⟧ (Pro)", 25: "⟦price:pro⟧ (Pro)", 50: "⟦price:pro⟧ (Pro, 50 odaya kadar)"}
    ex_rows = [(f"{r} oda ({t} oda tipi, {ch} kanal)", hl[r], hms[r], sv[r], eur(b24(r, t, ch))) for r, t, ch in ex]
    c = f'''<div class="answer"><p><strong>Kısa cevap:</strong> 2026'da otel programları dört farklı şekilde fiyatlanıyor: sabit aylık paket, oda sayısına göre ücret, rezervasyon gelirinden yüzde ve tek seferlik lisans. Fiyatını açıkça yayınlayan yazılımlarda küçük bir otel için aylık maliyet yaklaşık 15 € ile 150 € arasında başlıyor; bazı büyük firmalar ise yalnızca teklif veriyor. Aşağıdaki tablo, firmaların kendi fiyat sayfalarında {SRC_DATE} tarihinde yayınladığı rakamlara dayanıyor.</p></div>
<p class="small muted">Hostlio Pro bu karşılaştırmada taraftır. Yalnızca resmî fiyat sayfasında doğrulayabildiğimiz rakamları yazdık; fiyatlar değişebilir, karar vermeden önce her firmanın kendi sayfasını kontrol edin. Para birimleri firmaların kullandığı gibidir (€, $, ₺) ve doğrudan karşılaştırılamaz.</p>
<h2>Hostlio Pro ne kadar?</h2>
<p>Hostlio Pro'nun üç planı vardır: Starter aylık ⟦price:starter⟧ (10 oda), Pro ⟦price:pro⟧ (50 oda) ve Growth ⟦price:growth⟧ (150 oda, 2 tesis). Fiyat sabittir: Hostlio rezervasyon başına ücret ya da gelir yüzdesi almaz, yüksek sezonda faturanız büyümez. Sertifikalı kanal yöneticisi (100+ OTA) ve WhatsApp'ta misafirlere cevap veren AI asistan Lio tüm planlarda dahildir. Yıllık ödemede %20 indirim vardır; 7 gün ücretsiz deneyebilirsiniz.</p>
<div class="cta-row" style="margin-top:12px">{cta}</div>
<h2>Otel programı fiyat modelleri</h2>
<ul><li><strong>Sabit aylık paket:</strong> Ücret belli bir oda aralığı ya da plan için sabittir. Bütçe öngörülebilir; yüksek sezonda fatura büyümez.</li>
<li><strong>Oda başı ya da oda kademesi:</strong> Oda sayısı arttıkça ücret artar. Küçük tesisler için ucuz başlar.</li>
<li><strong>Gelir yüzdesi ya da rezervasyon başı ücret:</strong> Düşük sezonda az ödersiniz, yüksek sezonda maliyet gelirle birlikte büyür.</li>
<li><strong>Tek seferlik lisans:</strong> Yazılımı satın alırsınız; güncelleme, sunucu ve destek maliyetlerini ayrıca sorun.</li>
<li><strong>Teklif:</strong> Fiyat, demo sonrası tesisinize göre verilir.</li></ul>
<h2>2026 otel programı fiyatları (yayınlanan rakamlar)</h2>
{_tbl(["Yazılım", "Model", "Yayınlanan fiyat", "Not"], rows)}
<h2>Örnek hesap: 10, 25 ve 50 odalı otel</h2>
<p>Aşağıdaki aylık rakamlar yayınlanan fiyatlardan yaptığımız hesaptır. Beds24 için resmî hesaplayıcısındaki birim fiyatları kullandık (taban + oda başı + oda tipi × kanal). Rezervasyon gelirine bağlı modeller (HotelRunner, eviivo) gelirinize göre değiştiği için tabloya alınmadı; HotelRunner için gelire göre örnek hesabı <a href="{U("vs-hotelrunner")}">Hostlio Pro ile HotelRunner karşılaştırmasında</a> bulabilirsiniz. Yazılımların kapsamı aynı değildir; yalnızca fiyata bakarak karar vermeyin.</p>
{_tbl(["Tesis", "Hostlio Pro", "HMS Otel", "Sirvoy", "Beds24"], ex_rows, hl_col=1)}
<h2>Gözden kaçan maliyetler</h2>
<ul><li><strong>Ek modüller:</strong> SMS, e-posta, misafir ilişkileri ya da gelir yönetimi modülleri ayrı ücretlendirilebilir.</li>
<li><strong>Rezervasyon başı ücretler:</strong> Küçük görünür ama yüksek sezonda toplanır.</li>
<li><strong>Ödeme işlem ücretleri:</strong> Online tahsilat yapan sistemlerde işlem başına kesinti olur.</li>
<li><strong>Kurulum ve eğitim:</strong> Bazı firmalar ücretsiz yapar, bazıları ayrıca fiyatlar.</li>
<li><strong>KDV ve kur:</strong> Fiyatlar çoğunlukla KDV hariçtir; döviz bazlı fiyatlar kurla birlikte değişir.</li>
<li><strong>OTA komisyonları:</strong> Yazılımdan bağımsızdır ama asıl büyük kalem çoğu zaman budur. Kanal bazında net geliri <a href="{U("commission")}">OTA komisyon hesaplayıcısıyla</a> görebilirsiniz.</li></ul>
<h2>Hangi model size uygun?</h2>
<ul><li>Gelirin mevsime göre değiştiği ve bütçesini sabit tutmak isteyen tesisler için <strong>sabit aylık paket</strong> en öngörülebilir modeldir; Hostlio Pro bu modelle çalışır ve yüksek sezonda da aynı ücreti alır.</li>
<li><strong>Oda başı</strong> ya da <strong>gelir yüzdesi</strong> modellerinde maliyet oda sayısı ve gelirle birlikte artar; yıllık toplamı kendi rakamlarınızla hesaplayın.</li>
<li><strong>Tek seferlik lisansta</strong> güncelleme, sunucu ve destek maliyetlerini ayrıca sorun.</li></ul>
<p>Seçim kriterlerinin tamamı için <a href="{U("post-pms")}">küçük otel için otel programı seçimi</a> rehberine, ürün karşılaştırmaları için <a href="{U("cmp-hub")}">karşılaştırmalar</a> sayfasına bakın.</p>
'''
    c += _src(PRICE_SRC)
    faq = [("Otel programı fiyatları ne kadar?", "Fiyatını yayınlayan yazılımlarda küçük bir otel için aylık maliyet yaklaşık 15 € ile 150 € arasında başlıyor (8 Ekim 2026). Bazı yazılımlar gelirden yüzde alıyor, bazıları tek seferlik lisans satıyor, bazıları da yalnızca teklif veriyor."),
           ("Otel programını ücretsiz deneyebilir miyim?", "Hostlio Pro'yu 7 gün ücretsiz deneyebilirsiniz; deneme bitene kadar ücret çekilmez. Denemede kendi odalarınızı ve fiyatlarınızı girer, kanallarınızı bağlar ve AI asistan Lio'yu kendi misafir sorularınızla test edersiniz. Ücretsiz planı olan yazılımlarda oda, kanal ve destek sınırlarını mutlaka kontrol edin."),
           ("Komisyonlu mu sabit fiyatlı mı daha avantajlı?", "Gelir düşükse yüzdeye dayalı model daha ucuz olabilir; gelir arttıkça maliyeti de büyür. Bütçesini sabitlemek isteyen tesisler için sabit aylık ücret daha öngörülebilirdir."),
           ("Hostlio Pro'nun fiyatı ne kadar?", "Starter aylık ⟦price:starter⟧, Pro ⟦price:pro⟧, Growth ⟦price:growth⟧ (USD, erken kayıt fiyatı). Yıllık ödemede %20 indirim vardır; 7 gün ücretsiz deneme sunulur.")]
    return c, faq

# ------------------------------------------------------------------ Otel WhatsApp asistanı (landing)
def whatsapp_page(B):
    U = lambda k: B.url(k, "tr")
    steps = [("1. Otel bilgilerinizi girin", "Check-in ve check-out saatleri, otopark, kahvaltı, evcil hayvan kuralları, ulaşım, oda özellikleri. Bir kez girersiniz, Lio her cevapta tutarlı kullanır. Kurulumu bitirmeden “Lio'yu dene” ile bir misafir sorusu yazıp Lio'nun cevabını görebilirsiniz."),
             ("2. WhatsApp'ı bağlayın", "Otelinizin WhatsApp hattını Hostlio Pro'ya bağlarsınız. Pro ve Growth planlarında Booking.com, Airbnb ve Expedia mesajları da aynı gelen kutusuna düşer."),
             ("3. Lio cevaplasın, siz kontrol edin", "Lio misafire kendi dilinde, saniyeler içinde cevap verir; cevabın Türkçe çevirisini panelde görürsünüz. İlk günlerde cevapları göndermeden önce onaylayabilir, hangi konuları Lio'nun kapatacağını siz belirlersiniz.")]
    does = [("Sık soruları 7/24 yanıtlar", "Gece 02:00'de gelen “geç check-in olur mu?” sorusu sabahı beklemez. Lio yalnızca sizin girdiğiniz bilgileri ve rezervasyon verilerini kullanır; emin olmadığı soruyu size iletir."),
            ("Misafirin dilinde konuşur", "Misafir hangi dilde yazarsa Lio o dilde cevap verir. Sizin elle yazdığınız cevaplar ise yazdığınız gibi gönderilir, otomatik çevrilmez."),
            ("Rezervasyon talebi alır (Pro ve Growth)", "Misafir WhatsApp'tan oda sorduğunda Lio tarihleri, kişi sayısını ve oda tercihini toplar, sizin fiyat ve müsaitliğinize göre fiyat verir. Talep onayınıza gelir; siz onaylayınca rezervasyona dönüşür. Lio kendi başına rezervasyon kesinleştirmez."),
            ("Ek hizmet sunar (Pro ve Growth)", "Havalimanı transferi ve tur gibi tanımladığınız ek hizmetleri uygun anda önerir, talebi ekibinize iletir."),
            ("Eksik bilgiyi size söyler", "Lio cevaplayamadığı soru konularını kurulumda eksik alan olarak işaretler; alanı bir kez doldurursunuz, uyarı kendiliğinden kapanır."),
            ("Her sabah öneri getirir", "Lio Önerileri her sabah fiyat, operasyon ve kurulum için öneri sunar. Onayınız olmadan hiçbir şey değişmez.")]
    donts = ["Rezervasyonu kendi başına kesinleştirmez; her talep sizin onayınızdan geçer.", "Ödeme almaz ve indirim kararı vermez; bu tür mesajları size bırakır.",
             "Sizin yazdığınız mesajları otomatik çevirmez.", "Girmediğiniz bir bilgiyi uydurmak yerine soruyu size iletir."]
    rows = "".join(f'<div class="row"><h3>{h}</h3><div><p>{p}</p></div></div>' for h, p in does)
    st = "".join(f'<div class="row"><h3>{h}</h3><div><p>{p}</p></div></div>' for h, p in steps)
    plan = _tbl(["Plan", "Aylık fiyat", "Aylık AI mesajı", "Lio'nun cevap verdiği kanallar"], [
        ("Starter", "⟦price:starter⟧", "⟦quota:starter⟧", "WhatsApp"),
        ("Pro", "⟦price:pro⟧", "⟦quota:pro⟧", "WhatsApp + Booking.com, Airbnb, Expedia gelen kutuları"),
        ("Growth", "⟦price:growth⟧", "⟦quota:growth⟧", "WhatsApp + Booking.com, Airbnb, Expedia gelen kutuları")])
    body = f'''<section class="page-hero"><div class="wrap"><h1>Otel WhatsApp asistanı: <em class="hl">gece de</em> cevap veren Lio</h1>
<p class="lead">Misafirleriniz WhatsApp'tan yazıyor; check-in saati, otopark, transfer, kahvaltı. Hostlio Pro'nun AI asistanı Lio bu soruları otelinizin bilgileriyle, misafirin dilinde ve günün her saatinde yanıtlar; karar gerektiren mesajları size bırakır.</p>
<div class="cta-row">{B.btn("7 gün ücretsiz dene", B.SIGNUP_URL)}{B.btn("Lio'yu tanıyın", U("ai"), "ghost")}</div></div></section>
<section style="padding-top:0"><div class="wrap">
<div class="answer"><h2 style="font-size:var(--t-1);margin-bottom:.4em">Otel WhatsApp asistanı nedir?</h2><p>Otel WhatsApp asistanı, misafirlerin WhatsApp'tan sorduğu soruları otelin kendi bilgileriyle otomatik yanıtlayan yapay zekâ yazılımıdır. İyi bir asistan yalnızca bildiği konularda cevap verir, emin olmadığı ya da insan kararı gereken mesajları (indirim talebi, şikâyet, özel istek) personele devreder.</p></div>
<h2 style="margin-top:64px">Nasıl çalışır?</h2><div class="rows">{st}</div>
<h2 style="margin-top:64px">Lio neler yapar?</h2><div class="rows">{rows}</div>
<h2 style="margin-top:64px">Lio neleri yapmaz?</h2><div class="prose"><ul>{"".join(f"<li>{x}</li>" for x in donts)}</ul></div>
<h2 style="margin-top:64px">Planlar ve mesaj kotası</h2><p>Bir AI mesajı, Lio'nun misafire gönderdiği tek bir yanıttır. Kanal yöneticisi ve oda rafı tüm planlarda dahildir.</p>{plan}
<p class="small muted" style="margin-top:12px">Fiyatlar ABD doları, erken kayıt aylık fiyatlarıdır. Kullanım sayacı %80'de panelde uyarı verir, %100'de e-posta gönderilir. Ayrıntılar: <a href="{U("pricing")}">fiyatlandırma</a>.</p>
<h2 style="margin-top:64px">Kimler için uygun?</h2>
<div class="prose"><ul><li>Gece resepsiyonu olmayan ya da tek kişiyle dönen pansiyon, butik otel ve apart oteller</li>
<li>Yabancı misafiri çok olan, farklı dillerde mesaj alan tesisler</li>
<li>Booking.com, Airbnb ve WhatsApp mesajlarını tek ekranda toplamak isteyen ekipler (Pro ve Growth)</li></ul>
<p>Lio'nun size ne kadar zaman kazandırabileceğini <a href="{U("roi")}">tasarruf hesaplayıcısıyla</a> tahmin edebilirsiniz. Yöntemler ve sınırlar için <a href="{U("post-ai")}">misafir mesajlarını yapay zekâ ile yanıtlamak</a> ve <a href="{U("post-autoreply")}">Booking.com mesajlarına otomatik cevap</a> yazılarına bakın. Verilerin nasıl korunduğu <a href="{U("security")}">güvenlik ve veri</a> sayfasında.</p></div>
</div></section>'''
    faq = [("Lio yanlış bilgi verirse ne olur?", "Lio yalnızca sizin girdiğiniz otel bilgilerini ve rezervasyon verilerini kullanır. Emin olmadığı sorularda tahmin yürütmek yerine mesajı size iletir. Dilerseniz tüm cevapları gönderilmeden önce onaylayabilirsiniz."),
           ("Lio hangi dillerde cevap veriyor?", "Misafir hangi dilde yazarsa Lio o dilde cevap verir; cevabın Türkçe çevirisini panelde görürsünüz. Panel ve uygulama Türkçe, İngilizce, İspanyolca, Fransızca, İtalyanca ve Portekizce kullanılabilir."),
           ("Booking.com ve Airbnb mesajlarını da yanıtlıyor mu?", "Evet, Pro ve Growth planlarında. Starter planında Lio WhatsApp mesajlarını yanıtlar; OTA rezervasyonları senkronize edilir ama OTA mesajları Lio'ya bağlanmaz."),
           ("Lio WhatsApp'tan rezervasyon alabiliyor mu?", "Pro ve Growth planlarında rezervasyon talebi alır: tarih, kişi sayısı ve oda tercihini toplar, sizin fiyatlarınıza göre fiyat verir ve talebi size iletir. Talep ancak siz onayladığınızda rezervasyona dönüşür."),
           ("Mesaj kotası dolarsa ne olur?", "Paneldeki kullanım sayacı %80'de turuncuya döner, %100'de hesap sahibine e-posta ve anlık bildirim gider. Otomatik yanıt yaklaşık %110'da durur; mesajlar gelmeye ve panelde görünmeye devam eder, ekibiniz elle cevaplayabilir. Üst plana geçerek kotanızı artırabilirsiniz.")]
    return {"key": "whatsapp-tr", "title": "Otel WhatsApp Asistanı: Lio ile 7/24 Misafir Yanıtı | Hostlio Pro",
            "desc": "Otel WhatsApp asistanı Lio, misafir sorularını otel bilgilerinizle ve misafirin dilinde 7/24 yanıtlar; rezervasyon talebini onayınıza getirir.",
            "trail": [("AI asistan Lio", U("ai")), ("Otel WhatsApp asistanı", U("whatsapp-tr"))], "body": body, "faq": faq,
            "schema": [B.software_schema("tr")]}

# ------------------------------------------------------------------ En çok kullanılan otel programları (9 Ekim 2026)
# Bilgiler firmaların kendi sitelerinden, 9 Ekim 2026. Türkiye için açık pazar payı verisi yok ⇒ sıralama iddiası yok;
# müşteri sayıları "firmanın beyanı" olarak verilir. protel.com.tr (Oracle iş ortağı) ile Planet'in protel PMS'i ayrı şirketler.
PROG_DATE = "9 Ekim 2026"
PROG_SRC = [
 ("Elektraweb", "https://www.elektraweb.com"),
 ("Elektraweb yardım: Kimlik Bildirim Sistemi", "https://yardim.elektraweb.com/detayli-anlatim/kimlik-bildirim-sistemi"),
 ("HMS Otel", "https://www.hmsotel.com"),
 ("HMS Otel: Fiyat listesi", "https://www.hmsotel.com/fiyat-listesi/"),
 ("Sistem Otel", "https://www.sistemotel.com"),
 ("AKINSOFT: WOLVOX Otel Programı", "https://www.akinsoft.com.tr/programlar/detay/wolvox-otel-programi--who9"),
 ("HotelRunner: Hakkımızda", "https://www.hotelrunner.com/tr/hakkimizda"),
 ("HotelRunner: Fiyatlandırma", "https://www.hotelrunner.com/tr/fiyatlandirma"),
 ("Veboni (eski adıyla Sedna)", "https://www.veboni.com/"),
 ("Oracle: OPERA Cloud PMS", "https://www.oracle.com/hospitality/hotel-property-management/hotel-pms-software/"),
 ("Protel A.Ş.", "https://www.protel.com.tr"),
 ("Planet: Hospitality (protel PMS)", "https://www.weareplanet.com/hospitality"),
 ("Cloudbeds: Pricing", "https://www.cloudbeds.com/pricing/"),
 ("Sirvoy: Pricing", "https://sirvoy.com/pricing"),
 ("Beds24: Pricing", "https://beds24.com/pricing.html"),
 ("eviivo", "https://eviivo.com/"),
]

def programs(U):
    from build import btn, SIGNUP_URL
    cta = btn("7 gün ücretsiz dene", SIGNUP_URL) + btn("Planları gör", U("pricing"), "ghost")
    rows = [
      ("Elektraweb", "Bulut PMS + modüler paket", "Her büyüklük; geniş modül ihtiyacı olan oteller", "Teklif", "Kanal yöneticisi, POS, e-Fatura, KBS entegrasyonu"),
      ("HMS Otel", "Bulut PMS", "Küçük ve orta oteller, butik, apart", "Yayınlanıyor (oda aralığına göre €)", "Kanal yöneticisi, rezervasyon motoru ve KBS her pakette"),
      ("Sistem Otel", "Otel programı (PMS)", "Tek otel ve zincirler", "Teklif", "Kanal yöneticisi, restoran, e-Fatura, kimlik okuyucu"),
      ("AKINSOFT WOLVOX Otel", "Kurulu yazılım, tek seferlik lisans", "Yerel kurulum ve muhasebe bütünlüğü isteyen tesisler", "Yayınlanıyor (₺, KDV hariç)", "Kanal yöneticisi dahili değil (HotelRunner entegrasyonu)"),
      ("HotelRunner", "Satış odaklı paket: kanal yöneticisi, rezervasyon motoru, PMS", "Online satışı büyütmek isteyen bağımsız tesisler", "Yayınlanıyor (gelirden yüzde + asgari $)", "KBS entegrasyonu fiyat sayfasında listeleniyor"),
      ("Veboni (Sedna)", "Web tabanlı otel ERP", "Büyük oteller, resort ve zincirler", "Teklif", "Ön büro, POS, muhasebe, CRM, SPA"),
      ("Oracle OPERA Cloud", "Kurumsal bulut PMS", "Büyük oteller ve zincirler", "Teklif", "Türkiye'de iş ortakları üzerinden satılıyor"),
      ("Cloudbeds", "Bulut PMS + kanal yöneticisi", "Bağımsız tesisler", "Teklif", "Türkçe arayüz ve KBS bilgisi sitede yok"),
      ("Sirvoy, Beds24, eviivo", "Bulut PMS (yabancı)", "Küçük tesisler, pansiyon, kiralık daire", "Sirvoy ve Beds24 yayınlıyor; eviivo demo", "Sitelerinde Türkçe ve KBS bilgisi yok"),
      ("Hostlio Pro", "Bulut PMS + kanal yöneticisi + AI asistan", "1–150 odalı bağımsız oteller ve pansiyonlar", "Yayınlanıyor (sabit aylık, ⟦price:starter⟧'dan)", "WhatsApp'ta AI asistan her planda; KBS için CSV dışa aktarım"),
    ]
    c = f'''<div class="answer"><p><strong>Kısa cevap:</strong> Türkiye'de otellerde en sık karşılaşılan otel programları yerli tarafta Elektraweb, HMS Otel, Sistem Otel, AKINSOFT WOLVOX Otel, HotelRunner ve Veboni (eski adıyla Sedna); büyük otel ve zincirlerde Oracle OPERA Cloud. Küçük tesislerde Cloudbeds, Sirvoy ve Beds24 gibi yabancı bulut programları da kullanılıyor. Hangisinin "en çok" kullanıldığını gösteren bağımsız bir pazar payı verisi yok; doğru seçim oda sayınıza, satış kanallarınıza ve ihtiyaç duyduğunuz modüllere bağlı.</p></div>
<p class="small muted">Hostlio Pro bu listede taraftır. Bilgileri firmaların kendi sitelerinden {PROG_DATE} tarihinde aldık; müşteri sayıları firmaların kendi beyanıdır, bağımsız olarak doğrulanmadı. Liste bir sıralama değildir. Ürünler ve fiyatlar değişebilir; karar vermeden önce firmanın kendi sayfasını kontrol edin.</p>
<h2>Otel programı (PMS) ne işe yarar?</h2>
<p>Otel programı, sektördeki adıyla PMS (property management system), otelin günlük işini tek yerde toplar: rezervasyon takvimi, giriş ve çıkış, oda durumu, misafir kayıtları, fatura ve raporlar. Bugün çoğu program buna bir de <a href="{U("post-channel-manager")}">kanal yöneticisi</a> ekliyor; böylece Booking.com, Airbnb ve Expedia'daki müsaitlik ve fiyatlar otomatik güncelleniyor. Türkiye'de ayrıca konaklayan misafirlerin <a href="{U("post-kbs")}">KBS'ye bildirimi</a> ve e-Fatura gibi yerel ihtiyaçlar var.</p>
<h2>2026 listesi: kısa karşılaştırma</h2>
{_tbl(["Program", "Tür", "Kime uygun", "Fiyat", "Öne çıkan"], rows)}
<h2>Yerli otel programları</h2>
<h3>Elektraweb</h3>
<p>Talya Bilişim'in bulut tabanlı otel programı. Kendini "Türkiye'nin ilk bulutta barındırılan web tabanlı otel programı" olarak tanıtıyor ve 35'ten fazla ülkede 5.000'den fazla otel beyan ediyor. Kanal yöneticisi, rezervasyon motoru, POS, e-Fatura ve e-Arşiv modülleri var; yardım sayfalarında Emniyet ve Jandarma KBS entegrasyonu anlatılıyor. Fiyat yayınlanmıyor, teklif formuyla veriliyor. Ayrıntılı karşılaştırma: <a href="{U("vs-elektraweb")}">Hostlio Pro ile Elektraweb</a>.</p>
<h3>HMS Otel</h3>
<p>Denizli'de, Pamukkale Üniversitesi Teknokent'te 2010'dan beri geliştirilen bulut otel programı; 5.000'in üzerinde tesis beyan ediyor. Kanal yöneticisi, online rezervasyon motoru ve Polis/Jandarma KBS bağlantısı her pakette yer alıyor, iOS ve Android uygulaması var. Fiyatını oda aralığına göre avro olarak yayınlayan az sayıdaki yerli firmadan biri; rakamlar <a href="{U("post-prices")}">otel programı fiyatları</a> yazımızda.</p>
<h3>Sistem Otel</h3>
<p>Arpies Yazılım'ın otel programı; 20 ülkede 2.269 otel beyan ediyor. Kanal yöneticisi ve rezervasyon motoru, restoran programı, e-Fatura/e-Arşiv, kimlik okuyucu ve Emniyet/Jandarma bildirim entegrasyonu sunuyor; sitesinde WhatsApp için bir "AI resepsiyonist" ürünü de tanıtılıyor. Fiyat teklifle veriliyor.</p>
<h3>AKINSOFT WOLVOX Otel</h3>
<p>Konya merkezli AKINSOFT'un (1995) WOLVOX ERP üzerine kurulu otel programı; otel, motel, apart ve pansiyonlara yönelik. Bilgisayara kurulan, tek seferlik lisansla satılan bir yazılım; fiyatı sitede Türk lirası olarak yayınlanıyor (KDV hariç, Ekim 2026'da süreli kampanya var). AKBS ve Jandarma entegrasyonu ile e-Fatura modülleri var. Kanal yöneticisi dahili değil; online satış HotelRunner entegrasyonuyla yapılıyor.</p>
<h3>HotelRunner</h3>
<p>2011'de Türkiye'de kurulan HotelRunner kanal yöneticisi ve rezervasyon motoru olarak başladı; bugün PMS, POS, web sitesi ve otomatik fiyatlandırmayı da içeren satış odaklı bir paket. 100'den fazla ülkede 64.000'den fazla konaklama iş ortağı beyan ediyor. Fiyatı rezervasyon gelirinden yüzde ve aylık asgari ücret olarak yayınlanıyor; fiyat sayfasında KBS entegrasyonu listeleniyor. Ayrıntılı karşılaştırma: <a href="{U("vs-hotelrunner")}">Hostlio Pro ile HotelRunner</a>.</p>
<h3>Veboni (eski adıyla Sedna)</h3>
<p>Antalya merkezli Kod Yazılım'ın otel ERP'si; uzun süre Sedna adıyla bilinen ürün artık Veboni markasıyla sunuluyor. Ön büro, online rezervasyon, kanal yöneticisi, POS, CRM, muhasebe ve SPA modülleri var; 700'den fazla referans otel beyan ediyor. Daha çok resort ve büyük otellerin geniş modül ihtiyacına yönelik; fiyat yayınlanmıyor.</p>
<h2>Yabancı otel programları</h2>
<h3>Oracle OPERA Cloud</h3>
<p>Eski adıyla Fidelio olarak bilinen sistemin devamı olan OPERA, büyük oteller ve zincirlerin kullandığı kurumsal PMS. Türkiye'de Oracle iş ortakları üzerinden satılıyor; bunlardan biri Protel A.Ş. Bu yerli firma, Almanya kökenli protel PMS'ten (bugün Planet şirketinin ürünü) ayrı bir şirket; iki ad sık karıştırılıyor. Fiyat teklifle.</p>
<h3>Cloudbeds</h3>
<p>Bağımsız tesislere yönelik bulut PMS, kanal yöneticisi ve rezervasyon motoru; 150'den fazla ülkede 20.000'den fazla tesis beyan ediyor. Dört planın hepsi teklifle fiyatlanıyor. Sitesinde Türkçe arayüz ya da KBS bilgisine rastlamadık.</p>
<h3>Sirvoy, Beds24 ve eviivo</h3>
<p>Küçük oteller, pansiyonlar ve kiralık daireler için yabancı bulut programları. Sirvoy ve Beds24 fiyatlarını sitede yayınlıyor (Sirvoy'da kanal yöneticisi yalnız Pro planında); eviivo demo talebiyle ilerliyor. Üçünün sitesinde de Türkçe dil seçeneği ya da KBS bağlantısı yer almıyor; Türkiye'deki bir tesis için bu, misafir bildirimini ayrıca çözmek demek.</p>
<h2>Hostlio Pro bu listede nerede duruyor?</h2>
<p>Hostlio Pro, 1–150 odalı bağımsız oteller ve pansiyonlar için PMS, sertifikalı kanal yöneticisi (100+ OTA) ve WhatsApp'ta misafirlere cevap veren AI asistan Lio'yu tek pakette sunar. Fiyatı sitede açıktır ve sabittir: Starter ⟦price:starter⟧, Pro ⟦price:pro⟧, Growth ⟦price:growth⟧ / ay; rezervasyon başına ücret ya da gelir yüzdesi alınmaz. Panel Türkçe dahil 6 dilde, mobil uygulama her planda. Açık olmak gerekirse: Hostlio Pro KBS'ye otomatik bildirim yapmaz, misafir listesini CSV olarak dışa aktarır; POS, muhasebe ve bordro gibi modüller sunmaz. Bu modüllere ihtiyacı olan büyük tesisler için yukarıdaki kapsamlı paketler daha uygun olabilir.</p>
<div class="cta-row" style="margin-top:12px">{cta}</div>
<h2>Hangisini seçmeli?</h2>
<ul><li><strong>1–20 oda, pansiyon ve butik otel:</strong> Kurulumu kolay bir bulut PMS ve dahili kanal yöneticisi yeterli. Aylık sabit ücret ve mobil uygulama işinizi kolaylaştırır.</li>
<li><strong>20–150 oda, bağımsız otel:</strong> Kanal yöneticisinin sertifikalı bağlantıları, misafir mesajlarının tek yerden yönetimi, personel rolleri ve raporlar öne çıkar.</li>
<li><strong>Restoranı, SPA'sı ve muhasebesi aynı sistemde olması gereken resort ve zincirler:</strong> Modüler, kurumsal paketler (Elektraweb, Veboni, OPERA gibi) bu ihtiyaca göre tasarlanmıştır.</li>
<li><strong>İnternet bağımsız, yerel kurulum isteyenler:</strong> Tek seferlik lisanslı kurulu yazılımlar; güncelleme, yedekleme ve kanal yöneticisi maliyetini ayrıca hesaplayın.</li></ul>
<h2>Seçmeden önce sorulacak 5 soru</h2>
<ol><li><strong>Fiyat nasıl hesaplanıyor?</strong> Sabit mi, oda başı mı, gelirden yüzde mi? Yüksek sezonda fatura büyüyor mu?</li>
<li><strong>Kanal yöneticisi dahil mi?</strong> Hangi planda, hangi kanallara, sertifikalı bağlantıyla mı?</li>
<li><strong>KBS ve e-Fatura nasıl çözülüyor?</strong> Otomatik bildirim mi, dosya dışa aktarımı mı?</li>
<li><strong>Misafir mesajlaşması var mı?</strong> WhatsApp ve OTA mesajları tek ekranda mı, otomatik cevap var mı?</li>
<li><strong>Deneyebiliyor musunuz?</strong> Kendi odalarınız ve fiyatlarınızla, satış görüşmesi beklemeden?</li></ol>
<p>Kriterlerin ayrıntısı için <a href="{U("post-pms")}">küçük otel için otel programı seçimi</a>, maliyet için <a href="{U("post-prices")}">otel programı fiyatları 2026</a> yazılarına bakın.</p>
'''
    lis = "".join(f'<li><a href="{u}" rel="nofollow noopener">{html.escape(n)}</a></li>' for n, u in PROG_SRC)
    c += f'<h2>Kaynaklar</h2><p class="small muted">Tüm kaynaklara {PROG_DATE} tarihinde erişildi.</p><ul>{lis}</ul>'
    faq = [("Türkiye'de en çok kullanılan otel programı hangisi?", "Bunu gösteren bağımsız bir pazar payı verisi yok. Yerli tarafta Elektraweb, HMS Otel, Sistem Otel, AKINSOFT WOLVOX Otel, HotelRunner ve Veboni (Sedna) yaygın biliniyor; büyük otellerde Oracle OPERA Cloud kullanılıyor. Firmaların açıkladığı müşteri sayıları kendi beyanlarıdır."),
           ("Küçük otel için hangi otel programı uygun?", "1–50 odalı tesislerde kurulumu kolay, dahili kanal yöneticisi olan ve aylık sabit ücretli bir bulut program genellikle yeterlidir. POS, muhasebe ve bordro gibi modüllere ihtiyacınız yoksa kapsamlı kurumsal paketler gereğinden pahalı ve karmaşık olabilir."),
           ("Otel programı KBS bildirimini otomatik yapar mı?", "Bazı yerli programlar Emniyet ve Jandarma KBS entegrasyonu sunuyor (örneğin Elektraweb, HMS Otel, Sistem Otel, AKINSOFT WOLVOX, HotelRunner). Yabancı programların sitelerinde KBS bilgisi yok. Hostlio Pro otomatik bildirim yapmaz, misafir listesini CSV olarak dışa aktarır."),
           ("Hostlio Pro'yu ücretsiz deneyebilir miyim?", "Evet, 7 gün ücretsiz deneyebilirsiniz; deneme bitene kadar ücret çekilmez. Planlar Starter ⟦price:starter⟧, Pro ⟦price:pro⟧ ve Growth ⟦price:growth⟧ / ay (USD, erken kayıt).")]
    return c, faq

# ------------------------------------------------------------------ Konaklama vergisi (takvim: 20 Ekim 2026)
# Resmî kaynaklar 10 Ekim 2026: 6802 GVK md. 34, Konaklama Vergisi Uygulama Genel Tebliği (RG 14.12.2022),
# CK 11263 (RG 1.5.2026: %1, 31.12.2026'ya kadar), GİB beyanname kılavuzu. KDV oranı bilerek yazılmadı (doğrulanmadı).
# Hostlio fatura kesmez, beyanname hazırlamaz — metin bunu söyler.
TAX_DATE = "10 Ekim 2026"
TAX_SRC = [
 ("6802 sayılı Gider Vergileri Kanunu (md. 34, güncel metin)", "https://www.mevzuat.gov.tr/mevzuatmetin/1.3.6802.pdf"),
 ("Konaklama Vergisi Uygulama Genel Tebliği (Resmî Gazete, 14.12.2022)", "https://www.resmigazete.gov.tr/eskiler/2022/12/20221214-6.htm"),
 ("Cumhurbaşkanı Kararı 11263: oran %1 (Resmî Gazete, 1.5.2026)", "https://www.resmigazete.gov.tr/eskiler/2026/05/20260501-6.pdf"),
 ("GİB: Konaklama Vergisi Beyannamesi Düzenleme Kılavuzu", "https://intvrg.gib.gov.tr/KONAKLAMA_VERGISI_BEYANNAMESI_DUZENLEME_KILAVUZU.pdf"),
 ("7194 sayılı Kanun", "https://www.mevzuat.gov.tr/mevzuatmetin/1.5.7194.pdf"),
]

def tax(U):
    from build import btn, SIGNUP_URL
    cta = btn("7 gün ücretsiz dene", SIGNUP_URL) + btn("Planları gör", U("pricing"), "ghost")
    calc = _tbl(["Kalem", "Tutar", "Not"], [
        ("Konaklama bedeli (KDV hariç)", "5.000 TL", "Oda ile birlikte satılan kahvaltı ve yemek dahil"),
        ("Konaklama vergisi (%1)", "50 TL", "5.000 × 0,01; faturada ayrı satırda"),
        ("KDV matrahı", "5.000 TL", "Konaklama vergisi KDV matrahına girmez"),
        ("KDV", "Geçerli oranla hesaplanır", "Oranı muhasebecinizle teyit edin")])
    c = f'''<div class="answer"><p><strong>Kısa cevap:</strong> Konaklama vergisi, otel, pansiyon, apart ve benzeri tesislerde verilen geceleme hizmetinden ve bu hizmetle birlikte sunulan yeme-içme, havuz, spa gibi hizmetlerden alınan bir vergidir. Kanundaki oran %2'dir; ancak 1 Mayıs 2026'dan 31 Aralık 2026'ya kadar oran <strong>%1</strong> olarak uygulanıyor. Vergi KDV hariç bedel üzerinden hesaplanır, faturada ayrıca gösterilir ve her ay ayrı bir "Konaklama Vergisi Beyannamesi" ile ertesi ayın 26'sı akşamına kadar beyan edilip ödenir.</p></div>
<p class="small muted">Bu yazı genel bilgilendirme amaçlıdır, vergi danışmanlığı değildir. Bilgiler {TAX_DATE} tarihinde resmî kaynaklardan (kanun, tebliğ, Cumhurbaşkanı Kararı ve GİB kılavuzu) derlendi. Oranlar ve uygulama değişebilir; kendi durumunuz için mali müşavirinize danışın.</p>
<h2>Konaklama vergisi nedir, ne zamandan beri var?</h2>
<p>Konaklama vergisi 6802 sayılı Gider Vergileri Kanunu'nun 34. maddesinde düzenlenir; bu madde 7194 sayılı Kanun'la eklendi. Vergi ilk olarak 2020'de başlayacaktı, ancak salgın döneminde üç kez ertelendi ve <strong>1 Ocak 2023'ten beri</strong> uygulanıyor. Uygulamanın ayrıntıları Konaklama Vergisi Uygulama Genel Tebliği'nde (Resmî Gazete, 14 Aralık 2022) yer alır.</p>
<h2>2026'da oran ne kadar?</h2>
<p>Kanundaki oran <strong>%2</strong>'dir ve Cumhurbaşkanı bu oranı iki katına kadar artırabilir ya da yarısına kadar indirebilir. 1 Mayıs 2026'da yayımlanan 11263 sayılı Cumhurbaşkanı Kararı ile oran <strong>31 Aralık 2026'ya kadar %1</strong> olarak belirlendi. Yeni bir karar yayımlanmazsa 1 Ocak 2027'den itibaren yeniden %2 uygulanır. Ay sonunu ve yıl başını kapsayan konaklamalarda hangi oranın uygulanacağını mali müşavirinizle netleştirin.</p>
<h2>Hangi tesisler konaklama vergisi öder?</h2>
<p>Kanun otel, motel, tatil köyü, pansiyon, apart otel, misafirhane, kamping, dağ evi ve yayla evini sayar. Tebliğ kapsamı genişletir: butik otel, çiftlik ve köy evi, termal tesisler, uygulama otelleri, kurum misafirhaneleri ve <em>turizm işletmesi belgesi ya da işyeri açma belgesi olup olmadığına bakılmaksızın</em> geceleme hizmeti sunan diğer tüm tesisler. Misafirin yerli ya da yabancı olması fark etmez. Vergiyi tesisi fiilen işleten öder; mülkün sahibi olmak gerekmez.</p>
<h2>Hangi hizmetler vergiye tabi?</h2>
<ul><li><strong>Tabi:</strong> geceleme hizmeti ve onunla birlikte satılan her şey: oda-kahvaltı, yarım pansiyon, tam pansiyon, her şey dahil paketler, yeme-içme, havuz, spa, termal ve spor hizmetleri. Kahvaltı faturada ayrı satırda gösterilse bile vergiye tabidir.</li>
<li><strong>Tabi değil:</strong> konaklamayan kişilere verilen hizmetler (örneğin dışarıdan gelen misafire restoran ya da günübirlik spa), konaklamayla birlikte satılmayan ve ayrı fiyatlanan ekstralar, ayrı gösterilen ya da ayrı faturalanan transfer ve turlar, konaklama içermeyen düğün ve toplantılar.</li>
<li><strong>Ücretsiz konaklama:</strong> sahiplere, yakınlara, personele ya da tanıtım amacıyla verilen ücretsiz konaklamalarda vergi emsal bedel üzerinden hesaplanır.</li></ul>
<h2>Nasıl hesaplanır? Örnek</h2>
<p>Matrah, konaklama hizmetinin <strong>KDV hariç</strong> bedelidir; vade, kur ve fiyat farkları da matraha girer, faturada gösterilen ticari iskontolar düşülebilir. Döviz cinsinden fiyatlarda vergi doğduğu günün TCMB döviz alış kuru kullanılır. Vergi faturada ayrıca gösterilir, üzerinden indirim yapılamaz ve <strong>KDV matrahına dahil edilmez</strong>. Konaklamadan önce kesilen faturada (örneğin ön ödeme) konaklama vergisi gösterilmez.</p>
{calc}
<p>Örnek, Tebliğ'deki örneğin bugünkü %1 oranına uyarlanmış hâlidir. Konaklama hizmetindeki güncel KDV oranını muhasebecinizle teyit edin.</p>
<h2>İstisnalar</h2>
<ul><li><strong>Öğrenciler:</strong> öğrenci yurtları, pansiyonları ve kamplarında öğrencilere verilen konaklama hizmeti istisnadır. Bu yerlerde zaman zaman konaklayan öğrenci olmayan kişiler vergiye tabidir.</li>
<li><strong>Diplomatik temsilcilikler:</strong> karşılıklılık esasıyla diplomatik temsilcilikler, konsolosluklar ve vergi muafiyeti tanınan uluslararası kuruluşlar; Dışişleri Bakanlığı belgesi ve faturaya düşülen kanuni açıklama gerekir.</li>
<li><strong>Genel bir kamu istisnası yoktur:</strong> kurum misafirhaneleri de vergiye tabidir; yalnızca lojmanlar kapsam dışıdır.</li></ul>
<p>Kanunda ve Tebliğ'de konaklama süresine bağlı bir sınır yoktur; fiilen konaklanan geceler vergilendirilir.</p>
<h2>Beyan ve ödeme</h2>
<ol><li><strong>Ayrı beyanname:</strong> vergi, KDV ya da muhtasar beyannamesiyle değil, ayrı bir <em>Konaklama Vergisi Beyannamesi</em> ile elektronik ortamda beyan edilir.</li>
<li><strong>Dönem ve süre:</strong> aylıktır; bir ayın vergisi ertesi ayın <strong>26'sı akşamına kadar</strong> beyan edilir ve aynı sürede ödenir.</li>
<li><strong>Nereye:</strong> KDV mükellefiyseniz bağlı olduğunuz vergi dairesine; birden fazla tesisiniz varsa hepsi için tek beyanname verilir.</li>
<li><strong>Satış olmayan aylar:</strong> o ay vergiye tabi işlem olmasa da beyanname verilmesi gerekir.</li>
<li><strong>Fazla ödeme:</strong> önce misafire iade edilir, sonra beyanname düzeltilir ve iade talep edilir.</li></ol>
<h2>Geç beyan ve cezalar</h2>
<p>Konaklama vergisine özgü ayrı bir ceza yoktur; Vergi Usul Kanunu'nun genel hükümleri uygulanır. GİB kılavuzuna göre süresinden sonra pişmanlıkla verilen beyannamede vergi ziyaı cezası kesilmez ama pişmanlık zammı ve özel usulsüzlük cezası uygulanır. Pişmanlık şartları sağlanmadan süresinden sonra verilen beyannamede ise vergi ziyaı cezası (%50) ve gecikme faizi de gündeme gelir. En kolayı her ay 26'sını takvime yazmaktır.</p>
<h2>Sık yapılan yanlışlar</h2>
<ul><li>"Oran %2": 2026'nın Mayıs–Aralık döneminde %1.</li>
<li>"KDV beyannamesinde beyan edilir": hayır, ayrı bir beyanname vardır.</li>
<li>"Son gün ayın 28'i": konaklama vergisinde ertesi ayın 26'sıdır.</li>
<li>"Kahvaltı ayrı yazılırsa vergi yok": konaklamayla birlikte satılan kahvaltı vergiye tabidir.</li>
<li>"Satış yoksa beyanname yok": satış olmayan ayda da beyanname verilir.</li></ul>
<h2>Hostlio Pro bu işte ne yapar, ne yapmaz?</h2>
<p>Açık olalım: Hostlio Pro fatura kesmez ve konaklama vergisi beyannamesi hazırlamaz; bunlar muhasebe yazılımınızın ve mali müşavirinizin işidir. Hostlio Pro'da rezervasyonlarınız, gelir ve doluluk raporlarınız tek yerde durur; raporları Excel'e aktarıp muhasebecinize iletebilirsiniz. Misafir kimlik bildirimi için de <a href="{U("post-kbs")}">KBS bildirimi rehberimize</a> bakın.</p>
<div class="cta-row" style="margin-top:12px">{cta}</div>
'''
    lis = "".join(f'<li><a href="{u}" rel="nofollow noopener">{html.escape(n)}</a></li>' for n, u in TAX_SRC)
    c += f'<h2>Kaynaklar</h2><p class="small muted">Tüm kaynaklara {TAX_DATE} tarihinde erişildi.</p><ul>{lis}</ul>'
    faq = [("Konaklama vergisi oranı 2026'da kaç?", "Kanundaki oran %2'dir. 11263 sayılı Cumhurbaşkanı Kararı ile 1 Mayıs 2026'dan 31 Aralık 2026'ya kadar %1 uygulanıyor. Yeni karar çıkmazsa 1 Ocak 2027'den itibaren yeniden %2."),
           ("Konaklama vergisi KDV'ye dahil mi?", "Hayır. Konaklama vergisi KDV hariç bedel üzerinden hesaplanır, faturada ayrıca gösterilir ve KDV matrahına dahil edilmez."),
           ("Konaklama vergisi beyannamesi ne zaman verilir?", "Aylık olarak, ertesi ayın 26'sı akşamına kadar; ödeme de aynı sürede yapılır. Vergiye tabi işlem olmayan aylarda da beyanname verilir."),
           ("Pansiyonlar da konaklama vergisi öder mi?", "Evet. Kanun pansiyonları açıkça sayar; Tebliğ'e göre belgesi olup olmadığına bakılmaksızın geceleme hizmeti sunan tüm tesisler kapsamdadır."),
           ("Kahvaltı konaklama vergisine tabi mi?", "Konaklamayla birlikte satılıyorsa evet; faturada ayrı satırda gösterilse bile. Konaklamayan kişiye satılan kahvaltı ise vergiye tabi değildir.")]
    return c, faq

META = [
 dict(key="post-taxtr", date="2026-10-10", title="Konaklama vergisi 2026: oran, hesaplama ve beyan",
      desc="Konaklama vergisi 2026: oran %1 (Mayıs–Aralık 2026), kimler öder, KDV hariç matrah, örnek hesap, istisnalar, beyanname ve son gün. Resmî kaynaklı."),
 dict(key="post-programs", date="2026-10-09", title="En çok kullanılan otel programları: 2026 listesi",
      desc="Türkiye'de otellerin kullandığı otel programları: Elektraweb, HMS, Sistem Otel, WOLVOX, HotelRunner, OPERA ve diğerleri. Kime uygun, fiyat, KBS."),
 dict(key="post-channel-manager", date="2026-10-08", title="Channel manager nedir? Otelciler için kanal yöneticisi rehberi",
      desc="Channel manager (kanal yöneticisi) nedir, nasıl çalışır, PMS'ten farkı ne? Fiyat modelleri, seçim için 7 soru ve kurulum adımları. 2026 rehberi."),
 dict(key="post-kbs", date="2026-10-08", title="KBS bildirimi nasıl yapılır? Oteller ve pansiyonlar için rehber",
      desc="KBS (Kimlik Bildirim Sistemi) bildirimi adım adım: Emniyet ve Jandarma KBS farkı, kayıt, yabancı misafir, süreler ve cezalar. Resmî kaynaklı."),
 dict(key="post-prices", date="2026-10-08", title="Otel programı fiyatları 2026: modeller ve gerçek rakamlar",
      desc="2026 otel programı fiyatları: sabit paket, oda başı, komisyon ve lisans modelleri; resmî sayfalardan alınmış rakamlar ve 10, 25, 50 oda için örnek hesap."),
]
_FN = {"post-taxtr": tax, "post-programs": programs, "post-channel-manager": channel_manager, "post-kbs": kbs, "post-prices": prices}

def pages(B):
    import content_tr
    U = lambda k: B.url(k, "tr")
    out = []
    for m in META:
        c, faq = _FN[m["key"]](U)
        out.append(content_tr.article(m, c, faq))
    out.append(whatsapp_page(B))
    return out
