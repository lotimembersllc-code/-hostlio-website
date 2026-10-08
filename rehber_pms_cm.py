"""SEO içerik fikri #20 (SEO_RAPORU.md bölüm 8): "PMS vs channel manager" rehberi — EN, IT, PT, FR.
Ürün iddiaları yalnız canlı özellikler (llms.txt "Key facts" ile aynı): kanal yöneticisi tüm planlarda, Channex
üzerinden sertifikalı bağlantı, fiyat ızgarası + kısıtlar, satış dışı oda OTA'da kapanır, kanal bazında net gelir.
Rakip fiyat örnekleri guides_tr.PRICE_SRC ile aynı resmî sayfalardan (Sirvoy, Beds24), 8 Ekim 2026.
Fiyatlar ⟦token⟧ ile (pricing.py)."""
import html

SRC = [("Sirvoy: Pricing", "https://sirvoy.com/pricing"), ("Beds24: Pricing", "https://beds24.com/pricing.html")]
SRC_H = {"en": ("Sources", "Accessed 8 October 2026."), "it": ("Fonti", "Consultate l'8 ottobre 2026."),
         "pt": ("Fontes", "Acessadas em 8 de outubro de 2026."), "fr": ("Sources", "Consultées le 8 octobre 2026.")}


def _tbl(head, rows):
    h = "".join(f"<th>{x}</th>" for x in head)
    b = "".join("<tr>" + f'<th scope="row">{r[0]}</th>' + "".join(f"<td>{c}</td>" for c in r[1:]) + "</tr>" for r in rows)
    return f'<div class="table-wrap"><table><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table></div>'


def _src(L):
    h, note = SRC_H[L]
    lis = "".join(f'<li><a href="{u}" rel="nofollow noopener">{html.escape(n)}</a></li>' for n, u in SRC)
    return f'<h2>{h}</h2><p class="small muted">{note}</p><ul>{lis}</ul>'


META = {
 "en": dict(key="post-pms-vs-cm", date="2026-10-08", title="PMS vs channel manager: what's the difference?",
            desc="PMS vs channel manager: what each one does, how they work together, what they cost and whether a small hotel needs both. With a comparison table and FAQ."),
 "it": dict(key="post-pms-vs-cm", date="2026-10-08", title="Channel manager cos'è e che differenza c'è con un PMS",
            desc="Channel manager e PMS: cosa fa ciascuno, come lavorano insieme, quanto costano e se una piccola struttura ha bisogno di entrambi. Con tabella e FAQ."),
 "pt": dict(key="post-pms-vs-cm", date="2026-10-08", title="O que é channel manager e qual a diferença para o PMS",
            desc="Channel manager e PMS: o que cada um faz, como funcionam juntos, quanto custam e se um hotel pequeno precisa dos dois. Com tabela comparativa e FAQ."),
 "fr": dict(key="post-pms-vs-cm", date="2026-10-08", title="PMS ou channel manager : quelle différence ?",
            desc="PMS et channel manager : rôle de chacun, fonctionnement ensemble, coûts et faut-il les deux pour un petit hôtel ? Tableau comparatif et FAQ."),
}


def en(U):
    c = f'''<div class="answer"><p><strong>Short answer:</strong> A PMS (property management system) runs the inside of your hotel: the reservation calendar, rooms, guests, housekeeping and reports. A channel manager runs the connection to the outside: it sends your availability, rates and restrictions to Booking.com, Airbnb, Expedia and other channels, and brings their bookings back. If you sell on more than one online channel, you need both functions. For a small hotel the simplest setup is usually a PMS with a built-in channel manager, so there is only one calendar and nothing to keep in sync between two systems.</p></div>
<h2>What a PMS does</h2>
<p>The PMS is the system your front desk lives in. It is the single record of who is staying, in which room, on which dates and at what price. Typical PMS jobs:</p>
<ul><li><strong>Reservation calendar (room rack):</strong> every booking on a timeline by room, with room moves, date changes and conflict checks.</li>
<li><strong>Rooms and housekeeping:</strong> clean, dirty or out-of-order status and the day's cleaning list.</li>
<li><strong>Guests:</strong> contact details, check-in data, notes and stay history.</li>
<li><strong>Direct bookings:</strong> phone, email, walk-in and repeat guests entered by staff.</li>
<li><strong>Reports:</strong> occupancy, ADR, RevPAR, revenue and cancellations.</li></ul>
<h2>What a channel manager does</h2>
<p>A channel manager is a data link between your inventory and the places that sell it. It works in two directions:</p>
<ul><li><strong>From the hotel to the channels:</strong> availability (how many rooms of each type can be sold), rates and restrictions such as minimum stay, closed to arrival, closed to departure and stop sell. The industry calls this ARI: availability, rates and inventory.</li>
<li><strong>From the channels to the hotel:</strong> new bookings, modifications and cancellations.</li></ul>
<p>When the last free room sells on Airbnb, the channel manager receives the booking and sends “0 rooms” for those dates to Booking.com and Expedia, usually within seconds. That is what prevents most double bookings; see our guide on <a href="{U("post-overbooking")}">how to prevent overbooking</a>.</p>
<h2>PMS vs channel manager at a glance</h2>
{_tbl(["", "PMS", "Channel manager"], [
  ("Main job", "Runs daily operations: calendar, rooms, guests, reports", "Distributes availability and rates to channels and imports their bookings"),
  ("Who uses it", "Front desk, housekeeping, management, accounting", "Mostly runs in the background; set up by the owner or revenue manager"),
  ("Talks to", "Your team (and, through integrations, other tools)", "OTAs, metasearch and other sales channels"),
  ("Without it", "Bookings live in spreadsheets, extranets and paper", "Availability must be updated by hand in every extranet"),
  ("Key risk if it fails", "Lost or duplicated reservations, no overview", "Overbooking and rates that differ between channels")])}
<h2>How the two work together</h2>
<p>Think of the PMS as the source of truth and the channel manager as the messenger. A typical flow:</p>
<ol><li>A guest books a double room on Booking.com for 12–14 May.</li>
<li>The channel manager receives the reservation and passes it to the PMS, where it appears on the room rack.</li>
<li>The PMS recalculates availability for double rooms on those dates.</li>
<li>The channel manager sends the new availability to every other connected channel.</li>
<li>When you later change a rate or close a date in the PMS, the same path runs in reverse.</li></ol>
<p>The weak points are the hand-offs. If the PMS and the channel manager come from different vendors, they need an interface between them, and every room type and rate plan must be mapped twice: once between the channel and the channel manager, and once between the channel manager and the PMS.</p>
<h2>Three ways to set it up</h2>
{_tbl(["Setup", "How it works", "Good for", "Watch out for"], [
  ("PMS only, no channel manager", "You update each OTA extranet by hand", "One channel, very few rooms", "Overbooking risk grows with every extra channel"),
  ("Standalone channel manager + separate PMS", "Two systems linked by an interface", "Hotels tied to an existing PMS they want to keep", "Two bills, two support desks, double mapping, sync gaps between systems"),
  ("PMS with a built-in channel manager", "One system, one calendar", "Most small and independent hotels", "Check which channels are certified and how fast sync is")])}
<h2>Do you need both?</h2>
<ul><li><strong>You sell only direct and on one OTA:</strong> a PMS is enough to start; closing dates by hand in one extranet is manageable.</li>
<li><strong>You sell on two or more online channels:</strong> you need channel manager functionality. Updating several extranets by hand is the most common cause of overbooking at independent hotels.</li>
<li><strong>You already use a PMS you like:</strong> check whether it has its own channel manager or a certified integration with one before adding a second vendor.</li>
<li><strong>You are choosing from scratch:</strong> a PMS with a built-in channel manager avoids the integration layer entirely. Our guide on <a href="{U("post-pms")}">choosing hotel management software for a small hotel</a> lists the other criteria.</li></ul>
<h2>What it costs</h2>
<p>Channel managers are priced in several ways, and some PMS vendors only include one in their higher plans. Two examples from vendors' own pricing pages (8 October 2026):</p>
<ul><li><strong>Per room and per connection:</strong> Beds24 charges a base fee, a fee per room and a fee per room type for each channel connection; its pricing page says “from €15.50” a month.</li>
<li><strong>Only in a higher plan:</strong> Sirvoy offers a free plan for one room and a Starter plan, but the channel manager is listed only in its Pro plan (€79 a month for up to 10 rooms, paid monthly).</li></ul>
<p>Other models charge a percentage of booking revenue or a fee per reservation, which grows in high season. When you compare, add up the PMS, the channel manager and any per-booking fees, then check what each channel really leaves you after commission with our <a href="{U("commission")}">OTA commission calculator</a>.</p>
<h2>Questions to ask before you decide</h2>
<ol><li>Which channels are connected, and are the connections certified by the channels themselves?</li>
<li>Is sync real-time or on a schedule? What happens if a channel is down?</li>
<li>Do rates and restrictions (minimum stay, closed to arrival or departure, stop sell) go to every channel, or only availability?</li>
<li>Do modifications and cancellations come back automatically?</li>
<li>When a room is out of order, does availability drop on the channels too?</li>
<li>Who maps room types and rate plans at setup, and is that help included?</li>
<li>Is the price flat, or does it depend on rooms, channels or bookings?</li></ol>
<h2>How it works in Hostlio Pro</h2>
<p>Hostlio Pro is a PMS with the <a href="{U("channel")}">channel manager</a> built in, on every plan. Connections to 100+ channels, including Booking.com, Airbnb, Expedia, Agoda, Trip.com and Google Hotels, run over certified links through Channex, so bookings, modifications and cancellations land on the same room rack you work in. One grid holds price, minimum and maximum stay, closed to arrival, closed to departure and stop sell for every room type and rate plan, and you can enter a whole season by date range. When a room is taken out of order, availability drops on the channels automatically. The analytics show gross revenue, commission and net for each channel.</p>
<p>There is no per-booking fee or revenue percentage: Starter costs ⟦price:starter⟧ a month, Pro ⟦price:pro⟧ and Growth ⟦price:growth⟧, with a 7-day free trial. See <a href="{U("pricing")}">pricing</a> for room limits and what each plan includes.</p>'''
    c += _src("en")
    faq = [("Is a channel manager part of a PMS?", "Sometimes. Many PMS products include a channel manager, others integrate with a separate one, and some include it only in higher plans. Check the plan details rather than the feature list."),
           ("Can I use a channel manager without a PMS?", "Yes, many standalone channel managers have a basic calendar. You will still need somewhere to manage rooms, guests, housekeeping and reports, which is the job of a PMS."),
           ("Does a channel manager stop all overbookings?", "Real-time two-way sync removes most of the risk. Direct bookings entered late, wrong room mappings and channels that are temporarily unreachable can still cause problems."),
           ("Is the channel manager included in every Hostlio Pro plan?", "Yes. Starter, Pro and Growth all include the channel manager with 100+ channels. There are no per-booking fees.")]
    return c, faq


def it(U):
    c = f'''<div class="answer"><p><strong>In breve:</strong> il PMS (property management system, il gestionale) gestisce l'interno della struttura: planning delle prenotazioni, camere, ospiti, pulizie e report. Il channel manager gestisce il collegamento con l'esterno: invia disponibilità, tariffe e restrizioni a Booking.com, Airbnb, Expedia e agli altri canali e riporta indietro le loro prenotazioni. Se vendi su più di un canale online ti servono entrambe le funzioni. Per una piccola struttura la soluzione più semplice di solito è un PMS con channel manager integrato: un solo planning e nessuna sincronizzazione da tenere allineata tra due sistemi.</p></div>
<h2>Cosa fa un PMS</h2>
<p>Il PMS è il sistema in cui lavora la reception. È l'unico registro di chi alloggia, in quale camera, in quali date e a che prezzo. Compiti tipici:</p>
<ul><li><strong>Planning delle prenotazioni (tableau):</strong> ogni prenotazione su una linea del tempo per camera, con spostamenti, modifiche di date e controllo dei conflitti.</li>
<li><strong>Camere e pulizie:</strong> stato pulita, sporca o fuori servizio e la lista delle pulizie del giorno.</li>
<li><strong>Ospiti:</strong> contatti, dati del check-in, note e storico dei soggiorni.</li>
<li><strong>Prenotazioni dirette:</strong> telefono, email, clienti al banco e ospiti abituali inseriti dallo staff.</li>
<li><strong>Report:</strong> occupazione, ADR, RevPAR, ricavi e cancellazioni.</li></ul>
<h2>Channel manager: cos'è e cosa fa</h2>
<p>Il channel manager è un collegamento dati tra il tuo inventario e i canali che lo vendono. Lavora in due direzioni:</p>
<ul><li><strong>Dalla struttura ai canali:</strong> disponibilità (quante camere di ogni tipo si possono vendere), tariffe e restrizioni come soggiorno minimo, chiusura all'arrivo, chiusura alla partenza e stop sell. Nel settore si chiama ARI: availability, rates and inventory.</li>
<li><strong>Dai canali alla struttura:</strong> nuove prenotazioni, modifiche e cancellazioni.</li></ul>
<p>Quando l'ultima camera libera viene venduta su Airbnb, il channel manager riceve la prenotazione e invia “0 camere” per quelle date a Booking.com ed Expedia, di solito in pochi secondi. È questo che evita la maggior parte delle doppie prenotazioni: vedi la guida su <a href="{U("post-overbooking")}">come evitare l'overbooking</a>.</p>
<h2>PMS e channel manager a confronto</h2>
{_tbl(["", "PMS", "Channel manager"], [
  ("Compito principale", "Gestisce l'operatività: planning, camere, ospiti, report", "Distribuisce disponibilità e tariffe ai canali e importa le loro prenotazioni"),
  ("Chi lo usa", "Reception, housekeeping, direzione, amministrazione", "Lavora soprattutto in background; lo configura il titolare o il revenue manager"),
  ("Con chi parla", "Con il tuo staff (e, tramite integrazioni, con altri strumenti)", "Con OTA, metamotori e altri canali di vendita"),
  ("Senza", "Le prenotazioni vivono tra fogli Excel, extranet e carta", "La disponibilità va aggiornata a mano in ogni extranet"),
  ("Rischio principale se non funziona", "Prenotazioni perse o duplicate, nessuna visione d'insieme", "Overbooking e tariffe diverse tra i canali")])}
<h2>Come lavorano insieme</h2>
<p>Il PMS è la fonte di verità, il channel manager è il messaggero. Un flusso tipico:</p>
<ol><li>Un ospite prenota una doppia su Booking.com dal 12 al 14 maggio.</li>
<li>Il channel manager riceve la prenotazione e la passa al PMS, dove compare sul planning.</li>
<li>Il PMS ricalcola la disponibilità delle doppie per quelle date.</li>
<li>Il channel manager invia la nuova disponibilità a tutti gli altri canali collegati.</li>
<li>Quando poi cambi una tariffa o chiudi una data nel PMS, lo stesso percorso si ripete al contrario.</li></ol>
<p>I punti deboli sono i passaggi. Se PMS e channel manager sono di fornitori diversi serve un'interfaccia tra i due, e ogni tipologia di camera e piano tariffario va mappato due volte: tra canale e channel manager, e tra channel manager e PMS.</p>
<h2>Tre configurazioni possibili</h2>
{_tbl(["Configurazione", "Come funziona", "Adatta a", "Attenzione a"], [
  ("Solo PMS, senza channel manager", "Aggiorni a mano ogni extranet", "Un solo canale, pochissime camere", "Il rischio di overbooking cresce con ogni canale in più"),
  ("Channel manager separato + PMS", "Due sistemi collegati da un'interfaccia", "Strutture legate a un PMS che vogliono tenere", "Due canoni, due assistenze, doppia mappatura, ritardi tra i sistemi"),
  ("PMS con channel manager integrato", "Un solo sistema, un solo planning", "La maggior parte delle piccole strutture indipendenti", "Verifica quali canali sono certificati e quanto è rapida la sincronizzazione")])}
<h2>Servono davvero entrambi?</h2>
<ul><li><strong>Vendi solo in diretta e su una OTA:</strong> per iniziare basta un PMS; chiudere le date a mano in un'unica extranet è gestibile.</li>
<li><strong>Vendi su due o più canali online:</strong> ti serve la funzione di channel manager. Aggiornare a mano più extranet è la causa più comune di overbooking nelle strutture indipendenti.</li>
<li><strong>Usi già un gestionale che ti piace:</strong> controlla se ha un channel manager proprio o un'integrazione certificata prima di aggiungere un secondo fornitore.</li>
<li><strong>Scegli da zero:</strong> un PMS con channel manager integrato elimina lo strato di integrazione. La guida su <a href="{U("post-pms")}">come scegliere un gestionale per piccoli hotel</a> elenca gli altri criteri.</li></ul>
<h2>Quanto costa</h2>
<p>I channel manager hanno modelli di prezzo diversi e alcuni gestionali lo includono solo nei piani più alti. Due esempi dalle pagine prezzi ufficiali (8 ottobre 2026):</p>
<ul><li><strong>Per camera e per collegamento:</strong> Beds24 applica un canone base, un importo per camera e uno per tipologia di camera per ogni canale collegato; la pagina prezzi indica “da 15,50 €” al mese.</li>
<li><strong>Solo nel piano superiore:</strong> Sirvoy ha un piano gratuito per una camera e un piano Starter, ma il channel manager è previsto solo nel piano Pro (79 € al mese fino a 10 camere, pagamento mensile).</li></ul>
<p>Altri modelli prendono una percentuale sul fatturato delle prenotazioni o una quota per prenotazione, che cresce in alta stagione. Nel confronto somma PMS, channel manager ed eventuali costi a prenotazione, poi verifica quanto ti lascia davvero ogni canale dopo la commissione con il <a href="{U("commission")}">calcolatore delle commissioni OTA</a>.</p>
<h2>Domande da fare prima di scegliere</h2>
<ol><li>Quali canali sono collegati e i collegamenti sono certificati dai canali stessi?</li>
<li>La sincronizzazione è in tempo reale o a intervalli? Cosa succede se un canale non risponde?</li>
<li>Tariffe e restrizioni (soggiorno minimo, chiusura all'arrivo o alla partenza, stop sell) arrivano a tutti i canali, o solo la disponibilità?</li>
<li>Modifiche e cancellazioni rientrano in automatico?</li>
<li>Se una camera è fuori servizio, la disponibilità scende anche sui canali?</li>
<li>Chi mappa tipologie e piani tariffari all'attivazione, ed è incluso?</li>
<li>Il prezzo è fisso o dipende da camere, canali o prenotazioni?</li></ol>
<h2>Come funziona in Hostlio Pro</h2>
<p>Hostlio Pro è un PMS con il <a href="{U("channel")}">channel manager</a> integrato in tutti i piani. I collegamenti con oltre 100 canali, tra cui Booking.com, Airbnb, Expedia, Agoda, Trip.com e Google Hotels, passano da connessioni certificate tramite Channex: prenotazioni, modifiche e cancellazioni arrivano sullo stesso planning in cui lavori. Un'unica griglia contiene prezzo, soggiorno minimo e massimo, chiusura all'arrivo, chiusura alla partenza e stop sell per ogni tipologia e piano tariffario, e puoi inserire un'intera stagione per intervallo di date. Quando metti una camera fuori servizio, la disponibilità scende in automatico sui canali. Le analisi mostrano per ogni canale ricavo lordo, commissione e netto.</p>
<p>Nessuna commissione per prenotazione né percentuale sul fatturato: Starter costa ⟦price:starter⟧ al mese, Pro ⟦price:pro⟧ e Growth ⟦price:growth⟧, con 7 giorni di prova gratuita. Limiti di camere e contenuto dei piani nella pagina <a href="{U("pricing")}">prezzi</a>.</p>'''
    c += _src("it")
    faq = [("Il channel manager fa parte del PMS?", "Dipende. Molti gestionali includono un channel manager, altri si integrano con uno esterno, altri ancora lo offrono solo nei piani più alti. Controlla il contenuto del piano, non solo l'elenco delle funzioni."),
           ("Posso usare un channel manager senza PMS?", "Sì, molti channel manager hanno un calendario di base. Ti servirà comunque uno strumento per camere, ospiti, pulizie e report, che è il compito del PMS."),
           ("Il channel manager elimina ogni overbooking?", "La sincronizzazione bidirezionale in tempo reale elimina la maggior parte del rischio. Prenotazioni dirette inserite in ritardo, mappature sbagliate e canali temporaneamente irraggiungibili possono ancora creare problemi."),
           ("Il channel manager è incluso in tutti i piani di Hostlio Pro?", "Sì. Starter, Pro e Growth includono il channel manager con oltre 100 canali, senza costi per prenotazione.")]
    return c, faq


def pt(U):
    c = f'''<div class="answer"><p><strong>Resposta curta:</strong> o PMS (property management system, o sistema de gestão do hotel) cuida da parte de dentro: mapa de reservas, quartos, hóspedes, governança e relatórios. O channel manager cuida da conexão com fora: envia disponibilidade, tarifas e restrições para Booking.com, Airbnb, Expedia e outros canais e traz as reservas de volta. Se você vende em mais de um canal online, precisa das duas funções. Para um hotel pequeno, o mais simples costuma ser um PMS com channel manager integrado: um só calendário e nada para manter sincronizado entre dois sistemas.</p></div>
<h2>O que um PMS faz</h2>
<p>O PMS é o sistema em que a recepção trabalha. É o registro único de quem está hospedado, em qual quarto, em quais datas e por qual preço. Funções típicas:</p>
<ul><li><strong>Mapa de reservas:</strong> cada reserva em uma linha do tempo por quarto, com troca de quarto, mudança de datas e verificação de conflitos.</li>
<li><strong>Quartos e governança:</strong> status limpo, sujo ou fora de serviço e a lista de limpeza do dia.</li>
<li><strong>Hóspedes:</strong> contatos, dados do check-in, observações e histórico de estadias.</li>
<li><strong>Reservas diretas:</strong> telefone, e-mail, balcão e hóspedes que voltam, lançados pela equipe.</li>
<li><strong>Relatórios:</strong> ocupação, ADR, RevPAR, receita e cancelamentos.</li></ul>
<h2>O que é channel manager e o que ele faz</h2>
<p>O channel manager é uma ponte de dados entre o seu inventário e os canais que o vendem. Funciona nos dois sentidos:</p>
<ul><li><strong>Do hotel para os canais:</strong> disponibilidade (quantos quartos de cada tipo podem ser vendidos), tarifas e restrições como estadia mínima, fechado para chegada, fechado para saída e stop sell. No setor isso se chama ARI: availability, rates and inventory.</li>
<li><strong>Dos canais para o hotel:</strong> novas reservas, alterações e cancelamentos.</li></ul>
<p>Quando o último quarto livre é vendido no Airbnb, o channel manager recebe a reserva e envia “0 quartos” para essas datas ao Booking.com e à Expedia, normalmente em segundos. É isso que evita a maior parte das reservas duplicadas; veja o guia sobre <a href="{U("post-overbooking")}">como evitar overbooking</a>.</p>
<h2>PMS x channel manager</h2>
{_tbl(["", "PMS", "Channel manager"], [
  ("Função principal", "Opera o dia a dia: mapa, quartos, hóspedes, relatórios", "Distribui disponibilidade e tarifas aos canais e importa as reservas deles"),
  ("Quem usa", "Recepção, governança, gerência, financeiro", "Roda quase sempre em segundo plano; quem configura é o dono ou o revenue manager"),
  ("Conversa com", "A sua equipe (e, por integrações, outras ferramentas)", "OTAs, metabuscadores e outros canais de venda"),
  ("Sem ele", "As reservas ficam em planilhas, extranets e papel", "A disponibilidade precisa ser atualizada à mão em cada extranet"),
  ("Principal risco se falhar", "Reservas perdidas ou duplicadas, sem visão do todo", "Overbooking e tarifas diferentes entre canais")])}
<h2>Como os dois trabalham juntos</h2>
<p>O PMS é a fonte da verdade e o channel manager é o mensageiro. Um fluxo típico:</p>
<ol><li>Um hóspede reserva um quarto duplo no Booking.com de 12 a 14 de maio.</li>
<li>O channel manager recebe a reserva e a passa ao PMS, onde ela aparece no mapa.</li>
<li>O PMS recalcula a disponibilidade de duplos nessas datas.</li>
<li>O channel manager envia a nova disponibilidade a todos os outros canais conectados.</li>
<li>Quando você muda uma tarifa ou fecha uma data no PMS, o mesmo caminho é feito no sentido contrário.</li></ol>
<p>Os pontos fracos são as passagens. Se PMS e channel manager são de fornecedores diferentes, é preciso uma interface entre eles, e cada tipo de quarto e plano tarifário tem de ser mapeado duas vezes: entre o canal e o channel manager, e entre o channel manager e o PMS.</p>
<h2>Três formas de montar</h2>
{_tbl(["Formato", "Como funciona", "Bom para", "Cuidado com"], [
  ("Só PMS, sem channel manager", "Você atualiza cada extranet à mão", "Um canal só, pouquíssimos quartos", "O risco de overbooking cresce a cada canal a mais"),
  ("Channel manager separado + PMS", "Dois sistemas ligados por uma interface", "Hotéis presos a um PMS que querem manter", "Duas mensalidades, dois suportes, mapeamento duplo, atrasos entre sistemas"),
  ("PMS com channel manager integrado", "Um sistema, um calendário", "A maioria dos hotéis pequenos e independentes", "Confira quais canais são certificados e a velocidade da sincronização")])}
<h2>Preciso dos dois?</h2>
<ul><li><strong>Você vende só direto e em uma OTA:</strong> um PMS basta para começar; fechar datas à mão em uma única extranet é administrável.</li>
<li><strong>Você vende em dois ou mais canais online:</strong> precisa da função de channel manager. Atualizar várias extranets à mão é a causa mais comum de overbooking em hotéis independentes.</li>
<li><strong>Você já usa um PMS de que gosta:</strong> veja se ele tem channel manager próprio ou integração certificada antes de contratar um segundo fornecedor.</li>
<li><strong>Você está escolhendo do zero:</strong> um PMS com channel manager integrado elimina a camada de integração. O guia sobre <a href="{U("post-pms")}">como escolher um sistema para hotel pequeno</a> traz os outros critérios.</li></ul>
<h2>Quanto custa</h2>
<p>Channel managers são cobrados de formas diferentes, e alguns PMS só o incluem nos planos mais altos. Dois exemplos das páginas de preços oficiais (8 de outubro de 2026):</p>
<ul><li><strong>Por quarto e por conexão:</strong> o Beds24 cobra uma taxa base, um valor por quarto e um valor por tipo de quarto para cada canal conectado; a página de preços fala em “a partir de 15,50 €” por mês.</li>
<li><strong>Só no plano superior:</strong> o Sirvoy tem um plano gratuito para um quarto e um plano Starter, mas o channel manager aparece apenas no plano Pro (79 € por mês para até 10 quartos, pagamento mensal).</li></ul>
<p>Outros modelos cobram uma porcentagem da receita de reservas ou uma taxa por reserva, que cresce na alta temporada. Na comparação, some PMS, channel manager e taxas por reserva e veja quanto cada canal realmente deixa depois da comissão com a <a href="{U("commission")}">calculadora de comissão de OTA</a>.</p>
<h2>Perguntas para fazer antes de decidir</h2>
<ol><li>Quais canais estão conectados e as conexões são certificadas pelos próprios canais?</li>
<li>A sincronização é em tempo real ou em intervalos? O que acontece se um canal cair?</li>
<li>Tarifas e restrições (estadia mínima, fechado para chegada ou saída, stop sell) vão para todos os canais, ou só a disponibilidade?</li>
<li>Alterações e cancelamentos voltam automaticamente?</li>
<li>Quando um quarto fica fora de serviço, a disponibilidade cai também nos canais?</li>
<li>Quem mapeia tipos de quarto e planos tarifários na implantação, e isso está incluído?</li>
<li>O preço é fixo ou depende de quartos, canais ou reservas?</li></ol>
<h2>Como funciona no Hostlio Pro</h2>
<p>O Hostlio Pro é um PMS com o <a href="{U("channel")}">channel manager</a> integrado em todos os planos. As conexões com mais de 100 canais, entre eles Booking.com, Airbnb, Expedia, Agoda, Trip.com e Google Hotels, usam ligações certificadas via Channex: reservas, alterações e cancelamentos chegam ao mesmo mapa em que você trabalha. Uma única grade reúne preço, estadia mínima e máxima, fechado para chegada, fechado para saída e stop sell para cada tipo de quarto e plano tarifário, e dá para lançar uma temporada inteira por intervalo de datas. Quando um quarto fica fora de serviço, a disponibilidade cai nos canais automaticamente. As análises mostram receita bruta, comissão e valor líquido por canal.</p>
<p>Sem taxa por reserva nem porcentagem da receita: o Starter custa ⟦price:starter⟧ por mês, o Pro ⟦price:pro⟧ e o Growth ⟦price:growth⟧, com 7 dias de teste grátis. Limites de quartos e o que cada plano inclui estão em <a href="{U("pricing")}">preços</a>.</p>'''
    c += _src("pt")
    faq = [("O channel manager faz parte do PMS?", "Depende. Muitos PMS incluem channel manager, outros se integram a um externo e alguns só o oferecem nos planos mais altos. Confira o que o plano inclui, não só a lista de funções."),
           ("Posso usar um channel manager sem PMS?", "Sim, muitos channel managers têm um calendário básico. Mesmo assim você vai precisar de um lugar para quartos, hóspedes, governança e relatórios, que é o papel do PMS."),
           ("O channel manager acaba com todo overbooking?", "A sincronização bidirecional em tempo real elimina a maior parte do risco. Reservas diretas lançadas com atraso, mapeamentos errados e canais fora do ar ainda podem causar problemas."),
           ("O channel manager está em todos os planos do Hostlio Pro?", "Sim. Starter, Pro e Growth incluem o channel manager com mais de 100 canais, sem taxa por reserva.")]
    return c, faq


def fr(U):
    c = f'''<div class="answer"><p><strong>En bref :</strong> le PMS (property management system, le logiciel de gestion hôtelière) gère l'intérieur de l'établissement : planning des réservations, chambres, clients, ménage et rapports. Le channel manager gère le lien avec l'extérieur : il envoie disponibilités, tarifs et restrictions à Booking.com, Airbnb, Expedia et aux autres canaux, et rapatrie leurs réservations. Si vous vendez sur plus d'un canal en ligne, vous avez besoin des deux fonctions. Pour un petit hôtel, le plus simple est souvent un PMS avec channel manager intégré : un seul planning et aucune synchronisation à maintenir entre deux systèmes.</p></div>
<h2>Ce que fait un PMS</h2>
<p>Le PMS est l'outil de la réception. C'est le registre unique de qui séjourne, dans quelle chambre, à quelles dates et à quel prix. Ses tâches habituelles :</p>
<ul><li><strong>Planning des réservations :</strong> chaque réservation sur une frise par chambre, avec changements de chambre, modifications de dates et contrôle des conflits.</li>
<li><strong>Chambres et ménage :</strong> statut propre, sale ou hors service et la liste du ménage du jour.</li>
<li><strong>Clients :</strong> coordonnées, données de check-in, notes et historique des séjours.</li>
<li><strong>Réservations directes :</strong> téléphone, e-mail, clients de passage et habitués, saisis par l'équipe.</li>
<li><strong>Rapports :</strong> taux d'occupation, ADR, RevPAR, chiffre d'affaires et annulations.</li></ul>
<h2>Ce que fait un channel manager</h2>
<p>Le channel manager est une passerelle de données entre votre inventaire et les canaux qui le vendent. Il fonctionne dans les deux sens :</p>
<ul><li><strong>De l'hôtel vers les canaux :</strong> disponibilités (combien de chambres de chaque type peuvent être vendues), tarifs et restrictions comme la durée minimale de séjour, la fermeture à l'arrivée, la fermeture au départ et le stop sell. Le secteur parle d'ARI : availability, rates and inventory.</li>
<li><strong>Des canaux vers l'hôtel :</strong> nouvelles réservations, modifications et annulations.</li></ul>
<p>Quand la dernière chambre libre est vendue sur Airbnb, le channel manager reçoit la réservation et envoie « 0 chambre » pour ces dates à Booking.com et Expedia, en général en quelques secondes. C'est ce qui évite la plupart des doubles réservations ; voir notre guide pour <a href="{U("post-overbooking")}">éviter la surréservation</a>.</p>
<h2>PMS et channel manager en un coup d'œil</h2>
{_tbl(["", "PMS", "Channel manager"], [
  ("Rôle principal", "Fait tourner l'exploitation : planning, chambres, clients, rapports", "Distribue disponibilités et tarifs aux canaux et importe leurs réservations"),
  ("Qui l'utilise", "Réception, gouvernante, direction, comptabilité", "Tourne surtout en arrière-plan ; paramétré par le gérant ou le revenue manager"),
  ("Parle avec", "Votre équipe (et, via des intégrations, d'autres outils)", "Les OTA, les métamoteurs et les autres canaux de vente"),
  ("Sans lui", "Les réservations vivent dans des tableurs, des extranets et sur papier", "Les disponibilités se mettent à jour à la main dans chaque extranet"),
  ("Risque principal en cas de panne", "Réservations perdues ou en double, pas de vue d'ensemble", "Surréservation et tarifs différents selon les canaux")])}
<h2>Comment ils fonctionnent ensemble</h2>
<p>Le PMS est la source de vérité, le channel manager le messager. Un parcours type :</p>
<ol><li>Un client réserve une chambre double sur Booking.com du 12 au 14 mai.</li>
<li>Le channel manager reçoit la réservation et la transmet au PMS, où elle apparaît sur le planning.</li>
<li>Le PMS recalcule la disponibilité des doubles à ces dates.</li>
<li>Le channel manager envoie la nouvelle disponibilité à tous les autres canaux connectés.</li>
<li>Quand vous modifiez ensuite un tarif ou fermez une date dans le PMS, le même chemin se fait en sens inverse.</li></ol>
<p>Les points faibles sont les passages de relais. Si le PMS et le channel manager viennent de deux éditeurs différents, il faut une interface entre eux, et chaque type de chambre et plan tarifaire doit être mappé deux fois : entre le canal et le channel manager, puis entre le channel manager et le PMS.</p>
<h2>Trois façons de s'organiser</h2>
{_tbl(["Organisation", "Fonctionnement", "Convient à", "Points de vigilance"], [
  ("PMS seul, sans channel manager", "Vous mettez à jour chaque extranet à la main", "Un seul canal, très peu de chambres", "Le risque de surréservation augmente avec chaque canal ajouté"),
  ("Channel manager séparé + PMS", "Deux systèmes reliés par une interface", "Hôtels attachés à un PMS qu'ils veulent garder", "Deux abonnements, deux supports, double mapping, décalages entre systèmes"),
  ("PMS avec channel manager intégré", "Un seul système, un seul planning", "La plupart des petits hôtels indépendants", "Vérifiez quels canaux sont certifiés et la rapidité de synchronisation")])}
<h2>Faut-il les deux ?</h2>
<ul><li><strong>Vous vendez en direct et sur une seule OTA :</strong> un PMS suffit pour commencer ; fermer des dates à la main dans un extranet reste gérable.</li>
<li><strong>Vous vendez sur deux canaux en ligne ou plus :</strong> il vous faut la fonction channel manager. Mettre à jour plusieurs extranets à la main est la cause de surréservation la plus fréquente dans les hôtels indépendants.</li>
<li><strong>Vous utilisez déjà un PMS qui vous convient :</strong> vérifiez s'il a son propre channel manager ou une intégration certifiée avant d'ajouter un second éditeur.</li>
<li><strong>Vous partez de zéro :</strong> un PMS avec channel manager intégré supprime la couche d'intégration. Notre guide pour <a href="{U("post-pms")}">choisir un logiciel de gestion hôtelière pour un petit hôtel</a> détaille les autres critères.</li></ul>
<h2>Combien ça coûte</h2>
<p>Les channel managers sont facturés de plusieurs façons, et certains PMS ne l'incluent que dans leurs offres supérieures. Deux exemples tirés des pages tarifs officielles (8 octobre 2026) :</p>
<ul><li><strong>Par chambre et par connexion :</strong> Beds24 facture un forfait de base, un montant par chambre et un montant par type de chambre pour chaque canal connecté ; sa page tarifs annonce « à partir de 15,50 € » par mois.</li>
<li><strong>Seulement dans l'offre supérieure :</strong> Sirvoy propose une offre gratuite pour une chambre et une offre Starter, mais le channel manager ne figure que dans l'offre Pro (79 € par mois jusqu'à 10 chambres, paiement mensuel).</li></ul>
<p>D'autres modèles prennent un pourcentage du chiffre d'affaires des réservations ou des frais par réservation, qui augmentent en haute saison. Pour comparer, additionnez PMS, channel manager et frais par réservation, puis vérifiez ce que chaque canal vous laisse vraiment après commission avec notre <a href="{U("commission")}">calculateur de commission OTA</a>.</p>
<h2>Les questions à poser avant de choisir</h2>
<ol><li>Quels canaux sont connectés, et les connexions sont-elles certifiées par les canaux eux-mêmes ?</li>
<li>La synchronisation est-elle en temps réel ou par intervalles ? Que se passe-t-il si un canal ne répond pas ?</li>
<li>Les tarifs et restrictions (durée minimale, fermeture à l'arrivée ou au départ, stop sell) partent-ils vers tous les canaux, ou seulement les disponibilités ?</li>
<li>Les modifications et annulations reviennent-elles automatiquement ?</li>
<li>Quand une chambre est hors service, la disponibilité baisse-t-elle aussi sur les canaux ?</li>
<li>Qui mappe types de chambres et plans tarifaires à la mise en place, et est-ce inclus ?</li>
<li>Le prix est-il fixe, ou dépend-il des chambres, des canaux ou des réservations ?</li></ol>
<h2>Comment ça marche dans Hostlio Pro</h2>
<p>Hostlio Pro est un PMS avec le <a href="{U("channel")}">channel manager</a> intégré dans toutes les offres. Les connexions à plus de 100 canaux, dont Booking.com, Airbnb, Expedia, Agoda, Trip.com et Google Hotels, passent par des liaisons certifiées via Channex : réservations, modifications et annulations arrivent sur le planning où vous travaillez. Une seule grille réunit prix, durée minimale et maximale, fermeture à l'arrivée, fermeture au départ et stop sell pour chaque type de chambre et plan tarifaire, et vous saisissez une saison entière par plage de dates. Quand une chambre passe hors service, la disponibilité baisse automatiquement sur les canaux. Les analyses affichent pour chaque canal le chiffre d'affaires brut, la commission et le net.</p>
<p>Pas de frais par réservation ni de pourcentage du chiffre d'affaires : Starter coûte ⟦price:starter⟧ par mois, Pro ⟦price:pro⟧ et Growth ⟦price:growth⟧, avec 7 jours d'essai gratuit. Limites de chambres et contenu des offres sur la page <a href="{U("pricing")}">tarifs</a>.</p>'''
    c += _src("fr")
    faq = [("Le channel manager fait-il partie du PMS ?", "Cela dépend. Beaucoup de PMS incluent un channel manager, d'autres s'intègrent à un outil externe, certains ne l'offrent que dans leurs offres supérieures. Vérifiez le contenu de l'offre, pas seulement la liste des fonctions."),
           ("Peut-on utiliser un channel manager sans PMS ?", "Oui, beaucoup de channel managers ont un calendrier de base. Il vous faudra quand même un outil pour les chambres, les clients, le ménage et les rapports : c'est le rôle du PMS."),
           ("Un channel manager évite-t-il toute surréservation ?", "La synchronisation bidirectionnelle en temps réel supprime l'essentiel du risque. Des réservations directes saisies en retard, un mapping erroné ou un canal momentanément injoignable peuvent encore poser problème."),
           ("Le channel manager est-il inclus dans toutes les offres Hostlio Pro ?", "Oui. Starter, Pro et Growth incluent le channel manager avec plus de 100 canaux, sans frais par réservation.")]
    return c, faq


FN = {"en": en, "it": it, "pt": pt, "fr": fr}
