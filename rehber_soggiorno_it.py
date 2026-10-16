"""Takvim yazısı: "Imposta di soggiorno 2026: calcolo, versamento e dichiarazione" — yalnız IT.
Resmî kaynaklar 16 Ekim 2026: D.Lgs. 23/2011 art. 4 (c.1, 1-bis, 1-ter, 3), DL 34/2020 art. 180, D.Lgs. 147/2026 art. 12 (yeni cezalar
1.1.2027'den), DM MEF 29.4.2022 (model), MEF/finanze.gov.it, Agenzia Entrate, Comune di Milano tarifeleri 2026, Roma regolamento.
Roma tarifeleri doğrulanamadı → yazılmaz. Hostlio vergiyi hesaplamaz/beyan etmez."""
import html

SRC = [
 ("Normattiva: D.Lgs. 23/2011, art. 4", "https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2011-03-14;23~art4"),
 ("Normattiva: DL 34/2020, art. 180", "https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2020-05-19;34~art180"),
 ("Normattiva: D.Lgs. 147/2026, art. 12", "https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2026-08-07;147~art12"),
 ("MEF: imposta di soggiorno, disciplina del tributo", "https://www.finanze.gov.it/it/fiscalita/fiscalita-regionale-e-locale/TARI-Imposta-di-soggiorno-e-altri-tributi-comunali/imposta-di-soggiorno/Disciplina-del-tributo/"),
 ("MEF: dichiarazione telematica dell'imposta di soggiorno", "https://www.finanze.gov.it/it/fiscalita/fiscalita-regionale-e-locale/TARI-Imposta-di-soggiorno-e-altri-tributi-comunali/imposta-di-soggiorno/dichiarazione-telematica-imposta-di-soggiorno/"),
 ("Gazzetta Ufficiale: DM 29 aprile 2022 (modello di dichiarazione)", "https://www.gazzettaufficiale.it/atto/serie_generale/caricaDettaglioAtto/originario?atto.dataPubblicazioneGazzetta=2022-05-12&atto.codiceRedazionale=22A02828"),
 ("Comune di Milano: tariffe 2026", "https://www.comune.milano.it/documents/20118/1016509/Tariffe+2026+decorrenza+1%C2%B0aprile+2026.pdf/d101078f-26b0-4446-d16b-787845b76bca?version=1.1&t=1771602332605&download=true"),
 ("Roma Capitale: regolamento (Del. A.C. 34/2024)", "https://www.comune.roma.it/web-resources/cms/documents/Assemblea_Capitolina_34_2024.pdf"),
 ("Normattiva: DL 50/2017, art. 4 (locazioni brevi)", "https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2017-04-24;50~art4"),
]

def _tbl(head, rows):
    h = "".join(f'<th scope="col">{x}</th>' for x in head)
    b = "".join("<tr>" + f'<th scope="row">{r[0]}</th>' + "".join(f"<td>{c}</td>" for c in r[1:]) + "</tr>" for r in rows)
    return f'<div class="table-wrap"><table class="cmp"><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table></div>'

META = {"it": dict(key="post-soggiorno", date="2026-10-16", title="Imposta di soggiorno 2026: calcolo, versamento e dichiarazione",
                   desc="Imposta di soggiorno 2026 per hotel e B&B: chi la applica, quanto (fino a 10 € +2 €), il gestore responsabile, dichiarazione entro il 30 giugno, sanzioni 2027.")}

def it(U):
    from build import btn, SIGNUP_URL
    cta = btn("Prova gratis per ⟦trial⟧ giorni", SIGNUP_URL) + btn("Vedi il gestionale", U("features"), "ghost")
    milano = _tbl(["Struttura (Milano, dal 1° aprile 2026)", "Per persona e per notte"], [
        ("Hotel 1 stella", "3,00&nbsp;€"), ("Hotel 2 stelle", "4,00&nbsp;€"), ("Hotel 3 stelle", "7,00&nbsp;€"),
        ("Hotel 4 stelle", "10,00&nbsp;€"), ("Hotel 5 stelle", "12,00&nbsp;€"),
        ("B&amp;B, affittacamere, case vacanza, locazioni brevi", "9,50&nbsp;€"), ("Ostelli, strutture all'aria aperta", "3,00&nbsp;€")])
    sanz = _tbl(["Violazione", "Fino al 31 dicembre 2026", "Dal 1° gennaio 2027"], [
        ("Omessa dichiarazione", "Dal 100% al 200% dell'importo dovuto", "100% del tributo non versato, minimo 50&nbsp;€"),
        ("Dichiarazione infedele", "Dal 100% al 200% dell'importo dovuto", "40% del tributo, minimo 50&nbsp;€"),
        ("Omesso o tardivo versamento", "Art. 13 D.Lgs. 471/1997 e regolamento comunale", "Art. 13 D.Lgs. 471/1997 e regolamento comunale")])
    c = f'''<div class="answer"><p><strong>In breve:</strong> l'imposta di soggiorno la decide ogni comune che l'ha istituita, fino a 5&nbsp;€ per persona e per notte (10&nbsp;€ nelle città più turistiche), con un aumento facoltativo fino a 2&nbsp;€ prorogato anche per il 2026. Il gestore della struttura la incassa dall'ospite ed è <strong>responsabile del pagamento</strong>: la versa al comune nei tempi del regolamento comunale e presenta ogni anno, <strong>entro il 30 giugno</strong>, la dichiarazione telematica all'Agenzia delle Entrate. Dal 1° gennaio 2027 cambiano le sanzioni per dichiarazione omessa o infedele.</p></div>
<p class="small muted">Questa guida è informativa e non è una consulenza fiscale. Si basa su norme e pagine ufficiali (Normattiva, MEF, Agenzia delle Entrate, Comune di Milano, Roma Capitale) consultate il 16 ottobre 2026. Tariffe, esenzioni e scadenze dei versamenti dipendono dal tuo comune: verifica il regolamento comunale.</p>
<h2>Chi può applicarla e quanto</h2>
<ul><li><strong>Chi:</strong> comuni capoluogo di provincia, unioni di comuni e comuni inseriti negli elenchi regionali delle località turistiche o città d'arte (D.Lgs. 23/2011, art. 4).</li>
<li><strong>Quanto:</strong> fino a 5&nbsp;€ per notte, graduata in base al prezzo; i capoluoghi con presenze turistiche venti volte superiori ai residenti possono arrivare a 10&nbsp;€. Roma applica un contributo di soggiorno fino a 10&nbsp;€.</li>
<li><strong>Aumento 2026:</strong> la maggiorazione fino a 2&nbsp;€ per notte introdotta per il Giubileo è stata prorogata al 2026 dalla legge di bilancio; ogni comune decide se applicarla.</li>
<li><strong>Esenzioni e riduzioni:</strong> le stabilisce ogni comune nel proprio regolamento.</li></ul>
<h2>Un esempio: le tariffe di Milano nel 2026</h2>
{milano}
<p>A Milano il 5 stelle arriva a 12&nbsp;€ sommando il massimo di 10&nbsp;€ e la maggiorazione di 2&nbsp;€. A Roma, ad esempio, sono esenti i minori fino al compimento dei 10 anni e l'imposta si applica al massimo per 10 notti nell'anno solare.</p>
<h2>Il gestore è responsabile del pagamento</h2>
<p>Dal 2020 il gestore della struttura ricettiva è <em>responsabile del pagamento</em> dell'imposta, con diritto di rivalsa sull'ospite. In pratica: la incassi, la versi al comune e ne rispondi tu se non viene versata. Le modalità e le scadenze dei versamenti periodici le fissa il comune: a Roma, per esempio, comunicazione e versamento sono trimestrali, entro il 16 del mese successivo al trimestre.</p>
<h2>La dichiarazione annuale entro il 30 giugno</h2>
<ol><li><strong>Quando:</strong> entro il 30 giugno dell'anno successivo (per il 2026, entro il 30 giugno 2027).</li>
<li><strong>Come:</strong> solo per via telematica, con il modello approvato dal DM 29 aprile 2022, tramite i servizi dell'Agenzia delle Entrate (Fisconline/Entratel) o un intermediario abilitato.</li>
<li><strong>Cosa contiene:</strong> una dichiarazione per comune, con i dati per trimestre di ogni struttura: tariffa applicata, presenze ordinarie, esenti e ridotte, e l'importo versato al comune.</li></ol>
<h2>Sanzioni: cosa cambia dal 2027</h2>
{sanz}
<p>Le nuove sanzioni del D.Lgs. 147/2026 si applicano alle violazioni commesse dal 1° gennaio 2027. Il regolamento comunale può prevedere ulteriori sanzioni (Roma, ad esempio, per il versamento omesso o tardivo).</p>
<h2>Affitti brevi e portali</h2>
<p>Per le locazioni brevi, chi incassa il canone o interviene nel pagamento, compresi i portali online, è responsabile del pagamento dell'imposta e degli altri obblighi, con le stesse regole del gestore (DL 50/2017, art. 4). Se un portale la incassa per te dipende dagli accordi con il singolo comune: verifica sempre.</p>
<h2>Da non confondere</h2>
<ul><li><strong><a href="{U("post-alloggiati")}">Alloggiati Web</a>:</strong> la comunicazione degli ospiti alla Questura è un obbligo diverso.</li>
<li><strong>ISTAT:</strong> le statistiche turistiche vanno ai sistemi regionali, separatamente.</li></ul>
<h2>Cosa fa Hostlio Pro (e cosa no)</h2>
<p>Per essere chiari: Hostlio Pro non calcola l'imposta di soggiorno, non la versa e non presenta la dichiarazione. Ti aiuta a tenere in ordine prenotazioni, notti e ospiti in un unico pannello e a esportare i report in Excel per il tuo commercialista. Se vuoi un gestionale che gestisca anche l'imposta, chiedilo espressamente ai fornitori: lo trovi nel confronto dei <a href="{U("post-gestionali")}">gestionali per hotel più usati</a>.</p>
<div class="cta-row" style="margin-top:12px">{cta}</div>
'''
    lis = "".join(f'<li><a href="{u}" rel="nofollow noopener">{html.escape(n)}</a></li>' for n, u in SRC)
    c += f'<h2>Fonti</h2><p class="small muted">Tutte le fonti sono state consultate il 16 ottobre 2026.</p><ul>{lis}</ul>'
    faq = [("Quanto può essere al massimo l'imposta di soggiorno?", "Fino a 5 € per persona e per notte; fino a 10 € nei capoluoghi più turistici e a Roma. Nel 2026 i comuni possono aggiungere fino a 2 € di maggiorazione, prorogata dalla legge di bilancio."),
           ("Chi deve versare l'imposta di soggiorno?", "La paga l'ospite, ma il gestore della struttura è responsabile del pagamento: la incassa e la versa al comune, con diritto di rivalsa sull'ospite."),
           ("Entro quando si presenta la dichiarazione?", "Entro il 30 giugno dell'anno successivo, solo per via telematica con il modello del DM 29 aprile 2022."),
           ("Quali sanzioni ci sono?", "Fino al 31 dicembre 2026, dal 100% al 200% dell'importo per dichiarazione omessa o infedele. Dal 1° gennaio 2027: 100% (minimo 50 €) per omessa e 40% (minimo 50 €) per infedele dichiarazione."),
           ("Hostlio Pro calcola l'imposta di soggiorno?", "No. Hostlio Pro non calcola, non versa e non dichiara l'imposta; puoi esportare i report delle prenotazioni in Excel per il tuo commercialista.")]
    return c, faq

FN = {"it": it}
