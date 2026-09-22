"""K5 (Eylül 2026) — güncel Gizlilik Politikası, Kullanım Şartları, Veri İşleme Sözleşmesi (DPA) ve
Güvenlik ve veri sayfası. İngilizce metin esastır; diğer diller çeviridir (legal_v6_intl.py).

🔺 Yayından önce bir avukatın son okuması önerilir (rapor K5).
🔺 RETENTION içindeki süreler koddan/rapordan alındı — sunucu tarafı (Supabase) ile teyit edin:
   - mesaj içeriği: panel Kurulum → "Message Retention (days)", varsayılan 60 gün (Setup1.jsx)
   - misafir iletişim bilgisi: 90 gün (analiz raporu, "kodda tanımlı")
"""
LEGAL_ISO = "2026-09-23"
LEGAL_DATE = {"en": "September 23, 2026", "tr": "23 Eylül 2026", "es": "23 de septiembre de 2026",
              "it": "23 settembre 2026", "pt": "23 de setembro de 2026", "fr": "23 septembre 2026"}
RETENTION = {"msg_default_days": 60, "guest_contact_days": 90, "deletion_days": 30}
QUOTA = {"starter": "1,000", "pro": "5,000", "growth": "12,000"}

# Alt işleyiciler — gizlilik, DPA ve güvenlik sayfalarında aynı liste
SUBPROCESSORS = [
    # (ad, konum, amaç anahtarı)
    ("Supabase, Inc.", "USA", "db"),
    ("Vercel, Inc.", "USA", "web"),
    ("Stripe, Inc.", "USA", "pay"),
    ("Anthropic, PBC", "USA", "ai"),
    ("Meta Platforms, Inc. (WhatsApp Business Platform)", "USA / Ireland", "wa"),
    ("Channex.io Ltd", "United Kingdom", "chx"),
    ("Make (Celonis)", "EU", "make"),
]
PLANNED = [("Twilio Inc.", "USA", "tw"), ("Twilio SendGrid", "USA", "sg")]
SP_PURPOSE = {
 "en": {"db": "Database, authentication and server functions", "web": "Website and dashboard hosting", "pay": "Payments and subscription billing",
        "ai": "AI processing of guest messages to draft replies", "wa": "Sending and receiving WhatsApp messages", "chx": "Availability, rate, booking and OTA message sync",
        "make": "Contact form and internal workflow automation", "tw": "WhatsApp numbers and messaging billing for hotels", "sg": "Transactional email"},
 "tr": {"db": "Veritabanı, kimlik doğrulama ve sunucu fonksiyonları", "web": "Web sitesi ve panel barındırma", "pay": "Ödemeler ve abonelik faturalandırması",
        "ai": "Cevap taslağı için misafir mesajlarının yapay zekâ ile işlenmesi", "wa": "WhatsApp mesajlarının gönderilmesi ve alınması", "chx": "Müsaitlik, fiyat, rezervasyon ve OTA mesaj senkronizasyonu",
        "make": "İletişim formu ve iç iş akışı otomasyonu", "tw": "Oteller için WhatsApp numarası ve mesaj faturalandırması", "sg": "İşlemsel e-posta"},
}

def _ul(items): return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"

def sp_table(L, planned=True):
    P = SP_PURPOSE.get(L) or SP_PURPOSE["en"]
    H = {"en": ("Subprocessor", "Location", "Purpose", "Planned — added to this list before they process any data"),
         "tr": ("Alt işleyici", "Konum", "Amaç", "Planlanan — veri işlemeye başlamadan önce bu listeye eklenecek")}
    import legal_v6_intl as _i
    H.update(_i.SP_HEAD); P = {**SP_PURPOSE["en"], **P} if L in SP_PURPOSE else {**SP_PURPOSE["en"], **_i.SP_PURPOSE.get(L, {})}
    h = H.get(L, H["en"])
    rows = "".join(f'<tr><th scope="row">{n}</th><td>{loc}</td><td>{P[k]}</td></tr>' for n, loc, k in SUBPROCESSORS)
    if planned:
        rows += "".join(f'<tr class="muted"><th scope="row">{n}*</th><td>{loc}</td><td>{P[k]}</td></tr>' for n, loc, k in PLANNED)
    note = f'<p class="small muted">* {h[3]}</p>' if planned else ""
    return f'<div class="table-wrap"><table><thead><tr><th>{h[0]}</th><th>{h[1]}</th><th>{h[2]}</th></tr></thead><tbody>{rows}</tbody></table></div>{note}'

# ------------------------------------------------------------------ privacy
def privacy_en(U, EMAIL, ADDR):
    R = RETENTION
    return f'''<p>This Privacy Policy explains how Hostlio Pro, operated by Loti Members LLC (“we”, “us”), collects, uses and shares personal data when you visit hostliopro.com, sign up, or use the Hostlio Pro dashboard, mobile app and guest-facing features.</p>
<h2>1. Our role</h2><p>For data about our customers (hotel owners and staff) and website visitors, we are the <strong>controller</strong>. For data about a hotel’s guests that we process to run the service for that hotel, the hotel is the controller and we act as its <strong>processor</strong> (a “service provider” under California law). That processing is governed by our <a href="{U("dpa")}">Data Processing Addendum</a>. Guests who want to exercise their rights should contact the hotel; we help the hotel respond.</p>
<h2>2. Data we collect</h2>
{_ul(["<strong>Account data:</strong> name, email, phone, hotel name, number of rooms, country, guest currency and time zone",
      "<strong>Billing data:</strong> plan, billing period and payment status. Card details are collected and stored by Stripe, never by us",
      "<strong>Hotel data:</strong> room types, rooms, rates, availability, reservations and settings",
      "<strong>Guest data processed for hotels:</strong> guest names, contact details, booking details and the content of guest messages received on WhatsApp and OTA inboxes",
      "<strong>Online check-in data:</strong> identity document details and images, date of birth, nationality, companions and a digital signature, when the hotel uses online check-in. We treat this as sensitive data",
      "<strong>Signup and security data:</strong> IP address, a hashed email and the outcome of signup attempts, used to prevent fraud and abuse",
      "<strong>Marketing source:</strong> the first campaign or page that brought you to our website (for example UTM parameters and the referring site), stored in your browser and sent with your signup",
      "<strong>Usage data:</strong> how the dashboard and app are used, and technical logs"])}
<h2>3. How we use data</h2>
{_ul(["To provide the service: syncing channels, showing reservations, sending guest messages and running online check-in",
      "To draft and send AI replies to guest messages on the hotel’s behalf",
      "To run your subscription: the free trial, automatic charges when the trial ends and at each renewal, invoices and plan limits such as the monthly AI message quota",
      "To keep the service secure and prevent fraud",
      "To measure which marketing channels bring customers",
      "To answer support requests and send service and billing emails",
      "To meet legal obligations"])}
<p>We do not sell personal data and we do not share it for cross-context behavioural advertising. Guest message content is not used for our marketing. Our AI provider processes message content only to generate replies and, under its commercial terms, does not use it to train its models.</p>
<h2>4. Legal bases (EEA, UK, Türkiye)</h2><p>We rely on performance of our contract with you, our legitimate interests (security, fraud prevention, improving the service, measuring marketing), compliance with legal obligations and, where required, your consent. For guest data, the hotel determines the legal basis.</p>
<h2>5. Who we share data with</h2><p>We use the subprocessors below. Each is bound by a contract that protects the data. When you connect a sales channel (such as Booking.com, Airbnb or Expedia), data is exchanged with that channel under its own terms.</p>
{sp_table("en")}
<p>We may also disclose data when required by law or to protect our rights.</p>
<h2>6. International transfers</h2><p>We are based in the United States and some subprocessors process data outside the EEA, the UK and Türkiye. Where required, transfers are protected by the European Commission’s Standard Contractual Clauses, the UK Addendum or other lawful transfer mechanisms.</p>
<h2>7. How long we keep data</h2>
{_ul([f"Guest message content is anonymised after the retention period the hotel sets in its settings (default: {R['msg_default_days']} days)",
      f"Guest contact details are kept for {R['guest_contact_days']} days after departure, unless the hotel deletes them sooner",
      "Online check-in data is kept only as long as the hotel needs it to meet its guest-registration duties, and is deleted with the hotel’s account at the latest",
      f"Account and hotel data are kept while the account is active and deleted within {R['deletion_days']} days of a verified deletion request",
      "Billing records are kept for as long as tax and accounting law requires",
      "Signup and security logs are kept for a limited period for fraud prevention"])}
<h2>8. Security</h2><p>Data is encrypted in transit (TLS) and at rest. Access is restricted by role and by hotel. Our database provider is SOC 2 Type 2 audited and card payments are handled by Stripe, a PCI DSS Level 1 service provider. More on our <a href="{U("security")}">Security and data</a> page.</p>
<h2>9. Your rights</h2>
<p><strong>EEA and UK:</strong> you can request access, correction, deletion, restriction, portability, and object to processing. You may also complain to your local data protection authority.</p>
<p><strong>California (CCPA/CPRA):</strong> you can ask to know, delete and correct your personal information. We do not sell or share personal information, and we will not discriminate against you for exercising your rights.</p>
<p><strong>Türkiye (KVKK):</strong> under Article 11 of Law No. 6698 you can learn whether your data is processed, request information, correction or deletion, and object to results arising from automated processing.</p>
<p>To exercise any right, email <a href="mailto:{EMAIL}">{EMAIL}</a>. To close your account, see <a href="{U("delacc")}">Delete your account</a>.</p>
<h2>10. Cookies and browser storage</h2><p>The dashboard uses essential cookies and storage to keep you signed in. Our website stores your language choice and the first marketing source in your browser’s local storage. We do not use advertising cookies. If we add website analytics, we will update this policy first.</p>
<h2>11. WhatsApp and guest messaging</h2><p>Hostlio Pro connects to the WhatsApp Business Platform and to OTA inboxes to send and receive guest messages for hotels. Guest phone numbers are used only to communicate about the stay. Guests can stop receiving messages by telling the hotel.</p>
<h2>12. Children</h2><p>Hostlio Pro is a business service and is not directed to children under 16.</p>
<h2>13. Changes</h2><p>We will post changes on this page and update the date above. For material changes we will also notify customers by email or in the dashboard.</p>
<h2>14. Contact</h2>{_ul([f'Email: <a href="mailto:{EMAIL}">{EMAIL}</a>', f"Address: {ADDR}"])}'''

def privacy_tr(U, EMAIL, ADDR):
    R = RETENTION
    return f'''<p>Bu Gizlilik Politikası, Loti Members LLC (“biz”) tarafından işletilen Hostlio Pro’nun; hostliopro.com’u ziyaret ettiğinizde, kaydolduğunuzda ya da Hostlio Pro paneli, mobil uygulaması ve misafire dönük özelliklerini kullandığınızda kişisel verileri nasıl topladığını, kullandığını ve paylaştığını açıklar.</p>
<h2>1. Rolümüz</h2><p>Müşterilerimize (otel sahipleri ve çalışanları) ve site ziyaretçilerine ait veriler için <strong>veri sorumlusu</strong> biziz. Bir otel adına hizmeti yürütmek için işlediğimiz misafir verilerinde veri sorumlusu oteldir; biz <strong>veri işleyen</strong> konumundayız. Bu işleme <a href="{U("dpa")}">Veri İşleme Sözleşmemize (DPA)</a> tabidir. Haklarını kullanmak isteyen misafirler otele başvurmalıdır; otelin yanıt vermesine yardımcı oluruz.</p>
<h2>2. Topladığımız veriler</h2>
{_ul(["<strong>Hesap verileri:</strong> ad, e-posta, telefon, otel adı, oda sayısı, ülke, misafir para birimi ve saat dilimi",
      "<strong>Fatura verileri:</strong> plan, fatura dönemi ve ödeme durumu. Kart bilgileri bizde değil, Stripe’ta toplanır ve saklanır",
      "<strong>Otel verileri:</strong> oda tipleri, odalar, fiyatlar, müsaitlik, rezervasyonlar ve ayarlar",
      "<strong>Oteller adına işlenen misafir verileri:</strong> misafir adı, iletişim bilgileri, rezervasyon bilgileri ve WhatsApp ile OTA gelen kutularına gelen mesajların içeriği",
      "<strong>Online check-in verileri:</strong> otel online check-in kullanıyorsa kimlik belgesi bilgileri ve görseli, doğum tarihi, uyruk, refakatçiler ve dijital imza. Bu verileri hassas veri olarak ele alırız",
      "<strong>Kayıt ve güvenlik verileri:</strong> IP adresi, e-postanın özetlenmiş (hash) hali ve kayıt denemelerinin sonucu; dolandırıcılık ve kötüye kullanımı önlemek için",
      "<strong>Pazarlama kaynağı:</strong> sizi sitemize ilk getiren kampanya ya da sayfa (ör. UTM parametreleri ve yönlendiren site); tarayıcınızda saklanır ve kaydınızla birlikte gönderilir",
      "<strong>Kullanım verileri:</strong> panel ve uygulamanın nasıl kullanıldığı ve teknik kayıtlar"])}
<h2>3. Verileri nasıl kullanırız</h2>
{_ul(["Hizmeti sunmak için: kanalları senkronize etmek, rezervasyonları göstermek, misafir mesajlarını göndermek ve online check-in’i yürütmek",
      "Otel adına misafir mesajlarına yapay zekâ ile cevap taslağı hazırlamak ve göndermek",
      "Aboneliğinizi yürütmek için: ücretsiz deneme, deneme bitiminde ve her yenilemede otomatik ücretlendirme, faturalar ve aylık AI mesaj kotası gibi plan limitleri",
      "Hizmeti güvende tutmak ve dolandırıcılığı önlemek",
      "Hangi pazarlama kanallarının müşteri getirdiğini ölçmek",
      "Destek taleplerini yanıtlamak, hizmet ve fatura e-postaları göndermek",
      "Yasal yükümlülükleri yerine getirmek"])}
<p>Kişisel verileri satmayız ve davranışsal reklam için paylaşmayız. Misafir mesajları pazarlamamızda kullanılmaz. Yapay zekâ sağlayıcımız mesaj içeriğini yalnızca cevap üretmek için işler ve ticari şartları gereği modellerini eğitmekte kullanmaz.</p>
<h2>4. Hukuki sebepler (AEA, Birleşik Krallık, Türkiye)</h2><p>Sizinle yaptığımız sözleşmenin ifası, meşru menfaatlerimiz (güvenlik, dolandırıcılığın önlenmesi, hizmetin geliştirilmesi, pazarlamanın ölçülmesi), yasal yükümlülükler ve gerektiğinde açık rızanıza dayanırız. Misafir verilerinde hukuki sebebi otel belirler.</p>
<h2>5. Verileri kimlerle paylaşırız</h2><p>Aşağıdaki alt işleyicileri kullanırız; her biri verileri koruyan bir sözleşmeyle bağlıdır. Bir satış kanalı (Booking.com, Airbnb, Expedia gibi) bağladığınızda veriler o kanalla kendi şartları çerçevesinde paylaşılır.</p>
{sp_table("tr")}
<p>Kanunen gerektiğinde veya haklarımızı korumak için de veri açıklayabiliriz.</p>
<h2>6. Yurt dışına aktarım</h2><p>Şirketimiz ABD’dedir ve bazı alt işleyiciler verileri AEA, Birleşik Krallık ve Türkiye dışında işler. Gerektiğinde aktarımlar Avrupa Komisyonu Standart Sözleşme Maddeleri, Birleşik Krallık eki veya KVKK’ya uygun diğer aktarım araçlarıyla korunur.</p>
<h2>7. Saklama süreleri</h2>
{_ul([f"Misafir mesaj içerikleri, otelin ayarlarında belirlediği sürenin sonunda anonimleştirilir (varsayılan: {R['msg_default_days']} gün)",
      f"Misafir iletişim bilgileri, otel daha önce silmezse ayrılıştan sonra {R['guest_contact_days']} gün saklanır",
      "Online check-in verileri yalnızca otelin misafir kayıt yükümlülükleri için gerektiği kadar saklanır; en geç otelin hesabıyla birlikte silinir",
      f"Hesap ve otel verileri hesap aktif olduğu sürece saklanır; doğrulanmış silme talebinden sonra {R['deletion_days']} gün içinde silinir",
      "Fatura kayıtları vergi ve muhasebe mevzuatının gerektirdiği süre boyunca saklanır",
      "Kayıt ve güvenlik kayıtları dolandırıcılığı önlemek için sınırlı bir süre saklanır"])}
<h2>8. Güvenlik</h2><p>Veriler aktarım sırasında (TLS) ve depolamada şifrelenir. Erişim role ve otele göre sınırlandırılır. Veritabanı sağlayıcımız SOC 2 Type 2 denetimlidir; kart ödemeleri PCI DSS Level 1 hizmet sağlayıcısı Stripe tarafından işlenir. Ayrıntılar <a href="{U("security")}">Güvenlik ve veri</a> sayfasında.</p>
<h2>9. Haklarınız</h2>
<p><strong>Türkiye (KVKK):</strong> 6698 sayılı Kanun’un 11. maddesi uyarınca verilerinizin işlenip işlenmediğini öğrenme, bilgi talep etme, düzeltme veya silme isteme ve otomatik işleme sonucu aleyhinize bir sonuca itiraz etme haklarınız vardır.</p>
<p><strong>AEA ve Birleşik Krallık:</strong> erişim, düzeltme, silme, kısıtlama ve taşınabilirlik talep edebilir, işlemeye itiraz edebilirsiniz. Yerel veri koruma otoritesine şikâyette de bulunabilirsiniz.</p>
<p><strong>Kaliforniya (CCPA/CPRA):</strong> kişisel bilgilerinizi öğrenme, sildirme ve düzeltme talebinde bulunabilirsiniz. Kişisel bilgi satmayız veya paylaşmayız; haklarınızı kullandığınız için size farklı davranmayız.</p>
<p>Haklarınızı kullanmak için <a href="mailto:{EMAIL}">{EMAIL}</a> adresine yazın. Hesabınızı kapatmak için <a href="{U("delacc")}">hesap silme</a> sayfasına bakın.</p>
<h2>10. Çerezler ve tarayıcı depolaması</h2><p>Panel, oturumunuzu açık tutmak için zorunlu çerez ve depolama kullanır. Sitemiz dil tercihinizi ve ilk pazarlama kaynağını tarayıcınızın yerel depolamasında (localStorage) tutar. Reklam çerezi kullanmayız. Site analitiği eklersek önce bu politikayı güncelleriz.</p>
<h2>11. WhatsApp ve misafir mesajlaşması</h2><p>Hostlio Pro, oteller adına misafir mesajlarını göndermek ve almak için WhatsApp Business Platformu’na ve OTA gelen kutularına bağlanır. Misafir telefon numaraları yalnızca konaklamayla ilgili iletişim için kullanılır. Misafirler otele bildirerek mesaj almayı durdurabilir.</p>
<h2>12. Çocuklar</h2><p>Hostlio Pro bir işletme hizmetidir ve 16 yaşından küçüklere yönelik değildir.</p>
<h2>13. Değişiklikler</h2><p>Değişiklikleri bu sayfada yayınlar ve yukarıdaki tarihi güncelleriz. Önemli değişiklikleri ayrıca e-posta veya panel üzerinden bildiririz.</p>
<h2>14. İletişim</h2>{_ul([f'E-posta: <a href="mailto:{EMAIL}">{EMAIL}</a>', f"Adres: {ADDR}"])}'''

# ------------------------------------------------------------------ terms
def terms_en(U, EMAIL, ADDR):
    Q = QUOTA
    return f'''<p>These Terms of Service (“Terms”) govern your use of Hostlio Pro, operated by Loti Members LLC (“we”, “us”). By creating an account or using the service you agree to these Terms. If you use Hostlio Pro for a business, you accept them on its behalf.</p>
<h2>1. The service</h2><p>Hostlio Pro is cloud software for hotels: AI guest messaging (Lio), a channel manager, a reservation calendar, online check-in and related tools, available by subscription through the website, the dashboard and the mobile app.</p>
<h2>2. Your account</h2><p>You must give accurate information and keep your login details secure. You are responsible for everything done under your account, including by your staff.</p>
<h2>3. Free trial, payment and automatic renewal</h2>
{_ul(["Every plan starts with a 7-day free trial. A payment card is collected at signup through Stripe",
      "<strong>Unless you cancel before the trial ends, your card is charged automatically for the plan and billing period you chose when the trial ends</strong>",
      "Subscriptions are paid in advance and <strong>renew automatically</strong> at the end of each monthly or annual period until cancelled. We charge the card on file at each renewal",
      f'Prices are in US dollars and exclude taxes. Current plans and prices are on our <a href="{U("pricing")}">pricing page</a>. Annual billing costs 20% less than paying monthly',
      "<strong>Early-bird price:</strong> the first 50 customers keep their early-bird price for as long as their subscription stays active without interruption. If the subscription is cancelled or lapses, the early-bird price ends and current prices apply to any new subscription",
      "We may change prices for future periods with at least 30 days’ notice by email; the new price applies from your next renewal"])}
<h2>4. Plan limits and AI message quota</h2><p>Each plan includes a monthly quota of AI messages (Starter {Q["starter"]}, Pro {Q["pro"]}, Growth {Q["growth"]}) and a maximum number of properties and rooms. We notify you when you reach 80% of the quota. <strong>Automatic AI replies pause once usage passes 110% of the monthly quota</strong> and resume at the start of the next period or when you upgrade. Guest messages keep arriving in your inbox so you can reply yourself.</p>
<h2>5. Cancellation and refunds</h2><p>You can cancel at any time from the billing page of the dashboard or by emailing {EMAIL}. Cancelling during the trial means you are not charged. Otherwise cancellation takes effect at the end of the current paid period and the service stays available until then. We do not refund partial periods, except where the law requires it.</p>
<h2>6. Acceptable use</h2><p>You agree not to:</p>
{_ul(["use the service for anything unlawful, or to send spam or unsolicited messages to guests",
      "break the terms of OTAs, Meta/WhatsApp or other connected platforms through our integrations",
      "try to gain unauthorised access to our systems or other customers’ data",
      "resell or sublicense the service without our written permission"])}
<h2>7. Guest data and your responsibilities</h2><p>You are the controller of your guests’ personal data. You are responsible for having a lawful basis to process it, informing guests (for example in your own privacy notice) and meeting guest-registration and identity-document rules that apply to your property. Our <a href="{U("dpa")}">Data Processing Addendum</a> forms part of these Terms and applies to the guest data we process for you.</p>
<h2>8. AI-generated replies</h2><p>Lio drafts and sends replies using the information you provide. AI can make mistakes. You decide which messages Lio may answer automatically and which need approval, and you remain responsible for the replies sent on behalf of your property. Lio hands over messages it is not sure about, but you should not rely on it for legal, medical or emergency matters. To the extent permitted by law, we are not liable for the content of AI-generated replies.</p>
<h2>9. Connected channels and WhatsApp</h2><p>Channel connections are provided through our connectivity partner Channex, and messaging through the WhatsApp Business Platform and OTA inboxes. You must follow the terms of each platform you connect. Changes to third-party APIs or policies can affect features, and we are not responsible for them.</p>
<h2>10. Your data</h2><p>You own your data. We process it only to provide the service, as described in our <a href="{U("privacy")}">Privacy Policy</a> and the DPA. You can export your data while your account is active.</p>
<h2>11. Availability</h2><p>We aim for high availability but do not guarantee uninterrupted service. We announce planned maintenance in advance where possible.</p>
<h2>12. Intellectual property</h2><p>Hostlio Pro, its software and content belong to Loti Members LLC. You may not copy, modify or distribute any part of the service without written permission.</p>
<h2>13. Limitation of liability</h2><p>To the maximum extent permitted by law, we are not liable for indirect, incidental, special or consequential damages, or for lost profits or data. Our total liability for any claim is limited to the fees you paid us in the 12 months before the claim.</p>
<h2>14. Governing law</h2><p>These Terms are governed by the laws of the State of California, USA. Disputes will be resolved in the courts of Sacramento County, California, unless mandatory consumer or local law gives you other rights.</p>
<h2>15. Changes to these Terms</h2><p>We will notify you of material changes by email or in the dashboard at least 30 days before they apply. Continuing to use the service after that date means you accept the updated Terms.</p>
<h2>16. Contact</h2>{_ul([f'Email: <a href="mailto:{EMAIL}">{EMAIL}</a>', f"Address: {ADDR}"])}'''

def terms_tr(U, EMAIL, ADDR):
    Q = {k: v.replace(",", ".") for k, v in QUOTA.items()}
    return f'''<p>Bu Kullanım Şartları (“Şartlar”), Loti Members LLC (“biz”) tarafından işletilen Hostlio Pro’yu kullanımınızı düzenler. Hesap oluşturarak veya hizmeti kullanarak bu Şartları kabul edersiniz. Hostlio Pro’yu bir işletme adına kullanıyorsanız Şartları o işletme adına kabul etmiş olursunuz.</p>
<h2>1. Hizmet</h2><p>Hostlio Pro oteller için bulut yazılımıdır: yapay zekâ ile misafir mesajlaşması (Lio), kanal yöneticisi, rezervasyon takvimi, online check-in ve ilgili araçlar; web sitesi, panel ve mobil uygulama üzerinden abonelikle sunulur.</p>
<h2>2. Hesabınız</h2><p>Doğru bilgi vermeli ve giriş bilgilerinizi güvende tutmalısınız. Çalışanlarınız dahil, hesabınız altında yapılan her işlemden siz sorumlusunuz.</p>
<h2>3. Ücretsiz deneme, ödeme ve otomatik yenileme</h2>
{_ul(["Her plan 7 günlük ücretsiz denemeyle başlar. Kayıt sırasında Stripe üzerinden bir ödeme kartı alınır",
      "<strong>Deneme bitmeden iptal etmezseniz, deneme sonunda seçtiğiniz plan ve fatura dönemi için kartınızdan otomatik olarak ücret alınır</strong>",
      "Abonelikler peşin ödenir ve iptal edilene kadar her aylık veya yıllık dönemin sonunda <strong>otomatik olarak yenilenir</strong>. Her yenilemede kayıtlı karttan ücret alınır",
      f'Fiyatlar ABD doları cinsindendir, vergiler hariçtir. Güncel planlar ve fiyatlar <a href="{U("pricing")}">fiyatlandırma sayfamızda</a>. Yıllık ödeme, aylık ödemeye göre %20 daha ucuzdur',
      "<strong>Erken kayıt (Early Bird) fiyatı:</strong> ilk 50 müşteri, aboneliği kesintisiz devam ettiği sürece erken kayıt fiyatını korur. Abonelik iptal edilir veya süresi dolarsa erken kayıt fiyatı sona erer; yeni abonelikte güncel fiyatlar geçerlidir",
      "Gelecek dönemlerin fiyatlarını en az 30 gün önceden e-postayla bildirerek değiştirebiliriz; yeni fiyat bir sonraki yenilemeden itibaren uygulanır"])}
<h2>4. Plan limitleri ve AI mesaj kotası</h2><p>Her plan aylık bir AI mesaj kotası (Starter {Q["starter"]}, Pro {Q["pro"]}, Growth {Q["growth"]}) ve azami tesis ve oda sayısı içerir. Kotanın %80’ine ulaştığınızda sizi bilgilendiririz. <strong>Kullanım aylık kotanın %110’unu geçtiğinde otomatik AI cevapları durur</strong>; bir sonraki dönemin başında veya planınızı yükselttiğinizde yeniden başlar. Misafir mesajları gelen kutunuza gelmeye devam eder, kendiniz cevaplayabilirsiniz.</p>
<h2>5. İptal ve iade</h2><p>İstediğiniz zaman panelin faturalandırma sayfasından veya {EMAIL} adresine yazarak iptal edebilirsiniz. Deneme sırasında iptal ederseniz ücret alınmaz. Aksi halde iptal, ödenmiş dönemin sonunda geçerli olur ve hizmet o güne kadar açık kalır. Kanunun zorunlu kıldığı haller dışında kısmi dönem iadesi yapılmaz.</p>
<h2>6. Kabul edilebilir kullanım</h2><p>Şunları yapmamayı kabul edersiniz:</p>
{_ul(["hizmeti hukuka aykırı amaçlarla kullanmak, misafirlere spam veya istenmeyen mesaj göndermek",
      "entegrasyonlarımız üzerinden OTA’ların, Meta/WhatsApp’ın veya bağlı diğer platformların şartlarını ihlal etmek",
      "sistemlerimize veya diğer müşterilerin verilerine yetkisiz erişmeye çalışmak",
      "hizmeti yazılı iznimiz olmadan yeniden satmak veya alt lisanslamak"])}
<h2>7. Misafir verileri ve sorumluluklarınız</h2><p>Misafirlerinizin kişisel verilerinin veri sorumlusu sizsiniz. Bu verileri işlemek için hukuki sebebe sahip olmak, misafirleri bilgilendirmek (ör. kendi aydınlatma metninizle) ve tesisiniz için geçerli misafir kayıt ve kimlik belgesi kurallarına uymak sizin sorumluluğunuzdadır. <a href="{U("dpa")}">Veri İşleme Sözleşmemiz (DPA)</a> bu Şartların parçasıdır ve sizin adınıza işlediğimiz misafir verilerine uygulanır.</p>
<h2>8. Yapay zekâ cevapları</h2><p>Lio, verdiğiniz bilgileri kullanarak cevap hazırlar ve gönderir. Yapay zekâ hata yapabilir. Lio’nun hangi mesajlara otomatik cevap vereceğine, hangilerinin onay gerektireceğine siz karar verirsiniz ve tesisiniz adına gönderilen cevaplardan siz sorumlu olursunuz. Lio emin olmadığı mesajları size devreder; yine de hukuki, tıbbi veya acil konularda ona güvenmemelisiniz. Kanunun izin verdiği ölçüde yapay zekâ cevaplarının içeriğinden sorumlu değiliz.</p>
<h2>9. Bağlı kanallar ve WhatsApp</h2><p>Kanal bağlantıları bağlantı ortağımız Channex üzerinden; mesajlaşma ise WhatsApp Business Platformu ve OTA gelen kutuları üzerinden sağlanır. Bağladığınız her platformun şartlarına uymalısınız. Üçüncü taraf API veya politikalarındaki değişiklikler özellikleri etkileyebilir; bunlardan sorumlu değiliz.</p>
<h2>10. Verileriniz</h2><p>Verileriniz size aittir. Onları yalnızca hizmeti sunmak için, <a href="{U("privacy")}">Gizlilik Politikamız</a> ve DPA’da anlatıldığı şekilde işleriz. Hesabınız açıkken verilerinizi dışa aktarabilirsiniz.</p>
<h2>11. Hizmet sürekliliği</h2><p>Yüksek erişilebilirlik hedefleriz ancak kesintisiz hizmet garanti etmeyiz. Planlı bakımları mümkün olduğunca önceden duyururuz.</p>
<h2>12. Fikri mülkiyet</h2><p>Hostlio Pro, yazılımı ve içerikleri Loti Members LLC’ye aittir. Hizmetin herhangi bir bölümünü yazılı izin olmadan kopyalayamaz, değiştiremez veya dağıtamazsınız.</p>
<h2>13. Sorumluluğun sınırlandırılması</h2><p>Kanunun izin verdiği azami ölçüde dolaylı, arızi, özel veya sonuçsal zararlardan, kâr veya veri kaybından sorumlu değiliz. Herhangi bir talep için toplam sorumluluğumuz, talepten önceki 12 ayda bize ödediğiniz ücretlerle sınırlıdır.</p>
<h2>14. Uygulanacak hukuk</h2><p>Bu Şartlar ABD’nin Kaliforniya Eyaleti hukukuna tabidir. Emredici tüketici veya yerel mevzuat size başka haklar tanımadıkça uyuşmazlıklar Kaliforniya, Sacramento County mahkemelerinde çözülür.</p>
<h2>15. Şartlardaki değişiklikler</h2><p>Önemli değişiklikleri yürürlüğe girmeden en az 30 gün önce e-posta veya panel üzerinden bildiririz. O tarihten sonra hizmeti kullanmaya devam etmeniz güncel Şartları kabul ettiğiniz anlamına gelir.</p>
<h2>16. İletişim</h2>{_ul([f'E-posta: <a href="mailto:{EMAIL}">{EMAIL}</a>', f"Adres: {ADDR}"])}'''
