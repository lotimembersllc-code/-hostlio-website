"""post-pms-vs-cm ES (rehber_pms_cm.en uyarlaması, 16 Ekim 2026)."""
import html

from rehber_pms_cm import _tbl, SRC

META_ES = dict(key="post-pms-vs-cm", date="2026-10-16", title="PMS o channel manager: ¿cuál es la diferencia? (2026)",
               desc="PMS o channel manager: qué hace cada uno, cómo trabajan juntos, cuánto cuestan y si un hotel pequeño necesita ambos. Con tabla comparativa y FAQ.")


def _src_es():
    lis = "".join(f'<li><a href="{u}" rel="nofollow noopener">{html.escape(n)}</a></li>' for n, u in SRC)
    return f'<h2>Fuentes</h2><p class="small muted">Consultadas el 8 de octubre de 2026.</p><ul>{lis}</ul>'


def es(U):
    t1 = _tbl(["", "PMS", "Channel manager"], [
        ("Función principal", "Gestiona la operativa diaria: calendario, habitaciones, huéspedes, informes", "Distribuye disponibilidad y tarifas a los canales e importa sus reservas"),
        ("Quién lo usa", "Recepción, pisos, dirección, contabilidad", "Funciona sobre todo en segundo plano; lo configura el propietario o el revenue manager"),
        ("Con quién se comunica", "Con tu equipo (y, mediante integraciones, con otras herramientas)", "Con las OTAs, los metabuscadores y otros canales de venta"),
        ("Sin él", "Las reservas viven en hojas de cálculo, extranets y papel", "Hay que actualizar la disponibilidad a mano en cada extranet"),
        ("Riesgo principal si falla", "Reservas perdidas o duplicadas, sin visión de conjunto", "Overbooking y tarifas distintas entre canales")])
    t2 = _tbl(["Configuración", "Cómo funciona", "Ideal para", "Ojo con"], [
        ("Solo PMS, sin channel manager", "Actualizas a mano la extranet de cada OTA", "Un solo canal, muy pocas habitaciones", "El riesgo de overbooking crece con cada canal que añades"),
        ("Channel manager independiente + PMS aparte", "Dos sistemas unidos por una interfaz", "Hoteles atados a un PMS que quieren conservar", "Dos facturas, dos servicios de soporte, doble mapeo, desfases de sincronización entre sistemas"),
        ("PMS con channel manager integrado", "Un sistema, un calendario", "La mayoría de los hoteles pequeños e independientes", "Comprueba qué canales están certificados y lo rápida que es la sincronización")])
    c = f"""<div class="answer"><p><strong>Respuesta corta:</strong> Un PMS (property management system, o software de gestión hotelera) gestiona el interior de tu hotel: el calendario de reservas, las habitaciones, los huéspedes, la limpieza y los informes. Un channel manager gestiona la conexión con el exterior: envía tu disponibilidad, tus tarifas y tus restricciones a Booking.com, Airbnb, Expedia y otros canales, y trae de vuelta sus reservas. Si vendes en más de un canal online, necesitas las dos funciones. Para un hotel pequeño, lo más sencillo suele ser un PMS con channel manager integrado: así solo hay un calendario y nada que mantener sincronizado entre dos sistemas.</p></div>
<h2>Qué hace un PMS</h2>
<p>El PMS es el sistema en el que vive tu recepción. Es el registro único de quién se aloja, en qué habitación, en qué fechas y a qué precio. Tareas típicas de un PMS:</p>
<ul><li><strong>Calendario de reservas (planning de habitaciones):</strong> todas las reservas en una línea de tiempo por habitación, con cambios de habitación, cambios de fechas y control de conflictos.</li>
<li><strong>Habitaciones y pisos:</strong> estado limpia, sucia o fuera de servicio y la lista de limpieza del día.</li>
<li><strong>Huéspedes:</strong> datos de contacto, datos del check-in, notas e historial de estancias. En España, esos datos son también la base del registro de viajeros; lo explicamos en nuestra <a href="{U('post-ses')}">guía sobre SES.HOSPEDAJES</a>.</li>
<li><strong>Reservas directas:</strong> teléfono, email, clientes que llegan sin reserva y huéspedes que repiten, introducidos por el personal.</li>
<li><strong>Informes:</strong> ocupación, ADR, RevPAR, ingresos y cancelaciones.</li></ul>
<h2>Qué hace un channel manager</h2>
<p>Un channel manager es un enlace de datos entre tu inventario y los sitios que lo venden. Funciona en dos direcciones:</p>
<ul><li><strong>Del hotel a los canales:</strong> disponibilidad (cuántas habitaciones de cada tipo se pueden vender), tarifas y restricciones como estancia mínima, cerrado a la llegada, cerrado a la salida y cierre de ventas (stop sell). En el sector se le llama ARI: availability, rates and inventory (disponibilidad, tarifas e inventario).</li>
<li><strong>De los canales al hotel:</strong> reservas nuevas, modificaciones y cancelaciones.</li></ul>
<p>Cuando la última habitación libre se vende en Airbnb, el channel manager recibe la reserva y envía “0 habitaciones” para esas fechas a Booking.com y Expedia, normalmente en cuestión de segundos. Eso es lo que evita la mayoría de las dobles reservas; consulta nuestra guía sobre <a href="{U('post-overbooking')}">cómo evitar el overbooking</a>.</p>
<h2>PMS frente a channel manager, de un vistazo</h2>
{t1}
<h2>Cómo trabajan juntos</h2>
<p>Piensa en el PMS como la fuente de la verdad y en el channel manager como el mensajero. Un flujo típico:</p>
<ol><li>Un huésped reserva una habitación doble en Booking.com del 12 al 14 de mayo.</li>
<li>El channel manager recibe la reserva y la pasa al PMS, donde aparece en el planning de habitaciones.</li>
<li>El PMS recalcula la disponibilidad de habitaciones dobles para esas fechas.</li>
<li>El channel manager envía la nueva disponibilidad a todos los demás canales conectados.</li>
<li>Cuando más tarde cambias una tarifa o cierras una fecha en el PMS, el mismo camino se recorre a la inversa.</li></ol>
<p>Los puntos débiles son los traspasos. Si el PMS y el channel manager son de proveedores distintos, necesitan una interfaz entre ellos, y cada tipo de habitación y cada plan tarifario hay que mapearlos dos veces: una entre el canal y el channel manager, y otra entre el channel manager y el PMS.</p>
<h2>Tres formas de organizarlo</h2>
{t2}
<h2>¿Necesitas los dos?</h2>
<ul><li><strong>Solo vendes en directo y en una OTA:</strong> para empezar basta con un PMS; cerrar fechas a mano en una sola extranet es manejable.</li>
<li><strong>Vendes en dos o más canales online:</strong> necesitas la función de channel manager. Actualizar varias extranets a mano es la causa más habitual de overbooking en los hoteles independientes.</li>
<li><strong>Ya usas un PMS que te gusta:</strong> comprueba si tiene channel manager propio o una integración certificada con uno antes de añadir un segundo proveedor.</li>
<li><strong>Eliges desde cero:</strong> un PMS con channel manager integrado te ahorra por completo la capa de integración. Nuestra guía para <a href="{U('post-pms')}">elegir software de gestión para un hotel pequeño</a> recoge los demás criterios, y en nuestra <a href="{U('post-mejorespms')}">comparativa de PMS en España</a> puedes ver las opciones lado a lado.</li></ul>
<h2>Cuánto cuesta</h2>
<p>Los channel managers se cobran de varias formas, y algunos proveedores de PMS solo lo incluyen en sus planes superiores. Dos ejemplos tomados de las páginas de precios de los propios proveedores (8 de octubre de 2026):</p>
<ul><li><strong>Por habitación y por conexión:</strong> Beds24 cobra una cuota base, una cuota por habitación y una cuota por tipo de habitación por cada conexión de canal; su página de precios indica “desde 15,50 €” al mes.</li>
<li><strong>Solo en un plan superior:</strong> Sirvoy ofrece un plan gratuito para una habitación y un plan Starter, pero el channel manager solo figura en su plan Pro (79 € al mes para hasta 10 habitaciones, con pago mensual).</li></ul>
<p>Otros modelos cobran un porcentaje de los ingresos por reservas o una cuota por reserva, que crece en temporada alta. Al comparar, suma el PMS, el channel manager y cualquier cuota por reserva, y luego comprueba lo que de verdad te deja cada canal después de la comisión con nuestra <a href="{U('commission')}">calculadora de comisiones de OTAs</a>.</p>
<h2>Preguntas que hacer antes de decidir</h2>
<ol><li>¿Qué canales están conectados y están esas conexiones certificadas por los propios canales?</li>
<li>¿La sincronización es en tiempo real o programada? ¿Qué pasa si un canal se cae?</li>
<li>¿Las tarifas y las restricciones (estancia mínima, cerrado a la llegada o a la salida, cierre de ventas) llegan a todos los canales, o solo la disponibilidad?</li>
<li>¿Las modificaciones y cancelaciones vuelven automáticamente?</li>
<li>Cuando una habitación está fuera de servicio, ¿baja también la disponibilidad en los canales?</li>
<li>¿Quién mapea los tipos de habitación y los planes tarifarios en la puesta en marcha, y está incluida esa ayuda?</li>
<li>¿El precio es fijo o depende de las habitaciones, los canales o las reservas?</li></ol>
<h2>Cómo funciona en Hostlio Pro</h2>
<p>Hostlio Pro es un PMS con el <a href="{U('channel')}">channel manager</a> integrado, en todos los planes. Las conexiones con más de 100 canales, entre ellos Booking.com, Airbnb, Expedia, Agoda, Trip.com y Google Hotels, funcionan mediante enlaces certificados a través de Channex, así que las reservas, modificaciones y cancelaciones llegan al mismo planning de habitaciones en el que trabajas. Una sola cuadrícula reúne precio, estancia mínima y máxima, cerrado a la llegada, cerrado a la salida y cierre de ventas para cada tipo de habitación y plan tarifario, y puedes introducir una temporada entera por rango de fechas. Cuando pones una habitación fuera de servicio, la disponibilidad baja automáticamente en los canales. Los análisis muestran los ingresos brutos, la comisión y el neto de cada canal.</p>
<p>No hay cuota por reserva ni porcentaje sobre los ingresos: Starter cuesta ⟦price:starter⟧ al mes, Pro ⟦price:pro⟧ y Growth ⟦price:growth⟧, con una prueba gratuita de 7 días. Consulta los <a href="{U('pricing')}">precios</a> para ver los límites de habitaciones y lo que incluye cada plan.</p>"""
    c += _src_es()
    faq = [("¿El channel manager forma parte de un PMS?", "A veces. Muchos PMS incluyen un channel manager, otros se integran con uno independiente y algunos solo lo incluyen en los planes superiores. Revisa los detalles del plan, no solo la lista de funciones."),
           ("¿Puedo usar un channel manager sin PMS?", "Sí, muchos channel managers independientes tienen un calendario básico. Aun así, necesitarás un sitio donde gestionar habitaciones, huéspedes, limpieza e informes, que es el trabajo de un PMS."),
           ("¿Un channel manager evita todos los overbookings?", "La sincronización bidireccional en tiempo real elimina la mayor parte del riesgo. Las reservas directas introducidas tarde, los mapeos de habitaciones erróneos y los canales que no responden temporalmente todavía pueden causar problemas."),
           ("¿El channel manager está incluido en todos los planes de Hostlio Pro?", "Sí. Starter, Pro y Growth incluyen el channel manager con más de 100 canales. No hay cuotas por reserva.")]
    return c, faq
