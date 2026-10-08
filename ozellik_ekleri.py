"""Özellik boşlukları, ilk dalga (WEB_SITE_DUZELTMELER.md bölüm 2; 8 Ekim 2026).
Gap #1–#5, #7–#14, #18, #20, #25 için 6 dilde ortak metinler. İçerik sayfaları (content_<dil>.py) ve
güvenlik/ana sayfa bu tabloyu okur; böylece metin tek yerde, HTML şablonu sayfalarda kalır.
Doğrulama: ürün kodu (panel + backend) 8 Ekim okundu. Bilerek YAZILMAYANLAR: 300 oda (plan sınırı 150),
oda rafında blokaj, yatak bazlı satış, otomatik KBS/SES gönderimi, WhatsApp Coexistence (#17), mobil plan
ifadesi (A4). Mobil uygulamaya özgü kısımlar yalnız sabah özeti (Android canlı, iOS sonraki güncellemede)."""

FX = {
"en": dict(
  more_h="Run the whole day from one dashboard",
  more_p="Beyond messaging and distribution, these are the tools your team uses every day. All of them are in the web dashboard and included in every plan unless noted.",
  groups=[
   ("Daily operations", [
    ("Today screen", "Open the dashboard in the morning and the day is already laid out: arrivals, departures, rooms to clean, messages waiting for a reply, Lio drafts waiting for your approval, booking requests and reviews to answer."),
    ("Housekeeping", "Every room has a status: clean, dirty, maintenance or out of order. Today’s departures come first, and a room with a same-day arrival is marked high priority. Print the day’s housekeeping list as a PDF; housekeepers with the housekeeping role only see rooms."),
    ("Maintenance and out-of-order rooms", "Report a fault with up to five photos (location data is removed), a category and a priority. Take a room out of order and it leaves sale: availability drops on your connected channels automatically, the room can’t be assigned to a booking and your team is notified."),
    ("A room rack that scales", "For larger properties: three density levels, rooms grouped by type or floor, a daily free-room count, a free-room search and 7, 14 or 30-day views. The conflict check lists double-booked and unassigned reservations, the rack suggests a free room of the right type, and bookings move with the mouse or the keyboard."),
    ("Notifications and morning summary", "New, changed and cancelled bookings, messages waiting for a reply, drafts to approve, channel issues and maintenance reports land in one notification centre, kept for 90 days. The mobile app also sends a summary of the day at 08:00 hotel time (Android today, iOS with the upcoming app update)."),
   ]),
   ("Revenue, rates and reports", [
    ("Analytics", "Occupancy, ADR, RevPAR, revenue, length of stay, cancellations and no-shows, compared with the previous period. A 30, 60 and 90-day forward view with pickup shows what is already on the books, and the channel view shows gross revenue, commission and net for each OTA, so you know which one really pays. Room types, guests, extras and Lio’s work have their own tabs."),
    ("Excel, PDF and email reports", "Export every analytics tab to Excel in one click or print the open view as a PDF; your accountant gets the numbers without extra work. Every Monday a weekly summary reaches the owner’s inbox, and on the 1st of each month a monthly report with CSV attachments."),
    ("Rates and restrictions", "One grid for every room type and rate plan: price, minimum and maximum stay, closed to arrival, closed to departure, stop sell and availability. Enter a whole season at once: pick a date range, room types and plans, and tick “weekends only” to price Friday and Saturday nights separately. A “resend to channels” button pushes everything again if a channel ever falls out of step."),
    ("Reservation import", "Moving from another system? Upload your reservations as a .csv, .xlsx or .xls file. Columns are matched automatically and you can adjust them, the date format is detected or chosen by you, duplicates are skipped, and any row that can’t be imported is listed with the reason."),
   ]),
   ("Team and control", [
    ("Staff roles and permissions", "Invite colleagues by email and give each a role: owner, manager, front desk, housekeeping, accounting or viewer. Everyone sees only what their job needs: housekeeping sees rooms, accounting doesn’t see guest messages. Suspend access at any time. Starter includes 3 users, Pro 8 and Growth 20."),
    ("Activity log", "Who changed what, and when: changes are logged field by field with the old and new value, without guest personal data. Filter by person, module, property or date, look back 365 days and download the log as CSV."),
    ("Two properties on Growth", "Switch between properties in one click and see both properties’ arrivals, departures, occupancy and revenue on one “All properties” page. When you add the second property, copy policies, AI settings, message templates and notification settings from the first. Both properties share one AI message quota."),
    ("Dashboard in 6 languages", "The dashboard, mobile app and guest check-in form are available in English, Turkish, Spanish, French, Italian and Portuguese, so every team member works in their own language."),
   ]),
  ],
  tbl=[("Analytics, Excel export and weekly/monthly email reports", "Yes", "Yes", "Yes"),
       ("Automatic check-in link email (you choose the booking sources)", "No", "Yes", "Yes"),
       ("“All properties” overview and property switcher", "No", "No", "Yes")],
  faq_import=("Can I bring my reservations from my current software?", "Yes. Export your reservations from your current system as a CSV or Excel file and upload it in the dashboard. Columns are matched automatically, duplicates are skipped and any row with a problem is listed with the reason. Then connect your channels: new OTA bookings arrive on their own from then on."),
  faq_roles=("Can I limit what each staff member sees?", "Yes. Each person gets a role: owner, manager, front desk, housekeeping, accounting or viewer. Housekeeping only sees rooms, accounting doesn’t see guest messages, and an activity log records who changed what. Starter includes 3 users, Pro 8 and Growth 20."),
  faq_reports=("Which reports do I get?", "Every plan includes analytics for occupancy, ADR, RevPAR, revenue, cancellations, a 30/60/90-day forward view and revenue per channel after commission. You can export to Excel or PDF, and the owner receives a weekly summary every Monday and a monthly report with CSV attachments."),
  sec=[("Staff roles and permissions", "Six roles (owner, manager, front desk, housekeeping, accounting, viewer) with separate permissions, assigned per property. A housekeeper only sees rooms; accounting doesn’t see guest messages. Exports need their own permission, and you can suspend a person’s access at any time."),
       ("Activity log", "Changes in the dashboard are recorded field by field: who, when, which property, old and new value. Guest personal data is not copied into the log. Entries are kept for 365 days and can be filtered and downloaded as CSV.")],
  ci_row=("Check-in link by email, automatically", "Switch it on and every new reservation with an email address gets the guest’s personal check-in link by email, in the guest’s language. You choose which booking sources it applies to: direct bookings, Booking.com, Expedia, Airbnb, Agoda or other OTAs. It stays off until you turn it on."),
  ch_rows=[("A whole season in one go", "Pick a date range, the room types and rate plans, then set price, minimum and maximum stay, closed to arrival, closed to departure or stop sell. Tick “weekends only” to price Friday and Saturday nights separately. A “resend to channels” button pushes the current rates and availability again if a channel ever falls out of step."),
           ("Out-of-order rooms close automatically", "When a room is taken out of order because of a fault, availability drops on every connected channel and the room can’t be assigned until it is back in service."),
           ("Bring your existing bookings", "Upload the reservations from your old system as CSV or Excel. Columns are matched automatically, duplicates are skipped and problem rows are listed with the reason.")],
  ch_switch=("Is it hard to switch from my current channel manager?", "No. Create your room types in Hostlio Pro, import your existing reservations from a CSV or Excel file, and map your OTA accounts through Channex. Our onboarding team helps during the switch."),
  today=dict(tab="Today", h="The day’s work, ready each morning", p="Open the dashboard and see who arrives, who leaves, which rooms need cleaning and what is waiting for you.",
             li=["Arrivals, departures and rooms to clean", "Messages and Lio drafts waiting for you", "Out-of-order rooms close on every channel"], more="All features",
             top=("Today", "08:00"), items=[("Arrivals", "6"), ("Departures", "4"), ("Rooms to clean", "5"), ("Messages waiting", "2"), ("Drafts to approve", "1")]),
),
"tr": dict(
  more_h="Günün tamamını tek panelden yönetin",
  more_p="Mesajlaşma ve kanal yönetiminin yanında ekibinizin her gün kullandığı araçlar. Hepsi web panelinde; aksi belirtilmedikçe tüm planlara dahil.",
  groups=[
   ("Günlük operasyon", [
    ("Bugün ekranı", "Sabah paneli açtığınızda günün işleri hazırdır: gelenler, gidenler, temizlenecek odalar, cevap bekleyen mesajlar, onayınızı bekleyen Lio taslakları, rezervasyon talepleri ve cevaplanacak yorumlar."),
    ("Kat hizmetleri", "Her odanın bir durumu vardır: temiz, kirli, bakımda ya da servis dışı. Bugün çıkışı olan odalar listenin başındadır; aynı gün yeni misafir gelecek oda yüksek öncelikli işaretlenir. Günlük temizlik listesini PDF olarak yazdırın; kat hizmetleri rolündeki personel yalnız odaları görür."),
    ("Arıza kaydı ve satış dışı oda", "Arızayı en fazla beş fotoğrafla (konum bilgisi silinir), kategori ve öncelikle bildirin. Odayı servis dışı yaptığınızda satıştan çıkar: bağlı kanallardaki müsaitlik otomatik düşer, odaya rezervasyon atanamaz ve ekibinize bildirim gider."),
    ("Büyüyen otele uygun oda rafı", "Büyük tesisler için üç yoğunluk seviyesi, oda tipine ya da kata göre gruplama, günlük boş oda sayısı, boş oda arama ve 7, 14 ya da 30 günlük görünüm. Çakışma kontrolü çift ya da odası atanmamış rezervasyonları listeler, raf uygun tipte boş oda önerir; rezervasyonları fareyle ya da klavyeyle taşırsınız."),
    ("Bildirimler ve sabah özeti", "Yeni, değişen ve iptal edilen rezervasyonlar, cevap bekleyen mesajlar, onaylanacak taslaklar, kanal sorunları ve arıza kayıtları tek bildirim kutusunda toplanır, 90 gün saklanır. Mobil uygulama her sabah 08:00'de (otelin saatiyle) günün özetini de gönderir (bugün Android'de, iOS'ta yakında gelecek uygulama güncellemesiyle)."),
   ]),
   ("Gelir, fiyat ve raporlar", [
    ("Analiz", "Doluluk, ADR, RevPAR, gelir, ortalama konaklama süresi, iptal ve no-show; önceki dönemle karşılaştırmalı. 30, 60 ve 90 günlük ileriye bakış ve pickup, takvimde neyin dolu olduğunu gösterir; kanal görünümü her OTA için brüt gelir, komisyon ve neti verir, hangi kanalın gerçekten kazandırdığını görürsünüz. Oda tipleri, misafirler, ek hizmetler ve Lio'nun işi için ayrı sekmeler var."),
    ("Excel, PDF ve e-posta raporları", "Analizin tüm sekmelerini tek tıkla Excel'e aktarın ya da açık görünümü PDF olarak yazdırın; muhasebeciniz ayrıca bir şey istemez. Her pazartesi haftanın özeti, her ayın 1'inde CSV ekli aylık rapor otel sahibinin e-postasına gelir."),
    ("Fiyat ve kısıtlamalar", "Her oda tipi ve fiyat planı için tek ızgara: fiyat, en az ve en çok konaklama, varışa kapalı (CTA), çıkışa kapalı (CTD), satışa kapatma ve müsaitlik. Bir sezonu tek seferde girin: tarih aralığını, oda tiplerini ve planları seçin, cuma ve cumartesi gecelerini ayrı fiyatlamak için “yalnız hafta sonu” kutusunu işaretleyin. Bir kanal geride kalırsa “kanallara yeniden gönder” düğmesi her şeyi tekrar iletir."),
    ("Rezervasyon içe aktarma", "Başka bir programdan mı geliyorsunuz? Rezervasyonlarınızı .csv, .xlsx ya da .xls dosyasıyla yükleyin. Sütunlar otomatik eşlenir ve değiştirebilirsiniz, tarih biçimi algılanır ya da siz seçersiniz, mükerrer kayıtlar atlanır, aktarılamayan her satır nedeniyle listelenir."),
   ]),
   ("Ekip ve kontrol", [
    ("Personel, roller ve yetkiler", "Ekip arkadaşlarınızı e-postayla davet edin, her birine rol verin: sahip, yönetici, resepsiyon, kat hizmetleri, muhasebe ya da izleyici. Herkes yalnız işi için gerekeni görür: kat görevlisi odaları görür, muhasebe misafir mesajlarını görmez. Erişimi istediğiniz an askıya alın. Starter 3, Pro 8, Growth 20 kullanıcı içerir."),
    ("İşlem geçmişi", "Kim, ne zaman, neyi değiştirdi: değişiklikler alan alan, eski ve yeni değeriyle kaydedilir; misafirin kişisel verisi kayda girmez. Kişiye, modüle, tesise ya da tarihe göre süzün, 365 gün geriye bakın, kaydı CSV olarak indirin."),
    ("Growth'ta iki tesis", "Tesisler arasında tek tıkla geçin; iki tesisin gelen, giden, doluluk ve gelirini tek “Tüm mülkler” sayfasında görün. İkinci tesisi eklerken politikaları, AI ayarlarını, mesaj şablonlarını ve bildirim ayarlarını ilkinden kopyalayın. İki tesis tek AI mesaj kotasını paylaşır."),
    ("Panel 6 dilde", "Panel, mobil uygulama ve misafirin check-in formu Türkçe, İngilizce, İspanyolca, Fransızca, İtalyanca ve Portekizce; ekibinizdeki herkes kendi dilinde çalışır."),
   ]),
  ],
  tbl=[("Analiz, Excel'e aktarma ve haftalık/aylık e-posta raporu", "Var", "Var", "Var"),
       ("Otomatik check-in bağlantısı e-postası (kaynakları siz seçersiniz)", "Yok", "Var", "Var"),
       ("“Tüm mülkler” özeti ve tesis değiştirici", "Yok", "Yok", "Var")],
  faq_import=("Eski programımdaki rezervasyonları aktarabilir miyim?", "Evet. Rezervasyonlarınızı mevcut programınızdan CSV ya da Excel olarak dışa aktarın ve panelde yükleyin. Sütunlar otomatik eşlenir, mükerrer kayıtlar atlanır, sorunlu her satır nedeniyle listelenir. Ardından kanallarınızı bağlayın; yeni OTA rezervasyonları bundan sonra kendiliğinden gelir."),
  faq_roles=("Personelin neyi göreceğini sınırlayabilir miyim?", "Evet. Her kişiye bir rol verirsiniz: sahip, yönetici, resepsiyon, kat hizmetleri, muhasebe ya da izleyici. Kat görevlisi yalnız odaları görür, muhasebe misafir mesajlarını görmez; işlem geçmişi kimin neyi değiştirdiğini kaydeder. Starter 3, Pro 8, Growth 20 kullanıcı içerir."),
  faq_reports=("Hangi raporları alırım?", "Tüm planlarda doluluk, ADR, RevPAR, gelir, iptaller, 30/60/90 günlük ileriye bakış ve komisyon sonrası kanal geliri analizleri vardır. Excel'e ya da PDF'e aktarabilirsiniz; otel sahibine her pazartesi haftalık özet, her ay da CSV ekli aylık rapor e-postayla gelir."),
  sec=[("Personel rolleri ve yetkiler", "Ayrı yetkileri olan altı rol (sahip, yönetici, resepsiyon, kat hizmetleri, muhasebe, izleyici), tesis bazında atanır. Kat görevlisi yalnız odaları görür; muhasebe misafir mesajlarını görmez. Dışa aktarma ayrı bir yetki ister ve bir kişinin erişimini istediğiniz an askıya alabilirsiniz."),
       ("İşlem geçmişi", "Paneldeki değişiklikler alan alan kaydedilir: kim, ne zaman, hangi tesis, eski ve yeni değer. Misafirin kişisel verisi kayda kopyalanmaz. Kayıtlar 365 gün saklanır; süzülebilir ve CSV olarak indirilebilir.")],
  ci_row=("Check-in bağlantısı otomatik e-postayla", "Açtığınızda e-posta adresi olan her yeni rezervasyonda misafirin kişisel check-in bağlantısı, misafirin dilinde e-postayla gider. Hangi rezervasyon kaynaklarına gideceğini siz seçersiniz: doğrudan rezervasyon, Booking.com, Expedia, Airbnb, Agoda ya da diğer OTA'lar. Siz açana kadar kapalı kalır."),
  ch_rows=[("Bir sezonu tek seferde girin", "Tarih aralığını, oda tiplerini ve fiyat planlarını seçin; fiyatı, en az ve en çok konaklamayı, varışa kapalı, çıkışa kapalı ya da satışa kapatma kuralını girin. Cuma ve cumartesi gecelerini ayrı fiyatlamak için “yalnız hafta sonu”nu işaretleyin. Bir kanal geride kalırsa “kanallara yeniden gönder” güncel fiyat ve müsaitliği tekrar iletir."),
           ("Servis dışı oda otomatik kapanır", "Arıza nedeniyle oda servis dışı yapılınca bağlı tüm kanallarda müsaitlik düşer ve oda yeniden hizmete girene kadar rezervasyona atanamaz."),
           ("Mevcut rezervasyonlarınızı getirin", "Eski programınızdaki rezervasyonları CSV ya da Excel dosyasıyla yükleyin. Sütunlar otomatik eşlenir, mükerrerler atlanır, sorunlu satırlar nedeniyle listelenir.")],
  ch_switch=("Mevcut kanal yöneticimden geçiş zor mu?", "Hayır. Oda tiplerinizi Hostlio Pro'da oluşturun, mevcut rezervasyonlarınızı CSV ya da Excel dosyasıyla içeri aktarın ve OTA hesaplarınızı Channex üzerinden eşleyin. Kurulum ekibimiz geçiş sırasında yardımcı olur."),
  today=dict(tab="Bugün", h="Günün işleri her sabah hazır", p="Paneli açın: kim geliyor, kim çıkıyor, hangi oda temizlenecek, hangi mesaj sizi bekliyor.",
             li=["Gelen, giden ve temizlenecek odalar", "Sizi bekleyen mesajlar ve Lio taslakları", "Servis dışı oda tüm kanallarda kapanır"], more="Tüm özellikler",
             top=("Bugün", "08:00"), items=[("Gelenler", "6"), ("Gidenler", "4"), ("Temizlenecek oda", "5"), ("Cevap bekleyen mesaj", "2"), ("Onay bekleyen taslak", "1")]),
),
"es": dict(
  more_h="Todo el día desde un solo panel",
  more_p="Además de la mensajería y la distribución, estas son las herramientas que tu equipo usa a diario. Todas están en el panel web e incluidas en todos los planes, salvo que se indique lo contrario.",
  groups=[
   ("Operación diaria", [
    ("Pantalla Hoy", "Abres el panel por la mañana y el día ya está organizado: llegadas, salidas, habitaciones por limpiar, mensajes pendientes de respuesta, borradores de Lio que esperan tu aprobación, solicitudes de reserva y reseñas por contestar."),
    ("Housekeeping", "Cada habitación tiene un estado: limpia, sucia, en mantenimiento o fuera de servicio. Las salidas del día van primero y, si entra un huésped el mismo día, la habitación se marca como prioritaria. Imprime la lista de limpieza del día en PDF; el personal con rol de housekeeping solo ve las habitaciones."),
    ("Averías y habitaciones fuera de servicio", "Registra una avería con hasta cinco fotos (se elimina la ubicación), una categoría y una prioridad. Si pones una habitación fuera de servicio, sale de la venta: la disponibilidad baja automáticamente en tus canales conectados, no se puede asignar a ninguna reserva y tu equipo recibe un aviso."),
    ("Un planning que crece contigo", "Para alojamientos más grandes: tres niveles de densidad, habitaciones agrupadas por tipo o por planta, número de habitaciones libres por día, búsqueda de habitación libre y vistas de 7, 14 o 30 días. El control de conflictos lista las reservas duplicadas o sin habitación, el planning te sugiere una habitación libre del tipo correcto y las reservas se mueven con el ratón o con el teclado."),
    ("Notificaciones y resumen matinal", "Reservas nuevas, modificadas y canceladas, mensajes sin responder, borradores por aprobar, incidencias de canal y averías llegan a un único centro de notificaciones, que las guarda 90 días. La app móvil también te envía un resumen del día a las 08:00, hora del hotel (hoy en Android; en iOS con la próxima actualización de la app)."),
   ]),
   ("Ingresos, tarifas e informes", [
    ("Análisis", "Ocupación, ADR, RevPAR, ingresos, estancia media, cancelaciones y no-shows, comparados con el periodo anterior. La vista a 30, 60 y 90 días con pickup muestra lo que ya tienes reservado, y la vista por canal te da ingresos brutos, comisión y neto de cada OTA, para que sepas cuál te deja más. Tipos de habitación, huéspedes, extras y el trabajo de Lio tienen sus propias pestañas."),
    ("Informes en Excel, PDF y por email", "Exporta todas las pestañas del análisis a Excel en un clic o imprime la vista abierta en PDF; tu gestor tiene los números sin trabajo extra. Cada lunes llega un resumen semanal al email del propietario y el día 1 de cada mes, un informe mensual con archivos CSV adjuntos."),
    ("Tarifas y restricciones", "Una sola cuadrícula para cada tipo de habitación y plan tarifario: precio, estancia mínima y máxima, cerrado a la llegada (CTA), cerrado a la salida (CTD), cierre de ventas y disponibilidad. Carga una temporada entera de una vez: elige el rango de fechas, los tipos de habitación y los planes, y marca «solo fines de semana» para dar otro precio a las noches de viernes y sábado. Si un canal se desincroniza, el botón «reenviar a los canales» lo envía todo de nuevo."),
    ("Importación de reservas", "¿Vienes de otro sistema? Sube tus reservas en un archivo .csv, .xlsx o .xls. Las columnas se asignan automáticamente y puedes ajustarlas, el formato de fecha se detecta o lo eliges tú, los duplicados se omiten y cada fila que no se puede importar aparece con el motivo."),
   ]),
   ("Equipo y control", [
    ("Personal, roles y permisos", "Invita a tus compañeros por email y asigna a cada uno un rol: propietario, gerente, recepción, housekeeping, contabilidad u observador. Cada persona ve solo lo que necesita: housekeeping ve las habitaciones y contabilidad no ve los mensajes de los huéspedes. Suspende un acceso cuando quieras. Starter incluye 3 usuarios, Pro 8 y Growth 20."),
    ("Historial de actividad", "Quién cambió qué y cuándo: los cambios se registran campo a campo, con el valor anterior y el nuevo, sin datos personales de los huéspedes. Filtra por persona, módulo, alojamiento o fecha, consulta 365 días hacia atrás y descarga el registro en CSV."),
    ("Dos alojamientos en Growth", "Cambia de alojamiento con un clic y consulta las llegadas, salidas, ocupación e ingresos de ambos en una sola página «Todos los alojamientos». Al añadir el segundo, copia del primero las políticas, los ajustes de IA, las plantillas de mensajes y las notificaciones. Los dos comparten una misma cuota de mensajes de IA."),
    ("Panel en 6 idiomas", "El panel, la app móvil y el formulario de check-in del huésped están en español, inglés, turco, francés, italiano y portugués, así que cada persona del equipo trabaja en su idioma."),
   ]),
  ],
  tbl=[("Análisis, exportación a Excel e informes semanales/mensuales por email", "Sí", "Sí", "Sí"),
       ("Email automático con el enlace de check-in (tú eliges los canales de origen)", "No", "Sí", "Sí"),
       ("Vista «Todos los alojamientos» y cambio de alojamiento", "No", "No", "Sí")],
  faq_import=("¿Puedo traer las reservas de mi programa actual?", "Sí. Exporta tus reservas del sistema actual en CSV o Excel y súbelas en el panel. Las columnas se asignan automáticamente, los duplicados se omiten y cada fila con un problema aparece con el motivo. Después conecta tus canales: a partir de ahí, las nuevas reservas de las OTAs llegan solas."),
  faq_roles=("¿Puedo limitar lo que ve cada persona del equipo?", "Sí. Cada persona tiene un rol: propietario, gerente, recepción, housekeeping, contabilidad u observador. Housekeeping solo ve las habitaciones, contabilidad no ve los mensajes de los huéspedes y un historial de actividad registra quién cambió qué. Starter incluye 3 usuarios, Pro 8 y Growth 20."),
  faq_reports=("¿Qué informes obtengo?", "Todos los planes incluyen análisis de ocupación, ADR, RevPAR, ingresos, cancelaciones, una vista a 30/60/90 días e ingresos por canal después de comisión. Puedes exportarlos a Excel o PDF, y el propietario recibe un resumen semanal cada lunes y un informe mensual con CSV adjuntos."),
  sec=[("Roles y permisos del personal", "Seis roles (propietario, gerente, recepción, housekeeping, contabilidad, observador) con permisos distintos, asignados por alojamiento. El personal de limpieza solo ve las habitaciones; contabilidad no ve los mensajes de los huéspedes. Exportar requiere su propio permiso y puedes suspender el acceso de una persona en cualquier momento."),
       ("Historial de actividad", "Los cambios en el panel se registran campo a campo: quién, cuándo, en qué alojamiento, valor anterior y nuevo. Los datos personales de los huéspedes no se copian en el registro. Las entradas se conservan 365 días y se pueden filtrar y descargar en CSV.")],
  ci_row=("Enlace de check-in por email, automáticamente", "Actívalo y cada nueva reserva con email recibe el enlace personal de check-in, en el idioma del huésped. Tú eliges a qué canales de origen se aplica: reservas directas, Booking.com, Expedia, Airbnb, Agoda u otras OTAs. Está desactivado hasta que lo enciendas."),
  ch_rows=[("Una temporada entera de una vez", "Elige un rango de fechas, los tipos de habitación y los planes tarifarios, y define precio, estancia mínima y máxima, cerrado a la llegada, cerrado a la salida o cierre de ventas. Marca «solo fines de semana» para dar otro precio a las noches de viernes y sábado. Si un canal se desincroniza, «reenviar a los canales» envía de nuevo las tarifas y la disponibilidad actuales."),
           ("Las habitaciones fuera de servicio se cierran solas", "Cuando una habitación queda fuera de servicio por una avería, la disponibilidad baja en todos los canales conectados y la habitación no se puede asignar hasta que vuelve a estar operativa."),
           ("Trae tus reservas actuales", "Sube las reservas de tu sistema anterior en CSV o Excel. Las columnas se asignan automáticamente, los duplicados se omiten y las filas con problemas aparecen con el motivo.")],
  ch_switch=("¿Es difícil cambiar desde mi channel manager actual?", "No. Crea tus tipos de habitación en Hostlio Pro, importa tus reservas actuales desde un archivo CSV o Excel y vincula tus cuentas de OTAs a través de Channex. Nuestro equipo de onboarding te ayuda durante el cambio."),
  today=dict(tab="Hoy", h="El trabajo del día, listo cada mañana", p="Abre el panel y mira quién llega, quién se va, qué habitaciones hay que limpiar y qué te está esperando.",
             li=["Llegadas, salidas y habitaciones por limpiar", "Mensajes y borradores de Lio pendientes", "Las habitaciones fuera de servicio se cierran en todos los canales"], more="Todas las funcionalidades",
             top=("Hoy", "08:00"), items=[("Llegadas", "6"), ("Salidas", "4"), ("Habitaciones por limpiar", "5"), ("Mensajes pendientes", "2"), ("Borradores por aprobar", "1")]),
),
"it": dict(
  more_h="Tutta la giornata da un solo pannello",
  more_p="Oltre alla messaggistica e alla distribuzione, ecco gli strumenti che il tuo staff usa ogni giorno. Sono tutti nel pannello web e inclusi in ogni piano, salvo diversa indicazione.",
  groups=[
   ("Operatività quotidiana", [
    ("Schermata Oggi", "Apri il pannello al mattino e la giornata è già organizzata: arrivi, partenze, camere da pulire, messaggi in attesa di risposta, bozze di Lio da approvare, richieste di prenotazione e recensioni a cui rispondere."),
    ("Housekeeping", "Ogni camera ha uno stato: pulita, sporca, in manutenzione o fuori servizio. Le partenze del giorno vengono prima e, se nella stessa camera arriva un ospite in giornata, la camera è segnata come prioritaria. Stampa in PDF la lista delle pulizie del giorno; chi ha il ruolo housekeeping vede solo le camere."),
    ("Guasti e camere fuori servizio", "Segnala un guasto con un massimo di cinque foto (i dati di posizione vengono rimossi), una categoria e una priorità. Se metti una camera fuori servizio, esce dalla vendita: la disponibilità scende automaticamente sui canali collegati, la camera non può essere assegnata e il tuo staff riceve un avviso."),
    ("Un planning che cresce con te", "Per le strutture più grandi: tre livelli di densità, camere raggruppate per tipologia o piano, numero di camere libere per giorno, ricerca di camere libere e viste a 7, 14 o 30 giorni. Il controllo conflitti elenca le prenotazioni doppie o senza camera, il planning suggerisce una camera libera della tipologia giusta e le prenotazioni si spostano con il mouse o con la tastiera."),
    ("Notifiche e riepilogo del mattino", "Prenotazioni nuove, modificate e cancellate, messaggi senza risposta, bozze da approvare, problemi dei canali e guasti arrivano in un unico centro notifiche, conservato per 90 giorni. L’app mobile ti invia anche un riepilogo della giornata alle 08:00, ora dell’hotel (oggi su Android; su iOS con il prossimo aggiornamento dell’app)."),
   ]),
   ("Ricavi, tariffe e report", [
    ("Analisi", "Occupazione, ADR, RevPAR, ricavi, durata media del soggiorno, cancellazioni e no-show, a confronto con il periodo precedente. La vista a 30, 60 e 90 giorni con pickup mostra cosa è già prenotato, e la vista per canale riporta ricavo lordo, commissione e netto di ogni OTA, così sai quale ti rende davvero. Tipologie di camera, ospiti, extra e il lavoro di Lio hanno schede proprie."),
    ("Report in Excel, PDF e via email", "Esporta in Excel tutte le schede dell’analisi con un clic o stampa in PDF la vista aperta; il commercialista ha i numeri senza lavoro in più. Ogni lunedì un riepilogo settimanale arriva all’email del titolare e il 1° di ogni mese un report mensile con allegati CSV."),
    ("Tariffe e restrizioni", "Un’unica griglia per ogni tipologia di camera e piano tariffario: prezzo, soggiorno minimo e massimo, chiuso all’arrivo (CTA), chiuso alla partenza (CTD), stop vendite e disponibilità. Inserisci un’intera stagione in una volta: scegli l’intervallo di date, le tipologie e i piani e spunta «solo weekend» per prezzare a parte le notti di venerdì e sabato. Se un canale resta indietro, il pulsante «reinvia ai canali» invia di nuovo tutto."),
    ("Importazione delle prenotazioni", "Arrivi da un altro gestionale? Carica le prenotazioni in un file .csv, .xlsx o .xls. Le colonne vengono abbinate automaticamente e puoi modificarle, il formato della data viene riconosciuto o lo scegli tu, i duplicati vengono saltati e ogni riga non importabile è elencata con il motivo."),
   ]),
   ("Team e controllo", [
    ("Staff, ruoli e permessi", "Invita i colleghi via email e assegna a ciascuno un ruolo: titolare, manager, reception, housekeeping, contabilità o osservatore. Ognuno vede solo ciò che serve al suo lavoro: l’housekeeping vede le camere, la contabilità non vede i messaggi degli ospiti. Sospendi un accesso quando vuoi. Starter include 3 utenti, Pro 8 e Growth 20."),
    ("Registro attività", "Chi ha cambiato cosa e quando: le modifiche sono registrate campo per campo, con valore precedente e nuovo, senza dati personali degli ospiti. Filtra per persona, modulo, struttura o data, consulta 365 giorni di storico e scarica il registro in CSV."),
    ("Due strutture con Growth", "Passa da una struttura all’altra con un clic e vedi arrivi, partenze, occupazione e ricavi di entrambe in un’unica pagina «Tutte le strutture». Quando aggiungi la seconda, copia dalla prima regole, impostazioni AI, modelli di messaggio e notifiche. Le due strutture condividono una sola quota di messaggi AI."),
    ("Pannello in 6 lingue", "Il pannello, l’app mobile e il modulo di check-in dell’ospite sono disponibili in italiano, inglese, turco, spagnolo, francese e portoghese, così ognuno nel team lavora nella propria lingua."),
   ]),
  ],
  tbl=[("Analisi, esportazione in Excel e report settimanali/mensili via email", "Sì", "Sì", "Sì"),
       ("Email automatica con il link di check-in (scegli tu i canali di provenienza)", "No", "Sì", "Sì"),
       ("Vista «Tutte le strutture» e cambio struttura", "No", "No", "Sì")],
  faq_import=("Posso portare le prenotazioni dal mio gestionale attuale?", "Sì. Esporta le prenotazioni dal sistema attuale in CSV o Excel e caricale nel pannello. Le colonne vengono abbinate automaticamente, i duplicati saltati e ogni riga con un problema è elencata con il motivo. Poi collega i canali: da quel momento le nuove prenotazioni delle OTA arrivano da sole."),
  faq_roles=("Posso limitare ciò che vede ogni membro dello staff?", "Sì. Ogni persona ha un ruolo: titolare, manager, reception, housekeeping, contabilità o osservatore. L’housekeeping vede solo le camere, la contabilità non vede i messaggi degli ospiti e un registro attività annota chi ha cambiato cosa. Starter include 3 utenti, Pro 8 e Growth 20."),
  faq_reports=("Quali report ottengo?", "Tutti i piani includono l’analisi di occupazione, ADR, RevPAR, ricavi, cancellazioni, una vista a 30/60/90 giorni e i ricavi per canale al netto delle commissioni. Puoi esportare in Excel o PDF, e il titolare riceve un riepilogo settimanale ogni lunedì e un report mensile con allegati CSV."),
  sec=[("Ruoli e permessi dello staff", "Sei ruoli (titolare, manager, reception, housekeeping, contabilità, osservatore) con permessi distinti, assegnati per struttura. Chi fa le pulizie vede solo le camere; la contabilità non vede i messaggi degli ospiti. L’esportazione richiede un permesso a parte e puoi sospendere l’accesso di una persona in qualsiasi momento."),
       ("Registro attività", "Le modifiche nel pannello sono registrate campo per campo: chi, quando, in quale struttura, valore precedente e nuovo. I dati personali degli ospiti non vengono copiati nel registro. Le voci sono conservate 365 giorni e si possono filtrare e scaricare in CSV.")],
  ci_row=("Link di check-in via email, in automatico", "Attivalo e ogni nuova prenotazione con un indirizzo email riceve il link personale di check-in, nella lingua dell’ospite. Scegli tu a quali canali di provenienza si applica: prenotazioni dirette, Booking.com, Expedia, Airbnb, Agoda o altre OTA. Resta disattivato finché non lo accendi."),
  ch_rows=[("Un’intera stagione in una volta", "Scegli un intervallo di date, le tipologie di camera e i piani tariffari, poi imposta prezzo, soggiorno minimo e massimo, chiuso all’arrivo, chiuso alla partenza o stop vendite. Spunta «solo weekend» per prezzare a parte le notti di venerdì e sabato. Se un canale resta indietro, «reinvia ai canali» invia di nuovo tariffe e disponibilità attuali."),
           ("Le camere fuori servizio si chiudono da sole", "Quando una camera va fuori servizio per un guasto, la disponibilità scende su tutti i canali collegati e la camera non può essere assegnata finché non torna operativa."),
           ("Porta le prenotazioni esistenti", "Carica le prenotazioni del vecchio gestionale in CSV o Excel. Le colonne vengono abbinate automaticamente, i duplicati saltati e le righe con problemi elencate con il motivo.")],
  ch_switch=("È difficile passare dal mio channel manager attuale?", "No. Crea le tipologie di camera in Hostlio Pro, importa le prenotazioni esistenti da un file CSV o Excel e collega i tuoi account OTA tramite Channex. Il nostro team di onboarding ti aiuta durante il passaggio."),
  today=dict(tab="Oggi", h="Il lavoro del giorno, pronto ogni mattina", p="Apri il pannello e vedi chi arriva, chi parte, quali camere vanno pulite e cosa ti sta aspettando.",
             li=["Arrivi, partenze e camere da pulire", "Messaggi e bozze di Lio in attesa", "Le camere fuori servizio si chiudono su tutti i canali"], more="Tutte le funzionalità",
             top=("Oggi", "08:00"), items=[("Arrivi", "6"), ("Partenze", "4"), ("Camere da pulire", "5"), ("Messaggi in attesa", "2"), ("Bozze da approvare", "1")]),
),
"pt": dict(
  more_h="O dia inteiro em um só painel",
  more_p="Além da mensageria e da distribuição, estas são as ferramentas que sua equipe usa todos os dias. Todas estão no painel web e incluídas em todos os planos, salvo indicação em contrário.",
  groups=[
   ("Operação do dia a dia", [
    ("Tela Hoje", "Abra o painel de manhã e o dia já está organizado: chegadas, saídas, quartos para limpar, mensagens aguardando resposta, rascunhos do Lio esperando sua aprovação, pedidos de reserva e avaliações para responder."),
    ("Governança", "Cada quarto tem um status: limpo, sujo, em manutenção ou fora de serviço. As saídas do dia vêm primeiro e, se um hóspede chega no mesmo quarto no mesmo dia, ele fica marcado como prioritário. Imprima a lista de limpeza do dia em PDF; quem tem a função de governança vê só os quartos."),
    ("Manutenção e quartos fora de serviço", "Registre um problema com até cinco fotos (os dados de localização são removidos), uma categoria e uma prioridade. Coloque um quarto fora de serviço e ele sai da venda: a disponibilidade cai automaticamente nos canais conectados, o quarto não pode ser atribuído a nenhuma reserva e sua equipe é avisada."),
    ("Um mapa de quartos que acompanha o crescimento", "Para propriedades maiores: três níveis de densidade, quartos agrupados por tipo ou andar, número de quartos livres por dia, busca de quarto livre e visões de 7, 14 ou 30 dias. A verificação de conflitos lista reservas duplicadas ou sem quarto, o mapa sugere um quarto livre do tipo certo e as reservas se movem com o mouse ou com o teclado."),
    ("Notificações e resumo da manhã", "Reservas novas, alteradas e canceladas, mensagens sem resposta, rascunhos para aprovar, problemas de canal e registros de manutenção chegam a uma única central de notificações, guardada por 90 dias. O app também envia um resumo do dia às 08:00, horário do hotel (hoje no Android; no iOS com a próxima atualização do app)."),
   ]),
   ("Receita, tarifas e relatórios", [
    ("Análises", "Ocupação, ADR, RevPAR, receita, estadia média, cancelamentos e no-shows, comparados com o período anterior. A visão de 30, 60 e 90 dias com pickup mostra o que já está reservado, e a visão por canal traz receita bruta, comissão e líquido de cada OTA, para você saber qual realmente compensa. Tipos de quarto, hóspedes, extras e o trabalho do Lio têm abas próprias."),
    ("Relatórios em Excel, PDF e por e-mail", "Exporte todas as abas de análise para Excel com um clique ou imprima a visão aberta em PDF; seu contador recebe os números sem trabalho extra. Toda segunda-feira um resumo semanal chega ao e-mail do proprietário e, no dia 1º de cada mês, um relatório mensal com anexos CSV."),
    ("Tarifas e restrições", "Uma única grade para cada tipo de quarto e plano tarifário: preço, estadia mínima e máxima, fechado para chegada (CTA), fechado para saída (CTD), stop sell e disponibilidade. Lance uma temporada inteira de uma vez: escolha o período, os tipos de quarto e os planos e marque «só fins de semana» para dar outro preço às noites de sexta e sábado. Se um canal ficar dessincronizado, o botão «reenviar aos canais» envia tudo de novo."),
    ("Importação de reservas", "Vindo de outro sistema? Envie suas reservas em um arquivo .csv, .xlsx ou .xls. As colunas são associadas automaticamente e você pode ajustá-las, o formato de data é detectado ou escolhido por você, duplicatas são ignoradas e cada linha que não pode ser importada aparece com o motivo."),
   ]),
   ("Equipe e controle", [
    ("Equipe, funções e permissões", "Convide colegas por e-mail e dê a cada um uma função: proprietário, gerente, recepção, governança, financeiro ou observador. Cada pessoa vê só o que o trabalho exige: a governança vê os quartos e o financeiro não vê as mensagens dos hóspedes. Suspenda um acesso quando quiser. O Starter inclui 3 usuários, o Pro 8 e o Growth 20."),
    ("Histórico de atividades", "Quem mudou o quê, e quando: as alterações são registradas campo a campo, com o valor antigo e o novo, sem dados pessoais dos hóspedes. Filtre por pessoa, módulo, propriedade ou data, consulte 365 dias de histórico e baixe o registro em CSV."),
    ("Duas propriedades no Growth", "Alterne entre propriedades com um clique e veja chegadas, saídas, ocupação e receita das duas em uma só página «Todas as propriedades». Ao adicionar a segunda, copie da primeira as políticas, as configurações de IA, os modelos de mensagem e as notificações. As duas compartilham uma única cota de mensagens de IA."),
    ("Painel em 6 idiomas", "O painel, o app e o formulário de check-in do hóspede estão em português, inglês, turco, espanhol, francês e italiano, para que cada pessoa da equipe trabalhe no seu idioma."),
   ]),
  ],
  tbl=[("Análises, exportação para Excel e relatórios semanais/mensais por e-mail", "Sim", "Sim", "Sim"),
       ("E-mail automático com o link de check-in (você escolhe as origens das reservas)", "Não", "Sim", "Sim"),
       ("Visão «Todas as propriedades» e troca de propriedade", "Não", "Não", "Sim")],
  faq_import=("Posso trazer as reservas do meu sistema atual?", "Sim. Exporte as reservas do sistema atual em CSV ou Excel e envie o arquivo no painel. As colunas são associadas automaticamente, duplicatas são ignoradas e cada linha com problema aparece com o motivo. Depois conecte seus canais: a partir daí, as novas reservas das OTAs chegam sozinhas."),
  faq_roles=("Posso limitar o que cada pessoa da equipe vê?", "Sim. Cada pessoa recebe uma função: proprietário, gerente, recepção, governança, financeiro ou observador. A governança vê só os quartos, o financeiro não vê as mensagens dos hóspedes e um histórico de atividades registra quem mudou o quê. O Starter inclui 3 usuários, o Pro 8 e o Growth 20."),
  faq_reports=("Quais relatórios eu recebo?", "Todos os planos incluem análises de ocupação, ADR, RevPAR, receita, cancelamentos, uma visão de 30/60/90 dias e receita por canal depois da comissão. Você pode exportar para Excel ou PDF, e o proprietário recebe um resumo semanal toda segunda-feira e um relatório mensal com anexos CSV."),
  sec=[("Funções e permissões da equipe", "Seis funções (proprietário, gerente, recepção, governança, financeiro, observador) com permissões próprias, atribuídas por propriedade. Quem faz a limpeza vê só os quartos; o financeiro não vê as mensagens dos hóspedes. Exportar exige uma permissão própria, e você pode suspender o acesso de uma pessoa a qualquer momento."),
       ("Histórico de atividades", "As alterações no painel são registradas campo a campo: quem, quando, em qual propriedade, valor antigo e novo. Os dados pessoais dos hóspedes não são copiados para o registro. As entradas ficam guardadas por 365 dias e podem ser filtradas e baixadas em CSV.")],
  ci_row=("Link de check-in por e-mail, automaticamente", "Ative e cada nova reserva com e-mail recebe o link pessoal de check-in, no idioma do hóspede. Você escolhe a quais origens se aplica: reservas diretas, Booking.com, Expedia, Airbnb, Agoda ou outras OTAs. Fica desativado até você ligar."),
  ch_rows=[("Uma temporada inteira de uma vez", "Escolha um período, os tipos de quarto e os planos tarifários e defina preço, estadia mínima e máxima, fechado para chegada, fechado para saída ou stop sell. Marque «só fins de semana» para dar outro preço às noites de sexta e sábado. Se um canal ficar para trás, «reenviar aos canais» envia de novo as tarifas e a disponibilidade atuais."),
           ("Quartos fora de serviço fecham sozinhos", "Quando um quarto fica fora de serviço por um problema, a disponibilidade cai em todos os canais conectados e o quarto não pode ser atribuído até voltar a funcionar."),
           ("Traga suas reservas atuais", "Envie as reservas do sistema antigo em CSV ou Excel. As colunas são associadas automaticamente, duplicatas são ignoradas e linhas com problema aparecem com o motivo.")],
  ch_switch=("É difícil migrar do meu channel manager atual?", "Não. Crie seus tipos de quarto no Hostlio Pro, importe as reservas atuais de um arquivo CSV ou Excel e vincule suas contas das OTAs pela Channex. Nossa equipe de implantação ajuda durante a troca."),
  today=dict(tab="Hoje", h="O trabalho do dia, pronto toda manhã", p="Abra o painel e veja quem chega, quem sai, quais quartos precisam de limpeza e o que está esperando por você.",
             li=["Chegadas, saídas e quartos para limpar", "Mensagens e rascunhos do Lio aguardando você", "Quarto fora de serviço fecha em todos os canais"], more="Todas as funcionalidades",
             top=("Hoje", "08:00"), items=[("Chegadas", "6"), ("Saídas", "4"), ("Quartos para limpar", "5"), ("Mensagens aguardando", "2"), ("Rascunhos para aprovar", "1")]),
),
"fr": dict(
  more_h="Toute la journée depuis un seul tableau de bord",
  more_p="En plus de la messagerie et de la distribution, voici les outils que votre équipe utilise chaque jour. Ils sont tous dans le tableau de bord web et inclus dans chaque forfait, sauf mention contraire.",
  groups=[
   ("Opérations du quotidien", [
    ("Écran Aujourd’hui", "Ouvrez le tableau de bord le matin : la journée est déjà prête. Arrivées, départs, chambres à nettoyer, messages en attente de réponse, brouillons de Lio à valider, demandes de réservation et avis auxquels répondre."),
    ("Ménage (housekeeping)", "Chaque chambre a un statut : propre, sale, en maintenance ou hors service. Les départs du jour passent en premier, et une chambre où un client arrive le jour même est marquée prioritaire. Imprimez la liste de ménage du jour en PDF ; le personnel avec le rôle ménage ne voit que les chambres."),
    ("Pannes et chambres hors service", "Signalez une panne avec jusqu’à cinq photos (les données de localisation sont supprimées), une catégorie et une priorité. Passez une chambre hors service et elle sort de la vente : la disponibilité baisse automatiquement sur vos canaux connectés, la chambre ne peut plus être attribuée et votre équipe est prévenue."),
    ("Un planning qui suit votre croissance", "Pour les établissements plus grands : trois niveaux de densité, chambres regroupées par type ou par étage, nombre de chambres libres par jour, recherche de chambre libre et vues sur 7, 14 ou 30 jours. Le contrôle des conflits liste les réservations en double ou sans chambre, le planning propose une chambre libre du bon type, et les réservations se déplacent à la souris ou au clavier."),
    ("Notifications et résumé du matin", "Réservations nouvelles, modifiées ou annulées, messages sans réponse, brouillons à valider, incidents de canal et pannes arrivent dans un seul centre de notifications, conservé 90 jours. L’application mobile envoie aussi un résumé de la journée à 08:00, heure de l’hôtel (sur Android aujourd’hui, sur iOS avec la prochaine mise à jour de l’application)."),
   ]),
   ("Revenus, tarifs et rapports", [
    ("Analyses", "Taux d’occupation, ADR, RevPAR, chiffre d’affaires, durée moyenne de séjour, annulations et no-shows, comparés à la période précédente. La vue à 30, 60 et 90 jours avec pickup montre ce qui est déjà réservé, et la vue par canal donne le revenu brut, la commission et le net de chaque OTA : vous savez lequel rapporte vraiment. Types de chambre, clients, extras et travail de Lio ont leurs propres onglets."),
    ("Rapports Excel, PDF et par e-mail", "Exportez tous les onglets d’analyse vers Excel en un clic ou imprimez la vue ouverte en PDF ; votre comptable a les chiffres sans travail supplémentaire. Chaque lundi, un résumé hebdomadaire arrive dans la boîte du propriétaire, et le 1er de chaque mois un rapport mensuel avec pièces jointes CSV."),
    ("Tarifs et restrictions", "Une seule grille pour chaque type de chambre et plan tarifaire : prix, séjour minimum et maximum, fermé à l’arrivée (CTA), fermé au départ (CTD), arrêt des ventes et disponibilité. Saisissez toute une saison d’un coup : choisissez la période, les types de chambre et les plans, et cochez « week-ends uniquement » pour tarifer à part les nuits du vendredi et du samedi. Si un canal se désynchronise, le bouton « renvoyer aux canaux » renvoie tout."),
    ("Import de réservations", "Vous venez d’un autre logiciel ? Importez vos réservations depuis un fichier .csv, .xlsx ou .xls. Les colonnes sont associées automatiquement et vous pouvez les ajuster, le format de date est détecté ou choisi par vous, les doublons sont ignorés et chaque ligne non importée est listée avec la raison."),
   ]),
   ("Équipe et contrôle", [
    ("Personnel, rôles et droits", "Invitez vos collègues par e-mail et donnez à chacun un rôle : propriétaire, manager, réception, ménage, comptabilité ou lecteur. Chacun ne voit que ce dont il a besoin : le ménage voit les chambres, la comptabilité ne voit pas les messages des clients. Suspendez un accès à tout moment. Starter inclut 3 utilisateurs, Pro 8 et Growth 20."),
    ("Journal d’activité", "Qui a changé quoi, et quand : les modifications sont enregistrées champ par champ, avec l’ancienne et la nouvelle valeur, sans données personnelles des clients. Filtrez par personne, module, établissement ou date, remontez 365 jours en arrière et téléchargez le journal en CSV."),
    ("Deux établissements avec Growth", "Passez d’un établissement à l’autre en un clic et voyez arrivées, départs, occupation et chiffre d’affaires des deux sur une seule page « Tous les établissements ». En ajoutant le second, copiez depuis le premier les règles, les réglages IA, les modèles de message et les notifications. Les deux partagent un même quota de messages IA."),
    ("Tableau de bord en 6 langues", "Le tableau de bord, l’application mobile et le formulaire de check-in du client sont disponibles en français, anglais, turc, espagnol, italien et portugais : chacun dans l’équipe travaille dans sa langue."),
   ]),
  ],
  tbl=[("Analyses, export Excel et rapports hebdomadaires/mensuels par e-mail", "Oui", "Oui", "Oui"),
       ("E-mail automatique avec le lien de check-in (vous choisissez les sources de réservation)", "Non", "Oui", "Oui"),
       ("Vue « Tous les établissements » et changement d’établissement", "Non", "Non", "Oui")],
  faq_import=("Puis-je reprendre les réservations de mon logiciel actuel ?", "Oui. Exportez vos réservations depuis votre système actuel en CSV ou Excel, puis importez le fichier dans le tableau de bord. Les colonnes sont associées automatiquement, les doublons ignorés et chaque ligne posant problème est listée avec la raison. Connectez ensuite vos canaux : les nouvelles réservations des OTA arrivent alors toutes seules."),
  faq_roles=("Puis-je limiter ce que voit chaque membre du personnel ?", "Oui. Chaque personne reçoit un rôle : propriétaire, manager, réception, ménage, comptabilité ou lecteur. Le ménage ne voit que les chambres, la comptabilité ne voit pas les messages des clients, et un journal d’activité enregistre qui a changé quoi. Starter inclut 3 utilisateurs, Pro 8 et Growth 20."),
  faq_reports=("Quels rapports vais-je recevoir ?", "Tous les forfaits incluent des analyses d’occupation, d’ADR, de RevPAR, de chiffre d’affaires et d’annulations, une vue à 30/60/90 jours et le revenu par canal après commission. Vous pouvez exporter en Excel ou en PDF, et le propriétaire reçoit un résumé hebdomadaire chaque lundi et un rapport mensuel avec pièces jointes CSV."),
  sec=[("Rôles et droits du personnel", "Six rôles (propriétaire, manager, réception, ménage, comptabilité, lecteur) avec des droits distincts, attribués par établissement. Le personnel de ménage ne voit que les chambres ; la comptabilité ne voit pas les messages des clients. L’export nécessite un droit spécifique et vous pouvez suspendre l’accès d’une personne à tout moment."),
       ("Journal d’activité", "Les modifications dans le tableau de bord sont enregistrées champ par champ : qui, quand, dans quel établissement, ancienne et nouvelle valeur. Les données personnelles des clients ne sont pas copiées dans le journal. Les entrées sont conservées 365 jours et peuvent être filtrées et téléchargées en CSV.")],
  ci_row=("Lien de check-in envoyé automatiquement par e-mail", "Activez-le et chaque nouvelle réservation avec une adresse e-mail reçoit le lien de check-in personnel, dans la langue du client. Vous choisissez les sources concernées : réservations directes, Booking.com, Expedia, Airbnb, Agoda ou autres OTA. Il reste désactivé tant que vous ne l’allumez pas."),
  ch_rows=[("Toute une saison d’un coup", "Choisissez une période, les types de chambre et les plans tarifaires, puis fixez le prix, le séjour minimum et maximum, la fermeture à l’arrivée, au départ ou l’arrêt des ventes. Cochez « week-ends uniquement » pour tarifer à part les nuits du vendredi et du samedi. Si un canal prend du retard, « renvoyer aux canaux » renvoie les tarifs et la disponibilité actuels."),
           ("Les chambres hors service se ferment seules", "Quand une chambre passe hors service à cause d’une panne, la disponibilité baisse sur tous les canaux connectés et la chambre ne peut plus être attribuée tant qu’elle n’est pas remise en service."),
           ("Reprenez vos réservations existantes", "Importez les réservations de votre ancien logiciel en CSV ou Excel. Les colonnes sont associées automatiquement, les doublons ignorés et les lignes posant problème listées avec la raison.")],
  ch_switch=("Est-il difficile de quitter mon channel manager actuel ?", "Non. Créez vos types de chambre dans Hostlio Pro, importez vos réservations existantes depuis un fichier CSV ou Excel et associez vos comptes OTA via Channex. Notre équipe d’intégration vous accompagne pendant la transition."),
  today=dict(tab="Aujourd’hui", h="Le travail du jour, prêt chaque matin", p="Ouvrez le tableau de bord : qui arrive, qui part, quelles chambres nettoyer et ce qui vous attend.",
             li=["Arrivées, départs et chambres à nettoyer", "Messages et brouillons de Lio en attente", "Une chambre hors service se ferme sur tous les canaux"], more="Toutes les fonctionnalités",
             top=("Aujourd’hui", "08:00"), items=[("Arrivées", "6"), ("Départs", "4"), ("Chambres à nettoyer", "5"), ("Messages en attente", "2"), ("Brouillons à valider", "1")]),
),
}


def _fr_typo(x):
    """Fransızca: iki noktalı işaret ve tırnaklardan önce bölünmez boşluk (lang_fr.py ile aynı)."""
    import re
    if isinstance(x, str):
        x = re.sub(r" ([:;?!»])", "\u00a0\\1", x)
        return x.replace("« ", "«\u00a0")
    if isinstance(x, list): return [_fr_typo(i) for i in x]
    if isinstance(x, tuple): return tuple(_fr_typo(i) for i in x)
    if isinstance(x, dict): return {k: _fr_typo(v) for k, v in x.items()}
    return x
FX["fr"] = _fr_typo(FX["fr"])


def features_more(L):
    """Özellikler sayfasına ikinci modül bölümü (gruplu satırlar)."""
    d = FX[L]
    groups = "".join(
        f'<h3 class="fx-group">{gh}</h3><div class="rows">'
        + "".join(f'<div class="row"><h4>{h}</h4><div><p>{p}</p></div></div>' for h, p in rows)
        + "</div>" for gh, rows in d["groups"])
    return (f'<section class="rule"><div class="wrap"><div class="section-head"><h2>{d["more_h"]}</h2><p>{d["more_p"]}</p></div>'
            f'{groups}</div></section>')


def table_rows(L):
    return "".join(f'<tr><th>{a}</th><td class="c">{s}</td><td class="c">{p}</td><td class="c">{g}</td></tr>' for a, s, p, g in FX[L]["tbl"])


def rows_html(items):
    return "".join(f'<div class="row"><h3>{h}</h3><div><p>{p}</p></div></div>' for h, p in items)


def checkin_row(L):
    return rows_html([FX[L]["ci_row"]])


def channel_rows(L):
    return rows_html(FX[L]["ch_rows"])


def faq(L, *keys):
    return [FX[L][k] for k in keys]


def today_stage(L, icon):
    """Ana sayfa ürün turunun 5. sekmesi (gap #7). Görsel kodla çizilir; sayılar örnektir."""
    t = FX[L]["today"]
    rows = "".join(f'<div><span class="nm">{a}</span><span class="pill">{n}</span></div>' for a, n in t["items"])
    vis = f'<div class="ui"><div class="ui-top">{t["top"][0]}<span>{t["top"][1]}</span></div><div class="ui-body chan-list today-list" aria-hidden="true">{rows}</div></div>'
    return t, vis
