"""post-whatsapp TR sürümü (takvim: 3 Kasım planı, öne alındı; 16 Ekim 2026).
Resmî kaynaklar 16 Ekim 2026: Meta (fiyatlandırma sayfası 30.09.2026 güncel; 1.10.2026'dan beri servis mesajı ayda 1.000'den sonra
ücretli; Türkiye ücret kartı), WhatsApp Business Policy (23.09.2026), Coexistence dokümanı; 6563 s. Kanun md. 6/8, Ticari İletişim
Yönetmeliği md. 5/6/7, İYS (RG 04.01.2020); KVKK md. 9/10 (7499 s. Kanun), KVKK 2021/891 WhatsApp kararı.
Hostlio iddiaları yalnız canlı: Lio WhatsApp her planda, rezervasyon talebi Pro/Growth onaylı. Coexistence Hostlio'da İDDİA EDİLMEZ."""
import html

SRC = [
 ("Meta: WhatsApp Business Platform fiyatlandırması", "https://developers.facebook.com/docs/whatsapp/pricing"),
 ("Meta: mesaj gönderme ve 24 saatlik pencere", "https://developers.facebook.com/docs/whatsapp/cloud-api/guides/send-messages"),
 ("WhatsApp Business Messaging Policy", "https://whatsappbusiness.com/policy/"),
 ("Meta: şablon kategorileri", "https://developers.facebook.com/documentation/business-messaging/whatsapp/templates/template-categorization/"),
 ("Meta: WhatsApp Business uygulaması kullanıcılarını Platform'a bağlama (Coexistence)", "https://developers.facebook.com/documentation/business-messaging/whatsapp/embedded-signup/onboarding-business-app-users"),
 ("6563 sayılı Elektronik Ticaretin Düzenlenmesi Hakkında Kanun", "https://www.mevzuat.gov.tr/mevzuatmetin/1.5.6563.pdf"),
 ("Ticari İletişim ve Ticari Elektronik İletiler Hakkında Yönetmelik (RG 15.07.2015)", "https://www.resmigazete.gov.tr/eskiler/2015/07/20150715-4.htm"),
 ("Yönetmelik değişikliği, İYS (RG 04.01.2020)", "https://www.resmigazete.gov.tr/eskiler/2020/01/20200104-2.htm"),
 ("6698 sayılı Kişisel Verilerin Korunması Kanunu", "https://www.mevzuat.gov.tr/mevzuatmetin/1.5.6698.pdf"),
 ("KVKK: WhatsApp hakkında kamuoyu duyurusu (2021/891)", "https://www.kvkk.gov.tr/Icerik/7045/WHATSAPP-UYGULAMASI-HAKKINDA-YURUTULEN-RESEN-INCELEMEYE-ILISKIN-KAMUOYU-DUYURUSU"),
]

def _tbl(head, rows):
    h = "".join(f'<th scope="col">{x}</th>' for x in head)
    b = "".join("<tr>" + f'<th scope="row">{r[0]}</th>' + "".join(f"<td>{c}</td>" for c in r[1:]) + "</tr>" for r in rows)
    return f'<div class="table-wrap"><table class="cmp"><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table></div>'

META_TR = dict(key="post-whatsapp", date="2026-10-16", title="WhatsApp ile otel rezervasyonu ve misafir iletişimi (2026)",
               desc="Oteller için WhatsApp rehberi: Business uygulaması mı API mi, 24 saat kuralı, 2026 Meta ücretleri, İYS ve KVKK, rezervasyon talebi ve otomatik cevap.")

def tr(U):
    from build import btn, SIGNUP_URL
    cta = btn("7 gün ücretsiz dene", SIGNUP_URL) + btn("Otel WhatsApp asistanı", U("whatsapp-tr"), "ghost")
    karsi = _tbl(["", "WhatsApp Business uygulaması", "WhatsApp Business Platform (API)"], [
        ("Kimin için", "Mesajlara elle cevap veren tek işletmeci", "Ekip, otomatik cevap, PMS ve AI asistan bağlantısı"),
        ("Cihaz", "Bir telefon ve en fazla 4 bağlı cihaz", "Panel üzerinden, birden fazla kullanıcı"),
        ("Otomasyon", "Karşılama ve uzaktayım mesajları", "Kurallar, şablonlar, AI ile otomatik cevap"),
        ("Ücret", "Uygulama ücretsiz", "Meta mesaj başına ücretlendirir (aşağıda)")])
    ucret = _tbl(["Mesaj türü", "Ne zaman", "Türkiye ücreti (1 Ekim 2026)"], [
        ("Servis (misafire cevap)", "Misafirin son mesajından sonraki 24 saat içinde, serbest metin", "Her numara için ayda ilk 1.000 mesaj ücretsiz; sonrası mesaj başına 0,0009 $"),
        ("Hizmet (utility) şablonu", "Rezervasyon onayı, check-in bilgisi gibi bilgilendirmeler", "0,0009 $"),
        ("Pazarlama şablonu", "Kampanya, teklif, tekrar davet", "0,0109 $"),
        ("Doğrulama şablonu", "Tek kullanımlık kod", "0,0009 $")])
    c = f'''<div class="answer"><p><strong>Kısa cevap:</strong> Misafirler WhatsApp'ı zaten kullandığı ve hızlı cevap verdiği için oteller için en etkili iletişim kanalıdır. Tek kişilik küçük bir işletme ücretsiz WhatsApp Business uygulamasıyla başlayabilir; ekip, otomatik cevap ya da AI asistan gerekiyorsa WhatsApp Business Platform (API) kullanılır. Misafirin son mesajından sonraki 24 saat içinde serbestçe cevap verebilirsiniz; bu sürenin dışında Meta'nın onayladığı bir şablon gerekir. 1 Ekim 2026'dan beri misafire verilen cevaplar her numara için ayda ilk 1.000 mesajdan sonra ücretli. Kampanya mesajı göndermek için misafirin onayı ve İYS kaydı gerekir; rezervasyonla ilgili bilgilendirmeler için gerekmez.</p></div>
<p class="small muted">Bu yazı genel bilgilendirme amaçlıdır, hukuki danışmanlık değildir. Meta'nın kuralları ve ücretleri ile Türk mevzuatı 16 Ekim 2026 tarihinde resmî kaynaklardan derlendi; Meta kurallarını ve ücretlerini sık değiştirir.</p>
<h2>WhatsApp Business uygulaması mı, API mi?</h2>
{karsi}
<p>Aynı numarayı hem uygulamada hem Platform'da kullanmak Meta'nın "Coexistence" özelliğiyle mümkün: Mevcut uygulama numarası bir çözüm ortağı üzerinden Platform'a bağlanır ve sohbet geçmişi iki yönde eşitlenir. Bu durumda uygulamadaki grup, kaybolan mesaj ve yayın listesi gibi bazı özellikler kapanır; telefon 14 gün kadar kullanılmazsa bağlantı kopar. Kuracağınız sağlayıcıya bu özelliği destekleyip desteklemediğini sorun.</p>
<h2>24 saat kuralı</h2>
<p>Misafir size yazdığında 24 saatlik bir "müşteri hizmeti penceresi" açılır ve misafirin her yeni mesajı pencereyi yeniler. Pencere açıkken serbest metinle cevap verebilirsiniz. Pencere kapandıktan sonra yalnızca Meta'nın onayladığı mesaj şablonlarını gönderebilirsiniz. Pratikte bu, "geçen hafta yazan misafire bugün serbestçe yazamam" demektir: Rezervasyon onayı, check-in bilgisi ya da hatırlatma için önceden onaylanmış şablonlar hazırlamanız gerekir.</p>
<h2>2026'da Meta ücretleri</h2>
<p>Platform 1 Temmuz 2025'ten beri mesaj başına ücretlendiriliyor; misafirin size yazdığı mesajlar ücretsiz, ücret yalnızca işletmenin teslim edilen mesajlarından alınıyor. 1 Ekim 2026'dan itibaren iki şey değişti: Misafire verilen servis cevapları her işletme numarası için ayda ilk 1.000 mesajdan sonra ücretli, pencere içinde gönderilen hizmet (utility) şablonları da yeniden ücretli.</p>
{ucret}
<p class="small muted">Ücretler Meta'nın fiyatlandırma sayfasındaki ücret kartından, dolar olarak; Türk lirası ücret listesi yayınlanmıyor. Hizmet ve doğrulama mesajlarında hacim indirimi var.</p>
<h2>Şablonlar ve onay: neyi gönderebilirsiniz?</h2>
<ul><li><strong>Hizmet (utility):</strong> Misafirin bir işlemine bağlı, kişiye özel ve tanıtım içermeyen mesajlar: rezervasyon onayı, check-in saati, adres. İçine bir teklif eklerseniz Meta şablonu pazarlama sayar.</li>
<li><strong>Pazarlama:</strong> Kampanya, indirim, "tekrar bekleriz" mesajları.</li>
<li><strong>Onay (opt-in):</strong> Meta, bir kişiye WhatsApp'tan yazabilmeniz için numarasını size vermiş olmasını ve işletmenizin adıyla açıkça onay almış olmanızı ister. Mesaj almak istemeyenlerin talebine uymak zorunludur.</li>
<li><strong>Hassas bilgi:</strong> Meta politikasına göre sohbette misafirden tam kart numarası ya da kimlik numarası istenmemelidir.</li></ul>
<h2>Türkiye'de ticari ileti kuralları: İYS ve onay</h2>
<p>6563 sayılı Kanun'a göre mal ya da hizmet tanıtan ticari elektronik iletiler için alıcının önceden onayı gerekir. Ancak misafire, aldığı hizmetle ilgili değişiklik, kullanım ve bakım hakkında gönderilen iletiler için ayrıca onay gerekmez. Yönetmelik de abonelik, ödeme, bilgi güncelleme, satın alma, teslimat ve benzeri durumlara ilişkin bildirimleri onaydan muaf tutar; bu bildirimlerde tanıtım yapılamaz. Ticari ileti göndermek isteyen işletmeler İleti Yönetim Sistemi'ne (İYS) kaydolur ve İYS'ye kaydedilmeyen onaylar geçersiz sayılır. Misafir ret hakkını her zaman ücretsiz kullanabilir; gönderim 3 iş günü içinde durdurulmalıdır.</p>
<p>Pratikte: Rezervasyon onayı, giriş bilgisi ve konaklamayla ilgili hatırlatmalar bilgilendirme sayılır. Kampanya, indirim ve tekrar davet mesajları ise ticari iletidir; onay ve İYS kaydı gerekir. Onay, hizmetin verilmesi için şart koşulamaz.</p>
<h2>KVKK: aydınlatma ve yurt dışına aktarım</h2>
<p>Misafirin telefon numarası ve yazışmaları kişisel veridir. KVKK'nın 10. maddesine göre veriyi toplarken misafiri kimin, hangi amaçla, kime aktararak işlediğiniz ve haklarını konusunda bilgilendirmeniz gerekir. WhatsApp Business Platform kullanmak verinin yurt dışındaki sunuculara gitmesi demektir; 1 Haziran 2024'ten beri yürürlükte olan düzenlemeye göre düzenli aktarımlar yeterlilik kararı ya da standart sözleşme gibi güvencelere dayanmalı, açık rıza yalnızca arızi aktarımlarda kullanılabilir. KVK Kurulu 2021'de WhatsApp'a aydınlatma ve yurt dışı aktarım ihlalleri nedeniyle para cezası vermişti. Aydınlatma metninizi mali müşaviriniz ya da hukuk danışmanınızla birlikte güncelleyin.</p>
<h2>WhatsApp'tan rezervasyon nasıl alınır?</h2>
<ol><li><strong>Numarayı görünür yapın:</strong> Web sitenizde, Google profilinizde ve onay e-postalarında WhatsApp bağlantısı olsun.</li>
<li><strong>Hızlı cevap verin:</strong> Fiyat soran misafir genelde birkaç oteli aynı anda soruyor; ilk düzgün cevap çoğu zaman kazanır.</li>
<li><strong>Bilgileri tek seferde toplayın:</strong> Tarihler, kişi sayısı, oda tercihi.</li>
<li><strong>Fiyatı ve koşulları net yazın:</strong> Kahvaltı, iptal koşulu, ödeme şekli.</li>
<li><strong>Onayı yazılı verin:</strong> Rezervasyonu sisteminize girin ve misafire bilgilendirme olarak onay gönderin.</li></ol>
<p>Sık sorulan sorulara otomatik cevap vermek için <a href="{U("post-ai")}">misafir mesajlarını yapay zekâ ile yanıtlamak</a>, Booking.com mesajları için <a href="{U("post-autoreply")}">Booking.com mesajlarına otomatik cevap</a> rehberlerine bakabilirsiniz.</p>
<h2>Hostlio Pro'da WhatsApp</h2>
<p>Hostlio Pro'nun AI asistanı Lio, misafirlere WhatsApp'tan her planda, otelinizin bilgileriyle ve misafirin dilinde cevap verir; WhatsApp ve OTA mesajları tek gelen kutusunda toplanır. Pro ve Growth planlarında misafir WhatsApp'tan oda sorduğunda Lio tarihleri, kişi sayısını ve oda tercihini toplar, sizin fiyat ve müsaitliğinizden fiyat verir; talep size gelir ve siz onaylayınca rezervasyona dönüşür. Lio rezervasyonu kendi başına onaylamaz; indirim, şikâyet gibi kararları size bırakır. Ayrıntılar <a href="{U("whatsapp-tr")}">otel WhatsApp asistanı</a> sayfasında.</p>
<div class="cta-row" style="margin-top:12px">{cta}</div>
'''
    lis = "".join(f'<li><a href="{u}" rel="nofollow noopener">{html.escape(n)}</a></li>' for n, u in SRC)
    c += f'<h2>Kaynaklar</h2><p class="small muted">Tüm kaynaklara 16 Ekim 2026 tarihinde erişildi.</p><ul>{lis}</ul>'
    faq = [("WhatsApp Business oteller için ücretsiz mi?", "WhatsApp Business uygulaması ücretsiz. WhatsApp Business Platform'da (API) Meta mesaj başına ücret alır; 1 Ekim 2026'dan beri misafire verilen cevaplar her numara için ayda ilk 1.000 mesajdan sonra ücretli (Türkiye için mesaj başına 0,0009 $)."),
           ("Misafire 24 saatten sonra WhatsApp'tan yazabilir miyim?", "Yalnızca Meta'nın onayladığı bir mesaj şablonuyla ve misafir sizden mesaj almayı onayladıysa. Serbest metinli cevaplar misafirin son mesajından sonraki 24 saat içinde gönderilebilir."),
           ("Rezervasyon onayı göndermek için İYS kaydı gerekir mi?", "Rezervasyon onayı ve konaklamayla ilgili bilgilendirmeler, tanıtım içermedikleri sürece onaydan muaftır. Kampanya ve tekrar davet gibi ticari iletiler için misafirin onayı ve İYS kaydı gerekir."),
           ("Aynı numarayı hem telefonda hem panelde kullanabilir miyim?", "Meta'nın Coexistence özelliğiyle, destekleyen bir sağlayıcı üzerinden mümkün; bu durumda uygulamadaki bazı özellikler (gruplar, yayın listeleri) kapanır."),
           ("Hostlio Pro WhatsApp'tan rezervasyon alır mı?", "Pro ve Growth planlarında Lio misafirin rezervasyon talebini toplar ve fiyat verir; talep size gelir, siz onaylayınca rezervasyona dönüşür. Lio rezervasyonu kendi başına onaylamaz.")]
    return c, faq
