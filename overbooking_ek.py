"""SEO içerik fikri #21 (SEO_RAPORU.md bölüm 8): overbooking yazılarının güçlendirilmesi, 6 dil.
GSC: "how can hotels avoid overbookings across ota channels?" sıra 2,9; overbooking yazıları ~170 gösterim, sıra 3–42.
Eklenenler: "OTA kanalları arasında" bölümü, kriz senaryosu (walk the guest) adımları + misafire e-posta şablonu,
günlük kontrol listesi, Hostlio Pro paragrafına canlı araçlar (çakışma kontrolü, satış dışı oda, kanallara yeniden gönder,
Bugün ekranındaki kanal senk şeridi). pages_v4._with_templates() bu modülü uygular.
Ürün iddiaları: ozellik_ekleri.FX (gap #7, #11, #12, #20) ile aynı, 8 Ekim 2026 kodla doğrulanmış metinler."""

OB = {
"en": dict(
 title="How to prevent overbooking across OTA channels: 6 steps",
 desc="How hotels avoid overbooking across Booking.com, Airbnb and Expedia: one availability source, real-time sync, mapping checks, and what to do if it happens.",
 sec='''<h2>Overbooking across OTA channels: where the gaps are</h2>
<p>Most double bookings at independent hotels don't come from one channel. They come from the gaps between channels:</p>
<ul><li><strong>Calendar links instead of a connection.</strong> Syncing Airbnb or a smaller site through an iCal calendar link means availability is refreshed on a schedule, not the moment a booking arrives. Two guests can book the same night in that gap.</li>
<li><strong>Unmapped or wrongly mapped rooms.</strong> A new room type added on Booking.com but not mapped in the channel manager keeps selling on its own allotment.</li>
<li><strong>Changes made directly in an extranet.</strong> Opening rooms in one extranet by hand overrides what the channel manager sent, and the other channels never hear about it.</li>
<li><strong>Modifications and cancellations.</strong> A date change that reaches the PMS late leaves the old nights blocked and the new nights open everywhere.</li>
<li><strong>Rooms that can't actually be sold.</strong> A room with a broken air conditioner is still counted as available unless it is taken out of sale everywhere.</li></ul>
<p>The fix is the same in every case: every channel reads availability from one calendar, over a direct two-way connection, and nothing changes availability outside that calendar. For the difference between the calendar and the connection, see <a href="{pmscm}">PMS vs channel manager</a>.</p>
<h2>A daily 5-minute overbooking check</h2>
<ol><li>Look at today's and tomorrow's arrivals for any room with two bookings or a booking with no room.</li>
<li>Check that yesterday's cancellations and modifications are on the calendar.</li>
<li>Confirm the channel connection shows no sync errors.</li>
<li>Take any room with a fault out of sale before you open the next season.</li>
<li>After adding a room type or rate plan, check its mapping on every channel.</li></ol>
<h2>If it happens anyway: walking the guest</h2>
<p>Hotels call moving an overbooked guest to another property “walking the guest”. Done well, it can still end with a good review:</p>
<ol><li><strong>Decide early.</strong> As soon as you spot the conflict, decide which booking you can honour. Don't wait for the guest to arrive.</li>
<li><strong>Find an equal or better room nearby</strong> and confirm it before you contact the guest.</li>
<li><strong>Cover the difference:</strong> the price gap, the transfer and, if possible, the first night.</li>
<li><strong>Tell the guest in their language,</strong> with the new address, how they'll get there and who to call.</li>
<li><strong>Offer to bring them back</strong> for the rest of the stay if you have a room from the next night.</li>
<li><strong>Log the cause</strong> (channel, room, mapping, manual change) so it doesn't repeat.</li></ol>
<p>A message you can adapt:</p>
<blockquote><p>Dear [name], we're very sorry: because of a booking error on our side we can't offer you the room you reserved for [dates]. We have booked you an equal room at [hotel], [distance] from us, and we will cover the price difference and your taxi there. Your new confirmation is attached. If you'd like to come back to us for the rest of your stay, we'll have your room ready from [date]. Please call us on [phone] with any question. [Your name], [Hotel]</p></blockquote>
''',
 hl="<p>Behind the scenes, the room rack runs a conflict check that lists double-booked and unassigned reservations and suggests a free room of the right type. Taking a room out of order drops its availability on every connected channel, the Today screen shows whether channels are in sync with a retry button, and “resend to channels” pushes current rates and availability again if a channel ever falls out of step.</p>",
 faq=[("How can hotels avoid overbookings across OTA channels?", "Connect every OTA to one calendar through a two-way, real-time channel manager instead of updating extranets by hand or relying on calendar (iCal) links. Then make sure every room type is mapped, enter direct bookings immediately and never open rooms directly in an extranet."),
      ("What does “walking the guest” mean?", "Moving a guest who can't be accommodated because of an overbooking to a comparable hotel nearby, usually with the hotel paying the price difference and transport.")]),

"tr": dict(
 title="Overbooking nasıl önlenir? OTA kanallarında 6 adım",
 desc="Booking.com, Airbnb ve Expedia arasında overbooking nasıl önlenir: tek müsaitlik kaynağı, anlık senkron, eşleme kontrolü ve kriz anında yapılacaklar.",
 sec='''<h2>OTA kanalları arasında overbooking: açıklar nerede?</h2>
<p>Bağımsız otellerdeki çift rezervasyonların çoğu tek bir kanaldan değil, kanalların arasındaki boşluklardan çıkar:</p>
<ul><li><strong>Bağlantı yerine takvim linki.</strong> Airbnb'yi ya da küçük bir siteyi iCal takvim linkiyle senkronize etmek, müsaitliğin rezervasyon geldiği an değil belli aralıklarla güncellenmesi demektir. Bu arada iki misafir aynı geceyi alabilir.</li>
<li><strong>Eşlenmemiş ya da yanlış eşlenmiş odalar.</strong> Booking.com'a eklenen ama kanal yöneticisinde eşlenmeyen yeni oda tipi kendi kontenjanıyla satmaya devam eder.</li>
<li><strong>Extranet'te elle yapılan değişiklikler.</strong> Bir extranet'te elle oda açmak, kanal yöneticisinin gönderdiğini ezer; diğer kanalların bundan haberi olmaz.</li>
<li><strong>Değişiklik ve iptaller.</strong> PMS'e geç ulaşan bir tarih değişikliği eski geceleri kapalı, yeni geceleri her yerde açık bırakır.</li>
<li><strong>Aslında satılamayan odalar.</strong> Kliması bozuk bir oda, her yerde satıştan çıkarılmadıkça müsait sayılır.</li></ul>
<p>Çözüm hepsinde aynı: her kanal müsaitliği tek takvimden, doğrudan ve iki yönlü bir bağlantıyla okur; o takvimin dışında hiçbir şey müsaitliği değiştirmez. Takvim ile bağlantı arasındaki fark için <a href="{cm}">channel manager nedir</a> rehberine bakın.</p>
<h2>Günlük 5 dakikalık overbooking kontrolü</h2>
<ol><li>Bugün ve yarın gelenlerde iki rezervasyonu olan oda ya da odası atanmamış rezervasyon var mı, bakın.</li>
<li>Dünkü iptal ve değişikliklerin takvime yansıdığını kontrol edin.</li>
<li>Kanal bağlantısında senkron hatası olmadığını doğrulayın.</li>
<li>Yeni sezonu açmadan önce arızalı odaları satıştan çıkarın.</li>
<li>Yeni oda tipi ya da fiyat planı ekledikten sonra her kanaldaki eşlemesini kontrol edin.</li></ol>
<h2>Yine de olursa: misafiri başka otele yönlendirmek</h2>
<p>Sektörde overbooking olan misafiri başka bir tesise taşımaya “walk the guest” denir. İyi yönetilirse yine iyi bir yorumla bitebilir:</p>
<ol><li><strong>Erken karar verin.</strong> Çakışmayı fark ettiğiniz anda hangi rezervasyonu karşılayacağınıza karar verin; misafirin gelmesini beklemeyin.</li>
<li><strong>Yakında eşdeğer ya da daha iyi bir oda bulun</strong> ve misafire ulaşmadan önce kesinleştirin.</li>
<li><strong>Farkı siz karşılayın:</strong> fiyat farkı, transfer ve mümkünse ilk gece.</li>
<li><strong>Misafire kendi dilinde haber verin;</strong> yeni adres, oraya nasıl gideceği ve kimi arayacağı belli olsun.</li>
<li><strong>Geri dönmeyi teklif edin:</strong> ertesi geceden odanız varsa konaklamanın kalanı için.</li>
<li><strong>Nedeni kaydedin</strong> (kanal, oda, eşleme, elle değişiklik), tekrar etmesin.</li></ol>
<p>Uyarlayabileceğiniz bir mesaj:</p>
<blockquote><p>Sayın [ad], çok özür dileriz: bizden kaynaklanan bir rezervasyon hatası nedeniyle [tarihler] için ayırttığınız odayı size veremiyoruz. Size [mesafe] uzaklıktaki [otel]'de eşdeğer bir oda ayırdık; fiyat farkını ve oraya taksi ücretinizi biz karşılıyoruz. Yeni onayınız ektedir. Konaklamanızın kalanında bize dönmek isterseniz odanız [tarih] itibarıyla hazır olacak. Her sorunuz için [telefon] numarasından bize ulaşabilirsiniz. [Adınız], [Otel]</p></blockquote>
''',
 hl="<p>Arka planda oda rafı çakışma kontrolü yapar: çift ya da odası atanmamış rezervasyonları listeler ve uygun tipte boş oda önerir. Odayı servis dışı yaptığınızda müsaitliği tüm bağlı kanallarda düşer; Bugün ekranı kanalların senkron olup olmadığını “yeniden dene” düğmesiyle gösterir; bir kanal geride kalırsa “kanallara yeniden gönder” güncel fiyat ve müsaitliği tekrar iletir.</p>",
 faq=[("Oteller OTA kanalları arasında overbooking'i nasıl önler?", "Extranet'leri elle güncellemek ya da takvim (iCal) linklerine güvenmek yerine tüm OTA'ları iki yönlü, anlık çalışan bir kanal yöneticisiyle tek takvime bağlar. Ardından her oda tipinin eşlendiğinden emin olur, direkt rezervasyonları hemen girer ve hiçbir extranet'te elle oda açmaz."),
      ("“Walk the guest” ne demek?", "Overbooking nedeniyle konaklatılamayan misafiri, genellikle fiyat farkı ve ulaşımı otel karşılayarak, yakındaki eşdeğer bir otele yönlendirmek.")]),

"es": dict(
 title="Cómo evitar el overbooking entre canales OTA: 6 pasos",
 desc="Cómo evitar el overbooking entre Booking.com, Airbnb y Expedia: una sola fuente de disponibilidad, sincronización en tiempo real y qué hacer si ocurre.",
 sec='''<h2>Overbooking entre canales OTA: dónde están los huecos</h2>
<p>La mayoría de las dobles reservas en hoteles independientes no nacen en un solo canal, sino en los huecos entre canales:</p>
<ul><li><strong>Enlaces de calendario en lugar de conexión.</strong> Sincronizar Airbnb o un portal pequeño con un enlace iCal significa que la disponibilidad se actualiza cada cierto tiempo, no en el momento de la reserva. En ese intervalo dos huéspedes pueden reservar la misma noche.</li>
<li><strong>Habitaciones sin mapear o mal mapeadas.</strong> Un tipo de habitación nuevo creado en Booking.com y no mapeado en el channel manager sigue vendiendo con su propio cupo.</li>
<li><strong>Cambios hechos directamente en una extranet.</strong> Abrir habitaciones a mano en una extranet sobrescribe lo que envió el channel manager, y los demás canales no se enteran.</li>
<li><strong>Modificaciones y cancelaciones.</strong> Un cambio de fechas que llega tarde al PMS deja bloqueadas las noches antiguas y abiertas las nuevas en todas partes.</li>
<li><strong>Habitaciones que en realidad no se pueden vender.</strong> Una habitación con el aire acondicionado averiado sigue contando como disponible si no se retira de la venta en todos los canales.</li></ul>
<p>La solución es siempre la misma: todos los canales leen la disponibilidad de un único calendario, mediante una conexión directa y bidireccional, y nada cambia la disponibilidad fuera de ese calendario. Para ver cómo encaja el <a href="{ch}">channel manager</a> con el resto, consulta <a href="{pms}">cómo elegir software de gestión hotelera</a>.</p>
<h2>Control diario de 5 minutos</h2>
<ol><li>Revisa las llegadas de hoy y mañana: ninguna habitación con dos reservas ni reservas sin habitación.</li>
<li>Comprueba que las cancelaciones y modificaciones de ayer están en el calendario.</li>
<li>Confirma que la conexión con los canales no muestra errores de sincronización.</li>
<li>Retira de la venta las habitaciones averiadas antes de abrir la próxima temporada.</li>
<li>Tras añadir un tipo de habitación o un plan tarifario, revisa su mapeo en cada canal.</li></ol>
<h2>Si ocurre igualmente: reubicar al huésped</h2>
<p>En hotelería, trasladar a otro alojamiento a un huésped afectado por overbooking se llama reubicar (en inglés, “walking the guest”). Bien gestionado, todavía puede terminar en una buena reseña:</p>
<ol><li><strong>Decide pronto.</strong> En cuanto detectes el conflicto, decide qué reserva puedes atender. No esperes a que llegue el huésped.</li>
<li><strong>Busca una habitación igual o mejor cerca</strong> y confírmala antes de contactar al huésped.</li>
<li><strong>Asume la diferencia:</strong> el precio, el traslado y, si puedes, la primera noche.</li>
<li><strong>Avisa al huésped en su idioma,</strong> con la nueva dirección, cómo llegar y a quién llamar.</li>
<li><strong>Ofrece que vuelva</strong> para el resto de la estancia si tienes habitación a partir de la noche siguiente.</li>
<li><strong>Anota la causa</strong> (canal, habitación, mapeo, cambio manual) para que no se repita.</li></ol>
<p>Un mensaje que puedes adaptar:</p>
<blockquote><p>Estimado/a [nombre]: lo sentimos mucho. Por un error de reserva por nuestra parte no podemos ofrecerle la habitación que reservó para [fechas]. Le hemos reservado una habitación equivalente en [hotel], a [distancia] de nosotros, y nos hacemos cargo de la diferencia de precio y del taxi. Adjuntamos su nueva confirmación. Si desea volver con nosotros el resto de su estancia, tendremos su habitación lista a partir del [fecha]. Para cualquier duda, llámenos al [teléfono]. [Su nombre], [Hotel]</p></blockquote>
''',
 hl="<p>Además, el planning ejecuta un control de conflictos que lista las reservas duplicadas o sin habitación asignada y sugiere una habitación libre del tipo adecuado. Al poner una habitación fuera de servicio, su disponibilidad baja en todos los canales conectados; la pantalla Hoy muestra si los canales están sincronizados, con un botón para reintentar, y “reenviar a los canales” vuelve a enviar tarifas y disponibilidad si un canal se desfasa.</p>",
 faq=[("¿Cómo evitan los hoteles el overbooking entre canales OTA?", "Conectando todas las OTA a un único calendario mediante un channel manager bidireccional y en tiempo real, en lugar de actualizar extranets a mano o depender de enlaces iCal. Después, comprobando que cada tipo de habitación está mapeado, registrando las reservas directas al momento y sin abrir nunca habitaciones directamente en una extranet."),
      ("¿Qué significa reubicar a un huésped por overbooking?", "Alojar en un hotel cercano y comparable a un huésped que no se puede atender por overbooking; normalmente el hotel paga la diferencia de precio y el traslado.")]),

"it": dict(
 title="Come evitare l'overbooking tra i canali OTA: 6 passi",
 desc="Come evitare l'overbooking tra Booking.com, Airbnb ed Expedia: un'unica fonte di disponibilità, sincronizzazione in tempo reale e cosa fare se succede.",
 sec='''<h2>Overbooking tra i canali OTA: dove sono i buchi</h2>
<p>La maggior parte delle doppie prenotazioni nelle strutture indipendenti non nasce da un solo canale, ma dagli spazi tra i canali:</p>
<ul><li><strong>Link di calendario invece di una connessione.</strong> Sincronizzare Airbnb o un portale minore con un link iCal significa aggiornare la disponibilità a intervalli, non nel momento della prenotazione. In quell'intervallo due ospiti possono prenotare la stessa notte.</li>
<li><strong>Camere non mappate o mappate male.</strong> Una nuova tipologia creata su Booking.com e non mappata nel channel manager continua a vendere con il proprio allotment.</li>
<li><strong>Modifiche fatte direttamente in extranet.</strong> Aprire camere a mano in un'extranet sovrascrive ciò che ha inviato il channel manager, e gli altri canali non lo sanno.</li>
<li><strong>Modifiche e cancellazioni.</strong> Un cambio di date che arriva tardi al PMS lascia bloccate le vecchie notti e aperte le nuove ovunque.</li>
<li><strong>Camere che in realtà non si possono vendere.</strong> Una camera con il condizionatore guasto resta disponibile finché non viene tolta dalla vendita ovunque.</li></ul>
<p>La soluzione è sempre la stessa: tutti i canali leggono la disponibilità da un unico planning, con una connessione diretta e bidirezionale, e niente modifica la disponibilità al di fuori di quel planning. Per la differenza tra planning e connessione vedi <a href="{pmscm}">channel manager e PMS: le differenze</a>.</p>
<h2>Controllo quotidiano di 5 minuti</h2>
<ol><li>Guarda gli arrivi di oggi e domani: nessuna camera con due prenotazioni, nessuna prenotazione senza camera.</li>
<li>Verifica che le cancellazioni e le modifiche di ieri siano sul planning.</li>
<li>Controlla che la connessione con i canali non segnali errori di sincronizzazione.</li>
<li>Togli dalla vendita le camere guaste prima di aprire la stagione successiva.</li>
<li>Dopo aver aggiunto una tipologia o un piano tariffario, controllane la mappatura su ogni canale.</li></ol>
<h2>Se succede comunque: riproteggere l'ospite</h2>
<p>Spostare in un'altra struttura un ospite rimasto senza camera per overbooking si chiama riprotezione (in inglese “walking the guest”). Gestita bene, può ancora chiudersi con una buona recensione:</p>
<ol><li><strong>Decidi presto.</strong> Appena vedi il conflitto, decidi quale prenotazione puoi onorare. Non aspettare l'arrivo dell'ospite.</li>
<li><strong>Trova una camera uguale o migliore nelle vicinanze</strong> e confermala prima di contattare l'ospite.</li>
<li><strong>Copri la differenza:</strong> prezzo, trasferimento e, se possibile, la prima notte.</li>
<li><strong>Avvisa l'ospite nella sua lingua,</strong> con il nuovo indirizzo, come arrivarci e chi chiamare.</li>
<li><strong>Proponi il rientro</strong> per il resto del soggiorno se hai una camera dalla notte successiva.</li>
<li><strong>Registra la causa</strong> (canale, camera, mappatura, modifica manuale) perché non si ripeta.</li></ol>
<p>Un messaggio da adattare:</p>
<blockquote><p>Gentile [nome], ci scusiamo molto: a causa di un errore di prenotazione da parte nostra non possiamo offrirle la camera prenotata per [date]. Le abbiamo riservato una camera equivalente presso [hotel], a [distanza] da noi, e ci facciamo carico della differenza di prezzo e del taxi. In allegato la nuova conferma. Se desidera tornare da noi per il resto del soggiorno, la sua camera sarà pronta dal [data]. Per qualsiasi domanda ci chiami al [telefono]. [Il suo nome], [Hotel]</p></blockquote>
''',
 hl="<p>Dietro le quinte il planning esegue un controllo dei conflitti che elenca le prenotazioni doppie o senza camera assegnata e suggerisce una camera libera della tipologia giusta. Mettendo una camera fuori servizio la sua disponibilità scende su tutti i canali collegati; la schermata Oggi mostra se i canali sono sincronizzati, con un pulsante per riprovare, e “reinvia ai canali” invia di nuovo tariffe e disponibilità se un canale resta indietro.</p>",
 faq=[("Come evitano gli hotel l'overbooking tra i canali OTA?", "Collegando tutte le OTA a un unico planning con un channel manager bidirezionale e in tempo reale, invece di aggiornare le extranet a mano o affidarsi ai link iCal. Poi verificando che ogni tipologia sia mappata, inserendo subito le prenotazioni dirette e non aprendo mai camere direttamente in extranet."),
      ("Cosa vuol dire riproteggere un ospite?", "Sistemare in un hotel vicino e comparabile un ospite che non si può accogliere per overbooking; di solito l'hotel paga la differenza di prezzo e il trasferimento.")]),

"pt": dict(
 title="Como evitar overbooking entre canais OTA: 6 passos",
 desc="Como hotéis evitam overbooking entre Booking.com, Airbnb e Expedia: uma só fonte de disponibilidade, sincronização em tempo real e o que fazer se acontecer.",
 sec='''<h2>Overbooking entre canais OTA: onde ficam as brechas</h2>
<p>A maior parte das reservas duplicadas em hotéis independentes não nasce em um canal só, e sim nas brechas entre os canais:</p>
<ul><li><strong>Link de calendário em vez de conexão.</strong> Sincronizar o Airbnb ou um site menor por link iCal significa que a disponibilidade é atualizada de tempos em tempos, não no momento da reserva. Nesse intervalo dois hóspedes podem reservar a mesma noite.</li>
<li><strong>Quartos sem mapeamento ou mal mapeados.</strong> Um tipo de quarto novo criado no Booking.com e não mapeado no channel manager continua vendendo com a própria cota.</li>
<li><strong>Mudanças feitas direto na extranet.</strong> Abrir quartos à mão em uma extranet sobrescreve o que o channel manager enviou, e os outros canais não ficam sabendo.</li>
<li><strong>Alterações e cancelamentos.</strong> Uma mudança de datas que chega atrasada ao PMS deixa as noites antigas bloqueadas e as novas abertas em todo lugar.</li>
<li><strong>Quartos que na prática não podem ser vendidos.</strong> Um quarto com o ar-condicionado quebrado continua contando como disponível se não for tirado de venda em todos os canais.</li></ul>
<p>A solução é sempre a mesma: todos os canais leem a disponibilidade de um único calendário, por uma conexão direta e bidirecional, e nada muda a disponibilidade fora desse calendário. Para entender a diferença entre calendário e conexão, veja <a href="{pmscm}">o que é channel manager e a diferença para o PMS</a>.</p>
<h2>Checagem diária de 5 minutos</h2>
<ol><li>Veja as chegadas de hoje e de amanhã: nenhum quarto com duas reservas, nenhuma reserva sem quarto.</li>
<li>Confira se os cancelamentos e alterações de ontem estão no calendário.</li>
<li>Confirme que a conexão com os canais não mostra erros de sincronização.</li>
<li>Tire de venda os quartos com defeito antes de abrir a próxima temporada.</li>
<li>Depois de criar um tipo de quarto ou plano tarifário, confira o mapeamento em cada canal.</li></ol>
<h2>Se acontecer mesmo assim: realocar o hóspede</h2>
<p>Na hotelaria, transferir para outro hotel um hóspede afetado por overbooking se chama realocar (em inglês, “walking the guest”). Bem conduzido, ainda pode terminar em uma boa avaliação:</p>
<ol><li><strong>Decida cedo.</strong> Assim que perceber o conflito, decida qual reserva você consegue honrar. Não espere o hóspede chegar.</li>
<li><strong>Encontre um quarto igual ou melhor por perto</strong> e confirme antes de falar com o hóspede.</li>
<li><strong>Cubra a diferença:</strong> preço, transporte e, se possível, a primeira noite.</li>
<li><strong>Avise o hóspede no idioma dele,</strong> com o novo endereço, como chegar e para quem ligar.</li>
<li><strong>Ofereça a volta</strong> para o resto da estadia se tiver quarto a partir da noite seguinte.</li>
<li><strong>Registre a causa</strong> (canal, quarto, mapeamento, mudança manual) para não repetir.</li></ol>
<p>Uma mensagem para adaptar:</p>
<blockquote><p>Prezado(a) [nome], pedimos muitas desculpas: por um erro de reserva da nossa parte, não conseguimos oferecer o quarto reservado para [datas]. Reservamos um quarto equivalente no [hotel], a [distância] daqui, e vamos pagar a diferença de preço e o táxi até lá. Sua nova confirmação segue em anexo. Se quiser voltar para cá no restante da estadia, seu quarto estará pronto a partir de [data]. Qualquer dúvida, ligue para [telefone]. [Seu nome], [Hotel]</p></blockquote>
''',
 hl="<p>Por trás disso, o mapa de reservas faz uma verificação de conflitos que lista reservas duplicadas ou sem quarto atribuído e sugere um quarto livre do tipo certo. Ao colocar um quarto fora de serviço, a disponibilidade dele cai em todos os canais conectados; a tela Hoje mostra se os canais estão sincronizados, com um botão para tentar de novo, e “reenviar aos canais” manda de novo tarifas e disponibilidade se um canal ficar para trás.</p>",
 faq=[("Como os hotéis evitam overbooking entre canais OTA?", "Conectando todas as OTAs a um único calendário com um channel manager bidirecional e em tempo real, em vez de atualizar extranets à mão ou depender de links iCal. Depois, garantindo que cada tipo de quarto está mapeado, lançando reservas diretas na hora e nunca abrindo quartos direto em uma extranet."),
      ("O que significa realocar um hóspede?", "Hospedar em um hotel próximo e equivalente um hóspede que não pode ser atendido por overbooking; normalmente o hotel paga a diferença de preço e o transporte.")]),

"fr": dict(
 title="Éviter la surréservation entre canaux OTA : 6 étapes",
 desc="Éviter la surréservation entre Booking.com, Airbnb et Expedia : un seul planning, synchronisation en temps réel et que faire si elle survient.",
 sec='''<h2>Surréservation entre canaux OTA : où sont les failles</h2>
<p>La plupart des doubles réservations dans les hôtels indépendants ne viennent pas d'un seul canal, mais des failles entre les canaux :</p>
<ul><li><strong>Un lien de calendrier au lieu d'une connexion.</strong> Synchroniser Airbnb ou un petit site via un lien iCal signifie que les disponibilités se mettent à jour par intervalles, pas au moment de la réservation. Entre-temps, deux clients peuvent réserver la même nuit.</li>
<li><strong>Chambres non mappées ou mal mappées.</strong> Un nouveau type de chambre créé sur Booking.com mais pas mappé dans le channel manager continue de se vendre sur son propre stock.</li>
<li><strong>Modifications faites directement dans un extranet.</strong> Ouvrir des chambres à la main dans un extranet écrase ce qu'a envoyé le channel manager, et les autres canaux n'en savent rien.</li>
<li><strong>Modifications et annulations.</strong> Un changement de dates qui arrive en retard dans le PMS laisse les anciennes nuits bloquées et les nouvelles ouvertes partout.</li>
<li><strong>Des chambres qui ne sont pas vraiment vendables.</strong> Une chambre dont la climatisation est en panne reste disponible tant qu'elle n'est pas retirée de la vente partout.</li></ul>
<p>La solution est toujours la même : tous les canaux lisent les disponibilités dans un seul planning, via une connexion directe et bidirectionnelle, et rien ne modifie les disponibilités en dehors de ce planning. Pour la différence entre planning et connexion, voir <a href="{pmscm}">PMS ou channel manager : quelle différence</a>.</p>
<h2>Le contrôle quotidien de 5 minutes</h2>
<ol><li>Regardez les arrivées du jour et du lendemain : aucune chambre avec deux réservations, aucune réservation sans chambre.</li>
<li>Vérifiez que les annulations et modifications de la veille figurent au planning.</li>
<li>Confirmez que la connexion aux canaux n'affiche pas d'erreur de synchronisation.</li>
<li>Retirez de la vente les chambres en panne avant d'ouvrir la saison suivante.</li>
<li>Après l'ajout d'un type de chambre ou d'un plan tarifaire, vérifiez son mapping sur chaque canal.</li></ol>
<h2>Si elle survient quand même : délogement du client</h2>
<p>Reloger dans un autre établissement un client victime d'une surréservation s'appelle le délogement (en anglais « walking the guest »). Bien mené, il peut encore se terminer par un bon avis :</p>
<ol><li><strong>Décidez tôt.</strong> Dès que vous voyez le conflit, choisissez la réservation que vous pouvez honorer. N'attendez pas l'arrivée du client.</li>
<li><strong>Trouvez une chambre équivalente ou meilleure à proximité</strong> et confirmez-la avant de contacter le client.</li>
<li><strong>Prenez la différence à votre charge :</strong> l'écart de prix, le transfert et, si possible, la première nuit.</li>
<li><strong>Prévenez le client dans sa langue,</strong> avec la nouvelle adresse, le moyen d'y aller et la personne à appeler.</li>
<li><strong>Proposez-lui de revenir</strong> pour la suite du séjour si une chambre se libère le lendemain.</li>
<li><strong>Notez la cause</strong> (canal, chambre, mapping, modification manuelle) pour qu'elle ne se reproduise pas.</li></ol>
<p>Un message à adapter :</p>
<blockquote><p>Madame, Monsieur [nom], nous sommes sincèrement désolés : en raison d'une erreur de réservation de notre part, nous ne pouvons pas vous proposer la chambre réservée pour [dates]. Nous vous avons réservé une chambre équivalente à l'hôtel [hôtel], à [distance] de chez nous, et prenons en charge la différence de prix ainsi que votre taxi. Vous trouverez votre nouvelle confirmation en pièce jointe. Si vous souhaitez revenir chez nous pour la suite de votre séjour, votre chambre sera prête à partir du [date]. Pour toute question, appelez-nous au [téléphone]. [Votre nom], [Hôtel]</p></blockquote>
''',
 hl="<p>En coulisses, le planning effectue un contrôle des conflits qui liste les réservations en double ou sans chambre attribuée et suggère une chambre libre du bon type. Une chambre mise hors service voit sa disponibilité baisser sur tous les canaux connectés ; l'écran Aujourd'hui indique si les canaux sont synchronisés, avec un bouton pour réessayer, et « renvoyer aux canaux » renvoie tarifs et disponibilités si un canal se désynchronise.</p>",
 faq=[("Comment les hôtels évitent-ils la surréservation entre canaux OTA ?", "En reliant toutes les OTA à un seul planning via un channel manager bidirectionnel et en temps réel, plutôt qu'en mettant à jour les extranets à la main ou en comptant sur des liens iCal. Ensuite en vérifiant que chaque type de chambre est mappé, en saisissant tout de suite les réservations directes et en n'ouvrant jamais de chambres directement dans un extranet."),
      ("Que signifie déloger un client ?", "Reloger dans un hôtel proche et comparable un client qu'on ne peut pas accueillir à cause d'une surréservation ; l'hôtel paie en général la différence de prix et le transport.")]),
}


def apply(L, g, url):
    """Overbooking yazısına OTA bölümü + kriz senaryosu + günlük kontrol ekler (son "Hostlio Pro'da" bölümünden önce)."""
    o = OB.get(L)
    if not o: return g
    if L == "fr":
        from ozellik_ekleri import _fr_typo
        o = _fr_typo(o)
    links = {"pmscm": url("post-pms-vs-cm", L), "cm": url("post-channel-manager", L), "ch": url("channel", L), "pms": url("post-pms", L)}
    sec = o["sec"].format(**links)
    c = g["content"]
    k = c.rfind("<h2>")
    c = c[:k] + sec + c[k:] + o["hl"]
    return dict(g, title=o["title"], desc=o["desc"], content=c, faq=list(g["faq"]) + o["faq"])
