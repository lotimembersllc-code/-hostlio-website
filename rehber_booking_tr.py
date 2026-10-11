"""Takvim yazısı (15 Ekim 2026): "Booking.com komisyonu ne kadar, nasıl düşürülür?" — yalnız TR.
Resmî kaynaklar 12 Ekim 2026: Booking.com Partner Help (komisyon, Preferred, Visibility Booster, Genius, Payments),
Rekabet Kurulu 17-01/12-4, AB DMA. Resmî oran YOK (%15 resmî değil); TR'de yurt içi satış 2017'den beri kapalı (basın);
"Yabancı Dijital Konaklama Platformları" teklifi komisyonda kabul (6.10.2026), YASA DEĞİL. Hostlio'nun rezervasyon motoru yok."""
import html

SRC = [
 ("Booking.com Partner Help: Understanding your commission", "https://partner.booking.com/en-gb/help/payments-payouts-invoices/invoices/understanding-your-commission"),
 ("Booking.com Partner Help: Preferred Partner Programme", "https://partner.booking.com/en-gb/help/performance/tools-programmes/understanding-preferred-partner-programme"),
 ("Booking.com Partner Help: Visibility Booster", "https://partner.booking.com/en-gb/help/performance/tools-programmes/all-you-need-know-about-visibility-booster"),
 ("Booking.com Partner Help: Genius", "https://partner.booking.com/en-us/help/growing-your-business/tools-programs/understanding-genius-marketing-program"),
 ("Booking.com Partner Help: Payments by Booking.com", "https://partner.booking.com/en-us/help/payments-payouts-invoices/payments-bookingcom/joining-payments-bookingcom"),
 ("Booking.com Partner Help: Misafirle iletişim", "https://partner.booking.com/en-gb/help/reservations/contact-extranet/contacting-your-guests"),
 ("Rekabet Kurulu kararı 17-01/12-4 (Booking.com)", "https://www.rekabet.gov.tr/Dosya/nihai-karar-aciklamalari/tefhim-duyurulari/bookingsonn-20180226105418631.pdf"),
 ("Anadolu Ajansı: Booking.com'un Türkiye'deki faaliyetlerinin durdurulması (2017)", "https://www.aa.com.tr/en/turkey/turkey-court-rules-unfair-competition-of-bookingcom/1618938"),
 ("AA: Yabancı Dijital Konaklama Platformları Kanun Teklifi komisyonda kabul edildi (6.10.2026)", "https://www.foreks.com/haber/detay/6ac5179795016b5817e66198/AA/tr/yabanci-dijital-konaklama-platformlari-kanunu-teklifi-komisyonda-kabul-edildi-06-10-26/"),
 ("Avrupa Komisyonu: Booking, Dijital Piyasalar Yasası yükümlülükleri (14.11.2024)", "https://digital-markets-act.ec.europa.eu/booking-must-comply-all-relevant-obligations-under-digital-markets-act-2024-11-14_en"),
 ("GİB: Vergi takvimi", "https://gib.gov.tr/vergi-takvimi"),
]

def _tbl(head, rows):
    h = "".join(f'<th scope="col">{x}</th>' for x in head)
    b = "".join("<tr>" + f'<th scope="row">{r[0]}</th>' + "".join(f"<td>{c}</td>" for c in r[1:]) + "</tr>" for r in rows)
    return f'<div class="table-wrap"><table class="cmp"><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table></div>'

META = {"tr": dict(key="post-bookingkom", date="2026-10-12", title="Booking.com komisyonu ne kadar, nasıl düşürülür? (2026)",
                   desc="Booking.com komisyonu nasıl hesaplanır, oran neye göre değişir, Preferred ve Genius maliyeti, KDV ve %17 tavan teklifi. Resmî kaynaklı rehber.")}

def tr(U):
    from build import btn, SIGNUP_URL
    cta = btn("7 gün ücretsiz dene", SIGNUP_URL) + btn("Komisyon hesaplayıcı", U("commission"), "ghost")
    ex = _tbl(["Kalem", "Tutar", "Not"], [
        ("Konaklama bedeli (oda + temizlik ücreti)", "10.000 TL", "Komisyon toplam rezervasyon tutarı üzerinden"),
        ("Komisyon (örnek %15)", "1.500 TL", "Oran sözleşmenize göre değişir; %15 yalnız örnek"),
        ("Komisyon faturasındaki KDV", "Sorumlu sıfatıyla beyan", "Yurt dışından alınan hizmet; mali müşavirinize danışın"),
        ("Size kalan (KDV ve diğer vergiler hariç)", "8.500 TL", "Preferred ya da Visibility Booster açıksa daha az")])
    c = f'''<div class="answer"><p><strong>Kısa cevap:</strong> Booking.com komisyonu, misafirin ödediği toplam rezervasyon tutarının (oda ücreti ve sizin eklediğiniz temizlik, iptal gibi ücretler dahil) belirli bir yüzdesidir. Booking.com resmî bir oran yayınlamaz: oran ülkeye, tesis tipine ve sözleşmenize göre değişir ve extranet'te görünür. Sıkça dile getirilen "%15 ortalama" resmî bir rakam değildir. Preferred Partner ve Visibility Booster gibi programlar oranı artırır; komisyonu düşürmenin yolu bu programları bilinçli kullanmak, iptal ve no-show'ları zamanında işaretlemek ve doğrudan rezervasyonu büyütmektir.</p></div>
<p class="small muted">Bu yazı genel bilgilendirme amaçlıdır. Bilgiler 12 Ekim 2026'da Booking.com'un iş ortağı yardım sayfaları ve resmî kaynaklardan derlendi. Kendi oranınız ve kurallarınız için sözleşmenize (Genel Teslim Koşulları) ve extranet'e bakın; vergi konularında mali müşavirinize danışın.</p>
<h2>Booking.com komisyonu nasıl hesaplanır?</h2>
<p>Booking.com'a göre komisyon, toplam rezervasyon tutarının belirli bir yüzdesidir. Bu tutara oda ücreti ve sizin eklediğiniz ücretler (temizlik, hizmet, no-show ya da iptal ücreti) dahildir. Belediyenin aldığı konaklama vergisi gibi yerel vergilerden komisyon alınmaz, ama çoğu ülkede KDV dahil tutar üzerinden komisyon hesaplanır. Komisyon misafir çıkış yaptıktan sonra kesinleşir ve oran rezervasyon anında sabitlenir.</p>
<h3>Hangi durumlarda komisyon ödersiniz?</h3>
<ul><li>Tamamlanan konaklamalar</li><li>Misafir gelmese bile iade edilmez ve kısmen iade edilir rezervasyonlar</li><li>Tahsil ettiğiniz no-show ve iptal ücretleri</li><li>Overbooking (son 12 ayda 5'ten azsa ya da tesis 30 günden yeniyse alınmaz)</li></ul>
<h3>Ne zaman komisyon ödemezsiniz?</h3>
<ul><li>Vazgeçtiğiniz ücretler</li><li>Çıkıştan sonraki 48 saat içinde işaretlediğiniz no-show'lar</li><li>Geçersiz olarak işaretlenen kartlar</li></ul>
<p>48 saat içinde işaretlenmeyen değişiklikler tam komisyonla faturalanır. Bu tek kural bile yılda ciddi tutar demek olabilir.</p>
<h2>Örnek hesap</h2>
{ex}
<p>Kendi rakamlarınızla kanal bazında net geliri görmek için <a href="{U("commission")}">OTA komisyon hesaplayıcısını</a> kullanabilirsiniz.</p>
<h2>Fatura ve ödeme</h2>
<p>Booking.com ayda bir fatura keser; fatura bir önceki ay <strong>çıkış yapan</strong> rezervasyonları kapsar (örneğin 1 Şubat çıkışlı rezervasyon mart faturasına girer). Banka havalesi, bazı ülkelerde kart ya da otomatik ödeme kullanılabilir; "Payments by Booking.com" kullanıyorsanız komisyon size yapılan ödemeden düşülebilir. Ödenmeyen faturalar tesisin geçici olarak satışa kapanmasına yol açabilir. Son 3 ayın rezervasyonları için itiraz edebilirsiniz.</p>
<p><strong>KDV:</strong> Komisyon faturası yurt dışından alınan bir hizmettir; Türkiye'deki tesis bu hizmetin KDV'sini sorumlu sıfatıyla 2 No.lu KDV Beyannamesi ile beyan eder. Oran ve uygulama için mali müşavirinizle teyit edin.</p>
<h2>Komisyonu artıran programlar</h2>
<ul><li><strong>Preferred Partner Programı:</strong> Booking.com'un ifadesiyle "komisyonda küçük bir artış karşılığında" daha fazla görünürlük. Booking.com ortalamada %65 daha fazla görüntülenme ve %20 daha fazla rezervasyon olduğunu söylüyor. Ek oranı resmî sayfalarda yazmıyor. İstediğiniz zaman çıkabilirsiniz; şartları kaybedip çıkarsanız 180 gün tekrar katılamazsınız.</li>
<li><strong>Visibility Booster:</strong> Seçtiğiniz tarihler ve hedef ülkeler için komisyonu kendiniz yükseltirsiniz. Geçicidir, kapatılabilir.</li>
<li><strong>Genius:</strong> Komisyon değil indirimdir (seviyeye göre %10, %15, %20). Komisyon indirimli fiyat üzerinden hesaplandığı için asıl maliyetiniz indirimin kendisidir. Belirli odalara uygulayabilir, tarihlerde durdurabilirsiniz.</li>
<li><strong>Payments by Booking.com:</strong> Havaleyle ödemede, tesisin konumuna göre değişen bir ödeme hizmeti ücreti alınır; sanal kart kullanımında ise kendi bankanızın işlem ücreti olabilir.</li></ul>
<h2>Booking.com komisyonu nasıl düşürülür? 7 yol</h2>
<ol><li><strong>No-show ve iptalleri 48 saat içinde işaretleyin.</strong> Geç kalan her işaret tam komisyon demek.</li>
<li><strong>Ücretli programları ölçerek kullanın.</strong> Preferred ve Visibility Booster'ı yalnız boş kalacak dönemlerde açın, dolu sezonda kapatın.</li>
<li><strong>Genius'u seçerek uygulayın.</strong> Tüm odalara değil, satmakta zorlandığınız oda ve tarihlere.</li>
<li><strong>İptal politikanızı gözden geçirin.</strong> Tahsil ettiğiniz iptal ücretinden de komisyon ödersiniz.</li>
<li><strong>Doğrudan rezervasyonu büyütün.</strong> Web siteniz, telefonunuz ve WhatsApp'tan gelen her rezervasyon komisyonsuzdur. Tekrar gelen misafire doğrudan rezervasyon avantajı sunun.</li>
<li><strong>Kanal bazında net gelire bakın.</strong> Brüt rezervasyon değil, komisyon sonrası kalan tutar önemlidir.</li>
<li><strong>Booking.com misafirini platform dışına taşımayın.</strong> Booking.com iletişimin platformda kalmasını istiyor; onaylı bir rezervasyonu dışarı almak sözleşmenize aykırı olabilir ve hesabınızı riske atar.</li></ol>
<h2>Fiyat eşitliği (parite) ve Türkiye</h2>
<p>Booking.com ülkeleri geniş pariteli, dar pariteli ve paritesiz olarak ayırır; tesisinizin durumu sözleşmenizde yazar. Avrupa Birliği'nde Booking.com, Dijital Piyasalar Yasası kapsamında 14 Kasım 2024'ten beri otellerin kendi sitelerinde ve diğer kanallarda daha uygun fiyat vermesini kısıtlayamıyor; bu kural Türkiye'de geçerli değil. Türkiye'de Rekabet Kurulu 2017'de Booking.com'un parite koşullarını rekabete aykırı bularak para cezası vermişti.</p>
<h2>Türkiye'ye özel durum</h2>
<ul><li><strong>Yurt içi satış:</strong> 2017'deki mahkeme kararından beri Türkiye'deki kullanıcılar Booking.com'dan Türkiye'deki otellere rezervasyon yapamıyor; yabancı misafirler yapabiliyor. Basında bu durumun Ekim 2026'da da sürdüğü yazılıyor.</li>
<li><strong>Kanun teklifi:</strong> "Yabancı Dijital Konaklama Platformları" kanun teklifi 6 Ekim 2026'da TBMM komisyonunda kabul edildi. Teklif; izin, Türkiye'de temsilci, binde 7,5 turizm payı, komisyona <strong>%17 tavan</strong> ve tesislerin başka kanallardan farklı fiyatla satış yapmasının engellenmemesi gibi hükümler içeriyor. <strong>Henüz yasalaşmadı;</strong> Genel Kurul'dan geçerse 1 Ocak 2027'de yürürlüğe girmesi öngörülüyor. Yasalaşırsa bu yazıyı güncelleyeceğiz.</li></ul>
<h2>Hostlio Pro bu işte nasıl yardımcı olur?</h2>
<p>Hostlio Pro'nun <a href="{U("channel")}">kanal yöneticisi</a> Booking.com dahil 100'den fazla kanalda fiyat ve müsaitliği tek yerden yönetir; analiz ekranı her kanalın brüt gelirini, komisyonunu ve net gelirini yan yana gösterir. WhatsApp'ta misafirlere cevap veren AI asistan Lio, doğrudan gelen soruları kaçırmamanızı sağlar; Pro ve Growth'ta misafirin rezervasyon talebini toplar, siz onaylayınca rezervasyona dönüşür. Açık olalım: Hostlio Pro'nun kendi rezervasyon motoru ya da online ödeme tahsilatı yoktur.</p>
<div class="cta-row" style="margin-top:12px">{cta}</div>
'''
    lis = "".join(f'<li><a href="{u}" rel="nofollow noopener">{html.escape(n)}</a></li>' for n, u in SRC)
    c += f'<h2>Kaynaklar</h2><p class="small muted">Tüm kaynaklara 12 Ekim 2026 tarihinde erişildi. "%15 ortalama", "%10–25 aralığı" ve Preferred için dolaşan ek oranlar Booking.com tarafından yayımlanmış rakamlar değildir.</p><ul>{lis}</ul>'
    faq = [("Booking.com komisyonu yüzde kaç?", "Booking.com resmî bir oran yayınlamaz; oran ülkeye, tesis tipine ve sözleşmenize göre değişir ve extranet'te Finans bölümünde görünür. Sıkça söylenen %15 ortalama resmî bir rakam değildir."),
           ("Booking.com komisyonu KDV dahil mi hesaplanır?", "Booking.com'a göre çoğu ülkede komisyon KDV dahil tutar üzerinden hesaplanır; belediyenin aldığı konaklama vergisi gibi yerel vergilerden komisyon alınmaz. Tesisinize ne uygulandığı sözleşmenizde yazar."),
           ("Preferred Partner komisyonu ne kadar artırır?", "Booking.com yalnızca 'komisyonda küçük bir artış' diyor; güncel resmî sayfalarda oran yok. Programdan istediğiniz zaman çıkabilirsiniz."),
           ("Türkiye'de Booking.com komisyonuna tavan var mı?", "Şu an yok. Yabancı Dijital Konaklama Platformları kanun teklifi %17 tavan öngörüyor; 6 Ekim 2026'da TBMM komisyonunda kabul edildi ama henüz yasalaşmadı."),
           ("Türkler Booking.com'dan Türkiye'deki otellere rezervasyon yapabilir mi?", "2017'deki mahkeme kararından beri yapamıyor; yabancı misafirler Türkiye'deki otellere Booking.com üzerinden rezervasyon yapmaya devam ediyor.")]
    return c, faq

FN = {"tr": tr}
