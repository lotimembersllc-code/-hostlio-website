from build import store_badges, btn, icon, logo, url, room_rack, channel_strip, faq_block, SIGNUP_URL, EMAIL, UPDATED, CHECK, software_schema, SITE, PLANS
import ozellik_ekleri as FX
import derin_sayfalar as DS
L = "en"
def U(k): return url(k, L)

PLAN_TXT = {
 "starter": ("For small guesthouses and boutique hotels", ["1 property, up to 10 rooms, 3 users","⟦quota:starter⟧ AI messages / month","Channel sync with 100+ OTAs","WhatsApp AI messaging","Lio Suggestions every morning","Room rack reservation calendar","Accommodation confirmation for visas (PDF)","iOS and Android app"]),
 "pro":     ("For growing single-property hotels", ["1 property, up to 50 rooms, 8 users","⟦quota:pro⟧ AI messages / month","Everything in Starter","WhatsApp + OTA inbox messaging (Booking.com, Airbnb, Expedia)","Lio takes booking requests on WhatsApp (you approve)","AI insights from reviews and messages","Online check-in with digital signature","Transfer, tour and extras sales"]),
 "growth":  ("For teams running two properties", ["Up to 2 properties, 150 rooms in total, 20 users","⟦quota:growth⟧ AI messages / month","Everything in Pro","Weekly AI summary","Priority channel sync","Priority support (next business day)","Custom onboarding call","White-label: your logo, colours and assistant name"]),
}

def plans_html():
    out = []
    for p in PLANS:
        for_, feats = PLAN_TXT[p["id"]]
        pop = p["id"] == "pro"
        lis = "".join(f"<li>{CHECK}<span>{f}</span></li>" for f in feats)
        out.append(f'''<article class="plan{" pop" if pop else ""}" aria-labelledby="plan-{p["id"]}">
{'<span class="tag">Most popular</span>' if pop else ""}
<h3 id="plan-{p["id"]}">{p["name"]}</h3><p class="for">{for_}</p>
<div class="price num"><b data-price="{p["id"]}">⟦price:{p["id"]}⟧</b><span class="muted">/ month</span></div>
<p class="small muted num" style="margin:0" data-eb>Early-bird price (regularly <s data-regular="{p["id"]}">⟦regular:{p["id"]}⟧</s>)</p>
<ul>{lis}</ul>
{btn("Start with "+p["name"], SIGNUP_URL+"?plan="+p["id"], "primary" if pop else "ghost")}
</article>''')
    return '<div class="plans">' + "".join(out) + "</div>"

FAQ_CORE = [
 ("What is Hostlio Pro?", "Hostlio Pro is AI-powered hotel management software (PMS) built for independent hotels, boutique hotels and guesthouses. It combines Lio, an AI assistant that answers guest messages 24/7 in 30+ languages, a channel manager connected to 100+ OTAs, a drag-and-drop reservation calendar and online check-in in one platform."),
 ("How much does Hostlio Pro cost?", "There are three plans: Starter at ⟦price:starter⟧/month, Pro at ⟦price:pro⟧/month and Growth at ⟦price:growth⟧/month. These prices include a ⟦eb_pct⟧ early-bird discount for the first 50 customers, locked in for as long as you stay subscribed. Regular prices are ⟦regular:starter⟧, ⟦regular:pro⟧ and ⟦regular:growth⟧."),
 ("Is there a free trial?", "Yes. Every plan comes with a 7-day free trial. You enter a payment card at signup, but nothing is charged until the trial ends. There are no long-term contracts and you can cancel anytime."),
 ("Which OTAs does Hostlio Pro connect to?", "Through Channex, Hostlio Pro connects to 100+ channels including Booking.com, Airbnb, Expedia, Agoda, Trip.com, Hotels.com, Hotelbeds, Hostelworld and Google Hotels. Availability, rates and reservations stay in sync across all of them."),
 ("Which languages does Lio reply in?", "Lio replies in 30+ languages, including English, Turkish, Arabic, Russian, German, Japanese and Chinese. It answers in the guest's language, and you see a translation in your dashboard."),
]

def home():
    import home_v3
    return home_v3.home(L, plans_html, FAQ_CORE)

def ai():
    body = f'''
<section class="page-hero"><div class="wrap split">
<div><h1>Lio, the AI guest messaging assistant</h1>
<p class="lead">Lio is an AI assistant trained on your hotel's information. It answers guest messages on WhatsApp and in OTA inboxes (Booking.com, Airbnb, Expedia) in 30+ languages, at any hour.</p>
<div class="cta-row">{btn("Try Lio free for 7 days", SIGNUP_URL)}</div></div>
<div class="panel typing"><p class="panel-title">WhatsApp, 02:47</p>
<div class="msg in" style="background:var(--bg)" lang="de">Hallo! Unser Flug landet um 1 Uhr. Können Sie uns abholen, und ist ein später Check-in möglich?</div>
<div class="msg out" lang="de">Natürlich! Unser Flughafentransfer kostet 35 € für bis zu 3 Gäste. Soll ich ihn für Ihre Ankunft um 1 Uhr buchen? Später Check-in ist kein Problem.<small lang="en">Lio, German</small></div>
<p class="small muted" style="margin:10px 0 0">Transfer request created and passed to your team.</p></div>
</div></section>

<section class="white rule"><div class="wrap">
<div class="answer"><p><strong>What is an AI guest messaging assistant for hotels?</strong> Software that automatically answers the questions guests ask before and after booking, using the hotel's own information. Lio hands over messages it can't answer, or that need a human decision (discount requests, complaints, special requests), to your staff.</p></div>
<h2 style="margin-top:64px">What Lio does</h2><div class="rows">
<div class="row"><h3>One inbox</h3><div><p>WhatsApp and OTA inbox messages (Booking.com, Airbnb, Expedia) land on one screen. Lio automatically matches each guest to their reservation.</p></div></div>
<div class="row"><h3>30+ languages, auto-translated</h3><div><p>The guest writes in Japanese and Lio replies in Japanese; you see a translation of Lio's reply in your own language. Replies you type yourself are sent exactly as written, without automatic translation.</p></div></div>
<div class="row"><h3>Knows your hotel</h3><div><p>Check-in and check-out times, parking, pet policy, breakfast hours, transport and room features. Enter them once and Lio uses them consistently in every reply. If Lio can't answer a question, it flags the missing information in your setup; fill it in once and the alert clears itself.</p></div></div>
<div class="row"><h3>An assistant that sells</h3><div><p>Lio doesn't just answer questions: it offers airport transfers, city tours and extras at the right moment, then creates the request and passes it to your team.</p></div></div>
<div class="row"><h3>Takes booking requests</h3><div><p>On the Pro and Growth plans, when a guest asks about a room on WhatsApp, Lio collects the dates, number of guests and room preference and quotes a price from your own rates and availability. The request comes to you, and it becomes a reservation once you approve it.</p></div></div>
<div class="row"><h3>Suggestions every morning</h3><div><p>Every morning, Lio Suggestions flag pricing, operations (rooms waiting to be cleaned, pending requests), setup gaps and revenue opportunities. Nothing changes without your approval, and rate suggestions stay within the limits you set. Included in every plan.</p></div></div>
<div class="row"><h3>Insights from reviews and messages</h3><div><p>On Pro and Growth, Lio summarises recurring complaint and praise themes from guest reviews and messages. A weekly AI summary is included with Growth and optional on Pro.</p></div></div>
<div class="row"><h3>You stay in control</h3><div><p>During the first days you can approve Lio's replies before they're sent. You decide which topics Lio closes on its own and which it hands to you.</p></div></div>
</div></div></section>

<section><div class="wrap">
<div class="section-head"><figure class="app-shot"><a href="/assets/img/panel-msg-en.webp"><img src="/assets/img/panel-msg-en.webp" alt="Hostlio Pro inbox: Lio answers a Booking.com guest's airport transfer question" loading="lazy" width="1600" height="998"></a><figcaption>A real screen from the Hostlio Pro dashboard (demo hotel data)</figcaption></figure>
<h2>AI message quota by plan</h2><p>One message is a single reply Lio sends to a guest.</p></div>
<div class="table-wrap"><table><thead><tr><th>Plan</th><th class="c">AI messages / month</th><th>Messaging channels</th></tr></thead><tbody>
<tr><th>Starter</th><td class="c num">⟦quota:starter⟧</td><td>WhatsApp</td></tr>
<tr><th>Pro</th><td class="c num">⟦quota:pro⟧</td><td>WhatsApp + OTA inboxes (Booking.com, Airbnb, Expedia)</td></tr>
<tr><th>Growth</th><td class="c num">⟦quota:growth⟧</td><td>WhatsApp + OTA inboxes (Booking.com, Airbnb, Expedia)</td></tr>
</tbody></table></div>
</div></section>
'''
    faq = [
     ("What if Lio gives wrong information?", "Lio only uses the hotel information and reservation data you provide. When it isn't sure, it hands the message to you instead of guessing. You can also approve every reply before it's sent."),
     ("Does it answer Booking.com and Airbnb messages too?", "Yes. On the Pro and Growth plans, OTA messages arrive in Lio's inbox and are answered the same way."),
     ("Can Lio take bookings?", "Yes, on the Pro and Growth plans, with your approval. When a guest writes on WhatsApp, Lio asks for the dates, number of guests and room preference, quotes a price from your rates and availability, and passes the request to you. It only becomes a reservation once you approve it; Lio never confirms a booking on its own. Extra-service requests such as transfers and tours work the same way."),
     ("What happens when the message quota runs out?", "You won’t be surprised: the usage counter in the dashboard turns amber at 80%, and at 100% the account owner gets an email and a push notification. Lio keeps replying a little past the limit; automatic replies pause at about 110%. Messages keep arriving and appear in your dashboard, and your team can still answer them by hand. Upgrade to a higher plan to increase your quota."),
     FAQ_CORE[4],
    ]
    return {"key":"ai","title":"AI Guest Messaging for Hotels in 30+ Languages | Hostlio Pro",
            "desc":"Lio, Hostlio Pro's AI assistant, answers hotel guests on WhatsApp and OTA inboxes 24/7 in 30+ languages, takes booking requests and sends daily suggestions.",
            "trail":[("Lio AI assistant", U("ai"))],"body":body,"faq":faq}

def channel():
    body = f'''
<section class="page-hero"><div class="wrap split">
<div><h1>A channel manager for 100+ OTAs</h1>
<p class="lead">Manage availability, rates and bookings on Booking.com, Airbnb, Expedia, Agoda and 100+ other channels from one calendar. Hostlio Pro syncs in real time and both ways.</p>
<div class="cta-row">{btn("Start 7-day free trial", SIGNUP_URL)}</div></div>
<div class="panel"><p class="panel-title">Connected channels</p><div class="chan-list">
<div><span>Booking.com</span><span class="pill">In sync</span></div>
<div><span>Airbnb</span><span class="pill">In sync</span></div>
<div><span>Expedia</span><span class="pill">In sync</span></div>
<div><span>Agoda</span><span class="pill">In sync</span></div>
<div><span>Google Hotels</span><span class="pill">In sync</span></div>
</div></div>
</div></section>
<section class="white rule"><div class="wrap">
<div class="answer"><p><strong>What is a channel manager?</strong> Software that keeps a hotel's availability and rates in sync while it sells rooms on several online channels at once. When a room sells on one channel it closes on all the others immediately, preventing double bookings (overbooking).</p></div>
<figure class="page-photo"><img src="/assets/img/channel-owner-evening.webp" alt="" loading="lazy" width="1080" height="1341"></figure>
<h2 style="margin-top:64px">What the channel manager does</h2><div class="rows">
<div class="row"><h3>Two-way sync</h3><div><p>New bookings, modifications and cancellations drop onto the room rack automatically, and changes you make in the calendar go out to every channel.</p></div></div>
<div class="row"><h3>Rates and restrictions</h3><div><p>Push rates, minimum stays and stop-sells per room type to all channels from one screen.</p></div></div>
<div class="row"><h3>Colour-coded room rack</h3><div><p>See at a glance which channel each booking came from. Reassign rooms with drag and drop.</p></div></div>
<div class="row"><h3>Connected to messaging</h3><div><p>Guest messages for OTA bookings land in Lio's inbox with the guest, room and dates alongside every conversation.</p></div></div>
{FX.channel_rows(L)}
</div></div></section>
<section><div class="wrap"><div class="section-head"><figure class="app-shot"><a href="/assets/img/panel-rack-en.webp"><img src="/assets/img/panel-rack-en.webp" alt="Hostlio Pro room calendar: Booking.com, Airbnb, Expedia and direct bookings on one calendar" loading="lazy" width="1600" height="980"></a><figcaption>A real screen from the Hostlio Pro dashboard (demo hotel data)</figcaption></figure>
<h2>Main supported channels</h2><p>The list follows our certified connection network. Missing a channel? Get in touch.</p></div>
<div class="table-wrap"><table><thead><tr><th>Channel</th><th>Type</th></tr></thead><tbody>
<tr><th>Booking.com</th><td>OTA</td></tr><tr><th>Airbnb</th><td>Short-term rental</td></tr><tr><th>Expedia, Hotels.com</th><td>OTA</td></tr>
<tr><th>Agoda, Trip.com</th><td>OTA (Asia-focused)</td></tr><tr><th>Hotelbeds</th><td>Wholesaler (bedbank)</td></tr><tr><th>Hostelworld</th><td>Hostel marketplace</td></tr><tr><th>Google Hotels</th><td>Metasearch</td></tr>
</tbody></table></div></div></section>
{DS.more(L,"channel")}
'''
    faq = [FAQ_CORE[3],
     ("Is the channel manager included in every plan?", "Yes. Starter, Pro and Growth all include channel sync with 100+ OTAs. Growth adds priority sync."),
     FX.FX[L]["ch_switch"],
    ]
    return {"key":"channel","title":"Hotel Channel Manager for 100+ OTAs | Hostlio Pro",
            "desc":"Hostlio Pro's channel manager syncs rates and availability with 100+ OTAs like Booking.com, Airbnb, Expedia and Agoda in real time to prevent overbooking.",
            "trail":[("Channel manager", U("channel"))],"body":body,"faq":faq+DS.faq(L,"channel")}

def checkin():
    body = f'''
<section class="page-hero"><div class="wrap split">
<div><h1>Online check&#8209;in with digital signature</h1>
<p class="lead">Before arrival, guests scan their ID with their phone, add accompanying guests and sign. No document images are stored. Handing over the key takes minutes.</p>
<div class="cta-row">{btn("Try Pro free for 7 days", SIGNUP_URL+"?plan=pro")}</div></div>
<div class="panel"><p class="panel-title">Online check-in, Room 202</p>
<div class="field"><span>Full name</span><div>Keiko Sato</div></div>
<div class="field"><span>Nationality</span><div>Japan</div></div>
<div class="field"><span>Document</span><div>Passport scanned, no image stored</div></div>
<div class="field"><span>Accompanying guests</span><div>1 guest added</div></div>
<div class="field"><span>Signature</span><div class="sig">Digital signature received</div></div>
</div>
</div></section>
<section class="white rule"><div class="wrap">
<div class="answer"><p><strong>How does online check-in work?</strong> Hostlio Pro sends the booker a personal, time-limited, secure link. From that link the guest scans the machine-readable zone (MRZ) of their passport or ID card with the phone camera. The reading happens in the guest's own browser and the details fill in automatically. The guest then adds any accompanying guests and signs the form digitally. Only the extracted details and the signature are saved to the reservation; no image of the document is uploaded or stored.</p></div>
<h2 style="margin-top:64px">Online check-in features</h2><div class="rows">
<div class="row"><h3>Secure link</h3><div><p>A token-based link unique to each reservation. It only opens that reservation's form.</p></div></div>
{FX.checkin_row(L)}
<div class="row"><h3>Document scan, no images stored</h3><div><p>The machine-readable zone of the passport or ID card is read on the guest's own device. Only the name, document number (the T.C. identity number on Turkish ID cards), nationality, date of birth and expiry date are saved, never a picture of the document. This is in line with KVKK principle decision 2025/2120, under which accommodation businesses in Türkiye must not keep copies of ID documents. Documents without a machine-readable zone are entered by hand.</p></div></div>
<div class="row"><h3>Accompanying guests</h3><div><p>Everyone staying in the room is added in one form, so nobody has to type details at the desk.</p></div></div>
<div class="row"><h3>Digital signature and consent</h3><div><p>Guests accept house rules and data consent by signing on screen. Signatures are deleted automatically 30 days after check-out.</p></div></div>
<div class="row"><h3>Privacy by design</h3><div><p>You can delete a guest's profile from the dashboard; digital signatures are deleted automatically 30 days after check-out, and conversations are anonymised after the period you set. Legal records such as reservations and invoices are kept separately. The consent text is part of the form.</p></div></div>
<div class="row"><h3>Export for official reporting</h3><div><p>Collected guest details can be exported in a format you can use for local guest registration requirements.</p></div></div>
</div></div></section>
<section class="dark on-dark"><div class="wrap"><div class="section-head"><figure class="app-shot"><a href="/assets/img/panel-res-en.webp"><img src="/assets/img/panel-res-en.webp" alt="Hostlio Pro reservation list with the KBS export button" loading="lazy" width="1600" height="1176"></a><figcaption>A real screen from the Hostlio Pro dashboard (demo hotel data)</figcaption></figure>
<h2>Three steps for the guest</h2></div>
<ol class="steps"><li><h3>Open the link</h3><p>Open the personal link received after the booking is confirmed (sent automatically by email if the hotel has turned this on, or shared by the hotel).</p></li>
<li><h3>Scan the document</h3><p>Scan the passport or ID card with the phone: the details fill in automatically and no image is stored. Then list accompanying guests.</p></li>
<li><h3>Sign</h3><p>Accept house rules and sign on screen. At reception, just pick up the key.</p></li></ol>
</div></section>
{DS.more(L,"checkin")}
'''
    faq = [("Which plans include online check-in?", "Online check-in with digital signature is included in the Pro and Growth plans."),
           ("Does the guest need to download an app?", "No. The check-in form opens in the browser; no app download is required."),
           ("What if a guest doesn't complete the link?", "Check them in the usual way. Staff can also scan the guest's document at the desk from the web panel using the computer's or tablet's camera, or with the Hostlio Pro mobile app; it is read on the device and no image is stored."),
           ("Are photos of ID documents stored?", "No. The document's machine-readable zone (MRZ) is read on the guest's phone, or at the front desk on the hotel's device from the web panel, and only the extracted details and the signature are saved. Passports and ID cards with an MRZ can be scanned; other documents are entered by hand.")]
    return {"key":"checkin","title":"Hotel Online Check-in with Digital Signature | Hostlio Pro",
            "desc":"With Hostlio Pro online check-in, guests scan their ID on their phone (no image stored), add companions and sign before arrival. No queue at reception.",
            "trail":[("Online check-in", U("checkin"))],"body":body,"faq":faq+DS.faq(L,"checkin")}

def features():
    body = f'''
<section class="page-hero"><div class="wrap split"><div><h1>Everything in Hostlio Pro</h1>
<p class="lead">The modules an independent hotel needs day to day: guest communication, distribution, reservations, check-in and extra revenue.</p></div><div class="hero-img"><img src="/assets/img/gen-team-desk.webp" alt="" width="1080" height="1350"></div></div></section>
<section class="white rule"><div class="wrap"><h2 class="sr-only">Modules</h2><div class="rows">
<div class="row"><h3>Lio AI assistant</h3><div><p>24/7 guest replies in 30+ languages. WhatsApp and OTA inbox messages (Booking.com, Airbnb, Expedia) in one inbox.</p><a href="{U("ai")}">More about Lio</a></div></div>
<div class="row"><h3>Channel manager</h3><div><p>Availability, rate and booking sync with 100+ OTAs over certified connections.</p><a href="{U("channel")}">Channel manager</a></div></div>
<div class="row"><h3>Room rack</h3><div><p>Drag-and-drop reservation calendar. Drag a booking to move it to another room; see free rooms and conflicts at a glance.</p></div></div>
<div class="row"><h3>Online check-in</h3><div><p>Secure link, accompanying guests, document scan (no images stored) and digital signature.</p><a href="{U("checkin")}">Online check-in</a></div></div>
<div class="row"><h3>Guest documents</h3><div><p>From the reservation, create the accommodation confirmation guests need for a visa or invitation application, or a stay receipt with dates, nightly rate and total. Choose English, Turkish, Spanish, Italian, Portuguese or French (the guest’s language is suggested), then print or save as PDF. A guest registration form can be downloaded as a PDF too.</p></div></div>
<div class="row"><h3>Transfer and tour sales</h3><div><p>Lio suggests airport transfers and tours during the conversation and passes the request to your team.</p></div></div>
<div class="row"><h3>Lio Suggestions and AI insights</h3><div><p>Every morning Lio prepares suggestions on pricing, operations (rooms waiting to be cleaned, pending requests), setup gaps and revenue opportunities. Nothing changes without your approval, and rate suggestions stay within limits you set. On Pro and Growth, recurring complaints and praise in reviews and messages are summarised too.</p></div></div>
<div class="row"><h3>Mobile app</h3><div><p>Manage bookings, messages and check-ins away from the hotel with the iOS and Android app. It also has the Today screen, analytics and reports, the notification centre, maintenance reports with photos, team management and document scanning at the desk; with two properties, switch between them in one tap.</p>{store_badges("en")}</div></div>
</div></div></section>
{FX.features_more(L)}
<section><div class="wrap"><div class="section-head"><h2>Features by plan</h2></div>
<div class="table-wrap"><table><thead><tr><th>Feature</th><th class="c">Starter</th><th class="c">Pro</th><th class="c">Growth</th></tr></thead><tbody>
<tr><th>Properties</th><td class="c">1</td><td class="c">1</td><td class="c">2</td></tr>
<tr><th>Room limit</th><td class="c num">10</td><td class="c num">50</td><td class="c num">150</td></tr>
<tr><th>Users (staff accounts)</th><td class="c num">3</td><td class="c num">8</td><td class="c num">20</td></tr>
<tr><th>AI messages / month</th><td class="c num">⟦quota:starter⟧</td><td class="c num">⟦quota:pro⟧</td><td class="c num">⟦quota:growth⟧</td></tr>
<tr><th>Channel sync with 100+ OTAs</th><td class="c">Yes</td><td class="c">Yes</td><td class="c">Priority</td></tr>
<tr><th>WhatsApp AI messaging</th><td class="c">Yes</td><td class="c">Yes</td><td class="c">Yes</td></tr>
<tr><th>Lio Suggestions every morning (nothing changes without your approval)</th><td class="c">Yes</td><td class="c">Yes</td><td class="c">Yes</td></tr>
<tr><th>Booking and extra-service requests via Lio on WhatsApp</th><td class="c">No</td><td class="c">Yes</td><td class="c">Yes</td></tr>
<tr><th>AI insights from reviews and guest messages</th><td class="c">No</td><td class="c">Yes</td><td class="c">Yes</td></tr>
<tr><th>Weekly AI summary</th><td class="c">No</td><td class="c">Optional</td><td class="c">Yes</td></tr>
<tr><th>OTA inbox messaging (Booking.com, Airbnb, Expedia)</th><td class="c">No</td><td class="c">Yes</td><td class="c">Yes</td></tr>
<tr><th>Room rack calendar</th><td class="c">Yes</td><td class="c">Yes</td><td class="c">Yes</td></tr>
<tr><th>Accommodation confirmation for visas (PDF)</th><td class="c">Yes</td><td class="c">Yes</td><td class="c">Yes</td></tr>
<tr><th>Online check-in and digital signature</th><td class="c">No</td><td class="c">Yes</td><td class="c">Yes</td></tr>
<tr><th>Transfer and tour sales</th><td class="c">No</td><td class="c">Yes</td><td class="c">Yes</td></tr>
<tr><th>iOS and Android app</th><td class="c">Yes</td><td class="c">Yes</td><td class="c">Yes</td></tr>
<tr><th>Priority support and onboarding call</th><td class="c">No</td><td class="c">No</td><td class="c">Yes</td></tr>
<tr><th>White-label</th><td class="c">No</td><td class="c">No</td><td class="c">Yes</td></tr>
{FX.table_rows(L)}
</tbody></table></div></div></section>
'''
    return {"key":"features","title":"Hotel Management Software Features | Hostlio Pro",
            "desc":"Hostlio Pro features: AI guest assistant, 100+ OTA channel manager, drag-and-drop room rack, online check-in, visa letters, transfer sales, mobile app.",
            "trail":[("Features", U("features"))],"body":body,"faq":[FAQ_CORE[0], FAQ_CORE[3]]+FX.faq(L,"faq_import","faq_roles","faq_reports")}

def pricing():
    body = f'''
<section class="page-hero"><div class="wrap"><h1>Hostlio Pro pricing</h1>
<p class="lead">A flat monthly fee. No per-booking commission, no setup fee. Try any plan free for 7 days.</p></div></section>
<section style="padding-top:0"><div class="wrap"><h2 class="sr-only">Plans</h2>
<span class="billing-note">⟦eb_pct⟧ off for the first 50 customers, locked in for life</span>
{plans_html()}
<p class="small muted" style="margin-top:18px">Prices in US dollars, excluding taxes. Last updated: <time datetime="{UPDATED}">September 21, 2026</time>.</p>
</div></section>
<section class="white rule"><div class="wrap">
<div class="section-head"><h2>Which plan fits you?</h2></div>
<div class="rows">
<div class="row"><h3>Starter</h3><div><p>Guesthouses and boutique hotels with up to 10 rooms, sending fewer than ⟦quota:starter⟧ replies a month, who want to start with channel sync and AI replies.</p></div></div>
<div class="row"><h3>Pro</h3><div><p>Hotels with 11–50 rooms that want Lio to handle OTA messages too, use online check-in and sell transfers and tours.</p></div></div>
<div class="row"><h3>Growth</h3><div><p>Two properties or up to 150 rooms, when you need priority support, a custom onboarding and white-label use. With white-label, the check-in page and PDF documents your guests see carry your logo and colours with no Hostlio branding, the assistant uses the name you choose and emails go out under your hotel's name.</p></div></div>
</div></div></section>
'''
    faq = [FAQ_CORE[1], FAQ_CORE[2],
      ("Do you charge commission per booking?", "No. Hostlio Pro is a flat monthly subscription; it takes no percentage of booking value."),
      ("Is there an annual billing option?", "Yes. Subscriptions are billed monthly or annually in advance, and annual plans get a 20% discount (Terms of Service, section 3)."),
      ("Can I change plans?", "Yes. Upgrade or downgrade anytime. The change takes effect immediately, and the price difference is prorated on your next invoice."),
      ("How long does the early-bird discount last?", "It applies to the first 50 customers, and your price stays locked for as long as your subscription continues.")]
    return {"key":"pricing","title":"Hotel Software Pricing: Plans from ⟦price:starter⟧/month | Hostlio Pro",
            "desc":"Hostlio Pro pricing: Starter ⟦price:starter⟧, Pro ⟦price:pro⟧, Growth ⟦price:growth⟧ per month. No commission, no setup fee, 7-day free trial. Compare plans.",
            "trail":[("Pricing", U("pricing"))],"body":body,"faq":faq,"schema":[software_schema(L, detailed=True)]}

FAQ_ALL = FAQ_CORE + [
 ("What types of hotels is Hostlio Pro for?", "Independent properties with 1 to 150 rooms, such as boutique hotels, city hotels, guesthouses, aparthotels and hostels."),
 ("Is there a mobile app?", "Yes. Every plan, including Starter, includes the iOS and Android app. Manage bookings, messages and check-ins away from the hotel; analytics, notifications, maintenance reports and document scanning are in the app too."),
 ("How does online check-in work?", "Guests receive a personal secure link, scan their ID document on their phone (no image is stored) and send accompanying guests and a digital signature before arrival. Available on Pro and Growth."),
 ("What is the accommodation confirmation for visas?", "For guests who need a visa, it creates an accommodation confirmation from the reservation data in one click, to use in a visa or invitation application. You can save it as a PDF or print it."),
 ("Is my data secure?", "Data is transmitted over encrypted connections, and each hotel's data is isolated from other properties with row-level access rules. You can delete a guest's profile from the dashboard, and signatures and conversations are deleted or anonymised automatically after set periods."),
 ("How long does setup take?", "Your account is ready in minutes. Most hotels connect their channels the same day: add room types and rooms, authorise the connection in each OTA's extranet and map your rooms. The Growth plan includes a custom onboarding call."),
 ("Which languages is support offered in?", "Support is available in English and Turkish. The dashboard, mobile app and guest check-in form are available in 6 languages: English, Turkish, Spanish, French, Italian and Portuguese. Reach us at " + EMAIL + "."),
] + FX.faq(L,"faq_import","faq_roles","faq_reports","faq_owner")

def faq_page():
    body = f'''<section class="page-hero"><div class="wrap"><h1>Frequently asked questions</h1>
<p class="lead">The most common questions about Hostlio Pro's features, pricing and setup. Can't find your answer? <a href="{U("contact")}">Write to us</a>.</p></div></section>
<section style="padding-top:0"><div class="wrap">{faq_block(FAQ_ALL, L, heading=False, wrap=False)}</div></section>'''
    return {"key":"faq","title":"Hostlio Pro FAQ: Frequently Asked Questions",
            "desc":"Common questions about Hostlio Pro hotel management software: pricing, free trial, OTA integrations, the Lio AI assistant, online check-in and security.",
            "trail":[("FAQ", U("faq"))],"body":body,"faq":FAQ_ALL,"faq_inline":True,"page_type":"FAQPage"}

def about():
    body = f'''<section class="page-hero"><div class="wrap split"><div><h1>Why we built Hostlio Pro</h1>
<p class="lead">In small hotels, reception, sales and guest communication often sit on one person's shoulders. Hostlio Pro exists so that person isn't buried in messages at night and channel screens by day.</p></div><div class="hero-img"><img src="/assets/img/about-ledger.webp" alt="" width="1080" height="1341"></div></div></section>
<section class="white rule"><div class="wrap split">
<div class="prose"><h2>What we do</h2>
<p>Hostlio Pro is AI-powered hotel management software for independent hotels. We hand guest communication to our AI assistant Lio, bring OTA distribution onto one calendar over certified connections, and move check-in to the guest's phone.</p>
<h2>How we work</h2>
<ul><li>We publish our prices openly and take no commission.</li><li>We build from the real daily work of hoteliers.</li><li>No long contracts; customers stay because they're happy.</li></ul></div>
<div class="panel"><p class="panel-title">Company details</p><dl class="list-kv">
<dt>Product</dt><dd>Hostlio Pro (also “Hostlio”)</dd><dt>Company</dt><dd>Loti Members LLC</dd>
<dt>Address</dt><dd>2108 N ST STE N, Sacramento, CA 95816, USA</dd><dt>Email</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd>
<dt>Customers</dt><dd>Independent hotels in 20+ countries</dd></dl></div>
</div></section>'''
    return {"key":"about","title":"About Hostlio Pro","desc":"Hostlio Pro builds AI-powered hotel management software for independent hotels. Operated by Loti Members LLC and used in 20+ countries.",
            "trail":[("About", U("about"))],"body":body,"page_type":"AboutPage"}

def contact():
    from build import FORM_ENDPOINT
    act = f' action="{FORM_ENDPOINT}" method="post"' if FORM_ENDPOINT else ""
    body = f'''<section class="page-hero"><div class="wrap split" style="align-items:start">
<div><h1>Book a demo or get in touch</h1>
<p class="lead">Tell us briefly about your hotel and the channels you use, and we'll show you Hostlio Pro with your own rooms in a 30-minute call.</p>
<p>Email us directly: <a href="mailto:{EMAIL}">{EMAIL}</a></p></div>
<form class="contact" data-contact-form data-mail="{EMAIL}" data-subject="Demo request" data-sent="Your email app has opened. Press send and your request reaches us."{act}>
<label>Full name<input name="name" autocomplete="name" required></label>
<label>Email<input type="email" name="email" autocomplete="email" required></label>
<label>Hotel name<input name="hotel" autocomplete="organization" required></label>
<label>Number of rooms<select name="rooms"><option>1–10</option><option>11–50</option><option>51–150</option><option>150+</option></select></label>
<label>Country / city<input name="country" autocomplete="country-name"></label>
<label>Message <span class="hint">Channels you use, current software</span><textarea name="message" rows="4"></textarea></label>
<button class="btn btn-primary" type="submit">Send demo request</button>
<p class="form-status" role="status" aria-live="polite"></p>
</form></div></section>'''
    return {"key":"contact","title":"Contact and Demo Request | Hostlio Pro","desc":"Contact the Hostlio Pro team or book a free 30-minute demo tailored to your hotel. Support in English and Turkish, email: " + EMAIL,
            "trail":[("Contact", U("contact"))],"body":body,"page_type":"ContactPage","no_final":True}

POSTS = [
 {"key":"post-overbooking","title":"How to prevent overbooking: 6 steps for hotels","date":"2026-09-21","desc":"Why hotels get overbooked and how to prevent it: channel manager, stop-sell rules, availability buffers and what to do when it happens anyway."},
 {"key":"post-autoreply","title":"How to auto-reply to Booking.com guest messages","date":"2026-09-21","desc":"Three ways to automate Booking.com guest messages: templates, scheduled messages and an AI assistant."},
 {"key":"post-ai","title":"Answering hotel guest messages with AI: a practical guide","date":"2026-09-18",
  "desc":"The benefits, risks and setup steps of answering hotel guest messages with AI. Which questions to automate and which should stay with your team."},
 {"key":"post-pms","title":"PMS for small hotels: how to choose (7 criteria, 2026)","date":"2026-09-10",
  "desc":"How to choose a PMS for a small or boutique hotel: 7 criteria, what it should cost, and why a built-in channel manager and guest messaging matter."},
]

POSTS += __import__("legal_v5").legacy_meta()
import guides_intl as _gi
POSTS = _gi.meta(L) + POSTS
def blog():
    items = "".join(f'<article><h2><a href="{U(p["key"])}">{p["title"]}</a></h2><p class="meta"><time datetime="{p["date"]}">{p["date"]}</time></p><p>{p["desc"]}</p></article>' for p in [dict(p, **{k: v for k, v in __import__("pages_v4").post_meta(L).get(p["key"], {}).items() if k in ("title", "desc")}) for p in POSTS])
    body = f'<section class="page-hero"><div class="wrap"><h1>Blog for hoteliers</h1><p class="lead">Practical writing on running an independent hotel, distribution and guest communication.</p></div></section><section style="padding-top:0"><div class="wrap post-list">{items}</div></section>'
    return {"key":"blog","title":"Blog: Guides for Independent Hotels | Hostlio Pro","desc":"Practical guides for independent hoteliers on hotel management, channel management, OTA distribution and AI guest communication.",
            "trail":[("Blog", U("blog"))],"body":body,"page_type":"CollectionPage"}

COVERS={"post-ai":("gen-checkin-phone",1080,1350),"post-pms":("gen-owner-laptop",1080,1350),"post-overbooking":("overbooking-desk",1080,1341),"post-autoreply":("guest-balcony-dusk",1080,1341)}
COVERS.update(_gi.COVER)
import legal_v5 as _lg
COVERS.update(_lg.LEGACY_COVER)
def article(meta, content, faq=None):
    art = {"@type":"BlogPosting","headline":meta["title"],"description":meta["desc"],"datePublished":meta["date"],"inLanguage":"en","author":{"@type":"Organization","name":"Hostlio Pro product team","url":SITE+"/en/about/"},"dateModified":UPDATED,"publisher":{"@id":SITE+"/#org"},
           "mainEntityOfPage":SITE+U(meta["key"]),"image":SITE+"/assets/img/"+COVERS[meta["key"]][0]+".webp"}
    body = f'<article><section class="page-hero"><div class="wrap"><h1 style="max-width:22ch">{meta["title"]}</h1><p class="meta">By the <a href="/en/about/">Hostlio Pro product team</a>, the people who build Hostlio Pro. Published <time datetime="{meta["date"]}">{meta["date"]}</time>, updated <time datetime="{UPDATED}">{UPDATED}</time></p></div></section><section style="padding-top:0"><div class="wrap"><figure class="post-cover"><img src="/assets/img/{COVERS[meta["key"]][0]}.webp" alt="" width="{COVERS[meta["key"]][1]}" height="{COVERS[meta["key"]][2]}"></figure><div class="prose">{content}</div></div></section></article>'
    return {"key":meta["key"],"title":meta["title"],"desc":meta["desc"],"og_type":"article",
            "trail":[("Blog",U("blog")),(meta["title"],U(meta["key"]))],"body":body,"schema":[art],"faq":faq or []}

def post_ai():
    import rehber_ai_yanit
    c, faq = rehber_ai_yanit.get(L, U)
    return article(next(p for p in POSTS if p["key"]=="post-ai"), c, faq)

def post_pms():
    # 12 Ekim 2026: genişletildi (rehber_pms_secim)
    import rehber_pms_secim
    c, faq = rehber_pms_secim.get(L, U)
    return article(next(p for p in POSTS if p["key"]=="post-pms"), c, faq)

def pages():
    import pages_v4
    return [home(), ai(), channel(), checkin(), features(), pricing(), faq_page(), about(), contact(), blog(), post_ai(), post_pms()] + pages_v4.pages(L, article) + __import__("legal_v5").pages(L, article)
