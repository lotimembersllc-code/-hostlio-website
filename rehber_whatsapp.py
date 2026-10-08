"""WhatsApp for hotels — mevcut EN yazısı (post-whatsapp, eski adres korunur) genişletildi; SEO fikri #14 için
ES/IT/FR sürümleri aynı anahtar altında (hreflang kümesi). Tur 2, 8 Ekim 2026.

Meta kuralları YALNIZ resmî Meta sayfalarından (8 Ekim 2026 erişim; SRC listesi). Önemli: 1 Ekim 2026'dan beri Meta
24 saatlik pencere içindeki servis mesajlarını da mesaj başına ücretlendiriyor (pricing/non-template-messages);
eski fiyat sayfası hâlâ "ücretsiz" diyor — "ücretsiz" YAZMAYIN. Mesaj limiti kademeleri 250/2.000/10.000/100.000/sınırsız,
işletme portföyü düzeyinde (8 Ekim 2025 değişikliği).

Hostlio iddiaları kodla doğrulandı (backend + panel main, 8 Ekim 2026):
- Otel KENDİ numarasını panelden Meta'nın resmî kayıt akışıyla (Embedded Signup, Cloud API) bağlar; tüm planlar; yalnız hesap sahibi.
- Giden şablon mesajı CANLI DEĞİL (otomatik mesaj bayrağı kapalı) ⇒ Lio yalnız 24 saatlik pencere içinde cevap verir;
  pencere kapalıysa panel "24 saatlik pencere kapandı" uyarısı gösterir. Otomatik karşılama/hatırlatma YAZILMADI.
- Lio misafirin dilinde cevaplar; elle yazılan cevaplar çevrilmez. Modlar: tam otomatik / karma (varsayılan) / yalnız taslak;
  indirim, iade, şikâyet, rezervasyon konuları varsayılan olarak onaya gelir.
- Rezervasyon talebi (Pro+) onayla; OTA gelen kutuları Pro+; kota %80 panel uyarısı, %100 e-posta, ~%110 durur.
- WhatsApp Coexistence BİLEREK YAZILMADI (D9). "30+ dil" eklenmedi.
"""
import html

SRC = [
 ("WhatsApp Business: FAQ (app vs Platform)", "https://whatsappbusiness.com/resources/faq/"),
 ("WhatsApp Business Platform overview", "https://whatsappbusiness.com/products/business-platform/"),
 ("Meta for Developers: Cloud API overview", "https://developers.facebook.com/docs/whatsapp/cloud-api/overview"),
 ("Meta for Developers: On-Premises API sunset", "https://developers.facebook.com/docs/whatsapp/on-premises/sunset"),
 ("Meta for Developers: Sending messages (customer service window)", "https://developers.facebook.com/docs/whatsapp/cloud-api/guides/send-messages"),
 ("Meta for Developers: Message templates", "https://developers.facebook.com/docs/whatsapp/business-management-api/message-templates"),
 ("Meta for Developers: Pricing for non-template messages", "https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing/non-template-messages"),
 ("Meta for Developers: WhatsApp changelog", "https://developers.facebook.com/documentation/business-messaging/whatsapp/changelog"),
 ("Meta for Developers: Messaging limits", "https://developers.facebook.com/documentation/business-messaging/whatsapp/messaging-limits"),
 ("Meta for Developers: Business phone numbers", "https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers"),
 ("WhatsApp Business Messaging Policy", "https://whatsappbusiness.com/policy/"),
 ("Meta Terms for WhatsApp Business Platform", "https://www.facebook.com/legal/Meta-Terms-for-WhatsApp-Business-Platform"),
]
SRC_H = {"en": ("Sources", "All sources accessed 8 October 2026. Meta changes its rules and prices regularly; check the linked pages before you rely on a detail."),
         "es": ("Fuentes", "Consultadas el 8 de octubre de 2026. Meta cambia sus normas y precios con frecuencia; revisa las páginas enlazadas antes de basarte en un detalle."),
         "it": ("Fonti", "Consultate l'8 ottobre 2026. Meta cambia spesso regole e prezzi: verifica le pagine collegate prima di basarti su un dettaglio."),
         "fr": ("Sources", "Consultées le 8 octobre 2026. Meta modifie régulièrement ses règles et ses prix : vérifiez les pages citées avant de vous appuyer sur un détail.")}


def _tbl(head, rows):
    h = "".join(f"<th>{x}</th>" for x in head)
    b = "".join("<tr>" + f'<th scope="row">{r[0]}</th>' + "".join(f"<td>{c}</td>" for c in r[1:]) + "</tr>" for r in rows)
    return f'<div class="table-wrap"><table><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table></div>'


def _src(L):
    h, note = SRC_H[L]
    lis = "".join(f'<li><a href="{u}" rel="nofollow noopener">{html.escape(n)}</a></li>' for n, u in SRC)
    return f'<h2>{h}</h2><p class="small muted">{note}</p><ul>{lis}</ul>'


META = {
 "en": dict(key="post-whatsapp", date="2026-05-01", title="WhatsApp for hotels: setup, Meta's rules and AI replies (2026)",
            desc="WhatsApp for hotels in 2026: Business app or API, the 24-hour window, templates, opt-in, Meta's pricing, and what an AI assistant can and can't do."),
 "es": dict(key="post-whatsapp", date="2026-10-08", title="WhatsApp para hoteles: configuración, normas de Meta e IA (2026)",
            desc="WhatsApp para hoteles en 2026: app Business o API, la ventana de 24 horas, plantillas, consentimiento, precios de Meta y lo que puede hacer un asistente de IA."),
 "it": dict(key="post-whatsapp", date="2026-10-08", title="WhatsApp per hotel: configurazione, regole di Meta e AI (2026)",
            desc="WhatsApp per hotel nel 2026: app Business o API, finestra di 24 ore, modelli, consenso, prezzi di Meta e cosa può (e non può) fare un assistente AI."),
 "fr": dict(key="post-whatsapp", date="2026-10-08", title="WhatsApp pour hôtels : mise en place, règles de Meta et IA (2026)",
            desc="WhatsApp pour les hôtels en 2026 : app Business ou API, fenêtre de 24 heures, modèles, consentement, tarifs de Meta et ce que peut faire un assistant IA."),
}


def en(U):
    c = f'''<div class="answer"><p><strong>Short answer:</strong> WhatsApp works well for hotels because guests already use it and reply quickly. A small property can start with the free WhatsApp Business app on one phone. Once several people need to answer, or you want automatic replies and a link to your reservations, you need the WhatsApp Business Platform (Meta's Cloud API), usually through your PMS or a messaging provider. Three rules shape everything: guests must opt in, free-form replies are only possible within 24 hours of the guest's last message, and anything you send outside that window must be a template Meta has approved.</p></div>
<h2>Why hotels use WhatsApp</h2>
<p>For many travellers WhatsApp is the default way to message a business, especially across Europe, Latin America, the Middle East and Türkiye. A question on WhatsApp gets read; an email often doesn't. For a hotel that means fewer phone calls at reception, fewer “we never got your email” moments and an easy channel for the practical questions every stay produces:</p>
<ul><li>Before arrival: check-in time, parking, directions, early arrival, airport transfer</li>
<li>During the stay: towels, breakfast hours, a restaurant tip, a late check-out request</li>
<li>After departure: a forgotten charger, an invoice, a question about the next visit</li></ul>
<p>The catch is staffing. Guests write at 2 a.m., in languages your team doesn't speak, and expect an answer in minutes. That is where setup choices and automation matter.</p>
<h2>WhatsApp Business app or WhatsApp Business Platform?</h2>
<p>Meta offers two products. The app is free to download and is designed for small businesses talking to customers from a single device. The Platform is accessed through an API, either directly through the Cloud API that Meta hosts or through a business solution provider, and is built for automation and integration with your other systems.</p>
{_tbl(["", "WhatsApp Business app", "WhatsApp Business Platform (Cloud API)"], [
  ("Cost to start", "Free app", "No app fee; Meta charges per message (see below)"),
  ("Who answers", "Staff on the phone and linked devices", "Any number of team members through your software"),
  ("Automation", "Greeting and away messages, quick replies", "Full automation, AI replies, integration with your PMS"),
  ("Messages outside 24 hours", "Not restricted the same way", "Only approved templates"),
  ("Good for", "A few rooms, one person answering", "Hotels with a team, several channels or automation needs")])}
<p>Meta's older self-hosted option, the On-Premises API, was retired in October 2025; new integrations use the Cloud API. When you register a number on the Platform, it must be a number you own that can receive a call or SMS for verification, and your display name is reviewed against Meta's guidelines.</p>
<h2>The 24-hour customer service window</h2>
<p>This is the rule that surprises most hotels. Whenever a guest messages you, a 24-hour customer service window opens, and it resets each time the guest writes again. Inside the window you can send any normal reply, without approval. Once the window closes, you can only send pre-approved message templates.</p>
<p>In practice: a guest who asked about parking yesterday morning and hasn't written since can't receive a free-form “Your room is ready” message today. Either you use an approved template, or you reach them another way (email, phone, the OTA inbox).</p>
<h2>Message templates</h2>
<p>Templates are fixed messages with placeholders, such as a booking confirmation or a check-in reminder, that Meta reviews before you can use them. Each template must be categorised as <strong>marketing</strong>, <strong>utility</strong> (related to a specific transaction, like a booking) or <strong>authentication</strong> (one-time codes). Review is automated and can take up to 24 hours; only approved templates can be sent.</p>
<p>Keep utility templates genuinely transactional. A “Your booking is confirmed” message with a promotion bolted on will be treated as marketing.</p>
<h2>What Meta charges</h2>
<p>Since 1 July 2025 the Platform uses per-message pricing instead of the older per-conversation model. Meta's current pricing page states that, from 1 October 2026, it also charges per message for service messages and for utility messages sent in reply to users inside the 24-hour window. Messages sent within a 72-hour free entry point window, which opens when someone starts a chat from a Click-to-WhatsApp ad or a Facebook call-to-action button, remain free. Rates depend on the recipient's country and the message category, so check Meta's rate card and ask your provider how these fees are billed. The free Business app is not affected.</p>
<h2>Opt-in and opt-out: what the policy requires</h2>
<p>The WhatsApp Business Messaging Policy allows you to contact people only if they have given you their phone number and have opted in to receive messages from you. You must respect any request to stop, made on WhatsApp or elsewhere. For a hotel this usually means:</p>
<ul><li>Ask for consent where you collect the number: the booking form, online check-in or at the desk. Say what kind of messages to expect.</li>
<li>Keep a record of the consent with the reservation.</li>
<li>Don't add OTA guests to promotional lists just because a phone number came with the booking.</li>
<li>Answer “stop” requests immediately and remove the number.</li></ul>
<p>When a guest writes to you first, you can reply within the window. The opt-in question matters mostly for messages you start yourself, such as reminders and offers.</p>
<h2>Messaging limits</h2>
<p>Messaging limits cap how many different people you can reach with messages you start (outside a customer service window) in a rolling 24 hours. New accounts start at 250 recipients; the next tiers are 2,000, 10,000, 100,000 and unlimited. Since October 2025 the limit applies to your whole Meta business portfolio, shared by all its numbers. Business verification, or sending good-quality templates, moves you up. Replies to guests who wrote to you don't count against this limit, and most small hotels never reach it.</p>
<h2>Answering in every guest's language</h2>
<p>A hotel in Lisbon or Antalya can receive messages in a dozen languages in one week. Guests who can write in their own language ask clearer questions and are less likely to misunderstand the answer. Translation tools help, but copying text in and out of a translator at night is exactly the kind of work that slips. An AI assistant that detects the language and answers in it closes that gap, provided your team can still read the conversation in its own language.</p>
<h2>What an AI assistant can and can't do on WhatsApp</h2>
<p>Meta's terms bar companies whose main product is a general-purpose AI assistant from using the WhatsApp Business Platform. A hotel using automation to answer its own guests is a different case, and the messaging policy allows automated replies inside the 24-hour window as long as you also offer a prompt, clear way to reach a human: an in-chat handover, a phone number, an email address or the front desk.</p>
{_tbl(["A good AI assistant can", "It shouldn't, or can't"], [
  ("Answer routine questions 24/7 from your own hotel information", "Invent an answer to something you never told it"),
  ("Reply in the guest's language", "Message guests outside the 24-hour window with free text"),
  ("Collect dates and guests for a booking request and pass it on", "Confirm a booking, take payment or grant a discount on its own"),
  ("Recognise complaints, refunds and special requests and hand them over", "Handle a complaint that needs judgement or compensation"),
  ("Tell you which questions it couldn't answer", "Replace the opt-in your guests gave you")])}
<p>Start in approval mode for the first days, read every draft, and switch topics to automatic once the answers are consistent. Our guide on <a href="{U("post-ai")}">answering hotel guest messages with AI</a> covers that rollout in more detail.</p>
<h2>Setting up WhatsApp for your hotel: a checklist</h2>
<ol><li><strong>Choose the number.</strong> A dedicated business number that your team, not one person, controls.</li>
<li><strong>Decide app or Platform.</strong> One person answering a handful of messages: the app may be enough. A team, automation or a PMS link: the Platform.</li>
<li><strong>Prepare your hotel information.</strong> Check-in and check-out times, parking, breakfast, pets, transfers, house rules. Automatic replies are only as good as this.</li>
<li><strong>Set handover rules.</strong> Which topics always go to a person: discounts, refunds, complaints, group requests.</li>
<li><strong>Add the number where guests look.</strong> Confirmation emails, your website, the Google Business Profile, the OTA listing where allowed.</li>
<li><strong>Collect consent</strong> if you plan to send messages first, and keep the record.</li>
<li><strong>Plan the templates</strong> you will need outside the 24-hour window and submit them for review.</li></ol>
<h2>How Hostlio Pro's Lio fits in</h2>
<p>In Hostlio Pro you connect your hotel's own WhatsApp number from the dashboard through Meta's official signup flow, on every plan. WhatsApp messages then arrive in one inbox, where <a href="{U("ai")}">Lio, the AI assistant</a>, answers from your hotel information and reservation data in the guest's language. You read Lio's reply translated into your language; messages you write yourself are sent as you wrote them. You choose how much Lio does on its own: fully automatic, automatic for routine questions with drafts for the rest (the default), or drafts only. Discounts, refunds, complaints and booking requests come to you for approval by default.</p>
<ul><li><strong>Inside the window, by design.</strong> Lio replies to guests who write to you. If a guest's 24-hour window has closed, a free-form reply can't be delivered, and the dashboard tells you so you can reach the guest another way. Hostlio Pro doesn't send WhatsApp marketing campaigns.</li>
<li><strong>Booking requests (Pro and Growth).</strong> Lio collects dates, guests and room preference, quotes from your own rates and availability, and sends you the request. It becomes a reservation only when you approve it.</li>
<li><strong>One inbox for OTAs too (Pro and Growth).</strong> Booking.com, Airbnb and Expedia messages land next to WhatsApp, with the reservation alongside each conversation.</li>
<li><strong>Gaps flagged, not guessed.</strong> When guests ask something your setup doesn't cover, Lio marks the missing field so you can fill it once.</li>
<li><strong>Predictable quota.</strong> Starter includes ⟦quota:starter⟧ AI messages a month, Pro ⟦quota:pro⟧ and Growth ⟦quota:growth⟧. The counter turns amber at 80%, you get an email at 100%, and automatic replies pause at about 110% while messages keep arriving for your team.</li></ul>
<p>Plans start at ⟦price:starter⟧ a month with a 7-day free trial; see <a href="{U("pricing")}">pricing</a>. To estimate the time Lio could save, try the <a href="{U("roi")}">ROI calculator</a>, and for OTA messages read <a href="{U("post-autoreply")}">how to auto-reply to Booking.com guest messages</a>.</p>'''
    c += _src("en")
    faq = [("Is WhatsApp Business free for hotels?", "The WhatsApp Business app is free. The WhatsApp Business Platform (API) has no app fee, but Meta charges per message; from 1 October 2026 that includes service replies inside the 24-hour window, while messages within a 72-hour free entry point window from Click-to-WhatsApp ads stay free. Your software provider may charge separately."),
           ("Can a hotel message a guest who hasn't written for days?", "Only with a message template that Meta has approved, and only if the guest opted in to receive messages from you. Free-form replies are possible only within 24 hours of the guest's last message."),
           ("Do I need the WhatsApp Business API for automatic replies?", "For anything beyond the app's greeting, away messages and quick replies, yes. AI replies and integration with a PMS run on the WhatsApp Business Platform."),
           ("Is an AI chatbot allowed on WhatsApp?", "Meta's terms prohibit companies whose primary product is a general-purpose AI assistant from using the Platform. Businesses may automate replies to their own customers inside the 24-hour window, as long as they offer a clear way to reach a human."),
           ("Can Lio send WhatsApp reminders before arrival?", "Not today. Lio answers guests who write to you, within WhatsApp's 24-hour window. The online check-in link can be sent automatically by email on Pro and Growth.")]
    return c, faq


def es(U):
    c = f'''<div class="answer"><p><strong>Respuesta corta:</strong> WhatsApp funciona bien en hotelería porque los huéspedes ya lo usan y responden rápido. Un alojamiento pequeño puede empezar con la app gratuita WhatsApp Business en un solo teléfono. Cuando varias personas tienen que responder, o quieres respuestas automáticas y conexión con tus reservas, necesitas la WhatsApp Business Platform (la Cloud API de Meta), normalmente a través de tu PMS o de un proveedor de mensajería. Tres reglas lo condicionan todo: el huésped debe dar su consentimiento, las respuestas libres solo son posibles dentro de las 24 horas siguientes a su último mensaje y lo que envíes fuera de esa ventana tiene que ser una plantilla aprobada por Meta.</p></div>
<h2>Por qué los hoteles usan WhatsApp</h2>
<p>Para muchos viajeros WhatsApp es la forma normal de escribir a un negocio, sobre todo en España, Latinoamérica, Europa y Oriente Medio. Un mensaje de WhatsApp se lee; un email, muchas veces no. Para un hotel eso significa menos llamadas a recepción, menos “no recibí su correo” y un canal cómodo para las preguntas prácticas de cada estancia:</p>
<ul><li>Antes de llegar: hora de check-in, parking, cómo llegar, llegada temprana, traslado desde el aeropuerto</li>
<li>Durante la estancia: toallas, horario del desayuno, una recomendación de restaurante, salida tardía</li>
<li>Después de la salida: un cargador olvidado, una factura, una pregunta sobre la próxima visita</li></ul>
<p>El problema es el personal. Los huéspedes escriben a las 2 de la madrugada, en idiomas que tu equipo no habla, y esperan respuesta en minutos. Ahí es donde importan la configuración y la automatización.</p>
<h2>¿App WhatsApp Business o WhatsApp Business Platform?</h2>
<p>Meta ofrece dos productos. La app se descarga gratis y está pensada para pequeños negocios que atienden a sus clientes desde un solo dispositivo. La Platform se usa mediante una API, directamente con la Cloud API alojada por Meta o a través de un proveedor de soluciones, y está hecha para automatizar e integrarse con tus otros sistemas.</p>
{_tbl(["", "App WhatsApp Business", "WhatsApp Business Platform (Cloud API)"], [
  ("Coste para empezar", "App gratuita", "Sin cuota de app; Meta cobra por mensaje (ver abajo)"),
  ("Quién responde", "Personal en el teléfono y dispositivos vinculados", "Todo el equipo que quieras, desde tu software"),
  ("Automatización", "Mensajes de bienvenida y ausencia, respuestas rápidas", "Automatización completa, respuestas con IA, integración con el PMS"),
  ("Mensajes pasadas 24 horas", "Sin la misma restricción", "Solo plantillas aprobadas"),
  ("Ideal para", "Pocas habitaciones, una persona respondiendo", "Hoteles con equipo, varios canales o necesidad de automatizar")])}
<p>La antigua opción autoalojada de Meta, la On-Premises API, se retiró en octubre de 2025; las integraciones nuevas usan la Cloud API. Para registrar un número en la Platform debe ser un número tuyo capaz de recibir una llamada o un SMS de verificación, y Meta revisa el nombre visible según sus directrices.</p>
<h2>La ventana de atención de 24 horas</h2>
<p>Es la regla que más sorprende. Cada vez que un huésped te escribe se abre una ventana de atención al cliente de 24 horas, que se reinicia con cada nuevo mensaje suyo. Dentro de la ventana puedes enviar cualquier respuesta normal, sin aprobación. Cuando se cierra, solo puedes enviar plantillas de mensaje aprobadas previamente.</p>
<p>En la práctica: a un huésped que preguntó por el parking ayer por la mañana y no ha vuelto a escribir no le puedes mandar hoy un mensaje libre de “Su habitación está lista”. O usas una plantilla aprobada, o le contactas por otra vía (email, teléfono, el chat de la OTA).</p>
<h2>Plantillas de mensaje</h2>
<p>Las plantillas son mensajes fijos con campos variables, como una confirmación de reserva o un recordatorio de check-in, que Meta revisa antes de que puedas usarlas. Cada plantilla debe clasificarse como <strong>marketing</strong>, <strong>utilidad</strong> (ligada a una transacción concreta, como una reserva) o <strong>autenticación</strong> (códigos de un solo uso). La revisión es automática y puede tardar hasta 24 horas; solo se pueden enviar plantillas aprobadas.</p>
<p>Mantén las plantillas de utilidad realmente transaccionales. Un “Su reserva está confirmada” con una promoción añadida se tratará como marketing.</p>
<h2>Lo que cobra Meta</h2>
<p>Desde el 1 de julio de 2025 la Platform cobra por mensaje en lugar de por conversación. La página de precios actual de Meta indica que, desde el 1 de octubre de 2026, también cobra por mensaje los mensajes de servicio y los de utilidad enviados como respuesta dentro de la ventana de 24 horas. Siguen siendo gratuitos los mensajes enviados dentro de una ventana de punto de entrada gratuito de 72 horas, que se abre cuando alguien inicia el chat desde un anuncio de clic a WhatsApp o un botón de llamada a la acción de Facebook. Las tarifas dependen del país del destinatario y de la categoría, así que consulta la tabla de precios de Meta y pregunta a tu proveedor cómo se facturan. La app gratuita no se ve afectada.</p>
<h2>Consentimiento y baja: lo que exige la política</h2>
<p>La política de mensajería de WhatsApp Business solo permite contactar con personas que te han dado su número y han aceptado recibir mensajes tuyos. Debes respetar cualquier petición de dejar de recibirlos, hecha por WhatsApp o por otra vía. En un hotel suele significar:</p>
<ul><li>Pedir el consentimiento donde recoges el número: el formulario de reserva, el check-in online o la recepción, explicando qué mensajes recibirá.</li>
<li>Guardar constancia del consentimiento con la reserva.</li>
<li>No añadir huéspedes de OTA a listas promocionales solo porque la reserva traía un teléfono.</li>
<li>Atender las peticiones de baja de inmediato y eliminar el número.</li></ul>
<p>Cuando el huésped te escribe primero, puedes responder dentro de la ventana. El consentimiento importa sobre todo para los mensajes que inicias tú, como recordatorios y ofertas. En la UE recuerda además las obligaciones del RGPD sobre los datos de tus huéspedes.</p>
<h2>Límites de mensajería</h2>
<p>Los límites de mensajería fijan a cuántas personas distintas puedes enviar mensajes iniciados por ti (fuera de una ventana de atención) en 24 horas móviles. Las cuentas nuevas empiezan en 250 destinatarios; los siguientes niveles son 2.000, 10.000, 100.000 e ilimitado. Desde octubre de 2025 el límite se aplica a todo tu portfolio empresarial de Meta y lo comparten todos sus números. La verificación del negocio, o enviar plantillas de buena calidad, te hace subir de nivel. Las respuestas a huéspedes que te escribieron no cuentan, y la mayoría de hoteles pequeños nunca llega al límite.</p>
<h2>Responder en el idioma de cada huésped</h2>
<p>Un hotel en Barcelona o Málaga puede recibir mensajes en una docena de idiomas en una semana. El huésped que escribe en su idioma pregunta con más claridad y entiende mejor la respuesta. Los traductores ayudan, pero copiar y pegar textos a medianoche es justo el tipo de tarea que se escapa. Un asistente de IA que detecta el idioma y responde en él cierra ese hueco, siempre que tu equipo pueda leer la conversación en el suyo.</p>
<h2>Lo que un asistente de IA puede y no puede hacer en WhatsApp</h2>
<p>Los términos de Meta impiden usar la WhatsApp Business Platform a las empresas cuyo producto principal es un asistente de IA de uso general. Un hotel que automatiza las respuestas a sus propios huéspedes es otro caso: la política permite respuestas automáticas dentro de la ventana de 24 horas siempre que ofrezcas una vía rápida y clara para hablar con una persona, como el traspaso a un agente en el chat, un teléfono, un email o la recepción.</p>
{_tbl(["Un buen asistente de IA puede", "No debe o no puede"], [
  ("Responder preguntas habituales 24/7 con la información de tu hotel", "Inventarse una respuesta sobre algo que nunca le contaste"),
  ("Contestar en el idioma del huésped", "Escribir texto libre fuera de la ventana de 24 horas"),
  ("Recoger fechas y personas para una solicitud de reserva y pasártela", "Confirmar una reserva, cobrar o conceder un descuento por su cuenta"),
  ("Detectar quejas, reembolsos y peticiones especiales y derivarlas", "Gestionar una queja que exige criterio o compensación"),
  ("Decirte qué preguntas no ha sabido responder", "Sustituir el consentimiento que te dieron tus huéspedes")])}
<p>Empieza en modo aprobación los primeros días, revisa cada borrador y pasa los temas a automático cuando las respuestas sean coherentes. Nuestra guía para <a href="{U("post-ai")}">responder mensajes de huéspedes con IA</a> explica ese despliegue con más detalle.</p>
<h2>Configurar WhatsApp en tu hotel: lista de control</h2>
<ol><li><strong>Elige el número.</strong> Un número de empresa dedicado que controle el equipo, no una sola persona.</li>
<li><strong>Decide app o Platform.</strong> Una persona y pocos mensajes: la app puede bastar. Un equipo, automatización o conexión con el PMS: la Platform.</li>
<li><strong>Prepara la información del hotel.</strong> Horarios de entrada y salida, parking, desayuno, mascotas, traslados, normas. Las respuestas automáticas valen lo que vale esta información.</li>
<li><strong>Define qué pasa a una persona.</strong> Descuentos, reembolsos, quejas, grupos.</li>
<li><strong>Muestra el número donde miran los huéspedes.</strong> Emails de confirmación, tu web, el perfil de empresa de Google y la ficha de la OTA cuando esté permitido.</li>
<li><strong>Recoge el consentimiento</strong> si vas a escribir tú primero, y guarda la constancia.</li>
<li><strong>Prepara las plantillas</strong> que necesitarás fuera de la ventana de 24 horas y envíalas a revisión.</li></ol>
<h2>Cómo encaja Lio, el asistente de Hostlio Pro</h2>
<p>En Hostlio Pro conectas el número de WhatsApp de tu hotel desde el panel, con el proceso de alta oficial de Meta, en todos los planes. Los mensajes de WhatsApp llegan a una sola bandeja, donde <a href="{U("ai")}">Lio, el asistente de IA</a>, responde con la información de tu hotel y los datos de la reserva en el idioma del huésped. Tú lees la respuesta de Lio traducida a tu idioma; lo que escribes tú se envía tal cual. Decides cuánto hace Lio solo: todo automático, automático para preguntas habituales con borradores para el resto (la opción por defecto) o solo borradores. Descuentos, reembolsos, quejas y solicitudes de reserva llegan por defecto para tu aprobación.</p>
<ul><li><strong>Dentro de la ventana, por diseño.</strong> Lio responde a los huéspedes que te escriben. Si la ventana de 24 horas de un huésped se ha cerrado, una respuesta libre no se puede entregar y el panel te lo indica para que le contactes por otra vía. Hostlio Pro no envía campañas de marketing por WhatsApp.</li>
<li><strong>Solicitudes de reserva (Pro y Growth).</strong> Lio recoge fechas, personas y preferencia de habitación, da precio con tus tarifas y disponibilidad y te envía la solicitud. Solo se convierte en reserva cuando la apruebas.</li>
<li><strong>Una bandeja también para las OTA (Pro y Growth).</strong> Los mensajes de Booking.com, Airbnb y Expedia llegan junto a WhatsApp, con la reserva al lado de cada conversación.</li>
<li><strong>Señala lo que falta en lugar de adivinar.</strong> Si los huéspedes preguntan algo que tu configuración no cubre, Lio marca el campo que falta para que lo rellenes una vez.</li>
<li><strong>Cuota previsible.</strong> Starter incluye ⟦quota:starter⟧ mensajes de IA al mes, Pro ⟦quota:pro⟧ y Growth ⟦quota:growth⟧. El contador se pone en ámbar al 80 %, recibes un email al 100 % y las respuestas automáticas se pausan hacia el 110 %, mientras los mensajes siguen llegando para tu equipo.</li></ul>
<p>Los planes empiezan en ⟦price:starter⟧ al mes, con 7 días de prueba gratis; consulta los <a href="{U("pricing")}">precios</a>. Para estimar el tiempo que Lio puede ahorrarte, prueba la <a href="{U("roi")}">calculadora de ROI</a>, y para los mensajes de las OTA lee <a href="{U("post-autoreply")}">cómo responder automáticamente a los mensajes de Booking.com</a>.</p>'''
    c += _src("es")
    faq = [("¿WhatsApp Business es gratis para hoteles?", "La app WhatsApp Business es gratuita. La WhatsApp Business Platform (API) no tiene cuota de app, pero Meta cobra por mensaje; desde el 1 de octubre de 2026 eso incluye las respuestas de servicio dentro de la ventana de 24 horas, mientras que los mensajes dentro de una ventana de punto de entrada gratuito de 72 horas, abierta desde anuncios de clic a WhatsApp, siguen siendo gratis. Tu proveedor de software puede cobrar aparte."),
           ("¿Puede un hotel escribir a un huésped que lleva días sin escribir?", "Solo con una plantilla aprobada por Meta y si el huésped aceptó recibir mensajes tuyos. Las respuestas libres solo son posibles dentro de las 24 horas siguientes a su último mensaje."),
           ("¿Necesito la API de WhatsApp Business para respuestas automáticas?", "Para todo lo que vaya más allá de los mensajes de bienvenida, ausencia y respuestas rápidas de la app, sí. Las respuestas con IA y la integración con un PMS funcionan sobre la WhatsApp Business Platform."),
           ("¿Está permitido un chatbot de IA en WhatsApp?", "Los términos de Meta prohíben usar la Platform a empresas cuyo producto principal es un asistente de IA de uso general. Los negocios pueden automatizar las respuestas a sus propios clientes dentro de la ventana de 24 horas, siempre que ofrezcan una vía clara para hablar con una persona."),
           ("¿Puede Lio enviar recordatorios por WhatsApp antes de la llegada?", "Hoy no. Lio responde a los huéspedes que te escriben, dentro de la ventana de 24 horas de WhatsApp. En Pro y Growth el enlace de check-in online puede enviarse automáticamente por email.")]
    return c, faq


def it(U):
    c = f'''<div class="answer"><p><strong>In breve:</strong> WhatsApp funziona bene per gli hotel perché gli ospiti lo usano già e rispondono in fretta. Una piccola struttura può iniziare con l'app gratuita WhatsApp Business su un solo telefono. Quando devono rispondere più persone, o vuoi risposte automatiche e un collegamento con le prenotazioni, ti serve la WhatsApp Business Platform (la Cloud API di Meta), di solito tramite il gestionale o un fornitore di messaggistica. Tre regole condizionano tutto: l'ospite deve dare il consenso, le risposte libere sono possibili solo entro 24 ore dal suo ultimo messaggio e ciò che invii fuori da quella finestra deve essere un modello approvato da Meta.</p></div>
<h2>Perché gli hotel usano WhatsApp</h2>
<p>Per molti viaggiatori WhatsApp è il modo normale di scrivere a un'attività, in Italia come nel resto d'Europa, in America Latina e in Medio Oriente. Un messaggio WhatsApp viene letto; un'email spesso no. Per un hotel significa meno telefonate alla reception, meno “non ho ricevuto la sua email” e un canale comodo per le domande pratiche di ogni soggiorno:</p>
<ul><li>Prima dell'arrivo: orario del check-in, parcheggio, indicazioni, arrivo anticipato, transfer dall'aeroporto</li>
<li>Durante il soggiorno: asciugamani, orario della colazione, un consiglio per cena, late check-out</li>
<li>Dopo la partenza: un caricatore dimenticato, una fattura, una domanda per il prossimo soggiorno</li></ul>
<p>Il problema è il personale. Gli ospiti scrivono alle 2 di notte, in lingue che il tuo staff non parla, e si aspettano una risposta in pochi minuti. È qui che contano configurazione e automazione.</p>
<h2>App WhatsApp Business o WhatsApp Business Platform?</h2>
<p>Meta offre due prodotti. L'app si scarica gratis ed è pensata per piccole attività che parlano con i clienti da un solo dispositivo. La Platform si usa tramite API, direttamente con la Cloud API ospitata da Meta o attraverso un fornitore di soluzioni, ed è fatta per automatizzare e integrarsi con gli altri sistemi.</p>
{_tbl(["", "App WhatsApp Business", "WhatsApp Business Platform (Cloud API)"], [
  ("Costo per iniziare", "App gratuita", "Nessun canone per l'app; Meta addebita per messaggio (vedi sotto)"),
  ("Chi risponde", "Lo staff sul telefono e sui dispositivi collegati", "Tutto il team che vuoi, dal tuo software"),
  ("Automazione", "Messaggi di benvenuto e di assenza, risposte rapide", "Automazione completa, risposte con AI, integrazione con il PMS"),
  ("Messaggi dopo 24 ore", "Senza la stessa restrizione", "Solo modelli approvati"),
  ("Adatta a", "Poche camere, una persona che risponde", "Hotel con un team, più canali o bisogno di automatizzare")])}
<p>La vecchia opzione self-hosted di Meta, la On-Premises API, è stata dismessa a ottobre 2025; le nuove integrazioni usano la Cloud API. Per registrare un numero sulla Platform deve essere un numero tuo, in grado di ricevere una chiamata o un SMS di verifica, e il nome visualizzato viene controllato secondo le linee guida di Meta.</p>
<h2>La finestra di assistenza di 24 ore</h2>
<p>È la regola che sorprende di più. Ogni volta che un ospite ti scrive si apre una finestra di assistenza clienti di 24 ore, che riparte a ogni suo nuovo messaggio. Dentro la finestra puoi inviare qualsiasi risposta normale, senza approvazione. Quando si chiude, puoi inviare solo modelli di messaggio approvati in anticipo.</p>
<p>In pratica: a un ospite che ieri mattina ha chiesto del parcheggio e non ha più scritto non puoi mandare oggi un messaggio libero “La sua camera è pronta”. O usi un modello approvato, o lo contatti in un altro modo (email, telefono, la chat della OTA).</p>
<h2>Modelli di messaggio</h2>
<p>I modelli sono messaggi fissi con campi variabili, come una conferma di prenotazione o un promemoria di check-in, che Meta esamina prima che tu possa usarli. Ogni modello va classificato come <strong>marketing</strong>, <strong>utilità</strong> (legato a una transazione precisa, come una prenotazione) o <strong>autenticazione</strong> (codici monouso). La revisione è automatica e può richiedere fino a 24 ore; si possono inviare solo modelli approvati.</p>
<p>Mantieni i modelli di utilità davvero transazionali. Un “La sua prenotazione è confermata” con una promozione aggiunta verrà trattato come marketing.</p>
<h2>Quanto fa pagare Meta</h2>
<p>Dal 1° luglio 2025 la Platform applica un prezzo per messaggio invece che per conversazione. La pagina prezzi attuale di Meta indica che dal 1° ottobre 2026 addebita per messaggio anche i messaggi di servizio e i messaggi di utilità inviati in risposta all'utente dentro la finestra di 24 ore. Restano gratuiti i messaggi inviati in una finestra di ingresso gratuita di 72 ore, che si apre quando qualcuno avvia la chat da un annuncio click-to-WhatsApp o da un pulsante di invito all'azione di Facebook. Le tariffe dipendono dal paese del destinatario e dalla categoria: controlla il listino di Meta e chiedi al tuo fornitore come vengono fatturate. L'app gratuita non è interessata.</p>
<h2>Consenso e disiscrizione: cosa chiede la policy</h2>
<p>La policy di messaggistica di WhatsApp Business consente di contattare solo chi ti ha dato il proprio numero e ha accettato di ricevere messaggi da te. Devi rispettare ogni richiesta di non essere più contattato, fatta su WhatsApp o altrove. Per un hotel di solito vuol dire:</p>
<ul><li>Chiedere il consenso dove raccogli il numero: modulo di prenotazione, check-in online o reception, spiegando che tipo di messaggi arriveranno.</li>
<li>Conservare traccia del consenso con la prenotazione.</li>
<li>Non inserire gli ospiti delle OTA in liste promozionali solo perché la prenotazione conteneva un telefono.</li>
<li>Gestire subito le richieste di stop e cancellare il numero.</li></ul>
<p>Quando è l'ospite a scrivere per primo, puoi rispondere dentro la finestra. Il consenso conta soprattutto per i messaggi che avvii tu, come promemoria e offerte. Nell'UE valgono anche gli obblighi del GDPR sui dati degli ospiti.</p>
<h2>Limiti di messaggistica</h2>
<p>I limiti di messaggistica stabiliscono a quante persone diverse puoi inviare messaggi avviati da te (fuori da una finestra di assistenza) in 24 ore mobili. I nuovi account partono da 250 destinatari; i livelli successivi sono 2.000, 10.000, 100.000 e illimitato. Da ottobre 2025 il limite vale per l'intero portafoglio business di Meta ed è condiviso da tutti i suoi numeri. La verifica dell'attività, o l'invio di modelli di buona qualità, ti fa salire di livello. Le risposte agli ospiti che ti hanno scritto non contano, e quasi nessun piccolo hotel arriva al limite.</p>
<h2>Rispondere nella lingua di ogni ospite</h2>
<p>Un hotel a Roma o sul lago di Garda può ricevere messaggi in una dozzina di lingue in una settimana. L'ospite che scrive nella propria lingua fa domande più chiare e capisce meglio la risposta. I traduttori aiutano, ma copiare e incollare testi a mezzanotte è proprio il lavoro che salta. Un assistente AI che riconosce la lingua e risponde in quella lingua chiude il buco, a patto che il tuo staff possa leggere la conversazione nella propria.</p>
<h2>Cosa può e non può fare un assistente AI su WhatsApp</h2>
<p>I termini di Meta vietano l'uso della WhatsApp Business Platform alle aziende il cui prodotto principale è un assistente AI generico. Un hotel che automatizza le risposte ai propri ospiti è un caso diverso: la policy consente risposte automatiche dentro la finestra di 24 ore purché tu offra un modo rapido e chiaro per parlare con una persona, come il passaggio a un operatore in chat, un numero di telefono, un'email o la reception.</p>
{_tbl(["Un buon assistente AI può", "Non deve o non può"], [
  ("Rispondere alle domande ricorrenti 24/7 con le informazioni del tuo hotel", "Inventare una risposta su qualcosa che non gli hai mai detto"),
  ("Rispondere nella lingua dell'ospite", "Scrivere testo libero fuori dalla finestra di 24 ore"),
  ("Raccogliere date e persone per una richiesta di prenotazione e passartela", "Confermare una prenotazione, incassare o concedere uno sconto da solo"),
  ("Riconoscere reclami, rimborsi e richieste speciali e passarli a te", "Gestire un reclamo che richiede giudizio o un risarcimento"),
  ("Dirti a quali domande non ha saputo rispondere", "Sostituire il consenso che ti hanno dato gli ospiti")])}
<p>Parti in modalità approvazione nei primi giorni, leggi ogni bozza e passa gli argomenti in automatico quando le risposte sono coerenti. La guida su <a href="{U("post-ai")}">come rispondere ai messaggi degli ospiti con l'AI</a> spiega questo avvio nel dettaglio.</p>
<h2>Configurare WhatsApp per il tuo hotel: checklist</h2>
<ol><li><strong>Scegli il numero.</strong> Un numero aziendale dedicato, controllato dal team e non da una sola persona.</li>
<li><strong>Decidi app o Platform.</strong> Una persona e pochi messaggi: l'app può bastare. Un team, automazione o collegamento con il gestionale: la Platform.</li>
<li><strong>Prepara le informazioni dell'hotel.</strong> Orari di arrivo e partenza, parcheggio, colazione, animali, transfer, regole della casa. Le risposte automatiche valgono quanto queste informazioni.</li>
<li><strong>Decidi cosa passa a una persona.</strong> Sconti, rimborsi, reclami, gruppi.</li>
<li><strong>Metti il numero dove guardano gli ospiti.</strong> Email di conferma, sito web, profilo dell'attività su Google e scheda OTA dove consentito.</li>
<li><strong>Raccogli il consenso</strong> se scriverai tu per primo, e conservane traccia.</li>
<li><strong>Prepara i modelli</strong> che ti serviranno fuori dalla finestra di 24 ore e inviali in revisione.</li></ol>
<h2>Come si inserisce Lio, l'assistente di Hostlio Pro</h2>
<p>In Hostlio Pro colleghi il numero WhatsApp del tuo hotel dalla dashboard, con la procedura di registrazione ufficiale di Meta, in tutti i piani. I messaggi WhatsApp arrivano in un'unica casella, dove <a href="{U("ai")}">Lio, l'assistente AI</a>, risponde con le informazioni del tuo hotel e i dati della prenotazione nella lingua dell'ospite. Tu leggi la risposta di Lio tradotta nella tua lingua; quello che scrivi tu viene inviato così com'è. Decidi quanto fa Lio da solo: tutto automatico, automatico per le domande ricorrenti con bozze per il resto (l'impostazione predefinita) o solo bozze. Sconti, rimborsi, reclami e richieste di prenotazione arrivano di norma per la tua approvazione.</p>
<ul><li><strong>Dentro la finestra, per scelta.</strong> Lio risponde agli ospiti che ti scrivono. Se la finestra di 24 ore di un ospite è chiusa, una risposta libera non può essere consegnata e la dashboard te lo segnala, così puoi contattarlo in altro modo. Hostlio Pro non invia campagne di marketing su WhatsApp.</li>
<li><strong>Richieste di prenotazione (Pro e Growth).</strong> Lio raccoglie date, persone e preferenza di camera, fa il preventivo con le tue tariffe e disponibilità e ti invia la richiesta. Diventa una prenotazione solo quando la approvi.</li>
<li><strong>Una casella anche per le OTA (Pro e Growth).</strong> I messaggi di Booking.com, Airbnb ed Expedia arrivano accanto a WhatsApp, con la prenotazione vicino a ogni conversazione.</li>
<li><strong>Segnala le lacune invece di indovinare.</strong> Se gli ospiti chiedono qualcosa che la configurazione non copre, Lio indica il campo mancante così lo compili una volta.</li>
<li><strong>Quota prevedibile.</strong> Starter include ⟦quota:starter⟧ messaggi AI al mese, Pro ⟦quota:pro⟧ e Growth ⟦quota:growth⟧. Il contatore diventa ambra all'80%, ricevi un'email al 100% e le risposte automatiche si sospendono intorno al 110%, mentre i messaggi continuano ad arrivare al tuo staff.</li></ul>
<p>I piani partono da ⟦price:starter⟧ al mese, con 7 giorni di prova gratuita; vedi i <a href="{U("pricing")}">prezzi</a>. Per stimare il tempo che Lio può farti risparmiare prova il <a href="{U("roi")}">calcolatore ROI</a>, e per i messaggi delle OTA leggi <a href="{U("post-autoreply")}">come rispondere in automatico ai messaggi di Booking.com</a>.</p>'''
    c += _src("it")
    faq = [("WhatsApp Business è gratis per gli hotel?", "L'app WhatsApp Business è gratuita. La WhatsApp Business Platform (API) non ha canone per l'app, ma Meta addebita per messaggio; dal 1° ottobre 2026 questo include le risposte di servizio dentro la finestra di 24 ore, mentre i messaggi in una finestra di ingresso gratuita di 72 ore, aperta da annunci click-to-WhatsApp, restano gratuiti. Il fornitore del software può fatturare a parte."),
           ("Un hotel può scrivere a un ospite che non scrive da giorni?", "Solo con un modello approvato da Meta e se l'ospite ha accettato di ricevere messaggi da te. Le risposte libere sono possibili solo entro 24 ore dal suo ultimo messaggio."),
           ("Serve l'API di WhatsApp Business per le risposte automatiche?", "Per tutto ciò che va oltre i messaggi di benvenuto, di assenza e le risposte rapide dell'app, sì. Le risposte con AI e l'integrazione con un gestionale funzionano sulla WhatsApp Business Platform."),
           ("Un chatbot AI è consentito su WhatsApp?", "I termini di Meta vietano la Platform alle aziende il cui prodotto principale è un assistente AI generico. Le attività possono automatizzare le risposte ai propri clienti dentro la finestra di 24 ore, purché offrano un modo chiaro per parlare con una persona."),
           ("Lio può inviare promemoria WhatsApp prima dell'arrivo?", "Oggi no. Lio risponde agli ospiti che ti scrivono, dentro la finestra di 24 ore di WhatsApp. Su Pro e Growth il link per il check-in online può essere inviato automaticamente via email.")]
    return c, faq


def fr(U):
    c = f'''<div class="answer"><p><strong>En bref :</strong> WhatsApp fonctionne bien pour les hôtels parce que les clients l'utilisent déjà et répondent vite. Un petit établissement peut commencer avec l'application gratuite WhatsApp Business sur un seul téléphone. Dès que plusieurs personnes doivent répondre, ou que vous voulez des réponses automatiques reliées à vos réservations, il vous faut la WhatsApp Business Platform (la Cloud API de Meta), en général via votre PMS ou un prestataire de messagerie. Trois règles encadrent tout : le client doit avoir donné son accord, les réponses libres ne sont possibles que dans les 24 heures suivant son dernier message, et tout envoi en dehors de cette fenêtre doit être un modèle approuvé par Meta.</p></div>
<h2>Pourquoi les hôtels utilisent WhatsApp</h2>
<p>Pour beaucoup de voyageurs, WhatsApp est le moyen naturel d'écrire à une entreprise, en Europe comme en Amérique latine, au Moyen-Orient ou au Maghreb. Un message WhatsApp est lu ; un e-mail, souvent pas. Pour un hôtel, cela veut dire moins d'appels à la réception, moins de « je n'ai pas reçu votre e-mail » et un canal pratique pour les questions de chaque séjour :</p>
<ul><li>Avant l'arrivée : heure d'arrivée, parking, itinéraire, arrivée anticipée, transfert depuis l'aéroport</li>
<li>Pendant le séjour : serviettes, horaires du petit-déjeuner, une adresse pour dîner, départ tardif</li>
<li>Après le départ : un chargeur oublié, une facture, une question pour le prochain séjour</li></ul>
<p>Le problème, c'est le personnel. Les clients écrivent à 2 heures du matin, dans des langues que votre équipe ne parle pas, et attendent une réponse en quelques minutes. C'est là que la mise en place et l'automatisation comptent.</p>
<h2>Application WhatsApp Business ou WhatsApp Business Platform ?</h2>
<p>Meta propose deux produits. L'application se télécharge gratuitement et vise les petites entreprises qui échangent avec leurs clients depuis un seul appareil. La Platform s'utilise via une API, directement avec la Cloud API hébergée par Meta ou par un prestataire de solutions, et sert à automatiser et à se connecter à vos autres outils.</p>
{_tbl(["", "Application WhatsApp Business", "WhatsApp Business Platform (Cloud API)"], [
  ("Coût de départ", "Application gratuite", "Pas d'abonnement à l'application ; Meta facture par message (voir plus bas)"),
  ("Qui répond", "L'équipe sur le téléphone et les appareils associés", "Autant de membres de l'équipe que vous voulez, depuis votre logiciel"),
  ("Automatisation", "Messages d'accueil et d'absence, réponses rapides", "Automatisation complète, réponses par IA, lien avec le PMS"),
  ("Messages après 24 heures", "Pas la même restriction", "Uniquement des modèles approuvés"),
  ("Adapté à", "Quelques chambres, une personne qui répond", "Hôtels avec une équipe, plusieurs canaux ou un besoin d'automatiser")])}
<p>L'ancienne option auto-hébergée de Meta, l'API On-Premises, a été arrêtée en octobre 2025 ; les nouvelles intégrations passent par la Cloud API. Pour enregistrer un numéro sur la Platform, il doit vous appartenir et pouvoir recevoir un appel ou un SMS de vérification, et le nom affiché est vérifié selon les règles de Meta.</p>
<h2>La fenêtre de service client de 24 heures</h2>
<p>C'est la règle qui surprend le plus. Chaque fois qu'un client vous écrit, une fenêtre de service client de 24 heures s'ouvre, et elle repart à zéro à chaque nouveau message de sa part. Dans la fenêtre, vous pouvez envoyer n'importe quelle réponse normale, sans approbation. Une fois fermée, vous ne pouvez plus envoyer que des modèles de message approuvés.</p>
<p>Concrètement : à un client qui a demandé hier matin s'il y avait un parking et n'a plus écrit depuis, vous ne pouvez pas envoyer aujourd'hui un message libre « Votre chambre est prête ». Soit vous utilisez un modèle approuvé, soit vous le joignez autrement (e-mail, téléphone, messagerie de l'OTA).</p>
<h2>Les modèles de message</h2>
<p>Les modèles sont des messages fixes avec des champs variables, comme une confirmation de réservation ou un rappel avant l'arrivée, que Meta examine avant que vous puissiez les utiliser. Chaque modèle doit être classé en <strong>marketing</strong>, <strong>utilitaire</strong> (lié à une transaction précise, comme une réservation) ou <strong>authentification</strong> (codes à usage unique). L'examen est automatique et peut prendre jusqu'à 24 heures ; seuls les modèles approuvés peuvent être envoyés.</p>
<p>Gardez les modèles utilitaires vraiment transactionnels. Un « Votre réservation est confirmée » accompagné d'une promotion sera traité comme du marketing.</p>
<h2>Ce que facture Meta</h2>
<p>Depuis le 1er juillet 2025, la Platform facture par message et non plus par conversation. La page tarifaire actuelle de Meta indique qu'à partir du 1er octobre 2026, elle facture aussi par message les messages de service et les messages utilitaires envoyés en réponse dans la fenêtre de 24 heures. Restent gratuits les messages envoyés dans une fenêtre de point d'entrée gratuit de 72 heures, ouverte quand quelqu'un lance la conversation depuis une publicité « Click to WhatsApp » ou un bouton d'appel à l'action Facebook. Les tarifs dépendent du pays du destinataire et de la catégorie : consultez la grille de Meta et demandez à votre prestataire comment ces frais sont facturés. L'application gratuite n'est pas concernée.</p>
<h2>Consentement et désinscription : ce qu'exige la politique</h2>
<p>La politique de messagerie de WhatsApp Business n'autorise à contacter que les personnes qui vous ont donné leur numéro et ont accepté de recevoir vos messages. Vous devez respecter toute demande d'arrêt, faite sur WhatsApp ou ailleurs. Pour un hôtel, cela veut généralement dire :</p>
<ul><li>Demander l'accord là où vous collectez le numéro : formulaire de réservation, check-in en ligne ou réception, en précisant quels messages seront envoyés.</li>
<li>Conserver la trace de l'accord avec la réservation.</li>
<li>Ne pas ajouter les clients des OTA à des listes promotionnelles au seul motif que la réservation contenait un téléphone.</li>
<li>Traiter immédiatement les demandes d'arrêt et supprimer le numéro.</li></ul>
<p>Quand le client vous écrit en premier, vous pouvez répondre dans la fenêtre. L'accord compte surtout pour les messages que vous envoyez de vous-même, comme les rappels et les offres. Dans l'UE, le RGPD s'applique aussi aux données de vos clients.</p>
<h2>Limites d'envoi</h2>
<p>Les limites d'envoi fixent à combien de personnes différentes vous pouvez écrire de votre propre initiative (hors fenêtre de service) sur 24 heures glissantes. Les nouveaux comptes commencent à 250 destinataires ; les paliers suivants sont 2 000, 10 000, 100 000 et illimité. Depuis octobre 2025, la limite s'applique à l'ensemble de votre portefeuille d'entreprise Meta et elle est partagée par tous ses numéros. La vérification de l'entreprise, ou l'envoi de modèles de bonne qualité, fait monter de palier. Les réponses aux clients qui vous ont écrit ne comptent pas, et la plupart des petits hôtels n'atteignent jamais la limite.</p>
<h2>Répondre dans la langue de chaque client</h2>
<p>Un hôtel à Nice ou à Paris peut recevoir des messages dans une douzaine de langues en une semaine. Le client qui écrit dans sa langue pose des questions plus claires et comprend mieux la réponse. Les traducteurs aident, mais copier-coller des textes à minuit est exactement le genre de tâche qui saute. Un assistant IA qui détecte la langue et répond dans cette langue comble ce manque, à condition que votre équipe puisse lire l'échange dans la sienne.</p>
<h2>Ce qu'un assistant IA peut et ne peut pas faire sur WhatsApp</h2>
<p>Les conditions de Meta interdisent la WhatsApp Business Platform aux entreprises dont le produit principal est un assistant IA généraliste. Un hôtel qui automatise les réponses à ses propres clients est un autre cas : la politique autorise les réponses automatiques dans la fenêtre de 24 heures, à condition d'offrir un moyen rapide et clair de joindre un humain, comme un transfert à un conseiller dans la conversation, un numéro de téléphone, une adresse e-mail ou la réception.</p>
{_tbl(["Un bon assistant IA peut", "Il ne doit pas ou ne peut pas"], [
  ("Répondre aux questions courantes 24h/24 avec les informations de votre hôtel", "Inventer une réponse sur un sujet que vous ne lui avez jamais donné"),
  ("Répondre dans la langue du client", "Écrire un message libre en dehors de la fenêtre de 24 heures"),
  ("Recueillir dates et nombre de personnes pour une demande de réservation et vous la transmettre", "Confirmer une réservation, encaisser ou accorder une remise seul"),
  ("Repérer réclamations, remboursements et demandes spéciales et vous les transmettre", "Traiter une réclamation qui demande du jugement ou un geste commercial"),
  ("Vous dire à quelles questions il n'a pas su répondre", "Remplacer l'accord que vos clients vous ont donné")])}
<p>Commencez en mode validation les premiers jours, relisez chaque brouillon et passez les sujets en automatique quand les réponses sont fiables. Notre guide pour <a href="{U("post-ai")}">répondre aux messages clients avec l'IA</a> détaille ce démarrage.</p>
<h2>Mettre en place WhatsApp dans votre hôtel : check-list</h2>
<ol><li><strong>Choisissez le numéro.</strong> Un numéro professionnel dédié, contrôlé par l'équipe et non par une seule personne.</li>
<li><strong>Choisissez l'application ou la Platform.</strong> Une personne et peu de messages : l'application peut suffire. Une équipe, de l'automatisation ou un lien avec le PMS : la Platform.</li>
<li><strong>Préparez les informations de l'hôtel.</strong> Heures d'arrivée et de départ, parking, petit-déjeuner, animaux, transferts, règlement intérieur. Les réponses automatiques ne valent que ce que valent ces informations.</li>
<li><strong>Définissez ce qui revient à un humain.</strong> Remises, remboursements, réclamations, groupes.</li>
<li><strong>Affichez le numéro là où les clients regardent.</strong> E-mails de confirmation, site web, fiche d'établissement Google et annonce OTA quand c'est autorisé.</li>
<li><strong>Recueillez l'accord</strong> si vous comptez écrire en premier, et gardez-en la trace.</li>
<li><strong>Préparez les modèles</strong> nécessaires hors fenêtre de 24 heures et soumettez-les à l'examen.</li></ol>
<h2>La place de Lio, l'assistant de Hostlio Pro</h2>
<p>Dans Hostlio Pro, vous connectez le numéro WhatsApp de votre hôtel depuis le tableau de bord, via la procédure d'inscription officielle de Meta, dans toutes les offres. Les messages WhatsApp arrivent dans une seule boîte de réception, où <a href="{U("ai")}">Lio, l'assistant IA</a>, répond avec les informations de votre hôtel et les données de réservation dans la langue du client. Vous lisez la réponse de Lio traduite dans votre langue ; ce que vous écrivez vous-même part tel quel. Vous choisissez ce que Lio fait seul : tout en automatique, automatique pour les questions courantes avec des brouillons pour le reste (le réglage par défaut), ou brouillons uniquement. Remises, remboursements, réclamations et demandes de réservation vous sont soumis pour validation par défaut.</p>
<ul><li><strong>Dans la fenêtre, par principe.</strong> Lio répond aux clients qui vous écrivent. Si la fenêtre de 24 heures d'un client est fermée, une réponse libre ne peut pas être remise et le tableau de bord vous le signale pour que vous le joigniez autrement. Hostlio Pro n'envoie pas de campagnes marketing sur WhatsApp.</li>
<li><strong>Demandes de réservation (Pro et Growth).</strong> Lio recueille dates, nombre de personnes et préférence de chambre, fait un devis avec vos tarifs et disponibilités et vous transmet la demande. Elle ne devient une réservation qu'après votre validation.</li>
<li><strong>Une boîte aussi pour les OTA (Pro et Growth).</strong> Les messages Booking.com, Airbnb et Expedia arrivent à côté de WhatsApp, avec la réservation à côté de chaque conversation.</li>
<li><strong>Il signale les manques au lieu de deviner.</strong> Quand les clients demandent une information absente de votre configuration, Lio indique le champ manquant pour que vous le remplissiez une fois.</li>
<li><strong>Un quota prévisible.</strong> Starter inclut ⟦quota:starter⟧ messages IA par mois, Pro ⟦quota:pro⟧ et Growth ⟦quota:growth⟧. Le compteur passe à l'orange à 80 %, vous recevez un e-mail à 100 % et les réponses automatiques sont suspendues vers 110 %, tandis que les messages continuent d'arriver pour votre équipe.</li></ul>
<p>Les offres commencent à ⟦price:starter⟧ par mois, avec 7 jours d'essai gratuit ; voir les <a href="{U("pricing")}">tarifs</a>. Pour estimer le temps que Lio peut vous faire gagner, essayez le <a href="{U("roi")}">calculateur de ROI</a>, et pour les messages des OTA lisez <a href="{U("post-autoreply")}">comment répondre automatiquement aux messages Booking.com</a>.</p>'''
    c += _src("fr")
    faq = [("WhatsApp Business est-il gratuit pour les hôtels ?", "L'application WhatsApp Business est gratuite. La WhatsApp Business Platform (API) n'a pas d'abonnement d'application, mais Meta facture par message ; depuis le 1er octobre 2026, cela inclut les réponses de service dans la fenêtre de 24 heures, tandis que les messages envoyés dans une fenêtre de point d'entrée gratuit de 72 heures, ouverte depuis une publicité « Click to WhatsApp », restent gratuits. Votre éditeur de logiciel peut facturer à part."),
           ("Un hôtel peut-il écrire à un client qui n'a pas écrit depuis plusieurs jours ?", "Uniquement avec un modèle approuvé par Meta, et si le client a accepté de recevoir vos messages. Les réponses libres ne sont possibles que dans les 24 heures suivant son dernier message."),
           ("Faut-il l'API WhatsApp Business pour des réponses automatiques ?", "Pour tout ce qui dépasse les messages d'accueil, d'absence et les réponses rapides de l'application, oui. Les réponses par IA et le lien avec un PMS fonctionnent sur la WhatsApp Business Platform."),
           ("Un chatbot IA est-il autorisé sur WhatsApp ?", "Les conditions de Meta interdisent la Platform aux entreprises dont le produit principal est un assistant IA généraliste. Une entreprise peut automatiser les réponses à ses propres clients dans la fenêtre de 24 heures, à condition d'offrir un moyen clair de joindre un humain."),
           ("Lio peut-il envoyer des rappels WhatsApp avant l'arrivée ?", "Pas aujourd'hui. Lio répond aux clients qui vous écrivent, dans la fenêtre de 24 heures de WhatsApp. Avec Pro et Growth, le lien de check-in en ligne peut être envoyé automatiquement par e-mail.")]
    return c, faq


FN = {"en": en, "es": es, "it": it, "fr": fr}
