"""SEO S7 + S8 (8 Ekim 2026): ince para sayfalarını segmente özgü bölümlerle derinleştirme.
Kapsam: en/hostel-software, en/boutique-hotel-software, es/check-in-online, es/channel-manager.
Diğer dillerdeki kardeş sayfalar aynı kancayı kullanır (TYPE_MORE / PAGE_MORE'a anahtar eklemek yeter);
metinler dile özgü olduğu için bu dalgada yalnız bu dört sayfa yazıldı.

Dürüstlük notları (ürün kodu 8 Ekim okundu):
- Hostlio Pro oda bazlı çalışır: yatak (dorm) envanteri ve çok odalı grup rezervasyonu YOK.
- Check-in formu SES.Hospedajes'in istediği alanların bir kısmını toplar (ad tek alan, belge tipi/no,
  uyruk, doğum tarihi, adres); cinsiyet, ikinci soyadı, destek numarası (soporte), akrabalık ve ödeme verisi YOK.
  Dışa aktarma CSV'dir (tarih aralığı); SES XML dosyası üretilmez, SES'e doğrudan gönderim YOKTUR.
- SES bilgileri resmî kaynaklardan doğrulandı: BOE-A-2021-17461 (RD 933/2021), hospedajes.ses.mir.es
  Instrucciones v1.1.0, sede.interior.gob.es SSS ve bilgi sayfası, La Moncloa 2.12.2024 basın notu."""
from build import url, btn, SIGNUP_URL


def _sec(h, inner, cls="rule", hid=None):
    return f'<section class="{cls}"><div class="wrap"><h2>{h}</h2>{inner}</div></section>'


def _rows(items):
    return '<div class="rows">' + "".join(f'<div class="row"><h3>{h}</h3><div><p>{p}</p></div></div>' for h, p in items) + "</div>"


def _table(head, rows, label=None):
    th = "".join(f"<th>{x}</th>" for x in head)
    tr = "".join("<tr>" + "".join((f"<th>{c}</th>" if i == 0 else f"<td>{c}</td>") for i, c in enumerate(r)) + "</tr>" for r in rows)
    return f'<div class="table-wrap"><table><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div>'


def _steps(items):
    return '<ol class="steps">' + "".join(f"<li><h3>{h}</h3><p>{p}</p></li>" for h, p in items) + "</ol>"


# ------------------------------------------------------------------ segment pages (pages_v4.type_page)
def _hostel_en(U):
    return "".join([
        _sec("A day at the hostel desk with Hostlio Pro", _rows([
            ("08:00, the day is laid out", "The Today screen lists arrivals, departures, rooms to clean, messages waiting for a reply and Lio drafts waiting for approval. The mobile app can send the same summary to your phone at 08:00 hotel time (Android today, iOS with the upcoming app update)."),
            ("Late morning, turnover", "Housekeeping sees today’s departures first, with rooms that have a same-day arrival marked high priority. When a room is clean, its status changes and reception sees it at once. If a shower breaks, report it with a photo and take the room out of order: it leaves sale on every connected channel until it is fixed."),
            ("Afternoon, arrivals", "Guests who completed online check-in (Pro and Growth) have already scanned their passport or ID and signed, so the desk hands over keys instead of typing passport numbers. No document images are stored."),
            ("Night, the inbox keeps moving", "Travellers write at all hours, in many languages, about late arrival, luggage storage, lockers, the kitchen or the nearest bus stop. Lio answers from the information you entered and hands anything that needs a decision to your night staff or to the morning shift."),
        ]), "white rule"),
        _sec("What hostel guests ask, and where Lio gets the answer",
            '<p class="lead" style="font-size:var(--t-0);max-width:70ch">Lio only answers from your property information and the guest’s reservation. The more of these you fill in once, the fewer messages reach your team.</p>'
            + _table(["Typical question", "What Lio uses to answer"], [
                ("“We land at 1 am, can we still check in?”", "Your check-in hours and late-arrival rules"),
                ("“Can we leave our bags after check-out?”", "Your luggage storage policy"),
                ("“Are there lockers? Do I need my own padlock?”", "Room and facility details you add"),
                ("“Is there a kitchen guests can use?”", "Facilities and house rules"),
                ("“How do we get here from the airport?”", "Transport notes, plus your airport transfer if you sell one"),
                ("“Do you run a walking tour tomorrow?”", "Your extras list; on Pro and Growth Lio can pass the request to your team"),
                ("“Can I change my dates?”", "Handed to your team: Lio does not change reservations"),
            ])),
        _sec("Hostelworld, Booking.com and direct bookings on one calendar", _rows([
            ("One availability for every channel", "Hostlio Pro connects to Hostelworld, Booking.com, Airbnb, Expedia and 100+ other channels over certified connections. A room sold on one channel closes on the others, and cancellations reopen it everywhere."),
            ("Weekend and event pricing", "Set a whole season in one go: choose dates, room types and rate plans, tick “weekends only” to price Friday and Saturday nights separately, and add a minimum stay, closed to arrival or stop sell for festival weekends."),
            ("See which channel really pays", "Analytics shows occupancy, ADR and RevPAR, plus gross revenue, commission and net for each OTA, so you can decide where to push direct bookings. Export to Excel for your accountant."),
        ])),
        _sec("Night staff, volunteers and housekeeping", _rows([
            ("A role for everyone", "Give each person a role: manager, front desk, housekeeping, accounting or viewer. Housekeepers only see rooms; accounting doesn’t see guest messages. When a volunteer leaves, suspend their access in one click. Starter includes 3 users, Pro 8 and Growth 20."),
            ("Know who changed what", "The activity log records each change field by field, with the person and time, for 365 days. Useful when several shifts touch the same booking."),
            ("Everyone in their language", "The dashboard and mobile app are in English, Spanish, French, Italian, Portuguese and Turkish, so an international team can work in its own language."),
        ]), "white rule"),
        _sec("Is Hostlio Pro the right hostel software for you?",
            '<p class="lead" style="font-size:var(--t-0);max-width:70ch">We would rather tell you now than after a migration. Hostlio Pro manages availability by room, not by bed.</p>'
            + _table(["Area", "Good fit", "Check with us first"], [
                ("Inventory", "Private rooms, family rooms and whole dorm rooms sold as one unit", "Selling single beds in shared dorms as separate inventory is not supported"),
                ("Bookings", "One room per reservation, from any channel or entered by hand", "Group bookings across several rooms are entered as separate reservations"),
                ("Size", "1 to 150 rooms, one property or two on Growth", "More than two properties or more than 150 rooms"),
                ("Payments", "Prices, extras and printable receipts on the reservation", "There is no built-in card payment, folio or point of sale"),
                ("Guests", "International travellers who write on WhatsApp and through OTA inboxes", "—"),
            ])),
        _sec("Switching from your current hostel software", _steps([
            ("Set up rooms and rates", "Create your room types, rooms and rate plans. The setup assistant checks what is missing before you go live."),
            ("Import your bookings", "Export future reservations from your old system as CSV or Excel and upload them. Columns are matched automatically and problem rows are listed with the reason."),
            ("Connect your channels", "Authorise Hostelworld, Booking.com and your other OTAs and map your rooms. Most properties connect the same day."),
        ]), "dark on-dark"),
        f'<section class="rule"><div class="wrap"><p>Read more: <a href="{U("post-overbooking")}">how to prevent overbooking across channels</a> and <a href="{U("post-autoreply")}">how to auto-reply to Booking.com messages</a>.</p></div></section>',
    ])


HOSTEL_EN_FAQ = [
    ("Can Lio answer questions about lockers, the kitchen or late arrival?", "Yes, as long as that information is in your property settings. Lio answers in the guest’s language and only from what you entered; when something is missing, it hands the message to your team and the dashboard shows which detail to add."),
    ("Can I take group bookings?", "A reservation holds one room, so a group across several rooms is entered as several reservations. For large groups, tell us how you sell them and we will check the setup with you in a demo."),
    ("Can volunteers or night staff get limited access?", "Yes. Give them the front desk or viewer role, or housekeeping if they only clean rooms. You can suspend access at any time, and the activity log shows who changed what."),
]


def _boutique_en(U):
    return "".join([
        _sec("AI for boutique hotels, without losing the personal touch", _rows([
            ("Your tone, your details", "Lio writes in the guest’s language using your own property information: check-in times, breakfast on the terrace, parking, pets, how to find you. It does not invent offers or policies that you have not entered."),
            ("You decide what is automatic", "Start in approval mode and read every reply before it goes out. Then let Lio close routine questions on its own and keep discounts, complaints and special requests for your team."),
            ("One inbox for every guest", "WhatsApp messages, and on Pro and Growth the Booking.com, Airbnb and Expedia inboxes, arrive in one place next to the guest’s reservation. Your team stops switching between extranets."),
            ("Know the limits", "Replies you type yourself are sent exactly as written. Lio shows you a translation of its own replies, and it hands over anything it is not sure about instead of guessing."),
        ]), "white rule"),
        _sec("A 50-room boutique hotel on a normal day",
            '<p class="lead" style="font-size:var(--t-0);max-width:70ch">An illustration of how the pieces fit together; your numbers will differ.</p>'
            + _table(["Time", "What happens", "Where in Hostlio Pro"], [
                ("02:10", "A guest from Seoul asks whether late check-in is possible", "Lio replies in Korean from your check-in rules"),
                ("08:00", "The owner reads the day: 12 arrivals, 9 departures, 2 drafts to approve", "Today screen and Lio Suggestions"),
                ("10:30", "A sink is leaking in room 14", "Maintenance report; the room leaves sale on every channel"),
                ("12:00", "Housekeeping turns over today’s departures, priority rooms first", "Housekeeping list, printable as PDF"),
                ("15:00", "Arriving guests already checked in online", "Online check-in with digital signature (Pro and Growth)"),
                ("18:00", "A guest asks for an airport transfer for Friday", "Lio offers it and passes the request to your team"),
                ("Monday", "The owner compares channel net revenue with last week", "Analytics and the weekly email report"),
            ])),
        _sec("More revenue per stay, without a hard sell", _rows([
            ("Extras at the right moment", "Airport transfers, tours and other extras are offered when they are relevant to the conversation, and the request reaches your team (Pro and Growth)."),
            ("Booking requests on WhatsApp", "When a guest asks about dates on WhatsApp, Lio collects dates, guests and room preference and quotes your own rate. It becomes a reservation only after you approve it (Pro and Growth)."),
            ("Suggestions every morning", "Lio Suggestions point out pricing, operations and revenue opportunities. Nothing changes without your approval, and rate suggestions stay within limits you set."),
            ("Channel net revenue", "Analytics shows each OTA’s gross revenue, commission and net, plus a 30, 60 and 90-day forward view with pickup, so you can see where direct bookings would pay off most."),
        ])),
        _sec("Arrival that feels like a welcome, not a form", _rows([
            ("Check-in before arrival", "Guests scan the machine-readable zone of their passport or ID on their own phone, add companions and sign. No document images are stored, and signatures are deleted 30 days after check-out."),
            ("Link sent automatically", "Switch on the check-in email and every new reservation with an email address receives the link in the guest’s language. You choose which booking sources it applies to."),
            ("Visa letters in one click", "Create an accommodation confirmation for visa or invitation applications from the reservation and save it as a PDF."),
        ]), "white rule"),
        _sec("Boutique hotel software checklist", _table(["Question to ask any vendor", "Hostlio Pro"], [
            ("Is the price public and flat, without booking commission?", "Yes: from ⟦price:starter⟧ a month, no commission, 7-day free trial"),
            ("Is the channel manager included?", "Yes, on every plan, with certified connections to 100+ channels"),
            ("Can AI answer guests in their language, with approval?", "Yes: WhatsApp on every plan, OTA inboxes on Pro and Growth"),
            ("Can each team member see only what they need?", "Yes: six roles; 3, 8 or 20 users by plan; activity log"),
            ("Can I see revenue per channel after commission?", "Yes, with Excel export and weekly and monthly email reports"),
            ("Can I bring my existing bookings?", "Yes, from a CSV or Excel file"),
            ("Is there a mobile app?", "Yes, iOS and Android, included in every plan"),
        ])),
        f'<section class="white rule"><div class="wrap"><p>Read more: <a href="{U("post-ai")}">answering hotel guest messages with AI</a> and <a href="{U("post-pms")}">choosing hotel management software for a small hotel</a>.</p></div></section>',
    ])


BOUTIQUE_EN_FAQ = [
    ("Will AI make a boutique hotel feel generic?", "Only if it guesses. Lio answers routine questions from your own information, in the guest’s language, and hands discounts, complaints and special requests to your team. Many hotels start in approval mode and read every reply for the first days."),
    ("What is the best guest messaging setup for a 50-room boutique hotel?", "One inbox for WhatsApp and the OTA inboxes, automatic replies for routine questions, and clear handover rules for everything else. Hostlio Pro’s Pro plan covers up to 50 rooms with ⟦quota:pro⟧ AI messages a month; Growth covers two properties or up to 150 rooms."),
]


TYPE_MORE = {
    "en": {"t-hostel": (_hostel_en, HOSTEL_EN_FAQ), "t-boutique": (_boutique_en, BOUTIQUE_EN_FAQ)},
}


def type_more(L, key):
    f = TYPE_MORE.get(L, {}).get(key)
    if not f: return "", []
    return f[0](lambda k: url(k, L)), f[1]


# ------------------------------------------------------------------ product pages (content_<lang>.checkin / channel)
def _checkin_es(U):
    return "".join([
        _sec("Check-in online y SES.Hospedajes (parte de viajeros)",
            '<div class="answer"><p><strong>En resumen:</strong> en España, los alojamientos deben comunicar al Ministerio del Interior los datos de sus huéspedes a través de SES.Hospedajes. Hostlio Pro recoge con el check-in online una parte de esos datos y te permite exportarlos, pero <strong>no envía nada a SES.Hospedajes</strong>: la comunicación la sigue haciendo tu establecimiento.</p></div>'
            + _rows([
                ("Qué es", "El <a href=\"https://www.boe.es/buscar/act.php?id=BOE-A-2021-17461\" rel=\"noopener\">Real Decreto 933/2021</a>, de 26 de octubre, obliga a quienes prestan servicios de alojamiento, de forma profesional o no (hoteles, hostales, pensiones, apartamentos turísticos, turismo rural y campings, entre otros), a llevar un registro documental de sus huéspedes y a comunicarlo al Ministerio del Interior. La comunicación se hace en SES.Hospedajes, la plataforma del Ministerio, operativa desde el 2 de diciembre de 2024."),
                ("Qué se comunica", "Dos cosas distintas: el parte de viajeros (los datos de cada huésped) y los datos de la reserva o del contrato. El decreto pide comunicarlos de manera inmediata y, en todo caso, en un plazo máximo de 24 horas desde la reserva o su cancelación y desde el inicio de la estancia. Cualquier cambio exige una nueva comunicación."),
                ("Qué datos pide", "De cada viajero: nombre y apellidos, sexo, tipo y número de documento, número de soporte, nacionalidad, fecha de nacimiento, domicilio, teléfono o email y, si viaja un menor, la relación de parentesco con el adulto. De la operación: referencia y fechas del contrato, entrada y salida, número de viajeros y datos de pago."),
                ("Cómo se envía", "En la propia aplicación de SES.Hospedajes, cargando un fichero XML o mediante un servicio web automático. Los registros se conservan durante tres años."),
            ])
            + '<p class="small muted">Fuentes: <a href="https://www.boe.es/buscar/act.php?id=BOE-A-2021-17461" rel="noopener">BOE (RD 933/2021)</a>, <a href="https://sede.interior.gob.es/portal/sede/informacion_hospedajes" rel="noopener">Sede del Ministerio del Interior</a> y <a href="https://hospedajes.ses.mir.es/hospedajes-sede/assets/docs/Instrucciones.pdf" rel="noopener">instrucciones de SES.Hospedajes</a>. Consultado en octubre de 2026. Esta sección es informativa y no es asesoramiento legal.</p>',
            "white rule"),
        _sec("Qué datos recoge el check-in online de Hostlio Pro",
            '<p class="lead" style="font-size:var(--t-0);max-width:70ch">Así encaja el formulario de check-in con lo que pide el parte de viajeros. Lo que falta lo completas tú antes de comunicarlo.</p>'
            + _table(["Dato del parte de viajeros", "¿Lo recoge Hostlio Pro?"], [
                ("Nombre y apellidos", "Sí, en un solo campo (no separa primer y segundo apellido)"),
                ("Tipo y número de documento", "Sí: pasaporte o documento de identidad, leído de la zona MRZ o escrito a mano"),
                ("Nacionalidad y fecha de nacimiento", "Sí"),
                ("Domicilio", "Sí, del titular de la reserva (campo opcional)"),
                ("Acompañantes", "Sí: nombre, documento, nacionalidad y fecha de nacimiento de hasta 10 personas"),
                ("Sexo", "No"),
                ("Número de soporte del documento", "No"),
                ("Parentesco con menores", "No"),
                ("Teléfono o email", "No en el formulario; suelen estar en la reserva"),
                ("Datos de pago", "No"),
            ])),
        _sec("Cómo usar esos datos para tu comunicación", _steps([
            ("El huésped completa el check-in", "Antes de llegar, escanea su documento con el móvil, añade acompañantes y firma. No se guarda ninguna imagen del documento."),
            ("Exportas los datos", "Desde el panel descargas un CSV con los huéspedes registrados en un rango de fechas (nombre, tipo y número de documento, nacionalidad, fecha de nacimiento y fecha de entrada). Las reservas canceladas no se incluyen."),
            ("Comunicas a SES.Hospedajes", "Completa los datos que faltan y haz la comunicación en SES.Hospedajes como hasta ahora. Hostlio Pro no genera el fichero XML del Ministerio ni se conecta a su servicio web."),
        ]), "dark on-dark"),
        _sec("Check-in online integrado en el PMS, sin herramienta extra", _rows([
            ("Todo en la misma reserva", "Muchos programas de gestión hotelera resuelven el check-in online con una herramienta externa conectada por integración, con su propia suscripción. En Hostlio Pro el check-in forma parte del propio PMS: el enlace sale de la reserva y los datos, la firma y los acompañantes vuelven a esa misma reserva."),
            ("Enlace automático por email", "Activa el email de check-in y cada reserva nueva con dirección de email recibe su enlace en el idioma del huésped. Tú eliges los canales: reservas directas, Booking.com, Expedia, Airbnb, Agoda u otras OTAs."),
            ("En recepción, sin teclear", "Si un huésped no completa el enlace, el personal puede escanear su documento desde el panel; se lee en el dispositivo y tampoco se guarda imagen."),
            ("Privacidad", "Los datos del documento solo los ve el personal de tu alojamiento, las firmas se eliminan 30 días después del check-out y el texto de consentimiento forma parte del formulario. Para el RGPD, tu alojamiento es el responsable y Hostlio Pro el encargado del tratamiento."),
        ])),
        _sec("Qué ganas con el check-in online", _table(["En recepción, sin check-in online", "Con el check-in online de Hostlio Pro"], [
            ("Fotocopias o fotos del documento", "Solo los datos extraídos; ninguna imagen guardada"),
            ("Teclear nombres y números de pasaporte", "Los datos llegan rellenados desde la zona MRZ"),
            ("Cola a la llegada de un grupo o un vuelo", "Cada huésped llega con el formulario hecho"),
            ("Firma en papel que hay que archivar", "Firma digital en la reserva, eliminada a los 30 días del check-out"),
            ("Formularios en un solo idioma", "Formulario en español, inglés, francés, italiano, portugués y turco"),
        ]), "white rule"),
    ])


CHECKIN_ES_FAQ = [
    ("¿Hostlio Pro envía el parte de viajeros a SES.Hospedajes?", "No. Hostlio Pro recoge parte de los datos con el check-in online y te permite exportarlos en CSV, pero no se conecta a SES.Hospedajes ni genera el fichero XML del Ministerio. La comunicación sigue siendo responsabilidad del alojamiento."),
    ("¿Qué datos del parte de viajeros tendré que completar yo?", "El formulario no recoge el sexo, el número de soporte del documento, el segundo apellido por separado, el parentesco con menores ni los datos de pago. Tendrás que añadirlos antes de comunicar a SES.Hospedajes."),
    ("¿Necesito otra herramienta de check-in además del PMS?", "No. En Hostlio Pro el check-in online está integrado en el PMS en los planes Pro y Growth: el enlace sale de la reserva y los datos vuelven a ella, sin otra suscripción ni integración."),
    ("¿Sirve para el DNI y la TIE?", "Los documentos con zona de lectura mecánica (MRZ) se escanean con la cámara del móvil; los que no la tienen se introducen a mano en el mismo formulario."),
]


def _channel_es(U):
    return "".join([
        _sec("Cómo funciona la sincronización, paso a paso", _steps([
            ("Crea tu inventario", "Tipos de habitación, habitaciones y planes tarifarios en Hostlio Pro. Es la única fuente de disponibilidad para todos los canales."),
            ("Conecta cada OTA", "Autoriza la conexión en la extranet de Booking.com, Airbnb, Expedia o el canal que uses y asigna tus habitaciones. La mayoría de los alojamientos lo hacen el mismo día."),
            ("Vende y olvídate de copiar", "Cada reserva, modificación o cancelación llega sola al planning y la disponibilidad se actualiza en los demás canales."),
        ]), "dark on-dark"),
        _sec("PMS integrado con channel manager: por qué importa", _rows([
            ("Una sola disponibilidad", "Cuando el channel manager y el PMS son el mismo sistema, no hay dos calendarios que puedan desincronizarse. Una reserva por teléfono, una habitación fuera de servicio o una cancelación cambian la disponibilidad en todos los canales a la vez."),
            ("Habitaciones fuera de servicio", "Si registras una avería y pones la habitación fuera de servicio, sale de la venta en todas las OTAs conectadas y no se puede asignar hasta que vuelve a estar operativa."),
            ("Mensajes junto a la reserva", "Los mensajes de los huéspedes de Booking.com, Airbnb y Expedia llegan a la bandeja de Lio con la reserva al lado (planes Pro y Growth). Lio responde en el idioma del huésped."),
            ("Informes por canal", "Ves ingresos brutos, comisión y neto de cada OTA, ocupación, ADR y RevPAR, y una vista a 30, 60 y 90 días. Exporta a Excel cuando lo necesites."),
        ]), "white rule"),
        _sec("Tarifas y restricciones: qué es cada una",
            _table(["Restricción", "Para qué sirve", "Ejemplo"], [
                ("Precio", "La tarifa por noche de cada tipo de habitación y plan", "Doble estándar a 95 € de lunes a jueves"),
                ("Estancia mínima / máxima", "Limita cuántas noches puede reservar el huésped", "Mínimo 2 noches los fines de semana de agosto"),
                ("Cerrado a la llegada (CTA)", "Nadie puede llegar ese día, aunque sí alojarse", "Sin llegadas el sábado de un festival"),
                ("Cerrado a la salida (CTD)", "Nadie puede salir ese día", "Evitar salidas el domingo para no dejar huecos"),
                ("Cierre de ventas", "Cierra la venta de ese tipo de habitación o plan", "Cerrar la tarifa no reembolsable en temporada alta"),
            ])
            + '<p style="margin-top:18px">Con la edición masiva eliges un rango de fechas, los tipos de habitación y los planes, y aplicas todo de una vez; la opción «solo fines de semana» cambia solo las noches de viernes y sábado. Si un canal no recibe una actualización, el botón «reenviar a los canales» vuelve a enviar las tarifas y la disponibilidad actuales.</p>'),
        _sec("¿Existe un channel manager gratis?", _rows([
            ("Lo que suele haber detrás", "Los channel managers «gratis» suelen cobrar una comisión por reserva, limitar el número de canales o venir atados a un motor de reservas. Con comisión, el coste sube justo cuando más vendes."),
            ("Cómo lo hacemos nosotros", "Hostlio Pro no es gratis, pero el precio es fijo y público: desde ⟦price:starter⟧ al mes, sin comisión por reserva, con el channel manager incluido en todos los planes y 7 días de prueba gratuita."),
        ]), "white rule"),
        _sec("Cambiar de channel manager sin overbooking", _table(["Paso", "Qué hacer"], [
            ("1. Prepara el inventario", "Crea tipos de habitación y planes en Hostlio Pro con los mismos nombres que usas en las OTAs."),
            ("2. Importa las reservas futuras", "Exporta las reservas de tu sistema actual en CSV o Excel y súbelas; los duplicados se omiten."),
            ("3. Conecta en horas tranquilas", "Desconecta el canal en el sistema anterior y conéctalo en Hostlio Pro, uno a uno o todos el mismo día."),
            ("4. Revisa el planning", "El control de conflictos lista reservas duplicadas o sin habitación asignada."),
            ("5. Compara la disponibilidad", "Comprueba en la extranet de cada OTA que la disponibilidad coincide con tu planning."),
        ]) + f'<p style="margin-top:18px">Más detalles en nuestra guía <a href="{U("post-overbooking")}">cómo evitar el overbooking</a>.</p>'),
    ])


CHANNEL_ES_FAQ = [
    ("¿Hay un channel manager gratis?", "Hostlio Pro no es gratuito, pero puedes probarlo 7 días sin cargo. Después, el channel manager está incluido en todos los planes desde ⟦price:starter⟧ al mes, sin comisión por reserva."),
    ("¿Cuánto tarda en conectarse un canal?", "Tu cuenta está lista en minutos. Para cada OTA autorizas la conexión en su extranet y asignas tus habitaciones; la mayoría de los alojamientos conectan sus canales el mismo día."),
    ("¿Qué pasa si una OTA no recibe una actualización?", "El botón «reenviar a los canales» vuelve a enviar las tarifas, restricciones y disponibilidad actuales. Si el problema persiste, el centro de notificaciones te avisa de las incidencias del canal."),
]


PAGE_MORE = {
    "es": {"checkin": (_checkin_es, CHECKIN_ES_FAQ), "channel": (_channel_es, CHANNEL_ES_FAQ)},
}


def more(L, page):
    f = PAGE_MORE.get(L, {}).get(page)
    return f[0](lambda k: url(k, L)) if f else ""


def faq(L, page):
    f = PAGE_MORE.get(L, {}).get(page)
    return list(f[1]) if f else []
