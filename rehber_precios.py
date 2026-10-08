"""Takvim yazısı (14 Ekim 2026 planı): "¿Cuánto cuesta un software de gestión hotelera? Precios 2026" — yalnız ES.
Rakamlar firmaların resmî fiyat sayfalarından / sayfadaki hesaplayıcının kendi verisinden, 9 Ekim 2026.
Belirsizler (Little Hotelier: erişim engelli, Smoobu: sayfa içi çelişki, Ulyses: yayın yok) bilerek dışarıda.
Hostlio SES.Hospedajes'e veri GÖNDERMEZ — metin bunu açıkça söyler. Fiyatlar ⟦token⟧ ile (pricing.py)."""
import html

SRC = [
 ("Sirvoy: Precios", "https://sirvoy.com/es/precios"),
 ("Beds24: Pricing", "https://beds24.com/pricing.html"),
 ("Hotelgest: Planes", "https://hotelgest.com/planes"),
 ("RoomRaccoon: Precios", "https://roomraccoon.es/precios/"),
 ("eviivo: Precios", "https://eviivo.com/es/precios/"),
 ("Octorate: Precios", "https://www.octorate.com/es/precios/"),
 ("Amenitiz: Precios", "https://www.amenitiz.com/es/precios/"),
 ("Avirato: Planes de pago", "https://avirato.com/planes-de-pago"),
 ("Cloudbeds: Precios", "https://www.cloudbeds.com/es/pricing/"),
 ("Mews: Pricing", "https://www.mews.com/en/pricing"),
 ("BOE: Real Decreto 933/2021", "https://www.boe.es/buscar/act.php?id=BOE-A-2021-17461"),
 ("La Moncloa: el Ministerio del Interior activa SES.Hospedajes (2 de diciembre de 2024)", "https://www.lamoncloa.gob.es/serviciosdeprensa/notasprensa/interior/paginas/2024/021224-registro-hospedaje-alquiler-vehiculos.aspx"),
]

def _tbl(head, rows, hl_col=None):
    hc = lambda i: ' class="hl"' if i == hl_col else ""
    h = "".join(f'<th scope="col"{hc(i)}>{x}</th>' for i, x in enumerate(head))
    b = "".join(("<tr class=\"hl\">" if r[0] == "Hostlio Pro" else "<tr>") + f'<th scope="row">{r[0]}</th>'
                + "".join(f"<td{hc(i)}>{c}</td>" for i, c in enumerate(r[1:], 1)) + "</tr>" for r in rows)
    return f'<div class="table-wrap"><table class="cmp"><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table></div>'

META = {"es": dict(key="post-cost", date="2026-10-09", title="¿Cuánto cuesta un software de gestión hotelera? Precios 2026",
                   desc="Precios 2026 de software de gestión hotelera en España: cuotas publicadas, coste para 10 y 25 habitaciones, extras ocultos y SES.Hospedajes.")}

def es(U):
    from build import btn, SIGNUP_URL
    cta = btn("Prueba gratis ⟦trial⟧ días", SIGNUP_URL) + btn("Ver planes", U("pricing"), "ghost")
    rows = [
      ("Hostlio Pro", "Cuota fija mensual por plan", "Starter ⟦price:starter⟧, Pro ⟦price:pro⟧, Growth ⟦price:growth⟧ al mes (USD, precio de lanzamiento); 20&nbsp;% de descuento anual", "Incluido en todos los planes"),
      ("Sirvoy", "Cuota por tramos de habitaciones", "Starter 22&nbsp;€ y Pro 79&nbsp;€ al mes de 6 a 10 habitaciones; 42&nbsp;€ y 149&nbsp;€ de 21 a 50; plan gratuito para 1 habitación", "Solo en Pro"),
      ("Beds24", "Pago por uso", "12,90&nbsp;€ de base + 2,60&nbsp;€ por habitación + 0,55&nbsp;€ por tipo de habitación y canal, al mes", "Por conexión (0,55&nbsp;€)"),
      ("Hotelgest", "Tramos por habitación, sin IVA", "55&nbsp;€ hasta 5 habitaciones; luego 9,50&nbsp;€ por habitación de la 6 a la 10 y 7,50&nbsp;€ de la 11 a la 20; alta 590&nbsp;€", "Extra: +30&nbsp;€ al mes"),
      ("RoomRaccoon", "Cuota según habitaciones", "Desde 164&nbsp;€ (Entry) hasta 435&nbsp;€ (Pro) al mes hasta 18 habitaciones, según su calculadora", "Incluido"),
      ("eviivo", "Desde, sin impuestos", "Desde 40&nbsp;€ al mes (un alojamiento); precio por volumen a partir de 10 habitaciones", "Incluido"),
      ("Octorate", "Por habitación", "Basic desde 8&nbsp;€ por habitación al mes; Pro y Ultimate a consultar", "Incluido en Basic"),
      ("Amenitiz, Avirato, Cloudbeds, Mews", "Presupuesto", "No publicado", "Según plan"),
    ]
    ex = [
      ("Hostlio Pro", "⟦price:starter⟧ (Starter)", "⟦price:pro⟧ (Pro)", "Ninguno; channel manager incluido"),
      ("Sirvoy Pro", "79&nbsp;€", "149&nbsp;€", "Sin contrato"),
      ("Beds24", "42,20&nbsp;€", "82,30&nbsp;€", "Supone 3 y 4 tipos de habitación, 2 OTAs"),
      ("Hotelgest + channel manager", "132,50&nbsp;€", "242,50&nbsp;€", "Sin IVA; alta única de 590&nbsp;€"),
      ("RoomRaccoon Entry", "164&nbsp;€", "228&nbsp;€", "Módulo legal (SES) desde Essential"),
    ]
    c = f'''<div class="answer"><p><strong>Respuesta corta:</strong> en 2026, un software de gestión hotelera (PMS) para un hotel pequeño en España cuesta entre unos 40&nbsp;€ y 250&nbsp;€ al mes entre los proveedores que publican sus precios. Para 10 habitaciones, las cuotas publicadas van de unos 42&nbsp;€ a 164&nbsp;€ al mes; para 25 habitaciones, de unos 82&nbsp;€ a 243&nbsp;€. Varios proveedores conocidos solo dan presupuesto. Antes de comparar, suma el channel manager, la puesta en marcha, el IVA y las comisiones por reserva: ahí está la diferencia real.</p></div>
<p class="small muted">Hostlio Pro es parte interesada en esta comparativa. Solo incluimos cifras que hemos comprobado en la web oficial de cada proveedor (o en la calculadora de esa misma página) el 9 de octubre de 2026. Los precios cambian; consulta siempre la página del proveedor antes de decidir. Las monedas son las que usa cada proveedor (€ o USD) y no se comparan directamente.</p>
<h2>Cuánto cuesta Hostlio Pro</h2>
<p>Hostlio Pro tiene tres planes con cuota fija: Starter ⟦price:starter⟧ al mes (hasta ⟦rooms:starter⟧ habitaciones), Pro ⟦price:pro⟧ (hasta ⟦rooms:pro⟧) y Growth ⟦price:growth⟧ (hasta ⟦rooms:growth⟧ habitaciones y 2 alojamientos). No cobra comisión por reserva ni porcentaje de ingresos, así que en temporada alta pagas lo mismo. El channel manager certificado (más de 100 OTAs) y Lio, el asistente con IA que responde a los huéspedes por WhatsApp, están incluidos en todos los planes. Con pago anual hay un 20&nbsp;% de descuento y puedes probarlo ⟦trial⟧ días gratis.</p>
<div class="cta-row" style="margin-top:12px">{cta}</div>
<h2>Los 4 modelos de precio</h2>
<ul><li><strong>Cuota fija mensual:</strong> pagas lo mismo cada mes. Es el modelo más fácil de presupuestar.</li>
<li><strong>Por habitación o por tramos:</strong> la cuota sube con el número de habitaciones. Barato para alojamientos muy pequeños; calcula también el escenario si amplías.</li>
<li><strong>Comisión sobre reservas:</strong> un porcentaje o un importe por reserva. Pagas poco en temporada baja, pero el coste crece justo en los mejores meses.</li>
<li><strong>Licencia única:</strong> pagas al principio; pregunta por actualizaciones, servidor y soporte.</li>
<li><strong>Presupuesto:</strong> el precio se da tras una demo, según tu alojamiento.</li></ul>
<h2>Precios publicados en 2026</h2>
{_tbl(["Software", "Modelo", "Precio publicado", "Channel manager"], rows)}
<h2>Ejemplo: hotel de 10 y de 25 habitaciones</h2>
<p>Cuota mensual calculada con los precios publicados y las calculadoras oficiales. En Beds24 el precio depende de los tipos de habitación y de los canales conectados; usamos 3 tipos para 10 habitaciones, 4 tipos para 25 y 2 OTAs en ambos casos. eviivo y Octorate no se incluyen porque su precio para estos tamaños no se puede determinar desde la web. Los programas no incluyen lo mismo: no decidas solo por la cifra.</p>
{_tbl(["Software", "10 habitaciones", "25 habitaciones", "Nota"], ex, hl_col=None)}
<h2>Costes que no se ven en la cuota</h2>
<ul><li><strong>Channel manager aparte:</strong> en algunos proveedores es un extra mensual o solo está en el plan superior.</li>
<li><strong>Alta y migración:</strong> pueden cobrarse una vez (por ejemplo, 590&nbsp;€ en Hotelgest).</li>
<li><strong>Comisión por reserva o por pago:</strong> pequeña por reserva, pero se acumula en temporada alta.</li>
<li><strong>IVA:</strong> muchos precios se publican sin IVA; algunos proveedores ni lo indican.</li>
<li><strong>Módulos:</strong> motor de reservas, limpieza, mensajería o el módulo legal pueden ir aparte.</li>
<li><strong>Comisiones de las OTAs:</strong> no dependen del software, pero suelen ser la partida más grande. Mira el neto por canal en la <a href="{U("commission")}">calculadora de comisiones OTA</a>.</li></ul>
<h2>SES.Hospedajes: pregunta antes de contratar</h2>
<p>Desde el 2 de diciembre de 2024, los alojamientos en España comunican los datos de los viajeros al Ministerio del Interior a través de SES.Hospedajes. El Real Decreto 933/2021 exige enviarlos de inmediato y, en todo caso, en menos de 24 horas, y conservarlos tres años. Algunos PMS los envían automáticamente (Hotelgest, Avirato, Octorate y RoomRaccoon desde su plan Essential lo indican en su web); otros lo resuelven con un socio como Chekin o con un fichero que subes tú.</p>
<p>Para ser claros: Hostlio Pro recoge y organiza los datos de los huéspedes con el <a href="{U("checkin")}">check-in online</a>, pero no los envía a SES.Hospedajes; la comunicación se hace por el canal oficial. Si el envío automático es imprescindible para ti, tenlo en cuenta al comparar.</p>
<h2>¿Qué modelo te conviene?</h2>
<ul><li><strong>Hostales, pensiones y casas rurales de hasta 10 habitaciones:</strong> una cuota fija baja con el channel manager incluido evita sorpresas.</li>
<li><strong>Hoteles de 10 a 50 habitaciones:</strong> compara el coste anual completo; las cuotas por habitación y los extras crecen rápido con el tamaño.</li>
<li><strong>Si tu ocupación es muy estacional:</strong> un modelo por reserva puede salir barato en invierno, pero calcula el año entero.</li></ul>
<p>Para los criterios de elección más allá del precio, lee <a href="{U("post-pms")}">cómo elegir software para hoteles pequeños</a>. Y para ver cuánto tiempo y comisiones puede ahorrarte un PMS, prueba la <a href="{U("roi")}">calculadora de ROI</a>.</p>
'''
    lis = "".join(f'<li><a href="{u}" rel="nofollow noopener">{html.escape(n)}</a></li>' for n, u in SRC)
    c += f'<h2>Fuentes</h2><p class="small muted">Todas las fuentes se consultaron el 9 de octubre de 2026. En Sirvoy, Beds24, Hotelgest y RoomRaccoon, los importes por número de habitaciones salen de la calculadora de su página oficial.</p><ul>{lis}</ul>'
    faq = [("¿Cuánto cuesta un software de gestión hotelera para un hotel pequeño?", "Entre los proveedores que publican precios, un hotel de 10 habitaciones paga entre unos 42&nbsp;€ y 164&nbsp;€ al mes (9 de octubre de 2026). A eso hay que sumar, según el proveedor, el channel manager, la puesta en marcha, el IVA y las comisiones por reserva. Algunos proveedores solo dan presupuesto."),
           ("¿El channel manager está incluido en el precio?", "Depende. En Hostlio Pro, RoomRaccoon, eviivo y Octorate Basic está incluido; en Sirvoy solo en el plan Pro; en Beds24 se paga por conexión y en Hotelgest es un extra de 30&nbsp;€ al mes."),
           ("¿Hostlio Pro envía los datos a SES.Hospedajes?", "No. Hostlio Pro recoge los datos de los huéspedes con el check-in online, pero no los envía a SES.Hospedajes; la comunicación se hace por el canal oficial."),
           ("¿Puedo probar Hostlio Pro gratis?", "Sí, ⟦trial⟧ días. Registras la tarjeta al darte de alta, pero no se cobra nada hasta que termina la prueba. Los planes cuestan ⟦price:starter⟧, ⟦price:pro⟧ y ⟦price:growth⟧ al mes.")]
    return c, faq

FN = {"es": es}
