"""GA4 + çerez izni: altbilgi düğmesi etiketi ve gizlilik politikasının analitik paragrafı (6 dil).

Yalnız build.GA4_ID doluyken kullanılır. GA4_ID boşken gizlilik politikası olduğu gibi kalır (orada
"Site analitiği eklersek önce bu politikayı güncelleriz" yazıyor — dormant durumda doğru).

TASLAK (8 Ekim 2026): hukuki metin sahip/avukat gözden geçirmesi bekliyor (GA4_ID sahip isteğiyle aynı gün
dolduruldu, metin bu yüzden yayında; değişiklik gerekirse yalnız GA4_TEXT güncellenir).
Hukuk dalı (site-hukuk) legal_v6*.py dosyalarını değiştirebilir; bu modül o dosyalara dokunmaz,
çerez bölümünü başlığından ("Cookie"/"Çerez" geçen h2) bulup paragrafı ekler. Başlık bulunamazsa
build hata verir (GA4 açıkken politika sessizce eski kalmasın).
"""
import re

FOOT_LABEL = {"tr": "Çerez tercihleri", "en": "Cookie preferences", "es": "Preferencias de cookies",
              "it": "Preferenze cookie", "pt": "Preferências de cookies", "fr": "Préférences cookies"}

# Gizlilik politikasının çerez bölümünün son cümlesi — GA4 açılınca artık doğru değil, kaldırılır.
OLD_SENTENCE = {
    "en": " If we add website analytics, we will update this policy first.",
    "tr": " Site analitiği eklersek önce bu politikayı güncelleriz.",
    "es": " Si añadimos analítica web, actualizaremos antes esta política.",
    "it": " Se aggiungeremo strumenti di analisi, aggiorneremo prima questa informativa.",
    "pt": " Se adicionarmos análise de tráfego, atualizaremos esta política antes.",
    "fr": " Si nous ajoutons un outil d’analyse, nous mettrons d’abord cette politique à jour.",
}

GA4_TEXT = {
 "en": ("Website analytics (Google Analytics 4) — only with your consent",
  "If you choose “Accept” in the cookie banner, we use Google Analytics 4 (provided by Google LLC) to understand how our website is used and to improve it. It records pages viewed, the referring website, device and browser type, approximate location (country/city) and interactions such as clicks on signup buttons, signup form steps, contact form submissions and the monthly/annual price switch. We never send names, email addresses, phone numbers, hotel names or other form contents to Google.",
  "Google Analytics then sets first-party cookies (<code>_ga</code>, <code>_ga_&lt;ID&gt;</code>) that expire after up to 2 years. Google Analytics 4 does not log or store IP addresses; Google uses the IP address only briefly to derive the approximate location and then discards it. We keep analytics event data for 14 months, have switched off Google signals and ad personalisation, and do not use this data for advertising.",
  "Google acts as our processor under its data processing terms. Data may be processed in the United States; Google LLC is certified under the EU–US Data Privacy Framework, and Standard Contractual Clauses also apply. Legal basis: your consent (GDPR Art. 6(1)(a); for Türkiye, your explicit consent under KVKK, including for the transfer abroad). Without your consent Google Analytics is not loaded and no request is sent to Google.",
  "Your choice is saved for 6 months in your browser’s local storage under the key <code>hostlio_consent</code> (no cookie). You can withdraw or change it at any time with “Cookie preferences” at the bottom of every page or the button below; withdrawing deletes the Google Analytics cookies."),
 "tr": ("Site analitiği (Google Analytics 4) — yalnızca izninizle",
  "Çerez bandında “Kabul et”i seçerseniz, sitemizin nasıl kullanıldığını anlamak ve geliştirmek için Google Analytics 4’ü (sağlayıcı: Google LLC) kullanırız. Görüntülenen sayfalar, yönlendiren site, cihaz ve tarayıcı türü, yaklaşık konum (ülke/şehir) ile kayıt düğmesi tıklamaları, kayıt formu adımları, iletişim formu gönderimi ve aylık/yıllık fiyat geçişi gibi etkileşimler kaydedilir. Ad, e-posta adresi, telefon, otel adı veya başka form içeriklerini Google’a asla göndermeyiz.",
  "Bu durumda Google Analytics en fazla 2 yıl süreli birinci taraf çerezleri (<code>_ga</code>, <code>_ga_&lt;ID&gt;</code>) yerleştirir. Google Analytics 4 IP adreslerini kaydetmez veya saklamaz; Google IP adresini yalnızca yaklaşık konumu belirlemek için kısa süre kullanır ve ardından siler. Analitik olay verilerini 14 ay saklarız; Google sinyallerini ve reklam kişiselleştirmesini kapattık, bu verileri reklam için kullanmayız.",
  "Google, veri işleme koşulları kapsamında veri işleyenimiz olarak hareket eder. Veriler Amerika Birleşik Devletleri’nde işlenebilir; Google LLC, AB–ABD Veri Gizliliği Çerçevesi’ne sertifikalıdır ve ayrıca Standart Sözleşme Maddeleri uygulanır. Hukuki dayanak: açık rızanız (KVKK; yurt dışına aktarım dahil) ve AEA/Birleşik Krallık için GDPR md. 6(1)(a). İzniniz olmadan Google Analytics yüklenmez ve Google’a hiçbir istek gönderilmez.",
  "Seçiminiz tarayıcınızın yerel depolamasında <code>hostlio_consent</code> anahtarıyla 6 ay saklanır (çerez kullanılmaz). Her sayfanın altındaki “Çerez tercihleri” bağlantısıyla veya aşağıdaki düğmeyle izninizi dilediğiniz an geri alabilir ya da değiştirebilirsiniz; geri aldığınızda Google Analytics çerezleri silinir."),
 "es": ("Analítica web (Google Analytics 4): solo con tu consentimiento",
  "Si eliges «Aceptar» en el aviso de cookies, usamos Google Analytics 4 (proporcionado por Google LLC) para entender cómo se usa nuestro sitio y mejorarlo. Registra las páginas vistas, el sitio de procedencia, el tipo de dispositivo y navegador, la ubicación aproximada (país/ciudad) e interacciones como clics en los botones de registro, pasos del formulario de registro, envíos del formulario de contacto y el cambio de precio mensual/anual. Nunca enviamos a Google nombres, correos electrónicos, teléfonos, nombres de hotel ni otros contenidos de formularios.",
  "En ese caso, Google Analytics instala cookies propias (<code>_ga</code>, <code>_ga_&lt;ID&gt;</code>) que caducan en un máximo de 2 años. Google Analytics 4 no registra ni almacena direcciones IP; Google usa la IP solo brevemente para deducir la ubicación aproximada y después la descarta. Conservamos los datos de eventos de analítica durante 14 meses, hemos desactivado Google Signals y la personalización de anuncios, y no usamos estos datos con fines publicitarios.",
  "Google actúa como nuestro encargado del tratamiento según sus condiciones de tratamiento de datos. Los datos pueden tratarse en Estados Unidos; Google LLC está certificada en el Marco de Privacidad de Datos UE-EE. UU. y además se aplican Cláusulas Contractuales Tipo. Base jurídica: tu consentimiento (art. 6.1.a RGPD; en Turquía, tu consentimiento explícito según la KVKK, también para la transferencia internacional). Sin tu consentimiento, Google Analytics no se carga y no se envía ninguna solicitud a Google.",
  "Tu elección se guarda durante 6 meses en el almacenamiento local del navegador con la clave <code>hostlio_consent</code> (sin cookie). Puedes retirarla o cambiarla cuando quieras en «Preferencias de cookies», al pie de cada página, o con el botón de abajo; al retirarla se eliminan las cookies de Google Analytics."),
 "it": ("Analisi del sito (Google Analytics 4): solo con il tuo consenso",
  "Se scegli «Accetta» nel banner dei cookie, usiamo Google Analytics 4 (fornito da Google LLC) per capire come viene usato il sito e migliorarlo. Registra le pagine visitate, il sito di provenienza, il tipo di dispositivo e di browser, la posizione approssimativa (paese/città) e interazioni come i clic sui pulsanti di registrazione, i passaggi del modulo di registrazione, l’invio del modulo di contatto e il passaggio tra prezzo mensile e annuale. Non inviamo mai a Google nomi, indirizzi email, numeri di telefono, nomi di hotel o altri contenuti dei moduli.",
  "In tal caso Google Analytics imposta cookie di prima parte (<code>_ga</code>, <code>_ga_&lt;ID&gt;</code>) che scadono al massimo dopo 2 anni. Google Analytics 4 non registra né conserva gli indirizzi IP; Google usa l’IP solo per un breve momento per ricavare la posizione approssimativa e poi lo elimina. Conserviamo i dati sugli eventi per 14 mesi, abbiamo disattivato Google Signals e la personalizzazione degli annunci e non usiamo questi dati a fini pubblicitari.",
  "Google agisce come nostro responsabile del trattamento in base ai propri termini sul trattamento dei dati. I dati possono essere trattati negli Stati Uniti; Google LLC è certificata nell’ambito del Data Privacy Framework UE-USA e si applicano inoltre le Clausole contrattuali standard. Base giuridica: il tuo consenso (art. 6, par. 1, lett. a GDPR; per la Turchia, il consenso esplicito ai sensi della KVKK, anche per il trasferimento all’estero). Senza il tuo consenso Google Analytics non viene caricato e nessuna richiesta viene inviata a Google.",
  "La tua scelta viene salvata per 6 mesi nell’archiviazione locale del browser con la chiave <code>hostlio_consent</code> (nessun cookie). Puoi revocarla o modificarla in qualsiasi momento da «Preferenze cookie», in fondo a ogni pagina, o con il pulsante qui sotto; con la revoca i cookie di Google Analytics vengono eliminati."),
 "pt": ("Análise do site (Google Analytics 4): só com o seu consentimento",
  "Se você escolher “Aceitar” no aviso de cookies, usamos o Google Analytics 4 (fornecido pela Google LLC) para entender como o site é usado e melhorá-lo. São registradas as páginas vistas, o site de origem, o tipo de dispositivo e navegador, a localização aproximada (país/cidade) e interações como cliques nos botões de cadastro, etapas do formulário de cadastro, envios do formulário de contato e a troca entre preço mensal e anual. Nunca enviamos ao Google nomes, e-mails, telefones, nomes de hotel ou outros conteúdos de formulários.",
  "Nesse caso, o Google Analytics grava cookies próprios (<code>_ga</code>, <code>_ga_&lt;ID&gt;</code>) que expiram em no máximo 2 anos. O Google Analytics 4 não registra nem armazena endereços IP; o Google usa o IP apenas por um instante para estimar a localização aproximada e depois o descarta. Guardamos os dados de eventos de análise por 14 meses, desativamos os Indicadores do Google (Google Signals) e a personalização de anúncios, e não usamos esses dados para publicidade.",
  "O Google atua como nosso operador, conforme seus termos de processamento de dados. Os dados podem ser tratados nos Estados Unidos; a Google LLC é certificada no Data Privacy Framework UE-EUA e também se aplicam Cláusulas Contratuais Padrão. Base legal: o seu consentimento (LGPD art. 7º, I; RGPD art. 6.º, n.º 1, al. a; na Turquia, consentimento explícito nos termos da KVKK, inclusive para a transferência internacional). Sem o seu consentimento, o Google Analytics não é carregado e nenhuma solicitação é enviada ao Google.",
  "Sua escolha fica salva por 6 meses no armazenamento local do navegador, com a chave <code>hostlio_consent</code> (sem cookie). Você pode retirá-la ou alterá-la a qualquer momento em “Preferências de cookies”, no rodapé de cada página, ou no botão abaixo; ao retirá-la, os cookies do Google Analytics são apagados."),
 "fr": ("Mesure d’audience (Google Analytics 4) : uniquement avec votre accord",
  "Si vous choisissez « Accepter » dans le bandeau cookies, nous utilisons Google Analytics 4 (fourni par Google LLC) pour comprendre comment notre site est utilisé et l’améliorer. Sont enregistrés les pages vues, le site de provenance, le type d’appareil et de navigateur, la localisation approximative (pays/ville) et des interactions comme les clics sur les boutons d’inscription, les étapes du formulaire d’inscription, l’envoi du formulaire de contact et le passage entre tarif mensuel et annuel. Nous n’envoyons jamais à Google de noms, adresses e-mail, numéros de téléphone, noms d’hôtel ni autres contenus de formulaires.",
  "Google Analytics dépose alors des cookies internes (<code>_ga</code>, <code>_ga_&lt;ID&gt;</code>) qui expirent au plus tard après 2 ans. Google Analytics 4 n’enregistre ni ne conserve les adresses IP ; Google utilise l’adresse IP uniquement un court instant pour en déduire la localisation approximative, puis la supprime. Nous conservons les données d’événements pendant 14 mois, avons désactivé Google Signals et la personnalisation des annonces, et n’utilisons pas ces données à des fins publicitaires.",
  "Google agit en tant que sous-traitant selon ses conditions de traitement des données. Les données peuvent être traitées aux États-Unis ; Google LLC est certifiée au titre du Data Privacy Framework UE–États-Unis et des clauses contractuelles types s’appliquent également. Base légale : votre consentement (art. 6, § 1, a) du RGPD ; pour la Turquie, votre consentement explicite au sens de la KVKK, y compris pour le transfert à l’étranger). Sans votre accord, Google Analytics n’est pas chargé et aucune requête n’est envoyée à Google.",
  "Votre choix est conservé 6 mois dans le stockage local de votre navigateur sous la clé <code>hostlio_consent</code> (aucun cookie). Vous pouvez le retirer ou le modifier à tout moment via « Préférences cookies » en bas de chaque page ou avec le bouton ci-dessous ; le retrait supprime les cookies Google Analytics."),
}


def foot_button(lang, cls="linkbtn"):
    """Altbilgi "Çerez tercihleri" düğmesi; consent.js görünür yapar (JS yoksa GA da yok → gizli kalır)."""
    return f'<button type="button" class="{cls}" data-consent-open hidden>{FOOT_LABEL[lang]}</button>'


def privacy_patch(body, lang):
    """Gizlilik politikasının çerez bölümüne GA4 paragrafını ekler, h2'ye id="cookies" verir (banttaki
    bağlantı #cookies'e gider) ve "analitik eklersek güncelleriz" cümlesini kaldırır."""
    m = re.search(r'<h2([^>]*)>([^<]*(?:Cookie|Çerez)[^<]*)</h2>\s*<p>(.*?)</p>', body, re.S)
    if not m:
        raise SystemExit(f"analytics_consent: {lang} gizlilik politikasında çerez bölümü bulunamadı (GA4_ID dolu)")
    attrs = m.group(1) if "id=" in m.group(1) else m.group(1) + ' id="cookies"'
    para = m.group(3).replace(OLD_SENTENCE[lang], "")
    h, *ps = GA4_TEXT[lang]
    extra = (f'<h3>{h}</h3>' + "".join(f"<p>{p}</p>" for p in ps)
             + f'<p>{foot_button(lang, "btn btn-ghost")}</p>')
    return body[:m.start()] + f'<h2{attrs}>{m.group(2)}</h2><p>{para}</p>' + extra + body[m.end():]
