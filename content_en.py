from build import btn, icon, logo, url, room_rack, channel_strip, faq_block, SIGNUP_URL, EMAIL, UPDATED, CHECK, software_schema, SITE, PLANS
L = "en"
def U(k): return url(k, L)

PLAN_TXT = {
 "starter": ("For small guesthouses and boutique hotels", ["1 property, up to 10 rooms","1,000 AI messages / month","Channel sync with 100+ OTAs","WhatsApp AI messaging","Room rack reservation calendar","Automatic PDF visa forms"]),
 "pro":     ("For growing single-property hotels", ["1 property, up to 50 rooms","5,000 AI messages / month","Everything in Starter","WhatsApp + OTA inbox messaging (Booking.com, Airbnb, Expedia)","Online check-in with digital signature","Transfer and tour sales","Mobile app"]),
 "growth":  ("For teams running two properties", ["Up to 2 properties, 150 rooms","12,000 AI messages / month","Everything in Pro","Priority channel sync","Priority support (next business day)","Custom onboarding call","White-label options"]),
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
<div class="price num"><b>${p["price"]}</b><span class="muted">/ month</span></div>
<p class="small muted num" style="margin:0">Early-bird price (regularly <s>${p["regular"]}</s>)</p>
<ul>{lis}</ul>
{btn("Start with "+p["name"], SIGNUP_URL+"?plan="+p["id"], "primary" if pop else "ghost")}
</article>''')
    return '<div class="plans">' + "".join(out) + "</div>"

FAQ_CORE = [
 ("What is Hostlio Pro?", "Hostlio Pro is AI-powered hotel management software (PMS) built for independent hotels, boutique hotels and guesthouses. It combines Lio, an AI assistant that answers guest messages 24/7 in 30+ languages, a channel manager connected to 100+ OTAs, a drag-and-drop reservation calendar and online check-in in one platform."),
 ("How much does Hostlio Pro cost?", "There are three plans: Starter at $49/month, Pro at $89/month and Growth at $149/month. These prices include a 20% early-bird discount for the first 50 customers, locked in for as long as you stay subscribed. Regular prices are $59, $109 and $189."),
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
<p class="small muted" style="margin:10px 0 0">Transfer booked, payment link sent.</p></div>
</div></section>

<section class="white rule"><div class="wrap">
<div class="answer"><p><strong>What is an AI guest messaging assistant for hotels?</strong> Software that automatically answers the questions guests ask before and after booking, using the hotel's own information. Lio hands over messages it can't answer, or that need a human decision (discount requests, complaints, special requests), to your staff.</p></div>
<h2 style="margin-top:64px">What Lio does</h2><div class="rows">
<div class="row"><h3>One inbox</h3><div><p>WhatsApp and OTA inbox messages (Booking.com, Airbnb, Expedia) land on one screen. Lio automatically matches each guest to their reservation.</p></div></div>
<div class="row"><h3>30+ languages, auto-translated</h3><div><p>The guest writes in Japanese, Lio replies in Japanese, and you read the conversation in your own language. Manual replies are translated into the guest's language too.</p></div></div>
<div class="row"><h3>Knows your hotel</h3><div><p>Check-in and check-out times, parking, pet policy, breakfast hours, transport and room features. Enter them once and Lio uses them consistently in every reply.</p></div></div>
<div class="row"><h3>An assistant that sells</h3><div><p>Lio doesn't just answer questions: it offers airport transfers, city tours and extras at the right moment and creates the booking.</p></div></div>
<div class="row"><h3>You stay in control</h3><div><p>During the first days you can approve Lio's replies before they're sent. You decide which topics Lio closes on its own and which it hands to you.</p></div></div>
</div></div></section>

<section><div class="wrap">
<div class="section-head"><h2>AI message quota by plan</h2><p>One message is a single reply Lio sends to a guest.</p></div>
<div class="table-wrap"><table><thead><tr><th>Plan</th><th class="c">AI messages / month</th><th>Messaging channels</th></tr></thead><tbody>
<tr><th>Starter</th><td class="c num">1,000</td><td>WhatsApp</td></tr>
<tr><th>Pro</th><td class="c num">5,000</td><td>WhatsApp + OTA inboxes (Booking.com, Airbnb, Expedia)</td></tr>
<tr><th>Growth</th><td class="c num">12,000</td><td>WhatsApp + OTA inboxes (Booking.com, Airbnb, Expedia)</td></tr>
</tbody></table></div>
</div></section>
'''
    faq = [
     ("What if Lio gives wrong information?", "Lio only uses the hotel information and reservation data you provide. When it isn't sure, it hands the message to you instead of guessing. You can also approve every reply before it's sent."),
     ("Does it answer Booking.com and Airbnb messages too?", "Yes. On the Pro and Growth plans, OTA messages arrive in Lio's inbox and are answered the same way."),
     ("What happens when the message quota runs out?", "Messages keep arriving and appear in your dashboard; only automatic replies pause. You can upgrade to a higher plan to increase your quota."),
     FAQ_CORE[4],
    ]
    return {"key":"ai","title":"AI Guest Messaging for Hotels in 30+ Languages | Hostlio Pro",
            "desc":"Hostlio Pro's AI assistant Lio answers hotel guests on WhatsApp and OTA inboxes 24/7 in 30+ languages, and sells transfers and tours. See how it works.",
            "trail":[("Lio AI assistant", U("ai"))],"body":body,"faq":faq}

def channel():
    body = f'''
<section class="page-hero"><div class="wrap split">
<div><h1>A channel manager for 100+ OTAs</h1>
<p class="lead">Manage availability, rates and bookings on Booking.com, Airbnb, Expedia, Agoda and 100+ other channels from one calendar. Hostlio Pro syncs in real time, both ways, through Channex.</p>
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
<h2 style="margin-top:64px">What the channel manager does</h2><div class="rows">
<div class="row"><h3>Two-way sync</h3><div><p>New bookings, modifications and cancellations drop onto the room rack automatically, and changes you make in the calendar go out to every channel.</p></div></div>
<div class="row"><h3>Rates and restrictions</h3><div><p>Push rates, minimum stays and stop-sells per room type to all channels from one screen.</p></div></div>
<div class="row"><h3>Colour-coded room rack</h3><div><p>See at a glance which channel each booking came from. Reassign rooms with drag and drop.</p></div></div>
<div class="row"><h3>Connected to messaging</h3><div><p>Guest messages for OTA bookings land in Lio's inbox with the guest, room and dates alongside every conversation.</p></div></div>
</div></div></section>
<section><div class="wrap"><div class="section-head"><h2>Main supported channels</h2><p>The list follows Channex's connection network. Missing a channel? Get in touch.</p></div>
<div class="table-wrap"><table><thead><tr><th>Channel</th><th>Type</th></tr></thead><tbody>
<tr><th>Booking.com</th><td>OTA</td></tr><tr><th>Airbnb</th><td>Short-term rental</td></tr><tr><th>Expedia, Hotels.com</th><td>OTA</td></tr>
<tr><th>Agoda, Trip.com</th><td>OTA (Asia-focused)</td></tr><tr><th>Hotelbeds</th><td>Wholesaler (bedbank)</td></tr><tr><th>Hostelworld</th><td>Hostel marketplace</td></tr><tr><th>Google Hotels</th><td>Metasearch</td></tr>
</tbody></table></div></div></section>
'''
    faq = [FAQ_CORE[3],
     ("Is the channel manager included in every plan?", "Yes. Starter, Pro and Growth all include channel sync with 100+ OTAs. Growth adds priority sync."),
     ("Is it hard to switch from my current channel manager?", "No. Create your room types in Hostlio Pro and map your OTA accounts through Channex. Our onboarding team helps during the switch."),
    ]
    return {"key":"channel","title":"Hotel Channel Manager for 100+ OTAs | Hostlio Pro",
            "desc":"Hostlio Pro's channel manager syncs availability and rates across 100+ OTAs including Booking.com, Airbnb, Expedia and Agoda in real time and prevents overbooking.",
            "trail":[("Channel manager", U("channel"))],"body":body,"faq":faq}

def checkin():
    body = f'''
<section class="page-hero"><div class="wrap split">
<div><h1>Online check&#8209;in with digital signature</h1>
<p class="lead">Before arrival, guests send their ID details, accompanying guests and signature from their phone. Handing over the key takes minutes.</p>
<div class="cta-row">{btn("Try Pro free for 7 days", SIGNUP_URL+"?plan=pro")}</div></div>
<div class="panel"><p class="panel-title">Online check-in, Room 202</p>
<div class="field"><span>Full name</span><div>Keiko Sato</div></div>
<div class="field"><span>Nationality</span><div>Japan</div></div>
<div class="field"><span>Accompanying guests</span><div>1 guest added</div></div>
<div class="field"><span>Signature</span><div class="sig">Digital signature received</div></div>
</div>
</div></section>
<section class="white rule"><div class="wrap">
<div class="answer"><p><strong>How does online check-in work?</strong> Hostlio Pro sends the booker a personal, time-limited, secure link. From that link the guest enters ID details, adds an ID photo and any accompanying guests, and signs the form digitally. Everything is saved straight to the reservation.</p></div>
<h2 style="margin-top:64px">Online check-in features</h2><div class="rows">
<div class="row"><h3>Secure link</h3><div><p>A token-based link unique to each reservation. It only opens that reservation's form.</p></div></div>
<div class="row"><h3>Accompanying guests</h3><div><p>Everyone staying in the room is added in one form, so nobody has to type details at the desk.</p></div></div>
<div class="row"><h3>Digital signature and consent</h3><div><p>Guests accept house rules and data consent by signing on screen. The signed record is stored with the reservation.</p></div></div>
<div class="row"><h3>Privacy by design</h3><div><p>Guest data can be deleted on request, and the consent text is part of the form.</p></div></div>
<div class="row"><h3>Export for official reporting</h3><div><p>Collected guest details can be exported in a format you can use for local guest registration requirements.</p></div></div>
</div></div></section>
<section class="dark on-dark"><div class="wrap"><div class="section-head"><h2>Three steps for the guest</h2></div>
<ol class="steps"><li><h3>Open the link</h3><p>Open the personal link received after the booking is confirmed (sent by email automatically, or shared by the hotel).</p></li>
<li><h3>Fill in details</h3><p>Add ID details and a photo, and list accompanying guests.</p></li>
<li><h3>Sign</h3><p>Accept house rules and sign on screen. At reception, just pick up the key.</p></li></ol>
</div></section>
'''
    faq = [("Which plans include online check-in?", "Online check-in with digital signature is included in the Pro and Growth plans."),
           ("Does the guest need to download an app?", "No. The check-in form opens in the browser; no app download is required."),
           ("What if a guest doesn't complete the link?", "Check them in the usual way. Staff can also enter details at the desk using the Hostlio Pro mobile app.")]
    return {"key":"checkin","title":"Hotel Online Check-in with Digital Signature | Hostlio Pro",
            "desc":"With Hostlio Pro online check-in, guests send ID details, accompanying guests and a digital signature from their phone before arrival. No queue at reception.",
            "trail":[("Online check-in", U("checkin"))],"body":body,"faq":faq}

def features():
    body = f'''
<section class="page-hero"><div class="wrap split"><div><h1>Everything in Hostlio Pro</h1>
<p class="lead">The modules an independent hotel needs day to day: guest communication, distribution, reservations, check-in and extra revenue.</p></div><div class="hero-img"><img src="/assets/img/brand-hotelier.webp" alt="Hotel owner walking through the lobby with a morning coffee" width="720" height="900"></div></div></section>
<section class="white rule"><div class="wrap"><h2 class="sr-only">Modules</h2><div class="rows">
<div class="row"><h3>Lio AI assistant</h3><div><p>24/7 guest replies in 30+ languages. WhatsApp and OTA inbox messages (Booking.com, Airbnb, Expedia) in one inbox.</p><a href="{U("ai")}">More about Lio</a></div></div>
<div class="row"><h3>Channel manager</h3><div><p>Availability, rate and booking sync with 100+ OTAs through Channex.</p><a href="{U("channel")}">Channel manager</a></div></div>
<div class="row"><h3>Room rack</h3><div><p>Drag-and-drop reservation calendar. Room moves, extensions and blocks in one gesture.</p></div></div>
<div class="row"><h3>Online check-in</h3><div><p>Secure link, accompanying guests, ID photo and digital signature.</p><a href="{U("checkin")}">Online check-in</a></div></div>
<div class="row"><h3>Automatic PDF visa forms</h3><div><p>Generate hotel invitation and accommodation letters for visa applications from reservation data in one click.</p></div></div>
<div class="row"><h3>Transfer and tour sales</h3><div><p>Offer airport transfers and tours during the conversation; Lio attaches the request to the reservation.</p></div></div>
<div class="row"><h3>Mobile app</h3><div><p>Manage bookings, messages and check-ins away from the hotel with the iOS app. It keeps working offline and syncs when you're back online.</p></div></div>
</div></div></section>
<section><div class="wrap"><div class="section-head"><h2>Features by plan</h2></div>
<div class="table-wrap"><table><thead><tr><th>Feature</th><th class="c">Starter</th><th class="c">Pro</th><th class="c">Growth</th></tr></thead><tbody>
<tr><th>Properties</th><td class="c">1</td><td class="c">1</td><td class="c">2</td></tr>
<tr><th>Room limit</th><td class="c num">10</td><td class="c num">50</td><td class="c num">150</td></tr>
<tr><th>AI messages / month</th><td class="c num">1,000</td><td class="c num">5,000</td><td class="c num">12,000</td></tr>
<tr><th>Channel sync with 100+ OTAs</th><td class="c">Yes</td><td class="c">Yes</td><td class="c">Priority</td></tr>
<tr><th>WhatsApp AI messaging</th><td class="c">Yes</td><td class="c">Yes</td><td class="c">Yes</td></tr>
<tr><th>OTA inbox messaging (Booking.com, Airbnb, Expedia)</th><td class="c">No</td><td class="c">Yes</td><td class="c">Yes</td></tr>
<tr><th>Room rack calendar</th><td class="c">Yes</td><td class="c">Yes</td><td class="c">Yes</td></tr>
<tr><th>PDF visa forms</th><td class="c">Yes</td><td class="c">Yes</td><td class="c">Yes</td></tr>
<tr><th>Online check-in and digital signature</th><td class="c">No</td><td class="c">Yes</td><td class="c">Yes</td></tr>
<tr><th>Transfer and tour sales</th><td class="c">No</td><td class="c">Yes</td><td class="c">Yes</td></tr>
<tr><th>iOS mobile app</th><td class="c">No</td><td class="c">Yes</td><td class="c">Yes</td></tr>
<tr><th>Priority support and onboarding call</th><td class="c">No</td><td class="c">No</td><td class="c">Yes</td></tr>
<tr><th>White-label</th><td class="c">No</td><td class="c">No</td><td class="c">Yes</td></tr>
</tbody></table></div></div></section>
'''
    return {"key":"features","title":"Hotel Management Software Features | Hostlio Pro",
            "desc":"Hostlio Pro features: AI guest assistant, channel manager for 100+ OTAs, drag-and-drop room rack, online check-in, PDF visa forms, transfer sales and a mobile app.",
            "trail":[("Features", U("features"))],"body":body,"faq":[FAQ_CORE[0], FAQ_CORE[3]]}

def pricing():
    body = f'''
<section class="page-hero"><div class="wrap"><h1>Hostlio Pro pricing</h1>
<p class="lead">A flat monthly fee. No per-booking commission, no setup fee. Try any plan free for 7 days.</p></div></section>
<section style="padding-top:0"><div class="wrap"><h2 class="sr-only">Plans</h2>
<span class="billing-note">20% off for the first 50 customers, locked in for life</span>
{plans_html()}
<p class="small muted" style="margin-top:18px">Prices in US dollars, excluding taxes. Last updated: <time datetime="{UPDATED}">September 21, 2026</time>.</p>
</div></section>
<section class="white rule"><div class="wrap">
<div class="section-head"><h2>Which plan fits you?</h2></div>
<div class="rows">
<div class="row"><h3>Starter</h3><div><p>Guesthouses and boutique hotels with up to 10 rooms, sending fewer than 1,000 replies a month, who want to start with channel sync and AI replies.</p></div></div>
<div class="row"><h3>Pro</h3><div><p>Hotels with 11–50 rooms that want Lio to handle OTA messages too, use online check-in and sell transfers and tours.</p></div></div>
<div class="row"><h3>Growth</h3><div><p>Two properties or up to 150 rooms, when you need priority support, a custom onboarding and white-label use.</p></div></div>
</div></div></section>
'''
    faq = [FAQ_CORE[1], FAQ_CORE[2],
      ("Do you charge commission per booking?", "No. Hostlio Pro is a flat monthly subscription; it takes no percentage of booking value."),
      ("Is there an annual billing option?", "Yes. Subscriptions are billed monthly or annually in advance, and annual plans get a 20% discount (Terms of Service, section 3)."),
      ("Can I change plans?", "Yes. Upgrade or downgrade anytime; the change applies from your next billing period."),
      ("How long does the early-bird discount last?", "It applies to the first 50 customers, and your price stays locked for as long as your subscription continues.")]
    return {"key":"pricing","title":"Hotel Software Pricing: Plans from $49/month | Hostlio Pro",
            "desc":"Hostlio Pro pricing: Starter $49, Pro $89, Growth $149 per month. No commission, no setup fee, 7-day free trial. Compare plans.",
            "trail":[("Pricing", U("pricing"))],"body":body,"faq":faq,"schema":[software_schema(L, detailed=True)]}

FAQ_ALL = FAQ_CORE + [
 ("What types of hotels is Hostlio Pro for?", "Independent properties with 10 to 150 rooms, such as boutique hotels, city hotels, guesthouses, aparthotels and hostels."),
 ("Is there a mobile app?", "Yes. The Pro and Growth plans include an iOS app. It works without an internet connection and syncs data when you're back online."),
 ("How does online check-in work?", "Guests receive a personal secure link and send ID details, accompanying guests and a digital signature from their phone before arrival. Available on Pro and Growth."),
 ("What is the PDF visa form feature for?", "It automatically turns reservation data into hotel accommodation and invitation letters as PDFs for guests who need a visa."),
 ("Is my data secure?", "Data is transmitted over encrypted connections, and each hotel's data is isolated from other properties with row-level access rules. Guest data can be deleted on request."),
 ("How long does setup take?", "Most hotels start the same day by adding room types and connecting channels. The Growth plan includes a custom onboarding call."),
 ("Which languages is support offered in?", "The dashboard and support are available in English and Turkish. Reach us at " + EMAIL + "."),
]

def faq_page():
    body = f'''<section class="page-hero"><div class="wrap"><h1>Frequently asked questions</h1>
<p class="lead">The most common questions about Hostlio Pro's features, pricing and setup. Can't find your answer? <a href="{U("contact")}">Write to us</a>.</p></div></section>
<section style="padding-top:0"><div class="wrap">{faq_block(FAQ_ALL, L, heading=False, wrap=False)}</div></section>'''
    return {"key":"faq","title":"Hostlio Pro FAQ: Frequently Asked Questions",
            "desc":"Frequently asked questions about Hostlio Pro hotel management software: pricing, free trial, OTA integrations, the Lio AI assistant, online check-in and security.",
            "trail":[("FAQ", U("faq"))],"body":body,"faq":FAQ_ALL,"faq_inline":True,"page_type":"FAQPage"}

def about():
    body = f'''<section class="page-hero"><div class="wrap split"><div><h1>Why we built Hostlio Pro</h1>
<p class="lead">In small hotels, reception, sales and guest communication often sit on one person's shoulders. Hostlio Pro exists so that person isn't buried in messages at night and channel screens by day.</p></div><div class="hero-img"><img src="/assets/img/brand-courtyard.webp" alt="Boutique hotel courtyard with a pool and bougainvillea" width="880" height="804"></div></div></section>
<section class="white rule"><div class="wrap split">
<div class="prose"><h2>What we do</h2>
<p>Hostlio Pro is AI-powered hotel management software for independent hotels. We hand guest communication to our AI assistant Lio, bring OTA distribution onto one calendar through Channex, and move check-in to the guest's phone.</p>
<h2>How we work</h2>
<ul><li>We publish our prices openly and take no commission.</li><li>We build from the real daily work of hoteliers.</li><li>No long contracts; customers stay because they're happy.</li></ul></div>
<div class="panel"><p class="panel-title">Company details</p><dl class="list-kv">
<dt>Product</dt><dd>Hostlio Pro (Hostlio Pro)</dd><dt>Company</dt><dd>Loti Members LLC</dd>
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
 {"key":"post-pms","title":"How to choose hotel management software (PMS) for a small hotel","date":"2026-09-10",
  "desc":"7 criteria for choosing a PMS for a small or boutique hotel: channel manager, pricing model, guest messaging, mobile access and more."},
]

POSTS += __import__("legal_v5").legacy_meta()
def blog():
    items = "".join(f'<article><h2><a href="{U(p["key"])}">{p["title"]}</a></h2><p class="meta"><time datetime="{p["date"]}">{p["date"]}</time></p><p>{p["desc"]}</p></article>' for p in POSTS)
    body = f'<section class="page-hero"><div class="wrap"><h1>Blog for hoteliers</h1><p class="lead">Practical writing on running an independent hotel, distribution and guest communication.</p></div></section><section style="padding-top:0"><div class="wrap post-list">{items}</div></section>'
    return {"key":"blog","title":"Blog: Guides for Independent Hotels | Hostlio Pro","desc":"Practical guides for independent hoteliers on hotel management, channel management, OTA distribution and AI guest communication.",
            "trail":[("Blog", U("blog"))],"body":body,"page_type":"CollectionPage"}

COVERS={"post-ai":("brand-guest-bed",1200,675),"post-pms":("hostlio-lobby",720,900),"post-overbooking":("brand-hotelier",720,900),"post-autoreply":("brand-phone",720,900)}
import legal_v5 as _lg
COVERS.update(_lg.LEGACY_COVER)
def article(meta, content, faq=None):
    art = {"@type":"BlogPosting","headline":meta["title"],"description":meta["desc"],"datePublished":meta["date"],"inLanguage":"en","author":{"@type":"Organization","name":"Hostlio Pro product team","url":SITE+"/en/about/"},"dateModified":UPDATED,"publisher":{"@id":SITE+"/#org"},
           "mainEntityOfPage":SITE+U(meta["key"]),"image":SITE+"/assets/img/"+COVERS[meta["key"]][0]+".webp"}
    body = f'<article><section class="page-hero"><div class="wrap"><h1 style="max-width:22ch">{meta["title"]}</h1><p class="meta">By the <a href="/en/about/">Hostlio Pro product team</a>, the people who build Hostlio Pro. Published <time datetime="{meta["date"]}">{meta["date"]}</time>, updated <time datetime="{UPDATED}">{UPDATED}</time></p></div></section><section style="padding-top:0"><div class="wrap"><figure class="post-cover"><img src="/assets/img/{COVERS[meta["key"]][0]}.webp" alt="" width="{COVERS[meta["key"]][1]}" height="{COVERS[meta["key"]][2]}"></figure><div class="prose">{content}</div></div></section></article>'
    return {"key":meta["key"],"title":meta["title"],"desc":meta["desc"],"og_type":"article",
            "trail":[("Blog",U("blog")),(meta["title"],U(meta["key"]))],"body":body,"schema":[art],"faq":faq or []}

def post_ai():
    c = f'''
<div class="answer"><p><strong>Short answer:</strong> Most hotel messages are repeat questions (check-in time, parking, transfers, breakfast). Handing them to an AI assistant trained on your hotel's own information gets guests an answer in seconds, in their language. Discounts, complaints and special requests should stay with your staff.</p></div>
<h2>Which questions do hotels get most?</h2>
<p>At independent hotels, most messages cluster around a few topics:</p>
<ul><li>Check-in and check-out times, early arrival or late departure</li><li>Airport transfers and getting there</li><li>Parking, breakfast, pet policy</li><li>Luggage storage, room features, the neighbourhood</li><li>Booking changes and invoice requests</li></ul>
<p>The answers already exist at the hotel. The problem is giving them in the right language at the right hour.</p>
<h2>What should AI automate, and what shouldn't it?</h2>
<p>In a good setup the assistant closes information questions and hands decisions to staff.</p>
<div class="table-wrap"><table><thead><tr><th>Let AI answer</th><th>Hand to staff</th></tr></thead><tbody>
<tr><td>Times, rules, amenities</td><td>Discounts and price negotiation</td></tr><tr><td>Directions, transfer information</td><td>Complaints and compensation</td></tr><tr><td>Transfer and tour sales</td><td>Medical or safety situations</td></tr><tr><td>Reminding guests of booking details</td><td>Group and event requests</td></tr></tbody></table></div>
<h2>Step-by-step setup</h2>
<ol><li><strong>Write your hotel knowledge base.</strong> Times, rules, amenities and FAQs. The clearer it is, the more consistent the answers.</li>
<li><strong>Connect your channels.</strong> Bring WhatsApp and OTA inbox messages into one inbox.</li>
<li><strong>Start in approval mode.</strong> For the first week, read and correct replies before they go out.</li>
<li><strong>Set handover rules.</strong> Define which topics come to you.</li>
<li><strong>Switch to automatic.</strong> Once replies are consistent, let the assistant handle information questions fully.</li></ol>
<h2>Why multilingual replies matter</h2>
<p>Guests who write in their own language share more detail and trust the answer more. An assistant that replies in 30+ languages builds that trust even when nobody at reception speaks the language, and you still read the conversation in yours.</p>
<h2>How it works in Hostlio Pro</h2>
<p>Hostlio Pro's AI assistant <a href="{U("ai")}">Lio</a> uses your hotel information and reservation data to answer WhatsApp and OTA inbox messages (Booking.com, Airbnb, Expedia) in 30+ languages. Plans include between 1,000 and 12,000 AI messages a month; see the <a href="{U("pricing")}">pricing page</a> for details.</p>'''
    faq = [("Can AI give guests wrong information?", "The risk is minimal when the assistant only works from information the hotel provides and hands uncertain questions to staff. Starting in approval mode is recommended."),
           ("Will guests know they're talking to AI?", "Replies are written in the hotel's name and tone. For transparency, hotels can mention in the welcome message that the assistant is AI.")]
    return article(next(p for p in POSTS if p["key"]=="post-ai"), c, faq)

def post_pms():
    c = f'''
<div class="answer"><p><strong>Short answer:</strong> The right PMS for a small hotel has a built-in channel manager, flat and transparent pricing, one inbox for guest messages, mobile access and same-day setup. Enterprise systems with hundreds of features tend to go unused by small teams.</p></div>
<h2>1. A built-in channel manager</h2>
<p>If you sell on Booking.com, Airbnb and Expedia at the same time, availability has to sync instantly. A separate channel manager means extra cost and another screen. Whether the PMS includes one, and how many channels it connects to, is the first thing to check.</p>
<h2>2. Pricing model</h2>
<p>Some software charges a percentage of booking value on top of the monthly fee, so costs rise with occupancy. A flat monthly price keeps your budget predictable. With vendors who don't publish prices, expect a sales process.</p>
<h2>3. Guest communication</h2>
<p>When messages are scattered across WhatsApp and several OTA inboxes, response times suffer. One inbox plus automatic replies is the biggest time saver for small teams.</p>
<h2>4. A usable room rack</h2>
<p>The reservation calendar is the screen your front desk looks at most. Drag-and-drop room moves and seeing each booking's channel at a glance speed up daily work.</p>
<h2>5. Mobile access</h2>
<p>Owners are often away from the property. A mobile app, especially one that works through internet outages, is a real need.</p>
<h2>6. Online check-in</h2>
<p>Collecting guest details before arrival saves time at reception and simplifies guest registration requirements.</p>
<h2>7. Setup and support</h2>
<p>A small hotel can't absorb a weeks-long implementation project. Choose software you can use the same day, with support in your language, and test the trial with real bookings.</p>
<h2>Checklist</h2>
<div class="table-wrap"><table><thead><tr><th>Criterion</th><th>Question to ask</th></tr></thead><tbody>
<tr><td>Channel manager</td><td>Is it included, and how many channels does it connect to?</td></tr><tr><td>Pricing</td><td>Is it flat, is there commission, is the price public?</td></tr>
<tr><td>Messaging</td><td>Are WhatsApp and OTA messages in one place, with automatic replies?</td></tr><tr><td>Mobile</td><td>Is there an app, and does it work offline?</td></tr>
<tr><td>Check-in</td><td>Is there online check-in with digital signature?</td></tr><tr><td>Trial</td><td>Is there a free trial and commitment-free cancellation?</td></tr></tbody></table></div>
<p>Hostlio Pro was built around these criteria: see the <a href="{U("features")}">features</a> and <a href="{U("pricing")}">pricing</a>.</p>'''
    faq = [("Does a small hotel need a PMS?", "If you sell on several OTAs and get dozens of messages a day, yes. Working with spreadsheets and separate OTA extranets raises the risk of overbookings and slow replies."),
           ("What's the difference between a PMS and a channel manager?", "A PMS runs the hotel's internal operations (reservations, rooms, guests); a channel manager distributes availability and rates to OTAs. Software like Hostlio Pro combines both in one platform.")]
    return article(next(p for p in POSTS if p["key"]=="post-pms"), c, faq)

def pages():
    import pages_v4
    return [home(), ai(), channel(), checkin(), features(), pricing(), faq_page(), about(), contact(), blog(), post_ai(), post_pms()] + pages_v4.pages(L, article) + __import__("legal_v5").pages(L, article)
