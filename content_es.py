from build import btn, icon, logo, url, room_rack, channel_strip, faq_block, SIGNUP_URL, EMAIL, UPDATED, CHECK, software_schema, SITE, PLANS
L = "es"
def U(k): return url(k, L)

MESES = ["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]
def D(iso):
    y, m, d = iso[:10].split("-")
    return f"{int(d)} de {MESES[int(m)-1]} de {y}"

PLAN_TXT = {
 "starter": ("Para hostales, pensiones y hoteles boutique pequeños", ["1 alojamiento, hasta 10 habitaciones","1.000 mensajes de IA / mes","Sincronización de reservas de OTAs (más de 100 canales)","Mensajería IA por WhatsApp","Calendario de reservas (planning de habitaciones)","Formularios de visado en PDF automáticos"]),
 "pro":     ("Para hoteles en crecimiento con un solo alojamiento", ["1 alojamiento, hasta 50 habitaciones","5.000 mensajes de IA / mes","Todo lo de Starter","Mensajería por WhatsApp y bandejas de las OTAs (Booking.com, Airbnb, Expedia)","Check-in online con firma digital","Venta de traslados y excursiones","App móvil para iOS"]),
 "growth":  ("Para equipos que gestionan dos alojamientos", ["Hasta 2 alojamientos, 150 habitaciones","12.000 mensajes de IA / mes","Todo lo de Pro","Sincronización de canales prioritaria","Soporte prioritario (siguiente día hábil)","Llamada de onboarding personalizada","Opciones de marca blanca"]),
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
<div class="price num"><b>${p["price"]}</b><span class="muted">/ mes</span></div>
<p class="small muted num" style="margin:0">Precio de lanzamiento (normalmente <s>${p["regular"]}</s>)</p>
<ul>{lis}</ul>
{btn("Empieza con "+p["name"], SIGNUP_URL+"?plan="+p["id"], "primary" if pop else "ghost")}
</article>''')
    return '<div class="plans">' + "".join(out) + "</div>"

FAQ_CORE = [
 ("¿Qué es Hostlio Pro?", "Hostlio Pro es un software de gestión hotelera (PMS hotelero) con inteligencia artificial, creado para hoteles independientes, hoteles boutique y hostales. Reúne en una sola plataforma a Lio, un asistente de IA que responde a los huéspedes 24/7 en más de 30 idiomas, un channel manager conectado a más de 100 OTAs, un calendario de reservas con arrastrar y soltar y el check-in online."),
 ("¿Cuánto cuesta Hostlio Pro?", "Hay tres planes: Starter a 49 $/mes, Pro a 89 $/mes y Growth a 149 $/mes. Estos precios incluyen un descuento de lanzamiento del 20 % para los primeros 50 clientes, que se mantiene mientras sigas suscrito. Los precios normales son 59 $, 109 $ y 189 $."),
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
<p class="small muted" style="margin:10px 0 0">Traslado reservado, enlace de pago enviado.</p></div>
</div></section>

<section class="white rule"><div class="wrap">
<div class="answer"><p><strong>¿Qué es un asistente de IA para mensajes de huéspedes de hotel?</strong> Un software que responde automáticamente a las preguntas que hacen los huéspedes antes y después de reservar, usando la información del propio hotel. Lio pasa a tu equipo los mensajes que no sabe responder o que requieren una decisión humana (peticiones de descuento, quejas, solicitudes especiales).</p></div>
<h2 style="margin-top:64px">Qué hace Lio</h2><div class="rows">
<div class="row"><h3>Una sola bandeja de entrada</h3><div><p>Los mensajes de WhatsApp y de las bandejas de Booking.com, Airbnb y Expedia llegan a una sola pantalla. Lio asocia automáticamente a cada huésped con su reserva.</p></div></div>
<div class="row"><h3>Más de 30 idiomas, con traducción automática</h3><div><p>El huésped escribe en japonés, Lio responde en japonés y tú lees la conversación en tu idioma. Las respuestas manuales también se traducen al idioma del huésped.</p></div></div>
<div class="row"><h3>Conoce tu hotel</h3><div><p>Horarios de check-in y check-out, aparcamiento, política de mascotas, horario del desayuno, transporte y características de las habitaciones. Los introduces una vez y Lio los usa de forma coherente en cada respuesta.</p></div></div>
<div class="row"><h3>Un asistente que vende</h3><div><p>Lio no solo responde preguntas: ofrece traslados al aeropuerto, visitas por la ciudad y extras en el momento adecuado, y crea la reserva.</p></div></div>
<div class="row"><h3>Tú mantienes el control</h3><div><p>Durante los primeros días puedes aprobar las respuestas de Lio antes de que se envíen. Tú decides qué temas cierra Lio por su cuenta y cuáles te pasa a ti.</p></div></div>
</div></div></section>

<section><div class="wrap">
<div class="section-head"><h2>Cuota de mensajes de IA por plan</h2><p>Un mensaje es una sola respuesta que Lio envía a un huésped.</p></div>
<div class="table-wrap"><table><thead><tr><th>Plan</th><th class="c">Mensajes de IA / mes</th><th>Canales de mensajería</th></tr></thead><tbody>
<tr><th>Starter</th><td class="c num">1.000</td><td>WhatsApp</td></tr>
<tr><th>Pro</th><td class="c num">5.000</td><td>WhatsApp + bandejas de OTAs (Booking.com, Airbnb, Expedia)</td></tr>
<tr><th>Growth</th><td class="c num">12.000</td><td>WhatsApp + bandejas de OTAs (Booking.com, Airbnb, Expedia)</td></tr>
</tbody></table></div>
</div></section>
'''
    faq = [
     ("¿Y si Lio da información incorrecta?", "Lio solo usa la información del hotel y los datos de reserva que tú le proporcionas. Cuando no está seguro, te pasa el mensaje en lugar de adivinar. También puedes aprobar cada respuesta antes de que se envíe."),
     ("¿Responde también a los mensajes de Booking.com y Airbnb?", "Sí. En los planes Pro y Growth, los mensajes de las OTAs llegan a la bandeja de Lio y se responden de la misma manera."),
     ("¿Qué pasa cuando se agota la cuota de mensajes?", "Los mensajes siguen llegando y aparecen en tu panel; solo se pausan las respuestas automáticas. Puedes pasarte a un plan superior para ampliar tu cuota."),
     FAQ_CORE[4],
    ]
    return {"key":"ai","title":"Mensajería con IA para hoteles en 30+ idiomas | Hostlio Pro",
            "desc":"Lio, el asistente de IA de Hostlio Pro, responde a los huéspedes de tu hotel por WhatsApp y en Booking.com, Airbnb y Expedia 24/7 en más de 30 idiomas y vende traslados y excursiones.",
            "trail":[("Asistente IA Lio", U("ai"))],"body":body,"faq":faq}

def channel():
    body = f'''
<section class="page-hero"><div class="wrap split">
<div><h1>Un channel manager para más de 100 OTAs</h1>
<p class="lead">Gestiona la disponibilidad, las tarifas y las reservas de Booking.com, Airbnb, Expedia, Agoda y más de 100 canales desde un solo calendario. Hostlio Pro sincroniza en tiempo real y en ambos sentidos a través de Channex.</p>
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
<section><div class="wrap"><div class="section-head"><h2>Principales canales compatibles</h2><p>La lista sigue la red de conexiones de Channex. ¿Echas en falta algún canal? Escríbenos.</p></div>
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
            "desc":"El channel manager de Hostlio Pro sincroniza en tiempo real disponibilidad y tarifas en más de 100 OTAs como Booking.com, Airbnb, Expedia y Agoda, y evita el overbooking.",
            "trail":[("Channel manager", U("channel"))],"body":body,"faq":faq}

def checkin():
    body = f'''
<section class="page-hero"><div class="wrap split">
<div><h1>Check&#8209;in online con firma digital</h1>
<p class="lead">Antes de llegar, los huéspedes envían desde el móvil los datos de su documento de identidad, los acompañantes y su firma. Entregar la llave lleva solo unos minutos.</p>
<div class="cta-row">{btn("Prueba Pro gratis durante 7 días", SIGNUP_URL+"?plan=pro")}</div></div>
<div class="panel"><p class="panel-title">Check-in online, habitación 202</p>
<div class="field"><span>Nombre completo</span><div>Keiko Sato</div></div>
<div class="field"><span>Nacionalidad</span><div>Japón</div></div>
<div class="field"><span>Acompañantes</span><div>1 huésped añadido</div></div>
<div class="field"><span>Firma</span><div class="sig">Firma digital recibida</div></div>
</div>
</div></section>
<section class="white rule"><div class="wrap">
<div class="answer"><p><strong>¿Cómo funciona el check-in online?</strong> Hostlio Pro envía a quien hizo la reserva un enlace personal, seguro y con caducidad. Desde ese enlace, el huésped introduce los datos de su documento, añade una foto del documento y a sus acompañantes, y firma el formulario digitalmente. Todo se guarda directamente en la reserva.</p></div>
<h2 style="margin-top:64px">Funcionalidades del check-in online</h2><div class="rows">
<div class="row"><h3>Enlace seguro</h3><div><p>Un enlace basado en token, único para cada reserva. Solo abre el formulario de esa reserva.</p></div></div>
<div class="row"><h3>Acompañantes</h3><div><p>Todas las personas que se alojan en la habitación se añaden en un solo formulario, así nadie tiene que escribir datos en recepción.</p></div></div>
<div class="row"><h3>Firma digital y consentimiento</h3><div><p>Los huéspedes aceptan las normas de la casa y el consentimiento de datos firmando en pantalla. El registro firmado se guarda con la reserva.</p></div></div>
<div class="row"><h3>Privacidad desde el diseño</h3><div><p>Los datos de los huéspedes pueden eliminarse a petición, y el texto de consentimiento forma parte del formulario.</p></div></div>
<div class="row"><h3>Exportación para comunicaciones oficiales</h3><div><p>Los datos recogidos de los huéspedes pueden exportarse en un formato útil para cumplir los requisitos locales de registro de viajeros.</p></div></div>
</div></div></section>
<section class="dark on-dark"><div class="wrap"><div class="section-head"><h2>Tres pasos para el huésped</h2></div>
<ol class="steps"><li><h3>Abrir el enlace</h3><p>Toca el enlace personal que recibes una vez confirmada la reserva.</p></li>
<li><h3>Completar los datos</h3><p>Añade los datos y una foto del documento, e indica los acompañantes.</p></li>
<li><h3>Firmar</h3><p>Acepta las normas de la casa y firma en pantalla. En recepción, solo queda recoger la llave.</p></li></ol>
</div></section>
'''
    faq = [("¿Qué planes incluyen el check-in online?", "El check-in online con firma digital está incluido en los planes Pro y Growth."),
           ("¿El huésped tiene que descargar una app?", "No. El formulario de check-in se abre en el navegador; no hace falta descargar ninguna app."),
           ("¿Y si un huésped no completa el enlace?", "Haz el check-in de la forma habitual. El personal también puede introducir los datos en recepción con la app móvil de Hostlio Pro.")]
    return {"key":"checkin","title":"Check-in online para hoteles con firma digital | Hostlio Pro",
            "desc":"Con el check-in online de Hostlio Pro, los huéspedes envían desde el móvil sus datos, los acompañantes y una firma digital antes de llegar. Sin colas en recepción.",
            "trail":[("Check-in online", U("checkin"))],"body":body,"faq":faq}

def features():
    body = f'''
<section class="page-hero"><div class="wrap split"><div><h1>Todo lo que incluye Hostlio Pro</h1>
<p class="lead">Los módulos que un hotel independiente necesita en el día a día: comunicación con huéspedes, distribución, reservas, check-in e ingresos adicionales.</p></div><div class="hero-img"><img src="/assets/img/gen-team-desk.webp" alt="" width="1080" height="1350"></div></div></section>
<section class="white rule"><div class="wrap"><h2 class="sr-only">Módulos</h2><div class="rows">
<div class="row"><h3>Asistente IA Lio</h3><div><p>Respuestas a huéspedes 24/7 en más de 30 idiomas. Mensajes de WhatsApp y de las OTAs (Booking.com, Airbnb, Expedia) en una sola bandeja.</p><a href="{U("ai")}">Más sobre Lio</a></div></div>
<div class="row"><h3>Channel manager</h3><div><p>Sincronización de disponibilidad, tarifas y reservas con más de 100 OTAs a través de Channex.</p><a href="{U("channel")}">Channel manager</a></div></div>
<div class="row"><h3>Planning de habitaciones</h3><div><p>Calendario de reservas con arrastrar y soltar. Cambios de habitación, ampliaciones de estancia y bloqueos con un solo gesto.</p></div></div>
<div class="row"><h3>Check-in online</h3><div><p>Enlace seguro, acompañantes, foto del documento y firma digital.</p><a href="{U("checkin")}">Check-in online</a></div></div>
<div class="row"><h3>Formularios de visado en PDF automáticos</h3><div><p>Genera en un clic, a partir de los datos de la reserva, cartas de invitación y de alojamiento del hotel para solicitudes de visado.</p></div></div>
<div class="row"><h3>Venta de traslados y excursiones</h3><div><p>Ofrece traslados al aeropuerto y excursiones durante la conversación; Lio vincula la solicitud a la reserva.</p></div></div>
<div class="row"><h3>App móvil</h3><div><p>Gestiona reservas, mensajes y check-ins fuera del hotel con la app para iOS. Sigue funcionando sin conexión y se sincroniza cuando vuelves a estar online.</p></div></div>
</div></div></section>
<section><div class="wrap"><div class="section-head"><h2>Funcionalidades por plan</h2></div>
<div class="table-wrap"><table><thead><tr><th>Funcionalidad</th><th class="c">Starter</th><th class="c">Pro</th><th class="c">Growth</th></tr></thead><tbody>
<tr><th>Alojamientos</th><td class="c">1</td><td class="c">1</td><td class="c">2</td></tr>
<tr><th>Límite de habitaciones</th><td class="c num">10</td><td class="c num">50</td><td class="c num">150</td></tr>
<tr><th>Mensajes de IA / mes</th><td class="c num">1.000</td><td class="c num">5.000</td><td class="c num">12.000</td></tr>
<tr><th>Sincronización con más de 100 OTAs</th><td class="c">Sí</td><td class="c">Sí</td><td class="c">Prioritaria</td></tr>
<tr><th>Mensajería IA por WhatsApp</th><td class="c">Sí</td><td class="c">Sí</td><td class="c">Sí</td></tr>
<tr><th>Bandejas de OTAs (Booking.com, Airbnb, Expedia)</th><td class="c">No</td><td class="c">Sí</td><td class="c">Sí</td></tr>
<tr><th>Planning de habitaciones</th><td class="c">Sí</td><td class="c">Sí</td><td class="c">Sí</td></tr>
<tr><th>Formularios de visado en PDF</th><td class="c">Sí</td><td class="c">Sí</td><td class="c">Sí</td></tr>
<tr><th>Check-in online y firma digital</th><td class="c">No</td><td class="c">Sí</td><td class="c">Sí</td></tr>
<tr><th>Venta de traslados y excursiones</th><td class="c">No</td><td class="c">Sí</td><td class="c">Sí</td></tr>
<tr><th>App móvil para iOS</th><td class="c">No</td><td class="c">Sí</td><td class="c">Sí</td></tr>
<tr><th>Soporte prioritario y llamada de onboarding</th><td class="c">No</td><td class="c">No</td><td class="c">Sí</td></tr>
<tr><th>Marca blanca</th><td class="c">No</td><td class="c">No</td><td class="c">Sí</td></tr>
</tbody></table></div></div></section>
'''
    return {"key":"features","title":"Funcionalidades del software de gestión hotelera | Hostlio Pro",
            "desc":"Funcionalidades de Hostlio Pro: asistente IA para huéspedes, channel manager con 100+ OTAs, planning de habitaciones, check-in online, visados en PDF, traslados y app móvil.",
            "trail":[("Funcionalidades", U("features"))],"body":body,"faq":[FAQ_CORE[0], FAQ_CORE[3]]}

def pricing():
    body = f'''
<section class="page-hero"><div class="wrap"><h1>Precios de Hostlio Pro</h1>
<p class="lead">Una cuota mensual fija. Sin comisiones por reserva ni costes de alta. Prueba cualquier plan gratis durante 7 días.</p></div></section>
<section style="padding-top:0"><div class="wrap"><h2 class="sr-only">Planes</h2>
<span class="billing-note">20 % de descuento para los primeros 50 clientes, de por vida</span>
{plans_html()}
<p class="small muted" style="margin-top:18px">Precios en dólares estadounidenses, impuestos no incluidos. Última actualización: <time datetime="{UPDATED}">{D(UPDATED)}</time>.</p>
</div></section>
<section class="white rule"><div class="wrap">
<div class="section-head"><h2>¿Qué plan te conviene?</h2></div>
<div class="rows">
<div class="row"><h3>Starter</h3><div><p>Hostales, pensiones y hoteles boutique de hasta 10 habitaciones que envían menos de 1.000 respuestas al mes y quieren empezar con la sincronización de canales y las respuestas con IA.</p></div></div>
<div class="row"><h3>Pro</h3><div><p>Hoteles de 11 a 50 habitaciones que quieren que Lio gestione también los mensajes de las OTAs, usar el check-in online y vender traslados y excursiones.</p></div></div>
<div class="row"><h3>Growth</h3><div><p>Dos alojamientos o hasta 150 habitaciones, cuando necesitas soporte prioritario, un onboarding personalizado y uso en marca blanca.</p></div></div>
</div></div></section>
'''
    faq = [FAQ_CORE[1], FAQ_CORE[2],
      ("¿Cobráis comisión por reserva?", "No. Hostlio Pro es una suscripción mensual fija; no se queda ningún porcentaje del valor de las reservas."),
      ("¿Hay opción de facturación anual?", "Sí. Las suscripciones se facturan por adelantado de forma mensual o anual, y los planes anuales tienen un 20 % de descuento (Términos del servicio, sección 3)."),
      ("¿Puedo cambiar de plan?", "Sí. Sube o baja de plan cuando quieras; el cambio se aplica a partir de tu siguiente periodo de facturación."),
      ("¿Cuánto dura el descuento de lanzamiento?", "Se aplica a los primeros 50 clientes, y tu precio se mantiene mientras sigas con la suscripción.")]
    return {"key":"pricing","title":"Precios de software hotelero: desde 49 $/mes | Hostlio Pro",
            "desc":"Precios de Hostlio Pro: Starter 49 $, Pro 89 $ y Growth 149 $ al mes. Sin comisiones ni costes de alta, con prueba gratuita de 7 días. Compara los planes.",
            "trail":[("Precios", U("pricing"))],"body":body,"faq":faq,"schema":[software_schema(L, detailed=True)]}

FAQ_ALL = FAQ_CORE + [
 ("¿Para qué tipos de hotel es Hostlio Pro?", "Para alojamientos independientes de 10 a 150 habitaciones, como hoteles boutique, hoteles urbanos, hostales y pensiones, apartahoteles y hostels."),
 ("¿Hay una app móvil?", "Sí. Los planes Pro y Growth incluyen una app para iOS. Funciona sin conexión a internet y sincroniza los datos cuando vuelves a estar online."),
 ("¿Cómo funciona el check-in online?", "Los huéspedes reciben un enlace personal y seguro, y antes de llegar envían desde el móvil los datos de su documento, los acompañantes y una firma digital. Disponible en Pro y Growth."),
 ("¿Para qué sirve la función de formularios de visado en PDF?", "Convierte automáticamente los datos de la reserva en cartas de alojamiento e invitación del hotel en PDF para los huéspedes que necesitan visado."),
 ("¿Están seguros mis datos?", "Los datos se transmiten mediante conexiones cifradas, y los datos de cada hotel están aislados de los de otros alojamientos con reglas de acceso a nivel de fila. Los datos de los huéspedes pueden eliminarse a petición."),
 ("¿Cuánto tiempo lleva la configuración?", "La mayoría de los hoteles empiezan el mismo día añadiendo sus tipos de habitación y conectando los canales. El plan Growth incluye una llamada de onboarding personalizada."),
 ("¿En qué idiomas se ofrece el soporte?", "El panel y el soporte están disponibles en inglés y turco. Escríbenos a " + EMAIL + "."),
]

def faq_page():
    body = f'''<section class="page-hero"><div class="wrap"><h1>Preguntas frecuentes</h1>
<p class="lead">Las preguntas más habituales sobre las funcionalidades, los precios y la configuración de Hostlio Pro. ¿No encuentras tu respuesta? <a href="{U("contact")}">Escríbenos</a>.</p></div></section>
<section style="padding-top:0"><div class="wrap">{faq_block(FAQ_ALL, L, heading=False, wrap=False)}</div></section>'''
    return {"key":"faq","title":"Preguntas frecuentes sobre Hostlio Pro | Hostlio Pro",
            "desc":"Preguntas frecuentes sobre el software de gestión hotelera Hostlio Pro: precios, prueba gratuita, integraciones con OTAs, el asistente IA Lio, check-in online y seguridad.",
            "trail":[("Preguntas frecuentes", U("faq"))],"body":body,"faq":FAQ_ALL,"faq_inline":True,"page_type":"FAQPage"}

def about():
    body = f'''<section class="page-hero"><div class="wrap split"><div><h1>Por qué creamos Hostlio Pro</h1>
<p class="lead">En los hoteles pequeños, la recepción, las ventas y la comunicación con los huéspedes suelen recaer en una sola persona. Hostlio Pro existe para que esa persona no se ahogue en mensajes por la noche ni en pantallas de canales durante el día.</p></div><div class="hero-img"><img src="/assets/img/gen-shutters.webp" alt="" width="1080" height="1350"></div></div></section>
<section class="white rule"><div class="wrap split">
<div class="prose"><h2>Qué hacemos</h2>
<p>Hostlio Pro es un software de gestión hotelera con IA para hoteles independientes. Dejamos la comunicación con los huéspedes en manos de nuestro asistente de IA Lio, reunimos la distribución en OTAs en un solo calendario a través de Channex y llevamos el check-in al móvil del huésped.</p>
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
    return {"key":"contact","title":"Contacto y solicitud de demo | Hostlio Pro","desc":"Contacta con el equipo de Hostlio Pro o solicita una demo gratuita de 30 minutos adaptada a tu hotel. Soporte en inglés y turco, email: " + EMAIL,
            "trail":[("Contacto", U("contact"))],"body":body,"page_type":"ContactPage","no_final":True}

POSTS = [
 {"key":"post-overbooking","title":"Cómo evitar el overbooking: 6 pasos para hoteles","date":"2026-09-21","desc":"Por qué se producen las sobreventas en los hoteles y cómo evitarlas: channel manager, reglas de cierre de venta, márgenes de disponibilidad y qué hacer si aun así ocurre."},
 {"key":"post-autoreply","title":"Cómo responder automáticamente a los mensajes de Booking.com","date":"2026-09-21","desc":"Tres formas de automatizar los mensajes de huéspedes de Booking.com: plantillas, mensajes programados y un asistente de IA."},
 {"key":"post-ai","title":"Responder a los huéspedes del hotel con IA: guía práctica","date":"2026-09-18",
  "desc":"Ventajas, riesgos y pasos de configuración para responder con IA a los mensajes de los huéspedes. Qué preguntas automatizar y cuáles deben quedarse en manos de tu equipo."},
 {"key":"post-pms","title":"Cómo elegir un software de gestión hotelera (PMS) para un hotel pequeño","date":"2026-09-10",
  "desc":"7 criterios para elegir un PMS para un hotel pequeño o boutique: channel manager, modelo de precios, mensajería con huéspedes, acceso móvil y más."},
]

def blog():
    items = "".join(f'<article><h2><a href="{U(p["key"])}">{p["title"]}</a></h2><p class="meta"><time datetime="{p["date"]}">{D(p["date"])}</time></p><p>{p["desc"]}</p></article>' for p in POSTS)
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
<p>El asistente de IA de Hostlio Pro, <a href="{U("ai")}">Lio</a>, usa la información de tu hotel y los datos de las reservas para responder a mensajes de WhatsApp y de las OTAs (Booking.com, Airbnb, Expedia) en más de 30 idiomas. Los planes incluyen entre 1.000 y 12.000 mensajes de IA al mes; consulta la <a href="{U("pricing")}">página de precios</a> para más detalles.</p>'''
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
<p>Los propietarios suelen estar fuera del alojamiento. Una app móvil, sobre todo una que siga funcionando cuando se cae internet, es una necesidad real.</p>
<h2>6. Check-in online</h2>
<p>Recoger los datos de los huéspedes antes de su llegada ahorra tiempo en recepción y simplifica los requisitos de registro de viajeros.</p>
<h2>7. Configuración y soporte</h2>
<p>Un hotel pequeño no puede asumir un proyecto de implantación de varias semanas. Elige un software que puedas usar el mismo día, con soporte en tu idioma, y pon a prueba el periodo gratuito con reservas reales.</p>
<h2>Lista de comprobación</h2>
<div class="table-wrap"><table><thead><tr><th>Criterio</th><th>Pregunta que hacer</th></tr></thead><tbody>
<tr><td>Channel manager</td><td>¿Está incluido y con cuántos canales se conecta?</td></tr><tr><td>Precios</td><td>¿Es una tarifa fija, hay comisión, el precio es público?</td></tr>
<tr><td>Mensajería</td><td>¿Están los mensajes de WhatsApp y de las OTAs en un solo lugar, con respuestas automáticas?</td></tr><tr><td>Móvil</td><td>¿Hay app y funciona sin conexión?</td></tr>
<tr><td>Check-in</td><td>¿Hay check-in online con firma digital?</td></tr><tr><td>Prueba</td><td>¿Hay prueba gratuita y cancelación sin permanencia?</td></tr></tbody></table></div>
<p>Hostlio Pro se ha creado en torno a estos criterios: consulta las <a href="{U("features")}">funcionalidades</a> y los <a href="{U("pricing")}">precios</a>.</p>'''
    faq = [("¿Necesita un hotel pequeño un PMS?", "Si vendes en varias OTAs y recibes decenas de mensajes al día, sí. Trabajar con hojas de cálculo y extranets de OTAs por separado aumenta el riesgo de overbooking y de respuestas lentas."),
           ("¿Qué diferencia hay entre un PMS y un channel manager?", "Un PMS gestiona las operaciones internas del hotel (reservas, habitaciones, huéspedes); un channel manager distribuye la disponibilidad y las tarifas a las OTAs. Un software como Hostlio Pro combina ambos en una sola plataforma.")]
    return article(next(p for p in POSTS if p["key"]=="post-pms"), c, faq)

def pages():
    import pages_v4
    return [home(), ai(), channel(), checkin(), features(), pricing(), faq_page(), about(), contact(), blog(), post_ai(), post_pms()] + pages_v4.pages(L, article) + __import__("legal_v5").pages(L, article)
