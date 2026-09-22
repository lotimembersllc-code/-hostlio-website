"""Privacy Policy & Terms of Service (from hostliopro.com, April 20, 2026 text) + legacy EN blog posts."""
import json
from pathlib import Path
from build import url, EMAIL, LANGMOD

ADDR = "Loti Members LLC, 2108 N ST STE N, Sacramento, CA 95816"
# K5 (Eylül 2026): metinler legal_v6.py / legal_v6_intl.py'de güncellendi (eski 20 Nisan 2026 metni bu dosyanın git geçmişinde)
import legal_v6 as _v6, legal_v6_intl as _v6i
LEGAL_DATE = {**_v6.LEGAL_DATE, "iso": _v6.LEGAL_ISO}
def _U(L): return lambda k: url(k, "en" if k == "dpa" else L)

def _ul(items): return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"

def privacy_body(L):
    if L in ("en", "tr"): return (_v6.privacy_en if L == "en" else _v6.privacy_tr)(_U(L), EMAIL, ADDR)
    return _v6i.privacy(L, _U(L), EMAIL, ADDR, _v6.sp_table, _v6.RETENTION)

def privacy_body_v5(L):
    if L in LANGMOD: return LANGMOD[L].privacy_body(lambda k: url(k, L), EMAIL, ADDR, _ul)
    if L == "en":
        return f'''<p>This Privacy Policy describes how Hostlio Pro, operated by Loti Members LLC ("we", "us", or "our"), collects, uses, and shares information when you use our hotel management platform at hostliopro.com.</p>
<h2>1. Information We Collect</h2><p>We collect information you provide directly to us, including:</p>
{_ul(["Account information: name, email address, phone number, hotel name, number of rooms","Payment information: processed securely through Stripe (we do not store card details)","Hotel data: reservations, guest communications, room configurations","Usage data: how you interact with our platform"])}
<h2>2. How We Use Your Information</h2><p>We use the information we collect to:</p>
{_ul(["Provide, maintain, and improve our services","Process payments and send billing notifications","Send transactional emails and product updates","Respond to your comments and questions","Monitor and analyze usage patterns to improve user experience","Comply with legal obligations"])}
<h2>3. Information Sharing</h2><p>We do not sell, trade, or rent your personal information to third parties. We may share your information with:</p>
{_ul(["<strong>Service providers:</strong> Supabase (database), Make.com (automation), Stripe (payments), Vercel (hosting), Anthropic (AI processing)","<strong>Channel managers:</strong> Channex API for OTA synchronization (Booking.com, Airbnb, etc.)","<strong>Legal requirements:</strong> When required by law or to protect our rights"])}
<h2>4. Data Security</h2><p>We implement appropriate technical and organizational measures to protect your personal information against unauthorized access, alteration, disclosure, or destruction. Our infrastructure is SOC 2 compliant through Supabase, and payments are PCI DSS compliant through Stripe.</p>
<h2>5. Data Retention</h2><p>We retain your personal information for as long as your account is active or as needed to provide services. You may request deletion of your data at any time by contacting us at {EMAIL}.</p>
<h2>6. GDPR Rights</h2><p>If you are located in the European Economic Area, you have the right to access, correct, or delete your personal data. You also have the right to data portability and to object to processing. To exercise these rights, contact us at {EMAIL}.</p>
<h2>7. WhatsApp &amp; Messaging</h2><p>Our platform integrates with WhatsApp Business API to facilitate guest communications. Message content is processed to generate AI responses and is not used for marketing purposes. Guest phone numbers are stored only for communication purposes.</p>
<h2>8. Cookies</h2><p>We use essential cookies to maintain your session and preferences. We do not use tracking or advertising cookies. You can control cookies through your browser settings.</p>
<h2>9. Third-Party Links</h2><p>Our platform may contain links to third-party websites. We are not responsible for the privacy practices of those sites and encourage you to review their privacy policies.</p>
<h2>10. Changes to This Policy</h2><p>We may update this Privacy Policy from time to time. We will notify you of any changes by posting the new policy on this page and updating the "Last updated" date.</p>
<h2>11. Contact Us</h2><p>If you have any questions about this Privacy Policy, please contact us:</p>
{_ul([f'Email: <a href="mailto:{EMAIL}">{EMAIL}</a>', f"Address: {ADDR}"])}
<p>To delete your account, see <a href="{url("delacc", L)}">Delete your account</a>.</p>'''
    return f'''<p>Bu Gizlilik Politikası, Loti Members LLC ("biz") tarafından işletilen Hostlio Pro'nun, hostliopro.com adresindeki otel yönetim platformumuzu kullandığınızda bilgileri nasıl topladığını, kullandığını ve paylaştığını açıklar.</p>
<h2>1. Topladığımız bilgiler</h2><p>Doğrudan bize verdiğiniz bilgileri toplarız:</p>
{_ul(["Hesap bilgileri: ad, e-posta adresi, telefon numarası, otel adı, oda sayısı","Ödeme bilgileri: Stripe üzerinden güvenle işlenir (kart bilgilerini saklamayız)","Otel verileri: rezervasyonlar, misafir yazışmaları, oda yapılandırmaları","Kullanım verileri: platformumuzla nasıl etkileşim kurduğunuz"])}
<h2>2. Bilgilerinizi nasıl kullanırız</h2><p>Topladığımız bilgileri şu amaçlarla kullanırız:</p>
{_ul(["Hizmetlerimizi sunmak, sürdürmek ve geliştirmek","Ödemeleri işlemek ve fatura bildirimleri göndermek","İşlemsel e-postalar ve ürün güncellemeleri göndermek","Yorum ve sorularınızı yanıtlamak","Kullanıcı deneyimini iyileştirmek için kullanım eğilimlerini izlemek ve analiz etmek","Yasal yükümlülüklere uymak"])}
<h2>3. Bilgi paylaşımı</h2><p>Kişisel bilgilerinizi üçüncü taraflara satmaz, takas etmez veya kiralamayız. Bilgilerinizi şu taraflarla paylaşabiliriz:</p>
{_ul(["<strong>Hizmet sağlayıcılar:</strong> Supabase (veritabanı), Make.com (otomasyon), Stripe (ödemeler), Vercel (barındırma), Anthropic (yapay zekâ işleme)","<strong>Kanal yöneticileri:</strong> OTA senkronizasyonu için Channex API (Booking.com, Airbnb vb.)","<strong>Yasal gereklilikler:</strong> Kanunen gerektiğinde veya haklarımızı korumak için"])}
<h2>4. Veri güvenliği</h2><p>Kişisel bilgilerinizi yetkisiz erişim, değişiklik, ifşa veya imhaya karşı korumak için uygun teknik ve idari önlemler uygularız. Altyapımız Supabase aracılığıyla SOC 2 uyumludur; ödemeler Stripe aracılığıyla PCI DSS uyumludur.</p>
<h2>5. Veri saklama</h2><p>Kişisel bilgilerinizi hesabınız aktif olduğu sürece veya hizmet sunmak için gerektiği kadar saklarız. Verilerinizin silinmesini istediğiniz zaman {EMAIL} adresinden talep edebilirsiniz.</p>
<h2>6. GDPR hakları</h2><p>Avrupa Ekonomik Alanı'nda bulunuyorsanız kişisel verilerinize erişme, bunları düzeltme veya sildirme hakkına sahipsiniz. Ayrıca veri taşınabilirliği ve işlemeye itiraz haklarınız vardır. Bu hakları kullanmak için {EMAIL} adresinden bize ulaşın.</p>
<h2>7. WhatsApp ve mesajlaşma</h2><p>Platformumuz, misafir iletişimini kolaylaştırmak için WhatsApp Business API ile entegredir. Mesaj içerikleri yapay zekâ yanıtları üretmek için işlenir ve pazarlama amacıyla kullanılmaz. Misafir telefon numaraları yalnızca iletişim amacıyla saklanır.</p>
<h2>8. Çerezler</h2><p>Oturumunuzu ve tercihlerinizi sürdürmek için yalnızca zorunlu çerezler kullanırız. Takip veya reklam çerezi kullanmayız. Çerezleri tarayıcı ayarlarınızdan yönetebilirsiniz.</p>
<h2>9. Üçüncü taraf bağlantıları</h2><p>Platformumuz üçüncü taraf web sitelerine bağlantılar içerebilir. Bu sitelerin gizlilik uygulamalarından sorumlu değiliz; gizlilik politikalarını incelemenizi öneririz.</p>
<h2>10. Bu politikadaki değişiklikler</h2><p>Bu Gizlilik Politikası'nı zaman zaman güncelleyebiliriz. Değişiklikleri yeni politikayı bu sayfada yayınlayarak ve "Son güncelleme" tarihini değiştirerek bildiririz.</p>
<h2>11. İletişim</h2><p>Bu Gizlilik Politikası hakkında sorularınız için:</p>
{_ul([f'E-posta: <a href="mailto:{EMAIL}">{EMAIL}</a>', f"Adres: {ADDR}"])}
<p>Hesabınızı silmek için <a href="{url("delacc", L)}">hesap silme</a> sayfasına bakın.</p>'''

def terms_body(L):
    if L in ("en", "tr"): return (_v6.terms_en if L == "en" else _v6.terms_tr)(_U(L), EMAIL, ADDR)
    return _v6i.terms(L, _U(L), EMAIL, ADDR, _v6.QUOTA)

def terms_body_v5(L):
    if L in LANGMOD: return LANGMOD[L].terms_body(lambda k: url(k, L), EMAIL, ADDR, _ul)
    pricing = url("pricing", L)
    if L == "en":
        return f'''<p>These Terms of Service ("Terms") govern your use of Hostlio Pro, operated by Loti Members LLC ("Company", "we", "us", or "our"). By accessing or using our service, you agree to be bound by these Terms.</p>
<h2>1. Description of Service</h2><p>Hostlio Pro is a cloud-based hotel management platform that provides AI-powered guest communication, channel management, room rack calendar, and related hospitality management tools. The service is available via subscription at hostliopro.com.</p>
<h2>2. Account Registration</h2><p>To use Hostlio Pro, you must create an account and provide accurate, complete information. You are responsible for maintaining the confidentiality of your account credentials and for all activities that occur under your account.</p>
<h2>3. Subscription &amp; Payments</h2>
{_ul(["Subscriptions are billed monthly or annually in advance","All payments are processed securely through Stripe","7-day free trial available — a payment method is collected at signup, but no charge is made until the trial ends","After the trial, you will be charged based on your selected plan",f'Prices are in USD. Current plans and rates are listed on our <a href="{pricing}">pricing page</a>',"Annual plans offer a 20% discount"])}
<h2>4. Cancellation &amp; Refunds</h2><p>You may cancel your subscription at any time. Cancellation takes effect at the end of the current billing period. We do not offer refunds for partial billing periods. To cancel, contact us at {EMAIL}.</p>
<h2>5. Acceptable Use</h2><p>You agree not to:</p>
{_ul(["Use the service for any unlawful purpose","Violate OTA platform terms (Booking.com, Airbnb, etc.) through our integrations","Attempt to gain unauthorized access to our systems","Send spam or unsolicited messages to guests","Resell or sublicense the service without written permission"])}
<h2>6. AI-Generated Content</h2><p>Hostlio Pro uses artificial intelligence to generate responses to guest messages. You acknowledge that AI-generated content may occasionally contain errors. You are responsible for reviewing and managing AI responses sent on behalf of your property. We are not liable for any inaccuracies in AI-generated communications.</p>
<h2>7. OTA Channel Integrations</h2><p>Our platform integrates with third-party OTA channels (Booking.com, Airbnb, Expedia, etc.) via Channex API. You are responsible for complying with each platform's terms of service. We are not responsible for changes in OTA APIs or policies that may affect functionality.</p>
<h2>8. Data &amp; Privacy</h2><p>Your use of Hostlio Pro is also governed by our <a href="{url("privacy", L)}">Privacy Policy</a>, which is incorporated into these Terms by reference. You retain ownership of your data. We process your data solely to provide the service.</p>
<h2>9. Service Availability</h2><p>We strive for 99.9% uptime but do not guarantee uninterrupted service. We may perform scheduled maintenance with advance notice. We are not liable for losses resulting from service interruptions.</p>
<h2>10. Intellectual Property</h2><p>Hostlio Pro and all related software, designs, and content are the property of Loti Members LLC. You may not copy, modify, or distribute any part of our service without written permission.</p>
<h2>11. Limitation of Liability</h2><p>To the maximum extent permitted by law, Loti Members LLC shall not be liable for any indirect, incidental, special, consequential, or punitive damages, including loss of profits or data, arising from your use of the service.</p>
<h2>12. Governing Law</h2><p>These Terms are governed by the laws of the State of California, USA. Any disputes shall be resolved in the courts of Sacramento County, California.</p>
<h2>13. Changes to Terms</h2><p>We may update these Terms from time to time. We will notify you of significant changes via email or through the platform. Continued use of the service after changes constitutes acceptance of the new Terms.</p>
<h2>14. Contact</h2><p>For questions about these Terms, contact us:</p>
{_ul([f'Email: <a href="mailto:{EMAIL}">{EMAIL}</a>', f"Address: {ADDR}"])}'''
    return f'''<p>Bu Kullanım Şartları ("Şartlar"), Loti Members LLC ("Şirket", "biz") tarafından işletilen Hostlio Pro'yu kullanımınızı düzenler. Hizmetimize erişerek veya hizmetimizi kullanarak bu Şartlara bağlı kalmayı kabul edersiniz.</p>
<h2>1. Hizmetin tanımı</h2><p>Hostlio Pro; yapay zekâ destekli misafir iletişimi, kanal yönetimi, oda rafı takvimi ve ilgili konaklama yönetim araçları sunan bulut tabanlı bir otel yönetim platformudur. Hizmet, hostliopro.com üzerinden abonelikle sunulur.</p>
<h2>2. Hesap oluşturma</h2><p>Hostlio Pro'yu kullanmak için bir hesap oluşturmanız ve doğru, eksiksiz bilgi vermeniz gerekir. Hesap bilgilerinizin gizliliğini korumaktan ve hesabınız altında gerçekleşen tüm işlemlerden siz sorumlusunuz.</p>
<h2>3. Abonelik ve ödemeler</h2>
{_ul(["Abonelikler aylık veya yıllık olarak peşin faturalandırılır","Tüm ödemeler Stripe üzerinden güvenle işlenir","7 günlük ücretsiz deneme vardır; kayıt sırasında bir ödeme yöntemi alınır, ancak deneme süresi bitene kadar herhangi bir ücret tahsil edilmez","Deneme süresinden sonra seçtiğiniz plana göre ücretlendirilirsiniz",f'Fiyatlar ABD doları cinsindendir. Güncel planlar ve ücretler <a href="{pricing}">fiyatlandırma sayfamızda</a> yer alır',"Yıllık planlarda %20 indirim uygulanır"])}
<h2>4. İptal ve iade</h2><p>Aboneliğinizi istediğiniz zaman iptal edebilirsiniz. İptal, mevcut fatura döneminin sonunda geçerli olur. Kısmi fatura dönemleri için iade yapılmaz. İptal için {EMAIL} adresinden bize ulaşın.</p>
<h2>5. Kabul edilebilir kullanım</h2><p>Şunları yapmamayı kabul edersiniz:</p>
{_ul(["Hizmeti yasa dışı herhangi bir amaçla kullanmak","Entegrasyonlarımız aracılığıyla OTA platformlarının (Booking.com, Airbnb vb.) şartlarını ihlal etmek","Sistemlerimize yetkisiz erişim sağlamaya çalışmak","Misafirlere spam veya istenmeyen mesaj göndermek","Hizmeti yazılı izin olmadan yeniden satmak veya alt lisanslamak"])}
<h2>6. Yapay zekâ ile üretilen içerik</h2><p>Hostlio Pro, misafir mesajlarına yanıt üretmek için yapay zekâ kullanır. Yapay zekâ ile üretilen içeriğin zaman zaman hata içerebileceğini kabul edersiniz. Tesisiniz adına gönderilen yapay zekâ yanıtlarını gözden geçirmek ve yönetmek sizin sorumluluğunuzdadır. Yapay zekâ ile üretilen iletişimlerdeki yanlışlıklardan sorumlu değiliz.</p>
<h2>7. OTA kanal entegrasyonları</h2><p>Platformumuz, Channex API aracılığıyla üçüncü taraf OTA kanallarıyla (Booking.com, Airbnb, Expedia vb.) entegredir. Her platformun kullanım şartlarına uymaktan siz sorumlusunuz. İşlevselliği etkileyebilecek OTA API veya politika değişikliklerinden sorumlu değiliz.</p>
<h2>8. Veri ve gizlilik</h2><p>Hostlio Pro kullanımınız ayrıca bu Şartlara atıfla dahil edilen <a href="{url("privacy", L)}">Gizlilik Politikamıza</a> tabidir. Verilerinizin sahibi sizsiniz. Verilerinizi yalnızca hizmeti sunmak için işleriz.</p>
<h2>9. Hizmet sürekliliği</h2><p>%99,9 çalışma süresini hedefleriz ancak kesintisiz hizmet garanti etmeyiz. Önceden bildirimle planlı bakım yapabiliriz. Hizmet kesintilerinden doğan kayıplardan sorumlu değiliz.</p>
<h2>10. Fikri mülkiyet</h2><p>Hostlio Pro ve ilgili tüm yazılım, tasarım ve içerikler Loti Members LLC'ye aittir. Hizmetimizin herhangi bir bölümünü yazılı izin olmadan kopyalayamaz, değiştiremez veya dağıtamazsınız.</p>
<h2>11. Sorumluluğun sınırlandırılması</h2><p>Yasaların izin verdiği azami ölçüde Loti Members LLC, hizmeti kullanımınızdan doğan kâr veya veri kaybı dahil dolaylı, arızi, özel, sonuçsal veya cezai zararlardan sorumlu tutulamaz.</p>
<h2>12. Uygulanacak hukuk</h2><p>Bu Şartlar ABD'nin Kaliforniya Eyaleti yasalarına tabidir. Uyuşmazlıklar Kaliforniya, Sacramento County mahkemelerinde çözülür.</p>
<h2>13. Şartlardaki değişiklikler</h2><p>Bu Şartları zaman zaman güncelleyebiliriz. Önemli değişiklikleri e-posta veya platform üzerinden bildiririz. Değişikliklerden sonra hizmeti kullanmaya devam etmeniz yeni Şartları kabul ettiğiniz anlamına gelir.</p>
<h2>14. İletişim</h2><p>Bu Şartlarla ilgili sorularınız için:</p>
{_ul([f'E-posta: <a href="mailto:{EMAIL}">{EMAIL}</a>', f"Adres: {ADDR}"])}'''

T = {
 "privacy": {"tr": ("Gizlilik Politikası | Hostlio Pro", "Hostlio Pro gizlilik politikası: hangi verileri topladığımız, nasıl kullandığımız, kimlerle paylaştığımız, veri güvenliği, saklama süreleri ve GDPR haklarınız.", "Gizlilik Politikası"),
             "en": ("Privacy Policy | Hostlio Pro", "Hostlio Pro privacy policy: what data we collect, how we use and share it, data security, retention, cookies and your GDPR rights.", "Privacy Policy")},
 "terms":   {"tr": ("Kullanım Şartları | Hostlio Pro", "Hostlio Pro kullanım şartları: hizmet tanımı, abonelik ve ödemeler, iptal ve iade, yapay zekâ içeriği, OTA entegrasyonları ve sorumluluk.", "Kullanım Şartları"),
             "en": ("Terms of Service | Hostlio Pro", "Hostlio Pro terms of service: service description, subscriptions and payments, cancellation and refunds, AI-generated content, OTA integrations and liability.", "Terms of Service")},
}

for _l, _m in LANGMOD.items():
    for _k in ("privacy", "terms"): T[_k][_l] = _m.LEGAL_T[_k]

def legal_page(key, L):
    title, desc, h1 = T[key][L]
    body_fn = privacy_body if key == "privacy" else terms_body
    note = {"tr": f'Son güncelleme: <time datetime="{LEGAL_DATE["iso"]}">{LEGAL_DATE["tr"]}</time>, {ADDR}. Bu metin İngilizce aslının çevirisidir; farklılık halinde <a href="{url(key,"en")}">İngilizce metin</a> esas alınır.',
            "en": f'Last updated: <time datetime="{LEGAL_DATE["iso"]}">{LEGAL_DATE["en"]}</time>, {ADDR}',
            **{l: m.LEGAL_NOTE.format(iso=LEGAL_DATE["iso"], date=LEGAL_DATE[l], addr=ADDR, en_url=url(key, "en")) for l, m in LANGMOD.items()}}[L]
    body = f'''<section class="page-hero"><div class="wrap"><h1>{h1}</h1><p class="meta">{note}</p></div></section>
<section style="padding-top:0"><div class="wrap prose">{body_fn(L)}</div></section>'''
    return {"key": key, "title": title, "desc": desc, "trail": [(h1, url(key, L))], "body": body,
            "no_final": True, "modified": LEGAL_DATE["iso"], "updated_txt": LEGAL_DATE[L]}

LEGACY = json.loads((Path(__file__).parent / "legacy_posts.json").read_text())
LEGACY_KEYS = {"hotel-ai-front-desk-guide": "post-aifrontdesk", "how-to-reduce-hotel-no-shows": "post-noshows",
               "independent-hotel-vs-chain-technology": "post-chains", "whatsapp-hotel-guest-communication": "post-whatsapp"}
LEGACY_COVER = {"post-aifrontdesk": ("gen-arrival", 1080, 1350), "post-noshows": ("gen-room-dusk", 1080, 1350),
                "post-chains": ("gen-facade", 1080, 1350), "post-whatsapp": ("gen-terrace-phone", 1080, 1350)}

def legacy_meta():
    return [{"key": LEGACY_KEYS[p["slug"]], "title": p["title"], "date": p["date"], "desc": p["desc"]} for p in LEGACY]

def legacy_posts(article):
    return [article({"key": LEGACY_KEYS[p["slug"]], "title": p["title"], "date": p["date"], "desc": p["desc"]}, p["body"], []) for p in LEGACY]

DELACC = {
 "en": ("Delete Your Account | Hostlio Pro", "How to request deletion of your Hostlio Pro account and the data associated with it.", "Request account deletion",
        "To request deletion of your Hostlio Pro account and all associated data, email {e} with the subject line <strong>“Account Deletion Request”</strong> and include your registered email address. We will process your request within 30 days.", "Send deletion request", "Account Deletion Request",
        "Before you go: exporting your reservations and guest records from the dashboard is recommended, because deletion is permanent."),
 "tr": ("Hesap Silme | Hostlio Pro", "Hostlio Pro hesabınızın ve ilişkili verilerin silinmesini nasıl talep edeceğiniz.", "Hesap silme talebi",
        "Hostlio Pro hesabınızın ve ilişkili tüm verilerin silinmesini talep etmek için {e} adresine <strong>“Hesap Silme Talebi”</strong> konulu bir e-posta gönderin ve kayıtlı e-posta adresinizi ekleyin. Talebinizi 30 gün içinde işleme alırız.", "Silme talebi gönder", "Hesap Silme Talebi",
        "Göndermeden önce: silme işlemi kalıcı olduğundan rezervasyon ve misafir kayıtlarınızı panelden dışa aktarmanızı öneririz."),
 "es": ("Eliminar tu cuenta | Hostlio Pro", "Cómo solicitar la eliminación de tu cuenta de Hostlio Pro y de los datos asociados.", "Solicitar la eliminación de la cuenta",
        "Para solicitar la eliminación de tu cuenta de Hostlio Pro y de todos los datos asociados, envía un correo a {e} con el asunto <strong>“Solicitud de eliminación de cuenta”</strong> e incluye el correo con el que te registraste. Tramitaremos tu solicitud en un plazo de 30 días.", "Enviar solicitud de eliminación", "Solicitud de eliminación de cuenta",
        "Antes de enviarla: te recomendamos exportar tus reservas y fichas de huéspedes desde el panel, porque la eliminación es definitiva."),
 "it": ("Elimina il tuo account | Hostlio Pro", "Come richiedere l’eliminazione del tuo account Hostlio Pro e dei dati collegati.", "Richiedi l’eliminazione dell’account",
        "Per richiedere l’eliminazione del tuo account Hostlio Pro e di tutti i dati collegati, scrivi a {e} con oggetto <strong>“Richiesta di eliminazione account”</strong> indicando l’indirizzo email registrato. Gestiremo la richiesta entro 30 giorni.", "Invia la richiesta di eliminazione", "Richiesta di eliminazione account",
        "Prima di inviarla: ti consigliamo di esportare prenotazioni e schede ospiti dal pannello, perché l’eliminazione è definitiva."),
 "pt": ("Excluir sua conta | Hostlio Pro", "Como solicitar a exclusão da sua conta do Hostlio Pro e dos dados associados.", "Solicitar exclusão da conta",
        "Para solicitar a exclusão da sua conta do Hostlio Pro e de todos os dados associados, envie um e-mail para {e} com o assunto <strong>“Solicitação de exclusão de conta”</strong> e informe o e-mail cadastrado. Processaremos sua solicitação em até 30 dias.", "Enviar solicitação de exclusão", "Solicitação de exclusão de conta",
        "Antes de enviar: recomendamos exportar suas reservas e fichas de hóspedes pelo painel, pois a exclusão é definitiva."),
 "fr": ("Supprimer votre compte | Hostlio Pro", "Comment demander la suppression de votre compte Hostlio Pro et des données associées.", "Demander la suppression du compte",
        "Pour demander la suppression de votre compte Hostlio Pro et de toutes les données associées, écrivez à {e} avec l’objet <strong>« Demande de suppression de compte »</strong> en indiquant l’adresse e-mail utilisée à l’inscription. Nous traiterons votre demande sous 30 jours.", "Envoyer la demande de suppression", "Demande de suppression de compte",
        "Avant l’envoi : nous vous conseillons d’exporter vos réservations et fiches clients depuis le tableau de bord, car la suppression est définitive."),
}

def delacc_page(L):
    from build import btn, icon
    from urllib.parse import quote
    title, desc, h1, text, cta, subj, note = DELACC[L]
    mail = f'<a href="mailto:{EMAIL}">{EMAIL}</a>'
    body = f'''<section class="page-hero"><div class="wrap"><h1>{h1}</h1></div></section>
<section style="padding-top:0"><div class="wrap prose"><div class="answer"><p>{text.format(e=mail)}</p></div>
<p class="small muted">{note}</p>
<div class="cta-row">{btn(cta, f"mailto:{EMAIL}?subject={quote(subj)}")}</div></div></section>'''
    return {"key": "delacc", "title": title, "desc": desc, "trail": [(h1, url("delacc", L))], "body": body, "no_final": True}

def pages(L, article):
    import build as _b, security_page as _sp
    import roi_page as _roi
    out = [legal_page("privacy", L), legal_page("terms", L), delacc_page(L), _sp.security_page(L, _b), _roi.roi_page(L, _b)]
    if L == "en": out += legacy_posts(article) + [_sp.dpa_page(_b)]
    return out
