"""'PMS seçimi' (post-pms) — EN ana metin genişletmesi + PT/FR uyarlamaları (pms_secim_<dil>.py), 12 Ekim 2026.
EN 375, PT 429, FR 487 kelimeydi (FR 165 gösterim, 19. sıra). Rol: seçim KRİTERLERİ; ürün karşılaştırması post-bestpms (EN).
Rakip rakamları 10 Ekim resmî sayfalar (Sirvoy, Beds24, eviivo). Hostlio'nun yapmadıkları açık."""
import importlib

def en(U):
    from build import btn, SIGNUP_URL
    cta = btn("Try free for ⟦trial⟧ days", SIGNUP_URL) + btn("See plans", U("pricing"), "ghost")
    c = f'''<div class="answer"><p><strong>Short answer:</strong> the right PMS for a small hotel includes a channel manager, has a published and predictable price, brings guest messages into one inbox, works on your phone, tells you clearly how it handles your country's guest registration and invoicing rules, and can be set up the same day. Enterprise systems with hundreds of modules often go unused at a 10–30 room property and cost more than they return.</p></div>
<h2>What a PMS actually does</h2>
<p>A property management system (PMS) puts the day-to-day running of the hotel on one screen: the reservation calendar and room rack, check-in and check-out, room status and housekeeping, guest records, extras, invoices and reports. For a small property the real gain is that this work stops being spread across spreadsheets, a notebook, several OTA extranets and the WhatsApp on someone's phone. A booking from one channel closes the room on the others, and the screen you open in the morning shows what needs doing today. How it differs from a channel manager is explained in <a href="{U("post-pms-vs-cm")}">PMS vs channel manager</a>.</p>
<h2>1. A built-in channel manager</h2>
<p>If you sell on Booking.com, Airbnb and Expedia at the same time, availability has to sync instantly. A separate channel manager means another bill, another screen and another place where room mappings can go wrong. Ask: is the channel manager included in every plan, or only in a higher plan or as an add-on? How many channels does it connect to, and are the connections two-way? Can you set rates, minimum stay and stop-sell for a date range in one go?</p>
<h2>2. Pricing model and full yearly cost</h2>
<p>Hotel software is priced in four ways: a flat monthly fee, a fee per room or room band, a percentage or fee per booking, or a one-off licence. Percentage models get more expensive exactly when you are busiest; licences need updates, hosting and support priced separately. Vendors who don't publish prices usually mean a sales process. Compare the full yearly cost, including setup, add-ons, tax and currency, not just the headline monthly figure.</p>
<div class="table-wrap"><table><thead><tr><th>Property</th><th>Hostlio Pro</th><th>Sirvoy (Pro)</th><th>Beds24</th><th>eviivo</th></tr></thead><tbody>
<tr><td>10 rooms</td><td>⟦price:starter⟧ a month (Starter)</td><td>€79 a month</td><td>€43.85 a month</td><td>$100 a month</td></tr>
<tr><td>25 rooms</td><td>⟦price:pro⟧ a month (Pro)</td><td>€149 a month</td><td>€86.15 a month</td><td>Contact sales</td></tr></tbody></table></div>
<p class="small muted">From each vendor's official pricing page or calculator, 10 October 2026. Beds24 assumes 3 and 5 room types on 3 channels. What each plan includes differs; see the sourced comparison in <a href="{U("post-bestpms")}">best PMS for small hotels</a>.</p>
<h2>3. Guest messaging</h2>
<p>At a small property the biggest time sink is answering the same questions on different channels: check-in times, parking, breakfast, transfers. When messages are scattered across WhatsApp, Booking.com, Airbnb and email, replies get slower and review scores suffer. Ask: are WhatsApp and OTA messages in one inbox? Is there an automatic reply that uses your own hotel information, in the guest's language? Are prices, discounts and complaints left to you? More in <a href="{U("post-ai")}">answering guest messages with AI</a>.</p>
<h2>4. A room rack you will actually use</h2>
<p>The reservation calendar is the screen your front desk looks at most. Drag-and-drop room moves, seeing each booking's channel at a glance and a warning when two bookings clash make daily work faster. A morning view of who arrives, who leaves and which rooms to clean saves a small team real time.</p>
<h2>5. Mobile access</h2>
<p>Owners of small properties are often away from the desk. An iOS and Android app with notifications, where you can open a booking and reply to a guest, is a real need. Ask: is the app included in every plan, and what can you do on the phone versus only on a computer?</p>
<h2>6. Your country's rules: guest registration and invoicing</h2>
<p>Most countries require hotels to register guests with the authorities, and many have their own invoicing and tourist-tax rules. Ask plainly what the software does: does it submit guest data to the official system for you, or only export a file? Does it issue invoices in your country's format, or does that stay with your accounting software? Software that can't answer clearly will create manual work later. Online check-in helps either way, because guest details arrive before the guest does.</p>
<h2>7. Setup, migration and support</h2>
<p>A small hotel can't absorb a weeks-long implementation. With good software the account is ready the same day, rooms and rates go in, and channels are often connected the same day. When switching, check that future reservations can be imported from Excel or CSV and that support answers in a language your team uses.</p>
<h2>What to test during the free trial</h2>
<ol><li>Enter your own rooms, room types and rate plans.</li>
<li>Import your future reservations and check dates, rooms and amounts.</li>
<li>Connect one OTA, change one day's rate and confirm it appears in the extranet.</li>
<li>Try a real guest question (parking, late arrival) in the inbox.</li>
<li>Open a booking on your phone and move it to another room.</li>
<li>Look at a month-end report and the net revenue per channel.</li></ol>
<h2>Checklist</h2>
<div class="table-wrap"><table><thead><tr><th>Criterion</th><th>Question to ask</th></tr></thead><tbody>
<tr><td>Channel manager</td><td>Included in every plan? How many channels, two-way?</td></tr><tr><td>Pricing</td><td>Flat or per booking? Published? What is the full yearly cost?</td></tr>
<tr><td>Messaging</td><td>WhatsApp and OTA messages in one place, with automatic replies?</td></tr><tr><td>Room rack</td><td>Drag and drop, clash warnings, a daily view?</td></tr>
<tr><td>Mobile</td><td>iOS and Android app in every plan?</td></tr><tr><td>Local rules</td><td>Guest registration and invoicing: automatic, export or not at all?</td></tr>
<tr><td>Check-in</td><td>Online check-in with digital signature?</td></tr><tr><td>Migration</td><td>Reservation import from Excel or CSV?</td></tr>
<tr><td>Trial</td><td>Free trial and cancellation without commitment?</td></tr></tbody></table></div>
<h2>Where Hostlio Pro fits</h2>
<p>Hostlio Pro is built for independent hotels and guesthouses of 1–150 rooms. Every plan includes the channel manager (certified connections to 100+ OTAs), the room rack, the iOS and Android app and Lio, an AI assistant that answers guests on WhatsApp in their language; Pro and Growth add the OTA inboxes and online check-in. The price is published and flat: Starter ⟦price:starter⟧, Pro ⟦price:pro⟧, Growth ⟦price:growth⟧ a month, with no booking fees. Reservations can be imported from Excel or CSV. To be clear about what it doesn't do: it doesn't submit guest data to police registration systems, doesn't issue country-specific invoices, and has no POS, accounting or booking engine. If those are essential for you, a broader suite may fit better. See all <a href="{U("features")}">features</a>.</p>
<div class="cta-row" style="margin-top:12px">{cta}</div>'''
    faq = [("Does a small hotel need a PMS?", "If you sell on several OTAs and get dozens of messages a day, yes. Working with spreadsheets and separate OTA extranets raises the risk of overbookings and slow replies."),
           ("What's the difference between a PMS and a channel manager?", "A PMS runs the hotel's internal operations (reservations, rooms, guests); a channel manager distributes availability and rates to OTAs. Software like Hostlio Pro combines both in one place."),
           ("How much does a PMS cost for a small hotel?", "Among vendors that publish prices, a 10-room property pays roughly 40 to 165 a month in euros or dollars (October 2026). Booking fees, add-ons and setup costs can add to that; compare the full yearly cost."),
           ("Does the PMS handle guest registration with the police?", "It depends on the software and the country. Some submit data directly, others export a file. Hostlio Pro collects guest details with online check-in but does not submit them to official systems."),
           ("Is switching from my current software difficult?", "Export your future reservations to Excel or CSV and import them into the new system. Plan the moment you switch channels so availability is sent from one system only.")]
    return c, faq

def get(L, U):
    if L == "en": return en(U)
    return importlib.import_module("pms_secim_" + L).body(U)
