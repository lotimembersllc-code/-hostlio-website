"""K5 (Eylül 2026) — güncel Gizlilik Politikası, Kullanım Şartları, Veri İşleme Sözleşmesi (DPA) ve
Güvenlik ve veri sayfası. İngilizce metin esastır; diğer diller çeviridir (legal_v6_intl.py).

🔺 Yayından önce bir avukatın son okuması önerilir (rapor K5).
🔺 8 Eki 2026 hukuk taslağı (dal site-hukuk): metinler ürünün bugünkü davranışına hizalandı — avukat okuması
   bitmeden YAYINLANMAZ. Kaynak/karşılaştırma: scratchpad/hukuk_taslak.md. TASLAK=True iken hukuki sayfalarda
   görünür "TASLAK" şeridi çıkar; onaydan sonra False yapın ve LEGAL_ISO/LEGAL_DATE'i yayın gününe çekin.
🔺 RETENTION süreleri canlı `public.retention_policy` + cron ile teyit edildi (8 Eki 2026):
   conversations 60 (otel kısaltabilir, alt sınır 30 — otel_mesaj_saklama_gun), reservations_contact 90 (çıkıştan sonra;
   Lio rezervasyon talepleri de), guests_pii 365 (hareketsizlik), reviews_guest_name 365, checkin_files 30 (imza, çıkıştan
   sonra), islem_kayitlari 365, bildirimler 90 (bildirimleri_temizle). PASİF: reservations_name, checkin_id_data.
"""
TASLAK = True              # 8 Eki 2026 hukuk taslağı — avukat onayından sonra False
LEGAL_ISO = "2026-10-08"   # 8 Eki 2026: plan değişikliği (anında + kıst), saklama süreleri, personel/işlem geçmişi, Lio Önerileri, Resend
# 4 Eki 2026: P1 — kimlik görüntüsü saklanmaz (MRZ cihazda okunur), Google ML Kit eklendi
# 3 Eki 2026: Firebase alt işleyicisi, hostlio_acq 90 gün (O5/O6)
LEGAL_DATE = {"en": "October 8, 2026", "tr": "8 Ekim 2026", "es": "8 de octubre de 2026",
              "it": "8 ottobre 2026", "pt": "8 de outubro de 2026", "fr": "8 octobre 2026"}
RETENTION = {"msg_default_days": 60, "msg_min_days": 30, "guest_contact_days": 90, "guest_profile_days": 365,
             "review_name_days": 365, "signature_days": 30, "audit_days": 365, "notif_days": 90, "deletion_days": 30}
# Hesap silme (gizlilik §7, şartlar §5/§10, DPA §9) — metin hesap silme tasarımından (scratchpad/hesap_silme.md §7,
# 8 Eki 2026; feat/hesap-silme). ⚠️ Hesap silme özelliği canlıya alınmadan bu metinler YAYINLANMAMALI.
DELETION = {
 "en": "Account and hotel data are kept while the account is active. The account owner can request deletion in the dashboard or the mobile app (Settings), or by email from our account deletion page; we verify the request by password or by a confirmation link sent to the owner’s email address. The account and all of its properties are deleted {d} days after a verified request (the owner can cancel until then). During those {d} days automatic replies, automatic guest messages and channel sync are paused and the subscription does not renew. Invoices are kept by our payment provider (Stripe), and we keep a minimal billing record without personal data (account identifier, Stripe customer and subscription identifiers, plan and dates) for up to 10 years for tax and accounting purposes",
 "tr": "Hesap ve otel verileri hesap aktif olduğu sürece saklanır. Hesap sahibi silme talebini panelden veya mobil uygulamadan (Ayarlar) ya da hesap silme sayfamızdan e-postayla iletebilir; talebi parola ya da sahibin e-posta adresine gönderilen onay bağlantısıyla doğrularız. Hesap ve tüm mülkleri doğrulanmış talepten {d} gün sonra silinir (sahip o güne kadar iptal edebilir). Bu {d} gün boyunca otomatik yanıtlar, otomatik misafir mesajları ve kanal senkronizasyonu durur, abonelik yenilenmez. Faturalar ödeme sağlayıcımızda (Stripe) saklanır; vergi ve muhasebe amacıyla kişisel veri içermeyen asgari bir fatura kaydını (hesap kimliği, Stripe müşteri ve abonelik kimlikleri, plan ve tarihler) en fazla 10 yıl tutarız",
 "es": "Los datos de la cuenta y del hotel se conservan mientras la cuenta esté activa. El titular de la cuenta puede solicitar la eliminación desde el panel o la app móvil (Ajustes), o por email desde nuestra página de eliminación de cuenta; verificamos la solicitud con la contraseña o con un enlace de confirmación enviado al email del titular. La cuenta y todos sus alojamientos se eliminan {d} días después de una solicitud verificada (el titular puede cancelarla hasta entonces). Durante esos {d} días se pausan las respuestas automáticas, los mensajes automáticos a huéspedes y la sincronización de canales, y la suscripción no se renueva. Las facturas las conserva nuestro proveedor de pagos (Stripe), y guardamos un registro mínimo de facturación sin datos personales (identificador de la cuenta, identificadores de cliente y suscripción de Stripe, plan y fechas) durante un máximo de 10 años por motivos fiscales y contables",
 "it": "I dati dell’account e dell’hotel sono conservati finché l’account è attivo. Il titolare dell’account può chiedere l’eliminazione dal pannello o dall’app mobile (Impostazioni), oppure via email dalla nostra pagina di eliminazione dell’account; verifichiamo la richiesta con la password o con un link di conferma inviato all’indirizzo email del titolare. L’account e tutte le sue strutture vengono eliminati {d} giorni dopo una richiesta verificata (il titolare può annullarla fino ad allora). In quei {d} giorni le risposte automatiche, i messaggi automatici agli ospiti e la sincronizzazione dei canali sono sospesi e l’abbonamento non si rinnova. Le fatture sono conservate dal nostro fornitore di pagamenti (Stripe) e conserviamo un registro minimo di fatturazione senza dati personali (identificativo dell’account, identificativi cliente e abbonamento Stripe, piano e date) per un massimo di 10 anni a fini fiscali e contabili",
 "pt": "Os dados da conta e do hotel são guardados enquanto a conta estiver ativa. O titular da conta pode pedir a exclusão pelo painel ou pelo app (Configurações), ou por e-mail a partir da nossa página de exclusão de conta; verificamos o pedido pela senha ou por um link de confirmação enviado ao e-mail do titular. A conta e todas as suas propriedades são excluídas {d} dias após um pedido verificado (o titular pode cancelar até lá). Durante esses {d} dias, as respostas automáticas, as mensagens automáticas a hóspedes e a sincronização de canais ficam pausadas e a assinatura não é renovada. As faturas ficam com nosso provedor de pagamentos (Stripe), e mantemos um registro mínimo de cobrança sem dados pessoais (identificador da conta, identificadores de cliente e assinatura na Stripe, plano e datas) por até 10 anos para fins fiscais e contábeis",
 "fr": "Les données du compte et de l’hôtel sont conservées tant que le compte est actif. Le titulaire du compte peut demander la suppression depuis le tableau de bord ou l’application mobile (Réglages), ou par e-mail depuis notre page de suppression de compte ; nous vérifions la demande par mot de passe ou par un lien de confirmation envoyé à l’adresse e-mail du titulaire. Le compte et tous ses établissements sont supprimés {d} jours après une demande vérifiée (le titulaire peut l’annuler jusque-là). Pendant ces {d} jours, les réponses automatiques, les messages automatiques aux clients et la synchronisation des canaux sont suspendus et l’abonnement n’est pas renouvelé. Les factures sont conservées par notre prestataire de paiement (Stripe) et nous gardons un registre de facturation minimal sans données personnelles (identifiant du compte, identifiants client et abonnement Stripe, forfait et dates) pendant 10 ans au maximum à des fins fiscales et comptables",
}
DELETION = {k: v.format(d=RETENTION["deletion_days"]) for k, v in DELETION.items()}
# DPA §9 (yalnız EN). Not: silme yalnız TALEP üzerine; talepsiz biten abonelikte otomatik silme yok (hesap_silme.md §7).
DPA_DELETION = f"The account owner can request deletion of the account at any time. Customer Personal Data is deleted {RETENTION['deletion_days']} days after a verified deletion request (the owner can cancel until then), except where the law requires us to keep it; a minimal billing record without personal data is kept for up to 10 years."
# Kullanım Şartları §10 sonu — {u} = hesap silme sayfası.
DELETION_T = {
 "en": 'The account owner can request deletion of the account and all of its data; see <a href="{u}">Delete your account</a>.',
 "tr": 'Hesap sahibi hesabın ve tüm verilerinin silinmesini talep edebilir; <a href="{u}">hesap silme</a> sayfasına bakın.',
 "es": 'El titular de la cuenta puede solicitar la eliminación de la cuenta y de todos sus datos; consulta <a href="{u}">Eliminar tu cuenta</a>.',
 "it": 'Il titolare dell’account può chiedere l’eliminazione dell’account e di tutti i suoi dati; consulta <a href="{u}">Elimina il tuo account</a>.',
 "pt": 'O titular da conta pode pedir a exclusão da conta e de todos os seus dados; veja <a href="{u}">Excluir sua conta</a>.',
 "fr": 'Le titulaire du compte peut demander la suppression du compte et de toutes ses données ; voir <a href="{u}">Supprimer votre compte</a>.',
}
# Kullanım Şartları §5 sonuna (hesap silme ve abonelik).
DELETION_CANCEL = {
 "en": "If you request account deletion, your subscription is set not to renew; if a paid period is still running {d} days later, it ends when the account is deleted, without a partial refund.",
 "tr": "Hesap silme talebinde aboneliğiniz yenilenmeyecek şekilde ayarlanır; {d} gün sonra hâlâ süren bir ödenmiş dönem varsa hesap silindiğinde sona erer, kısmi iade yapılmaz.",
 "es": "Si solicitas la eliminación de la cuenta, tu suscripción se configura para no renovarse; si {d} días después sigue en curso un periodo pagado, termina cuando se elimina la cuenta, sin reembolso parcial.",
 "it": "Se chiedi l’eliminazione dell’account, l’abbonamento viene impostato per non rinnovarsi; se {d} giorni dopo è ancora in corso un periodo pagato, termina con l’eliminazione dell’account, senza rimborso parziale.",
 "pt": "Se você pedir a exclusão da conta, a assinatura é configurada para não renovar; se {d} dias depois ainda houver um período pago em curso, ele termina quando a conta é excluída, sem reembolso parcial.",
 "fr": "Si vous demandez la suppression du compte, votre abonnement est paramétré pour ne pas se renouveler ; si une période payée est encore en cours {d} jours plus tard, elle prend fin à la suppression du compte, sans remboursement partiel.",
}
DELETION_CANCEL = {k: v.format(d=RETENTION["deletion_days"]) for k, v in DELETION_CANCEL.items()}
_TASLAK_TXT = {"en": "DRAFT – under legal review, not yet in effect. Not legal advice.",
               "tr": "TASLAK – hukuki inceleme sürüyor, henüz yürürlükte değil. Hukuki görüş değildir.",
               "es": "BORRADOR – en revisión legal, aún no está en vigor. No constituye asesoramiento jurídico.",
               "it": "BOZZA – in revisione legale, non ancora in vigore. Non costituisce consulenza legale.",
               "pt": "RASCUNHO – em revisão jurídica, ainda não está em vigor. Não constitui aconselhamento jurídico.",
               "fr": "BROUILLON – en cours de relecture juridique, pas encore en vigueur. Ne constitue pas un conseil juridique."}

def taslak_serit(L):
    """TASLAK=True iken hukuki sayfaların başlığına eklenen görünür şerit (onaydan sonra TASLAK=False)."""
    return f'<p class="meta" role="note"><strong>{_TASLAK_TXT.get(L, _TASLAK_TXT["en"])}</strong></p>' if TASLAK else ""
import pricing  # tek fiyat/kota kaynağı

def quota(lang):
    """Aylık AI mesaj kotası, dilin sayı biçimiyle (pricing.py'den)."""
    return {pid: pricing.number(pricing.BY_ID[pid]["ai_messages"], lang) for pid in ("starter", "pro", "growth")}

# Alt işleyiciler — gizlilik, DPA ve güvenlik sayfalarında aynı liste
SUBPROCESSORS = [
    # (ad, konum, amaç anahtarı)
    ("Supabase, Inc.", "EU (Ireland); company in USA", "db"),
    ("Vercel, Inc.", "USA", "web"),
    ("Stripe, Inc.", "USA", "pay"),
    ("Anthropic, PBC", "USA", "ai"),
    ("Meta Platforms, Inc. (WhatsApp Business Platform)", "USA / Ireland", "wa"),
    ("Channex.io Ltd", "United Kingdom", "chx"),
    ("Resend, Inc.", "USA", "mail"),
    ("Make (Celonis)", "EU", "make"),
    ("Google LLC / Google Ireland Ltd. (Firebase Cloud Messaging)", "USA / global", "push"),
    ("Apple Inc. (Apple Push Notification service)", "USA", "apns"),
    ("Google LLC (ML Kit — on-device text recognition)", "On device (metrics: USA)", "mlkit"),
]
PLANNED = [("Twilio Inc.", "USA", "tw"), ("Twilio SendGrid", "USA", "sg")]
SP_PURPOSE = {
 "en": {"db": "Database, authentication and server functions", "web": "Website, dashboard and guest check-in page hosting, including hotels’ own check-in domains", "pay": "Payments and subscription billing",
        "ai": "AI processing to draft replies to guest messages and OTA reviews, translate the hotel’s message templates and, for Lio Suggestions, find recurring themes in guest messages and reviews after personal details are masked", "wa": "Sending and receiving WhatsApp messages", "chx": "Availability, rate, booking and OTA message sync",
        "mail": "Sending emails: account, billing and quota notices, staff invitations, weekly and monthly reports, and, when the hotel enables them, check-in links and messages to guests", "make": "Contact form and internal workflow automation", "push": "Push notifications to the Hostlio Pro mobile app on iOS and Android (device push token, app instance identifiers, notification content such as new message or reservation alerts)", "apns": "Delivery of push notifications to iPhone and iPad devices (device token and notification content, passed on by Firebase Cloud Messaging)", "mlkit": "Reading the ID document’s machine-readable zone on the hotel staff’s device in the mobile app; no images or text leave the device; Google receives only anonymous API usage and performance metrics", "tw": "WhatsApp numbers and messaging billing for hotels", "sg": "Receiving guest emails for a planned email channel"},
 "tr": {"db": "Veritabanı, kimlik doğrulama ve sunucu fonksiyonları", "web": "Web sitesi, panel ve misafir check-in sayfası barındırma (otellerin kendi check-in alan adları dahil)", "pay": "Ödemeler ve abonelik faturalandırması",
        "ai": "Misafir mesajlarına ve OTA yorumlarına cevap taslağı hazırlamak, otelin mesaj şablonlarını çevirmek ve Lio Önerileri için kişisel bilgiler maskelendikten sonra misafir mesajları ile yorumlarda tekrarlayan konuları bulmak üzere yapay zekâ ile işleme", "wa": "WhatsApp mesajlarının gönderilmesi ve alınması", "chx": "Müsaitlik, fiyat, rezervasyon ve OTA mesaj senkronizasyonu",
        "mail": "E-posta gönderimi: hesap, fatura ve kota bildirimleri, personel davetleri, haftalık ve aylık raporlar ile otel açtığında misafirlere check-in bağlantısı ve mesajlar", "make": "İletişim formu ve iç iş akışı otomasyonu", "push": "Hostlio Pro mobil uygulamasına (iOS ve Android) anlık bildirim gönderimi (cihaz bildirim jetonu, uygulama örneği kimlikleri, yeni mesaj veya rezervasyon uyarısı gibi bildirim içeriği)", "apns": "iPhone ve iPad cihazlara anlık bildirimin iletilmesi (Firebase Cloud Messaging üzerinden aktarılan cihaz jetonu ve bildirim içeriği)", "mlkit": "Mobil uygulamada kimlik belgesinin makine okunabilir alanının otel personelinin cihazında okunması; görüntü veya metin cihazdan çıkmaz, Google yalnızca anonim API kullanım ve performans ölçümlerini alır", "tw": "Oteller için WhatsApp numarası ve mesaj faturalandırması", "sg": "Planlanan e-posta kanalı için misafir e-postalarının alınması"},
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
      "<strong>Online check-in data:</strong> identity document details (name, document number or, for Turkish ID cards, the T.C. identity number, nationality, date of birth and expiry date), companions and a digital signature, when the hotel uses online check-in. The document’s machine-readable zone is read on the guest’s or the hotel staff’s own device; we do not collect or store images of identity documents. We treat this data as sensitive",
      "<strong>Signup and security data:</strong> IP address, a hashed email and the outcome of signup attempts, used to prevent fraud and abuse",
      "<strong>Marketing source:</strong> only if you arrive through a link with campaign parameters (UTM parameters or an ad click ID): those parameters, the landing page and the time of your first visit, stored in your browser and sent to us only with your signup or contact form",
      "<strong>Staff data:</strong> when you invite team members, their email address, name, role, the properties they can access, invitation status and preferred language",
      "<strong>Activity log:</strong> who did what and when in the dashboard and app (user, role, action, affected record, source app and a shortened IP address). For guest and check-in records only the action and the names of changed fields are logged, never their values",
      "<strong>OTA reviews:</strong> review text, ratings and the reviewer’s name received from connected channels, and the replies you approve",
      "<strong>Usage data:</strong> how the dashboard and app are used, technical logs and, when you use the mobile app, your device’s push notification token. Cookies and website analytics on hostliopro.com are described in section 10"])}
<h2>3. How we use data</h2>
{_ul(["To provide the service: syncing channels, showing reservations, sending guest messages and running online check-in",
      "To draft and send AI replies to guest messages on the hotel’s behalf",
      "To show the hotel its analytics (occupancy, revenue and similar totals) and to send weekly and monthly report emails, which contain totals only and no guest details",
      "To give the hotel Lio Suggestions: suggestions based on its own data, including recurring themes in guest messages and reviews (see section 13)",
      "To keep an activity log so the account owner can see who changed what, and to investigate security incidents",
      "To run your subscription: the free trial, automatic charges when the trial ends and at each renewal, invoices and plan limits such as the monthly AI message quota",
      "To keep the service secure and prevent fraud",
      "To measure which marketing channels bring customers",
      "To answer support requests and send service and billing emails",
      "To meet legal obligations"])}
<p>We do not sell personal data and we do not share it for cross-context behavioural advertising. Guest message content is not used for our marketing. Our AI provider processes this content only to provide the AI features described in section 13 and, under its commercial terms, does not use it to train its models.</p>
<h2>4. Legal bases (EEA, UK, Türkiye)</h2><p>We rely on performance of our contract with you, our legitimate interests (security, fraud prevention, improving the service, measuring marketing), compliance with legal obligations and, where required, your consent. For guest data, the hotel determines the legal basis.</p>
<h2>5. Who we share data with</h2><p>We use the subprocessors below. Each is bound by a contract that protects the data. When you connect a sales channel (such as Booking.com, Airbnb or Expedia), data is exchanged with that channel under its own terms.</p>
{sp_table("en")}
<p>We may also disclose data when required by law or to protect our rights.</p>
<h2>6. International transfers</h2><p>We are based in the United States and some subprocessors process data outside the EEA, the UK and Türkiye. Where required, transfers are protected by the European Commission’s Standard Contractual Clauses, the UK Addendum or other lawful transfer mechanisms.</p>
<h2>7. How long we keep data</h2>
{_ul([f"Guest message content and attachments are anonymised {R['msg_default_days']} days after check-out, or after the last message if the conversation is not linked to a reservation. The hotel can shorten this period in its settings to as little as {R['msg_min_days']} days, but cannot extend it",
      f"Guest email addresses, phone numbers and reservation notes are erased {R['guest_contact_days']} days after check-out, unless the hotel deletes them sooner. For booking requests guests make through Lio, the guest’s name and contact details are erased {R['guest_contact_days']} days after the hotel decides on the request. Guest names and booking details (dates, room, price, channel) stay on the reservation while the hotel’s account is active, because the hotel may need them for invoicing and accounting",
      f"Guest profiles in the hotel’s guest list are anonymised after {R['guest_profile_days']} days without a stay",
      f"Reviewer names on OTA reviews are removed {R['review_name_days']} days after the review is received; the review text, which is public on the channel, is kept",
      f"Online check-in: images of identity documents are never stored. Guest signatures are deleted automatically {R['signature_days']} days after check-out. Identity document details are kept only as long as the hotel needs them to meet its guest-registration duties, and are deleted with the hotel’s account at the latest",
      f"The activity log is kept for {R['audit_days']} days and in-app notifications for {R['notif_days']} days",
      DELETION["en"],
      "Billing records are kept for as long as tax and accounting law requires",
      "Signup and security logs are kept for a limited period for fraud prevention"])}
<h2>8. Security</h2><p>Data is encrypted in transit (TLS) and at rest. Access is restricted by hotel and by role: staff only see the properties and features their role allows, and important actions are recorded in the activity log. Our database provider is SOC 2 Type 2 audited and card payments are handled by Stripe, a PCI DSS Level 1 service provider. More on our <a href="{U("security")}">Security and data</a> page.</p>
<h2>9. Your rights</h2>
<p><strong>EEA and UK:</strong> you can request access, correction, deletion, restriction, portability, and object to processing. You may also complain to your local data protection authority.</p>
<p><strong>California (CCPA/CPRA):</strong> you can ask to know, delete and correct your personal information. We do not sell or share personal information, and we will not discriminate against you for exercising your rights.</p>
<p><strong>Türkiye (KVKK):</strong> under Article 11 of Law No. 6698 you can learn whether your data is processed, request information, correction or deletion, and object to results arising from automated processing.</p>
<p>To exercise any right, email <a href="mailto:{EMAIL}">{EMAIL}</a>. To close your account, see <a href="{U("delacc")}">Delete your account</a>.</p>
<h2>10. Cookies and browser storage</h2><p>The dashboard uses essential cookies and storage to keep you signed in. Our website stores your language choice in your browser’s local storage. For marketing measurement nothing is stored on ordinary visits: only when you arrive through a link that carries campaign parameters (utm_source, utm_medium, utm_campaign, utm_term, utm_content, or an ad click ID: gclid, msclkid, ttclid, fbclid) does the site save those parameters, the landing page path and the time of that first visit in local storage under the key <code>hostlio_acq</code>. No cookie is set for this. The referring website’s domain is read only for the current page view and is not stored. This record is first-party: the site never shares it with ad networks, it is sent to us only if you submit the signup or contact form (attached to that submission), and it is deleted automatically after 90 days. We rely on our legitimate interest in measuring which marketing channels bring customers; you can object and erase the record at any time by clearing the site data for hostliopro.com in your browser. We do not use advertising cookies. If we add website analytics, we will update this policy first.</p>
<h2>11. WhatsApp and guest messaging</h2><p>Hostlio Pro connects to the WhatsApp Business Platform and to OTA inboxes to send and receive guest messages for hotels. Guest phone numbers are used only to communicate about the stay. Guests can stop receiving messages by telling the hotel.</p>
<h2>12. Staff accounts and activity log</h2><p>The account owner can invite staff and give each person a role (manager, front desk, housekeeping, accounting or viewer) and access to selected properties. We use the invited person’s email address to send the invitation and, once they accept, their name, email address, role and property access to let them in. The owner decides who is invited and should tell staff that their actions are logged.</p><p>The activity log records actions such as creating, changing or cancelling reservations, changing rates, rooms, settings or team members, and approving or rejecting AI replies, together with the user, their role, the time, the app used and a shortened IP address (IPv4 to /24, IPv6 to /48). Entries cannot be edited, are visible to the account owner and to roles with permission, and are deleted after {R['audit_days']} days.</p>
<h2>13. AI features (Lio)</h2>{_ul(["<strong>Replies to guests:</strong> Lio sends the guest’s message, earlier messages in the conversation, the guest’s booking details (such as name, dates and room) and the hotel’s information to our AI provider to draft a reply. The hotel decides which topics are answered automatically and which need approval",
      "<strong>Review replies:</strong> on plans that include it, Lio drafts replies to OTA reviews. No review reply is sent without the hotel’s approval",
      "<strong>Translation:</strong> the hotel’s welcome and farewell templates can be translated with AI",
      "<strong>Lio Suggestions:</strong> on the Pro and Growth plans, new guest messages and reviews are checked once a day for recurring themes (for example cleanliness or Wi-Fi). Before any text is sent, email addresses, phone numbers, web links, long numbers such as booking or card numbers, and the guest’s name are masked automatically. The results are short, general summaries without personal names, room numbers, dates or contact details; the original texts are not stored with the suggestions or in our logs. The optional weekly summary is written only from these themes and statistics, without guest texts. The hotel can turn off the AI part of Lio Suggestions in its settings"])}
<h2>14. Children</h2><p>Hostlio Pro is a business service and is not directed to children under 16.</p>
<h2>15. Changes</h2><p>We will post changes on this page and update the date above. For material changes we will also notify customers by email or in the dashboard.</p>
<h2>16. Contact</h2>{_ul([f'Email: <a href="mailto:{EMAIL}">{EMAIL}</a>', f"Address: {ADDR}"])}'''

def privacy_tr(U, EMAIL, ADDR):
    R = RETENTION
    return f'''<p>Bu Gizlilik Politikası, Loti Members LLC (“biz”) tarafından işletilen Hostlio Pro’nun; hostliopro.com’u ziyaret ettiğinizde, kaydolduğunuzda ya da Hostlio Pro paneli, mobil uygulaması ve misafire dönük özelliklerini kullandığınızda kişisel verileri nasıl topladığını, kullandığını ve paylaştığını açıklar.</p>
<h2>1. Rolümüz</h2><p>Müşterilerimize (otel sahipleri ve çalışanları) ve site ziyaretçilerine ait veriler için <strong>veri sorumlusu</strong> biziz. Bir otel adına hizmeti yürütmek için işlediğimiz misafir verilerinde veri sorumlusu oteldir; biz <strong>veri işleyen</strong> konumundayız. Bu işleme <a href="{U("dpa")}">Veri İşleme Sözleşmemize (DPA)</a> tabidir. Haklarını kullanmak isteyen misafirler otele başvurmalıdır; otelin yanıt vermesine yardımcı oluruz.</p>
<h2>2. Topladığımız veriler</h2>
{_ul(["<strong>Hesap verileri:</strong> ad, e-posta, telefon, otel adı, oda sayısı, ülke, misafir para birimi ve saat dilimi",
      "<strong>Fatura verileri:</strong> plan, fatura dönemi ve ödeme durumu. Kart bilgileri bizde değil, Stripe’ta toplanır ve saklanır",
      "<strong>Otel verileri:</strong> oda tipleri, odalar, fiyatlar, müsaitlik, rezervasyonlar ve ayarlar",
      "<strong>Oteller adına işlenen misafir verileri:</strong> misafir adı, iletişim bilgileri, rezervasyon bilgileri ve WhatsApp ile OTA gelen kutularına gelen mesajların içeriği",
      "<strong>Online check-in verileri:</strong> otel online check-in kullanıyorsa kimlik belgesi bilgileri (ad soyad, belge numarası ya da T.C. kimlik kartlarında T.C. kimlik no, uyruk, doğum tarihi ve geçerlilik tarihi), refakatçiler ve dijital imza. Belgenin makine okunabilir alanı misafirin ya da otel personelinin kendi cihazında okunur; kimlik belgesi görüntüsü toplamaz ve saklamayız. Bu verileri hassas veri olarak ele alırız",
      "<strong>Kayıt ve güvenlik verileri:</strong> IP adresi, e-postanın özetlenmiş (hash) hali ve kayıt denemelerinin sonucu; dolandırıcılık ve kötüye kullanımı önlemek için",
      "<strong>Pazarlama kaynağı:</strong> yalnızca sitemize kampanya parametreleri (UTM parametreleri veya reklam tıklama kimliği) içeren bir bağlantıyla geldiyseniz bu parametreler, giriş sayfası ve ilk ziyaretinizin zamanı; tarayıcınızda saklanır ve bize yalnızca kayıt veya iletişim formuyla birlikte iletilir",
      "<strong>Personel verileri:</strong> ekip üyesi davet ettiğinizde o kişinin e-posta adresi, adı, rolü, erişebileceği tesisler, davet durumu ve dil tercihi",
      "<strong>İşlem geçmişi:</strong> panelde ve uygulamada kimin neyi ne zaman yaptığı (kullanıcı, rol, işlem, etkilenen kayıt, kullanılan uygulama ve kısaltılmış IP adresi). Misafir ve check-in kayıtlarında yalnız işlem ve değişen alanların adları kaydedilir, değerleri asla kaydedilmez",
      "<strong>OTA yorumları:</strong> bağlı kanallardan gelen yorum metni, puanlar ve yorum yapanın adı ile onayladığınız cevaplar",
      "<strong>Kullanım verileri:</strong> panel ve uygulamanın nasıl kullanıldığı, teknik kayıtlar ve mobil uygulamayı kullandığınızda cihazınızın bildirim jetonu (push token). hostliopro.com’daki çerezler ve site analitiği 10. bölümde anlatılır"])}
<h2>3. Verileri nasıl kullanırız</h2>
{_ul(["Hizmeti sunmak için: kanalları senkronize etmek, rezervasyonları göstermek, misafir mesajlarını göndermek ve online check-in’i yürütmek",
      "Otel adına misafir mesajlarına yapay zekâ ile cevap taslağı hazırlamak ve göndermek",
      "Otele analizlerini (doluluk, gelir ve benzeri toplamlar) göstermek ve yalnız toplamları içeren, misafir bilgisi taşımayan haftalık ve aylık rapor e-postaları göndermek",
      "Otele Lio Önerileri sunmak: misafir mesajları ve yorumlardaki tekrarlayan konular dahil, otelin kendi verilerine dayanan öneriler (bkz. 13. bölüm)",
      "Hesap sahibinin kimin neyi değiştirdiğini görebilmesi ve güvenlik olaylarının incelenebilmesi için işlem geçmişi tutmak",
      "Aboneliğinizi yürütmek için: ücretsiz deneme, deneme bitiminde ve her yenilemede otomatik ücretlendirme, faturalar ve aylık AI mesaj kotası gibi plan limitleri",
      "Hizmeti güvende tutmak ve dolandırıcılığı önlemek",
      "Hangi pazarlama kanallarının müşteri getirdiğini ölçmek",
      "Destek taleplerini yanıtlamak, hizmet ve fatura e-postaları göndermek",
      "Yasal yükümlülükleri yerine getirmek"])}
<p>Kişisel verileri satmayız ve davranışsal reklam için paylaşmayız. Misafir mesajları pazarlamamızda kullanılmaz. Yapay zekâ sağlayıcımız bu içeriği yalnızca 13. bölümde anlatılan yapay zekâ özelliklerini sunmak için işler ve ticari şartları gereği modellerini eğitmekte kullanmaz.</p>
<h2>4. Hukuki sebepler (AEA, Birleşik Krallık, Türkiye)</h2><p>Sizinle yaptığımız sözleşmenin ifası, meşru menfaatlerimiz (güvenlik, dolandırıcılığın önlenmesi, hizmetin geliştirilmesi, pazarlamanın ölçülmesi), yasal yükümlülükler ve gerektiğinde açık rızanıza dayanırız. Misafir verilerinde hukuki sebebi otel belirler.</p>
<h2>5. Verileri kimlerle paylaşırız</h2><p>Aşağıdaki alt işleyicileri kullanırız; her biri verileri koruyan bir sözleşmeyle bağlıdır. Bir satış kanalı (Booking.com, Airbnb, Expedia gibi) bağladığınızda veriler o kanalla kendi şartları çerçevesinde paylaşılır.</p>
{sp_table("tr")}
<p>Kanunen gerektiğinde veya haklarımızı korumak için de veri açıklayabiliriz.</p>
<h2>6. Yurt dışına aktarım</h2><p>Şirketimiz ABD’dedir ve bazı alt işleyiciler verileri AEA, Birleşik Krallık ve Türkiye dışında işler. Gerektiğinde aktarımlar Avrupa Komisyonu Standart Sözleşme Maddeleri, Birleşik Krallık eki veya KVKK’ya uygun diğer aktarım araçlarıyla korunur.</p>
<h2>7. Saklama süreleri</h2>
{_ul([f"Misafir mesaj içerikleri ve ekleri çıkıştan {R['msg_default_days']} gün sonra (konuşma bir rezervasyona bağlı değilse son mesajdan {R['msg_default_days']} gün sonra) anonimleştirilir. Otel bu süreyi ayarlarından en az {R['msg_min_days']} güne kadar kısaltabilir, uzatamaz",
      f"Misafirin e-posta adresi, telefonu ve rezervasyon notları, otel daha önce silmezse çıkıştan {R['guest_contact_days']} gün sonra silinir. Misafirlerin Lio üzerinden yaptığı rezervasyon taleplerinde misafirin adı ve iletişim bilgileri, otel talep hakkında karar verdikten {R['guest_contact_days']} gün sonra silinir. Misafir adı ve rezervasyon bilgileri (tarihler, oda, fiyat, kanal) otel faturalandırma ve muhasebe için ihtiyaç duyabileceğinden otelin hesabı aktif olduğu sürece rezervasyonda kalır",
      f"Otelin misafir listesindeki misafir profilleri {R['guest_profile_days']} gün konaklama olmazsa anonimleştirilir",
      f"OTA yorumlarındaki yorum sahibi adı, yorum alındıktan {R['review_name_days']} gün sonra silinir; kanalda herkese açık olan yorum metni saklanır",
      f"Online check-in: kimlik belgesi görüntüsü hiçbir zaman saklanmaz. Misafir imzaları çıkıştan {R['signature_days']} gün sonra otomatik silinir. Kimlik belgesi bilgileri yalnızca otelin misafir kayıt (kimlik bildirimi) yükümlülükleri için gerektiği kadar saklanır; en geç otelin hesabıyla birlikte silinir",
      f"İşlem geçmişi {R['audit_days']} gün, uygulama içi bildirimler {R['notif_days']} gün saklanır",
      DELETION["tr"],
      "Fatura kayıtları vergi ve muhasebe mevzuatının gerektirdiği süre boyunca saklanır",
      "Kayıt ve güvenlik kayıtları dolandırıcılığı önlemek için sınırlı bir süre saklanır"])}
<h2>8. Güvenlik</h2><p>Veriler aktarım sırasında (TLS) ve depolamada şifrelenir. Erişim otele ve role göre sınırlandırılır: personel yalnız rolünün izin verdiği tesisleri ve özellikleri görür, önemli işlemler işlem geçmişine kaydedilir. Veritabanı sağlayıcımız SOC 2 Type 2 denetimlidir; kart ödemeleri PCI DSS Level 1 hizmet sağlayıcısı Stripe tarafından işlenir. Ayrıntılar <a href="{U("security")}">Güvenlik ve veri</a> sayfasında.</p>
<h2>9. Haklarınız</h2>
<p><strong>Türkiye (KVKK):</strong> 6698 sayılı Kanun’un 11. maddesi uyarınca verilerinizin işlenip işlenmediğini öğrenme, bilgi talep etme, düzeltme veya silme isteme ve otomatik işleme sonucu aleyhinize bir sonuca itiraz etme haklarınız vardır.</p>
<p><strong>AEA ve Birleşik Krallık:</strong> erişim, düzeltme, silme, kısıtlama ve taşınabilirlik talep edebilir, işlemeye itiraz edebilirsiniz. Yerel veri koruma otoritesine şikâyette de bulunabilirsiniz.</p>
<p><strong>Kaliforniya (CCPA/CPRA):</strong> kişisel bilgilerinizi öğrenme, sildirme ve düzeltme talebinde bulunabilirsiniz. Kişisel bilgi satmayız veya paylaşmayız; haklarınızı kullandığınız için size farklı davranmayız.</p>
<p>Haklarınızı kullanmak için <a href="mailto:{EMAIL}">{EMAIL}</a> adresine yazın. Hesabınızı kapatmak için <a href="{U("delacc")}">hesap silme</a> sayfasına bakın.</p>
<h2>10. Çerezler ve tarayıcı depolaması</h2><p>Panel, oturumunuzu açık tutmak için zorunlu çerez ve depolama kullanır. Sitemiz dil tercihinizi tarayıcınızın yerel depolamasında (localStorage) tutar. Pazarlama ölçümü için olağan ziyaretlerde hiçbir şey saklanmaz: yalnızca kampanya parametreleri (utm_source, utm_medium, utm_campaign, utm_term, utm_content veya reklam tıklama kimliği: gclid, msclkid, ttclid, fbclid) içeren bir bağlantıyla geldiğinizde site bu parametreleri, giriş sayfasının yolunu ve o ilk ziyaretin zamanını <code>hostlio_acq</code> anahtarıyla yerel depolamaya kaydeder. Bunun için çerez kullanılmaz. Yönlendiren sitenin alan adı yalnızca o sayfa görüntülemesi sırasında okunur, saklanmaz. Bu kayıt birinci taraf verisidir: site onu reklam ağlarıyla asla paylaşmaz; yalnızca kayıt veya iletişim formunu gönderirseniz o gönderimle birlikte bize iletilir ve 90 gün sonra otomatik olarak silinir. Hangi pazarlama kanallarının müşteri getirdiğini ölçmekteki meşru menfaatimize dayanırız; tarayıcınızda hostliopro.com için site verilerini temizleyerek dilediğiniz an itiraz edebilir ve kaydı silebilirsiniz. Reklam çerezi kullanmayız. Site analitiği eklersek önce bu politikayı güncelleriz.</p>
<h2>11. WhatsApp ve misafir mesajlaşması</h2><p>Hostlio Pro, oteller adına misafir mesajlarını göndermek ve almak için WhatsApp Business Platformu’na ve OTA gelen kutularına bağlanır. Misafir telefon numaraları yalnızca konaklamayla ilgili iletişim için kullanılır. Misafirler otele bildirerek mesaj almayı durdurabilir.</p>
<h2>12. Personel hesapları ve işlem geçmişi</h2><p>Hesap sahibi personel davet edebilir, her kişiye bir rol (yönetici, resepsiyon, kat hizmetleri, muhasebe veya izleyici) ve seçtiği tesislere erişim verebilir. Daveti göndermek için davet edilen kişinin e-posta adresini, kişi daveti kabul ettikten sonra da erişim sağlamak için adını, e-posta adresini, rolünü ve tesis erişimlerini kullanırız. Kimin davet edileceğine hesap sahibi karar verir; personeli işlemlerinin kayda alındığı konusunda bilgilendirmelidir.</p><p>İşlem geçmişi; rezervasyon oluşturma, değiştirme veya iptal etme, fiyat, oda, ayar veya ekip değişiklikleri ve yapay zekâ cevaplarının onaylanması ya da reddedilmesi gibi işlemleri; kullanıcı, rolü, zaman, kullanılan uygulama ve kısaltılmış IP adresiyle (IPv4 /24, IPv6 /48) birlikte kaydeder. Kayıtlar değiştirilemez, hesap sahibi ve yetkili roller tarafından görülebilir ve {R['audit_days']} gün sonra silinir.</p>
<h2>13. Yapay zekâ özellikleri (Lio)</h2>{_ul(["<strong>Misafirlere cevaplar:</strong> Lio cevap taslağı hazırlamak için misafirin mesajını, konuşmadaki önceki mesajları, misafirin rezervasyon bilgilerini (ad, tarihler, oda gibi) ve otelin bilgilerini yapay zekâ sağlayıcımıza gönderir. Hangi konuların otomatik cevaplanacağına, hangilerinin onay gerektireceğine otel karar verir",
      "<strong>Yorum cevapları:</strong> bu özelliği içeren planlarda Lio OTA yorumlarına cevap taslağı hazırlar. Hiçbir yorum cevabı otelin onayı olmadan gönderilmez",
      "<strong>Çeviri:</strong> otelin karşılama ve veda mesajı şablonları yapay zekâ ile çevrilebilir",
      "<strong>Lio Önerileri:</strong> Pro ve Growth planlarında yeni misafir mesajları ve yorumlar günde bir kez tekrarlayan konular (ör. temizlik, Wi-Fi) için incelenir. Metin gönderilmeden önce e-posta adresleri, telefon numaraları, web bağlantıları, rezervasyon veya kart numarası gibi uzun sayılar ve misafirin adı otomatik olarak maskelenir. Sonuçlar kişi adı, oda numarası, tarih veya iletişim bilgisi içermeyen kısa ve genel özetlerdir; orijinal metinler önerilerle birlikte veya kayıtlarımızda saklanmaz. İsteğe bağlı haftalık özet yalnız bu konular ve istatistiklerden, misafir metni kullanılmadan yazılır. Otel, Lio Önerileri’nin yapay zekâ bölümünü ayarlarından kapatabilir"])}
<h2>14. Çocuklar</h2><p>Hostlio Pro bir işletme hizmetidir ve 16 yaşından küçüklere yönelik değildir.</p>
<h2>15. Değişiklikler</h2><p>Değişiklikleri bu sayfada yayınlar ve yukarıdaki tarihi güncelleriz. Önemli değişiklikleri ayrıca e-posta veya panel üzerinden bildiririz.</p>
<h2>16. İletişim</h2>{_ul([f'E-posta: <a href="mailto:{EMAIL}">{EMAIL}</a>', f"Adres: {ADDR}"])}'''

# ------------------------------------------------------------------ terms
def terms_en(U, EMAIL, ADDR):
    Q = quota("en")
    return f'''<p>These Terms of Service (“Terms”) govern your use of Hostlio Pro, operated by Loti Members LLC (“we”, “us”). By creating an account or using the service you agree to these Terms. If you use Hostlio Pro for a business, you accept them on its behalf.</p>
<h2>1. The service</h2><p>Hostlio Pro is cloud software for hotels: AI guest messaging (Lio), a channel manager, a reservation calendar, online check-in and related tools, available by subscription through the website, the dashboard and the mobile app.</p>
<h2>2. Your account</h2><p>You must give accurate information and keep your login details secure. You are responsible for everything done under your account, including by your staff. The account owner can invite staff, give them roles and property access, and remove them at any time; the owner decides who has access. Actions in the dashboard and app are recorded in an activity log, as described in our <a href="{U("privacy")}">Privacy Policy</a>.</p>
<h2>3. Free trial, payment and automatic renewal</h2>
{_ul(["Every plan starts with a 7-day free trial. A payment card is collected at signup through Stripe",
      "<strong>Unless you cancel before the trial ends, your card is charged automatically for the plan and billing period you chose when the trial ends</strong>",
      "Subscriptions are paid in advance and <strong>renew automatically</strong> at the end of each monthly or annual period until cancelled. We charge the card on file at each renewal",
      "<strong>Plan changes:</strong> you can switch to another plan or billing period at any time from the billing page. <strong>The change takes effect immediately.</strong> The price difference for the rest of the current period is prorated: moving to a higher plan adds a prorated charge and moving to a lower plan a prorated credit, both settled on your next invoice. Switching between monthly and annual billing starts a new billing period at once and is invoiced immediately, with credit for the unused part of the previous period. If a payment needed for the change fails, the change is not applied",
      f'Prices are in US dollars and exclude taxes. Current plans and prices are on our <a href="{U("pricing")}">pricing page</a>. Annual billing costs 20% less than paying monthly',
      "<strong>Early-bird price:</strong> the first 50 customers keep their early-bird price for as long as their subscription stays active without interruption. If the subscription is cancelled or lapses, the early-bird price ends and current prices apply to any new subscription",
      "We may change prices for future periods with at least 30 days’ notice by email; the new price applies from your next renewal"])}
<h2>4. Plan limits and AI message quota</h2><p>Each plan includes a monthly quota of AI messages (Starter {Q["starter"]}, Pro {Q["pro"]}, Growth {Q["growth"]}) and a maximum number of properties and rooms. We notify you when you reach 80% of the quota. <strong>Automatic AI replies pause once usage passes 110% of the monthly quota</strong> and resume at the start of the next period or when you upgrade. Guest messages keep arriving in your inbox so you can reply yourself.</p>
<h2>5. Cancellation and refunds</h2><p>You can cancel at any time from the billing page of the dashboard or by emailing {EMAIL}. Cancelling during the trial means you are not charged. Otherwise cancellation takes effect at the end of the current paid period and the service stays available until then. We do not refund partial periods, except where the law requires it. {DELETION_CANCEL["en"]}</p>
<h2>6. Acceptable use</h2><p>You agree not to:</p>
{_ul(["use the service for anything unlawful, or to send spam or unsolicited messages to guests",
      "break the terms of OTAs, Meta/WhatsApp or other connected platforms through our integrations",
      "try to gain unauthorised access to our systems or other customers’ data",
      "resell or sublicense the service without our written permission"])}
<h2>7. Guest data and your responsibilities</h2><p>You are the controller of your guests’ personal data. You are responsible for having a lawful basis to process it, informing guests (for example in your own privacy notice) and meeting guest-registration and identity-document rules that apply to your property. Our <a href="{U("dpa")}">Data Processing Addendum</a> forms part of these Terms and applies to the guest data we process for you.</p>
<h2>8. AI-generated replies</h2><p>Lio drafts and sends replies using the information you provide. AI can make mistakes. You decide which messages Lio may answer automatically and which need approval, and you remain responsible for the replies sent on behalf of your property. Lio hands over messages it is not sure about, but you should not rely on it for legal, medical or emergency matters. Replies to OTA reviews are only sent after you approve them. Lio Suggestions, analytics and reports are suggestions and summaries based on your data; you decide whether to act on them and we do not guarantee any result. To the extent permitted by law, we are not liable for the content of AI-generated replies or suggestions.</p>
<h2>9. Connected channels and WhatsApp</h2><p>Channel connections are provided through our connectivity partner Channex, and messaging through the WhatsApp Business Platform and OTA inboxes. You must follow the terms of each platform you connect. Changes to third-party APIs or policies can affect features, and we are not responsible for them.</p>
<h2>10. Your data</h2><p>You own your data. We process it only to provide the service, as described in our <a href="{U("privacy")}">Privacy Policy</a> and the DPA. You can export your data while your account is active. {DELETION_T["en"].format(u=U("delacc"))}</p>
<h2>11. Availability</h2><p>We aim for high availability but do not guarantee uninterrupted service. We announce planned maintenance in advance where possible.</p>
<h2>12. Intellectual property</h2><p>Hostlio Pro, its software and content belong to Loti Members LLC. You may not copy, modify or distribute any part of the service without written permission.</p>
<h2>13. Limitation of liability</h2><p>To the maximum extent permitted by law, we are not liable for indirect, incidental, special or consequential damages, or for lost profits or data. Our total liability for any claim is limited to the fees you paid us in the 12 months before the claim.</p>
<h2>14. Governing law</h2><p>These Terms are governed by the laws of the State of California, USA. Disputes will be resolved in the courts of Sacramento County, California, unless mandatory consumer or local law gives you other rights.</p>
<h2>15. Changes to these Terms</h2><p>We will notify you of material changes by email or in the dashboard at least 30 days before they apply. Continuing to use the service after that date means you accept the updated Terms.</p>
<h2>16. Contact</h2>{_ul([f'Email: <a href="mailto:{EMAIL}">{EMAIL}</a>', f"Address: {ADDR}"])}'''

def terms_tr(U, EMAIL, ADDR):
    Q = quota("tr")
    return f'''<p>Bu Kullanım Şartları (“Şartlar”), Loti Members LLC (“biz”) tarafından işletilen Hostlio Pro’yu kullanımınızı düzenler. Hesap oluşturarak veya hizmeti kullanarak bu Şartları kabul edersiniz. Hostlio Pro’yu bir işletme adına kullanıyorsanız Şartları o işletme adına kabul etmiş olursunuz.</p>
<h2>1. Hizmet</h2><p>Hostlio Pro oteller için bulut yazılımıdır: yapay zekâ ile misafir mesajlaşması (Lio), kanal yöneticisi, rezervasyon takvimi, online check-in ve ilgili araçlar; web sitesi, panel ve mobil uygulama üzerinden abonelikle sunulur.</p>
<h2>2. Hesabınız</h2><p>Doğru bilgi vermeli ve giriş bilgilerinizi güvende tutmalısınız. Çalışanlarınız dahil, hesabınız altında yapılan her işlemden siz sorumlusunuz. Hesap sahibi personel davet edebilir, onlara rol ve tesis erişimi verebilir ve istediği an kaldırabilir; kimin erişeceğine hesap sahibi karar verir. Panelde ve uygulamada yapılan işlemler <a href="{U("privacy")}">Gizlilik Politikamızda</a> anlatıldığı şekilde işlem geçmişine kaydedilir.</p>
<h2>3. Ücretsiz deneme, ödeme ve otomatik yenileme</h2>
{_ul(["Her plan 7 günlük ücretsiz denemeyle başlar. Kayıt sırasında Stripe üzerinden bir ödeme kartı alınır",
      "<strong>Deneme bitmeden iptal etmezseniz, deneme sonunda seçtiğiniz plan ve fatura dönemi için kartınızdan otomatik olarak ücret alınır</strong>",
      "Abonelikler peşin ödenir ve iptal edilene kadar her aylık veya yıllık dönemin sonunda <strong>otomatik olarak yenilenir</strong>. Her yenilemede kayıtlı karttan ücret alınır",
      "<strong>Plan değişikliği:</strong> faturalandırma sayfasından istediğiniz zaman başka bir plana veya fatura dönemine geçebilirsiniz. <strong>Değişiklik hemen geçerli olur.</strong> İçinde bulunulan dönemin kalan kısmı için fiyat farkı kıst (orantılı) hesaplanır: üst plana geçişte orantılı ek ücret, alt plana geçişte orantılı alacak oluşur; ikisi de bir sonraki faturanıza yansır. Aylık ile yıllık ödeme arasında geçiş yeni bir fatura dönemini hemen başlatır ve önceki dönemin kullanılmayan kısmı düşülerek hemen faturalanır. Değişiklik için gereken ödeme alınamazsa değişiklik uygulanmaz",
      f'Fiyatlar ABD doları cinsindendir, vergiler hariçtir. Güncel planlar ve fiyatlar <a href="{U("pricing")}">fiyatlandırma sayfamızda</a>. Yıllık ödeme, aylık ödemeye göre %20 daha ucuzdur',
      "<strong>Erken kayıt (Early Bird) fiyatı:</strong> ilk 50 müşteri, aboneliği kesintisiz devam ettiği sürece erken kayıt fiyatını korur. Abonelik iptal edilir veya süresi dolarsa erken kayıt fiyatı sona erer; yeni abonelikte güncel fiyatlar geçerlidir",
      "Gelecek dönemlerin fiyatlarını en az 30 gün önceden e-postayla bildirerek değiştirebiliriz; yeni fiyat bir sonraki yenilemeden itibaren uygulanır"])}
<h2>4. Plan limitleri ve AI mesaj kotası</h2><p>Her plan aylık bir AI mesaj kotası (Starter {Q["starter"]}, Pro {Q["pro"]}, Growth {Q["growth"]}) ve azami tesis ve oda sayısı içerir. Kotanın %80’ine ulaştığınızda sizi bilgilendiririz. <strong>Kullanım aylık kotanın %110’unu geçtiğinde otomatik AI cevapları durur</strong>; bir sonraki dönemin başında veya planınızı yükselttiğinizde yeniden başlar. Misafir mesajları gelen kutunuza gelmeye devam eder, kendiniz cevaplayabilirsiniz.</p>
<h2>5. İptal ve iade</h2><p>İstediğiniz zaman panelin faturalandırma sayfasından veya {EMAIL} adresine yazarak iptal edebilirsiniz. Deneme sırasında iptal ederseniz ücret alınmaz. Aksi halde iptal, ödenmiş dönemin sonunda geçerli olur ve hizmet o güne kadar açık kalır. Kanunun zorunlu kıldığı haller dışında kısmi dönem iadesi yapılmaz. {DELETION_CANCEL["tr"]}</p>
<h2>6. Kabul edilebilir kullanım</h2><p>Şunları yapmamayı kabul edersiniz:</p>
{_ul(["hizmeti hukuka aykırı amaçlarla kullanmak, misafirlere spam veya istenmeyen mesaj göndermek",
      "entegrasyonlarımız üzerinden OTA’ların, Meta/WhatsApp’ın veya bağlı diğer platformların şartlarını ihlal etmek",
      "sistemlerimize veya diğer müşterilerin verilerine yetkisiz erişmeye çalışmak",
      "hizmeti yazılı iznimiz olmadan yeniden satmak veya alt lisanslamak"])}
<h2>7. Misafir verileri ve sorumluluklarınız</h2><p>Misafirlerinizin kişisel verilerinin veri sorumlusu sizsiniz. Bu verileri işlemek için hukuki sebebe sahip olmak, misafirleri bilgilendirmek (ör. kendi aydınlatma metninizle) ve tesisiniz için geçerli misafir kayıt ve kimlik belgesi kurallarına uymak sizin sorumluluğunuzdadır. <a href="{U("dpa")}">Veri İşleme Sözleşmemiz (DPA)</a> bu Şartların parçasıdır ve sizin adınıza işlediğimiz misafir verilerine uygulanır.</p>
<h2>8. Yapay zekâ cevapları</h2><p>Lio, verdiğiniz bilgileri kullanarak cevap hazırlar ve gönderir. Yapay zekâ hata yapabilir. Lio’nun hangi mesajlara otomatik cevap vereceğine, hangilerinin onay gerektireceğine siz karar verirsiniz ve tesisiniz adına gönderilen cevaplardan siz sorumlu olursunuz. Lio emin olmadığı mesajları size devreder; yine de hukuki, tıbbi veya acil konularda ona güvenmemelisiniz. OTA yorumlarına cevaplar yalnızca siz onayladıktan sonra gönderilir. Lio Önerileri, analizler ve raporlar verilerinize dayanan öneri ve özetlerdir; bunlara göre hareket edip etmeyeceğinize siz karar verirsiniz ve herhangi bir sonucu garanti etmeyiz. Kanunun izin verdiği ölçüde yapay zekâ cevaplarının ve önerilerinin içeriğinden sorumlu değiliz.</p>
<h2>9. Bağlı kanallar ve WhatsApp</h2><p>Kanal bağlantıları bağlantı ortağımız Channex üzerinden; mesajlaşma ise WhatsApp Business Platformu ve OTA gelen kutuları üzerinden sağlanır. Bağladığınız her platformun şartlarına uymalısınız. Üçüncü taraf API veya politikalarındaki değişiklikler özellikleri etkileyebilir; bunlardan sorumlu değiliz.</p>
<h2>10. Verileriniz</h2><p>Verileriniz size aittir. Onları yalnızca hizmeti sunmak için, <a href="{U("privacy")}">Gizlilik Politikamız</a> ve DPA’da anlatıldığı şekilde işleriz. Hesabınız açıkken verilerinizi dışa aktarabilirsiniz. {DELETION_T["tr"].format(u=U("delacc"))}</p>
<h2>11. Hizmet sürekliliği</h2><p>Yüksek erişilebilirlik hedefleriz ancak kesintisiz hizmet garanti etmeyiz. Planlı bakımları mümkün olduğunca önceden duyururuz.</p>
<h2>12. Fikri mülkiyet</h2><p>Hostlio Pro, yazılımı ve içerikleri Loti Members LLC’ye aittir. Hizmetin herhangi bir bölümünü yazılı izin olmadan kopyalayamaz, değiştiremez veya dağıtamazsınız.</p>
<h2>13. Sorumluluğun sınırlandırılması</h2><p>Kanunun izin verdiği azami ölçüde dolaylı, arızi, özel veya sonuçsal zararlardan, kâr veya veri kaybından sorumlu değiliz. Herhangi bir talep için toplam sorumluluğumuz, talepten önceki 12 ayda bize ödediğiniz ücretlerle sınırlıdır.</p>
<h2>14. Uygulanacak hukuk</h2><p>Bu Şartlar ABD’nin Kaliforniya Eyaleti hukukuna tabidir. Emredici tüketici veya yerel mevzuat size başka haklar tanımadıkça uyuşmazlıklar Kaliforniya, Sacramento County mahkemelerinde çözülür.</p>
<h2>15. Şartlardaki değişiklikler</h2><p>Önemli değişiklikleri yürürlüğe girmeden en az 30 gün önce e-posta veya panel üzerinden bildiririz. O tarihten sonra hizmeti kullanmaya devam etmeniz güncel Şartları kabul ettiğiniz anlamına gelir.</p>
<h2>16. İletişim</h2>{_ul([f'E-posta: <a href="mailto:{EMAIL}">{EMAIL}</a>', f"Adres: {ADDR}"])}'''
