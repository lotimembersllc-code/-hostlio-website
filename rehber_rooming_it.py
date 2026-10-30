"""Takvim yazısı: "Rooming list: cos'è e come gestirla" — yalnız IT. GSC: "rooming list cos'è" ~70. sıra (yazı yokken).
Kaynaklar 16 Ekim 2026: D.M. Interno 7.1.2013 (gruppi guidati: capogruppo + elenco; tipi 16–20), manuale Alloggiati Web (Questura),
art. 109 TULPS, Roma Del. A.C. 34/2024 art. 5 c.2 lett. c (autisti/accompagnatori), sözleşme dili (Law Insider), Mews/WuBook açıklamaları.
Cut-off/release gün sayıları ve attrition yüzdeleri doğrulanamadı → rakam verilmez. Hostlio'da ayrı grup/rooming list özelliği YOK → iddia edilmez."""
import html

SRC = [
 ("Gazzetta Ufficiale: D.M. Interno 7 gennaio 2013", "https://www.gazzettaufficiale.it/eli/id/2013/01/17/13A00360/sg"),
 ("Alloggiati Web: D.M. 7 gennaio 2013 (PDF)", "https://alloggiatiweb.poliziadistato.it/PortaleAlloggiati/Download/Normativa/2013_DM.pdf"),
 ("Polizia di Stato: manuale Alloggiati Web per le strutture", "https://questure.poliziadistato.it/statics/38/3678_5574.pdf"),
 ("Normattiva: TULPS (R.D. 773/1931), art. 109", "https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:regio.decreto:1931-06-18;773~art109"),
 ("Roma Capitale: regolamento sul contributo di soggiorno (Del. A.C. 34/2024)", "https://www.comune.roma.it/web-resources/cms/documents/Assemblea_Capitolina_34_2024.pdf"),
 ("Law Insider: rooming list (clausole contrattuali)", "https://www.lawinsider.com/dictionary/rooming-list"),
 ("Mews: la lista delle camere d'albergo", "https://www.mews.com/it/blog/lista-delle-camere-dalbergo"),
 ("AltexSoft: rooming list (glossario)", "https://www.altexsoft.com/glossary/rooming-list/"),
]

def _tbl(head, rows):
    h = "".join(f'<th scope="col">{x}</th>' for x in head)
    b = "".join("<tr>" + f'<th scope="row">{r[0]}</th>' + "".join(f"<td>{c}</td>" for c in r[1:]) + "</tr>" for r in rows)
    return f'<div class="table-wrap"><table class="cmp"><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table></div>'

META = {"it": dict(key="post-rooming", date="2026-10-16", title="Rooming list: cos'è e come gestirla in hotel (2026)",
                   desc="Rooming list: significato, cosa contiene, chi la invia e quando, release e allotment, Alloggiati Web per i gruppi (capogruppo) e un modello pronto.")}

def it(U):
    from build import btn, SIGNUP_URL
    cta = btn("Prova gratis per ⟦trial⟧ giorni", SIGNUP_URL) + btn("Vedi il calendario prenotazioni", U("features"), "ghost")
    modello = _tbl(["Camera", "Tipologia", "Ospiti", "Arrivo", "Partenza", "Trattamento", "Addebito", "Note"], [
        ("1", "Doppia", "Rossi Mario, Rossi Anna", "12/05", "15/05", "B&amp;B", "Agenzia", "Letto matrimoniale"),
        ("2", "Twin", "Bianchi Luca, Verdi Paolo", "12/05", "15/05", "B&amp;B", "Agenzia", "Celiaco (Verdi)"),
        ("3", "Singola", "Neri Giulia (capogruppo)", "12/05", "15/05", "B&amp;B", "Extra a carico ospite", "Piano basso"),
        ("4", "Singola", "Autista", "12/05", "15/05", "B&amp;B", "Agenzia", "Esente imposta? Verifica regolamento")])
    allog = _tbl(["Tipo alloggiato", "Codice", "Dati richiesti"], [
        ("Capo gruppo", "18", "Dati anagrafici completi e documento d'identità (tipo, numero, luogo di rilascio); deve essere maggiorenne"),
        ("Membro gruppo", "20", "Cognome, nome, sesso, data e luogo di nascita, cittadinanza; nessun dato del documento"),
        ("Capo famiglia / Familiare", "17 / 19", "Stessa logica per i nuclei familiari"),
        ("Ospite singolo", "16", "Dati completi e documento")])
    c = f'''<div class="answer"><p><strong>In breve:</strong> la rooming list è l'elenco degli ospiti di una prenotazione di gruppo con la camera assegnata a ciascuno. La invia l'agenzia, il tour operator o l'organizzatore dell'evento, di solito entro una data concordata nel contratto (cut-off o release). Contiene nomi, tipologia di camera, chi dorme con chi, date di arrivo e partenza, trattamento, chi paga cosa e richieste speciali. In Italia serve anche per la comunicazione su Alloggiati Web: per i gruppi guidati basta il documento del capogruppo, ma ogni membro va comunque registrato.</p></div>
<p class="small muted">Guida informativa, non consulenza legale. Fonti normative e di settore consultate il 16 ottobre 2026; i termini contrattuali (cut-off, release, penali) dipendono dal tuo contratto.</p>
<h2>Rooming list: significato</h2>
<p>Letteralmente "lista delle camere". Nei contratti per gruppi è il documento con cui l'organizzatore comunica all'hotel chi occuperà ciascuna camera del blocco. Finché la rooming list non arriva, l'hotel conosce solo il numero e il tipo di camere opzionate; con la rooming list le camere diventano prenotazioni nominative.</p>
<h2>Cosa contiene</h2>
<ul><li>nome e cognome di ogni ospite e chi divide la camera con chi;</li>
<li>tipologia di camera (singola, doppia, twin, tripla) ed eventuali camere comunicanti;</li>
<li>date di arrivo e partenza, anche diverse per alcuni partecipanti;</li>
<li>trattamento (solo pernottamento, B&amp;B, mezza pensione);</li>
<li>istruzioni di addebito: cosa paga l'agenzia (conto master) e cosa paga l'ospite (extra);</li>
<li>richieste speciali: letti, allergie e diete, accessibilità;</li>
<li>contatti del capogruppo o dell'accompagnatore.</li></ul>
<h2>Un modello di rooming list</h2>
{modello}
<p>Conviene mandare all'organizzatore un modello già pronto, con le stesse colonne del tuo gestionale: riduci errori di copiatura e nomi scritti in modo diverso.</p>
<h2>Chi la invia e quando: allotment, release e cut-off</h2>
<p>Nei contratti di gruppo l'hotel blocca un certo numero di camere (allotment). Il contratto fissa una data entro cui l'organizzatore deve inviare la rooming list: le camere non nominate entro quella data tornano in vendita. Una clausola tipica dice che tutte le prenotazioni vanno fatte tramite rooming list entro la data di cut-off e che la parte di allotment non coperta viene automaticamente rilasciata all'hotel. I giorni di release, le penali e la percentuale di camere che il gruppo può cancellare senza costi (attrition) variano da contratto a contratto: scrivili sempre in modo esplicito.</p>
<h2>Rooming list e Alloggiati Web</h2>
<p>L'articolo 109 del TULPS impone di alloggiare solo ospiti con un documento valido e di comunicarne i dati alla Questura tramite <a href="{U("post-alloggiati")}">Alloggiati Web</a>. Per i gruppi il D.M. 7 gennaio 2013 prevede una semplificazione: "Per i gruppi guidati è sufficiente la compilazione da parte del capogruppo, che indicherà l'elenco degli altri componenti del gruppo."</p>
{allog}
<p>Nel file di invio le righe dei membri devono seguire subito quella del capogruppo, con la stessa data di arrivo. Attenzione: la semplificazione vale per i gruppi <em>guidati</em>. Ogni ospite deve comunque avere un documento valido, che l'hotel è tenuto a verificare. Per questo la rooming list dovrebbe includere data e luogo di nascita e cittadinanza di tutti i partecipanti: senza questi dati non puoi inviare le schedine.</p>
<h2>Imposta di soggiorno per i gruppi</h2>
<p>Molti comuni prevedono esenzioni per autisti e accompagnatori. A Roma, per esempio, sono esenti gli autisti di pullman e un accompagnatore turistico ogni 25 partecipanti per i gruppi organizzati da agenzie, previa dichiarazione sostitutiva. Le regole cambiano da comune a comune: controlla il regolamento del tuo. Ne parliamo nella guida all'<a href="{U("post-soggiorno")}">imposta di soggiorno</a>.</p>
<h2>Gli errori più comuni</h2>
<ul><li><strong>Rooming list in ritardo:</strong> fissa il cut-off nel contratto e ricordalo all'organizzatore una settimana prima.</li>
<li><strong>Cambi di nome dell'ultimo minuto:</strong> chiedi che arrivino per iscritto e aggiorna subito le prenotazioni.</li>
<li><strong>No-show nel gruppo:</strong> definisci nel contratto se la prima notte è garantita.</li>
<li><strong>Doppio inserimento:</strong> se una parte del gruppo prenota anche da OTA, rischi l'overbooking. Leggi <a href="{U("post-overbooking")}">come evitare l'overbooking</a>.</li>
<li><strong>Dati mancanti per la Questura:</strong> senza data e luogo di nascita dei membri non puoi completare Alloggiati Web in tempo.</li></ul>
<h2>Gestire la rooming list con un gestionale</h2>
<p>Con un <a href="{U("t-guesthouse")}">gestionale</a> ogni camera della rooming list diventa una prenotazione nel calendario: vedi subito quali camere sono bloccate, quali sono ancora libere e quali puoi rimettere in vendita dopo il release. In Hostlio Pro inserisci le camere del gruppo nel calendario prenotazioni e il <a href="{U("channel")}">channel manager</a> aggiorna la disponibilità sulle OTA, così le camere del gruppo non vengono vendute due volte. Hostlio Pro non ha ancora una funzione dedicata per importare la rooming list da Excel: le camere si inseriscono una per una.</p>
<div class="cta-row" style="margin-top:12px">{cta}</div>
'''
    lis = "".join(f'<li><a href="{u}" rel="nofollow noopener">{html.escape(n)}</a></li>' for n, u in SRC)
    c += f'<h2>Fonti</h2><p class="small muted">Fonti consultate il 16 ottobre 2026.</p><ul>{lis}</ul>'
    faq = [("Cos'è una rooming list?", "È l'elenco degli ospiti di una prenotazione di gruppo con la camera assegnata a ciascuno, inviato all'hotel dall'agenzia, dal tour operator o dall'organizzatore."),
           ("Cosa significa release in una rooming list?", "È la data, fissata nel contratto, entro cui l'organizzatore deve nominare le camere; quelle non coperte dalla rooming list tornano in vendita."),
           ("Per un gruppo bisogna registrare tutti su Alloggiati Web?", "Sì. Per i gruppi guidati basta il documento del capogruppo (tipo 18), ma ogni membro va inserito come membro gruppo (tipo 20) con i dati anagrafici."),
           ("Hostlio Pro importa la rooming list da Excel?", "Non ancora. Le camere del gruppo si inseriscono nel calendario prenotazioni e il channel manager aggiorna la disponibilità sulle OTA.")]
    return c, faq

FN = {"it": it}
