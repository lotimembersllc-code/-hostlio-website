from build import btn, icon, logo, url, room_rack, channel_strip, faq_block, SIGNUP_URL, EMAIL, UPDATED, CHECK, software_schema, SITE, PLANS
L = "es"
def U(k): return url(k, L)

MESES = ["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]
def D(iso):
    y, m, d = iso[:10].split("-")
    return f"{int(d)} de {MESES[int(m)-1]} de {y}"

PLAN_TXT = {
 "starter": ("Para hostales, pensiones y hoteles boutique pequeños", ["1 alojamiento, hasta 10 habitaciones, 3 usuarios","⟦quota:starter⟧ mensajes de IA / mes","Sincronización de reservas de OTAs (más de 100 canales)","Mensajería IA por WhatsApp","Sugerencias de Lio cada mañana","Calendario de reservas (planning de habitaciones)","Confirmación de alojamiento para visados (PDF)"]),
 "pro":     ("Para hoteles en crecimiento con un solo alojamiento", ["1 alojamiento, hasta 50 habitaciones, 8 usuarios","⟦quota:pro⟧ mensajes de IA / mes","Todo lo de Starter","Mensajería por WhatsApp y bandejas de las OTAs (Booking.com, Airbnb, Expedia)","Lio recibe solicitudes de reserva por WhatsApp (con tu aprobación)","Análisis con IA de reseñas y mensajes","Check-in online con firma digital","Venta de traslados, excursiones y extras","App móvil para iOS y Android"]),
 "growth":  ("Para equipos que gestionan dos alojamientos", ["Hasta 2 alojamientos, 150 habitaciones en total, 20 usuarios","⟦quota:growth⟧ mensajes de IA / mes","Todo lo de Pro","Resumen semanal con IA","Sincronización de canales prioritaria","Soporte prioritario (siguiente día hábil)","Llamada de onboarding personalizada","Opciones de marca blanca"]),
}

def plans_html():
    out = []
    for p in PLANS:
        for_, feats = PLAN_TXT[p["id"]]
        pop = p["id"] == "pro"
        lis = "".join(f"<li>{CHECK}<span>{f}</span></li>" for f in feats)
        out.append(f'''<article class="plan{" pop" if pop else ""}" aria-labelledby="plan-{p["id"]}">
{'<span class="tag">El más elegido</span>' if pop else ""}
<h3 id="plan-{p["id"]}">{p["name"]}</h3><p class="for">{for_}</p>
<div class="price num"><b data-price="{p["id"]}">⟦price:{p["id"]}⟧</b><span class="muted">/ mes</span></div>
<p class="small muted num" style="margin:0" data-eb>Precio de lanzamiento (normalmente <s data-regular="{p["id"]}">⟦regular:{p["id"]}⟧</s>)</p>
<ul>{lis}</ul>
{btn("Empieza con "+p["name"], SIGNUP_URL+"?plan="+p["id"], "primary" if pop else "ghost")}
</article>''')
    return '<div class="plans">' + "".join(out) + "</div>"

FAQ_CORE = [
 ("¿Qué es Hostlio Pro?", "Hostlio Pro es un software de gestión hotelera (PMS hotelero) con inteligencia artificial, creado para hoteles independientes, hoteles boutique y hostales. Reúne en una sola plataforma a Lio, un asistente de IA que responde a los huéspedes 24/7 en más de 30 idiomas, un channel manager conectado a más de 100 OTAs, un calendario de reservas con arrastrar y soltar y el check-in online."),
 ("¿Cuánto cuesta Hostlio Pro?", "Hay tres planes: Starter a ⟦price:starter⟧/mes, Pro a ⟦price:pro⟧/mes y Growth a ⟦price:growth⟧/mes. Estos precios incluyen un descuento de lanzamiento del ⟦eb_pct⟧ para los primeros 50 clientes, que se mantiene mientras sigas suscrito. Los precios normales son ⟦regular:starter⟧, ⟦regular:pro⟧ y ⟦regular:growth⟧."),
 ("¿Hay una prueba gratuita?", "Sí. Todos los planes incluyen una prueba gratuita de 7 días. Introduces una tarjeta al registrarte, pero no se te cobra nada hasta que termine la prueba y puedes cancelar antes cuando quieras. No hay contratos de permanencia."),
 ("¿Con qué OTAs se conecta Hostlio Pro?", "A través de Channex, Hostlio Pro se conecta con más de 100 canales, entre ellos Booking.com, Airbnb, Expedia, Agoda, Trip.com, Hotels.com, Hotelbeds, Hostelworld y Google Hotels. La disponibilidad, las tarifas y las reservas se mantienen sincronizadas en todos ellos."),
 ("¿En qué idiomas responde Lio?", "Lio responde en más de 30 idiomas, entre ellos inglés, turco, árabe, ruso, alemán, japonés y chino. Contesta en el idioma del huésped y tú ves la traducción en tu panel."),
]

def home():
    import home_v3
    return home_v3.home(L, plans_html, FAQ_CORE)

def ai():
    body = f'''
<section class="page-hero"><div class="wrap split">
<div><h1>Lio, el asistente de IA para mensajes de huéspedes</h1>
<p class="lead">Lio es un asistente de IA entrenado con la información de tu hotel. Responde a los huéspedes por WhatsApp y en las bandejas de las OTAs (Booking.com, Airbnb, Expedia) en más de 30 idiomas, a cualquier hora.</p>
<div class="cta-row">{btn("Prueba Lio gratis durante 7 días", SIGNUP_URL)}</div></div>
<div class="panel typing"><p class="panel-title">WhatsApp, 02:47</p>
<div class="msg in" style="background:var(--bg)" lang="de">Hallo! Unser Flug landet um 1 Uhr. Können Sie uns abholen, und ist ein später Check-in möglich?</div>
<div class="msg out" lang="de">Natürlich! Unser Flughafentransfer kostet 35 € für bis zu 3 Gäste. Soll ich ihn für Ihre Ankunft um 1 Uhr buchen? Später Check-in ist kein Problem.<small lang="es">Lio, alemán</small></div>
<p class="small muted" style="margin:10px 0 0">Solicitud de traslado creada y enviada a tu equipo.</p></div>
</div></section>

<section class="white rule"><div class="wrap">
<div class="answer"><p><strong>¿Qué es un asistente de IA para mensajes de huéspedes de hotel?</strong> Un software que responde automáticamente a las preguntas que hacen los huéspedes antes y después de reservar, usando la información del propio hotel. Lio pasa a tu equipo los mensajes que no sabe responder o que requieren una decisión humana (peticiones de descuento, quejas, solicitudes especiales).</p></div>
<h2 style="margin-top:64px">Qué hace Lio</h2><div class="rows">
<div class="row"><h3>Una sola bandeja de entrada</h3><div><p>Los mensajes de WhatsApp y de las bandejas de Booking.com, Airbnb y Expedia llegan a una sola pantalla. Lio asocia automáticamente a cada huésped con su reserva.</p></div></div>
<div class="row"><h3>Más de 30 idiomas, con traducción automática</h3><div><p>El huésped escribe en japonés y Lio responde en japonés; tú ves la traducción de la respuesta de Lio en tu idioma. Las respuestas que escribes tú se envían tal cual, sin traducción automática.</p></div></div>
<div class="row"><h3>Conoce tu hotel</h3><div><p>Horarios de check-in y check-out, aparcamiento, política de mascotas, horario del desayuno, transporte y características de las habitaciones. Los introduces una vez y Lio los usa de forma coherente en cada respuesta.</p></div></div>
<div class="row"><h3>Un asistente que vende</h3><div><p>Lio no solo responde preguntas: ofrece traslados al aeropuerto, visitas por la ciudad y extras en el momento adecuado, y pasa la solicitud a tu equipo.</p></div></div>
<div class="row"><h3>Recibe solicitudes de reserva</h3><div><p>En los planes Pro y Growth, cuando un huésped pregunta por una habitación en WhatsApp, Lio recoge las fechas, el número de personas y la habitación que prefiere, y le da un precio según tus tarifas y tu disponibilidad. La solicitud te llega a ti y se convierte en reserva cuando la apruebas.</p></div></div>
<div class="row"><h3>Sugerencias cada mañana</h3><div><p>Cada mañana, las Sugerencias de Lio señalan oportunidades de precio, tareas operativas (habitaciones por limpiar, solicitudes pendientes), ajustes de configuración que faltan y oportunidades de ingresos. Nada cambia sin tu aprobación y las sugerencias de precio no salen de los límites que tú fijas. Incluidas en todos los planes.</p></div></div>
<div class="row"><h3>Análisis de reseñas y mensajes</h3><div><p>En Pro y Growth, Lio resume los temas de queja y de elogio que se repiten en las reseñas y los mensajes de tus huéspedes. El resumen semanal con IA viene incluido en Growth y es opcional en Pro.</p></div></div>
<div class="row"><h3>Tú mantienes el control</h3><div><p>Durante los primeros días puedes aprobar las respuestas de Lio antes de que se envíen. Tú decides qué temas cierra Lio por su cuenta y cuáles te pasa a ti.</p></div></div>
</div></div></section>

<section><div class="wrap">
<div class="section-head"><h2>Cuota de mensajes de IA por plan</h2><p>Un mensaje es una sola respuesta que Lio envía a un huésped.</p></div>
<div class="table-wrap"><table><thead><tr><th>Plan</th><th class="c">Mensajes de IA / mes</th><th>Canales de mensajería</th></tr></thead><tbody>
<tr><th>Starter</th><td class="c num">⟦quota:starter⟧</td><td>WhatsApp</td></tr>
<tr><th>Pro</th><td class="c num">⟦quota:pro⟧</td><td>WhatsApp + bandejas de OTAs (Booking.com, Airbnb, Expedia)</td></tr>
<tr><th>Growth</th><td class="c num">⟦quota:growth⟧</td><td>WhatsApp + bandejas de OTAs (Booking.com, Airbnb, Expedia)</td></tr>
</tbody></table></div>
</div></section>
'''
    faq = [
     ("¿Y si Lio da información incorrecta?", "Lio solo usa la información del hotel y los datos de reserva que tú le proporcionas. Cuando no está seguro, te pasa el mensaje en lugar de adivinar. También puedes aprobar cada respuesta antes de que se envíe."),
     ("¿Responde también a los mensajes de Booking.com y Airbnb?", "Sí. En los planes Pro y Growth, los mensajes de las OTAs llegan a la bandeja de Lio y se responden de la misma manera."),
     ("¿Lio puede recibir reservas?", "Sí, en los planes Pro y Growth y siempre con tu aprobación. Cuando un huésped escribe por WhatsApp, Lio le pregunta las fechas, el número de personas y la habitación que prefiere, le da un precio según tus tarifas y tu disponibilidad y te pasa la solicitud. Solo se convierte en reserva cuando tú la apruebas; Lio nunca confirma una reserva por su cuenta. Las solicitudes de servicios extra, como traslados o excursiones, funcionan igual."),
     ("¿Qué pasa cuando se agota la cuota de mensajes?", "Los mensajes siguen llegando y aparecen en tu panel; solo se pausan las respuestas automáticas. Puedes pasarte a un plan superior para ampliar tu cuota."),
     FAQ_CORE[4],
    ]
    return {"key":"ai","title":"Mensajería con IA para hoteles en 30+ idiomas | Hostlio Pro",
            "desc":"Lio, la IA de Hostlio Pro, responde a tus huéspedes 24/7 por WhatsApp y en las OTAs en 30+ idiomas, recibe solicitudes de reserva y te sugiere mejoras.",
            "trail":[("Asistente IA Lio", U("ai"))],"body":body,"faq":faq}

def channel():
    body = f'''
<section class="page-hero"><div class="wrap split">
<div><h1>Un channel manager para más de 100 OTAs</h1>
<p class="lead">Gestiona la disponibilidad, las tarifas y las reservas de Booking.com, Airbnb, Expedia, Agoda y más de 100 canales desde un solo calendario. Hostlio Pro sincroniza en tiempo real y en ambos sentidos.</p>
<div class="cta-row">{btn("Empieza tu prueba gratuita de 7 días", SIGNUP_URL)}</div></div>
<div class="panel"><p class="panel-title">Canales conectados</p><div class="chan-list">
<div><span>Booking.com</span><span class="pill">Sincronizado</span></div>
<div><span>Airbnb</span><span class="pill">Sincronizado</span></div>
<div><span>Expedia</span><span class="pill">Sincronizado</span></div>
<div><span>Agoda</span><span class="pill">Sincronizado</span></div>
<div><span>Google Hotels</span><span class="pill">Sincronizado</span></div>
</div></div>
</div></section>
<section class="white rule"><div class="wrap">
<div class="answer"><p><strong>¿Qué es un channel manager?</strong> Un software que mantiene sincronizadas la disponibilidad y las tarifas de un hotel mientras vende habitaciones en varios canales online a la vez. Cuando una habitación se vende en un canal, se cierra al instante en todos los demás, lo que evita las reservas duplicadas (overbooking).</p></div>
<h2 style="margin-top:64px">Qué hace el channel manager</h2><div class="rows">
<div class="row"><h3>Sincronización bidireccional</h3><div><p>Las nuevas reservas, modificaciones y cancelaciones aparecen automáticamente en el planning de habitaciones, y los cambios que haces en el calendario se envían a todos los canales.</p></div></div>
<div class="row"><h3>Tarifas y restricciones</h3><div><p>Envía tarifas, estancias mínimas y cierres de venta por tipo de habitación a todos los canales desde una sola pantalla.</p></div></div>
<div class="row"><h3>Planning de habitaciones por colores</h3><div><p>Ve de un vistazo de qué canal viene cada reserva. Reasigna habitaciones arrastrando y soltando.</p></div></div>
<div class="row"><h3>Conectado a la mensajería</h3><div><p>Los mensajes de los huéspedes de reservas de OTAs llegan a la bandeja de Lio con el huésped, la habitación y las fechas junto a cada conversación.</p></div></div>
</div></div></section>
<section><div class="wrap"><div class="section-head"><h2>Principales canales compatibles</h2><p>La lista sigue nuestra red de conexiones certificadas. ¿Echas en falta algún canal? Escríbenos.</p></div>
<div class="table-wrap"><table><thead><tr><th>Canal</th><th>Tipo</th></tr></thead><tbody>
<tr><th>Booking.com</th><td>OTA</td></tr><tr><th>Airbnb</th><td>Alquiler de corta estancia</td></tr><tr><th>Expedia, Hotels.com</th><td>OTA</td></tr>
<tr><th>Agoda, Trip.com</th><td>OTA (enfocada en Asia)</td></tr><tr><th>Hotelbeds</th><td>Mayorista (banco de camas)</td></tr><tr><th>Hostelworld</th><td>Marketplace de hostels</td></tr><tr><th>Google Hotels</th><td>Metabuscador</td></tr>
</tbody></table></div></div></section>
'''
    faq = [FAQ_CORE[3],
     ("¿El channel manager está incluido en todos los planes?", "Sí. Starter, Pro y Growth incluyen la sincronización con más de 100 OTAs. Growth añade sincronización prioritaria."),
     ("¿Es difícil cambiar desde mi channel manager actual?", "No. Crea tus tipos de habitación en Hostlio Pro y vincula tus cuentas de OTAs a través de Channex. Nuestro equipo de onboarding te ayuda durante el cambio."),
    ]
    return {"key":"channel","title":"Channel manager hotelero para 100+ OTAs | Hostlio Pro",
            "desc":"El channel manager de Hostlio Pro sincroniza en tiempo real disponibilidad y tarifas con 100+ OTAs (Booking.com, Airbnb, Expedia, Agoda) sin overbooking.",
            "trail":[("Channel manager", U("channel"))],"body":body,"faq":faq}

def checkin():
    body = f'''
<section class="page-hero"><div class="wrap split">
<div><h1>Check&#8209;in online con firma digital</h1>
<p class="lead">Antes de llegar, los huéspedes escanean su documento de identidad con el móvil, añaden a sus acompañantes y firman. No se guarda ninguna imagen del documento. Entregar la llave lleva solo unos minutos.</p>
<div class="cta-row">{btn("Prueba Pro gratis durante 7 días", SIGNUP_URL+"?plan=pro")}</div></div>
<div class="panel"><p class="panel-title">Check-in online, habitación 202</p>
<div class="field"><span>Nombre completo</span><div>Keiko Sato</div></div>
<div class="field"><span>Nacionalidad</span><div>Japón</div></div>
<div class="field"><span>Documento</span><div>Pasaporte escaneado, sin imagen guardada</div></div>
<div class="field"><span>Acompañantes</span><div>1 huésped añadido</div></div>
<div class="field"><span>Firma</span><div class="sig">Firma digital recibida</div></div>
</div>
</div></section>
<section class="white rule"><div class="wrap">
<div class="answer"><p><strong>¿Cómo funciona el check-in online?</strong> Hostlio Pro envía a quien hizo la reserva un enlace personal, seguro y con caducidad. Desde ese enlace, el huésped escanea con la cámara del móvil la zona de lectura mecánica (MRZ) de su pasaporte o documento de identidad. La lectura se hace en su propio navegador y los datos se rellenan solos. Después añade a sus acompañantes y firma el formulario digitalmente. En la reserva solo se guardan los datos extraídos y la firma; ninguna imagen del documento se sube ni se almacena.</p></div>
<h2 style="margin-top:64px">Funcionalidades del check-in online</h2><div class="rows">
<div class="row"><h3>Enlace seguro</h3><div><p>Un enlace basado en token, único para cada reserva. Solo abre el formulario de esa reserva.</p></div></div>
<div class="row"><h3>Escaneo del documento sin guardar imágenes</h3><div><p>La zona de lectura mecánica del pasaporte o del documento de identidad se lee en el propio dispositivo del huésped. Solo se guardan el nombre, el número de documento, la nacionalidad, la fecha de nacimiento y la fecha de caducidad, nunca una foto del documento. Los documentos sin zona de lectura mecánica se introducen a mano.</p></div></div>
<div class="row"><h3>Acompañantes</h3><div><p>Todas las personas que se alojan en la habitación se añaden en un solo formulario, así nadie tiene que escribir datos en recepción.</p></div></div>
<div class="row"><h3>Firma digital y consentimiento</h3><div><p>Los huéspedes aceptan las normas de la casa y el consentimiento de datos firmando en pantalla. Las firmas se eliminan automáticamente 30 días después del check-out.</p></div></div>
<div class="row"><h3>Privacidad desde el diseño</h3><div><p>Los datos de los huéspedes pueden eliminarse a petición, y el texto de consentimiento forma parte del formulario.</p></div></div>
<div class="row"><h3>Exportación para comunicaciones oficiales</h3><div><p>Los datos recogidos de los huéspedes pueden exportarse en un formato útil para cumplir los requisitos locales de registro de viajeros.</p></div></div>
</div></div></section>
<section class="dark on-dark"><div class="wrap"><div class="section-head"><h2>Tres pasos para el huésped</h2></div>
<ol class="steps"><li><h3>Abrir el enlace</h3><p>Toca el enlace personal que recibes una vez confirmada la reserva.</p></li>
<li><h3>Escanear el documento</h3><p>Escanea el pasaporte o el documento de identidad con el móvil: los datos se rellenan solos y no se guarda ninguna imagen. Después indica los acompañantes.</p></li>
<li><h3>Firmar</h3><p>Acepta las normas de la casa y firma en pantalla. En recepción, solo queda recoger la llave.</p></li></ol>
</div></section>
'''
    faq = [("¿Qué planes incluyen el check-in online?", "El check-in online con firma digital está incluido en los planes Pro y Growth."),
           ("¿El huésped tiene que descargar una app?", "No. El formulario de check-in se abre en el navegador; no hace falta descargar ninguna app."),
           ("¿Y si un huésped no completa el enlace?", "Haz el check-in de la forma habitual. El personal también puede escanear el documento en recepción con la app móvil de Hostlio Pro; se lee en el dispositivo y no se guarda ninguna imagen."),
           ("¿Se guardan fotos de los documentos de identidad?", "No. La zona de lectura mecánica (MRZ) del documento se lee en el móvil del huésped, o en el dispositivo del hotel con la app móvil de Hostlio Pro, y solo se guardan los datos extraídos y la firma. Se pueden escanear pasaportes y documentos de identidad con MRZ; los demás se introducen a mano.")]
    return {"key":"checkin","title":"Check-in online para hoteles con firma digital | Hostlio Pro",
            "desc":"Check-in online de Hostlio Pro: el huésped escanea su documento (sin guardar imágenes), añade acompañantes y firma desde el móvil. Sin colas en recepción.",
            "trail":[("Check-in online", U("checkin"))],"body":body,"faq":faq}

def features():
    body = f'''
<section class="page-hero"><div class="wrap split"><div><h1>Todo lo que incluye Hostlio Pro</h1>
<p class="lead">Los módulos que un hotel independiente necesita en el día a día: comunicación con huéspedes, distribución, reservas, check-in e ingresos adicionales.</p></div><div class="hero-img"><img src="/assets/img/gen-team-desk.webp" alt="" width="1080" height="1350"></div></div></section>
<section class="white rule"><div class="wrap"><h2 class="sr-only">Módulos</h2><div class="rows">
<div class="row"><h3>Asistente IA Lio</h3><div><p>Respuestas a huéspedes 24/7 en más de 30 idiomas. Mensajes de WhatsApp y de las OTAs (Booking.com, Airbnb, Expedia) en una sola bandeja.</p><a href="{U("ai")}">Más sobre Lio</a></div></div>
<div class="row"><h3>Channel manager</h3><div><p>Sincronización de disponibilidad, tarifas y reservas con más de 100 OTAs mediante conexiones certificadas.</p><a href="{U("channel")}">Channel manager</a></div></div>
<div class="row"><h3>Planning de habitaciones</h3><div><p>Calendario de reservas con arrastrar y soltar. Arrastra una reserva para cambiarla de habitación y ve de un vistazo las habitaciones libres y los conflictos.</p></div></div>
<div class="row"><h3>Check-in online</h3><div><p>Enlace seguro, acompañantes, escaneo del documento (sin guardar imágenes) y firma digital.</p><a href="{U("checkin")}">Check-in online</a></div></div>
<div class="row"><h3>Confirmación de alojamiento para visados</h3><div><p>Prepara en un clic, a partir de la reserva, la confirmación de alojamiento que el huésped necesita para su visado o carta de invitación. Guárdala en PDF o imprímela.</p></div></div>
<div class="row"><h3>Venta de traslados y excursiones</h3><div><p>Lio sugiere traslados al aeropuerto y excursiones durante la conversación y pasa la solicitud a tu equipo.</p></div></div>
<div class="row"><h3>Sugerencias de Lio y análisis con IA</h3><div><p>Cada mañana Lio prepara sugerencias sobre precios, operaciones (habitaciones pendientes de limpieza, solicitudes sin atender), configuración incompleta y oportunidades de ingresos. Nada cambia sin tu aprobación y las sugerencias de precio respetan los límites que tú fijas. En Pro y Growth también resume las quejas y los elogios que se repiten en reseñas y mensajes.</p></div></div>
<div class="row"><h3>Informes y equipo</h3><div><p>Informes de ocupación, ADR, RevPAR y rendimiento por canal, con un informe semanal y mensual por email. Seis roles de personal con sus propios permisos y todas las notificaciones en un solo lugar.</p></div></div>
<div class="row"><h3>App móvil</h3><div><p>Gestiona reservas, mensajes y check-ins fuera del hotel con la app para iOS y Android.</p></div></div>
</div></div></section>
<section><div class="wrap"><div class="section-head"><h2>Funcionalidades por plan</h2></div>
<div class="table-wrap"><table><thead><tr><th>Funcionalidad</th><th class="c">Starter</th><th class="c">Pro</th><th class="c">Growth</th></tr></thead><tbody>
<tr><th>Alojamientos</th><td class="c">1</td><td class="c">1</td><td class="c">2</td></tr>
<tr><th>Límite de habitaciones</th><td class="c num">10</td><td class="c num">50</td><td class="c num">150</td></tr>
<tr><th>Usuarios (cuentas de personal)</th><td class="c num">3</td><td class="c num">8</td><td class="c num">20</td></tr>
<tr><th>Mensajes de IA / mes</th><td class="c num">⟦quota:starter⟧</td><td class="c num">⟦quota:pro⟧</td><td class="c num">⟦quota:growth⟧</td></tr>
<tr><th>Sincronización con más de 100 OTAs</th><td class="c">Sí</td><td class="c">Sí</td><td class="c">Prioritaria</td></tr>
<tr><th>Mensajería IA por WhatsApp</th><td class="c">Sí</td><td class="c">Sí</td><td class="c">Sí</td></tr>
<tr><th>Sugerencias de Lio cada mañana (nada cambia sin tu aprobación)</th><td class="c">Sí</td><td class="c">Sí</td><td class="c">Sí</td></tr>
<tr><th>Solicitudes de reserva y de servicios extra con Lio por WhatsApp</th><td class="c">No</td><td class="c">Sí</td><td class="c">Sí</td></tr>
<tr><th>Análisis con IA de reseñas y mensajes de huéspedes</th><td class="c">No</td><td class="c">Sí</td><td class="c">Sí</td></tr>
<tr><th>Resumen semanal con IA</th><td class="c">No</td><td class="c">Opcional</td><td class="c">Sí</td></tr>
<tr><th>Bandejas de OTAs (Booking.com, Airbnb, Expedia)</th><td class="c">No</td><td class="c">Sí</td><td class="c">Sí</td></tr>
<tr><th>Planning de habitaciones</th><td class="c">Sí</td><td class="c">Sí</td><td class="c">Sí</td></tr>
<tr><th>Confirmación de alojamiento para visados (PDF)</th><td class="c">Sí</td><td class="c">Sí</td><td class="c">Sí</td></tr>
<tr><th>Check-in online y firma digital</th><td class="c">No</td><td class="c">Sí</td><td class="c">Sí</td></tr>
<tr><th>Venta de traslados y excursiones</th><td class="c">No</td><td class="c">Sí</td><td class="c">Sí</td></tr>
<tr><th>App móvil para iOS y Android</th><td class="c">No</td><td class="c">Sí</td><td class="c">Sí</td></tr>
<tr><th>Soporte prioritario y llamada de onboarding</th><td class="c">No</td><td class="c">No</td><td class="c">Sí</td></tr>
<tr><th>Marca blanca</th><td class="c">No</td><td class="c">No</td><td class="c">Sí</td></tr>
</tbody></table></div></div></section>
'''
    return {"key":"features","title":"Funciones del software de gestión hotelera | Hostlio Pro",
            "desc":"Hostlio Pro incluye asistente IA, channel manager con 100+ OTAs, planning de habitaciones, check-in online, cartas para visado, traslados y app móvil.",
            "trail":[("Funcionalidades", U("features"))],"body":body,"faq":[FAQ_CORE[0], FAQ_CORE[3]]}

def pricing():
    body = f'''
<section class="page-hero"><div class="wrap"><h1>Precios de Hostlio Pro</h1>
<p class="lead">Una cuota mensual fija. Sin comisiones por reserva ni costes de alta. Prueba cualquier plan gratis durante 7 días.</p></div></section>
<section style="padding-top:0"><div class="wrap"><h2 class="sr-only">Planes</h2>
<span class="billing-note">⟦eb_pct⟧ de descuento para los primeros 50 clientes, de por vida</span>
{plans_html()}
<p class="small muted" style="margin-top:18px">Precios en dólares estadounidenses, impuestos no incluidos. Última actualización: <time datetime="{UPDATED}">{D(UPDATED)}</time>.</p>
</div></section>
<section class="white rule"><div class="wrap">
<div class="section-head"><h2>¿Qué plan te conviene?</h2></div>
<div class="rows">
<div class="row"><h3>Starter</h3><div><p>Hostales, pensiones y hoteles boutique de hasta 10 habitaciones que envían menos de ⟦quota:starter⟧ respuestas al mes y quieren empezar con la sincronización de canales y las respuestas con IA.</p></div></div>
<div class="row"><h3>Pro</h3><div><p>Hoteles de 11 a 50 habitaciones que quieren que Lio gestione también los mensajes de las OTAs, usar el check-in online y vender traslados y excursiones.</p></div></div>
<div class="row"><h3>Growth</h3><div><p>Dos alojamientos o hasta 150 habitaciones, cuando necesitas soporte prioritario, un onboarding personalizado y uso en marca blanca.</p></div></div>
</div></div></section>
'''
    faq = [FAQ_CORE[1], FAQ_CORE[2],
      ("¿Cobráis comisión por reserva?", "No. Hostlio Pro es una suscripción mensual fija; no se queda ningún porcentaje del valor de las reservas."),
      ("¿Hay opción de facturación anual?", "Sí. Las suscripciones se facturan por adelantado de forma mensual o anual, y los planes anuales tienen un 20 % de descuento (Términos del servicio, sección 3)."),
      ("¿Puedo cambiar de plan?", "Sí. Sube o baja de plan cuando quieras. El cambio se aplica al momento y la diferencia de precio se prorratea en tu próxima factura."),
      ("¿Cuánto dura el descuento de lanzamiento?", "Se aplica a los primeros 50 clientes, y tu precio se mantiene mientras sigas con la suscripción.")]
    return {"key":"pricing","title":"Precios de software hotelero: desde ⟦price:starter⟧/mes | Hostlio Pro",
            "desc":"Precios de Hostlio Pro: Starter ⟦price:starter⟧, Pro ⟦price:pro⟧ y Growth ⟦price:growth⟧ al mes. Sin comisiones ni costes de alta, con prueba gratuita de 7 días. Compara los planes.",
            "trail":[("Precios", U("pricing"))],"body":body,"faq":faq,"schema":[software_schema(L, detailed=True)]}

FAQ_ALL = FAQ_CORE + [
 ("¿Para qué tipos de hotel es Hostlio Pro?", "Para alojamientos independientes de 1 a 150 habitaciones, como hoteles boutique, hoteles urbanos, hostales y pensiones, apartahoteles y hostels."),
 ("¿Hay una app móvil?", "Sí. Los planes Pro y Growth incluyen una app para iOS y Android. Gestiona reservas, mensajes y check-ins fuera del alojamiento."),
 ("¿Cómo funciona el check-in online?", "Los huéspedes reciben un enlace personal y seguro, escanean su documento con el móvil (no se guarda ninguna imagen) y, antes de llegar, envían sus acompañantes y una firma digital. Disponible en Pro y Growth."),
 ("¿Para qué sirve la confirmación de alojamiento para visados?", "Para los huéspedes que necesitan visado, prepara en un clic una confirmación de alojamiento a partir de los datos de la reserva, para usarla en la solicitud de visado o de invitación. Puedes guardarla en PDF o imprimirla."),
 ("¿Están seguros mis datos?", "Los datos se transmiten mediante conexiones cifradas, y los datos de cada hotel están aislados de los de otros alojamientos con reglas de acceso a nivel de fila. Los datos de los huéspedes pueden eliminarse a petición."),
 ("¿Cuánto tiempo lleva la configuración?", "Tu cuenta está lista en minutos. La mayoría de los hoteles conectan sus canales el mismo día: añade tipos de habitación y habitaciones, autoriza la conexión en la extranet de cada OTA y asigna las habitaciones. El plan Growth incluye una llamada de onboarding personalizada."),
 ("¿En qué idiomas se ofrece el soporte?", "El soporte se ofrece en inglés y turco. El panel, la app móvil y el formulario de check-in del huésped están disponibles en 6 idiomas: español, inglés, turco, francés, italiano y portugués. Escríbenos a " + EMAIL + "."),
]

def faq_page():
    body = f'''<section class="page-hero"><div class="wrap"><h1>Preguntas frecuentes</h1>
<p class="lead">Las preguntas más habituales sobre las funcionalidades, los precios y la configuración de Hostlio Pro. ¿No encuentras tu respuesta? <a href="{U("contact")}">Escríbenos</a>.</p></div></section>
<section style="padding-top:0"><div class="wrap">{faq_block(FAQ_ALL, L, heading=False, wrap=False)}</div></section>'''
    return {"key":"faq","title":"Preguntas frecuentes sobre Hostlio Pro | Hostlio Pro",
            "desc":"Preguntas frecuentes sobre Hostlio Pro, software de gestión hotelera: precios, prueba gratis, OTAs, asistente IA Lio, check-in online y seguridad.",
            "trail":[("Preguntas frecuentes", U("faq"))],"body":body,"faq":FAQ_ALL,"faq_inline":True,"page_type":"FAQPage"}

def about():
    body = f'''<section class="page-hero"><div class="wrap split"><div><h1>Por qué creamos Hostlio Pro</h1>
<p class="lead">En los hoteles pequeños, la recepción, las ventas y la comunicación con los huéspedes suelen recaer en una sola persona. Hostlio Pro existe para que esa persona no se ahogue en mensajes por la noche ni en pantallas de canales durante el día.</p></div><div class="hero-img"><img src="/assets/img/gen-shutters.webp" alt="" width="1080" height="1350"></div></div></section>
<section class="white rule"><div class="wrap split">
<div class="prose"><h2>Qué hacemos</h2>
<p>Hostlio Pro es un software de gestión hotelera con IA para hoteles independientes. Dejamos la comunicación con los huéspedes en manos de nuestro asistente de IA Lio, reunimos la distribución en OTAs en un solo calendario mediante conexiones certificadas y llevamos el check-in al móvil del huésped.</p>
<h2>Cómo trabajamos</h2>
<ul><li>Publicamos nuestros precios abiertamente y no cobramos comisiones.</li><li>Construimos a partir del trabajo diario real de los hoteleros.</li><li>Sin contratos largos: los clientes se quedan porque están contentos.</li></ul></div>
<div class="panel"><p class="panel-title">Datos de la empresa</p><dl class="list-kv">
<dt>Producto</dt><dd>Hostlio Pro (Hostlio)</dd><dt>Empresa</dt><dd>Loti Members LLC</dd>
<dt>Dirección</dt><dd>2108 N ST STE N, Sacramento, CA 95816, USA</dd><dt>Email</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd>
<dt>Clientes</dt><dd>Hoteles independientes en más de 20 países</dd></dl></div>
</div></section>'''
    return {"key":"about","title":"Sobre nosotros | Hostlio Pro","desc":"Hostlio Pro desarrolla software de gestión hotelera con IA para hoteles independientes. Operado por Loti Members LLC y utilizado en más de 20 países.",
            "trail":[("Sobre nosotros", U("about"))],"body":body,"page_type":"AboutPage"}

def contact():
    from build import FORM_ENDPOINT
    act = f' action="{FORM_ENDPOINT}" method="post"' if FORM_ENDPOINT else ""
    body = f'''<section class="page-hero"><div class="wrap split" style="align-items:start">
<div><h1>Solicita una demo o contacta con nosotros</h1>
<p class="lead">Cuéntanos brevemente sobre tu hotel y los canales que usas, y te mostraremos Hostlio Pro con tus propias habitaciones en una llamada de 30 minutos.</p>
<p>Escríbenos directamente: <a href="mailto:{EMAIL}">{EMAIL}</a></p></div>
<form class="contact" data-contact-form data-mail="{EMAIL}" data-subject="Solicitud de demo" data-sent="Se ha abierto tu aplicación de correo. Pulsa enviar y tu solicitud nos llegará."{act}>
<label>Nombre completo<input name="name" autocomplete="name" required></label>
<label>Email<input type="email" name="email" autocomplete="email" required></label>
<label>Nombre del hotel<input name="hotel" autocomplete="organization" required></label>
<label>Número de habitaciones<select name="rooms"><option>1–10</option><option>11–50</option><option>51–150</option><option>150+</option></select></label>
<label>País / ciudad<input name="country" autocomplete="country-name"></label>
<label>Mensaje <span class="hint">Canales que usas, software actual</span><textarea name="message" rows="4"></textarea></label>
<button class="btn btn-primary" type="submit">Enviar solicitud de demo</button>
<p class="form-status" role="status" aria-live="polite"></p>
</form></div></section>'''
    return {"key":"contact","title":"Contacto y solicitud de demo | Hostlio Pro","desc":"Contacta con el equipo de Hostlio Pro o pide una demo gratuita de 30 minutos adaptada a tu hotel. Soporte en inglés y turco, email: " + EMAIL,
            "trail":[("Contacto", U("contact"))],"body":body,"page_type":"ContactPage","no_final":True}

POSTS = [
 {"key":"post-overbooking","title":"Cómo evitar el overbooking: 6 pasos para hoteles","date":"2026-09-21","desc":"Por qué se producen las sobreventas en los hoteles y cómo evitarlas: channel manager, reglas de cierre de venta, márgenes de disponibilidad y qué hacer si aun así ocurre."},
 {"key":"post-autoreply","title":"Cómo responder automáticamente a los mensajes de Booking.com","date":"2026-09-21","desc":"Tres formas de automatizar los mensajes de huéspedes de Booking.com: plantillas, mensajes programados y un asistente de IA."},
 {"key":"post-ai","title":"Responder a los huéspedes del hotel con IA: guía práctica","date":"2026-09-18",
  "desc":"Ventajas, riesgos y pasos de configuración para responder con IA a los mensajes de los huéspedes. Qué preguntas automatizar y cuáles dejar a tu equipo."},
 {"key":"post-pms","title":"Software para hoteles pequeños: cómo elegirlo y precios 2026","date":"2026-09-10",
  "desc":"Cómo elegir software de gestión hotelera para un hotel pequeño: cuánto cuesta, qué calcular para 8, 20 y 45 habitaciones y SES.Hospedajes. Desde ⟦price:starter⟧/mes."},
]

def blog():
    items = "".join(f'<article><h2><a href="{U(p["key"])}">{p["title"]}</a></h2><p class="meta"><time datetime="{p["date"]}">{D(p["date"])}</time></p><p>{p["desc"]}</p></article>' for p in [dict(p, **{k: v for k, v in __import__("pages_v4").post_meta(L).get(p["key"], {}).items() if k in ("title", "desc")}) for p in POSTS])
    body = f'<section class="page-hero"><div class="wrap"><h1>Blog para hoteleros</h1><p class="lead">Artículos prácticos sobre la gestión de un hotel independiente, la distribución y la comunicación con los huéspedes.</p></div></section><section style="padding-top:0"><div class="wrap post-list">{items}</div></section>'
    return {"key":"blog","title":"Blog: guías para hoteles independientes | Hostlio Pro","desc":"Guías prácticas para hoteleros independientes sobre gestión hotelera, channel manager, distribución en OTAs y comunicación con huéspedes mediante IA.",
            "trail":[("Blog", U("blog"))],"body":body,"page_type":"CollectionPage"}

COVERS={"post-ai":("gen-checkin-phone",1080,1350),"post-pms":("gen-owner-laptop",1080,1350),"post-overbooking":("gen-reception",1080,1350),"post-autoreply":("gen-night-desk",1080,1350)}
def article(meta, content, faq=None):
    art = {"@type":"BlogPosting","headline":meta["title"],"description":meta["desc"],"datePublished":meta["date"],"inLanguage":L,"author":{"@type":"Organization","name":"Equipo de producto de Hostlio Pro","url":SITE+U("about")},"dateModified":UPDATED,"publisher":{"@id":SITE+"/#org"},
           "mainEntityOfPage":SITE+U(meta["key"]),"image":SITE+"/assets/img/"+COVERS[meta["key"]][0]+".webp"}
    body = f'<article><section class="page-hero"><div class="wrap"><h1 style="max-width:22ch">{meta["title"]}</h1><p class="meta">Por el <a href="{U("about")}">equipo de producto de Hostlio Pro</a>, las personas que desarrollan Hostlio Pro. Publicado el <time datetime="{meta["date"]}">{D(meta["date"])}</time>, actualizado el <time datetime="{UPDATED}">{D(UPDATED)}</time></p></div></section><section style="padding-top:0"><div class="wrap"><figure class="post-cover"><img src="/assets/img/{COVERS[meta["key"]][0]}.webp" alt="" width="{COVERS[meta["key"]][1]}" height="{COVERS[meta["key"]][2]}"></figure><div class="prose">{content}</div></div></section></article>'
    return {"key":meta["key"],"title":meta["title"],"desc":meta["desc"],"og_type":"article",
            "trail":[("Blog",U("blog")),(meta["title"],U(meta["key"]))],"body":body,"schema":[art],"faq":faq or []}

def post_ai():
    c = f'''
<div class="answer"><p><strong>Respuesta corta:</strong> La mayoría de los mensajes que recibe un hotel son preguntas repetidas (hora de check-in, aparcamiento, traslados, desayuno). Si se las encargas a un asistente de IA entrenado con la información de tu propio hotel, los huéspedes reciben respuesta en segundos y en su idioma. Los descuentos, las quejas y las solicitudes especiales deben quedarse en manos de tu equipo.</p></div>
<h2>¿Qué preguntas reciben más los hoteles?</h2>
<p>En los hoteles independientes, la mayoría de los mensajes giran en torno a unos pocos temas:</p>
<ul><li>Horarios de check-in y check-out, llegada anticipada o salida tardía</li><li>Traslados al aeropuerto y cómo llegar</li><li>Aparcamiento, desayuno, política de mascotas</li><li>Consigna de equipaje, características de la habitación, el barrio</li><li>Cambios en la reserva y solicitudes de factura</li></ul>
<p>Las respuestas ya existen en el hotel. El problema es darlas en el idioma adecuado y a la hora adecuada.</p>
<h2>¿Qué debe automatizar la IA y qué no?</h2>
<p>En una buena configuración, el asistente resuelve las preguntas informativas y deja las decisiones al personal.</p>
<div class="table-wrap"><table><thead><tr><th>Que responda la IA</th><th>Que lo gestione el personal</th></tr></thead><tbody>
<tr><td>Horarios, normas, servicios</td><td>Descuentos y negociación de precios</td></tr><tr><td>Cómo llegar, información de traslados</td><td>Quejas y compensaciones</td></tr><tr><td>Venta de traslados y excursiones</td><td>Situaciones médicas o de seguridad</td></tr><tr><td>Recordar a los huéspedes los datos de su reserva</td><td>Solicitudes de grupos y eventos</td></tr></tbody></table></div>
<h2>Configuración paso a paso</h2>
<ol><li><strong>Redacta la base de conocimiento de tu hotel.</strong> Horarios, normas, servicios y preguntas frecuentes. Cuanto más clara sea, más coherentes serán las respuestas.</li>
<li><strong>Conecta tus canales.</strong> Reúne los mensajes de WhatsApp y de las OTAs en una sola bandeja de entrada.</li>
<li><strong>Empieza en modo de aprobación.</strong> Durante la primera semana, lee y corrige las respuestas antes de que se envíen.</li>
<li><strong>Define las reglas de traspaso.</strong> Decide qué temas te llegan a ti.</li>
<li><strong>Pasa al modo automático.</strong> Cuando las respuestas sean coherentes, deja que el asistente gestione por completo las preguntas informativas.</li></ol>
<h2>Por qué importan las respuestas en varios idiomas</h2>
<p>Los huéspedes que escriben en su propio idioma dan más detalles y confían más en la respuesta. Un asistente que responde en más de 30 idiomas genera esa confianza aunque nadie en recepción hable el idioma, y tú sigues leyendo la conversación en el tuyo.</p>
<h2>Cómo funciona en Hostlio Pro</h2>
<p>El asistente de IA de Hostlio Pro, <a href="{U("ai")}">Lio</a>, usa la información de tu hotel y los datos de las reservas para responder a mensajes de WhatsApp y de las OTAs (Booking.com, Airbnb, Expedia) en más de 30 idiomas. Los planes incluyen entre ⟦quota:starter⟧ y ⟦quota:growth⟧ mensajes de IA al mes; consulta la <a href="{U("pricing")}">página de precios</a> para más detalles.</p>'''
    faq = [("¿Puede la IA dar información incorrecta a los huéspedes?", "El riesgo es mínimo cuando el asistente solo trabaja con la información que proporciona el hotel y pasa al personal las preguntas dudosas. Se recomienda empezar en modo de aprobación."),
           ("¿Sabrán los huéspedes que hablan con una IA?", "Las respuestas se redactan en nombre del hotel y con su tono. Por transparencia, el hotel puede indicar en el mensaje de bienvenida que el asistente es una IA.")]
    return article(next(p for p in POSTS if p["key"]=="post-ai"), c, faq)

def post_pms():
    c = f'''
<div class="answer"><p><strong>Respuesta corta:</strong> El PMS adecuado para un hotel pequeño tiene channel manager integrado, precios fijos y transparentes, una sola bandeja para los mensajes de los huéspedes, acceso móvil y se configura en el mismo día. Los sistemas empresariales con cientos de funciones suelen quedarse sin usar en los equipos pequeños.</p></div>
<h2>1. Un channel manager integrado</h2>
<p>Si vendes en Booking.com, Airbnb y Expedia a la vez, la disponibilidad tiene que sincronizarse al instante. Un channel manager aparte supone un coste extra y otra pantalla más. Lo primero que debes comprobar es si el PMS lo incluye y con cuántos canales se conecta.</p>
<h2>2. Modelo de precios</h2>
<p>Algunos programas para hoteles cobran un porcentaje del valor de la reserva además de la cuota mensual, así que los costes suben con la ocupación. Un precio mensual fijo mantiene tu presupuesto previsible. Con los proveedores que no publican sus precios, prepárate para un proceso comercial.</p>
<h2>3. Comunicación con los huéspedes</h2>
<p>Cuando los mensajes están repartidos entre WhatsApp y las bandejas de Booking.com, Airbnb y Expedia, los tiempos de respuesta se resienten. Una sola bandeja de entrada con respuestas automáticas es lo que más tiempo ahorra a los equipos pequeños.</p>
<h2>4. Un planning de habitaciones fácil de usar</h2>
<p>El calendario de reservas es la pantalla que más mira tu recepción. Mover habitaciones arrastrando y soltando y ver de un vistazo el canal de cada reserva agiliza el trabajo diario.</p>
<h2>5. Acceso móvil</h2>
<p>Los propietarios suelen estar fuera del alojamiento. Poder revisar llegadas, disponibilidad y mensajes desde el teléfono, con una app móvil o al menos con un panel que funcione bien en el smartphone, es una necesidad real.</p>
<h2>6. Check-in online</h2>
<p>Recoger los datos de los huéspedes antes de su llegada ahorra tiempo en recepción y simplifica los requisitos de registro de viajeros. Conviene comprobar cómo se leen los documentos (a mano o mediante la zona MRZ), si se guardan imágenes del DNI o del pasaporte y si incluye firma digital.</p>
<h2>7. Configuración y soporte</h2>
<p>Un hotel pequeño no puede asumir un proyecto de implantación de varias semanas. Elige un software que puedas usar el mismo día, con soporte en tu idioma, y pon a prueba el periodo gratuito con reservas reales.</p>
<h2>¿Cuánto cuesta un software de gestión hotelera?</h2>
<p>La cuota mensual que aparece en la web es solo una parte del precio. Para comparar dos programas hay que calcular el coste anual completo, porque cada proveedor combina conceptos distintos:</p>
<ul><li><strong>Cuota fija mensual o anual:</strong> pagas lo mismo independientemente de las reservas. Es el modelo más fácil de presupuestar.</li>
<li><strong>Precio por habitación:</strong> la cuota crece con el número de habitaciones. Si vas a ampliar el hotel, calcula también ese escenario.</li>
<li><strong>Comisión sobre reservas:</strong> un porcentaje del importe de las reservas gestionadas. El coste sube justo en los mejores meses. Por ejemplo, un 1&nbsp;% sobre 100.000&nbsp;€ de reservas al año son 1.000&nbsp;€ anuales que se suman a la cuota.</li>
<li><strong>Costes de alta:</strong> puesta en marcha, formación o migración de datos cobradas una sola vez.</li>
<li><strong>Coste por canal:</strong> algunos channel managers cobran por cada OTA conectada o incluyen solo un número limitado de canales.</li>
<li><strong>Módulos aparte:</strong> channel manager, check-in online, mensajería o app móvil vendidos por separado. Un precio base bajo puede encarecerse mucho al añadir lo imprescindible.</li></ul>
<h3>Ejemplo: qué calcular para 8, 20 y 45 habitaciones</h3>
<p>La tabla no recoge precios de otros proveedores, que cambian a menudo y muchas veces no son públicos, sino los conceptos que conviene pedir para obtener presupuestos comparables. Si quieres ver los datos publicados por los principales proveedores, con sus fuentes, consulta nuestra <a href="{U("compare")}">comparativa de software hotelero</a>.</p>
<div class="table-wrap"><table><thead><tr><th>Alojamiento</th><th>Qué calcular con cada proveedor</th><th>Plan de Hostlio Pro adecuado</th></tr></thead><tbody>
<tr><td>Hostal o hotel pequeño de 8 habitaciones</td><td>Cuota anual + posible comisión sobre reservas + channel manager si se paga aparte</td><td>Starter: ⟦price:starter⟧/mes, o ⟦annual_mo:starter⟧/mes con pago anual</td></tr>
<tr><td>Hotel de 20 habitaciones</td><td>Cuota anual (¿cambia por habitación?) + módulos de check-in online y bandejas de OTAs + usuarios adicionales</td><td>Pro: ⟦price:pro⟧/mes, o ⟦annual_mo:pro⟧/mes con pago anual</td></tr>
<tr><td>Hotel de 45 habitaciones</td><td>Cuota anual + coste por canal + usuarios incluidos + costes de alta y migración</td><td>Pro (hasta ⟦rooms:pro⟧ habitaciones), o Growth si gestionas un segundo alojamiento</td></tr></tbody></table></div>
<p>Para estimar cuánto tiempo y cuántas comisiones puede ahorrarte un PMS, prueba la <a href="{U("roi")}">calculadora de ROI</a> con los datos de tu hotel.</p>
<h3>Precios de Hostlio Pro</h3>
<p>Hostlio Pro publica sus precios y cobra una cuota fija, sin comisiones sobre las reservas. El channel manager está incluido en todos los planes. Precios en dólares estadounidenses:</p>
<div class="table-wrap"><table><thead><tr><th>Plan</th><th>Mensual</th><th>Anual (por mes)</th><th>Límite</th></tr></thead><tbody>
<tr><td>Starter</td><td>⟦price:starter⟧</td><td>⟦annual_mo:starter⟧ (⟦annual:starter⟧/año)</td><td>1 alojamiento, hasta ⟦rooms:starter⟧ habitaciones, 3 usuarios</td></tr>
<tr><td>Pro</td><td>⟦price:pro⟧</td><td>⟦annual_mo:pro⟧ (⟦annual:pro⟧/año)</td><td>1 alojamiento, hasta ⟦rooms:pro⟧ habitaciones, 8 usuarios</td></tr>
<tr><td>Growth</td><td>⟦price:growth⟧</td><td>⟦annual_mo:growth⟧ (⟦annual:growth⟧/año)</td><td>Hasta 2 alojamientos, ⟦rooms:growth⟧ habitaciones en total, 20 usuarios</td></tr></tbody></table></div>
<p>Todos los planes empiezan con una prueba gratuita de ⟦trial⟧ días: la tarjeta se registra al darte de alta, pero no se cobra nada hasta que termina la prueba. Tienes todos los detalles en la <a href="{U("pricing")}">página de precios</a>.</p>
<h2>Qué plan según el tamaño del hotel</h2>
<ul><li><strong>Hasta ⟦rooms:starter⟧ habitaciones</strong> (hostales, pensiones, casas rurales, hoteles boutique pequeños): Starter incluye el planning de habitaciones, el <a href="{U("channel")}">channel manager</a> y respuestas con IA por WhatsApp.</li>
<li><strong>De 11 a ⟦rooms:pro⟧ habitaciones:</strong> Pro añade las bandejas de las OTAs (Booking.com, Airbnb, Expedia) en la misma bandeja de entrada, el <a href="{U("checkin")}">check-in online</a> con firma digital y más usuarios para el equipo.</li>
<li><strong>Dos alojamientos</strong>, hasta ⟦rooms:growth⟧ habitaciones en total: Growth permite gestionarlos desde la misma cuenta, con 20 usuarios.</li></ul>
<h2>Registro de viajeros y SES.Hospedajes: qué preguntar</h2>
<p>En España, los establecimientos de alojamiento están obligados a registrar los datos de los viajeros (el antiguo parte de viajeros) y comunicarlos al Ministerio del Interior a través de SES.Hospedajes, además de las obligaciones que pueda fijar cada comunidad autónoma. Un software de gestión hotelera puede ahorrarte mucho trabajo aquí, pero el nivel de integración varía: algunos envían los datos directamente, otros solo generan un fichero para subirlo y otros no ofrecen nada.</p>
<p>Antes de decidir, pregunta expresamente si el PMS envía los partes directamente a SES.Hospedajes o si solo exporta los datos. Hostlio Pro recoge y organiza los datos de los huéspedes con el check-in online, pero no los envía a SES.Hospedajes: la comunicación se hace a través del canal oficial.</p>
<h2>Cómo aprovechar la prueba gratuita: lista para la migración</h2>
<ol><li><strong>Importa las reservas futuras</strong> desde tu sistema actual, por ejemplo con un archivo CSV o Excel, y comprueba que fechas, habitaciones e importes coinciden.</li>
<li><strong>Mapea habitaciones y tarifas en las OTAs</strong> con cuidado: cada tipo de habitación del PMS debe corresponder al correcto en Booking.com, Airbnb y Expedia.</li>
<li><strong>Haz una reserva de prueba</strong> en un canal y comprueba que la disponibilidad se cierra en los demás. Es la forma más sencilla de <a href="{U("post-overbooking")}">evitar el overbooking</a> tras el cambio.</li>
<li><strong>Conecta WhatsApp</strong> y carga la información del hotel; deja que <a href="{U("ai")}">Lio</a> proponga respuestas y revísalas durante unos días.</li>
<li><strong>Crea los usuarios del equipo</strong> con los permisos adecuados y deja que recepción trabaje con el planning al menos un turno completo.</li>
<li><strong>Revisa la exportación de datos</strong>: comprueba que puedes llevarte tu información en un formato legible si algún día cambias de proveedor.</li>
<li><strong>Decide antes de que acabe la prueba</strong>, para poder cancelar sin cargos si el software no encaja.</li></ol>
<h2>Lista de comprobación</h2>
<div class="table-wrap"><table><thead><tr><th>Criterio</th><th>Pregunta que hacer</th></tr></thead><tbody>
<tr><td>Channel manager</td><td>¿Está incluido y con cuántos canales se conecta?</td></tr><tr><td>Precios</td><td>¿Es una tarifa fija, hay comisión, el precio es público?</td></tr>
<tr><td>Coste total</td><td>¿Hay costes de alta, por canal, por habitación o módulos aparte?</td></tr>
<tr><td>Mensajería</td><td>¿Están los mensajes de WhatsApp y de las OTAs en un solo lugar, con respuestas automáticas?</td></tr><tr><td>Móvil</td><td>¿Hay app móvil o un panel que se pueda usar desde el smartphone?</td></tr>
<tr><td>Check-in</td><td>¿Hay check-in online con firma digital?</td></tr><tr><td>SES.Hospedajes</td><td>¿El PMS envía los partes directamente o solo exporta los datos?</td></tr>
<tr><td>Datos</td><td>¿Se pueden importar y exportar las reservas?</td></tr><tr><td>Prueba</td><td>¿Hay prueba gratuita y cancelación sin permanencia?</td></tr></tbody></table></div>
<p>Hostlio Pro se ha creado en torno a estos criterios: consulta las <a href="{U("features")}">funcionalidades</a> y los <a href="{U("pricing")}">precios</a>.</p>'''
    faq = [("¿Necesita un hotel pequeño un PMS?", "Si vendes en varias OTAs y recibes decenas de mensajes al día, sí. Trabajar con hojas de cálculo y extranets de OTAs por separado aumenta el riesgo de overbooking y de respuestas lentas."),
           ("¿Qué diferencia hay entre un PMS y un channel manager?", "Un PMS gestiona las operaciones internas del hotel (reservas, habitaciones, huéspedes); un channel manager distribuye la disponibilidad y las tarifas a las OTAs. Un software como Hostlio Pro combina ambos en una sola plataforma."),
           ("¿Cuánto cuesta un software de gestión hotelera para un hotel pequeño en España?", "Depende del modelo de precios: cuota fija, precio por habitación o comisión sobre reservas, más posibles módulos y costes de alta. Con Hostlio Pro, un hotel de hasta ⟦rooms:starter⟧ habitaciones encaja en el plan Starter, por ⟦price:starter⟧ al mes o ⟦annual_mo:starter⟧ al mes con pago anual, con channel manager incluido y sin comisiones."),
           ("¿Compensa un software que cobra comisión por reserva?", "Puede compensar con muy pocas reservas, pero el coste crece con la ocupación. Para compararlo con una cuota fija, multiplica el porcentaje por el importe anual de las reservas que pasan por el sistema."),
           ("¿Hostlio Pro envía los partes de viajeros a SES.Hospedajes?", "No. El check-in online de Hostlio Pro recoge y organiza los datos de los huéspedes antes de la llegada, pero la comunicación al Ministerio del Interior se realiza a través de SES.Hospedajes.")]
    return article(next(p for p in POSTS if p["key"]=="post-pms"), c, faq)

def pages():
    import pages_v4
    return [home(), ai(), channel(), checkin(), features(), pricing(), faq_page(), about(), contact(), blog(), post_ai(), post_pms()] + pages_v4.pages(L, article) + __import__("legal_v5").pages(L, article)
