"""Takvim yazısı (21 Ekim 2026 planı): "SES.Hospedajes: guía 2026" — yalnız ES.
Resmî kaynaklar 13 Ekim 2026: RD 933/2021 (art. 2, 4, 5, 6, Anexo I), LO 4/2015 (art. 25, 36.20, 37.9, 39.1), Interior SSS
(10.08.2026), Interior sede, La Moncloa (2.12.2024), Mossos/Ertzaintza. Supremo kararları RD 1312/2024 hakkında (SES değil).
Hostlio SES'e GÖNDERMEZ (FAQ 22'ye göre yetkili üçüncü taraf gönderebilir ama Hostlio bunu yapmıyor)."""
import html

SRC = [
 ("BOE: Real Decreto 933/2021", "https://www.boe.es/buscar/act.php?id=BOE-A-2021-17461"),
 ("BOE: Ley Orgánica 4/2015 de protección de la seguridad ciudadana", "https://www.boe.es/buscar/act.php?id=BOE-A-2015-3442"),
 ("Ministerio del Interior: preguntas frecuentes (actualizadas el 10/08/2026)", "https://sede.interior.gob.es/portal/dam/jcr:995aad35-2632-4de2-97fe-94cc2489c9c6/Preguntas-frecuentes-hospedajes-alquiler-vehiculos-20260810.pdf"),
 ("Sede del Ministerio del Interior: información sobre hospedajes", "https://sede.interior.gob.es/portal/sede/informacion_hospedajes"),
 ("Sede del Ministerio del Interior: guía visual de Hospedajes", "https://sede.interior.gob.es/portal/dam/jcr:01a016b6-5ec0-41b4-898c-7f77b2f16e7d/Guia-visual-de-Hospedajes-v.29.08.2025.pdf"),
 ("La Moncloa: Interior activa el registro de hospedajes (2/12/2024)", "https://www.lamoncloa.gob.es/serviciosdeprensa/notasprensa/interior/Paginas/2024/021224-registro-hospedaje-alquiler-vehiculos.aspx"),
 ("Mossos d'Esquadra: Registre de viatgers", "https://registreviatgers.mossos.gencat.cat/mossos_hotels/AppJava/faqs.do?reqCode=init"),
 ("Euskadi: registro hostelero de la Ertzaintza", "https://www.euskadi.eus/comunicacion/registro-hostelero/web01-tramite/es/"),
]

def _tbl(head, rows):
    h = "".join(f'<th scope="col">{x}</th>' for x in head)
    b = "".join("<tr>" + f'<th scope="row">{r[0]}</th>' + "".join(f"<td>{c}</td>" for c in r[1:]) + "</tr>" for r in rows)
    return f'<div class="table-wrap"><table class="cmp"><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table></div>'

META = {"es": dict(key="post-ses", date="2026-10-13", title="SES.Hospedajes: guía 2026 para hoteles y viviendas turísticas",
                   desc="SES.Hospedajes en 2026: quién debe comunicar, plazos de 24 horas, datos del viajero y del pago, cómo darse de alta, Cataluña y País Vasco, y sanciones.")}

def es(U):
    from build import btn, SIGNUP_URL
    cta = btn("Prueba gratis ⟦trial⟧ días", SIGNUP_URL) + btn("Ver el check-in online", U("checkin"), "ghost")
    plazos = _tbl(["Qué", "Cuándo", "Base"], [
        ("Alta del establecimiento", "En 10 días desde completar los trámites administrativos y, en todo caso, antes de empezar la actividad", "RD 933/2021, art. 6.1–6.2"),
        ("Comunicación de la reserva (o su anulación)", "De inmediato y, como máximo, en 24 horas", "RD 933/2021, art. 6.3.a"),
        ("Parte de entrada (inicio del servicio)", "De inmediato y, como máximo, en 24 horas desde la llegada", "RD 933/2021, art. 6.3.b"),
        ("Cambios en los datos comunicados", "Nueva comunicación", "FAQ de Interior, n.º 26"),
        ("Conservación del registro", "3 años desde el fin del servicio", "RD 933/2021, art. 5")])
    multas = _tbl(["Infracción", "Ejemplos", "Multa"], [
        ("Leve (LO 4/2015, art. 37.9)", "Errores, datos falsos, omisiones parciales o envío fuera de plazo", "100 a 600&nbsp;€"),
        ("Grave (LO 4/2015, art. 36.20)", "No tener el registro o no hacer las comunicaciones obligatorias", "601 a 30.000&nbsp;€")])
    c = f'''<div class="answer"><p><strong>Respuesta corta:</strong> desde el 2 de diciembre de 2024, quien aloja viajeros en España a cambio de un precio (hoteles, hostales, casas rurales, campings, apartamentos y también particulares con viviendas turísticas) debe comunicar al Ministerio del Interior, a través de <strong>SES.Hospedajes</strong>, dos cosas: la <strong>reserva</strong> (o su anulación) y la <strong>entrada</strong> de los viajeros, en ambos casos de inmediato y como máximo en 24 horas. Los datos incluyen la identidad, el contacto y el medio de pago, y hay que conservarlos tres años. Las multas van de 100 a 30.000&nbsp;€.</p></div>
<p class="small muted">Esta guía es informativa y no es asesoramiento jurídico. Se basa en el Real Decreto 933/2021, la Ley Orgánica 4/2015, las preguntas frecuentes del Ministerio del Interior (actualizadas el 10 de agosto de 2026) y otras fuentes oficiales consultadas el 13 de octubre de 2026. Para tu caso concreto, consulta la sede del Ministerio del Interior o a un profesional.</p>
<h2>Qué es SES.Hospedajes</h2>
<p>SES.Hospedajes es la plataforma del Ministerio del Interior para el registro documental de las actividades de hospedaje. La obligación nace de la Ley Orgánica 4/2015, que considera el hospedaje una actividad relevante para la seguridad ciudadana, y se desarrolla en el Real Decreto 933/2021. Las obligaciones de comunicación tenían efecto desde 2023, pero tras varias moratorias Interior activó el sistema el 2 de diciembre de 2024. Sustituye al antiguo parte de viajeros, con muchos más datos.</p>
<h2>Quién está obligado</h2>
<p>El Real Decreto se aplica a quien ofrece hospedaje a cambio de un precio, sea profesional o no:</p>
<ul><li>Hoteles, hostales, pensiones, casas de huéspedes y turismo rural</li>
<li>Campings, zonas de autocaravanas, apartamentos, bungalós y alojamientos similares</li>
<li>Particulares que alquilan viviendas o habitaciones a viajeros (también las viviendas de uso turístico)</li>
<li>Operadores turísticos que intermedian y plataformas digitales que ofrecen servicios en España</li></ul>
<p>Según las preguntas frecuentes de Interior, también cuentan las estancias largas que no son vivienda habitual, y los albergues si los huéspedes pagan. Cuando hay varios intermediarios, el obligado es quien tiene la relación contractual directa y final con el cliente.</p>
<h2>Plazos: 24 horas para la reserva y para la entrada</h2>
{plazos}
<p>El parte de entrada lo firman todos los viajeros mayores de 14 años; los datos de los menores de 14 los aporta el adulto que los acompaña.</p>
<h2>Qué datos hay que comunicar</h2>
<p>Además de los datos del antiguo parte, el Real Decreto pide:</p>
<ul><li><strong>Viajeros:</strong> nombre y apellidos, sexo, tipo y número de documento (y número de soporte en los establecimientos profesionales), nacionalidad, fecha de nacimiento, dirección de residencia, teléfono y correo electrónico, número de viajeros y, si hay menores, la relación de parentesco.</li>
<li><strong>Contrato:</strong> referencia, fecha, fechas y horas de entrada y salida, dirección del alojamiento, número de habitaciones y si hay conexión a Internet.</li>
<li><strong>Pago:</strong> tipo de pago, identificación del medio (por ejemplo, tarjeta, IBAN o pago móvil), titular, caducidad de la tarjeta y fecha del pago.</li></ul>
<p>Las preguntas frecuentes aclaran que basta un móvil si no hay correo, que el sexo solo se indica si consta en el documento o lo facilita el viajero y que, si un menor viaja con un adulto que no es su progenitor, hay que indicar la relación (tutor, profesor, monitor).</p>
<h2>Cómo darse de alta y comunicar</h2>
<ol><li><strong>Alta del establecimiento</strong> en la sede electrónica del Ministerio del Interior, con certificado digital o Cl@ve, firmando la solicitud.</li>
<li><strong>Credenciales:</strong> recibes unas para la aplicación web y otras distintas para el envío automático mediante servicio web.</li>
<li><strong>Comunicaciones:</strong> por formulario web, por lotes o mediante el servicio web de tu software, si lo tiene. La documentación técnica del servicio web se descarga dentro de la plataforma.</li>
<li><strong>Terceros:</strong> un tercero, por ejemplo un proveedor de software, puede enviar los datos si lo autorizas.</li>
<li><strong>Guarda tu propio registro:</strong> según las preguntas frecuentes actualizadas, Interior no facilita listados de las comunicaciones enviadas, ni siquiera al propio obligado.</li></ol>
<h2>Cataluña y País Vasco</h2>
<p>En Cataluña, los Mossos d'Esquadra tienen su propio Registre de viatgers (alta por establecimiento con el formulario PI-15, comunicación en 24 horas y conservación de 3 años), y en Euskadi la Ertzaintza tiene su servicio de registro hostelero. Si tu alojamiento está en una de estas comunidades, consulta con los Mossos o la Ertzaintza cómo se coordina su sistema con SES.Hospedajes.</p>
<h2>Sanciones</h2>
{multas}
<h2>Qué no hay que confundir</h2>
<ul><li><strong>Registro único de arrendamientos:</strong> es otra norma (RD 1312/2024). Las sentencias del Tribunal Supremo de mayo y junio de 2026 se refieren a ese registro, no a SES.Hospedajes.</li>
<li><strong>Reglamento europeo 2024/1028:</strong> se aplica desde el 20 de mayo de 2026 y trata del número de registro de los anfitriones y del intercambio de datos de las plataformas; no sustituye el registro de viajeros.</li></ul>
<h2>Cómo te ayuda Hostlio Pro (y qué no hace)</h2>
<p>Con el <a href="{U("checkin")}">check-in online</a> de Hostlio Pro, el huésped rellena sus datos antes de llegar y puede escanear su documento con el móvil: la lectura se hace en el dispositivo y no se guarda ninguna imagen. Así, en recepción ya tienes los datos ordenados. Para ser claros: <strong>Hostlio Pro no envía los datos a SES.Hospedajes</strong> ni actúa como tercero autorizado; la comunicación sigue siendo tuya, por la sede de Interior o con otra herramienta.</p>
<div class="cta-row" style="margin-top:12px">{cta}</div>
<p>Si estás eligiendo programa, mira también <a href="{U("post-cost")}">cuánto cuesta un software de gestión hotelera</a> y <a href="{U("post-pms")}">cómo elegir software para hoteles pequeños</a>.</p>
'''
    lis = "".join(f'<li><a href="{u}" rel="nofollow noopener">{html.escape(n)}</a></li>' for n, u in SRC)
    c += f'<h2>Fuentes</h2><p class="small muted">Todas las fuentes se consultaron el 13 de octubre de 2026.</p><ul>{lis}</ul>'
    faq = [("¿Qué plazo hay para comunicar a SES.Hospedajes?", "De inmediato y, como máximo, en 24 horas: desde la reserva (o su anulación) para la comunicación de la reserva, y desde la llegada para el parte de entrada (RD 933/2021, art. 6.3)."),
           ("¿Los particulares con vivienda turística también deben comunicar?", "Sí. El Real Decreto 933/2021 se aplica a quien ofrece hospedaje a cambio de un precio, sea profesional o no; las preguntas frecuentes de Interior lo confirman."),
           ("¿Qué multa hay si no comunico a SES.Hospedajes?", "No tener el registro o no hacer las comunicaciones es infracción grave (601 a 30.000 €); los errores, los datos falsos o el envío fuera de plazo son leves (100 a 600 €), según la Ley Orgánica 4/2015."),
           ("¿Cuánto tiempo hay que conservar los datos?", "Tres años desde el fin del servicio, en un registro informático (RD 933/2021, art. 5)."),
           ("¿Hostlio Pro envía los datos a SES.Hospedajes?", "No. El check-in online de Hostlio Pro recoge y ordena los datos del huésped antes de la llegada, pero la comunicación a Interior la haces tú, por la sede electrónica o con otra herramienta.")]
    return c, faq

FN = {"es": es}
