"""Takvim yazısı (21 Ekim 2026 planı): "Alloggiati Web: guida per hotel e B&B" — yalnız IT.
Resmî kaynaklar 12 Ekim 2026: TULPS art. 109 + art. 17 (Normattiva), D.M. Interno 7/1/2013 ve 16/9/2021 (GU 14.10.2021:
≤24 saatlik konaklamada 6 saat), portal PDF'leri, Consiglio di Stato Sez. III n. 9101/2025 (circolare 18.11.2024 geçerli).
Hostlio Alloggiati'ye GÖNDERMEZ — metin bunu açıkça söyler; ceza tutarı (€) resmî kaynakta doğrulanmadı, yazılmadı."""
import html

SRC = [
 ("Normattiva: TULPS (R.D. 773/1931), art. 109 e art. 17", "https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:regio.decreto:1931-06-18;773~art109"),
 ("Gazzetta Ufficiale: D.M. Interno 16 settembre 2021 (GU n. 246 del 14 ottobre 2021)", "https://www.gazzettaufficiale.it/atto/serie_generale/caricaDettaglioAtto/originario?atto.dataPubblicazioneGazzetta=2021-10-14&atto.codiceRedazionale=21A06000"),
 ("Alloggiati Web: D.M. 7 gennaio 2013", "https://alloggiatiweb.poliziadistato.it/PortaleAlloggiati/Download/Normativa/2013_DM.pdf"),
 ("Alloggiati Web: informazioni generali", "https://alloggiatiweb.poliziadistato.it/PortaleAlloggiati/Download/Info/InfoGen.pdf"),
 ("Alloggiati Web: ricevute digitali", "https://alloggiatiweb.poliziadistato.it/PortaleAlloggiati/Download/Info/RICDIGALLO.pdf"),
 ("Alloggiati Web: manuale web service", "https://alloggiatiweb.poliziadistato.it/PortaleAlloggiati/Download/Manuali/MANUALEWS.pdf"),
 ("Consiglio di Stato, Sez. III, sentenza n. 9101/2025", "https://mdp.giustizia-amministrativa.it/visualizza/?nodeRef=&schema=cds&nrg=202505732&nomeFile=202509101_11.html&subDir=Provvedimenti"),
 ("Questura di Oristano: comunicazione alloggiati", "https://questure.poliziadistato.it/it/Oristano/articolo/9025c93a2332b98e686663089"),
 ("Ministero del Turismo: CIN", "https://www.ministeroturismo.gov.it/cin-termine-per-lacquisizione-spostato-al-1-gennaio-2025/"),
]

META = {"it": dict(key="post-alloggiati", date="2026-10-12", title="Alloggiati Web: guida 2026 per hotel, B&B e affitti brevi",
                   desc="Alloggiati Web nel 2026: chi deve comunicare, entro 24 ore (6 per soggiorni brevi), quali dati, credenziali, self check-in e sanzioni. Fonti ufficiali.")}

def it(U):
    from build import btn, SIGNUP_URL
    cta = btn("Prova gratis per ⟦trial⟧ giorni", SIGNUP_URL) + btn("Vedi il check-in online", U("checkin"), "ghost")
    c = f'''<div class="answer"><p><strong>In breve:</strong> chi ospita persone a pagamento in Italia (hotel, B&amp;B, affittacamere, case vacanza e anche i privati che affittano per meno di 30 giorni) deve comunicare le generalità di ogni ospite alla Questura tramite il portale <strong>Alloggiati Web</strong> della Polizia di Stato. Il termine è di <strong>24 ore dall'arrivo</strong>, che diventano <strong>6 ore</strong> per i soggiorni non superiori alle 24 ore. Le credenziali si chiedono alla Questura della provincia, l'invio è gratuito e la ricevuta va conservata per cinque anni.</p></div>
<p class="small muted">Questa guida ha scopo informativo e non è una consulenza legale. Le informazioni sono tratte da fonti ufficiali (Normattiva, Gazzetta Ufficiale, portale Alloggiati Web, Consiglio di Stato) consultate il 12 ottobre 2026. Le modalità di richiesta delle credenziali cambiano da Questura a Questura: verifica sempre la pagina della tua.</p>
<h2>Chi deve comunicare gli ospiti</h2>
<p>L'obbligo nasce dall'articolo 109 del Testo unico delle leggi di pubblica sicurezza (TULPS, R.D. 773/1931). Riguarda i gestori di alberghi e di altre strutture ricettive, compresi campeggi, case e appartamenti per vacanze, affittacamere e strutture di accoglienza non convenzionali. Dal 2018 vale espressamente anche per chi affitta o subaffitta immobili, o parti di essi, con contratti di durata inferiore a trenta giorni: quindi anche per i privati con affitti brevi. Si possono ospitare solo persone munite di carta d'identità o di altro documento valido; per gli stranieri extra UE va bene il passaporto o un documento equipollente con fotografia.</p>
<h2>Entro quando: 24 ore, oppure 6 ore</h2>
<ul><li><strong>Regola generale:</strong> entro le 24 ore successive all'arrivo.</li>
<li><strong>Soggiorni non superiori alle 24 ore:</strong> entro le 6 ore successive all'arrivo. La regola è stata introdotta dal D.L. 53/2019 e resa operativa dal D.M. 16 settembre 2021, in vigore dal 2022.</li>
<li><strong>Se il portale non funziona:</strong> la comunicazione si fa alla Questura via fax o PEC.</li></ul>
<p>Attenzione: alcune pagine ufficiali, compresa la home del portale, riportano ancora la vecchia dicitura "all'arrivo" per i soggiorni brevi. Il testo vigente del decreto parla di sei ore.</p>
<h2>Quali dati inviare</h2>
<p>Per ogni ospite si comunicano data di arrivo, numero di notti, cognome, nome, sesso, data e luogo di nascita (comune e provincia, oppure Stato estero), cittadinanza e i dati del documento: tipo, numero e luogo di rilascio.</p>
<ul><li><strong>Famiglie:</strong> basta il documento di uno dei coniugi, che indica i dati dell'altro coniuge e dei figli minorenni.</li>
<li><strong>Gruppi guidati:</strong> vale lo stesso per il capogruppo.</li>
<li><strong>Familiari e membri del gruppo:</strong> si inviano notti, cognome, nome, sesso, data e luogo di nascita e cittadinanza, senza dati del documento. Nel file vanno subito dopo il capofamiglia o il capogruppo, con la stessa data di arrivo.</li></ul>
<h2>Come ottenere le credenziali</h2>
<ol><li><strong>Richiesta alla Questura</strong> della provincia in cui si trova la struttura. Moduli e modalità variano: alcune Questure vogliono la consegna di persona con copia del documento del titolare, altre accettano solo la PEC.</li>
<li><strong>Accesso al portale</strong> con nome utente, password e codice monouso (autenticazione a due fattori).</li>
<li><strong>Uso personale:</strong> le credenziali le usa il gestore, oppure un soggetto identificato e appositamente incaricato della trasmissione.</li></ol>
<p>L'invio è gratuito.</p>
<h2>Tre modi per inviare le schedine</h2>
<ul><li><strong>Inserimento online,</strong> una schedina alla volta: comodo per poche presenze.</li>
<li><strong>Caricamento di un file di testo</strong> con una riga per ospite e campi a lunghezza fissa. Gli hotel usano un tracciato, case vacanza e affittacamere un altro, con il campo dell'appartamento.</li>
<li><strong>Web service</strong> (servizi di cooperazione applicativa) per i software gestionali che inviano direttamente, con una chiave generata nel portale.</li></ul>
<h2>La ricevuta: scaricala e conservala 5 anni</h2>
<p>Dopo l'invio il portale genera una ricevuta, che va <strong>conservata per cinque anni</strong>. Il portale la tiene online solo per gli ultimi 30 giorni, quindi conviene scaricarla subito. Una volta generata la ricevuta, i dati digitali trasmessi e le eventuali copie cartacee di fax o PEC vanno cancellati o distrutti.</p>
<h2>Self check-in e keybox: cosa dice il Consiglio di Stato</h2>
<p>Con la circolare del 18 novembre 2024 il Ministero dell'Interno ha chiarito che il check-in totalmente a distanza (invio della copia del documento e codice della porta o keybox) non basta: il gestore deve verificare <em>de visu</em> che l'ospite corrisponda al documento. Il TAR Lazio aveva annullato la circolare, ma il <strong>Consiglio di Stato (Sez. III, sentenza n. 9101/2025)</strong> ha accolto l'appello del Ministero: la circolare è di nuovo pienamente valida.</p>
<p>Nella stessa sentenza il Consiglio di Stato osserva che la verifica può avvenire anche con dispositivi di videocollegamento all'ingresso della struttura, purché permettano di accertare in quel momento la corrispondenza tra ospite e documento. Sono invece escluse le procedure di check-in remoto più estreme. In pratica: il check-in online va benissimo per raccogliere i dati in anticipo, ma l'identificazione dell'ospite va fatta all'arrivo.</p>
<h2>Sanzioni</h2>
<p>La mancata comunicazione non è una semplice sanzione amministrativa: per la violazione dell'art. 109 si applica l'art. 17 del TULPS, che prevede l'arresto fino a tre mesi o l'ammenda. È quindi un reato contravvenzionale. Per l'importo esatto dell'ammenda e per il tuo caso specifico rivolgiti a un professionista.</p>
<h2>Obblighi da non confondere</h2>
<ul><li><strong>CIN:</strong> il codice identificativo nazionale si richiede sul portale BDSR del Ministero del Turismo ed è separato da Alloggiati Web.</li>
<li><strong>Imposta di soggiorno:</strong> la stabilisce e la riscuote il comune, con regole proprie.</li>
<li><strong>Statistiche turistiche (ISTAT):</strong> si inviano tramite i sistemi regionali, diversi da regione a regione.</li></ul>
<h2>Come ti aiuta Hostlio Pro (e cosa non fa)</h2>
<p>Con il <a href="{U("checkin")}">check-in online</a> di Hostlio Pro l'ospite compila i propri dati prima dell'arrivo e può scansionare il documento dal telefono: la lettura avviene sul dispositivo e non viene salvata alcuna immagine. Così, al banco, i dati sono già pronti e ti resta solo l'identificazione di persona. Per essere chiari: <strong>Hostlio Pro non invia i dati ad Alloggiati Web</strong>. La comunicazione alla Questura resta a tuo carico e va fatta tramite il portale ufficiale.</p>
<div class="cta-row" style="margin-top:12px">{cta}</div>
<p>Per scegliere un gestionale che si adatti a questi obblighi leggi anche <a href="{U("post-pms")}">come scegliere un gestionale per piccoli hotel</a>.</p>
'''
    lis = "".join(f'<li><a href="{u}" rel="nofollow noopener">{html.escape(n)}</a></li>' for n, u in SRC)
    c += f'<h2>Fonti</h2><p class="small muted">Tutte le fonti sono state consultate il 12 ottobre 2026.</p><ul>{lis}</ul>'
    faq = [("Entro quanto tempo bisogna comunicare gli ospiti ad Alloggiati Web?", "Entro 24 ore dall'arrivo. Per i soggiorni non superiori alle 24 ore il termine è di 6 ore dall'arrivo (D.M. Interno 16 settembre 2021)."),
           ("Anche chi fa affitti brevi deve usare Alloggiati Web?", "Sì. Dal 2018 l'obbligo dell'art. 109 TULPS vale anche per chi affitta o subaffitta immobili con contratti inferiori a 30 giorni, quindi anche per i privati."),
           ("Il self check-in con keybox è vietato?", "Il check-in totalmente a distanza non basta: secondo la circolare del 18 novembre 2024, confermata dal Consiglio di Stato con la sentenza n. 9101/2025, il gestore deve verificare de visu l'identità dell'ospite. La sentenza ammette anche sistemi di videocollegamento all'ingresso, se permettono il controllo in quel momento."),
           ("Per quanto tempo va conservata la ricevuta di Alloggiati Web?", "Cinque anni. Il portale la mantiene online solo 30 giorni, quindi va scaricata subito dopo l'invio."),
           ("Hostlio Pro invia i dati ad Alloggiati Web?", "No. Il check-in online di Hostlio Pro raccoglie e organizza i dati degli ospiti prima dell'arrivo, ma la comunicazione alla Questura va effettuata tramite il portale Alloggiati Web.")]
    return c, faq

FN = {"it": it}
