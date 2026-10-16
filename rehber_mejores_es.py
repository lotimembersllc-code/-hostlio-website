"""Takvim yazısı (28 Ekim planı, öne alındı): "Los mejores PMS para hoteles pequeños en España (2026)" — yalnız ES.
Veriler 9 Ekim 2026 resmî siteler (post-cost araştırması): Avirato, Hotelgest, RoomRaccoon, Octorate, Amenitiz, Cloudbeds, Mews,
Sirvoy, Beds24, eviivo, Smoobu. SES iddiaları firmaların kendi sayfalarından ("dicen"); Little Hotelier (erişim yok) ve Ulyses
(fiyat/SES bilgisi yok) dışarıda. post-cost (fiyat) ve post-pms (kriter) ile rol ayrımı: ürün ürün karşılaştırma + SES."""
import html

SRC = [
 ("Avirato: planes de pago", "https://avirato.com/planes-de-pago"),
 ("Avirato: integración con la Policía (SES.Hospedajes)", "https://avirato.com/integraciones/policia-nacional/"),
 ("Hotelgest: planes", "https://hotelgest.com/planes"),
 ("RoomRaccoon: precios", "https://roomraccoon.es/precios/"),
 ("Octorate: precios", "https://www.octorate.com/es/precios/"),
 ("Octorate: SES.Hospedajes", "https://octorate.com/es/ses-hospedajes/"),
 ("Amenitiz: precios", "https://www.amenitiz.com/es/precios/"),
 ("Amenitiz: activar Chekin en España", "https://support.amenitiz.com/en/articles/332535-how-to-activate-and-connect-chekin-in-spain"),
 ("Cloudbeds: precios", "https://www.cloudbeds.com/es/pricing/"),
 ("Mews: pricing", "https://www.mews.com/en/pricing"),
 ("Sirvoy: precios", "https://sirvoy.com/es/precios"),
 ("Beds24: pricing", "https://beds24.com/pricing.html"),
 ("eviivo: precios", "https://eviivo.com/es/precios/"),
 ("Smoobu: precios", "https://www.smoobu.com/es/precios/"),
]

def _tbl(head, rows):
    h = "".join(f'<th scope="col">{x}</th>' for x in head)
    b = "".join(("<tr class=\"hl\">" if r[0] == "Hostlio Pro" else "<tr>") + f'<th scope="row">{r[0]}</th>'
                + "".join(f"<td>{c}</td>" for c in r[1:]) + "</tr>" for r in rows)
    return f'<div class="table-wrap"><table class="cmp"><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table></div>'

META = {"es": dict(key="post-mejorespms", date="2026-10-16", title="Los mejores PMS para hoteles pequeños en España (2026)",
                   desc="Comparamos 12 PMS para hoteles pequeños, hostales y casas rurales en España: channel manager, SES.Hospedajes, precio y prueba. Fuentes oficiales.")}

def es(U):
    from build import btn, SIGNUP_URL
    cta = btn("Prueba gratis ⟦trial⟧ días", SIGNUP_URL) + btn("Ver planes", U("pricing"), "ghost")
    rows = [
      ("Hostlio Pro", "PMS + channel manager + asistente IA", "No envía (recoge datos con check-in online)", "Precio fijo publicado: ⟦price:starter⟧ / ⟦price:pro⟧ / ⟦price:growth⟧ al mes (USD)", "⟦trial⟧ días"),
      ("Avirato (ES)", "PMS con channel manager en todos los planes", "Dice enviar los partes automáticamente", "Presupuesto según unidades", "20 días, sin tarjeta"),
      ("Hotelgest (ES)", "PMS; channel manager como extra", "Incluido en el plan base, según su web", "Desde 55&nbsp;€/mes sin IVA; alta de 590&nbsp;€", "No indicado"),
      ("RoomRaccoon", "Suite con channel manager", "Envío automático desde el plan Essential", "Desde 164&nbsp;€/mes (Entry, sin módulo legal)", "No indicado"),
      ("Octorate", "Suite; Basic sin PMS", "Conectado por servicio web, según su web", "Basic desde 8&nbsp;€ por habitación", "14 días"),
      ("Amenitiz", "Todo en uno", "Mediante Chekin (marketplace)", "Precio a petición", "No indicado"),
      ("Cloudbeds", "Plataforma", "Tiene artículo de ayuda sobre SES (no verificado)", "Presupuesto", "No indicado"),
      ("Mews", "Plataforma", "Integración con herramientas como Chekin vía API", "Presupuesto", "No indicado"),
      ("eviivo", "Suite para pequeños alojamientos", "Mediante el socio Check-in Scan", "Desde 40&nbsp;€/mes sin impuestos", "14 días"),
      ("Sirvoy", "PMS; channel manager solo en Pro", "No lo menciona", "Pro 79&nbsp;€/mes hasta 10 habitaciones", "14 días, sin tarjeta"),
      ("Beds24", "PMS + channel manager por uso", "No lo menciona", "12,90&nbsp;€ + 2,60&nbsp;€ por habitación + 0,55&nbsp;€ por conexión", "Gratis"),
      ("Smoobu", "Sobre todo alquiler vacacional", "Mediante el socio Chekin", "Desde 29&nbsp;€/mes + 0,9% por reserva", "14 días"),
    ]
    c = f'''<div class="answer"><p><strong>Respuesta corta:</strong> no hay un "mejor PMS" para todos. Para un hotel pequeño, hostal o casa rural en España, los que conviene comparar en 2026 son los que incluyen channel manager, resuelven SES.Hospedajes (enviando los partes o con un socio) y publican un precio que puedas comprobar. Entre los españoles destacan Avirato y Hotelgest, que dicen enviar los partes a SES; entre los internacionales, RoomRaccoon, Octorate y eviivo publican precios. Hostlio Pro es la opción con precio fijo y asistente de IA en WhatsApp, pero no envía los partes a SES.</p></div>
<p class="small muted">Hostlio Pro es uno de los productos comparados, así que no somos neutrales. Solo usamos información publicada en las webs oficiales de cada proveedor, consultadas el 9 de octubre de 2026; lo que dicen sobre SES.Hospedajes es su propia afirmación y no hemos comprobado cómo funciona cada envío. Los precios cambian: revisa siempre la web del proveedor.</p>
<h2>Cómo hemos comparado</h2>
<p>Para un alojamiento de 5 a 40 habitaciones miramos cinco cosas: si el <a href="{U("channel")}">channel manager</a> está incluido, cómo se resuelve <a href="{U("post-ses")}">SES.Hospedajes</a> (envío directo, socio o nada), si el precio es público, si hay prueba gratuita y para qué tipo de alojamiento está pensado. Los precios en detalle están en <a href="{U("post-cost")}">cuánto cuesta un software de gestión hotelera</a> y los criterios generales en <a href="{U("post-pms")}">cómo elegir software para hoteles pequeños</a>.</p>
<h2>Tabla comparativa</h2>
{_tbl(["PMS", "Qué es", "SES.Hospedajes", "Precio", "Prueba"], rows)}
<h2>Los PMS uno por uno</h2>
<h3>Hostlio Pro</h3>
<p>PMS, channel manager certificado (más de 100 OTAs) y Lio, un asistente de IA que responde a los huéspedes por WhatsApp en su idioma, en todos los planes; en Pro y Growth también las bandejas de Booking.com, Airbnb y Expedia y el <a href="{U("checkin")}">check-in online</a>. Precio fijo publicado y sin comisiones. Lo que no hace: no envía los partes a SES.Hospedajes, no emite facturas con Verifactu y no tiene motor de reservas ni cobro online. Si el envío automático a SES es imprescindible para ti, tenlo en cuenta.</p>
<div class="cta-row" style="margin-top:12px">{cta}</div>
<h3>Avirato</h3>
<p>PMS español con channel manager en todos los planes. Afirma que los partes "se envían automáticamente a través de SES Hospedajes" y que las integraciones no tienen coste extra. Trabaja con presupuesto según el número de unidades y ofrece 20 días de prueba sin tarjeta.</p>
<h3>Hotelgest</h3>
<p>PMS español que publica su tarifa por tramos de habitaciones (desde 55&nbsp;€ al mes sin IVA hasta 5 habitaciones) e incluye en el plan base SES.Hospedajes, Verifactu y TicketBAI, según su web. El channel manager es un extra de 30&nbsp;€ al mes y hay un alta única de 590&nbsp;€.</p>
<h3>RoomRaccoon</h3>
<p>Suite con channel manager incluido y envío automático diario a la policía desde el plan Essential. El plan Entry (desde 164&nbsp;€ al mes) no incluye el módulo legal y limita a 3 canales.</p>
<h3>Octorate</h3>
<p>Suite italiana que dice estar conectada a SES.Hospedajes por servicio web. Su plan Basic (desde 8&nbsp;€ por habitación) incluye channel manager y motor de reservas pero no el PMS, que está en los planes superiores con presupuesto.</p>
<h3>Amenitiz, Cloudbeds y Mews</h3>
<p>Tres plataformas con presupuesto. Amenitiz resuelve SES mediante Chekin, que se activa desde su marketplace; Mews permite integrar herramientas como Chekin por API; Cloudbeds tiene un artículo de ayuda sobre la conexión con SES que no hemos podido verificar.</p>
<h3>eviivo, Sirvoy, Beds24 y Smoobu</h3>
<p><strong>eviivo</strong> parte de 40&nbsp;€ al mes y resuelve SES con el socio Check-in Scan. <strong>Sirvoy</strong> y <strong>Beds24</strong> son económicos y publican precios, pero no mencionan SES; en Sirvoy el channel manager solo está en el plan Pro. <strong>Smoobu</strong> está pensado sobre todo para alquiler vacacional y usa Chekin para SES.</p>
<h2>¿Cuál te conviene?</h2>
<ul><li><strong>Casa rural u hostal de pocas habitaciones:</strong> precio fijo bajo, channel manager incluido y una solución clara para SES, aunque sea con un socio.</li>
<li><strong>Hotel independiente de 10 a 40 habitaciones:</strong> prioriza la fiabilidad de la sincronización con las OTAs, una bandeja de mensajes única y el coste anual completo con módulos.</li>
<li><strong>Si el envío automático a SES es imprescindible:</strong> pide una demostración del envío con datos reales antes de contratar.</li></ul>
'''
    lis = "".join(f'<li><a href="{u}" rel="nofollow noopener">{html.escape(n)}</a></li>' for n, u in SRC)
    c += f'<h2>Fuentes</h2><p class="small muted">Todas las fuentes se consultaron el 9 de octubre de 2026.</p><ul>{lis}</ul>'
    faq = [("¿Cuál es el mejor PMS para un hotel pequeño en España?", "Depende de tu tamaño y de cómo quieras resolver SES.Hospedajes. Compara si incluye channel manager, si envía los partes a SES (directamente o con un socio), si el precio es público y si puedes probarlo gratis."),
           ("¿Qué PMS envían los partes a SES.Hospedajes?", "Según sus propias webs, Avirato, Hotelgest, RoomRaccoon (desde el plan Essential) y Octorate dicen enviarlos; Amenitiz, Smoobu y eviivo lo resuelven con socios como Chekin o Check-in Scan. Pide siempre una demostración."),
           ("¿Hostlio Pro envía los partes a SES.Hospedajes?", "No. El check-in online de Hostlio Pro recoge y ordena los datos del huésped antes de la llegada, pero la comunicación a Interior la haces tú."),
           ("¿Cuánto cuesta Hostlio Pro?", "Starter ⟦price:starter⟧, Pro ⟦price:pro⟧ y Growth ⟦price:growth⟧ al mes (USD), con un 20% de descuento en el pago anual y ⟦trial⟧ días de prueba gratis.")]
    return c, faq

FN = {"es": es}
