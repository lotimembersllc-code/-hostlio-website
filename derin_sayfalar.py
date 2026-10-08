"""SEO S7 + S8 (8 Ekim 2026): ince para sayfalarını segmente özgü bölümlerle derinleştirme.
İlk dalga: en/hostel-software, en/boutique-hotel-software, es/check-in-online, es/channel-manager.
İkinci dalga (site-derin-2): aynı dört sayfanın tüm kardeş dilleri (tr, en, fr, es, it, pt); metinler pazara özgü
yazıldı (TR: KBS, IT: Alloggiati Web, FR: fiche individuelle de police, PT-BR: FNRH Digital + kısa SIBA notu).
Her yerde aynı ilke: Hostlio Pro yalnız CSV dışa aktarır; resmî sistemlere gönderim YOK.

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


# ------------------------------------------------------------------ S7 ikinci dalga: kardeş diller (8 Ekim 2026)
def _checkin_en(U):
    return "".join([
        _sec("Why hotels ask for a passport, and what online check-in changes", _rows([
            ("Guest registration is a legal duty in many countries", "In much of Europe and beyond, accommodation providers must record who stays with them and, in several countries, report it to the police or the interior ministry. Spain uses SES.Hospedajes, Türkiye the KBS identity notification system. That is why reception asks for a passport or ID card, and why the details have to be right."),
            ("The desk is the bottleneck", "Typing a passport number, a date of birth and a nationality for every guest takes a few minutes per person, and mistakes are easy at the end of a long shift. Photocopies and phone photos of documents then sit in a drawer or a shared folder."),
            ("Online check-in moves the work before arrival", "The guest reads their own passport with their own phone, adds the people travelling with them and signs. Reception checks the result and hands over the key. Nothing is retyped, and no document image is kept."),
        ]), "rule"),
        _sec("What is stored, and for how long",
            '<p class="lead" style="font-size:var(--t-0);max-width:70ch">A clear answer for your privacy notice and for guests who ask.</p>'
            + _table(["Item", "Stored in Hostlio Pro?", "Notes"], [
                ("Image of the passport or ID card", "No", "The machine-readable zone is read in the guest’s browser; no picture is uploaded"),
                ("Name, document type and number, nationality, date of birth", "Yes, on the reservation", "Visible only to your property’s staff, according to their role"),
                ("Booker’s home address", "Optional field", "Useful where local registration rules ask for it"),
                ("Accompanying guests", "Yes, up to 10 per form", "Name, document, nationality and date of birth"),
                ("Digital signature", "Yes, temporarily", "Deleted automatically 30 days after check-out"),
                ("Consent to house rules and data processing", "Yes", "The consent text is part of the form"),
            ])
            + '<p style="margin-top:18px">Under GDPR your property is the controller and Hostlio Pro the processor. Details are in our <a href="' + U("security") + '">security and data protection page</a>.</p>'),
        _sec("Official guest reporting: what Hostlio Pro does and does not do", _rows([
            ("What it does", "It collects the guest details listed above and lets you download a CSV of the guests registered in a date range (name, document type and number, nationality, date of birth and arrival date). Cancelled reservations are left out."),
            ("What it does not do", "Hostlio Pro does not send anything to the police, the interior ministry or any government portal, and it does not generate official files such as the Spanish SES.Hospedajes XML. You remain responsible for your reporting, in the official system and within the official deadline."),
            ("Why we say this plainly", "Some fields that local systems require, such as sex, a second surname or the document support number in Spain, are not part of the form. Check the export against your country’s requirements before you rely on it."),
        ]), "white rule"),
        _sec("Guest registration in some of our markets",
            _table(["Country", "Official system", "With Hostlio Pro"], [
                ("Spain", "SES.Hospedajes (Ministry of the Interior), under Royal Decree 933/2021", "CSV export to help you complete the report; no direct submission. See our <a href=\"" + url("checkin", "es") + "\" hreflang=\"es\">Spanish page</a> for a field-by-field table"),
                ("Türkiye", "KBS identity notification system (police or gendarmerie), under Law 1774", "CSV export by date range that you use when entering KBS; no automatic notification"),
            ])
            + '<p class="small muted">Sources: <a href="https://www.boe.es/buscar/act.php?id=BOE-A-2021-17461" rel="noopener">BOE, Royal Decree 933/2021</a> and <a href="https://www.mevzuat.gov.tr/MevzuatMetin/1.5.1774.pdf" rel="noopener">Law 1774 on Identity Notification</a>. Checked October 2026. This section is for information only and is not legal advice.</p>'),
        _sec("Setting it up in an afternoon", _steps([
            ("Write your house rules", "Add check-in times, house rules and the consent text guests will see. The form is available in English, Spanish, French, Italian, Portuguese and Turkish."),
            ("Choose how the link goes out", "Share the link from the reservation yourself, or switch on the automatic email and pick the booking sources it applies to."),
            ("Check arrivals on the Today screen", "See who has checked in online before they arrive. If someone hasn’t, staff can scan the document from the dashboard at the desk; again, no image is stored."),
        ]), "dark on-dark"),
        _sec("Online check-in inside the PMS, not a separate tool", _rows([
            ("One reservation, one record", "Standalone check-in apps need their own subscription and an integration with your PMS. In Hostlio Pro, check-in is part of the system: the link comes from the reservation and the details, companions and signature go back to it."),
            ("Works with every channel", "The same form works for direct bookings and for reservations from Booking.com, Expedia, Airbnb, Agoda and the other connected channels."),
            ("Visa letters and receipts", "From the same reservation you can create an accommodation confirmation for a visa or invitation application, or a printable receipt, in the guest’s language."),
        ]), "white rule"),
    ])


CHECKIN_EN_FAQ = [
    ("Why do hotels scan your passport?", "Because in many countries accommodation providers must record each guest’s identity and, in some, report it to the authorities. With Hostlio Pro’s online check-in the guest reads the passport on their own phone; only the extracted details are saved, never an image."),
    ("Does Hostlio Pro submit guest data to the police or SES.Hospedajes?", "No. It collects guest details and exports them as a CSV for a date range. The official report is still made by your property in the official system."),
    ("How long are signatures kept?", "Digital signatures are deleted automatically 30 days after check-out. Guest details stay on the reservation, and staff can delete a guest’s data on request."),
]


def _channel_en(U):
    return "".join([
        _sec("How a channel manager works, step by step", _steps([
            ("One inventory", "You set up room types, rooms and rate plans once in Hostlio Pro. This is the single source of availability for every channel."),
            ("Connect each channel", "Authorise the connection in the Booking.com, Airbnb or Expedia extranet (or any other connected channel) and map your rooms. Most properties connect their channels the same day."),
            ("Sell everywhere, type nothing twice", "Each booking, modification or cancellation arrives on the room rack on its own, and availability updates on every other channel."),
        ]), "dark on-dark"),
        _sec("PMS vs channel manager: do you need both?", _rows([
            ("What each one does", "A PMS (property management system) runs the property: reservations, the room rack, guests, housekeeping and reports. A channel manager distributes availability and rates to the OTAs and brings their bookings back. Every hotel that sells on more than one channel needs both jobs done."),
            ("Why it matters if they are one system", "With separate tools, two calendars have to agree. A phone booking typed into the PMS, a room taken out of order or a late cancellation can reach the channels late, and that is when overbooking happens. In Hostlio Pro the PMS and the channel manager are the same system, so there is only one availability."),
            ("Messages next to the booking", "On Pro and Growth, guest messages from Booking.com, Airbnb and Expedia reach Lio’s inbox with the reservation alongside, and Lio replies in the guest’s language."),
            ("Revenue per channel", "Analytics shows gross revenue, commission and net revenue for each OTA, together with occupancy, ADR and RevPAR and a 30, 60 and 90-day forward view. Export to Excel whenever you need to."),
        ]), "white rule"),
        _sec("Rates and restrictions in plain words",
            _table(["Restriction", "What it does", "Example"], [
                ("Rate", "The nightly price for each room type and rate plan", "Standard double at €120 Monday to Thursday"),
                ("Minimum / maximum stay", "How many nights a guest can book", "Minimum 3 nights over a bank holiday weekend"),
                ("Closed to arrival (CTA)", "No check-ins that day, stays through it are fine", "No arrivals on a marathon Saturday"),
                ("Closed to departure (CTD)", "No check-outs that day", "Avoid Sunday departures that leave one-night gaps"),
                ("Stop sell", "Closes a room type or rate plan for sale", "Close the non-refundable rate in peak season"),
            ])
            + '<p style="margin-top:18px">Bulk editing applies all of this to a date range, several room types and several rate plans in one go; “weekends only” changes just Friday and Saturday nights.</p>'),
        _sec("How much does a channel manager cost?", _rows([
            ("Three common pricing models", "A flat monthly fee per property; a fee that grows with the number of rooms or channels; or a commission on every booking that passes through. Some “free” channel managers are paid for by a booking commission or come tied to a booking engine."),
            ("Why the model matters more than the headline price", "A commission rises exactly when you sell more. At 1% of €200,000 in yearly bookings, that is €2,000 a year on top of any subscription. A flat fee stays the same in August and in November."),
            ("Hostlio Pro’s model", "A public, flat price from ⟦price:starter⟧ a month with no booking commission. The channel manager is included in every plan together with the PMS, and Lio, the AI guest assistant. You can try it free for 7 days."),
        ]), "white rule"),
        _sec("Questions to ask before you choose", _table(["Question", "Hostlio Pro"], [
            ("Is the price published, and is there a booking commission?", "Published on the pricing page; no commission"),
            ("Are Booking.com, Airbnb, Expedia and Hostelworld connected?", "Yes, with 100+ channels over certified connections"),
            ("Are the PMS and channel manager one system?", "Yes, one availability for every channel"),
            ("Do out-of-order rooms close on the channels?", "Yes, automatically, until the room is back in service"),
            ("Can I see net revenue per channel after commission?", "Yes, in Analytics, with Excel export and weekly and monthly email reports"),
            ("Can I bring my future bookings when I switch?", "Yes, from a CSV or Excel file; duplicates are skipped"),
        ]) + f'<p style="margin-top:18px">More on avoiding double bookings in our guide <a href="{U("post-overbooking")}">how to prevent overbooking across channels</a>, and a side-by-side view on the <a href="{U("compare")}">hotel software comparison</a> page.</p>'),
    ])


CHANNEL_EN_FAQ = [
    ("How does a channel manager prevent overbooking?", "It keeps one availability for every channel. When a room sells on Booking.com, availability drops on Airbnb, Expedia and the others straight away, and a cancellation reopens it everywhere."),
    ("Do I need a PMS and a channel manager?", "You need both jobs done. In Hostlio Pro they are one system, so reservations, the room rack and channel availability can’t drift apart."),
    ("What if an OTA misses an update?", "The “resend to channels” button sends current rates, restrictions and availability again, and the notification centre flags channel problems."),
]


def _hostel_es(U):
    return "".join([
        _sec("Un día en la recepción de un hostel con Hostlio Pro", _rows([
            ("08:00, el día ordenado", "La pantalla Hoy reúne llegadas, salidas, habitaciones por limpiar, mensajes sin responder y borradores de Lio pendientes de aprobar. Sabes de un vistazo qué toca antes de que lleguen los primeros mochileros."),
            ("Mediodía, cambio de habitaciones", "El equipo de pisos ve primero las salidas del día, con prioridad para las habitaciones que tienen llegada ese mismo día. Cuando una habitación está limpia, recepción lo ve al momento. Si se rompe una ducha, se registra la avería con una foto y la habitación queda fuera de servicio: deja de venderse en todos los canales hasta que se repara."),
            ("Tarde, llegadas", "Quien ha hecho el check-in online (planes Pro y Growth) ya ha escaneado su pasaporte y firmado, así que recepción entrega llaves en lugar de copiar números de documento. No se guarda ninguna imagen del documento."),
            ("Noche, la bandeja no para", "Los viajeros escriben a cualquier hora y en su idioma: llegada tarde, consigna, taquillas, cocina, el bus nocturno. Lio contesta con la información que has cargado y deja para el turno de noche o de la mañana lo que requiere una decisión."),
        ]), "white rule"),
        _sec("Lo que preguntan los huéspedes de un hostel y de dónde saca Lio la respuesta",
            '<p class="lead" style="font-size:var(--t-0);max-width:70ch">Lio solo responde con la información de tu alojamiento y de la reserva del huésped. Cuanto más completes una vez, menos mensajes llegan a tu equipo.</p>'
            + _table(["Pregunta típica", "Con qué responde Lio"], [
                ("«Aterrizamos a la 1, ¿podemos hacer el check-in?»", "Tu horario de check-in y tus normas de llegada tardía"),
                ("«¿Podemos dejar las mochilas después del check-out?»", "Tu política de consigna de equipaje"),
                ("«¿Hay taquillas? ¿Tengo que traer candado?»", "Los datos de habitaciones e instalaciones que añadas"),
                ("«¿Hay cocina para huéspedes?»", "Instalaciones y normas de la casa"),
                ("«¿Cómo llego desde el aeropuerto?»", "Tus notas de transporte y, si lo vendes, tu traslado"),
                ("«¿Mañana hay free tour?»", "Tu lista de extras; en Pro y Growth Lio pasa la solicitud a tu equipo"),
                ("«¿Puedo cambiar las fechas?»", "Pasa a tu equipo: Lio no modifica reservas"),
            ])),
        _sec("Hostelworld, Booking.com y reservas directas en un solo calendario", _rows([
            ("Una sola disponibilidad", "Hostlio Pro se conecta con Hostelworld, Booking.com, Airbnb, Expedia y más de 100 canales mediante conexiones certificadas. Lo que se vende en un canal se cierra en los demás, y una cancelación lo vuelve a abrir en todos."),
            ("Precios de fin de semana y de eventos", "Carga una temporada entera de una vez: fechas, tipos de habitación y planes, con la opción «solo fines de semana» para viernes y sábado. Para las fiestas locales o un festival, añade estancia mínima, cerrado a la llegada o cierre de ventas."),
            ("Qué canal te deja más", "Los informes muestran ocupación, ADR y RevPAR, y para cada OTA los ingresos brutos, la comisión y el neto. Así decides dónde empujar la reserva directa. Exporta a Excel para tu gestoría."),
        ])),
        _sec("Voluntarios, turno de noche y limpieza", _rows([
            ("Cada uno con su rol", "Asigna a cada persona un rol: dirección, recepción, pisos, contabilidad o solo lectura. Pisos solo ve habitaciones; contabilidad no ve los mensajes de los huéspedes. Cuando un voluntario se va, suspendes su acceso con un clic. Starter incluye 3 usuarios, Pro 8 y Growth 20."),
            ("Quién cambió qué", "El historial de actividad registra cada cambio campo a campo, con persona y hora, durante 365 días. Útil cuando varios turnos tocan la misma reserva."),
            ("Cada uno en su idioma", "El panel y la app móvil están en español, inglés, francés, italiano, portugués y turco, así que un equipo internacional trabaja en su propio idioma."),
        ]), "white rule"),
        _sec("¿Es Hostlio Pro el software adecuado para tu hostel?",
            '<p class="lead" style="font-size:var(--t-0);max-width:70ch">Preferimos decírtelo ahora y no después de una migración: Hostlio Pro gestiona la disponibilidad por habitación, no por cama.</p>'
            + _table(["Área", "Encaja bien", "Consúltanos antes"], [
                ("Inventario", "Habitaciones privadas, familiares y dormitorios completos vendidos como una unidad", "Vender camas sueltas en dormitorios compartidos como inventario separado no está disponible"),
                ("Reservas", "Una habitación por reserva, de cualquier canal o creada a mano", "Los grupos que ocupan varias habitaciones se registran como reservas separadas"),
                ("Tamaño", "De 1 a 150 habitaciones, uno o dos alojamientos en Growth", "Más de dos alojamientos o más de 150 habitaciones"),
                ("Cobros", "Precios, extras y recibos imprimibles en la reserva", "No hay cobro con tarjeta, folio ni TPV integrados"),
                ("Huéspedes", "Viajeros internacionales que escriben por WhatsApp y desde las OTAs", "—"),
            ])),
        _sec("El parte de viajeros también va contigo", _rows([
            ("SES.Hospedajes", "Como cualquier alojamiento en España, un hostel tiene que comunicar los datos de sus huéspedes al Ministerio del Interior a través de SES.Hospedajes. Con el check-in online recoges buena parte de esos datos antes de la llegada y los exportas en CSV."),
            ("Lo que no hacemos", f"Hostlio Pro no envía el parte a SES.Hospedajes ni genera su fichero XML; la comunicación la sigues haciendo tú. Te lo explicamos campo por campo en la página de <a href=\"{U('checkin')}\">check-in online</a>."),
        ])),
        _sec("Cambiar de software de hostel sin perder reservas", _steps([
            ("Crea habitaciones y tarifas", "Da de alta tipos de habitación, habitaciones y planes tarifarios. El asistente de configuración te avisa de lo que falta antes de empezar."),
            ("Importa tus reservas", "Exporta las reservas futuras de tu sistema actual en CSV o Excel y súbelas. Las columnas se asignan solas y las filas con problemas aparecen con el motivo."),
            ("Conecta tus canales", "Autoriza Hostelworld, Booking.com y el resto de OTAs y asigna tus habitaciones. La mayoría de los alojamientos lo hacen el mismo día."),
        ]), "dark on-dark"),
        f'<section class="rule"><div class="wrap"><p>Más información: <a href="{U("post-overbooking")}">cómo evitar el overbooking entre canales</a> y <a href="{U("post-autoreply")}">respuestas automáticas a los mensajes de Booking.com</a>.</p></div></section>',
    ])


HOSTEL_ES_FAQ = [
    ("¿Lio puede responder sobre taquillas, cocina o llegadas de madrugada?", "Sí, siempre que esa información esté en los datos de tu alojamiento. Lio responde en el idioma del huésped y solo con lo que has cargado; si falta algo, pasa el mensaje a tu equipo y el panel te indica qué dato añadir."),
    ("¿Puedo gestionar reservas de grupo?", "Cada reserva ocupa una habitación, así que un grupo repartido en varias habitaciones se registra como varias reservas. Para grupos grandes, cuéntanos cómo los vendes y lo revisamos contigo en una demo."),
    ("¿Hostlio Pro envía el parte de viajeros a SES.Hospedajes?", "No. Recoge parte de los datos con el check-in online y te permite exportarlos en CSV, pero la comunicación a SES.Hospedajes la sigue haciendo el alojamiento."),
]


def _boutique_es(U):
    return "".join([
        _sec("IA para hoteles boutique sin perder el trato personal", _rows([
            ("Tu tono, tus detalles", "Lio escribe en el idioma del huésped con la información de tu hotel: horario de check-in, desayuno en la terraza, aparcamiento, mascotas, cómo llegar por el casco antiguo. No se inventa ofertas ni políticas que no hayas cargado."),
            ("Tú decides qué es automático", "Empieza en modo aprobación y lee cada respuesta antes de enviarla. Después deja que Lio cierre solo las preguntas rutinarias y reserva para tu equipo los descuentos, las quejas y las peticiones especiales."),
            ("Una bandeja para todos los huéspedes", "Los mensajes de WhatsApp y, en Pro y Growth, los de Booking.com, Airbnb y Expedia llegan a un solo sitio, junto a la reserva del huésped. Se acabó saltar de extranet en extranet."),
            ("Límites claros", "Lo que escribes tú se envía tal cual. De las respuestas de Lio ves una traducción a tu idioma, y cuando Lio no está seguro pasa el mensaje a tu equipo en lugar de adivinar."),
        ]), "white rule"),
        _sec("Un hotel boutique de 30 habitaciones, un día cualquiera",
            '<p class="lead" style="font-size:var(--t-0);max-width:70ch">Un ejemplo para ver cómo encajan las piezas; tus cifras serán otras.</p>'
            + _table(["Hora", "Qué pasa", "Dónde, en Hostlio Pro"], [
                ("01:40", "Una huésped de Chicago pregunta si puede llegar después de medianoche", "Lio responde en inglés con tus normas de llegada"),
                ("08:00", "La propietaria revisa el día: 9 llegadas, 7 salidas, 2 borradores por aprobar", "Pantalla Hoy y Sugerencias de Lio"),
                ("10:30", "Gotea un grifo en la habitación 12", "Parte de avería; la habitación sale de la venta en todos los canales"),
                ("12:00", "Pisos prepara las salidas del día, primero las prioritarias", "Lista de pisos, imprimible en PDF"),
                ("15:00", "Los huéspedes que llegan ya han hecho el check-in online", "Check-in online con firma digital (Pro y Growth)"),
                ("19:00", "Un huésped pide traslado al aeropuerto para el domingo", "Lio lo ofrece y pasa la solicitud a tu equipo"),
                ("Lunes", "Se compara el neto por canal con la semana anterior", "Informes y email semanal"),
            ])),
        _sec("Más ingresos por estancia, sin presionar", _rows([
            ("Extras en el momento oportuno", "Traslados, excursiones, catas o cualquier extra que vendas se ofrecen cuando vienen a cuento en la conversación, y la solicitud llega a tu equipo (Pro y Growth)."),
            ("Solicitudes de reserva por WhatsApp", "Cuando un huésped pregunta por fechas en WhatsApp, Lio recoge fechas, personas y tipo de habitación y le da tu tarifa. Solo se convierte en reserva cuando tú la apruebas (Pro y Growth)."),
            ("Sugerencias cada mañana", "Las Sugerencias de Lio señalan oportunidades de precio, operación e ingresos. Nada cambia sin tu aprobación, y las sugerencias de tarifa respetan los límites que fijes."),
            ("Neto por canal", "Ves los ingresos brutos, la comisión y el neto de cada OTA, más una vista a 30, 60 y 90 días con el ritmo de reservas, para saber dónde compensa más la venta directa."),
        ])),
        _sec("Una llegada que parezca una bienvenida, no un trámite", _rows([
            ("Check-in antes de llegar", "El huésped escanea la zona MRZ de su pasaporte o documento con su propio móvil, añade acompañantes y firma. No se guarda ninguna imagen del documento y las firmas se eliminan 30 días después del check-out."),
            ("Enlace enviado automáticamente", "Activa el email de check-in y cada reserva nueva con email recibe el enlace en el idioma del huésped. Tú eliges a qué canales se aplica."),
            ("Y el parte de viajeros", f"Los datos recogidos se exportan en CSV para ayudarte con la comunicación a SES.Hospedajes, que sigue haciendo el hotel. Detalle en <a href=\"{U('checkin')}\">check-in online</a>."),
        ]), "white rule"),
        _sec("Lista de comprobación para elegir software de hotel boutique", _table(["Pregunta para cualquier proveedor", "Hostlio Pro"], [
            ("¿El precio es público y fijo, sin comisión por reserva?", "Sí: desde ⟦price:starter⟧ al mes, sin comisión y con 7 días de prueba gratuita"),
            ("¿Incluye channel manager?", "Sí, en todos los planes, con conexiones certificadas a más de 100 canales"),
            ("¿La IA responde en el idioma del huésped y con aprobación?", "Sí: WhatsApp en todos los planes, bandejas de OTAs en Pro y Growth"),
            ("¿Cada persona ve solo lo que necesita?", "Sí: seis roles; 3, 8 o 20 usuarios según el plan; historial de actividad"),
            ("¿Veo los ingresos por canal después de comisión?", "Sí, con exportación a Excel e informes semanales y mensuales por email"),
            ("¿Puedo traer mis reservas actuales?", "Sí, desde un archivo CSV o Excel"),
            ("¿Hay app móvil?", "Sí, para iOS y Android, incluida en todos los planes"),
        ])),
        f'<section class="white rule"><div class="wrap"><p>Más información: <a href="{U("post-ai")}">responder a los huéspedes con IA</a> y <a href="{U("post-pms")}">cómo elegir un software de gestión para un hotel pequeño</a>.</p></div></section>',
    ])


BOUTIQUE_ES_FAQ = [
    ("¿La IA hace que un hotel boutique parezca impersonal?", "Solo si improvisa. Lio responde a las preguntas rutinarias con tu información y en el idioma del huésped, y deja para tu equipo los descuentos, las quejas y las peticiones especiales. Muchos hoteles empiezan en modo aprobación y leen cada respuesta los primeros días."),
    ("¿Qué plan conviene a un hotel boutique de 30 habitaciones?", "Pro cubre hasta 50 habitaciones con ⟦quota:pro⟧ mensajes de IA al mes, bandejas de OTAs, check-in online y venta de extras. Growth cubre dos alojamientos o hasta 150 habitaciones."),
]


# ---- TR
# ------------------------------------------------------------------ TR (SEO S7 kardeş sayfalar, 8 Ekim 2026)
_KBS_SRC_TR = ('<p class="small muted">Kaynaklar: <a href="https://www.mevzuat.gov.tr/MevzuatMetin/1.5.1774.pdf" rel="noopener">1774 sayılı Kimlik Bildirme Kanunu</a>, '
               '<a href="https://www.resmigazete.gov.tr/eskiler/2025/12/20251205-6.htm" rel="noopener">7565 sayılı Kanun (RG 5.12.2025)</a>, '
               '<a href="https://www.asayis.pol.tr/kmlkbldrmsstm" rel="noopener">EGM Kimlik Bildirim Sistemi</a> ve '
               '<a href="https://www.jandarma.gov.tr/kimlik-bildirim-sistemi" rel="noopener">Jandarma Kimlik Bildirim Sistemi</a>. '
               'Ekim 2026’da kontrol edildi. Bilgilendirme amaçlıdır, hukuki danışmanlık değildir.</p>')


def _hostel_tr(U):
    return "".join([
        _sec("Hostel resepsiyonunda bir gün, Hostlio Pro ile", _rows([
            ("08:00, gün önünüzde", "Bugün ekranı gelenleri, gidenleri, temizlenecek odaları, cevap bekleyen mesajları ve onayınızı bekleyen Lio taslaklarını tek listede gösterir. Mobil uygulama aynı özeti otelin saatiyle 08:00’de telefonunuza gönderebilir."),
            ("Öğleye doğru, oda devri", "Kat ekibi önce bugün çıkışı olan odaları görür; aynı gün girişi olan odalar öncelikli işaretlenir. Temizlenen oda anında resepsiyona yansır. Duş bozulduysa fotoğrafıyla arıza kaydı açın ve odayı servis dışı yapın: tamir edilene kadar bağlı tüm kanallarda satıştan çıkar."),
            ("Öğleden sonra, girişler", "Online check-in yapan misafirler (Pro ve Growth) pasaportlarını ya da kimliklerini önceden taramış ve imzalamış olur. Resepsiyon pasaport numarası yazmak yerine anahtar verir; belge görüntüsü saklanmaz."),
            ("Gece, gelen kutusu durmaz", "Gezginler her saatte, farklı dillerde yazar: geç varış, bagaj bırakma, dolap, mutfak, en yakın otobüs durağı. Lio sizin girdiğiniz bilgilerle cevap verir; karar gerektiren her şeyi gece görevlisine ya da sabah vardiyasına bırakır."),
        ]), "white rule"),
        _sec("Gezginler ne sorar, Lio cevabı nereden alır?",
            '<p class="lead" style="font-size:var(--t-0);max-width:70ch">Lio yalnızca tesis bilgilerinizden ve misafirin rezervasyonundan cevap verir. Bu bilgileri bir kez ne kadar eksiksiz girerseniz ekibinize o kadar az mesaj düşer. Lio bir soruyu cevaplayamazsa panel hangi bilginin eksik olduğunu gösterir.</p>'
            + _table(["Sık gelen soru", "Lio’nun cevap için kullandığı bilgi"], [
                ("“Gece 1’de iniyoruz, yine de giriş yapabilir miyiz?”", "Check-in saatleriniz ve geç varış kurallarınız"),
                ("“Çıkıştan sonra çantalarımızı bırakabilir miyiz?”", "Bagaj emanet kuralınız"),
                ("“Dolap var mı, kendi kilidimi getirmeli miyim?”", "Oda ve olanak bilgileri"),
                ("“Misafirlerin kullanabileceği mutfak var mı?”", "Olanaklar ve ev kuralları"),
                ("“Havalimanından nasıl gelirim?”", "Ulaşım notlarınız; transfer satıyorsanız o da"),
                ("“Yarın şehir turu var mı?”", "Ek hizmet listeniz; Pro ve Growth’ta Lio talebi ekibinize iletir"),
                ("“Tarihlerimi değiştirebilir miyim?”", "Ekibinize devredilir: Lio rezervasyon değiştirmez"),
            ])),
        _sec("Hostelworld, Booking.com ve doğrudan rezervasyon tek takvimde", _rows([
            ("Her kanal için tek müsaitlik", "Hostlio Pro sertifikalı bağlantılarla Hostelworld, Booking.com, Airbnb, Expedia ve 100’den fazla başka kanala bağlanır. Bir kanalda satılan oda diğerlerinde kapanır, iptal edilen oda her yerde yeniden açılır."),
            ("Hafta sonu ve etkinlik fiyatı", "Bir sezonu tek seferde girin: tarih aralığını, oda tiplerini ve fiyat planlarını seçin, cuma ve cumartesi gecelerini ayrı fiyatlamak için “yalnız hafta sonu”nu işaretleyin. Festival ya da konser haftası için en az konaklama, varışa kapalı veya satışa kapatma kuralı ekleyin."),
            ("Hangi kanal gerçekten kazandırıyor?", "Analiz ekranı doluluk, ADR ve RevPAR’ın yanında her OTA için brüt gelir, komisyon ve neti gösterir. Doğrudan rezervasyonu nerede artırmanız gerektiğini görürsünüz; raporu muhasebeciniz için Excel’e aktarırsınız."),
        ])),
        _sec("Gece görevlisi, gönüllüler ve kat ekibi", _rows([
            ("Herkese kendi rolü", "Her kişiye bir rol verin: yönetici, resepsiyon, kat hizmetleri, muhasebe ya da izleyici. Kat görevlisi yalnız odaları görür, muhasebe misafir mesajlarını görmez. Gönüllü ayrıldığında erişimini tek tıkla askıya alın. Starter’da 3, Pro’da 8, Growth’ta 20 kullanıcı vardır."),
            ("Kim neyi değiştirdi?", "İşlem geçmişi her değişikliği alan alan, kişi ve saatle 365 gün kaydeder. Aynı rezervasyona birkaç vardiya dokunduğunda tartışmayı bitirir."),
            ("Herkes kendi dilinde", "Panel ve mobil uygulama Türkçe, İngilizce, İspanyolca, Fransızca, İtalyanca ve Portekizce kullanılabilir. Yabancı gönüllülerle çalışan bir ekip de kendi dilinde çalışır."),
            ("Yabancı misafir ve KBS", f"Türkiye’de hosteller de her misafiri Kimlik Bildirim Sistemi’ne (KBS) bildirmek zorundadır. Hostlio Pro bildirimi sizin yerinize yapmaz; online check-in’de toplanan bilgileri KBS girişinizde kullanmak üzere CSV olarak indirirsiniz. Ayrıntılar <a href=\"{U('checkin')}\">online check-in</a> sayfasında."),
        ]), "white rule"),
        _sec("Hostlio Pro sizin hostelinize uygun mu?",
            '<p class="lead" style="font-size:var(--t-0);max-width:70ch">Bunu geçişten sonra değil, şimdi söylemeyi tercih ederiz: Hostlio Pro müsaitliği yatak bazında değil, oda bazında yönetir.</p>'
            + _table(["Konu", "Uygun", "Önce bizimle konuşun"], [
                ("Envanter", "Özel odalar, aile odaları ve tek birim olarak satılan yatakhane odaları", "Ortak yatakhanede tek tek yatakları ayrı envanter olarak satmak desteklenmiyor"),
                ("Rezervasyon", "Her kanaldan gelen ya da elle girilen, rezervasyon başına bir oda", "Birden fazla odalı grup rezervasyonları ayrı rezervasyonlar olarak girilir"),
                ("Büyüklük", "1–150 oda; Growth’ta bir ya da iki tesis", "İkiden fazla tesis ya da 150’den fazla oda"),
                ("Ödeme", "Rezervasyonda fiyat, ek hizmetler ve yazdırılabilir makbuz", "Yerleşik kartla ödeme, folyo ya da POS yok"),
                ("Misafir", "WhatsApp’tan ve OTA gelen kutularından yazan yabancı gezginler", "—"),
            ])),
        _sec("Mevcut hostel programınızdan geçiş", _steps([
            ("Odaları ve fiyatları kurun", "Oda tiplerinizi, odalarınızı ve fiyat planlarınızı oluşturun. Kurulum sihirbazı canlıya geçmeden önce neyin eksik olduğunu gösterir."),
            ("Rezervasyonları içeri aktarın", "Eski sisteminizdeki gelecek rezervasyonları CSV ya da Excel olarak dışa aktarıp yükleyin. Sütunlar otomatik eşlenir, sorunlu satırlar nedeniyle listelenir."),
            ("Kanalları bağlayın", "Hostelworld, Booking.com ve diğer OTA’larınızı yetkilendirip odalarınızı eşleyin. Çoğu tesis aynı gün bağlanır."),
        ]), "dark on-dark"),
        f'<section class="rule"><div class="wrap"><p>Devamını okuyun: <a href="{U("post-overbooking")}">kanallar arasında overbooking nasıl önlenir</a> ve <a href="{U("post-autoreply")}">Booking.com mesajlarına otomatik cevap</a>.</p></div></section>',
    ])


HOSTEL_TR_FAQ = [
    ("Hostel programı ile otel programı arasında fark var mı?", "Temelde aynı işleri yapar: rezervasyon, kanal senkronu, check-in ve misafir iletişimi. Hostellerde fark, yoğun ve çok dilli mesaj trafiği, Hostelworld bağlantısı ve çoğu zaman yatak bazlı satıştır. Hostlio Pro ilk ikisinde güçlüdür; yatak bazlı satış yapmaz, odaları bütün olarak satar."),
    ("Lio dolap, mutfak ya da geç varış sorularını cevaplayabilir mi?", "Evet, bu bilgiler tesis ayarlarınızda olduğu sürece. Lio misafirin dilinde ve yalnızca girdiğiniz bilgilerle cevap verir; bilgi eksikse mesajı ekibinize devreder ve panel hangi bilgiyi eklemeniz gerektiğini gösterir."),
    ("Grup rezervasyonu alabilir miyim?", "Bir rezervasyon bir odayı tutar; birkaç odaya yayılan bir grup birkaç ayrı rezervasyon olarak girilir. Büyük grupları nasıl sattığınızı anlatın, kurulumu bir demoda birlikte kontrol edelim."),
    ("Gönüllüler ya da gece görevlisi sınırlı erişim alabilir mi?", "Evet. Onlara resepsiyon ya da izleyici rolünü, yalnız oda temizliyorlarsa kat hizmetleri rolünü verin. Erişimi istediğiniz an askıya alabilirsiniz; işlem geçmişi kimin neyi değiştirdiğini gösterir."),
]


def _boutique_tr(U):
    return "".join([
        _sec("Butik otelde yapay zekâ, kişisel ilgiden ödün vermeden", _rows([
            ("Sizin üslubunuz, sizin bilgileriniz", "Lio misafirin dilinde ve kendi tesis bilgilerinizle yazar: check-in saatleri, terasta kahvaltı, otopark, evcil hayvan, size nasıl ulaşılacağı. Girmediğiniz bir teklifi ya da kuralı uydurmaz."),
            ("Neyin otomatik olacağına siz karar verirsiniz", "Onay modunda başlayın, her cevabı gitmeden önce okuyun. Sonra rutin soruları Lio’ya bırakın; indirim, şikâyet ve özel talepleri ekibinizde tutun."),
            ("Her misafir için tek gelen kutusu", "WhatsApp mesajları, Pro ve Growth’ta Booking.com, Airbnb ve Expedia gelen kutuları tek yerde, misafirin rezervasyonunun yanında toplanır. Ekibiniz extranet’ler arasında dolaşmayı bırakır."),
            ("Sınırları bilin", "Sizin yazdığınız cevaplar yazdığınız gibi gönderilir, otomatik çevrilmez. Lio kendi cevaplarının çevirisini size gösterir; emin olmadığı konuda tahmin etmek yerine ekibe devreder."),
        ]), "white rule"),
        _sec("30 odalı bir butik otelde sıradan bir gün",
            '<p class="lead" style="font-size:var(--t-0);max-width:70ch">Parçaların nasıl birleştiğini gösteren bir örnek; sizin rakamlarınız farklı olacaktır.</p>'
            + _table(["Saat", "Ne olur", "Hostlio Pro’da nerede"], [
                ("02:10", "Seul’den bir misafir geç girişin mümkün olup olmadığını sorar", "Lio check-in kurallarınızdan Korece cevap verir"),
                ("08:00", "Otel sahibi günü okur: 9 giriş, 7 çıkış, onay bekleyen 2 taslak", "Bugün ekranı ve Lio Önerileri"),
                ("10:30", "14 numaralı odada lavabo sızdırıyor", "Arıza kaydı; oda tüm kanallarda satıştan çıkar"),
                ("12:00", "Kat ekibi çıkışı olan odaları, öncelikliler önde olmak üzere hazırlar", "Kat hizmetleri listesi, PDF olarak yazdırılabilir"),
                ("15:00", "Gelen misafirler online check-in’i çoktan yapmış", "Dijital imzalı online check-in (Pro ve Growth)"),
                ("18:00", "Bir misafir cuma için havalimanı transferi ister", "Lio transferi sunar, talebi ekibinize iletir"),
                ("Pazartesi", "Sahip kanal bazında net geliri geçen haftayla karşılaştırır", "Analiz ekranı ve haftalık e-posta raporu"),
            ])),
        _sec("Israrcı satış yapmadan konaklama başına daha fazla gelir", _rows([
            ("Ek hizmet, doğru anda", "Havalimanı transferi, tekne turu, balon turu ya da şarap tadımı gibi ek hizmetler sohbetle ilgili olduğunda sunulur; talep ekibinize ulaşır (Pro ve Growth)."),
            ("WhatsApp’tan rezervasyon talebi", "Misafir WhatsApp’tan tarih sorduğunda Lio tarihleri, kişi sayısını ve oda tercihini toplar, sizin fiyatınızı söyler. Talep ancak siz onaylayınca rezervasyona dönüşür (Pro ve Growth)."),
            ("Her sabah öneriler", "Lio Önerileri fiyat, operasyon ve gelir fırsatlarını gösterir. Onayınız olmadan hiçbir şey değişmez; fiyat önerileri belirlediğiniz sınırlar içinde kalır."),
            ("Komisyon sonrası kanal geliri", "Analiz ekranı her OTA’nın brüt gelirini, komisyonunu ve netini, ayrıca pickup ile 30, 60 ve 90 günlük ileriye bakışı gösterir. Doğrudan rezervasyonun en çok nerede kazandıracağını görürsünüz."),
        ])),
        _sec("Form değil, karşılama gibi hissettiren bir varış", _rows([
            ("Varıştan önce check-in", "Misafir pasaportunun ya da kimliğinin makine okunabilir alanını kendi telefonuyla tarar, refakatçilerini ekler ve imzalar. Belge görüntüsü saklanmaz, imzalar çıkıştan 30 gün sonra silinir."),
            ("Bağlantı kendiliğinden gider", "Check-in e-postasını açın; e-posta adresi olan her yeni rezervasyona bağlantı misafirin dilinde gider. Hangi rezervasyon kaynaklarına gideceğini siz seçersiniz."),
            ("KBS girişi için hazır bilgiler", f"Toplanan kimlik bilgilerini tarih aralığına göre CSV olarak indirip Kimlik Bildirim Sistemi girişinizde kullanırsınız; bildirimi yine tesisiniz yapar. Ayrıntılar <a href=\"{U('checkin')}\">online check-in</a> sayfasında."),
            ("Tek tıkla vize mektubu", "Vize ya da davet başvurusu için konaklama onayını rezervasyondan oluşturup PDF olarak kaydedin."),
            ("Küçük ekip, net roller", "Resepsiyon, kat hizmetleri ve muhasebe her biri kendi rolüyle çalışır: kat görevlisi yalnız odaları görür, muhasebe misafir mesajlarını görmez. İşlem geçmişi kimin neyi ne zaman değiştirdiğini 365 gün saklar; sezonluk çalışan ayrıldığında erişimini tek tıkla askıya alırsınız."),
        ]), "white rule"),
        _sec("Butik otel programı seçerken sorulacak sorular",
            '<p class="lead" style="font-size:var(--t-0);max-width:70ch">“Butik otel programı yorumları”nı okumadan önce her firmaya şu soruları sorun. Hostlio Pro’nun cevapları sağ sütunda.</p>'
            + _table(["Firmaya sorulacak soru", "Hostlio Pro"], [
                ("Fiyat açık ve sabit mi, rezervasyon komisyonu var mı?", "Evet, aylık ⟦price:starter⟧’dan başlar, komisyon yok, 7 gün ücretsiz deneme"),
                ("Kanal yöneticisi fiyata dahil mi?", "Evet, tüm planlarda, 100+ kanala sertifikalı bağlantıyla"),
                ("AI misafire kendi dilinde, onayımla cevap verebiliyor mu?", "Evet: WhatsApp tüm planlarda, OTA gelen kutuları Pro ve Growth’ta"),
                ("Her çalışan yalnız ihtiyacı olanı görebiliyor mu?", "Evet: altı rol, plana göre 3, 8 ya da 20 kullanıcı, işlem geçmişi"),
                ("Komisyon sonrası kanal gelirini görebiliyor muyum?", "Evet, Excel’e aktarma ve haftalık, aylık e-posta raporlarıyla"),
                ("Mevcut rezervasyonlarımı taşıyabilir miyim?", "Evet, CSV ya da Excel dosyasından"),
                ("KBS bildirimini otomatik yapıyor mu?", "Hayır. Check-in bilgilerini KBS girişinizde kullanacağınız CSV olarak verir; bildirimi tesis yapar"),
                ("Mobil uygulama var mı?", "Evet, iOS ve Android, tüm planlarda"),
            ])),
        f'<section class="white rule"><div class="wrap"><p>Devamını okuyun: <a href="{U("post-ai")}">otel misafir mesajlarını yapay zekâ ile yanıtlamak</a> ve <a href="{U("post-pms")}">küçük otel için otel yönetim yazılımı seçimi</a>.</p></div></section>',
    ])


BOUTIQUE_TR_FAQ = [
    ("Butik otel programı yorumlarını okurken nelere dikkat etmeliyim?", "Yorumun sizin büyüklüğünüzde ve misafir profilinizde bir tesisten gelip gelmediğine, kanal senkronunun ve desteğin nasıl anlatıldığına bakın. Ardından 7 günlük deneme ya da demoyla kendi odalarınız ve kanallarınızla deneyin; yorumlardan daha çok şey söyler."),
    ("Yapay zekâ butik oteli sıradanlaştırır mı?", "Ancak tahmin yürütürse. Lio rutin soruları kendi bilgilerinizle ve misafirin dilinde cevaplar; indirim, şikâyet ve özel talepleri ekibinize bırakır. Birçok otel ilk günlerde onay modunda başlayıp her cevabı okur."),
    ("30–50 odalı bir butik otel için hangi plan uygun?", "Pro planı 50 odaya kadar tesisler içindir: aylık ⟦quota:pro⟧ AI mesajı, WhatsApp ve OTA gelen kutuları, online check-in, transfer ve tur satışı. İki tesisiniz ya da 50’den fazla odanız varsa Growth 150 odaya kadar destekler."),
    ("Hostlio Pro KBS bildirimini benim yerime yapar mı?", "Hayır. Online check-in’de toplanan bilgileri tarih aralığına göre CSV olarak indirir, KBS girişinizde kullanırsınız. Bildirim yükümlülüğü tesiste kalır."),
]


def _checkin_tr(U):
    return "".join([
        _sec("Online check-in ve KBS bildirimi",
            '<div class="answer"><p><strong>Kısaca:</strong> Türkiye’de her konaklama tesisi misafirlerinin kimlik bilgilerini Kimlik Bildirim Sistemi’ne (KBS) anlık olarak bildirmek zorundadır. Hostlio Pro online check-in’de bu bilgilerin bir kısmını toplar ve KBS girişinizde kullanmanız için CSV olarak indirmenizi sağlar; ancak <strong>KBS’ye hiçbir şey göndermez</strong>. Bildirimi tesisiniz yapmaya devam eder.</p></div>'
            + _rows([
                ("KBS nedir?", "Kimlik Bildirim Sistemi, 1774 sayılı Kimlik Bildirme Kanunu’na dayanır. Kanunun ek 1. maddesine göre otel, motel, pansiyon, apart ve benzeri her türlü konaklama tesisi kayıtlarını bilgisayarda günü gününe tutmak ve genel kolluk kuvvetlerine anlık olarak bildirmek zorundadır. Çalışanlar da 24 saat içinde bildirilir."),
                ("Polis mi, jandarma mı?", "Tesisiniz polis bölgesindeyse Emniyet Genel Müdürlüğü’nün KBS’sini (kbs.egm.gov.tr), jandarma bölgesindeyse Jandarma Genel Komutanlığı’nın KBS’sini kullanırsınız. Kayıt için bağlı olduğunuz polis merkezine ya da jandarma karakoluna başvurulur."),
                ("Hangi bilgiler girilir?", "T.C. vatandaşları için T.C. kimlik numarası, oda numarası ve giriş tarihi temel bilgilerdir; ad ve doğum tarihi gibi bilgiler sistemden kontrol edilir. Yabancı kimlik numarası olmayan yabancı misafirlerde pasaport numarası ve kimlik bilgilerinin tamamı elle girilir. Ailelerde ve gruplarda her kişi ayrı bildirilir."),
                ("Bildirmezseniz ne olur?", "Kanun, sisteme bağlanmayan ve anlık veri göndermeyen ya da gerçeğe aykırı kayıt tutan tesislere idari para cezası öngörür; tutarlar her yıl yeniden değerlenir. Aralık 2025’teki değişiklikle aynı takvim yılında tekrarında son cezanın iki katı uygulanır, dördüncü kez işlenmesinde işletme ruhsatı iptal edilir."),
            ])
            + _KBS_SRC_TR,
            "white rule"),
        _sec("Hostlio Pro’nun online check-in’i hangi bilgileri toplar?",
            '<p class="lead" style="font-size:var(--t-0);max-width:70ch">Check-in formunun KBS girişinde gereken bilgilerle nasıl eşleştiği aşağıda. Eksik kalanları bildirimi yaparken siz tamamlarsınız.</p>'
            + _table(["KBS’de kullanılan bilgi", "Hostlio Pro topluyor mu?"], [
                ("T.C. kimlik numarası", "Evet, T.C. kimlik kartının makine okunabilir alanından ya da elle"),
                ("Pasaport ya da belge numarası", "Evet: pasaport veya kimlik kartı, MRZ’den okunur ya da elle yazılır"),
                ("Ad soyad", "Evet, tek alanda"),
                ("Uyruk ve doğum tarihi", "Evet"),
                ("Refakatçiler", "Evet: 10 kişiye kadar ad, belge, uyruk ve doğum tarihi"),
                ("Giriş tarihi", "Evet, rezervasyondan; dışa aktarılan dosyada yer alır"),
                ("Oda numarası", "Rezervasyonda görünür; KBS girişinde siz eklersiniz"),
                ("Araç plakası ve telefon", "Check-in formunda yok"),
            ])),
        _sec("KBS bildirimi nasıl yapılır: online check-in ile adım adım", _steps([
            ("Misafir check-in’i tamamlar", "Varıştan önce kişisel bağlantıyı açar, belgesini telefonuyla tarar, refakatçilerini ekler ve imzalar. Belge görüntüsü saklanmaz."),
            ("Bilgileri dışa aktarırsınız", "Panelden bir tarih aralığı seçip check-in yapan misafirlerin CSV dosyasını indirirsiniz (ad, belge türü ve numarası, uyruk, doğum tarihi, giriş tarihi). İptal edilen rezervasyonlar dosyaya girmez. İlk kullanımda dosyayı kendi KBS ekranınızla karşılaştırın."),
            ("KBS’ye bildirimi siz yaparsınız", "Eksik bilgileri tamamlayıp EGM ya da Jandarma KBS’sine her zamanki gibi girişi yaparsınız. Hostlio Pro KBS’ye bağlanmaz ve otomatik bildirim yapmaz."),
        ]), "dark on-dark"),
        _sec("Kimlik okuma: cihaz mı, telefon mu?", _rows([
            ("Ayrı kimlik okuma cihazı gerekmez", "Pasaport ve yeni tip kimlik kartlarının alt kısmında makine okunabilir bir alan (MRZ) vardır. Hostlio Pro bu alanı misafirin telefon kamerasıyla okur; resepsiyona ayrı bir pasaport okuma cihazı almanız gerekmez."),
            ("Resepsiyonda da tarayabilirsiniz", "Misafir bağlantıyı doldurmadıysa personel belgeyi panelden tarayabilir. Okuma cihazda yapılır, görüntü yine saklanmaz."),
            ("MRZ’si olmayan belgeler", "Eski tip nüfus cüzdanı gibi makine okunabilir alanı olmayan belgeler aynı formda elle girilir."),
            ("Fotokopi yok", "Kimliğin fotoğrafı ya da fotokopisi tutulmaz; yalnızca okunan bilgiler ve imza rezervasyona kaydedilir. Bilgileri yalnızca tesisinizin personeli görür. KVKK açısından tesisiniz veri sorumlusu, Hostlio Pro veri işleyendir."),
        ])),
        _sec("Online check-in otelde ne kazandırır?", _table(["Online check-in olmadan resepsiyonda", "Hostlio Pro online check-in ile"], [
            ("Kimlik fotokopisi ya da fotoğrafı", "Yalnızca okunan bilgiler, görüntü saklanmaz"),
            ("Pasaport numaralarını tek tek yazmak", "Bilgiler MRZ’den dolu gelir"),
            ("KBS için bilgileri yeniden toplamak", "Tarih aralığına göre tek CSV dosyası"),
            ("Grup ya da uçak gelince kuyruk", "Her misafir formu doldurmuş gelir"),
            ("Arşivlenecek kâğıt imza", "Rezervasyonda dijital imza, çıkıştan 30 gün sonra silinir"),
            ("Tek dilde form", "Türkçe, İngilizce, İspanyolca, Fransızca, İtalyanca ve Portekizce form"),
        ]), "white rule"),
        f'<section class="rule"><div class="wrap"><p>Online check-in, PMS’in içinde çalışır; ayrı bir abonelik ya da entegrasyon gerekmez. Bağlantı rezervasyondan çıkar, bilgiler, imza ve refakatçiler aynı rezervasyona döner. Planları <a href="{U("pricing")}">fiyatlandırma</a> sayfasında karşılaştırın.</p></div></section>',
    ])


CHECKIN_TR_FAQ = [
    ("Hostlio Pro KBS bildirimini otomatik yapıyor mu?", "Hayır. Hostlio Pro EGM ya da Jandarma KBS’sine bağlanmaz. Online check-in’de toplanan bilgileri tarih aralığına göre CSV olarak indirir, KBS girişinizde kullanırsınız; bildirim yükümlülüğü tesiste kalır."),
    ("KBS bildirimi nasıl yapılır?", "Tesisiniz polis bölgesindeyse EGM’nin, jandarma bölgesindeyse Jandarma’nın Kimlik Bildirim Sistemi’ne kayıtlı kullanıcıyla girip her misafirin giriş ve çıkışını işlersiniz. Kayıt için bağlı olduğunuz polis merkezine ya da jandarma karakoluna başvurulur."),
    ("Online check-in nedir, otelde nasıl yapılır?", "Misafirin kimlik bilgilerini, refakatçilerini ve imzasını varıştan önce kendi telefonundan göndermesidir. Hostlio Pro’da misafir kişisel bağlantıyı açar, belgesini tarar ve imzalar; resepsiyonda yalnızca anahtarını alır."),
    ("Kimlik okuma cihazı almam gerekir mi?", "Hayır. Pasaport ve kimlik kartının makine okunabilir alanı misafirin telefonunda ya da resepsiyonda panelden kamerayla okunur. Bu alanı olmayan belgeler elle girilir."),
]


def _channel_tr(U):
    return "".join([
        _sec("Kanal yöneticisi ne iş yapar? Adım adım senkronizasyon", _steps([
            ("Envanterinizi oluşturun", "Oda tiplerini, odaları ve fiyat planlarını Hostlio Pro’da tanımlayın. Bu, bütün kanallar için tek müsaitlik kaynağıdır."),
            ("Her OTA’yı bağlayın", "Booking.com, Airbnb, Expedia ya da kullandığınız kanalın extranet’inde bağlantıyı yetkilendirin ve odalarınızı eşleyin. Çoğu tesis bunu aynı gün yapar."),
            ("Satın, kopyalamayı bırakın", "Her rezervasyon, değişiklik ve iptal oda rafına kendiliğinden düşer; müsaitlik diğer kanallarda güncellenir."),
        ]), "dark on-dark"),
        _sec("Bir rezervasyonun yolculuğu", _table(["An", "Ne olur"], [
            ("Booking.com’da son oda satılır", "Rezervasyon oda rafına Booking.com rengiyle düşer"),
            ("Aynı saniyelerde", "O oda tipinin müsaitliği Airbnb, Expedia ve diğer kanallarda bir azalır"),
            ("Misafir mesaj atar", "Mesaj, rezervasyon bilgisiyle birlikte Lio’nun gelen kutusuna gelir (Pro ve Growth)"),
            ("Misafir iptal eder", "Oda tüm kanallarda yeniden satışa açılır"),
            ("Bir oda arızalanır", "Servis dışı yapılan oda tüm kanallarda satıştan çıkar"),
        ]), "white rule"),
        _sec("Otel programı ile kanal yöneticisi arasındaki fark", _rows([
            ("Otel programı (PMS)", "Tesisin içini yönetir: rezervasyonlar, oda rafı, check-in, kat hizmetleri, misafir kayıtları ve raporlar."),
            ("Kanal yöneticisi", "Tesisin dışarıya açılan yüzünü yönetir: müsaitliği, fiyatı ve kısıtlamaları OTA’lara gönderir, rezervasyonları geri alır."),
            ("İkisi aynı sistemde olunca", "İki takvim olmadığı için senkron kayması da olmaz. Telefonla alınan bir rezervasyon, servis dışı bir oda ya da bir iptal tüm kanallarda aynı anda müsaitliği değiştirir. Hostlio Pro’da kanal yöneticisi her planda PMS’in parçasıdır."),
            ("Ayrı kanal yöneticisi kullanınca", "PMS ile kanal yöneticisi farklı firmalardansa aradaki entegrasyon bir üçüncü halka olur: bir taraf güncellemeyi geç alırsa ya da oda eşlemesi bozulursa müsaitlik iki yerde farklılaşır ve sorunun hangi tarafta olduğunu bulmak zaman alır. Tek sistemde bu halka yoktur."),
            ("Kanal bazında rapor", "Her OTA’nın brüt geliri, komisyonu ve neti, doluluk, ADR ve RevPAR ile 30, 60 ve 90 günlük ileriye bakış tek ekranda. Gerekirse Excel’e aktarın."),
        ])),
        _sec("Fiyat ve kısıtlama terimleri",
            _table(["Kısıtlama", "Ne işe yarar", "Örnek"], [
                ("Fiyat", "Her oda tipi ve fiyat planı için gecelik fiyat", "Standart çift kişilik oda, pazartesi–perşembe 3.500 TL"),
                ("En az / en çok konaklama", "Misafirin kaç gece rezerve edebileceğini sınırlar", "Ağustos hafta sonlarında en az 2 gece"),
                ("Varışa kapalı (CTA)", "O gün kimse giriş yapamaz, ama konaklayabilir", "Bayram arifesinde giriş yok"),
                ("Çıkışa kapalı (CTD)", "O gün kimse çıkış yapamaz", "Pazar çıkışlarını kapatıp boşluk bırakmamak"),
                ("Satışa kapatma", "O oda tipi ya da fiyat planının satışını durdurur", "Yüksek sezonda iadesiz fiyatı kapatmak"),
            ])
            + f'<p style="margin-top:18px">Bu kuralları toplu düzenlemeyle bir tarih aralığına tek seferde uygularsınız. Overbooking’e karşı diğer önlemler için <a href="{U("post-overbooking")}">overbooking nasıl önlenir</a> rehberimize bakın.</p>', "white rule"),
        _sec("Ücretsiz kanal yöneticisi var mı?", _rows([
            ("Genelde arkasında ne vardır?", "“Ücretsiz” kanal yöneticileri çoğunlukla rezervasyon başına komisyon alır, kanal sayısını sınırlar ya da bir rezervasyon motoruna bağlı gelir. Komisyonlu modelde maliyet tam da en çok sattığınız aylarda artar."),
            ("Bizim yaklaşımımız", "Hostlio Pro ücretsiz değildir ama fiyatı sabit ve açıktır: aylık ⟦price:starter⟧’dan başlar, rezervasyon komisyonu yoktur, kanal yöneticisi tüm planlara dahildir ve 7 gün ücretsiz deneyebilirsiniz."),
            ("Kimin işine yarar?", "Odalarını iki ya da daha fazla kanalda satan her tesisin: tek odalı bir pansiyondan 150 odalı bir otele kadar. Tek kanalla çalışıyorsanız bile Booking.com ile Airbnb’yi eklemeye karar verdiğiniz gün takviminiz hazır olur; satış kanallarını elle güncellemek ve çift rezervasyon riskini taşımak zorunda kalmazsınız."),
        ])),
        _sec("Kanal yöneticisi değiştirirken overbooking yaşamamak için", _table(["Adım", "Ne yapılır"], [
            ("1. Envanteri hazırlayın", "Hostlio Pro’da oda tiplerini ve fiyat planlarını OTA’larda kullandığınız adlarla oluşturun."),
            ("2. Gelecek rezervasyonları aktarın", "Mevcut sisteminizden CSV ya da Excel olarak alıp yükleyin; mükerrerler atlanır."),
            ("3. Sakin saatte bağlayın", "Kanalı eski sistemde kapatıp Hostlio Pro’da bağlayın; tek tek ya da hepsini aynı gün."),
            ("4. Oda rafını kontrol edin", "Çakışma kontrolü mükerrer ya da odası atanmamış rezervasyonları listeler."),
            ("5. Müsaitliği karşılaştırın", "Her OTA’nın extranet’inde müsaitliğin oda rafınızla aynı olduğunu doğrulayın."),
        ]), "white rule"),
    ])


CHANNEL_TR_FAQ = [
    ("Hangi kanallarla başlamalıyım?", "Çoğu bağımsız otel için Booking.com ve Airbnb, ardından yabancı misafir profilinize göre Expedia, Agoda ya da Hostelworld iyi bir başlangıçtır. Kanal eklemek kolaydır; önce az sayıda kanalı düzgün eşleyip analiz ekranında komisyon sonrası neti izlemek, gereksiz kanal açmaktan daha çok kazandırır."),
    ("Kanal yöneticisi ne iş yapar?", "Odalarınızı birden fazla OTA’da satarken müsaitliği, fiyatları ve kısıtlamaları tek yerden bütün kanallara gönderir, rezervasyonları geri alır. Bir kanalda satılan oda diğerlerinde kapandığı için overbooking önlenir."),
    ("Otel programı ile kanal yöneticisi arasındaki fark nedir?", "Otel programı (PMS) rezervasyon, oda rafı, check-in ve kat hizmetleri gibi tesis içi işleri yönetir; kanal yöneticisi müsaitlik ve fiyatı OTA’lara dağıtır. Hostlio Pro’da ikisi aynı sistemdedir."),
    ("Booking.com ve Airbnb’yi aynı anda bağlayabilir miyim?", "Evet. İki kanal ve 100’den fazla başka kanal aynı takvimde senkronize edilir; birinde satılan oda diğerinde kapanır."),
    ("Bir OTA güncellemeyi almazsa ne olur?", "“Kanallara yeniden gönder” düğmesi güncel fiyat, kısıtlama ve müsaitliği tekrar gönderir. Sorun sürerse bildirim merkezi kanal hatasını size bildirir."),
]


# ---- FR
# ------------------------------------------------------------------ FR (S7 kardeş sayfalar)
def _hostel_fr(U):
    return "".join([
        _sec("Une journée à l’accueil d’une auberge avec Hostlio Pro", _rows([
            ("8 h, la journée est prête", "L’écran Aujourd’hui affiche les arrivées, les départs, les chambres à nettoyer, les messages en attente de réponse et les brouillons de Lio à valider. L’application mobile peut aussi envoyer ce résumé sur votre téléphone à 8 h, heure de l’établissement (sur Android aujourd’hui, sur iOS avec la prochaine mise à jour de l’application)."),
            ("Fin de matinée, le grand ménage", "L’équipe de ménage voit d’abord les départs du jour, et les chambres où quelqu’un arrive le soir même sont marquées prioritaires. Dès qu’une chambre est propre, son statut change et l’accueil le voit aussitôt. Une douche en panne ? Signalez-la avec une photo et passez la chambre hors service : elle sort de la vente sur tous les canaux connectés jusqu’à la réparation."),
            ("Après-midi, les arrivées", "Les voyageurs qui ont fait leur check-in en ligne (forfaits Pro et Growth) ont déjà scanné leur passeport ou leur carte d’identité et signé : à l’accueil, on remet les clés au lieu de recopier des numéros de passeport. Aucune image du document n’est conservée."),
            ("La nuit, la boîte de réception ne dort pas", "Arrivée tardive, consigne à bagages, casiers, cuisine commune, dernier métro : les voyageurs écrivent à toute heure et dans toutes les langues. Lio répond à partir des informations que vous avez saisies et transmet ce qui demande une décision au veilleur de nuit ou à l’équipe du matin."),
        ]), "white rule"),
        _sec("Ce que demandent les voyageurs, et où Lio trouve la réponse",
            '<p class="lead" style="font-size:var(--t-0);max-width:70ch">Lio ne répond qu’à partir des informations de votre établissement et de la réservation du client. Plus vous en renseignez une fois pour toutes, moins votre équipe reçoit de messages.</p>'
            + _table(["Question fréquente", "Ce que Lio utilise pour répondre"], [
                ("« On atterrit à 1 h du matin, on peut encore arriver ? »", "Vos horaires d’arrivée et vos règles pour les arrivées tardives"),
                ("« On peut laisser nos sacs après le départ ? »", "Votre règle de consigne à bagages"),
                ("« Il y a des casiers ? Il faut un cadenas ? »", "Les informations sur les chambres et les équipements que vous ajoutez"),
                ("« La cuisine est accessible aux clients ? »", "Équipements et règlement intérieur"),
                ("« Vous organisez une visite à pied demain ? »", "Votre liste d’extras ; avec Pro et Growth, Lio transmet la demande à votre équipe"),
                ("« Je peux changer mes dates ? »", "Transmis à votre équipe : Lio ne modifie pas les réservations"),
            ])),
        _sec("Hostelworld, Booking.com et réservations directes sur un seul calendrier", _rows([
            ("Une seule disponibilité pour tous les canaux", "Hostlio Pro se connecte à Hostelworld, Booking.com, Airbnb, Expedia et plus de 100 autres canaux par des connexions certifiées. Une chambre vendue sur un canal se ferme sur les autres, et une annulation la rouvre partout."),
            ("Festivals, ponts et week-ends", "Saisissez toute une saison d’un coup : choisissez la période, les types de chambre et les plans tarifaires, cochez « week-ends uniquement » pour tarifer à part le vendredi et le samedi, et ajoutez un séjour minimum, une fermeture à l’arrivée ou un arrêt des ventes pour les week-ends de festival."),
            ("Savoir quel canal rapporte vraiment", "Les analyses donnent le taux d’occupation, l’ADR et le RevPAR, ainsi que le revenu brut, la commission et le net de chaque OTA. Vous voyez où pousser la réservation directe, et l’export Excel part directement chez le comptable."),
            ("Les voyageurs étrangers et la fiche de police", f"En France, les hébergeurs doivent faire remplir une fiche individuelle de police aux clients étrangers. Le <a href=\"{U('checkin')}\">check-in en ligne</a> recueille une partie de ces données avant l’arrivée ; la fiche elle-même reste sous votre responsabilité."),
        ])),
        _sec("Veilleurs de nuit, bénévoles et équipe de ménage", _rows([
            ("Un rôle pour chacun", "Attribuez à chaque personne un rôle : manager, réception, ménage, comptabilité ou lecteur. Le ménage ne voit que les chambres ; la comptabilité ne voit pas les messages des clients. Quand un bénévole s’en va, suspendez son accès en un clic. Starter inclut 3 utilisateurs, Pro 8 et Growth 20."),
            ("Savoir qui a changé quoi", "Le journal d’activité enregistre chaque modification champ par champ, avec la personne et l’heure, pendant 365 jours. Pratique quand plusieurs équipes se relaient sur la même réservation."),
        ]), "white rule"),
        _sec("Hostlio Pro convient-il à votre auberge de jeunesse ?",
            '<p class="lead" style="font-size:var(--t-0);max-width:70ch">Nous préférons vous le dire maintenant plutôt qu’après une migration : Hostlio Pro gère la disponibilité par chambre, pas par lit.</p>'
            + _table(["Domaine", "Ça convient", "Parlons-en d’abord"], [
                ("Inventaire", "Chambres privées, chambres familiales et dortoirs vendus en entier comme une seule unité", "La vente de lits à l’unité en dortoir partagé, comme inventaire séparé, n’est pas prise en charge"),
                ("Réservations", "Une chambre par réservation, venue d’un canal ou saisie à la main", "Un groupe sur plusieurs chambres se saisit en plusieurs réservations"),
                ("Taille", "De 1 à 150 chambres, un établissement, ou deux avec Growth", "Plus de deux établissements ou plus de 150 chambres"),
                ("Paiements", "Prix, extras et reçus imprimables dans la réservation", "Pas d’encaissement par carte intégré, ni de folio ou de caisse"),
            ])),
        _sec("Quitter votre logiciel actuel en trois étapes", _steps([
            ("Créez chambres et tarifs", "Créez vos types de chambre, vos chambres et vos plans tarifaires. L’assistant de configuration vérifie ce qui manque avant la mise en service."),
            ("Importez vos réservations", "Exportez les réservations à venir de votre ancien système en CSV ou Excel et chargez le fichier. Les colonnes sont associées automatiquement et chaque ligne refusée est listée avec la raison."),
            ("Connectez vos canaux", "Autorisez Hostelworld, Booking.com et vos autres OTA, puis associez vos chambres. La plupart des établissements sont connectés le jour même."),
        ]), "dark on-dark"),
        f'<section class="rule"><div class="wrap"><p>À lire aussi : <a href="{U("post-overbooking")}">comment éviter le surbooking entre plusieurs canaux</a> et <a href="{U("post-autoreply")}">répondre automatiquement aux messages Booking.com</a>.</p></div></section>',
    ])


HOSTEL_FR_FAQ = [
    ("Lio peut-il répondre sur les casiers, la cuisine ou l’arrivée tardive ?", "Oui, à condition que ces informations figurent dans les réglages de votre établissement. Lio répond dans la langue du voyageur et uniquement à partir de ce que vous avez saisi ; s’il manque une information, il transmet le message à votre équipe et le tableau de bord indique quel détail ajouter."),
    ("Puis-je accueillir des groupes ?", "Une réservation correspond à une chambre : un groupe réparti sur plusieurs chambres se saisit en plusieurs réservations. Pour les grands groupes, expliquez-nous comment vous les vendez et nous vérifierons la configuration avec vous en démo."),
]


def _boutique_fr(U):
    return "".join([
        _sec("L’IA dans un hôtel boutique, sans perdre la touche personnelle", _rows([
            ("Votre ton, vos détails", "Lio écrit dans la langue du client à partir des informations de votre hôtel : horaires d’arrivée, petit-déjeuner en terrasse, parking, animaux, accès par la ruelle piétonne. Il n’invente ni offre ni règle que vous n’avez pas saisie."),
            ("Vous décidez de ce qui est automatique", "Commencez en mode validation et relisez chaque réponse avant envoi. Laissez ensuite Lio traiter seul les questions courantes, et gardez remises, réclamations et demandes particulières pour votre équipe."),
            ("Une seule boîte pour tous les clients", "Les messages WhatsApp et, avec Pro et Growth, ceux de Booking.com, Airbnb et Expedia arrivent au même endroit, à côté de la réservation du client. Fini les allers-retours entre extranets."),
            ("Des limites claires", "Les réponses que vous tapez vous-même partent exactement comme vous les avez écrites. Lio vous montre une traduction de ses propres réponses et, quand il n’est pas sûr, il passe la main au lieu de deviner."),
        ]), "white rule"),
        _sec("Une journée ordinaire dans un hôtel de charme de 30 chambres",
            '<p class="lead" style="font-size:var(--t-0);max-width:70ch">Une illustration de la façon dont tout s’articule ; vos chiffres seront différents.</p>'
            + _table(["Heure", "Ce qui se passe", "Dans Hostlio Pro"], [
                ("2 h 10", "Une cliente de Séoul demande si elle peut arriver tard", "Lio répond en coréen à partir de vos règles d’arrivée"),
                ("8 h", "La propriétaire découvre la journée : 9 arrivées, 7 départs, 2 brouillons à valider", "Écran Aujourd’hui et Suggestions de Lio"),
                ("10 h 30", "Un lavabo fuit en chambre 12", "Signalement de panne ; la chambre sort de la vente sur tous les canaux"),
                ("12 h", "Le ménage enchaîne les départs du jour, chambres prioritaires d’abord", "Liste de ménage, imprimable en PDF"),
                ("15 h", "Les clients attendus ont déjà fait leur check-in en ligne", "Check-in en ligne avec signature électronique (Pro et Growth)"),
                ("18 h", "Un client demande un transfert vers la gare pour vendredi", "Lio le propose et transmet la demande à votre équipe"),
                ("Lundi", "La propriétaire compare le net par canal avec la semaine passée", "Analyses et rapport hebdomadaire par e-mail"),
            ])),
        _sec("Plus de revenu par séjour, sans vente forcée", _rows([
            ("Des extras au bon moment", "Transferts, excursions, dégustations et autres extras sont proposés quand la conversation s’y prête, et la demande arrive à votre équipe (Pro et Growth)."),
            ("Demandes de réservation sur WhatsApp", "Quand un client demande des dates sur WhatsApp, Lio recueille les dates, le nombre de personnes et la chambre souhaitée, et donne votre propre tarif. Cela ne devient une réservation qu’après votre validation (Pro et Growth)."),
            ("Des suggestions chaque matin", "Les Suggestions de Lio signalent des pistes sur les tarifs, l’exploitation et le chiffre d’affaires. Rien ne change sans votre accord, et les propositions de prix restent dans les limites que vous fixez."),
            ("Le net par canal", "Les analyses donnent le revenu brut, la commission et le net de chaque OTA, plus une vue à 30, 60 et 90 jours avec pickup : vous voyez où la réservation directe rapporterait le plus."),
        ])),
        _sec("Une arrivée qui ressemble à un accueil, pas à un formulaire", _rows([
            ("Check-in avant l’arrivée", "Le client scanne la bande MRZ de son passeport ou de sa carte d’identité sur son propre téléphone, ajoute ses accompagnants et signe. Aucune image du document n’est conservée, et les signatures sont supprimées 30 jours après le départ."),
            ("Lien envoyé automatiquement", "Activez l’e-mail de check-in : chaque nouvelle réservation avec une adresse e-mail reçoit le lien dans la langue du client. Vous choisissez les sources de réservation concernées."),
            ("Clients étrangers", f"Le formulaire recueille une partie des données de la fiche individuelle de police ; voyez le détail champ par champ sur la page <a href=\"{U('checkin')}\">check-in en ligne</a>."),
            ("Attestation d’hébergement en un clic", "Créez depuis la réservation une confirmation d’hébergement pour une demande de visa ou d’invitation, et enregistrez-la en PDF."),
        ]), "white rule"),
        _sec("Logiciel hôtelier pour hôtel boutique : la check-list", _table(["Question à poser à tout éditeur", "Hostlio Pro"], [
            ("Le prix est-il public et fixe, sans commission sur les réservations ?", "Oui : à partir de ⟦price:starter⟧ par mois, sans commission, 7 jours d’essai gratuit"),
            ("Le channel manager est-il inclus ?", "Oui, dans toutes les formules, avec des connexions certifiées vers plus de 100 canaux"),
            ("L’IA répond-elle aux clients dans leur langue, avec validation ?", "Oui : WhatsApp dans toutes les formules, messageries des OTA avec Pro et Growth"),
            ("Chaque collaborateur ne voit-il que ce dont il a besoin ?", "Oui : six rôles ; 3, 8 ou 20 utilisateurs selon la formule ; journal d’activité"),
            ("Puis-je voir le revenu par canal après commission ?", "Oui, avec export Excel et rapports hebdomadaires et mensuels par e-mail"),
            ("Puis-je reprendre mes réservations existantes ?", "Oui, depuis un fichier CSV ou Excel"),
            ("Y a-t-il une application mobile ?", "Oui, iOS et Android, incluse dans toutes les formules"),
        ])),
        f'<section class="white rule"><div class="wrap"><p>À lire aussi : <a href="{U("post-ai")}">répondre aux messages des clients avec l’IA</a> et <a href="{U("post-pms")}">choisir un logiciel de gestion hôtelière pour un petit hôtel</a>.</p></div></section>',
    ])


BOUTIQUE_FR_FAQ = [
    ("L’IA ne risque-t-elle pas de rendre un hôtel boutique impersonnel ?", "Seulement si elle devine. Lio répond aux questions courantes à partir de vos propres informations, dans la langue du client, et laisse à votre équipe les remises, les réclamations et les demandes particulières. Beaucoup d’hôtels démarrent en mode validation et relisent chaque réponse les premiers jours."),
    ("Quelle formule pour un hôtel de charme de 30 chambres ?", "Pro couvre jusqu’à 50 chambres avec ⟦quota:pro⟧ messages IA par mois, les messageries des OTA, le check-in en ligne et la vente d’extras. Growth couvre deux établissements ou jusqu’à 150 chambres."),
]


def _checkin_fr(U):
    return "".join([
        _sec("Check-in en ligne et fiche individuelle de police",
            '<div class="answer"><p><strong>En bref :</strong> en France, les hébergeurs doivent faire remplir et signer par chaque client étranger, dès son arrivée, une fiche individuelle de police. Le check-in en ligne de Hostlio Pro recueille une partie de ces informations avant l’arrivée et permet de les exporter, mais <strong>il ne remplace pas la fiche et ne transmet rien aux autorités</strong> : la fiche, sa conservation et sa remise restent sous la responsabilité de l’établissement.</p></div>'
            + _rows([
                ("Qui est concerné", "L’<a href=\"https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000042804990\" rel=\"noopener\">article R814-1 du Code de l’entrée et du séjour des étrangers et du droit d’asile</a> vise les hôteliers, les exploitants de villages et maisons familiales de vacances, de résidences et villages résidentiels de tourisme, les loueurs de meublés de tourisme et de chambres d’hôtes, et les exploitants de terrains de camping. Ils doivent remplir ou faire remplir la fiche et la faire signer par le client étranger dès son arrivée."),
                ("Quelles informations", "Selon l’article R814-2 : nom et prénoms, date et lieu de naissance, nationalité, domicile habituel, numéro de téléphone mobile et adresse e-mail, date d’arrivée et date de départ prévue. Les enfants de moins de 15 ans peuvent figurer sur la fiche de l’adulte qui les accompagne. Le modèle de fiche est fixé par arrêté."),
                ("Combien de temps la garder", "Selon l’article R814-3, les fiches sont conservées six mois et remises, sur demande, aux services de police et aux unités de gendarmerie. Cette remise peut se faire sous forme dématérialisée."),
                ("Ce que cela implique pour vous", "Hostlio Pro supprime les signatures électroniques 30 jours après le départ. Si vous vous appuyez sur le check-in en ligne pour établir vos fiches, conservez de votre côté, pendant six mois, la fiche ou l’export correspondant selon votre propre procédure."),
            ])
            + '<p class="small muted">Sources : <a href="https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006070158/LEGISCTA000042803266/" rel="noopener">Légifrance, CESEDA, articles R814-1 à R814-3</a> et <a href="https://www.legifrance.gouv.fr/loda/id/JORFTEXT000031285813" rel="noopener">arrêté du 1er octobre 2015 fixant le modèle de fiche</a>. Consulté en octobre 2026. Cette section est informative et ne constitue pas un conseil juridique.</p>',
            "white rule"),
        _sec("Ce que le check-in en ligne de Hostlio Pro recueille",
            '<p class="lead" style="font-size:var(--t-0);max-width:70ch">Voici comment le formulaire de check-in se compare aux rubriques de la fiche individuelle de police. Ce qui manque, vous le complétez vous-même.</p>'
            + _table(["Rubrique de la fiche", "Recueillie par Hostlio Pro ?"], [
                ("Nom et prénoms", "Oui, dans un seul champ"),
                ("Date de naissance", "Oui"),
                ("Lieu de naissance", "Non"),
                ("Nationalité", "Oui"),
                ("Domicile habituel", "Oui pour le titulaire de la réservation (champ facultatif) ; non pour les accompagnants"),
                ("Téléphone mobile et e-mail", "Pas dans le formulaire ; ils figurent souvent dans la réservation"),
                ("Date d’arrivée et date de départ prévue", "Oui, reprises de la réservation"),
                ("Accompagnants, dont les enfants", "Oui : nom, document, nationalité et date de naissance, jusqu’à 10 personnes"),
                ("Signature du client", "Oui, signature électronique, supprimée 30 jours après le départ"),
            ])),
        _sec("De la réservation à la fiche, en trois étapes", _steps([
            ("Le client fait son check-in", "Avant d’arriver, il scanne sa pièce d’identité avec son téléphone, ajoute ses accompagnants et signe. Aucune image du document n’est conservée."),
            ("Vous exportez les données", "Depuis le tableau de bord, téléchargez un fichier CSV des clients enregistrés sur une période donnée (nom, type et numéro de document, nationalité, date de naissance et date d’arrivée). Les réservations annulées ne sont pas incluses."),
            ("Vous établissez et conservez vos fiches", "Complétez les rubriques manquantes, comme le lieu de naissance, et conservez vos fiches six mois selon votre procédure habituelle. Hostlio Pro ne génère pas la fiche officielle et ne transmet rien à la police ni à la gendarmerie."),
        ]), "dark on-dark"),
        _sec("Un check-in en ligne intégré au PMS, sans outil en plus", _rows([
            ("Tout dans la même réservation", "Beaucoup de logiciels hôteliers confient le check-in en ligne à un outil tiers, relié par une intégration et facturé à part. Dans Hostlio Pro, le check-in fait partie du PMS : le lien part de la réservation, et les données, la signature et les accompagnants y reviennent."),
            ("Lien envoyé par e-mail, si vous le souhaitez", "Activez l’e-mail de check-in : chaque nouvelle réservation avec une adresse e-mail reçoit son lien dans la langue du client. Vous choisissez les sources : réservations directes, Booking.com, Expedia, Airbnb, Agoda ou autres OTA."),
            ("À la réception, sans rien taper", "Si un client n’a pas utilisé son lien, le personnel peut scanner son document depuis le tableau de bord web ; la lecture se fait sur l’appareil et aucune image n’est conservée."),
            ("Données personnelles", "Seul le personnel de votre établissement voit les données du document, les signatures sont supprimées 30 jours après le départ et le texte de consentement fait partie du formulaire. Au sens du RGPD, votre établissement est responsable du traitement et Hostlio Pro sous-traitant."),
        ])),
    ])


CHECKIN_FR_FAQ = [
    ("Hostlio Pro remplit-il la fiche de police à ma place ?", "Non. Le check-in en ligne recueille une partie des informations (nom, date de naissance, nationalité, document, adresse du titulaire, signature) et vous pouvez les exporter en CSV, mais Hostlio Pro ne produit pas la fiche individuelle de police et ne la transmet ni à la police ni à la gendarmerie."),
    ("Hostlio Pro conserve-t-il les fiches pendant six mois ?", "Non. Les signatures électroniques sont supprimées 30 jours après le départ. Conservez vos fiches, ou l’export qui vous sert à les établir, pendant six mois selon votre propre procédure."),
]


def _channel_fr(U):
    return "".join([
        _sec("Comment fonctionne la synchronisation, étape par étape", _steps([
            ("Créez votre inventaire", "Types de chambre, chambres et plans tarifaires dans Hostlio Pro. C’est la seule source de disponibilité pour tous les canaux."),
            ("Connectez chaque OTA", "Autorisez la connexion dans l’extranet de Booking.com, Airbnb, Expedia ou du canal concerné, puis associez vos chambres. La plupart des établissements le font le jour même."),
            ("Vendez sans rien recopier", "Chaque réservation, modification ou annulation arrive seule sur le planning, et la disponibilité se met à jour sur les autres canaux."),
        ]), "dark on-dark"),
        _sec("PMS et channel manager réunis : pourquoi c’est important", _rows([
            ("Une seule disponibilité", "Quand le channel manager et le PMS sont un seul et même système, il n’y a pas deux calendriers qui peuvent se décaler. Une réservation prise au téléphone, une chambre hors service ou une annulation modifient la disponibilité sur tous les canaux à la fois."),
            ("Les chambres hors service sortent de la vente", "Signalez une panne et passez la chambre hors service : elle disparaît de la vente sur toutes les OTA connectées et ne peut plus être attribuée tant qu’elle n’est pas réparée."),
            ("Les messages à côté de la réservation", "Les messages des clients Booking.com, Airbnb et Expedia arrivent dans la boîte de réception de Lio, avec la réservation à côté (formules Pro et Growth). Lio répond dans la langue du client."),
            ("Des rapports par canal", "Revenu brut, commission et net de chaque OTA, taux d’occupation, ADR et RevPAR, plus une vue à 30, 60 et 90 jours. Exportez en Excel quand vous en avez besoin."),
        ]), "white rule"),
        _sec("Tarifs et restrictions : à quoi sert chacun",
            _table(["Restriction", "À quoi elle sert", "Exemple"], [
                ("Prix", "Le tarif par nuit de chaque type de chambre et plan tarifaire", "Chambre double classique à 110 € du lundi au jeudi"),
                ("Séjour minimum / maximum", "Limite le nombre de nuits réservables", "Deux nuits minimum les week-ends de juillet et août"),
                ("Fermé à l’arrivée (CTA)", "Personne ne peut arriver ce jour-là, mais on peut y séjourner", "Pas d’arrivée le samedi d’un festival"),
                ("Fermé au départ (CTD)", "Personne ne peut partir ce jour-là", "Éviter les départs le dimanche pour ne pas créer de trous"),
                ("Arrêt des ventes", "Ferme la vente d’un type de chambre ou d’un plan", "Fermer le tarif non remboursable pendant un salon"),
            ])
            + '<p style="margin-top:18px">Avec la modification groupée, vous choisissez une période, les types de chambre et les plans, puis vous appliquez tout d’un coup ; l’option « week-ends uniquement » ne change que les nuits du vendredi et du samedi. Si un canal n’a pas reçu une mise à jour, le bouton « renvoyer aux canaux » renvoie les tarifs et la disponibilité actuels.</p>'),
        _sec("Petits établissements : chambres d’hôtes, gîtes et hôtels indépendants", _rows([
            ("Même avec trois chambres", f"Dès que vous êtes sur Booking.com et Airbnb à la fois, le risque de double réservation existe. La formule Starter couvre jusqu’à 10 chambres, avec le channel manager inclus ; voyez aussi notre page <a href=\"{U('t-guesthouse')}\">logiciel pour chambres d’hôtes</a>."),
            ("Réservations directes et téléphone", "Les réservations prises au téléphone ou par e-mail se saisissent sur le planning et ferment aussitôt la chambre sur les OTA."),
            ("Hostelworld, Agoda, Google Hotels", "Au-delà des grandes OTA, les connexions couvrent plus de 100 canaux : plateformes d’auberges de jeunesse, OTA orientées Asie, grossistes et métamoteurs."),
        ])),
        _sec("Channel manager gratuit ou le moins cher : ce qu’il faut regarder", _rows([
            ("Ce qui se cache souvent derrière", "Les channel managers « gratuits » prélèvent souvent une commission par réservation, limitent le nombre de canaux ou sont liés à un moteur de réservation. Avec une commission, le coût augmente justement quand vous vendez le plus."),
            ("Notre approche", "Hostlio Pro n’est pas gratuit, mais son prix est fixe et public : à partir de ⟦price:starter⟧ par mois, sans commission sur les réservations, channel manager inclus dans toutes les formules et 7 jours d’essai gratuit."),
        ]), "white rule"),
        _sec("Changer de channel manager sans surbooking", _table(["Étape", "Que faire"], [
            ("1. Préparez l’inventaire", "Créez types de chambre et plans dans Hostlio Pro avec les mêmes noms que sur vos OTA."),
            ("2. Importez les réservations à venir", "Exportez-les de votre système actuel en CSV ou Excel et chargez le fichier ; les doublons sont ignorés."),
            ("3. Basculez aux heures calmes", "Déconnectez le canal dans l’ancien système et connectez-le dans Hostlio Pro, un par un ou tous le même jour."),
            ("4. Vérifiez le planning", "Le contrôle des conflits liste les réservations en double ou sans chambre attribuée."),
            ("5. Comparez la disponibilité", "Vérifiez dans l’extranet de chaque OTA que la disponibilité correspond à votre planning."),
        ]) + f'<p style="margin-top:18px">Plus de détails dans notre guide <a href="{U("post-overbooking")}">comment éviter le surbooking</a>.</p>'),
    ])


CHANNEL_FR_FAQ = [
    ("Existe-t-il un channel manager gratuit ?", "Hostlio Pro n’est pas gratuit, mais vous pouvez l’essayer 7 jours sans frais. Ensuite, le channel manager est inclus dans toutes les formules à partir de ⟦price:starter⟧ par mois, sans commission sur les réservations."),
    ("Combien de temps faut-il pour connecter un canal ?", "Votre compte est prêt en quelques minutes. Pour chaque OTA, vous autorisez la connexion dans son extranet et associez vos chambres ; la plupart des établissements connectent leurs canaux le jour même."),
    ("Que se passe-t-il si une OTA ne reçoit pas une mise à jour ?", "Le bouton « renvoyer aux canaux » renvoie les tarifs, restrictions et disponibilités actuels. Si le problème persiste, le centre de notifications vous signale les incidents du canal."),
]


# ---- IT
# ------------------------------------------------------------------ IT (SEO S7 kardeş sayfalar, 8 Ekim 2026)
# Alloggiati Web: art. 109 TULPS (testo vigente dal 10-8-2019), D.M. Interno 7 gennaio 2013 come modificato
# dal D.M. 16 settembre 2021 (GU n. 246 del 14-10-2021) + allegato tecnico; PDF ufficiali dal portale
# alloggiatiweb.poliziadistato.it (Normativa). Hostlio Pro NON invia ad Alloggiati Web e NON genera il tracciato.
def _hostel_it(U):
    return "".join([
        _sec("Una giornata alla reception dell’ostello con Hostlio Pro", _rows([
            ("Mattina, il piano del giorno", "La schermata Oggi elenca arrivi, partenze, camere da pulire, messaggi in attesa di risposta e bozze di Lio da approvare. Chi apre il turno sa subito cosa fare, senza scorrere tre extranet diverse."),
            ("Tarda mattinata, il cambio camere", "L’housekeeping vede per prime le partenze del giorno, con in evidenza le camere che hanno un arrivo in giornata. Quando una camera è pulita lo stato cambia e la reception lo vede subito. Se si rompe una doccia, la segnali con una foto e metti la camera fuori servizio: esce dalla vendita su tutti i canali collegati finché non viene riparata."),
            ("Pomeriggio, gli arrivi", "Chi ha completato il check-in online (piani Pro e Growth) ha già scansionato passaporto o carta d’identità e firmato: al banco si consegnano le chiavi invece di ricopiare numeri di passaporto. Nessuna immagine del documento viene conservata."),
            ("Notte, la casella non si ferma", "I viaggiatori scrivono a ogni ora e in molte lingue: arrivo dopo mezzanotte, deposito bagagli, armadietti, cucina, fermata dell’autobus più vicina. Lio risponde con le informazioni che hai inserito e passa al turno di notte, o a quello del mattino, solo ciò che richiede una decisione."),
        ]), "white rule"),
        _sec("Cosa chiedono gli ospiti di un ostello, e dove Lio trova la risposta",
            '<p class="lead" style="font-size:var(--t-0);max-width:70ch">Lio risponde solo con le informazioni della tua struttura e della prenotazione dell’ospite. Più dettagli inserisci una volta, meno messaggi arrivano al tuo staff.</p>'
            + _table(["Domanda tipica", "Cosa usa Lio per rispondere"], [
                ("«Atterriamo all’una di notte, possiamo fare il check-in?»", "I tuoi orari di check-in e le regole per gli arrivi tardivi"),
                ("«Possiamo lasciare i bagagli dopo il check-out?»", "La tua politica sul deposito bagagli"),
                ("«Ci sono armadietti? Serve un lucchetto?»", "I dettagli su camere e servizi che aggiungi"),
                ("«C’è una cucina per gli ospiti?»", "Servizi e regolamento della struttura"),
                ("«Come arrivo dall’aeroporto?»", "Le indicazioni di trasporto, più il tuo transfer se lo vendi"),
                ("«Domani c’è un free walking tour?»", "Il tuo elenco di extra; con Pro e Growth Lio passa la richiesta al tuo staff"),
                ("«Posso cambiare le date?»", "Passa al tuo staff: Lio non modifica le prenotazioni"),
            ])),
        _sec("Hostelworld, Booking.com e prenotazioni dirette in un solo calendario", _rows([
            ("Una sola disponibilità per tutti i canali", "Hostlio Pro si collega a Hostelworld, Booking.com, Airbnb, Expedia e oltre 100 altri canali tramite connessioni certificate. Una camera venduta su un canale si chiude sugli altri; una cancellazione la riapre ovunque."),
            ("Prezzi per weekend ed eventi", "Imposta un’intera stagione in una volta: scegli date, tipologie e piani tariffari, spunta «solo weekend» per prezzare a parte venerdì e sabato e aggiungi soggiorno minimo, chiuso all’arrivo o stop vendite per i weekend di concerti e festival."),
            ("Quale canale rende davvero", "L’analisi mostra occupazione, ADR e RevPAR, più ricavi lordi, commissioni e netto di ogni OTA, così capisci dove conviene spingere le prenotazioni dirette. Esporta in Excel per il commercialista."),
        ])),
        _sec("Turni di notte, volontari e pulizie", _rows([
            ("Un ruolo per ognuno", "Assegna a ogni persona un ruolo: manager, reception, housekeeping, contabilità o osservatore. Chi pulisce vede solo le camere, la contabilità non legge i messaggi degli ospiti. Quando un volontario va via, sospendi l’accesso con un clic. Starter include 3 utenti, Pro 8 e Growth 20."),
            ("Chi ha cambiato cosa", "Il registro attività annota ogni modifica campo per campo, con persona e ora, per 365 giorni. Utile quando più turni lavorano sulla stessa prenotazione."),
            ("Ognuno nella sua lingua", "Pannello e app mobile sono in italiano, inglese, spagnolo, francese, portoghese e turco: uno staff internazionale lavora nella propria lingua. L’app iOS e Android è inclusa in tutti i piani."),
        ]), "white rule"),
        _sec("Hostlio Pro è il gestionale giusto per il tuo ostello?",
            '<p class="lead" style="font-size:var(--t-0);max-width:70ch">Preferiamo dirtelo adesso piuttosto che dopo una migrazione. Hostlio Pro gestisce la disponibilità per camera, non per posto letto.</p>'
            + _table(["Ambito", "Adatto", "Parliamone prima"], [
                ("Inventario", "Camere private, familiari e dormitori venduti come unità intera", "La vendita di singoli letti in dormitorio come inventario separato non è supportata"),
                ("Prenotazioni", "Una camera per prenotazione, da qualsiasi canale o inserita a mano", "I gruppi su più camere si registrano come prenotazioni separate"),
                ("Dimensioni", "Da 1 a 150 camere, una struttura o due con Growth", "Più di due strutture o più di 150 camere"),
                ("Pagamenti", "Prezzi, extra e ricevute stampabili sulla prenotazione", "Non ci sono pagamenti con carta integrati, conto ospite o cassa"),
                ("Ospiti", "Viaggiatori internazionali che scrivono su WhatsApp e dalle caselle delle OTA", "—"),
            ])),
        _sec("Passare dal tuo gestionale attuale", _steps([
            ("Configura camere e tariffe", "Crea tipologie, camere e piani tariffari. La procedura guidata ti segnala cosa manca prima di andare online."),
            ("Importa le prenotazioni", "Esporta le prenotazioni future dal vecchio sistema in CSV o Excel e caricale. Le colonne vengono abbinate automaticamente e le righe con problemi sono elencate con il motivo."),
            ("Collega i canali", "Autorizza Hostelworld, Booking.com e le altre OTA e abbina le camere. La maggior parte delle strutture si collega in giornata."),
        ]), "dark on-dark"),
        f'<section class="rule"><div class="wrap"><p>Approfondisci: <a href="{U("post-overbooking")}">come evitare l’overbooking tra i canali</a> e <a href="{U("post-autoreply")}">come rispondere in automatico ai messaggi di Booking.com</a>. Per il check-in degli ospiti e gli obblighi verso la Questura leggi la pagina sul <a href="{U("checkin")}">check-in online</a>.</p></div></section>',
    ])


HOSTEL_IT_FAQ = [
    ("Lio sa rispondere su armadietti, cucina o arrivi in tarda notte?", "Sì, se queste informazioni sono nelle impostazioni della struttura. Lio risponde nella lingua dell’ospite e solo con ciò che hai inserito; se manca qualcosa passa il messaggio allo staff e il pannello ti indica quale dettaglio aggiungere."),
    ("Posso gestire prenotazioni di gruppo?", "Una prenotazione occupa una camera, quindi un gruppo su più camere si registra con più prenotazioni. Per gruppi numerosi raccontaci come li vendi e verifichiamo insieme la configurazione in una demo."),
    ("Volontari e turno di notte possono avere un accesso limitato?", "Sì. Assegna il ruolo reception o osservatore, oppure housekeeping se si occupano solo delle camere. Puoi sospendere l’accesso in qualsiasi momento e il registro attività mostra chi ha cambiato cosa."),
]


def _boutique_it(U):
    return "".join([
        _sec("AI per boutique hotel, senza perdere il tocco personale", _rows([
            ("Il tuo tono, i tuoi dettagli", "Lio scrive nella lingua dell’ospite usando le informazioni della tua struttura: orari di check-in, colazione in terrazza, parcheggio, animali, come raggiungerti nel centro storico. Non inventa offerte o regole che non hai inserito."),
            ("Decidi tu cosa è automatico", "Parti in modalità approvazione e leggi ogni risposta prima che venga inviata. Poi lascia che Lio chiuda da solo le domande di routine e tieni per il tuo staff sconti, reclami e richieste speciali."),
            ("Una sola casella per ogni ospite", "I messaggi WhatsApp e, con Pro e Growth, quelli di Booking.com, Airbnb ed Expedia arrivano in un unico posto accanto alla prenotazione. Il team smette di saltare da un’extranet all’altra."),
            ("Limiti chiari", "Le risposte che scrivi tu partono esattamente come le hai scritte. Delle risposte di Lio vedi la traduzione nella tua lingua, e quando non è sicuro passa la conversazione invece di tirare a indovinare."),
        ]), "white rule"),
        _sec("Un boutique hotel di 30 camere in una giornata normale",
            '<p class="lead" style="font-size:var(--t-0);max-width:70ch">Un esempio di come i pezzi lavorano insieme; i tuoi numeri saranno diversi.</p>'
            + _table(["Ora", "Cosa succede", "Dove, in Hostlio Pro"], [
                ("02:10", "Un ospite di Seul chiede se può arrivare dopo mezzanotte", "Lio risponde in coreano con le tue regole di check-in"),
                ("08:00", "La titolare legge la giornata: 9 arrivi, 7 partenze, 2 bozze da approvare", "Schermata Oggi e Suggerimenti di Lio"),
                ("10:30", "Perde il lavandino della camera 14", "Segnalazione guasto; la camera esce dalla vendita su tutti i canali"),
                ("12:00", "L’housekeeping rifà le camere in partenza, prima quelle con arrivo in giornata", "Elenco housekeeping, stampabile in PDF"),
                ("15:00", "Gli ospiti in arrivo hanno già fatto il check-in online", "Check-in online con firma digitale (Pro e Growth)"),
                ("18:00", "Un ospite chiede un transfer per l’aeroporto per venerdì", "Lio lo propone e passa la richiesta al tuo staff"),
                ("Lunedì", "La titolare confronta i ricavi netti per canale con la settimana prima", "Analisi e report settimanale via email"),
            ])),
        _sec("Più ricavi per soggiorno, senza vendere a tutti i costi", _rows([
            ("Extra al momento giusto", "Transfer, degustazioni, tour e altri extra vengono proposti quando c’entrano con la conversazione, e la richiesta arriva al tuo staff (Pro e Growth)."),
            ("Richieste di prenotazione su WhatsApp", "Quando un ospite chiede disponibilità su WhatsApp, Lio raccoglie date, persone e preferenza di camera e indica la tua tariffa. Diventa una prenotazione solo dopo la tua approvazione (Pro e Growth)."),
            ("Suggerimenti ogni mattina", "I Suggerimenti di Lio segnalano opportunità su prezzi, operatività e ricavi. Nulla cambia senza la tua approvazione e le proposte di tariffa restano nei limiti che imposti."),
            ("Ricavi netti per canale", "L’analisi mostra lordo, commissione e netto di ogni OTA, più una vista a 30, 60 e 90 giorni con il pickup: vedi dove le prenotazioni dirette renderebbero di più."),
        ])),
        _sec("Un arrivo che sembra un benvenuto, non un modulo", _rows([
            ("Check-in prima dell’arrivo", "L’ospite scansiona dal proprio telefono la zona a lettura ottica del passaporto o della carta d’identità, aggiunge gli accompagnatori e firma. Nessuna immagine del documento viene conservata e le firme si cancellano 30 giorni dopo il check-out. I dati raccolti ti aiutano a preparare le schedine per Alloggiati Web, che invii tu dal portale della Polizia di Stato."),
            ("Link inviato in automatico", "Attiva l’email di check-in e ogni nuova prenotazione con un indirizzo email riceve il link nella lingua dell’ospite. Scegli tu a quali canali di provenienza si applica."),
            ("Lettere per il visto con un clic", "Crea dalla prenotazione una conferma di soggiorno per richieste di visto o inviti e salvala in PDF."),
        ]), "white rule"),
        _sec("Checklist per scegliere il gestionale del tuo boutique hotel", _table(["Domanda da fare a ogni fornitore", "Hostlio Pro"], [
            ("Il prezzo è pubblico e fisso, senza commissioni sulle prenotazioni?", "Sì: da ⟦price:starter⟧ al mese, nessuna commissione, 7 giorni di prova gratuita"),
            ("Il channel manager è incluso?", "Sì, in tutti i piani, con connessioni certificate a oltre 100 canali"),
            ("L’AI risponde agli ospiti nella loro lingua, con approvazione?", "Sì: WhatsApp in tutti i piani, caselle delle OTA con Pro e Growth"),
            ("Ogni collaboratore vede solo ciò che gli serve?", "Sì: sei ruoli; 3, 8 o 20 utenti a seconda del piano; registro attività"),
            ("Vedo i ricavi per canale al netto delle commissioni?", "Sì, con esportazione in Excel e report settimanali e mensili via email"),
            ("Invia i dati ad Alloggiati Web?", "No: raccoglie parte dei dati con il check-in online e li esporta in CSV; l’invio resta a te"),
            ("Posso portare le prenotazioni esistenti?", "Sì, da un file CSV o Excel"),
            ("C’è un’app mobile?", "Sì, iOS e Android, inclusa in tutti i piani"),
        ])),
        f'<section class="white rule"><div class="wrap"><p>Approfondisci: <a href="{U("post-ai")}">rispondere ai messaggi degli ospiti con l’AI</a> e <a href="{U("post-pms")}">come scegliere un gestionale per un piccolo hotel</a>.</p></div></section>',
    ])


BOUTIQUE_IT_FAQ = [
    ("L’AI rende un boutique hotel impersonale?", "Solo se tira a indovinare. Lio risponde alle domande di routine con le tue informazioni, nella lingua dell’ospite, e passa sconti, reclami e richieste speciali al tuo staff. Molti hotel partono in modalità approvazione e rileggono ogni risposta nei primi giorni."),
    ("Che piano serve a un boutique hotel da 30 camere?", "Il piano Pro copre fino a 50 camere con ⟦quota:pro⟧ messaggi AI al mese, caselle delle OTA, check-in online e vendita di extra. Growth copre due strutture o fino a 150 camere."),
]


def _checkin_it(U):
    return "".join([
        _sec("Check-in online e Alloggiati Web: cosa fa Hostlio Pro e cosa resta a te",
            '<div class="answer"><p><strong>In breve:</strong> in Italia chi dà alloggio deve comunicare le generalità degli ospiti alla Questura tramite il portale Alloggiati Web della Polizia di Stato. Hostlio Pro raccoglie con il check-in online una parte di quei dati e ti permette di esportarli, ma <strong>non invia nulla ad Alloggiati Web</strong>: la comunicazione resta a carico della struttura.</p></div>'
            + _rows([
                ("Chi è obbligato", "L’<a href=\"https://alloggiatiweb.poliziadistato.it/PortaleAlloggiati/Download/Normativa/109_TULPS.pdf\" rel=\"noopener\">art. 109 del TULPS</a> (R.D. 773/1931) riguarda i gestori di alberghi e di altre strutture ricettive, compresi campeggi, case e appartamenti per vacanze e affittacamere. Dal 2018 la legge chiarisce che gli stessi obblighi valgono per chi affitta immobili, o parti di essi, con contratti inferiori a trenta giorni."),
                ("Entro quando", "Entro le 24 ore successive all’arrivo e, per i soggiorni non superiori alle 24 ore, entro sei ore dall’arrivo. L’ospite può essere alloggiato solo se munito di carta d’identità o di altro documento idoneo; per gli stranieri extracomunitari basta il passaporto o un documento equivalente con fotografia."),
                ("Quali dati", "Per ogni schedina: data di arrivo, giorni di permanenza, cognome, nome, sesso, data e luogo di nascita, cittadinanza, tipo, numero e luogo di rilascio del documento. Per nuclei familiari e gruppi guidati bastano i dati del documento di un coniuge o del capogruppo; per gli altri componenti si indicano permanenza, generalità, luogo di nascita e cittadinanza."),
                ("Come si invia", "Con le credenziali rilasciate dalla Questura, in tre modi: inserendo una schedina alla volta sul portale, caricando un file di testo che rispetta il tracciato record e le tabelle di codifica ufficiali (comuni, stati, documenti), oppure tramite i servizi web del portale. Fax o PEC solo in caso di problemi tecnici del portale."),
                ("Cosa conservare", "La ricevuta in PDF scaricata dal portale, che va conservata per cinque anni. Il decreto chiede inoltre di cancellare i dati digitali trasmessi una volta generata la ricevuta."),
            ])
            + '<p class="small muted">Fonti: <a href="https://alloggiatiweb.poliziadistato.it/PortaleAlloggiati/Normativa.aspx" rel="noopener">Alloggiati Web, Normativa (Polizia di Stato)</a>, <a href="https://alloggiatiweb.poliziadistato.it/PortaleAlloggiati/Download/Normativa/109_TULPS.pdf" rel="noopener">art. 109 TULPS, testo vigente</a> e <a href="https://www.gazzettaufficiale.it/eli/id/2021/10/14/21A06000/sg" rel="noopener">D.M. Interno 16 settembre 2021 (GU n. 246 del 14 ottobre 2021)</a>, che modifica il D.M. 7 gennaio 2013. Consultato a ottobre 2026. Questa sezione è informativa e non costituisce consulenza legale: per i casi particolari fa fede la Questura competente.</p>',
            "white rule"),
        _sec("Quali dati della schedina raccoglie il check-in online di Hostlio Pro",
            '<p class="lead" style="font-size:var(--t-0);max-width:70ch">Ecco come il modulo di check-in si confronta con i dati richiesti da Alloggiati Web. Quello che manca lo completi tu prima dell’invio.</p>'
            + _table(["Dato richiesto da Alloggiati Web", "Lo raccoglie Hostlio Pro?"], [
                ("Data di arrivo e giorni di permanenza", "Sì, dalla prenotazione (arrivo e partenza)"),
                ("Cognome e nome", "Sì, ma in un unico campo: cognome e nome non sono separati"),
                ("Data di nascita e cittadinanza", "Sì"),
                ("Tipo e numero del documento", "Sì: passaporto o carta d’identità, letti dalla zona MRZ o inseriti a mano"),
                ("Accompagnatori (familiari o gruppo)", "Sì: nome, documento, nazionalità e data di nascita fino a 10 persone"),
                ("Sesso", "No"),
                ("Luogo di nascita", "No"),
                ("Luogo di rilascio del documento", "No"),
                ("Codifiche ufficiali e tracciato record", "No: il CSV esportato non è il file di testo nel formato del portale"),
            ])),
        _sec("Dal check-in alla schedina, passo per passo", _steps([
            ("L’ospite completa il check-in", "Prima di arrivare scansiona il documento con il telefono, aggiunge gli accompagnatori e firma. Nessuna immagine del documento viene conservata."),
            ("Esporti i dati", "Dal pannello scarichi un CSV con gli ospiti registrati in un intervallo di date: nome, tipo e numero di documento, nazionalità, data di nascita e data di arrivo. Le prenotazioni cancellate non sono incluse."),
            ("Invii ad Alloggiati Web", "Completa sesso, luogo di nascita e luogo di rilascio, poi inserisci le schedine sul portale come fai oggi e scarica la ricevuta. Hostlio Pro non genera il file nel tracciato ufficiale e non si collega ai servizi web della Polizia di Stato."),
        ]), "dark on-dark"),
        _sec("Check-in online integrato nel gestionale, senza un’app in più", _rows([
            ("Tutto nella stessa prenotazione", "Molti gestionali risolvono il check-in online con uno strumento esterno collegato via integrazione, con il suo abbonamento. In Hostlio Pro il check-in fa parte del gestionale: il link parte dalla prenotazione e dati, firma e accompagnatori tornano nella stessa prenotazione."),
            ("Link automatico via email", "Attiva l’email di check-in e ogni nuova prenotazione con un indirizzo email riceve il proprio link nella lingua dell’ospite. Scegli tu i canali: prenotazioni dirette, Booking.com, Expedia, Airbnb, Agoda o altre OTA."),
            ("Al banco, senza digitare", "Se un ospite non completa il link, lo staff può scansionare il documento dal pannello web; la lettura avviene sul dispositivo e anche qui non si salva nessuna immagine."),
        ]), "white rule"),
    ])


CHECKIN_IT_FAQ = [
    ("Hostlio Pro invia le schedine ad Alloggiati Web?", "No. Hostlio Pro raccoglie parte dei dati con il check-in online e ti permette di esportarli in CSV, ma non si collega ad Alloggiati Web e non genera il file nel tracciato record della Polizia di Stato. La comunicazione alla Questura resta a carico della struttura."),
    ("Quali dati della schedina dovrò completare io?", "Il modulo non raccoglie sesso, luogo di nascita e luogo di rilascio del documento, e non separa cognome e nome. Vanno aggiunti prima dell’invio sul portale Alloggiati Web."),
    ("Serve un’app di check-in oltre al gestionale?", "No. In Hostlio Pro il check-in online è integrato nel gestionale nei piani Pro e Growth: il link parte dalla prenotazione e i dati tornano lì, senza un altro abbonamento."),
    ("Funziona con la carta d’identità elettronica?", "I documenti con zona a lettura ottica (MRZ), come il passaporto e la carta d’identità elettronica, si scansionano con la fotocamera del telefono; quelli senza MRZ si inseriscono a mano nello stesso modulo."),
]


def _channel_it(U):
    return "".join([
        _sec("Come funziona la sincronizzazione, passo per passo", _steps([
            ("Crea il tuo inventario", "Tipologie di camera, camere e piani tariffari in Hostlio Pro. È l’unica fonte di disponibilità per tutti i canali."),
            ("Collega ogni OTA", "Autorizza la connessione nell’extranet di Booking.com, Airbnb, Expedia o del canale che usi e abbina le camere. La maggior parte delle strutture lo fa in giornata."),
            ("Vendi senza ricopiare", "Ogni prenotazione, modifica o cancellazione arriva da sola sul planning e la disponibilità si aggiorna sugli altri canali."),
        ]), "dark on-dark"),
        _sec("Channel manager per piccole strutture: cosa conta davvero", _rows([
            ("Gestionale e channel manager nello stesso sistema", "Quando PMS e channel manager sono lo stesso software non ci sono due calendari che possono andare fuori sincrono. Una prenotazione telefonica, una camera fuori servizio o una cancellazione cambiano la disponibilità su tutti i canali insieme."),
            ("Camere fuori servizio", "Se registri un guasto e metti la camera fuori servizio, esce dalla vendita su tutte le OTA collegate e non può essere assegnata finché non torna operativa."),
            ("Messaggi accanto alla prenotazione", "I messaggi degli ospiti di Booking.com, Airbnb ed Expedia arrivano nella casella di Lio con la prenotazione a fianco (piani Pro e Growth). Lio risponde nella lingua dell’ospite."),
            ("Report per canale", "Vedi lordo, commissione e netto di ogni OTA, occupazione, ADR e RevPAR e una vista a 30, 60 e 90 giorni. Esporta in Excel quando serve."),
            ("Dimensioni giuste", "Starter copre fino a 10 camere, Pro fino a 50, Growth due strutture o fino a 150 camere. Il channel manager è incluso in tutti i piani."),
        ]), "white rule"),
        _sec("Tariffe e restrizioni: a cosa serve ciascuna",
            _table(["Restrizione", "A cosa serve", "Esempio"], [
                ("Prezzo", "La tariffa per notte di ogni tipologia e piano", "Doppia standard a 95 € dal lunedì al giovedì"),
                ("Soggiorno minimo / massimo", "Limita quante notti può prenotare l’ospite", "Minimo 3 notti a Ferragosto"),
                ("Chiuso all’arrivo (CTA)", "Nessuno può arrivare quel giorno, ma si può soggiornare", "Niente arrivi il sabato di una fiera"),
                ("Chiuso alla partenza (CTD)", "Nessuno può partire quel giorno", "Evitare partenze la domenica per non lasciare buchi"),
                ("Stop vendite", "Chiude la vendita di quella tipologia o piano", "Chiudere la tariffa non rimborsabile in alta stagione"),
            ])
            + '<p style="margin-top:18px">Con la modifica in blocco scegli un intervallo di date, le tipologie e i piani e applichi tutto in una volta; l’opzione «solo weekend» cambia solo le notti di venerdì e sabato. Se un canale non riceve un aggiornamento, il pulsante «reinvia ai canali» invia di nuovo tariffe e disponibilità attuali.</p>'),
        _sec("Quanto costa un channel manager?", _rows([
            ("I modelli più diffusi", "Canone mensile fisso, commissione sulle prenotazioni gestite o un mix dei due. Alcuni channel manager «gratuiti» si ripagano con la commissione, limitano il numero di canali o sono legati a un motore di prenotazione. Con la commissione il costo sale proprio nei mesi migliori."),
            ("Come lo facciamo noi", "Hostlio Pro non è gratuito, ma il prezzo è fisso e pubblico: da ⟦price:starter⟧ al mese, nessuna commissione sulle prenotazioni, channel manager incluso in tutti i piani e 7 giorni di prova gratuita."),
            ("Fai i conti", f"Confronta il canone con le commissioni che paghi oggi con il nostro <a href=\"{U('roi')}\">calcolatore</a> o con la <a href=\"{U('compare')}\">pagina di confronto</a> dei gestionali."),
        ])),
        _sec("Cambiare channel manager senza overbooking", _table(["Passo", "Cosa fare"], [
            ("1. Prepara l’inventario", "Crea tipologie e piani in Hostlio Pro con gli stessi nomi che usi sulle OTA."),
            ("2. Importa le prenotazioni future", "Esporta le prenotazioni dal sistema attuale in CSV o Excel e caricale; i duplicati vengono saltati."),
            ("3. Collega nelle ore tranquille", "Scollega il canale dal vecchio sistema e collegalo in Hostlio Pro, uno alla volta o tutti lo stesso giorno."),
            ("4. Controlla il planning", "Il controllo conflitti elenca prenotazioni doppie o senza camera assegnata."),
            ("5. Confronta la disponibilità", "Verifica nell’extranet di ogni OTA che la disponibilità coincida con il tuo planning."),
        ]) + f'<p style="margin-top:18px">Più dettagli nella nostra guida <a href="{U("post-overbooking")}">come evitare l’overbooking</a>.</p>', "white rule"),
    ])


CHANNEL_IT_FAQ = [
    ("Esiste un channel manager gratuito?", "Hostlio Pro non è gratuito, ma puoi provarlo 7 giorni senza costi. Dopo, il channel manager è incluso in tutti i piani da ⟦price:starter⟧ al mese, senza commissioni sulle prenotazioni."),
    ("Va bene per un B&B o una piccola struttura?", "Sì. Il piano Starter copre fino a 10 camere con lo stesso channel manager dei piani superiori; il prezzo non cambia se hai meno camere."),
    ("Quanto ci vuole per collegare un canale?", "L’account è pronto in pochi minuti. Per ogni OTA autorizzi la connessione nella sua extranet e abbini le camere; la maggior parte delle strutture collega i canali in giornata."),
    ("Cosa succede se una OTA non riceve un aggiornamento?", "Il pulsante «reinvia ai canali» invia di nuovo tariffe, restrizioni e disponibilità attuali. Se il problema continua, il centro notifiche ti avvisa degli errori del canale."),
]


# ---- PT
# ------------------------------------------------------------------ PT (pt-BR): segmentos
def _hostel_pt(U):
    return "".join([
        _sec("Um dia na recepção de um hostel com o Hostlio Pro", _rows([
            ("8h, o dia já está organizado", "A tela Hoje mostra chegadas, saídas, quartos para limpar, mensagens sem resposta e rascunhos do Lio esperando aprovação. Você abre o painel e já sabe por onde começar, sem montar planilha nem conferir três extranets."),
            ("Fim da manhã, troca de quartos", "A governança vê primeiro as saídas do dia, com os quartos que têm chegada no mesmo dia marcados como prioridade. Quando o quarto fica limpo, o status muda e a recepção vê na hora. Se o chuveiro quebrar, registre o problema com foto e coloque o quarto fora de serviço: ele sai da venda em todos os canais conectados até ser consertado."),
            ("Tarde, chegadas", "Quem fez o check-in online (planos Pro e Growth) já leu o passaporte ou a identidade pelo celular e assinou. A recepção entrega a chave em vez de digitar números de passaporte, e nenhuma imagem do documento é guardada."),
            ("Madrugada, a caixa de entrada não para", "Mochileiros escrevem a qualquer hora e em vários idiomas: chegada tarde, guarda-volumes, armários, cozinha, ônibus do aeroporto. O Lio responde com as informações que você cadastrou e deixa para a equipe da noite ou da manhã só o que exige uma decisão."),
        ]), "white rule"),
        _sec("O que os hóspedes de hostel perguntam e de onde o Lio tira a resposta",
            '<p class="lead" style="font-size:var(--t-0);max-width:70ch">O Lio só responde com as informações da sua hospedagem e da reserva do hóspede. Quanto mais você preenche uma vez, menos mensagens chegam à equipe.</p>'
            + _table(["Pergunta comum", "O que o Lio usa para responder"], [
                ("“Nosso voo chega à 1h, ainda dá para fazer check-in?”", "Seus horários de check-in e as regras para chegada tarde"),
                ("“Posso deixar a mochila depois do check-out?”", "Sua política de guarda-volumes"),
                ("“Tem armário? Preciso levar cadeado?”", "Os detalhes de quartos e instalações que você cadastrar"),
                ("“Dá para usar a cozinha?”", "Instalações e regras da casa"),
                ("“Como chego aí saindo do aeroporto?”", "Suas instruções de acesso e, se você vender, o transfer"),
                ("“Vocês têm passeio pela cidade amanhã?”", "Sua lista de extras; nos planos Pro e Growth o Lio repassa o pedido à equipe"),
                ("“Posso mudar minhas datas?”", "Vai para a equipe: o Lio não altera reservas"),
            ])),
        _sec("Hostelworld, Booking.com e reservas diretas no mesmo calendário", _rows([
            ("Uma só disponibilidade", "O Hostlio Pro se conecta ao Hostelworld, ao Booking.com, ao Airbnb, à Expedia e a mais de 100 canais por conexões certificadas. O quarto vendido em um canal fecha nos outros, e um cancelamento reabre a vaga em todos."),
            ("Feriadão e alta temporada", "Defina uma temporada inteira de uma vez: escolha datas, tipos de quarto e planos tarifários, use «só fins de semana» para dar outro preço às noites de sexta e sábado e acrescente estadia mínima, fechado para chegada ou stop sell para Carnaval, réveillon ou festivais."),
            ("Qual canal paga de verdade", "As análises mostram ocupação, ADR e RevPAR, além de receita bruta, comissão e líquido por OTA. Assim você sabe onde vale a pena puxar reserva direta. Exporte para Excel quando o contador pedir."),
        ])),
        _sec("Equipe da noite, voluntários e governança", _rows([
            ("Cada um com sua função", "Dê a cada pessoa uma função: gerente, recepção, governança, financeiro ou visualizador. Quem limpa vê só os quartos; o financeiro não vê as mensagens dos hóspedes. Quando um voluntário vai embora, suspenda o acesso com um clique. O Starter inclui 3 usuários, o Pro 8 e o Growth 20."),
            ("Quem mudou o quê", "O histórico de atividades registra cada alteração campo a campo, com pessoa e horário, por 365 dias. Útil quando vários turnos mexem na mesma reserva."),
            ("Cada um no seu idioma", "O painel e o app funcionam em português, inglês, espanhol, francês, italiano e turco, e o app para iOS e Android está incluído em todos os planos."),
        ]), "white rule"),
        _sec("O Hostlio Pro é o sistema certo para o seu hostel?",
            '<p class="lead" style="font-size:var(--t-0);max-width:70ch">Preferimos dizer agora a descobrir depois de uma migração: o Hostlio Pro controla a disponibilidade por quarto, não por cama.</p>'
            + _table(["Área", "Encaixa bem", "Fale com a gente antes"], [
                ("Inventário", "Quartos privativos, quartos família e dormitórios vendidos inteiros, como uma unidade", "Vender camas avulsas de dormitório compartilhado como inventário separado não é suportado"),
                ("Reservas", "Um quarto por reserva, vinda de qualquer canal ou lançada à mão", "Grupos em vários quartos entram como reservas separadas"),
                ("Tamanho", "De 1 a 150 quartos, uma propriedade, ou duas no Growth", "Mais de duas propriedades ou mais de 150 quartos"),
                ("Pagamentos", "Preços, extras e recibos para imprimir na reserva", "Não há cobrança de cartão, conta corrente (folio) nem PDV integrados"),
                ("Hóspedes", "Viajantes de vários países que escrevem pelo WhatsApp e pelas caixas das OTAs", "—"),
            ])),
        _sec("Trocar de sistema sem parar o hostel", _steps([
            ("Monte quartos e tarifas", "Crie tipos de quarto, quartos e planos tarifários. O assistente de configuração mostra o que falta antes de você entrar no ar."),
            ("Importe as reservas", "Exporte as reservas futuras do sistema antigo em CSV ou Excel e envie. As colunas são associadas automaticamente e as linhas com problema aparecem com o motivo."),
            ("Conecte os canais", "Autorize o Hostelworld, o Booking.com e as outras OTAs e associe seus quartos. A maioria das hospedagens conecta tudo no mesmo dia."),
        ]), "dark on-dark"),
        f'<section class="rule"><div class="wrap"><p>Leia também: <a href="{U("post-overbooking")}">como evitar overbooking entre canais</a> e <a href="{U("post-autoreply")}">como responder automaticamente às mensagens do Booking.com</a>.</p></div></section>',
    ])


HOSTEL_PT_FAQ = [
    ("O Lio responde sobre armários, cozinha e chegada tarde?", "Sim, desde que essas informações estejam nas configurações da hospedagem. O Lio responde no idioma do hóspede e só com o que você cadastrou; se faltar algo, passa a mensagem para a equipe e o painel mostra qual informação acrescentar."),
    ("Dá para receber grupos?", "Uma reserva ocupa um quarto, então um grupo em vários quartos entra como várias reservas. Para grupos grandes, conte como você vende hoje e verificamos a configuração juntos numa demonstração."),
    ("Voluntários e equipe da noite podem ter acesso limitado?", "Sim. Use a função recepção ou visualizador, ou governança para quem só limpa quartos. Você suspende o acesso quando quiser, e o histórico de atividades mostra quem mudou o quê."),
]


def _boutique_pt(U):
    return "".join([
        _sec("IA para hotel boutique sem perder o toque pessoal", _rows([
            ("Seu tom, seus detalhes", "O Lio escreve no idioma do hóspede usando as informações do seu hotel: horário de check-in, café da manhã no jardim, estacionamento, pets, como chegar. Ele não inventa ofertas nem regras que você não cadastrou."),
            ("Você decide o que é automático", "Comece no modo de aprovação e leia cada resposta antes de ela sair. Depois deixe o Lio fechar sozinho as perguntas de rotina e mantenha descontos, reclamações e pedidos especiais com a equipe."),
            ("Uma caixa de entrada para todos", "As mensagens do WhatsApp e, nos planos Pro e Growth, as caixas do Booking.com, do Airbnb e da Expedia chegam a um só lugar, ao lado da reserva. A equipe para de pular de extranet em extranet."),
            ("Limites claros", "O que você digita é enviado exatamente como escrito. O Lio mostra a tradução das próprias respostas e, quando não tem certeza, passa a conversa para você em vez de chutar."),
        ]), "white rule"),
        _sec("Um hotel boutique de 30 quartos num dia comum",
            '<p class="lead" style="font-size:var(--t-0);max-width:70ch">Um exemplo de como as peças se encaixam; os números do seu hotel serão outros.</p>'
            + _table(["Hora", "O que acontece", "Onde no Hostlio Pro"], [
                ("02h10", "Um hóspede de Buenos Aires pergunta se pode chegar depois da meia-noite", "O Lio responde em espanhol com suas regras de check-in"),
                ("08h00", "A dona confere o dia: 9 chegadas, 7 saídas, 2 rascunhos para aprovar", "Tela Hoje e Sugestões do Lio"),
                ("10h30", "Vazamento na pia do quarto 12", "Registro de manutenção; o quarto sai da venda em todos os canais"),
                ("12h00", "A governança limpa as saídas do dia, prioritários primeiro", "Lista de governança, imprimível em PDF"),
                ("15h00", "Os hóspedes que chegam já fizeram o check-in online", "Check-in online com assinatura digital (Pro e Growth)"),
                ("18h00", "Um casal pede transfer para o aeroporto na sexta", "O Lio oferece e repassa o pedido à equipe"),
                ("Segunda", "A dona compara a receita líquida por canal com a semana anterior", "Análises e relatório semanal por e-mail"),
            ])),
        _sec("Mais receita por estadia, sem empurrar venda", _rows([
            ("Extras na hora certa", "Transfer, passeios e outros extras aparecem quando fazem sentido na conversa, e o pedido chega à sua equipe (Pro e Growth)."),
            ("Pedidos de reserva pelo WhatsApp", "Quando o hóspede pergunta por datas no WhatsApp, o Lio coleta datas, número de pessoas e preferência de quarto e informa a sua tarifa. Só vira reserva depois da sua aprovação (Pro e Growth)."),
            ("Sugestões toda manhã", "As Sugestões do Lio apontam oportunidades de preço, operação e receita. Nada muda sem a sua aprovação, e as sugestões de tarifa ficam dentro dos limites que você define."),
            ("Receita líquida por canal", "As análises mostram receita bruta, comissão e líquido de cada OTA, além da visão dos próximos 30, 60 e 90 dias com pickup, para você ver onde a reserva direta compensa mais."),
        ])),
        _sec("Uma chegada que parece boas-vindas, não um formulário", _rows([
            ("Check-in antes da chegada", "O hóspede lê a zona de leitura mecânica do passaporte ou da identidade no próprio celular, adiciona acompanhantes e assina. Nenhuma imagem do documento é guardada, e as assinaturas são excluídas 30 dias após o check-out."),
            ("Link enviado automaticamente", "Ative o e-mail de check-in e toda nova reserva com e-mail recebe o link no idioma do hóspede. Você escolhe a quais origens de reserva isso se aplica."),
            ("Carta para visto em um clique", "Gere uma confirmação de hospedagem para pedidos de visto ou convite direto da reserva e salve em PDF."),
        ]), "white rule"),
        _sec("Checklist para escolher sistema para hotel boutique", _table(["Pergunte a qualquer fornecedor", "Hostlio Pro"], [
            ("O preço é público e fixo, sem comissão por reserva?", "Sim: a partir de ⟦price:starter⟧ por mês, sem comissão, 7 dias grátis"),
            ("O channel manager está incluído?", "Sim, em todos os planos, com conexões certificadas a mais de 100 canais"),
            ("A IA responde no idioma do hóspede, com aprovação?", "Sim: WhatsApp em todos os planos, caixas das OTAs no Pro e no Growth"),
            ("Cada pessoa da equipe vê só o que precisa?", "Sim: seis funções; 3, 8 ou 20 usuários conforme o plano; histórico de atividades"),
            ("Dá para ver a receita por canal depois da comissão?", "Sim, com exportação para Excel e relatórios por e-mail semanais e mensais"),
            ("Consigo trazer as reservas que já tenho?", "Sim, por arquivo CSV ou Excel"),
            ("Tem app para celular?", "Sim, iOS e Android, incluído em todos os planos"),
        ])),
        f'<section class="white rule"><div class="wrap"><p>Leia também: <a href="{U("post-ai")}">como responder hóspedes com IA</a> e <a href="{U("post-pms")}">como escolher um sistema para hotel pequeno</a>.</p></div></section>',
    ])


BOUTIQUE_PT_FAQ = [
    ("A IA não deixa o hotel boutique com cara de rede?", "Só se ela chutar. O Lio responde as perguntas de rotina com as suas informações, no idioma do hóspede, e passa descontos, reclamações e pedidos especiais para a equipe. Muitos hotéis começam no modo de aprovação e leem cada resposta nos primeiros dias."),
    ("Qual plano serve para um hotel boutique de 30 quartos?", "O Pro atende até 50 quartos, com ⟦quota:pro⟧ mensagens de IA por mês, caixas das OTAs, check-in online e venda de extras. O Growth cobre duas propriedades ou até 150 quartos."),
]


# ------------------------------------------------------------------ PT: páginas de produto
_FNRH = "https://www.gov.br/turismo/pt-br/centrais-de-conteudo-/publicacoes/atos-normativos-2/2025/portaria-mtur-no-41-de-14-de-novembro-de-2025"
_LGT = "https://www.planalto.gov.br/ccivil_03/_ato2007-2010/2008/lei/l11771.htm"
_SIBA = "https://siba.ssi.gov.pt/en/ajuda/perguntas-frequentes/"


def _checkin_pt(U):
    return "".join([
        _sec("Check-in online e FNRH Digital (Ficha Nacional de Registro de Hóspedes)",
            '<div class="answer"><p><strong>Em resumo:</strong> no Brasil, a ficha de hóspede em papel foi substituída pela FNRH Digital, a plataforma do Ministério do Turismo. O Hostlio Pro coleta parte desses dados no check-in online e permite exportá-los, mas <strong>não envia nada à FNRH Digital</strong> e não está integrado à API da plataforma: o registro continua sendo feito pela sua hospedagem.</p></div>'
            + _rows([
                ("O que é", f"A <a href=\"{_FNRH}\" rel=\"noopener\">Portaria MTur nº 41, de 14 de novembro de 2025</a>, com base no art. 26 da <a href=\"{_LGT}\" rel=\"noopener\">Lei Geral do Turismo (Lei nº 11.771/2008)</a>, instituiu a FNRH em meio digital para os meios de hospedagem de todo o país, em substituição à ficha em papel (vedada a exigência de ficha física, salvo contingência). A portaria passou a valer 150 dias após a publicação no Diário Oficial de 21 de novembro de 2025, e o acesso exige conta gov.br e cadastro regular no Cadastur."),
                ("Como funciona", "É gerada uma ficha para cada hóspede; menores e pessoas legalmente incapazes ficam vinculados à ficha do responsável. O hóspede pode fazer um pré-check-in na própria plataforma, por QR Code ou link da hospedagem, com ou sem conta gov.br (estrangeiros não precisam dela). Com ou sem pré-check-in, o check-in é confirmado no estabelecimento, na presença do hóspede, com conferência dos dados e documentos, e depois se registra o checkout."),
                ("Que dados pede", "Identificação (nome completo, nome social, data de nascimento, nacionalidade, sexo, tipo e número do documento, CPF ou passaporte para estrangeiros), contato (telefone e e-mail), endereço completo de residência, informações da viagem (motivo, origem, próximo destino, meio de transporte, placa do veículo) e dados da hospedagem (código da reserva, datas previstas e efetivas, número de hóspedes, tipo de unidade)."),
                ("Como se envia", "Pelos módulos da própria Plataforma FNRH Digital (Reservas, Hóspedes e Fichas) ou por um PMS integrado à API da plataforma com credencial própria do estabelecimento. Um sistema sem essa integração não substitui o registro na plataforma."),
            ])
            + f'<p class="small muted">Em Portugal a regra é outra: o alojamento de cidadãos estrangeiros é comunicado pelo SIBA (Sistema de Informação de Boletins de Alojamento) em até três dias úteis, na entrada e na saída (<a href="{_SIBA}" rel="noopener">perguntas frequentes do SIBA</a>). O Hostlio Pro também não envia dados ao SIBA.</p>'
            + f'<p class="small muted">Fontes: <a href="{_FNRH}" rel="noopener">Portaria MTur nº 41/2025 (Ministério do Turismo)</a>, <a href="{_LGT}" rel="noopener">Lei nº 11.771/2008 (Planalto)</a> e <a href="{_SIBA}" rel="noopener">SIBA</a>. Consultado em outubro de 2026. Esta seção é informativa e não é aconselhamento jurídico.</p>',
            "white rule"),
        _sec("Quais dados da FNRH o check-in online do Hostlio Pro coleta",
            '<p class="lead" style="font-size:var(--t-0);max-width:70ch">Veja como o formulário de check-in se compara aos campos da FNRH. O que falta é completado por você ou pelo hóspede na Plataforma FNRH Digital.</p>'
            + _table(["Campo da FNRH", "O Hostlio Pro coleta?"], [
                ("Nome completo", "Sim, em um único campo"),
                ("Tipo e número do documento / passaporte", "Sim: passaporte ou identidade, lidos da zona MRZ ou digitados"),
                ("Nacionalidade e data de nascimento", "Sim"),
                ("Endereço de residência", "Sim, do titular da reserva (campo opcional)"),
                ("Acompanhantes", "Sim: nome, documento, nacionalidade e data de nascimento de até 10 pessoas"),
                ("CPF", "Não há campo próprio"),
                ("Nome social e sexo", "Não"),
                ("Telefone e e-mail", "Não no formulário; costumam estar na reserva"),
                ("Motivo da viagem, origem, próximo destino, transporte e placa", "Não"),
                ("Menores vinculados e autorizações", "Não"),
            ])),
        _sec("Como usar os dois sem retrabalho", _steps([
            ("O hóspede faz o check-in online", "Antes de chegar, lê o documento com o celular, adiciona acompanhantes, aceita as regras da casa e assina. Nenhuma imagem do documento é guardada."),
            ("Você exporta os dados", "No painel, baixe um CSV com os hóspedes registrados num intervalo de datas (nome, tipo e número do documento, nacionalidade, data de nascimento e data de entrada). Reservas canceladas ficam de fora."),
            ("Você registra na FNRH Digital", "Use os dados para conferir ou completar as fichas na Plataforma FNRH Digital e confirme o check-in na presença do hóspede, como manda a portaria. O Hostlio Pro não gera fichas na plataforma nem se conecta à sua API."),
        ]), "dark on-dark"),
        _sec("Check-in online dentro do PMS, sem ferramenta extra", _rows([
            ("Tudo na mesma reserva", "Muitos sistemas resolvem o check-in online com uma ferramenta externa, ligada por integração e com assinatura própria. No Hostlio Pro o check-in faz parte do PMS: o link sai da reserva e os dados, a assinatura e os acompanhantes voltam para ela."),
            ("Na recepção, sem digitar", "Se o hóspede não preencher o link, a equipe pode ler o documento pelo painel; a leitura acontece no aparelho e nenhuma imagem é guardada."),
            ("Privacidade e LGPD", "Só a equipe da sua hospedagem vê os dados do documento, as assinaturas são excluídas 30 dias após o check-out e o texto de consentimento faz parte do formulário. Na LGPD, a hospedagem é a controladora e o Hostlio Pro atua como operador."),
        ])),
        _sec("O que muda na recepção", _table(["Sem check-in online", "Com o check-in online do Hostlio Pro"], [
            ("Xerox ou foto do documento", "Só os dados extraídos; nenhuma imagem guardada"),
            ("Digitar nomes e números de passaporte", "Os dados chegam preenchidos pela zona MRZ"),
            ("Fila quando chega um grupo ou um voo", "Cada hóspede chega com o formulário pronto"),
            ("Termo de regras da casa em papel", "Aceite e assinatura digital na reserva, excluída 30 dias após o check-out"),
        ]), "white rule"),
    ])


CHECKIN_PT_FAQ = [
    ("O Hostlio Pro envia a ficha de hóspedes para a FNRH Digital?", "Não. O Hostlio Pro coleta parte dos dados no check-in online e permite exportá-los em CSV, mas não está integrado à API da Plataforma FNRH Digital. O registro e a confirmação do check-in na plataforma continuam com a hospedagem."),
    ("Que dados da FNRH vou ter que completar?", "O formulário não coleta CPF em campo próprio, nome social, sexo, telefone e e-mail, dados da viagem (motivo, origem, destino, transporte, placa) nem os dados de menores vinculados. Eles precisam ser preenchidos na Plataforma FNRH Digital."),
    ("Preciso de outra ferramenta de check-in além do PMS?", "Não para o check-in online do hotel: nos planos Pro e Growth ele já faz parte do Hostlio Pro, sem outra assinatura. O registro oficial de hóspedes, porém, é feito na Plataforma FNRH Digital."),
]


def _channel_pt(U):
    return "".join([
        _sec("Como a sincronização funciona, passo a passo", _steps([
            ("Monte seu inventário", "Tipos de quarto, quartos e planos tarifários no Hostlio Pro. Ele vira a única fonte de disponibilidade para todos os canais."),
            ("Conecte cada OTA", "Autorize a conexão na extranet do Booking.com, do Airbnb, da Expedia ou do canal que você usa e associe seus quartos. A maioria das hospedagens conecta no mesmo dia."),
            ("Venda sem copiar nada", "Cada reserva, alteração ou cancelamento cai sozinho no mapa de reservas, e a disponibilidade se ajusta nos outros canais."),
        ]), "dark on-dark"),
        _sec("PMS com channel manager integrado: por que faz diferença", _rows([
            ("Uma só disponibilidade", "Quando channel manager e PMS são o mesmo sistema, não existem dois calendários para sair de sincronia. Uma reserva por telefone, um quarto fora de serviço ou um cancelamento mudam a disponibilidade em todos os canais ao mesmo tempo."),
            ("Booking.com e Airbnb juntos", "Muita pousada começa no Airbnb e depois entra no Booking.com, e é aí que nasce o overbooking. Com os dois conectados ao mesmo calendário, uma noite vendida num canal fecha no outro."),
            ("Mensagens ao lado da reserva", "As mensagens dos hóspedes do Booking.com, do Airbnb e da Expedia chegam à caixa de entrada do Lio com a reserva ao lado (planos Pro e Growth), e o Lio responde no idioma do hóspede."),
            ("Relatórios por canal", "Receita bruta, comissão e líquido de cada OTA, ocupação, ADR e RevPAR e a visão dos próximos 30, 60 e 90 dias. Exporte para Excel quando precisar."),
        ]), "white rule"),
        _sec("Tarifas e restrições: para que serve cada uma",
            _table(["Restrição", "Para que serve", "Exemplo"], [
                ("Preço", "A diária de cada tipo de quarto e plano", "Duplo standard a R$ 380 de segunda a quinta"),
                ("Estadia mínima / máxima", "Limita quantas noites o hóspede pode reservar", "Mínimo de 4 noites no Carnaval"),
                ("Fechado para chegada (CTA)", "Ninguém chega nesse dia, mas pode estar hospedado", "Sem chegadas no sábado do réveillon"),
                ("Fechado para saída (CTD)", "Ninguém sai nesse dia", "Evitar saídas no domingo para não deixar buracos"),
                ("Stop sell", "Fecha a venda daquele tipo de quarto ou plano", "Fechar a tarifa não reembolsável na alta temporada"),
            ])
            + '<p style="margin-top:18px">Na edição em massa você escolhe um período, os tipos de quarto e os planos e aplica tudo de uma vez. Se um canal não receber uma atualização, o botão «reenviar aos canais» manda de novo as tarifas e a disponibilidade atuais.</p>'),
        _sec("Existe channel manager gratuito?", _rows([
            ("O que costuma haver por trás", "Channel managers «gratuitos» geralmente cobram comissão por reserva, limitam o número de canais ou vêm presos a um motor de reservas. Com comissão, o custo sobe justamente quando você mais vende."),
            ("Como fazemos", "O Hostlio Pro não é gratuito, mas o preço é fixo e público: a partir de ⟦price:starter⟧ por mês, sem comissão por reserva, com o channel manager incluído em todos os planos e 7 dias de teste grátis."),
        ]), "white rule"),
        _sec("Trocar de channel manager sem overbooking", _table(["Passo", "O que fazer"], [
            ("1. Prepare o inventário", "Crie tipos de quarto e planos no Hostlio Pro com os mesmos nomes que você usa nas OTAs."),
            ("2. Importe as reservas futuras", "Exporte as reservas do sistema atual em CSV ou Excel e envie; duplicatas são ignoradas."),
            ("3. Conecte num horário tranquilo", "Desconecte o canal no sistema anterior e conecte no Hostlio Pro, um por vez ou todos no mesmo dia."),
            ("4. Revise o mapa de reservas", "A verificação de conflitos lista reservas duplicadas ou sem quarto atribuído."),
            ("5. Compare a disponibilidade", "Confira na extranet de cada OTA se a disponibilidade bate com o seu mapa."),
        ]) + f'<p style="margin-top:18px">Mais detalhes no guia <a href="{U("post-overbooking")}">como evitar overbooking</a>.</p>'),
    ])


CHANNEL_PT_FAQ = [
    ("Existe channel manager gratuito?", "O Hostlio Pro não é gratuito, mas você pode testar por 7 dias sem custo. Depois, o channel manager está incluído em todos os planos a partir de ⟦price:starter⟧ por mês, sem comissão por reserva."),
    ("Qual a diferença entre PMS e channel manager?", "O PMS é o sistema de gestão do dia a dia: reservas, quartos, hóspedes, governança. O channel manager distribui disponibilidade e tarifas para as OTAs. No Hostlio Pro os dois são o mesmo sistema, então não há calendários para conciliar."),
    ("Quanto tempo leva para conectar um canal?", "Sua conta fica pronta em minutos. Para cada OTA você autoriza a conexão na extranet e associa os quartos; a maioria das hospedagens conecta os canais no mesmo dia."),
]


TYPE_MORE = {
    "en": {"t-hostel": (_hostel_en, HOSTEL_EN_FAQ), "t-boutique": (_boutique_en, BOUTIQUE_EN_FAQ)},
    "es": {"t-hostel": (_hostel_es, HOSTEL_ES_FAQ), "t-boutique": (_boutique_es, BOUTIQUE_ES_FAQ)},
    "tr": {"t-hostel": (_hostel_tr, HOSTEL_TR_FAQ), "t-boutique": (_boutique_tr, BOUTIQUE_TR_FAQ)},
    "fr": {"t-hostel": (_hostel_fr, HOSTEL_FR_FAQ), "t-boutique": (_boutique_fr, BOUTIQUE_FR_FAQ)},
    "it": {"t-hostel": (_hostel_it, HOSTEL_IT_FAQ), "t-boutique": (_boutique_it, BOUTIQUE_IT_FAQ)},
    "pt": {"t-hostel": (_hostel_pt, HOSTEL_PT_FAQ), "t-boutique": (_boutique_pt, BOUTIQUE_PT_FAQ)},
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
    "en": {"checkin": (_checkin_en, CHECKIN_EN_FAQ), "channel": (_channel_en, CHANNEL_EN_FAQ)},
    "tr": {"checkin": (_checkin_tr, CHECKIN_TR_FAQ), "channel": (_channel_tr, CHANNEL_TR_FAQ)},
    "fr": {"checkin": (_checkin_fr, CHECKIN_FR_FAQ), "channel": (_channel_fr, CHANNEL_FR_FAQ)},
    "it": {"checkin": (_checkin_it, CHECKIN_IT_FAQ), "channel": (_channel_it, CHANNEL_IT_FAQ)},
    "pt": {"checkin": (_checkin_pt, CHECKIN_PT_FAQ), "channel": (_channel_pt, CHANNEL_PT_FAQ)},
}


def more(L, page):
    f = PAGE_MORE.get(L, {}).get(page)
    return f[0](lambda k: url(k, L)) if f else ""


def faq(L, page):
    f = PAGE_MORE.get(L, {}).get(page)
    return list(f[1]) if f else []
