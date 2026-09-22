"""Spanish (es) data for the shared modules: build.py, home_v3.py, pages_v4.py, legal_v5.py.
Pure data + functions; no project imports. Links come from the U callable passed in."""

L = "es"
UPDATED_TXT = "21 de septiembre de 2026"
LEGAL_DATE_TXT = "20 de abril de 2026"

# ------------------------------------------------------------------ build.UI
UI = {
   "nav": [("features","Funcionalidades"),("ai","Asistente IA Lio"),("channel","Channel manager"),("pricing","Precios"),("blog","Blog")],
   "top": [("pricing","Precios"),("blog","Blog"),("faq","Preguntas frecuentes"),("about","Sobre nosotros")],
   "login":"Iniciar sesión", "trial":"Prueba gratis", "demo":"Solicitar demo", "menu":"Abrir menú",
   "skip":"Saltar al contenido", "home":"Inicio",
   "lang_label":"Idioma", "crumb_label":"Ruta de navegación",
   "foot_tag":"Software de gestión hotelera con IA para hoteles independientes. Mensajes de huéspedes, gestión de canales y calendario de reservas en un solo lugar.",
   "foot_product":"Producto","foot_company":"Empresa","foot_res":"Recursos","foot_sol":"Soluciones","privacy":"Política de privacidad","terms":"Términos del servicio","delacc":"Eliminar cuenta","sol":["Software para hoteles boutique","Software para hostales y pensiones","Software para apartahoteles","Software para hostels","Comparativa de software hotelero"],
   "foot_about":"Sobre nosotros","foot_contact":"Contacto","foot_faq":"Preguntas frecuentes",
   "rights":"Todos los derechos reservados.","updated":"Última actualización",
   "final_h":"Mantén tu recepción abierta también esta noche.",
   "final_p":"Pruébalo gratis durante 7 días. No se te cobra nada hasta que termine la prueba y puedes cancelar cuando quieras.",
   "faq_h":"Preguntas frecuentes",
}

# ------------------------------------------------------------------ build.MEGA
MEGA = {"btn":"Producto","cols":[
   ("Huéspedes",[("ai","sparkle","Asistente IA Lio","Respuestas 24/7 en más de 30 idiomas"),("checkin","identification-card","Check-in online","Documento, acompañantes y firma digital")]),
   ("Distribución",[("channel","arrows-left-right","Channel manager","Más de 100 OTAs en un solo calendario"),("features","calendar-dots","Planning de habitaciones","Calendario de reservas con arrastrar y soltar")]),
   ("Operaciones",[("features","van","Traslados y excursiones","Ingresos extra mientras conversas"),("features","device-mobile","App móvil","iOS que también funciona sin conexión")]),
   ("Por tipo de alojamiento",[("t-boutique","sparkle","Hoteles boutique","Hoteles de 10 a 50 habitaciones"),("t-guesthouse","users-three","Hostales y pensiones","Alojamientos de 1 a 10 habitaciones"),("t-apart","calendar-dots","Apartahoteles","Apartamentos y suites"),("t-hostel","globe-simple","Hostels","Venta por camas")]),
  ],"feat":("pricing","Comparar planes","Desde $49 al mes, 7 días gratis")}

# ------------------------------------------------------------------ build.software_schema / room_rack / 404
SOFT_DESC = "Software de gestión hotelera con IA para hoteles independientes: mensajería con huéspedes 24/7 en más de 30 idiomas, channel manager para más de 100 OTAs, calendario de reservas y check-in online."
SOFT_FEATURES = ["Asistente IA Lio para huéspedes (más de 30 idiomas)", "Channel manager (más de 100 OTAs vía Channex)", "Calendario de reservas con arrastrar y soltar", "Check-in online con firma digital", "Formularios de visado en PDF automáticos", "Venta de traslados y excursiones", "App móvil que funciona sin conexión"]
DAYS = ["Lun","Mar","Mié","Jue","Vie","Sáb","Dom"]
RACK = ("Planning de habitaciones", "Septiembre, semana 3", "Reservas con el color de cada canal: Booking.com azul, Airbnb melocotón, Expedia lila, Agoda arena, reserva directa verde")
NOTFOUND = ("Página no encontrada | Hostlio Pro",
            "La página que buscas no existe o se ha movido. Vuelve al inicio de Hostlio Pro, el software de gestión hotelera con IA para hoteles independientes.",
            "Página no encontrada",
            'Es posible que la página se haya movido o eliminado. Vuelve a la <a href="{home}">página de inicio</a>.')

# ------------------------------------------------------------------ home_v3.T
HOME = dict(
  title="Hostlio Pro | Software de gestión hotelera con IA",
  desc="Software de gestión hotelera Hostlio Pro: el asistente IA Lio responde a huéspedes 24/7 en 30+ idiomas y el channel manager sincroniza 100+ OTAs. 7 días gratis.",
  h1='Mientras tu hotel duerme, <em class="hl">Lio</em> responde',
  lead="Software de gestión hotelera con IA para hoteles independientes y hostales. Reservas, más de 100 canales y mensajes de huéspedes en un solo lugar, en más de 30 idiomas.",
  try_="Prueba gratis", demo="Solicitar demo", via="Conectado a través de Channex:", more="y más de 100 canales",
  coll_alt1="Patio de un hotel boutique con buganvillas y piscina al atardecer", coll_alt2="Propietaria de un hotel sonriendo con una taza de café",
  chip1=("Habitación 202 vendida","Booking.com, 21:40"), chip2="Cerrada en Airbnb y Expedia",
  bub_h=("Lio","Recepcionista IA, en línea"), bub_in="Hallo! Ist ein später Check-in möglich?", bub_out="Natürlich! Unsere Rezeption ist rund um die Uhr besetzt.", bub_note="Respondido en alemán, 4 s",
  pick_h="¿Por dónde quieres empezar?", pick_p="Elige lo que te importa y preparamos tu cuenta en torno a ello.", pick_none="Elige todos los que quieras.", pick_some="{n} seleccionados, pruébalos gratis durante 7 días.", pick_btn="Empezar", pick_name="interest",
  tiles=[("ai","sparkle","t-peach","Asistente IA Lio","Respuestas a huéspedes en más de 30 idiomas"),("channel","arrows-left-right","t-lilac","Channel manager","Sincronización en tiempo real con más de 100 OTAs"),("rack","calendar-dots","t-sand","Planning de habitaciones","Calendario de reservas con arrastrar y soltar"),("checkin","identification-card","t-peach","Check-in online","Documento y firma antes de la llegada"),("upsell","van","t-lilac","Traslados y excursiones","Ingresos extra mientras conversas"),("mobile","device-mobile","t-sand","App móvil","Gestiona el hotel desde cualquier lugar")],
  story_h='<em class="hl">2:14 de la madrugada</em>: un huésped escribe',
  story_p="Lo que pasa mientras duermes, en tres escenas.",
  story=[("brand-night","Propietario de un hotel dormido con el móvil iluminándose en la mesita de noche","02:14","Un huésped escribe","Un huésped de Alemania pregunta por el check-in tardío. Tú estás profundamente dormido."),
         ("brand-phone","Mano sosteniendo un móvil con la pantalla naranja de respuesta de Lio","02:14","Lio responde al instante","Con la información de tu hotel y en el idioma del huésped. Si hace falta, te deja una nota."),
         ("brand-hotelier","Propietaria de un hotel caminando por el lobby con su café de la mañana","08:30","Por la mañana, todo resuelto","La conversación te espera en tu panel, traducida. Un huésped contento y tú, descansado.")],
  story_chip="Lio respondió",
  tour_h='Gestiona el día de tu hotel <em class="hl">desde una sola pantalla</em>', tour_p="Mensajes de huéspedes, reservas, canales y check-in funcionan conectados.", tour_label="Recorrido por el producto",
  tabs=["Mensajes","Calendario","Canales","Check-in"],
  st=[("Todos los mensajes de huéspedes en una sola bandeja","WhatsApp y los mensajes de Booking.com, Airbnb y Expedia, todo junto. Lio responde con la información de tu hotel y tú solo ves lo que te necesita.",["Respuestas automáticas en más de 30 idiomas","Los datos de la reserva junto a cada mensaje","Te deriva lo que no tiene claro"],"ai","Cómo funciona Lio"),
      ("Toda tu semana en el planning de habitaciones","Ve cada reserva con el color de su canal. Cambiar de habitación, alargar una estancia o bloquear fechas es un solo gesto.",["Cambios de habitación con arrastrar y soltar","Reservas con el color de cada canal","El mismo calendario en la web y en iOS"],"features","Todas las funcionalidades"),
      ("Más de 100 canales, una sola disponibilidad","Sincronización bidireccional a través de Channex. Una habitación vendida en un canal se cierra al instante en los demás.",["Tarifas y restricciones desde una sola pantalla","Nuevas reservas y cancelaciones entran solas","Sin riesgo de overbooking"],"channel","Channel manager"),
      ("El check-in, hecho antes de la llegada","Los huéspedes envían los datos de su documento, sus acompañantes y su firma desde el móvil mediante un enlace seguro.",["En el navegador, sin descargar ninguna app","Acompañantes en un único formulario","Firma digital y consentimiento"],"checkin","Check-in online")],
  inbox_top=("Bandeja de entrada","12 conversaciones abiertas"), inbox_note="Traducción: el check-in es a partir de las 14:00, podemos guardarte el equipaje.",
  chan_top=("Canales conectados","Última sincronización: ahora mismo"), sync="Sincronizado",
  ci_top=("Check-in online","Habitación 202"), ci_f=[("Nombre completo","Keiko Sato"),("Nacionalidad","Japón"),("Acompañantes","1 huésped añadido")], ci_sig="Firma",
  bento_h='<em class="hl">Todo</em> lo que un hotel necesita', bento_p="Todos los módulos están conectados: sin herramientas sueltas ni contraseñas distintas.",
  b_lio=("Asistente IA Lio","Resuelve la mayoría de las preguntas de los huéspedes antes de que las veas y te resume el resto.","Is breakfast included?","Yes, from 7:30 to 10:30 on the terrace."),
  b_chan=("Channel manager","Más de 100 canales de venta a través de Channex, una sola disponibilidad."),
  b_rack=("Planning de habitaciones","Calendario de reservas con arrastrar y soltar."),
  b_ci=("Check-in online","Documento, acompañantes y firma digital antes de la llegada."),
  b_pdf=("Formularios de visado en PDF","Cartas de alojamiento e invitación en un clic.","Carta de alojamiento","PDF"),
  b_tr=("Venta de traslados y excursiones","Lio los ofrece en el momento justo; tú ganas más.","Traslado al aeropuerto","+35 €"),
  b_lang=("Más de 30 idiomas","El huésped escribe en su idioma y recibe la respuesta en ese mismo idioma."),
  b_mob=("App móvil","Reservas, mensajes y check-ins en iOS, incluso sin conexión."),
  types_h='Pensado para <em class="hl">cada tipo de alojamiento</em>', types_p="Diseñado para alojamientos independientes de 10 a 150 habitaciones.",
  types=[("brand-courtyard","Patio de un hotel boutique con piscina y buganvillas","Hotel boutique","10–50 habitaciones","Muchos huéspedes internacionales, cada mensaje personal."),
         ("gen-hostel","Lobby con paneles de madera y zona común","Hostel","Camas y habitaciones","Viajeros de muchos idiomas, bandejas llenas."),
         ("gen-guesthouse","Acogedora habitación de hostal con lámpara de escritorio","Hostal / pensión","1–10 habitaciones","Un turno de noche para un equipo de una sola persona."),
         ("gen-apart","Apartamento luminoso con ropa de cama blanca","Apartahotel","10–40 unidades","Check-in online para una llegada sin llaves.")],
  plans_h="Un plan a la medida de tu hotel", plans_p="Una cuota mensual fija, sin contratos de permanencia. Todos los planes son gratis durante 7 días.",
  early="20 % de descuento para los primeros 50 clientes, para siempre", tax='Precios sin impuestos. <a href="{p}">Compara los planes en detalle</a>.',
  ai_h='Lio, el <em class="hl">turno de noche</em> de tu recepción', ai_p="Un asistente de IA que trabaja con la información de tu hotel. Responde a los huéspedes, vende extras y te deja a ti el resto.",
  ai_wide=("Responde en el idioma del huésped","Una pregunta en japonés recibe respuesta en japonés; una en árabe, en árabe. Tú lees la conversación en tu idioma."),
  ai_cards=[("van","Vende por ti","Ofrece traslados al aeropuerto y excursiones en el momento justo y vincula la solicitud a la reserva."),("hand-arrow-up","Sabe cuándo derivar","Los mensajes que requieren una decisión, como descuentos, quejas o peticiones especiales, pasan a tu equipo."),("calendar-dots","Conoce la reserva","Qué huésped, qué habitación, qué fechas: cada respuesta usa los datos de la reserva.")],
  ai_photo=("brand-guest-phone","Huésped junto a una ventana escribiendo un mensaje en su móvil","En WhatsApp y en las OTAs","WhatsApp, Booking.com, Airbnb y Expedia."),
  ai_btn="Descubre Lio",
  answer="<strong>¿Qué es Hostlio Pro?</strong> Hostlio Pro es un software de gestión hotelera en la nube (un PMS hotelero) para hoteles independientes y hostales de 10 a 150 habitaciones. Delega la comunicación con los huéspedes en la IA, reúne las reservas de las OTAs en un solo calendario y lleva el check-in al móvil del huésped. Se gestiona desde la web y desde una app para iOS, y se usa en más de 20 países.",
  stats=[("30+","idiomas atendidos"),("100+","OTAs y canales de venta"),("20+","países con hoteles en Hostlio Pro"),("7 días","de prueba gratis, sin compromiso")],
  sup_h="Un equipo que te respalda",
  sup=[("rocket-launch","t-peach","Configuración en el mismo día","Añade los tipos de habitación y conecta los canales. El plan Growth incluye una llamada de puesta en marcha personalizada."),
       ("lifebuoy","t-lilac","Soporte en inglés y turco",'¿Te has atascado con algo? Escribe al equipo a <a href="mailto:{e}">{e}</a>.'),
       ("book-open-text","t-sand","Guías",'<a href="{b}">Artículos del blog</a> sobre gestión hotelera y distribución, además de <a href="{f}">preguntas frecuentes</a>.')],
  sup_img=("gen-support-call","Propietario de un hotel revisando las reservas en su portátil"),
)

# ------------------------------------------------------------------ pages_v4 labels
PV4 = dict(trial="Prueba gratis durante 7 días", demo="Solicitar demo", plan_h="¿Qué plan te conviene?",
           cmp_t='Para compararlo con otros programas para hoteles, consulta nuestra <a href="{c}">comparativa de software hotelero</a>.',
           see_pricing="Ver precios")

# ------------------------------------------------------------------ pages_v4.TYPES
def types(U):
    return [
 dict(key="t-guesthouse", img=("gen-guesthouse", "Acogedora habitación de hostal con lámpara de escritorio", 1080, 1350),
  title="Software para hostales y pensiones con IA | Hostlio Pro",
  desc="Software para hostales y pensiones: respuestas automáticas en más de 30 idiomas, sincronización con Booking.com y Airbnb, check-in online. Desde $49/mes.",
  crumb="Software para hostales y pensiones", h1='<em class="hl">Software para hostales</em> y pensiones que responde por ti',
  lead="En un hostal o una pensión, una sola persona se encarga de los mensajes de madrugada, las reservas de varios canales y el check-in. Hostlio Pro le quita carga de encima.",
  q="¿Qué es un software para hostales y pensiones?",
  a="Un software para hostales y pensiones permite a los alojamientos pequeños de 1 a 10 habitaciones gestionar reservas, disponibilidad y comunicación con los huéspedes en un solo lugar. Hostlio Pro añade Lio, un asistente de IA que responde a las preguntas de los huéspedes 24/7 en más de 30 idiomas. El plan Starter cuesta $49 al mes para alojamientos de hasta 10 habitaciones.",
  pains_h="¿Con qué problemas lidian más los hostales y pensiones?",
  pains=[("Mensajes de noche","Las preguntas sobre check-in tardío, aparcamiento y desayuno llegan a medianoche. Lio responde en el idioma del huésped y tú lees un resumen por la mañana."),
         ("Varios canales","Vender la misma habitación en Booking.com y Airbnb provoca dobles reservas. El channel manager sincroniza la disponibilidad al instante."),
         ("Documentos y registro","Anotar los datos de los huéspedes en recepción lleva tiempo. El check-in online los recoge antes de la llegada."),
         ("Presupuesto ajustado","El software con comisiones se encarece a medida que sube la ocupación. Hostlio Pro tiene una cuota mensual fija.")],
  plan="Para la mayoría de los hostales y pensiones basta con el plan <strong>Starter</strong>: hasta 10 habitaciones, 1000 mensajes de IA al mes y mensajería IA por WhatsApp. Elige <strong>Pro</strong> si además quieres check-in online y que Lio gestione los mensajes de las OTAs.",
  faq=[("¿Existe un software gratuito para hostales y pensiones?","Puedes probar Hostlio Pro gratis durante 7 días. Después, Starter cuesta $49 al mes (precio de lanzamiento para los primeros 50 clientes)."),
       ("¿Sirve para una pensión de 3 habitaciones?","Sí. Starter está pensado para un alojamiento de hasta 10 habitaciones; el precio es el mismo aunque tengas menos."),
       ("¿Puedo usar Airbnb y Booking.com a la vez?","Sí. Hostlio Pro sincroniza ambos, y más de 100 canales más, en un solo calendario a través de Channex.")]),
 dict(key="t-boutique", img=("gen-boutique-room", "Patio de un hotel boutique con piscina y buganvillas", 1080, 1350),
  title="Software para hoteles boutique con mensajería IA | Hostlio Pro",
  desc="Software para hoteles boutique: respuestas personales a huéspedes extranjeros en 30+ idiomas, sincronización con 100+ OTAs, check-in online y venta de traslados.",
  crumb="Software para hoteles boutique", h1='<em class="hl">Software para hoteles boutique</em> centrado en el huésped',
  lead="Lo que distingue a un hotel boutique es la atención personal. Hostlio Pro se encarga de las preguntas repetitivas para que tu equipo tenga más tiempo para los huéspedes.",
  q="¿Qué es un software para hoteles boutique?",
  a="Un software para hoteles boutique es un sistema de gestión hotelera (PMS hotelero) para hoteles de unas 10 a 50 habitaciones con un concepto propio. En Hostlio Pro, el asistente de IA Lio responde a los mensajes de los huéspedes con la información del propio hotel y en el idioma del huésped, y el channel manager mantiene sincronizadas más de 100 OTAs.",
  pains_h="¿Por qué un hotel boutique necesita un software específico?",
  pains=[("Huéspedes de muchos idiomas","Muchos huéspedes vienen del extranjero. Lio responde a cada mensaje en el idioma del huésped y con el tono de tu hotel."),
         ("Ingresos extra","Los traslados al aeropuerto y las excursiones son importantes para los hoteles boutique. Lio los ofrece en el momento justo."),
         ("Mucho tráfico de OTAs","Las reservas de Booking.com, Expedia y Airbnb aparecen en un solo planning de habitaciones, con el color de cada canal."),
         ("Check-in rápido","Con el check-in online y la firma digital, el huésped recibe una bebida de bienvenida en lugar de un formulario.")],
  plan="Para hoteles boutique de 10 a 50 habitaciones recomendamos <strong>Pro</strong>: 5000 mensajes de IA al mes, mensajería por WhatsApp y en las bandejas de Booking.com, Airbnb y Expedia, check-in online, venta de traslados y excursiones y la app para iOS.",
  faq=[("¿Cuál es el mejor software para un hotel boutique?","Depende del número de habitaciones, del perfil de los huéspedes y del presupuesto. Para hoteles de 10 a 50 habitaciones con muchos huéspedes internacionales que buscan un precio fijo, la mensajería con IA y el channel manager de Hostlio Pro encajan bien. Consulta nuestra página comparativa para ver otras opciones."),
       ("¿Puedo usar Hostlio Pro con mi web actual?","Sí. Hostlio Pro funciona junto a tu web actual, no la sustituye. Lio responde a los huéspedes por WhatsApp y en las bandejas de las OTAs, y las reservas de todos los canales llegan al mismo calendario."),
       ("¿Cuántos usuarios puedo añadir?","Consulta la página de precios para ver los detalles de cada plan o pregunta a nuestro equipo durante la demo.")]),
 dict(key="t-apart", img=("gen-apart", "Apartamento luminoso con ropa de cama blanca", 1080, 1350),
  title="Software para apartahoteles con check-in online | Hostlio Pro",
  desc="Software para apartahoteles y apartamentos turísticos: sincronización con Airbnb y Booking.com, check-in online con firma digital y mensajería IA en 30+ idiomas.",
  crumb="Software para apartahoteles", h1='<em class="hl">Software para apartahoteles</em> pensado para gestionar en remoto',
  lead="Los apartahoteles a menudo no tienen recepción o la tienen con horario limitado, así que la comunicación con los huéspedes y el check-in se hacen en remoto. Hostlio Pro está hecho para eso.",
  q="¿Qué es un software para apartahoteles?",
  a="Un software para apartahoteles gestiona las reservas, los canales y los procesos con huéspedes de los alojamientos que venden apartamentos y suites con cocina. En Hostlio Pro, los huéspedes envían los datos de su documento y su firma mediante un enlace de check-in online antes de llegar, y el asistente de IA Lio responde a las preguntas sobre el acceso en más de 30 idiomas.",
  pains_h="¿Qué es lo que más tiempo quita en un apartahotel?",
  pains=[("Check-in en remoto","El formulario de check-in online recoge el documento, los acompañantes y la firma antes de la llegada."),
         ("Instrucciones de acceso","Las preguntas sobre la entrega de llaves, el wifi y el aparcamiento se repiten. Lio las responde con la información de tu alojamiento."),
         ("Canales de estancias cortas","La disponibilidad de Airbnb y Booking.com se sincroniza al instante a través de Channex."),
         ("Estancias largas","Alargar una estancia o cambiar de apartamento es cuestión de arrastrar y soltar en el planning de habitaciones.")],
  plan="El check-in online está incluido en Pro y Growth, por eso recomendamos <strong>Pro</strong> para apartahoteles. Si gestionas dos alojamientos, mira <strong>Growth</strong>.",
  faq=[("¿Funciona Hostlio Pro en un apartahotel sin recepción?","Sí. El check-in online y la mensajería con IA hacen en remoto la recogida de datos y la atención de preguntas que haría una recepción."),
       ("¿Responde también a los mensajes de Airbnb?","En Pro y Growth, los mensajes de las OTAs, incluido Airbnb, llegan a la bandeja de Lio."),
       ("¿Hay un límite de unidades?","Starter admite hasta 10, Pro hasta 50 y Growth hasta 150 habitaciones o unidades.")]),
 dict(key="t-hostel", img=("gen-hostel", "Lobby con paneles de madera y zona común", 1080, 1350),
  title="Software para hostels: mensajes multilingües y OTAs | Hostlio Pro",
  desc="Software para hostels: sincronización con Hostelworld, Booking.com y 100+ canales, mensajería IA en más de 30 idiomas y check-in online. 7 días gratis.",
  crumb="Software para hostels", h1='<em class="hl">Software para hostels</em> con bandejas llenas y multilingües',
  lead="Los hostels tienen huéspedes internacionales, mucho volumen de mensajes y equipos pequeños. Hostlio Pro se encarga de las preguntas en varios idiomas y mantiene los canales en un solo calendario.",
  q="¿Qué es un software para hostels?",
  a="Un software para hostels gestiona las reservas, los canales y la comunicación con los huéspedes de los hostels que venden camas y habitaciones. Hostlio Pro se conecta a más de 100 canales, incluido Hostelworld, a través de Channex y responde a las preguntas de los huéspedes en más de 30 idiomas con su asistente de IA Lio.",
  pains_h="¿Qué es lo que más necesita un hostel?",
  pains=[("Tráfico multilingüe","Los viajeros escriben en su propio idioma. Lio responde en cada uno de ellos."),
         ("Hostelworld y OTAs","Hostelworld, Booking.com y los demás canales comparten una sola disponibilidad."),
         ("Excursiones y traslados","Los tours por la ciudad y los traslados al aeropuerto son extras habituales en los hostels; Lio los ofrece en el momento justo."),
         ("Turno de noche","Las preguntas nocturnas no esperan a la mañana; el equipo solo se ocupa de lo que requiere una decisión.")],
  plan="Para hostels con mucho volumen recomendamos <strong>Pro</strong>, con 5000 mensajes de IA al mes. Planifiquemos juntos la configuración por camas durante la demo.",
  faq=[("¿Funciona con Hostelworld?","Sí. Hostelworld está entre los canales conectados a Channex."),
       ("¿Se admite la venta por camas (dormitorios compartidos)?","Depende de tu configuración; planifiquemos juntos la estructura de habitaciones y camas durante la demo."),
       ("¿Cuántos mensajes de IA necesito?","Unas 150 respuestas automáticas al día son aproximadamente 4500 al mes, lo que encaja con el plan Pro.")]),
    ]

# ------------------------------------------------------------------ pages_v4.CMP
def cmp(U):
    return dict(
  title="Comparativa de software hotelero 2026: precios e IA | Hostlio Pro",
  desc="Hostlio Pro, Cloudbeds, Mews, Little Hotelier y HotelRunner comparados: precios publicados, precio inicial, comisiones, prueba gratuita y mensajería IA.",
  crumb="Comparativa de software hotelero", h1='<em class="hl">Comparativa</em> de software hotelero (2026)',
  lead="Comparamos cinco programas para hoteles populares entre los hoteles independientes, usando solo lo que cada proveedor publica en su propia página de precios.",
  q="¿Qué software de gestión hotelera te conviene?",
  a="Respuesta corta: para hoteles de un solo establecimiento con 10 a 150 habitaciones y muchos huéspedes internacionales, un software de precio fijo con mensajería IA incluida (como Hostlio Pro) mantiene el presupuesto previsible. Los grupos con varios establecimientos y necesidades corporativas pueden valorar plataformas con precio bajo presupuesto como Mews o Cloudbeds; los alojamientos en Turquía que buscan soporte local y una red B2B pueden mirar HotelRunner; y los alojamientos pequeños que quieren la red de SiteMinder pueden considerar Little Hotelier.",
  cols=["Software","¿Precios publicados?","Desde","Comisión por reserva","Prueba gratuita","Mensajería IA con huéspedes"],
  rows=[("Hostlio Pro","Sí","$49/mes (precio de lanzamiento)","Ninguna, cuota mensual fija","7 días","Todos los planes (Lio, más de 30 idiomas)"),
        ("Cloudbeds","No, bajo presupuesto","Presupuesto","Indica que no añade comisión a las reservas del Booking Engine y del Channel Manager","No se indica en la página de precios","No se indica por separado en la página de precios"),
        ("Mews","No, bajo presupuesto","Presupuesto","No se indica en la página de precios","No se indica en la página de precios","Resúmenes con IA de las preferencias del huésped en Advanced; la mensajería no se indica por separado"),
        ("Little Hotelier","Se calcula según el número de habitaciones","Mediante calculadora de precios","Comisión del 1 % por reserva en Basics","30 días","No se indica en la página de precios"),
        ("HotelRunner","Sí (planes principales)","$19,95/mes + 0,75 % (Manage)","Del 0,75 % al 1,25 % según el plan","Disponible","En el nivel Advanced \"Automate\"")],
  when_h="¿Cuál elegir y cuándo?",
  when=[("Hostlio Pro","Uno o dos establecimientos, de 10 a 150 habitaciones, mucho tráfico de huéspedes internacionales y un presupuesto mensual fijo."),
        ("Cloudbeds y Mews","Grupos con varios establecimientos y necesidades corporativas, como revenue management y un amplio marketplace de integraciones."),
        ("HotelRunner","Alojamientos en Turquía que quieren soporte local, una red de ventas B2B y una cuota fija baja más comisión."),
        ("Little Hotelier","Alojamientos pequeños que quieren la infraestructura de SiteMinder y aceptan un precio basado en el número de habitaciones.")],
  note="Información recopilada el 21 de septiembre de 2026 de la página de precios de cada proveedor; los precios y planes pueden cambiar, así que consulta la página de cada proveedor para ver los datos actualizados. Hostlio Pro es parte interesada en esta comparativa; hemos basado la tabla solo en información publicada.",
  src_h="Fuentes",
  faq=[("¿Qué es un software de gestión hotelera?","Un software de gestión hotelera (un PMS hotelero) permite a un alojamiento gestionar reservas, disponibilidad de habitaciones, canales de venta e información de los huéspedes en un solo lugar."),
       ("¿Cuánto cuesta un programa para hoteles?","Según los precios publicados, los planes empiezan aproximadamente entre $20 y $150 al mes; algunos proveedores añaden una comisión del 0,75–1,25 % por reserva y otros solo dan presupuestos."),
       ("¿Qué es mejor, comisión o cuota fija?","A medida que suben la ocupación y la tarifa media, el coste basado en comisiones crece. Una cuota mensual fija es más previsible para los hoteles que quieren un presupuesto fijo.")],
    )

# ------------------------------------------------------------------ pages_v4.GUIDES
def guides(U):
    return [
 dict(key="post-overbooking", date="2026-09-21", title="Cómo evitar el overbooking: 6 pasos para hoteles",
  desc="Por qué se produce el overbooking en hoteles y cómo evitarlo: channel manager, cierres de venta, márgenes de disponibilidad y qué hacer si ocurre igualmente.",
  content=f'''<div class="answer"><p><strong>Respuesta corta:</strong> el overbooking consiste en aceptar más reservas de las que puedes alojar para la misma habitación y las mismas fechas. En los hoteles independientes, la causa más habitual es actualizar la disponibilidad a mano en varias OTAs. Un channel manager bidireccional y en tiempo real elimina la mayor parte del riesgo.</p></div>
<h2>¿Por qué se produce el overbooking?</h2>
<ul><li>Actualizar la disponibilidad en Booking.com, Airbnb y Expedia por separado y a mano</li><li>Registrar tarde las reservas por teléfono o de clientes sin reserva previa (walk-in)</li><li>Cancelaciones y cambios que llegan a un canal pero no a otro</li><li>Sincronización con retraso (cada hora) entre canales</li></ul>
<h2>Evita el overbooking en 6 pasos</h2>
<ol><li><strong>Usa una única fuente de disponibilidad.</strong> Todos los canales deben leer la disponibilidad de un solo calendario (tu PMS).</li>
<li><strong>Elige una sincronización bidireccional y en tiempo real.</strong> Cuando llega una reserva, la habitación debe cerrarse en los demás canales en cuestión de segundos.</li>
<li><strong>Registra las reservas directas de inmediato.</strong> Añade al mismo calendario, al momento, las ventas por teléfono y las de clientes walk-in.</li>
<li><strong>Gestiona los cierres de venta (stop-sell) y las estancias mínimas en un solo lugar.</strong> Cambiarlos canal por canal invita a cometer errores.</li>
<li><strong>Deja un pequeño margen en temporada alta.</strong> Abrir la última habitación solo en tu canal directo reduce el riesgo.</li>
<li><strong>Revisa con regularidad el mapeo de canales.</strong> Cuando añadas un tipo de habitación, confirma el mapeo en todos los canales.</li></ol>
<h2>¿Y si ocurre igualmente?</h2>
<p>Informa al huésped de inmediato y con honestidad, ofrécele una alternativa igual o mejor (un hotel cercano, una mejora de habitación) y asume los costes adicionales, como los traslados. Registra qué canal lo provocó y por qué.</p>
<h2>Cómo funciona en Hostlio Pro</h2>
<p>El <a href="{U("channel")}">channel manager</a> de Hostlio Pro sincroniza la disponibilidad de forma bidireccional y en tiempo real en más de 100 canales a través de Channex. Las reservas aparecen en un solo planning de habitaciones, con el color de cada canal.</p>''',
  faq=[("¿Qué significa overbooking?","El overbooking se produce cuando un hotel acepta más reservas de las que puede alojar para la misma habitación y las mismas fechas; también se conoce como doble reserva o sobreventa."),
       ("¿Un channel manager evita por completo el overbooking?","La sincronización bidireccional en tiempo real elimina la mayor parte del riesgo; aun así, las reservas directas que no se registran y los mapeos de habitaciones incorrectos pueden seguir causando problemas.")]),
 dict(key="post-autoreply", date="2026-09-21", title="Cómo responder automáticamente a los mensajes de Booking.com",
  desc="Tres formas de automatizar los mensajes de Booking.com: plantillas, mensajes programados y un asistente de IA. Cuándo funciona cada una y dónde se queda corta.",
  content=f'''<div class="answer"><p><strong>Respuesta corta:</strong> hay tres formas de automatizar los mensajes de Booking.com: las plantillas de mensajes guardadas en la extranet, los mensajes programados según la fase de la reserva y un asistente de IA que entiende la pregunta del huésped y responde con la información de tu hotel. Las plantillas sirven para la información estándar; un asistente de IA, para las preguntas que cambian con cada huésped.</p></div>
<h2>1. Plantillas de mensajes</h2>
<p>Guarda como plantillas las respuestas frecuentes, como la hora del check-in, cómo llegar o el aparcamiento, y envíalas con un clic. Son sencillas, pero alguien tiene que leer el mensaje y elegir la plantilla adecuada.</p>
<h2>2. Mensajes programados</h2>
<p>Mensajes que se envían automáticamente después de la reserva, un día antes de la llegada o el día de salida. El huésped recibe la información antes de preguntar, pero estos mensajes no responden a las preguntas que escribe después.</p>
<h2>3. Un asistente de IA</h2>
<p>Lee el mensaje del huésped y redacta una respuesta a partir de tu base de conocimiento, en el idioma del huésped. Funciona mejor con las preguntas nocturnas, en varios idiomas o que no encajan en ninguna plantilla, y debe derivar las decisiones (descuentos, quejas) al personal.</p>
<div class="table-wrap"><table><thead><tr><th>Método</th><th>Ideal para</th><th>Límite</th></tr></thead><tbody>
<tr><td>Plantillas</td><td>Información estándar</td><td>Alguien tiene que leer y elegir</td></tr>
<tr><td>Mensajes programados</td><td>Información previa a la llegada</td><td>No responde a las preguntas entrantes</td></tr>
<tr><td>Asistente de IA</td><td>Preguntas a cualquier hora y en cualquier idioma</td><td>Necesita una buena base de conocimiento</td></tr></tbody></table></div>
<h2>Por qué importa el tiempo de respuesta</h2>
<p>Una respuesta rápida antes de reservar facilita la decisión del huésped; una respuesta rápida durante la estancia influye en la satisfacción y en las reseñas.</p>
<h2>Cómo funciona en Hostlio Pro</h2>
<p>En Pro y Growth, los mensajes de las OTAs, incluido Booking.com, llegan a la bandeja de <a href="{U("ai")}">Lio, el asistente de IA</a>. Lio responde con la información de tu hotel en el idioma del huésped y te deja a ti lo que no tiene claro.</p>''',
  faq=[("¿Se puede responder automáticamente a los mensajes de Booking.com?","Sí. Las plantillas de la extranet y los mensajes programados son herramientas propias de Booking.com; para respuestas automáticas adaptadas a cada pregunta hace falta un asistente de IA que lea los mensajes."),
       ("¿Puede un asistente de IA dar información incorrecta?","El riesgo es bajo cuando el asistente solo usa la información que proporciona el hotel y deriva al personal las preguntas en las que tiene dudas.")]),
    ]

# ------------------------------------------------------------------ legal_v5
LEGAL_T = {
 "privacy": ("Política de privacidad | Hostlio Pro",
             "Política de privacidad de Hostlio Pro: qué datos recopilamos, cómo los usamos y compartimos, seguridad de los datos, conservación, cookies y tus derechos del RGPD.",
             "Política de privacidad"),
 "terms":   ("Términos del servicio | Hostlio Pro",
             "Términos del servicio de Hostlio Pro: descripción del servicio, suscripciones y pagos, cancelación y reembolsos, contenido generado por IA, integraciones con OTAs y responsabilidad.",
             "Términos del servicio"),
}
LEGAL_NOTE = 'Última actualización: <time datetime="{iso}">{date}</time>, {addr}. Este texto es una traducción del original en inglés; en caso de discrepancia, prevalecerá la <a href="{en_url}">versión en inglés</a>.'

def privacy_body(U, EMAIL, ADDR, ul):
    return f'''<p>Esta Política de privacidad describe cómo Hostlio Pro, operado por Loti Members LLC («nosotros», «nos» o «nuestro»), recopila, utiliza y comparte información cuando utiliza nuestra plataforma de gestión hotelera en hostliopro.com.</p>
<h2>1. Información que recopilamos</h2><p>Recopilamos la información que usted nos proporciona directamente, incluida:</p>
{ul(["Información de la cuenta: nombre, dirección de correo electrónico, número de teléfono, nombre del hotel, número de habitaciones","Información de pago: procesada de forma segura a través de Stripe (no almacenamos los datos de la tarjeta)","Datos del hotel: reservas, comunicaciones con los huéspedes, configuración de las habitaciones","Datos de uso: cómo interactúa con nuestra plataforma"])}
<h2>2. Cómo utilizamos su información</h2><p>Utilizamos la información que recopilamos para:</p>
{ul(["Prestar, mantener y mejorar nuestros servicios","Procesar pagos y enviar notificaciones de facturación","Enviar correos electrónicos transaccionales y novedades del producto","Responder a sus comentarios y preguntas","Supervisar y analizar patrones de uso para mejorar la experiencia del usuario","Cumplir con las obligaciones legales"])}
<h2>3. Información que compartimos</h2><p>No vendemos, intercambiamos ni alquilamos su información personal a terceros. Podemos compartir su información con:</p>
{ul(["<strong>Proveedores de servicios:</strong> Supabase (base de datos), Make.com (automatización), Stripe (pagos), Vercel (alojamiento), Anthropic (procesamiento de IA)","<strong>Channel managers:</strong> la API de Channex para la sincronización con las OTAs (Booking.com, Airbnb, etc.)","<strong>Requisitos legales:</strong> cuando lo exija la ley o para proteger nuestros derechos"])}
<h2>4. Seguridad de los datos</h2><p>Aplicamos medidas técnicas y organizativas adecuadas para proteger su información personal frente al acceso, la alteración, la divulgación o la destrucción no autorizados. Nuestra infraestructura cumple con SOC 2 a través de Supabase, y los pagos cumplen con PCI DSS a través de Stripe.</p>
<h2>5. Conservación de los datos</h2><p>Conservamos su información personal mientras su cuenta esté activa o durante el tiempo necesario para prestar los servicios. Puede solicitar la eliminación de sus datos en cualquier momento escribiéndonos a {EMAIL}.</p>
<h2>6. Derechos conforme al RGPD</h2><p>Si se encuentra en el Espacio Económico Europeo, tiene derecho a acceder a sus datos personales, rectificarlos o suprimirlos. También tiene derecho a la portabilidad de los datos y a oponerse a su tratamiento. Para ejercer estos derechos, escríbanos a {EMAIL}.</p>
<h2>7. WhatsApp y mensajería</h2><p>Nuestra plataforma se integra con la API de WhatsApp Business para facilitar la comunicación con los huéspedes. El contenido de los mensajes se procesa para generar respuestas de IA y no se utiliza con fines de marketing. Los números de teléfono de los huéspedes se almacenan únicamente con fines de comunicación.</p>
<h2>8. Cookies</h2><p>Utilizamos cookies esenciales para mantener su sesión y sus preferencias. No utilizamos cookies de seguimiento ni de publicidad. Puede controlar las cookies desde la configuración de su navegador.</p>
<h2>9. Enlaces de terceros</h2><p>Nuestra plataforma puede contener enlaces a sitios web de terceros. No somos responsables de las prácticas de privacidad de dichos sitios y le recomendamos que revise sus políticas de privacidad.</p>
<h2>10. Cambios en esta política</h2><p>Podemos actualizar esta Política de privacidad periódicamente. Le notificaremos cualquier cambio publicando la nueva política en esta página y actualizando la fecha de «Última actualización».</p>
<h2>11. Contacto</h2><p>Si tiene alguna pregunta sobre esta Política de privacidad, póngase en contacto con nosotros:</p>
{ul([f'Correo electrónico: <a href="mailto:{EMAIL}">{EMAIL}</a>', f"Dirección: {ADDR}"])}
<p>Para eliminar su cuenta, consulte <a href="/delete-account">Eliminar su cuenta</a>.</p>'''

def terms_body(U, EMAIL, ADDR, ul):
    pricing = U("pricing")
    privacy = U("privacy")
    return f'''<p>Estos Términos del servicio (los «Términos») rigen el uso que usted haga de Hostlio Pro, operado por Loti Members LLC (la «Empresa», «nosotros», «nos» o «nuestro»). Al acceder a nuestro servicio o utilizarlo, usted acepta quedar vinculado por estos Términos.</p>
<h2>1. Descripción del servicio</h2><p>Hostlio Pro es una plataforma de gestión hotelera en la nube que ofrece comunicación con los huéspedes basada en IA, gestión de canales, un calendario de planning de habitaciones y herramientas relacionadas de gestión hotelera. El servicio está disponible mediante suscripción en hostliopro.com.</p>
<h2>2. Registro de la cuenta</h2><p>Para utilizar Hostlio Pro, debe crear una cuenta y proporcionar información exacta y completa. Usted es responsable de mantener la confidencialidad de las credenciales de su cuenta y de todas las actividades que se realicen con ella.</p>
<h2>3. Suscripción y pagos</h2>
{ul(["Las suscripciones se facturan por adelantado, de forma mensual o anual","Todos los pagos se procesan de forma segura a través de Stripe","Prueba gratuita de 7 días disponible: se solicita un método de pago al registrarse, pero no se realiza ningún cargo hasta que finaliza la prueba","Tras la prueba, se le cobrará según el plan que haya seleccionado",f'Los precios están expresados en USD. Los planes y tarifas vigentes figuran en nuestra <a href="{pricing}">página de precios</a>',"Los planes anuales tienen un 20 % de descuento"])}
<h2>4. Cancelación y reembolsos</h2><p>Puede cancelar su suscripción en cualquier momento. La cancelación surte efecto al final del periodo de facturación en curso. No ofrecemos reembolsos por periodos de facturación parciales. Para cancelar, escríbanos a {EMAIL}.</p>
<h2>5. Uso aceptable</h2><p>Usted se compromete a no:</p>
{ul(["Utilizar el servicio con fines ilícitos","Infringir los términos de las plataformas OTA (Booking.com, Airbnb, etc.) a través de nuestras integraciones","Intentar obtener acceso no autorizado a nuestros sistemas","Enviar spam o mensajes no solicitados a los huéspedes","Revender o sublicenciar el servicio sin autorización por escrito"])}
<h2>6. Contenido generado por IA</h2><p>Hostlio Pro utiliza inteligencia artificial para generar respuestas a los mensajes de los huéspedes. Usted reconoce que el contenido generado por IA puede contener errores ocasionalmente. Usted es responsable de revisar y gestionar las respuestas de IA enviadas en nombre de su establecimiento. No somos responsables de ninguna inexactitud en las comunicaciones generadas por IA.</p>
<h2>7. Integraciones con canales OTA</h2><p>Nuestra plataforma se integra con canales OTA de terceros (Booking.com, Airbnb, Expedia, etc.) mediante la API de Channex. Usted es responsable de cumplir los términos del servicio de cada plataforma. No somos responsables de los cambios en las API o en las políticas de las OTAs que puedan afectar a la funcionalidad.</p>
<h2>8. Datos y privacidad</h2><p>El uso que usted haga de Hostlio Pro también se rige por nuestra <a href="{privacy}">Política de privacidad</a>, que se incorpora a estos Términos por referencia. Usted conserva la propiedad de sus datos. Tratamos sus datos únicamente para prestar el servicio.</p>
<h2>9. Disponibilidad del servicio</h2><p>Nos esforzamos por alcanzar una disponibilidad del 99,9 %, pero no garantizamos un servicio ininterrumpido. Podemos realizar tareas de mantenimiento programadas con aviso previo. No somos responsables de las pérdidas derivadas de interrupciones del servicio.</p>
<h2>10. Propiedad intelectual</h2><p>Hostlio Pro y todo el software, los diseños y el contenido relacionados son propiedad de Loti Members LLC. No puede copiar, modificar ni distribuir ninguna parte de nuestro servicio sin autorización por escrito.</p>
<h2>11. Limitación de responsabilidad</h2><p>En la máxima medida permitida por la ley, Loti Members LLC no será responsable de ningún daño indirecto, incidental, especial, consecuente o punitivo, incluida la pérdida de beneficios o de datos, derivado del uso que usted haga del servicio.</p>
<h2>12. Legislación aplicable</h2><p>Estos Términos se rigen por las leyes del Estado de California (EE. UU.). Cualquier controversia se resolverá ante los tribunales del condado de Sacramento, California.</p>
<h2>13. Cambios en los Términos</h2><p>Podemos actualizar estos Términos periódicamente. Le notificaremos los cambios importantes por correo electrónico o a través de la plataforma. El uso continuado del servicio tras los cambios constituye la aceptación de los nuevos Términos.</p>
<h2>14. Contacto</h2><p>Para cualquier pregunta sobre estos Términos, póngase en contacto con nosotros:</p>
{ul([f'Correo electrónico: <a href="mailto:{EMAIL}">{EMAIL}</a>', f"Dirección: {ADDR}"])}'''
