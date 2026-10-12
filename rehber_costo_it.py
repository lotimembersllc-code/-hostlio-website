"""Takvim yazısı (22 Ekim 2026 planı, öne alındı): "Quanto costa un gestionale per hotel nel 2026" — yalnız IT.
Veriler 12 Ekim 2026 resmî siteler/hesaplayıcılar (post-gestionali ve post-cmit araştırmaları): TeamSystem Hospitality listino,
RoomRaccoon hesaplayıcı, SiteMinder ve Little Hotelier İtalya fiyat akışı (resmî SiteMinder feed), Beds24 hesaplayıcı, Octorate.
post-gestionali'den ayrım: bu yazı yalnız MALİYET (modeller, gizli kalemler, yıllık toplam)."""
import html

SRC = [
 ("TeamSystem Hospitality: prezzi", "https://www.teamsystem.com/horeca/ts-hospitality/prezzi/prezzi-hotel-bb-agriturismo/"),
 ("RoomRaccoon: prezzi", "https://roomraccoon.it/prezzi/"),
 ("SiteMinder: prezzi", "https://www.siteminder.com/it/prezzi/"),
 ("SiteMinder: listino ufficiale (feed prezzi, Italia)", "https://resources.siteminder.com/services/pricing/2022/data/products/index.php"),
 ("Beds24: pricing", "https://beds24.com/pricing.html"),
 ("Octorate: prezzi", "https://www.octorate.com/it/prezzi/"),
 ("Smoobu: prezzi", "https://www.smoobu.com/it/prezzi/"),
 ("Zak by WuBook: prezzi", "https://wubook.net/page/prezzi-22.html"),
 ("Slope: prezzi", "https://www.slope.it/prezzi/"),
 ("Bedzzle: prezzi", "https://www.bedzzle.com/it/prezzi"),
]

def _tbl(head, rows, hl=True):
    h = "".join(f'<th scope="col">{x}</th>' for x in head)
    b = "".join(("<tr class=\"hl\">" if hl and r[0] == "Hostlio Pro" else "<tr>") + f'<th scope="row">{r[0]}</th>'
                + "".join(f"<td>{c}</td>" for c in r[1:]) + "</tr>" for r in rows)
    return f'<div class="table-wrap"><table class="cmp"><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table></div>'

META = {"it": dict(key="post-costit", date="2026-10-13", title="Quanto costa un gestionale per hotel nel 2026: prezzi reali",
                   desc="Prezzi 2026 dei gestionali per hotel e B&B: modelli di costo, costo annuo per 10 e 25 camere, IVA, moduli e costi nascosti. Fonti ufficiali.")}

def it(U):
    from build import btn, SIGNUP_URL
    cta = btn("Prova gratis per ⟦trial⟧ giorni", SIGNUP_URL) + btn("Vedi i piani", U("pricing"), "ghost")
    models = _tbl(["Modello", "Come funziona", "Esempi", "Attenzione a"], [
        ("Canone fisso", "Stesso importo ogni mese o anno", "Hostlio Pro, TeamSystem Hospitality (per fascia di camere)", "Cosa è incluso e cosa è un modulo extra"),
        ("Per camera", "Il canone cresce con le camere", "Octorate Basic (da 8&nbsp;€ a camera), Beds24", "Il costo se aggiungi camere o canali"),
        ("Commissione a prenotazione", "Una percentuale su ogni prenotazione", "Smoobu Flex (+0,9%)", "Pesa proprio nei mesi migliori"),
        ("Su preventivo", "Prezzo dopo una demo", "Zak, Slope, Bedzzle, gruppo Zucchetti", "Chiedi il costo annuo completo per iscritto")], hl=False)
    y10 = _tbl(["Gestionale", "10 camere / anno", "Cosa include"], [
        ("Hostlio Pro (Starter)", "⟦annual:starter⟧ (pagamento annuale)", "PMS, channel manager, app, assistente AI"),
        ("Beds24", "circa 506&nbsp;€", "PMS e channel manager a consumo (3 tipologie, 2 OTA)"),
        ("TeamSystem Hospitality", "864&nbsp;€ + IVA", "PMS, channel manager, booking engine, fatturazione elettronica"),
        ("SiteMinder", "1.080&nbsp;€ (annuale) – 1.140&nbsp;€ (mensile)", "Solo channel manager"),
        ("Little Hotelier Pro", "1.548&nbsp;€", "PMS con channel manager"),
        ("RoomRaccoon Entry", "1.968&nbsp;€", "Suite; solo 3 canali")])
    y25 = _tbl(["Gestionale", "25 camere / anno", "Cosa include"], [
        ("Hostlio Pro (Pro)", "⟦annual:pro⟧ (pagamento annuale)", "Come sopra, più caselle OTA e check-in online"),
        ("Beds24", "circa 1.014&nbsp;€", "4 tipologie, 3 OTA"),
        ("SiteMinder", "1.584&nbsp;€ (annuale) – 1.668&nbsp;€ (mensile)", "Solo channel manager"),
        ("TeamSystem Hospitality", "2.014&nbsp;€ + IVA", "Come sopra"),
        ("Little Hotelier Pro", "2.628&nbsp;€", "Fascia fino a 30 camere"),
        ("RoomRaccoon Entry", "2.736&nbsp;€", "Solo 3 canali")])
    c = f'''<div class="answer"><p><strong>In breve:</strong> nel 2026 un gestionale per un piccolo hotel o un B&amp;B in Italia costa, tra i fornitori che pubblicano i prezzi, da circa 500 a 2.000 l'anno per 10 camere e da circa 850 a 2.700 per 25 camere, in euro o dollari a seconda del fornitore. Molti gestionali italiani lavorano solo su preventivo. Per confrontare davvero, somma canone, IVA, attivazione, moduli (channel manager, booking engine, fatturazione) e commissioni: la differenza sta lì, non nel prezzo di partenza.</p></div>
<p class="small muted">Hostlio Pro è uno dei prodotti confrontati, quindi non siamo neutrali. Le cifre provengono dai listini e dai calcolatori ufficiali dei fornitori, consultati il 12 ottobre 2026; IVA indicata solo dove il fornitore la specifica. Prezzi e piani cambiano: verifica sempre sul sito del fornitore.</p>
<h2>Quanto costa Hostlio Pro</h2>
<p>Hostlio Pro ha tre piani a canone fisso: Starter ⟦price:starter⟧ al mese (fino a ⟦rooms:starter⟧ camere), Pro ⟦price:pro⟧ (fino a ⟦rooms:pro⟧) e Growth ⟦price:growth⟧ (fino a ⟦rooms:growth⟧ camere e 2 strutture), in dollari USA. Con il pagamento annuale lo sconto è del 20%: Starter ⟦annual:starter⟧, Pro ⟦annual:pro⟧ l'anno. Nessuna commissione sulle prenotazioni; channel manager, app e l'assistente AI Lio sono inclusi in tutti i piani. Prova gratuita di ⟦trial⟧ giorni.</p>
<div class="cta-row" style="margin-top:12px">{cta}</div>
<h2>I modelli di prezzo</h2>
{models}
<h2>Costo annuo per 10 camere</h2>
<p>Costo di un anno calcolato da listini e calcolatori ufficiali. I prodotti non includono le stesse funzioni: guarda anche la colonna "cosa include".</p>
{y10}
<h2>Costo annuo per 25 camere</h2>
{y25}
<p class="small muted">SiteMinder e Little Hotelier: listino ufficiale per l'Italia caricato dalla pagina prezzi di SiteMinder; per 25 camere vale la fascia 21–30. Beds24: calcolatore ufficiale. RoomRaccoon: calcolatore ufficiale, IVA non indicata. TeamSystem Hospitality: listino annuale + IVA. Fornitori su preventivo esclusi.</p>
<h2>I costi che non vedi nel canone</h2>
<ul><li><strong>IVA:</strong> alcuni listini sono IVA esclusa, altri non lo dicono. Confronta sempre importi omogenei.</li>
<li><strong>Attivazione e formazione:</strong> alcuni fornitori le fanno pagare a parte, una tantum.</li>
<li><strong>Channel manager:</strong> in alcuni prodotti è incluso, in altri è un modulo o un prodotto separato (SiteMinder, ad esempio, è solo channel manager).</li>
<li><strong>Canali limitati:</strong> i piani d'ingresso possono limitare a 3 o 5 canali.</li>
<li><strong>Adempimenti italiani:</strong> invio ad <a href="{U("post-alloggiati")}">Alloggiati Web</a>, ISTAT, imposta di soggiorno, fatturazione elettronica SDI e registratore telematico. Chiedi se sono inclusi, a pagamento o non disponibili.</li>
<li><strong>Commissioni:</strong> una percentuale per prenotazione sembra piccola, ma cresce con l'alta stagione.</li>
<li><strong>Commissioni OTA:</strong> non dipendono dal gestionale, ma spesso sono la voce più grande. Calcola il netto per canale con il <a href="{U("commission")}">calcolatore di commissioni OTA</a>.</li></ul>
<h2>Come risparmiare senza sbagliare</h2>
<ol><li><strong>Scegli in base alle camere che hai</strong> e a quelle che avrai: un prezzo per camera sale in fretta.</li>
<li><strong>Preferisci un canone fisso</strong> se la tua stagione è forte: le commissioni pesano proprio nei mesi migliori.</li>
<li><strong>Valuta il pagamento annuale</strong> solo dopo la prova: lo sconto conviene se sei sicuro della scelta.</li>
<li><strong>Chiedi il costo annuo completo per iscritto</strong> ai fornitori su preventivo, moduli inclusi.</li>
<li><strong>Prova con dati reali:</strong> le tue camere, i tuoi prezzi e almeno un portale collegato.</li></ol>
<h2>Cosa non fa Hostlio Pro</h2>
<p>Per un confronto onesto: Hostlio Pro non invia i dati ad Alloggiati Web (li raccoglie con il <a href="{U("checkin")}">check-in online</a>), non gestisce fatturazione elettronica SDI né registratore telematico e non ha POS o contabilità. Se questi invii automatici sono indispensabili per te, considera un gestionale italiano o abbina Hostlio Pro al tuo software fiscale. Per il confronto completo dei prodotti leggi <a href="{U("post-gestionali")}">i gestionali per hotel più usati nel 2026</a>; per i criteri di scelta, <a href="{U("post-pms")}">come scegliere un gestionale per piccoli hotel</a>.</p>
'''
    lis = "".join(f'<li><a href="{u}" rel="nofollow noopener">{html.escape(n)}</a></li>' for n, u in SRC)
    c += f'<h2>Fonti</h2><p class="small muted">Tutte le fonti sono state consultate il 12 ottobre 2026.</p><ul>{lis}</ul>'
    faq = [("Quanto costa un gestionale per hotel all'anno?", "Tra i fornitori che pubblicano i prezzi, da circa 500 a 2.000 l'anno per 10 camere e da circa 850 a 2.700 per 25 camere, in euro o dollari (12 ottobre 2026), a seconda di cosa è incluso. Molti gestionali italiani lavorano su preventivo."),
           ("Il channel manager è compreso nel prezzo?", "Dipende: in Hostlio Pro, TeamSystem Hospitality, RoomRaccoon e Little Hotelier è incluso; SiteMinder è solo channel manager; in Beds24 si paga per collegamento; il piano Basic di Octorate comprende channel manager e booking engine ma non il PMS."),
           ("Meglio canone fisso o commissione?", "Se la tua stagione è forte, il canone fisso è più prevedibile: la commissione cresce proprio nei mesi migliori. Con pochissime prenotazioni l'anno, una commissione può costare meno."),
           ("Quanto costa Hostlio Pro?", "Starter ⟦price:starter⟧, Pro ⟦price:pro⟧ e Growth ⟦price:growth⟧ al mese (USD); con il pagamento annuale il 20% in meno. Prova gratuita di ⟦trial⟧ giorni.")]
    return c, faq

FN = {"it": it}
