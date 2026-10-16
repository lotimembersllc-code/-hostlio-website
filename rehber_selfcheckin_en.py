"""Takvim yazısı: "Aparthotel self check-in without a 24/7 front desk (2026)" — yalnız EN.
Resmî kaynaklar 16 Ekim 2026: IT Consiglio di Stato 9101/2025; ES Interior FAQ 10.08.2026 (md. 18–19); FR CESEDA R814-1/3;
PT SIBA (Lei 23/2007 art. 15–16; 3 iş günü doğrulanamadı → yazılmaz); UK SI 1972/1689 art. 4–5; DE BMG §29 (BEG IV, 1.1.2025).
Hostlio: online check-in Pro/Growth, MRZ cihazda; akıllı kilit entegrasyonu YOK, polis kaydı göndermez."""
import html

SRC = [
 ("Consiglio di Stato, Sez. III, judgment 9101/2025 (Italy)", "https://mdp.giustizia-amministrativa.it/visualizza/?nodeRef=&schema=cds&nrg=202505732&nomeFile=202509101_11.html&subDir=Provvedimenti"),
 ("Spain, Ministry of the Interior: SES.Hospedajes FAQ (updated 10/08/2026)", "https://sede.interior.gob.es/portal/dam/jcr:995aad35-2632-4de2-97fe-94cc2489c9c6/Preguntas-frecuentes-hospedajes-alquiler-vehiculos-20260810.pdf"),
 ("Spain: Real Decreto 933/2021", "https://www.boe.es/eli/es/rd/2021/10/26/933/con"),
 ("France: CESEDA, articles R814-1 to R814-3", "https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006070158/LEGISCTA000042804992/"),
 ("Portugal: SIBA privacy notice (Lei 23/2007, art. 15–16)", "https://siba.ssi.gov.pt/files/RGPD_SIBA.pdf"),
 ("UK: Immigration (Hotel Records) Order 1972, article 4", "https://www.legislation.gov.uk/uksi/1972/1689/article/4/made"),
 ("UK: Immigration (Hotel Records) Order 1972, article 5", "https://www.legislation.gov.uk/uksi/1972/1689/article/5/made"),
 ("Germany: Bundesmeldegesetz §29", "https://www.gesetze-im-internet.de/bmg/__29.html"),
]

def _tbl(head, rows):
    h = "".join(f'<th scope="col">{x}</th>' for x in head)
    b = "".join("<tr>" + f'<th scope="row">{r[0]}</th>' + "".join(f"<td>{c}</td>" for c in r[1:]) + "</tr>" for r in rows)
    return f'<div class="table-wrap"><table class="cmp"><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table></div>'

META = {"en": dict(key="post-selfcheckin", date="2026-10-16", title="Aparthotel self check-in without a 24/7 front desk (2026)",
                   desc="Running an aparthotel without a 24/7 front desk: online check-in, access, guest messaging and the guest ID rules in Italy, Spain, France, Portugal, UK, Germany.")}

def en(U):
    from build import btn, SIGNUP_URL
    cta = btn("Try free for ⟦trial⟧ days", SIGNUP_URL) + btn("See online check-in", U("checkin"), "ghost")
    rules = _tbl(["Country", "What the rules say about checking in foreign guests", "Remote check-in?"], [
        ("Italy", "Operators must verify in person (<em>de visu</em>) that the guest matches the ID; the Consiglio di Stato restored this rule in November 2025. It said a video link at the entrance that checks the guest in real time could work.", "Collect data online, but check identity live"),
        ("Spain", "The Interior Ministry's FAQ allows collecting and verifying guest data with systems that work without the guest being physically present, if the data can be verified and data-protection rules are met. Data still goes to SES.Hospedajes within 24 hours.", "Yes, explicitly allowed"),
        ("France", "Foreign guests (EU citizens included) must fill in and sign a <em>fiche individuelle de police</em> on arrival; it is kept 6 months and shown to police on request.", "Signature on arrival"),
        ("Portugal", "Foreign guests, EU citizens included, must complete and sign a <em>boletim de alojamento</em> in person; the operator sends it via SIBA.", "Personal signature"),
        ("United Kingdom", "Guests aged 16+ give their name and nationality; non-British guests also give passport number and place of issue. The record is kept for 12 months for inspection.", "Record only; no in-person rule in the Order"),
        ("Germany", "Since 1 January 2025 only foreign guests fill in a registration form; they sign it by hand on arrival and show a passport. An electronic form is allowed if confirmed on arrival (card payment with strong authentication, eID or reading the eID/residence permit).", "Electronic, confirmed on arrival")])
    c = f'''<div class="answer"><p><strong>Short answer:</strong> an aparthotel can run without a 24/7 front desk if four things work: guests complete online check-in before arrival, they get clear arrival instructions and access, their questions are answered at any hour, and someone can step in when something goes wrong. What you cannot automate away is the local law on identifying foreign guests: Spain explicitly allows remote checks, but Italy requires a live identity check, and France, Portugal and Germany require the guest's own signature or confirmation on arrival.</p></div>
<p class="small muted">This guide is general information, not legal advice. Legal points come from official sources checked on 16 October 2026; rules change and local authorities may interpret them differently. Check with your local police or a lawyer for your property.</p>
<h2>What "self check-in" really involves</h2>
<ol><li><strong>Before arrival:</strong> the guest fills in their details, scans their ID and signs the house rules online.</li>
<li><strong>Arrival instructions:</strong> address, parking, entrance, apartment number and how to get in, sent at the right time in the guest's language.</li>
<li><strong>Access:</strong> a key box, a door code or a smart lock, or a staffed check-in point for part of the day.</li>
<li><strong>Identity check where the law requires it:</strong> live, by video at the entrance, or on arrival.</li>
<li><strong>Support at any hour:</strong> answers to "where is the key", "how does the heating work", "can we check out later".</li>
<li><strong>A fallback:</strong> a phone number someone answers for real problems.</li></ol>
<h2>The ID rules, country by country</h2>
{rules}
<p>The common thread is a Schengen-wide rule that foreign guests personally complete and sign registration forms. Online check-in helps you collect the data early and accurately, but in most countries it does not replace the identity check or signature on arrival.</p>
<h2>Designing the arrival without a front desk</h2>
<ul><li><strong>Send instructions in two steps:</strong> practical details a few days before, access details on the day.</li>
<li><strong>Write instructions for a tired traveller at night:</strong> short sentences, photos of the entrance, the exact apartment number.</li>
<li><strong>Plan the identity check:</strong> a short staffed window, a video call at the entrance, or a member of staff meeting late arrivals, depending on the country.</li>
<li><strong>Keep messages in one place:</strong> WhatsApp and OTA messages in one inbox, so nothing is missed at night. See <a href="{U("post-ai")}">answering guest messages with AI</a>.</li>
<li><strong>Prepare for the common questions:</strong> Wi-Fi, heating and air conditioning, rubbish, parking, late checkout.</li></ul>
<h2>What to automate, and what to keep human</h2>
<p>Automate the predictable: pre-arrival forms, arrival instructions, answers to factual questions, checkout reminders. Keep people for exceptions: lost keys, noise complaints, refunds, guests who cannot get in, and the identity check where your country requires one.</p>
<h2>How Hostlio Pro helps (and what it doesn't do)</h2>
<p>With Hostlio Pro's <a href="{U("checkin")}">online check-in</a> (Pro and Growth plans), guests enter their details and sign before arrival, and can scan the machine-readable zone of their passport or ID card with their own phone: it is read on the device and no image is stored. The check-in link can be sent automatically by email. Lio, the AI assistant, answers guests on WhatsApp in their language at any hour using your property's information, and hands anything unusual to your team; on Pro and Growth it also covers the Booking.com, Airbnb and Expedia inboxes. To be clear: Hostlio Pro does not integrate with smart locks or key boxes and does not submit guest registrations to the police; those stay with your access system and your local procedure. For aparthotel-specific features, see <a href="{U("t-apart")}">aparthotel software</a>.</p>
<div class="cta-row" style="margin-top:12px">{cta}</div>
'''
    lis = "".join(f'<li><a href="{u}" rel="nofollow noopener">{html.escape(n)}</a></li>' for n, u in SRC)
    c += f'<h2>Sources</h2><p class="small muted">All sources accessed 16 October 2026.</p><ul>{lis}</ul>'
    faq = [("Is self check-in legal for aparthotels?", "Collecting guest data online is fine everywhere covered here, but identity rules differ: Spain explicitly allows remote verification, Italy requires a live in-person check (a real-time video check at the entrance may work), and France, Portugal and Germany require the foreign guest's signature or confirmation on arrival."),
           ("Do I need a 24/7 front desk?", "No, but you need a reliable way to answer guests at any hour and someone who can step in for real problems, plus a plan for the identity check where the law requires it."),
           ("Can guests scan their passport before arrival?", "Yes, with an online check-in that reads the machine-readable zone. In Hostlio Pro this happens on the guest's phone and no image is stored. It collects the data; it does not replace an in-person check where one is required."),
           ("Does Hostlio Pro work with smart locks?", "No. Hostlio Pro handles online check-in, guest messaging and operations; access codes and locks stay with your access system.")]
    return c, faq

FN = {"en": en}
