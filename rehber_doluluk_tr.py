"""Takvim yazısı: "Otel doluluk oranı nasıl artırılır? 9 yöntem (2026)" — yalnız TR. RevPAR/ADR hesaplayıcısına bağlanır.
Kaynaklar 16 Ekim 2026: KTB konaklama istatistikleri (2025 yıllık bülten, Ocak–Ağustos 2026 aylık bülten 06.10.2026; YATAK doluluğu),
KTB metaveri, Booking.com Partner Hub (Genius, Preferred, görünürlük, promosyonlar, yorumlar), Google Hotel Center yardım.
Preferred rezervasyon artışı Booking'in iki sayfasında farklı (%20 / %35) → muhafazakâr %20. Mesaj yanıt süresi–sıralama verisi YOK → yazılmaz."""
import html

SRC = [
 ("Kültür ve Turizm Bakanlığı: konaklama istatistikleri", "https://yigm.ktb.gov.tr/TR-201121/bakanlik-belgeli-tesis-konaklama-istatistikleri.html"),
 ("KTB: 2025 yıllık konaklama bülteni (xlsx)", "https://yigm.ktb.gov.tr/Eklenti/145670,konaklama-yillik-b-lten-2025-ver2xlsx.xlsx"),
 ("KTB: 2026 Ağustos aylık konaklama bülteni (xlsx, 6 Ekim 2026)", "https://yigm.ktb.gov.tr/Eklenti/152772,konaklama-aylik-b-lten-2026-ag-stos-06102026xlsx.xlsx"),
 ("KTB: konaklama istatistikleri metaveri", "https://yigm.ktb.gov.tr/TR-201124/metaveri.html"),
 ("Booking.com Partner Hub: Genius programı", "https://partner.booking.com/en-gb/solutions/genius_programme"),
 ("Booking.com Partner Hub: Preferred Partner programı", "https://partner.booking.com/en-gb/solutions/preferred-partner-programme"),
 ("Booking.com Partner Hub: görünürlük ve sıralama", "https://partner.booking.com/en-gb/advice/improve-visibility-and-ranking"),
 ("Booking.com Partner Hub: promosyonlarla misafir çekmek", "https://partner.booking.com/en-gb/learn-more/new-partner/attracting-guests-promotions"),
 ("Booking.com Partner Hub: misafir yorumları", "https://partner.booking.com/en-gb/learn-more/new-partner/handling-guest-reviews"),
 ("Google: ücretsiz rezervasyon bağlantıları", "https://support.google.com/hotelprices/answer/9296693"),
]

def _tbl(head, rows):
    h = "".join(f'<th scope="col">{x}</th>' for x in head)
    b = "".join("<tr>" + f'<th scope="row">{r[0]}</th>' + "".join(f"<td>{c}</td>" for c in r[1:]) + "</tr>" for r in rows)
    return f'<div class="table-wrap"><table class="cmp"><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table></div>'

META = {"tr": dict(key="post-doluluk", date="2026-10-16", title="Otel doluluk oranı nasıl artırılır? 9 yöntem (2026)",
                   desc="Otel doluluk oranı nasıl hesaplanır, Türkiye ortalaması ne? Bakanlık 2025–2026 verileri, RevPAR ve ADR, Booking.com ve Google ile 9 yöntem.")}

def tr(U):
    from build import btn, SIGNUP_URL
    cta = btn("7 gün ücretsiz dene", SIGNUP_URL) + btn("RevPAR hesaplayıcı", U("kpi"), "ghost")
    aylar = _tbl(["Ay", "2025", "2026"], [
        ("Ocak", "%33,1", "%31,2"), ("Şubat", "%30,3", "%26,0"), ("Mart", "%26,8", "%26,9"), ("Nisan", "%41,1", "%35,5"),
        ("Mayıs", "%51,9", "%49,0"), ("Haziran", "%57,8", "%52,2"), ("Temmuz", "%66,0", "%68,0"), ("Ağustos", "%71,2", "%72,7"),
        ("Eylül", "%61,1", "henüz yayımlanmadı"), ("Ekim", "%56,6", "–"), ("Kasım", "%33,1", "–"), ("Aralık", "%31,0", "–")])
    tip = _tbl(["Tesis türü", "2025 yatak doluluğu"], [
        ("Pansiyon (Bakanlık belgeli)", "%35,1"), ("Pansiyon (basit belgeli)", "%33,5"), ("Butik otel", "%42,3"),
        ("Apart otel", "%37,9"), ("3 yıldızlı otel", "%42,1"), ("5 yıldızlı otel", "%61,0"), ("Tüm tesisler", "%49,5")])
    form = _tbl(["Gösterge", "Formül", "Örnek (20 oda, 30 gün)"], [
        ("Doluluk oranı", "Satılan oda ÷ satılabilir oda × 100", "360 ÷ 600 = %60"),
        ("ADR (ortalama oda fiyatı)", "Oda geliri ÷ satılan oda", "1.080.000 TL ÷ 360 = 3.000 TL"),
        ("RevPAR", "Oda geliri ÷ satılabilir oda = ADR × doluluk", "1.080.000 TL ÷ 600 = 1.800 TL")])
    c = f'''<div class="answer"><p><strong>Kısa cevap:</strong> Doluluk oranı, satılan oda sayısının satılabilir oda sayısına oranıdır. Türkiye'de Bakanlık belgeli tesislerde 2025 yatak doluluğu ortalama %49,5; pansiyonlarda %35 civarında, ağustosta %71 ama martta %27. Doluluğu artırmanın en etkili yolları: takvimi tüm kanallarda açık ve güncel tutmak, Booking.com'da yorum puanını ve görünürlüğü yükseltmek, boş dönemlere hedefli indirim ve kısa konaklama kuralı koymak, Google'da ücretsiz rezervasyon bağlantısında görünmek ve mesajlara hızlı cevap vermek. Doluluğu tek başına değil, RevPAR ile birlikte izleyin.</p></div>
<p class="small muted">Rakamlar Kültür ve Turizm Bakanlığı'nın 2025 yıllık ve 2026 Ocak–Ağustos konaklama bültenlerinden ve Booking.com ile Google'ın resmî iş ortağı sayfalarından 16 Ekim 2026'da derlendi.</p>
<h2>Doluluk oranı nasıl hesaplanır?</h2>
<p>Doluluk oranı = satılan oda ÷ satılabilir oda × 100. Satılabilir oda, oda sayınızın dönemdeki gün sayısıyla çarpımıdır; 20 odalı bir otel 30 günde 600 oda satabilir. Yalnız doluluğa bakmak yanıltır: odaları çok ucuza satarak %90 doluluğa ulaşabilirsiniz ama kâr etmeyebilirsiniz. Bu yüzden doluluğu ADR ve RevPAR ile birlikte izleyin.</p>
{form}
<p>Kendi rakamlarınızı <a href="{U("kpi")}">RevPAR, ADR ve doluluk hesaplayıcısıyla</a> hesaplayabilirsiniz.</p>
<h2>Türkiye'de otel doluluk oranları (2025–2026)</h2>
<p>Bakanlık istatistikleri <strong>yatak doluluğunu</strong> ölçer, oda doluluğunu değil; bazı kategorilerde oranın %100'ü geçmesi bu yüzdendir. Yine de sezonun şeklini ve tesis türleri arasındaki farkı iyi gösterir. 2025'te tüm tesislerde ortalama yatak doluluğu %49,5 oldu; 2026'nın ilk sekiz ayında %47,0.</p>
{aylar}
{tip}
<p>Tablodan iki sonuç çıkıyor. Birincisi, küçük tesislerin yıllık doluluğu büyük otellerin çok altında: pansiyonlarda %35, 5 yıldızlılarda %61. İkincisi, kaybedilen doluluk asıl ara sezonda: nisan, mayıs, ekim ve kasım. Kışın doluluğu ağırlıklı olarak yerli misafir taşıyor; 2025 ocağında 33,1 puanlık doluluğun 20,0 puanı yerli misafirdendi.</p>
<h2>Doluluk oranını artırmanın 9 yolu</h2>
<h3>1. Takviminizi bütün kanallarda açık ve doğru tutun</h3>
<p>Satışa kapalı tarih satılmaz. Booking.com, misafirlerin 16 ay öncesinden plan yapabildiğini söylüyor ve takvimi ileriye doğru açık tutmayı öneriyor. Fiyat ve müsaitliği tek tek ekstranetlerde güncellemek yerine bir <a href="{U("channel")}">kanal yöneticisi</a> kullanırsanız hem açık tarih kalmaz hem de <a href="{U("post-overbooking")}">overbooking</a> riski düşer.</p>
<h3>2. Yorum puanınızı yükseltin</h3>
<p>Booking.com'a göre puanınız yükseldikçe arama sonuçlarında görünme ihtimaliniz artar ve yorumlar dönüşüm oranını ciddi biçimde etkiler. Puan, son 36 ayın genel puanıdır. Her yoruma, özellikle olumsuzlara kısa ve kişisel cevap verin.</p>
<h3>3. Genius'a katılın, gerekirse duraklatın</h3>
<p>Booking.com'un açıklamasına göre Genius'a katılan tesisler ortalama %30 daha fazla arama görüntülemesi alıyor; indirim maliyeti düşüldükten sonra gelirde ortalama %40 artış görüyor. Şart: en az 3 yorum, en az 7,5 puan ve en az %10 indirim. Yoğun tarihlerde fiyatınızı korumak için Genius'u yılda belli günler duraklatabilirsiniz.</p>
<h3>4. Preferred Partner programını değerlendirin</h3>
<p>Preferred tesisler Booking.com'a göre ortalama %65 daha fazla görüntüleme ve %20 daha fazla rezervasyon alıyor. Programa bölgedeki tesislerin en fazla %30'u girebiliyor ve karşılığında daha yüksek komisyon ödüyorsunuz. Hesabı yapmadan girmeyin: <a href="{U("post-bookingkom")}">Booking.com komisyonu</a> yazımız bu hesabı anlatıyor.</p>
<h3>5. Boş dönemlere hedefli promosyon koyun</h3>
<p>Booking.com'un temel promosyonu, doluluk boşluklarını hedeflemek için indirimi, tarihleri ve minimum konaklama süresini seçmenize izin veriyor. Erken rezervasyon, son dakika ve mobil fiyatlar da var; en fazla üç indirim birleşebiliyor. Bütün yıla indirim vermek yerine yalnız boş haftalara indirim verin.</p>
<h3>6. Minimum konaklama kuralını akıllıca kullanın</h3>
<p>Kısıtlama koyduğunuz tarihler, o kısıtlamaya uymayan aramalarda hiç görünmeyebilir. Yoğun hafta sonunda 2 gece kuralı mantıklıdır; ara sezonda aynı kural boş gece bırakır. Booking.com satılmayan odalara göre otomatik değişen dinamik kısıtlamaları öneriyor.</p>
<h3>7. Google'da ücretsiz rezervasyon bağlantısında görünün</h3>
<p>Google otel aramalarında "Tüm seçenekler" altında ücretsiz rezervasyon bağlantıları gösteriyor; bu tıklamalar için ücret alınmıyor. Kendi rezervasyon motorunuz ya da bağlantı ortağınız varsa burada otelinizin kendi sitesi de listelenebilir. Bu, komisyonsuz doğrudan rezervasyon demektir.</p>
<h3>8. Ara sezon için yerli misafiri hedefleyin</h3>
<p>Bakanlık verisi kışın ve ara sezonda doluluğu yerli misafirin taşıdığını gösteriyor. Hafta sonu paketleri, uzun konaklama indirimi, iş seyahati ve yakın şehirlere yönelik kampanyalar bu dönemde yabancı pazardan daha hızlı sonuç verir.</p>
<h3>9. Mesajlara hızlı ve her dilde cevap verin</h3>
<p>Booking.com, özenli cevapların iptal ihtimalini azaltıp yorum puanını yükselttiğini söylüyor. Gece gelen bir "müsait misiniz?" sorusu sabaha kalırsa misafir başka otele geçer. <a href="{U("ai")}">Yapay zekâ misafir asistanı</a> gece de dahil her mesaja misafirin dilinde cevap verebilir; <a href="{U("post-autoreply")}">Booking.com mesajlarına otomatik cevap</a> yazımız ayrıntıları anlatıyor.</p>
<h2>Hostlio Pro ile doluluğu takip etmek</h2>
<p>Hostlio Pro rezervasyon takvimini, 100'den fazla kanala bağlanan kanal yöneticisini ve AI asistan Lio'yu tek panelde toplar. Lio her sabah fiyat ve gelir fırsatları için öneri getirir (onayınız olmadan hiçbir şey değişmez); doluluk, ADR ve RevPAR'ı kendi rakamlarınızla izlemek için ücretsiz hesaplayıcıyı kullanabilirsiniz.</p>
<div class="cta-row" style="margin-top:12px">{cta}</div>
'''
    lis = "".join(f'<li><a href="{u}" rel="nofollow noopener">{html.escape(n)}</a></li>' for n, u in SRC)
    c += f'<h2>Kaynaklar</h2><p class="small muted">Tüm kaynaklara 16 Ekim 2026 tarihinde erişildi.</p><ul>{lis}</ul>'
    faq = [("Otel doluluk oranı nasıl hesaplanır?", "Satılan oda sayısı satılabilir oda sayısına bölünür ve 100 ile çarpılır. 20 odalı bir otel 30 günde 360 oda sattıysa doluluk 360 ÷ 600 = %60'tır."),
           ("Türkiye'de otel doluluk oranı ortalaması nedir?", "Kültür ve Turizm Bakanlığı verilerine göre Bakanlık belgeli tesislerde 2025 yatak doluluğu %49,5, pansiyonlarda yaklaşık %35 oldu. 2026'nın ilk sekiz ayında ortalama %47,0."),
           ("Doluluk mu RevPAR mı daha önemli?", "RevPAR. Doluluk ucuz satışla da yükselir; RevPAR hem doluluğu hem fiyatı birlikte gösterir (RevPAR = ADR × doluluk)."),
           ("Booking.com'da görünürlük nasıl artırılır?", "Yorum puanını yükseltmek, takvimi açık tutmak, Genius ve hedefli promosyonlar kullanmak Booking.com'un kendi önerileri arasında.")]
    return c, faq

FN = {"tr": tr}
