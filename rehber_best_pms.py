"""Takvim yazısı (15 Ekim 2026 planı): "Best PMS for small hotels in 2026: an honest comparison" — yalnız EN.
post-pms (EN, seçim kriterleri) ile rol ayrımı: bu yazı ürün karşılaştırması, o yazı kriterler; birbirine bağlanır.
Rakip bilgileri firmaların resmî sayfalarından, 10 Ekim 2026. Little Hotelier fiyat sayfası otomatik erişimi
engellediği için rakamı yazılmadı (yalnız model). RoomRaccoon rakamları 9 Ekim hesaplayıcısından.
Hostlio'nun yapmadıkları açıkça yazılır (POS/muhasebe yok, polis kaydı otomatik gönderilmez)."""
import html

SRC = [
 ("Cloudbeds: Pricing", "https://www.cloudbeds.com/pricing/"),
 ("Cloudbeds", "https://www.cloudbeds.com/"),
 ("Little Hotelier: Pricing", "https://www.littlehotelier.com/pricing/"),
 ("Mews: Pricing", "https://www.mews.com/en/pricing"),
 ("eviivo: Pricing", "https://eviivo.com/pricing/"),
 ("eviivo", "https://eviivo.com/"),
 ("Sirvoy: Pricing", "https://sirvoy.com/pricing"),
 ("Beds24: Pricing", "https://beds24.com/pricing.html"),
 ("RoomRaccoon: Pricing", "https://roomraccoon.com/pricing/"),
 ("WebRezPro: Pricing", "https://www.webrezpro.com/pricing/"),
 ("innRoad: Pricing", "https://www.innroad.com/pricing/"),
 ("ResNexus: Pricing", "https://www.resnexus.us/pricing"),
 ("ThinkReservations: Guest communications", "https://www.thinkreservations.com/products/guest-communications"),
]

def _tbl(head, rows):
    h = "".join(f'<th scope="col">{x}</th>' for x in head)
    b = "".join(("<tr class=\"hl\">" if r[0] == "Hostlio Pro" else "<tr>") + f'<th scope="row">{r[0]}</th>'
                + "".join(f"<td>{c}</td>" for c in r[1:]) + "</tr>" for r in rows)
    return f'<div class="table-wrap"><table class="cmp"><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table></div>'

META = {"en": dict(key="post-bestpms", date="2026-10-10", title="Best PMS for small hotels in 2026: an honest comparison",
                   desc="11 PMS for small hotels compared: published prices for 10 and 25 rooms, channel manager, guest messaging, mobile app and trials. Sourced, Oct 2026.")}

def en(U):
    from build import btn, SIGNUP_URL
    cta = btn("Try free for ⟦trial⟧ days", SIGNUP_URL) + btn("See plans", U("pricing"), "ghost")
    rows = [
      ("Hostlio Pro", "Published flat fee: ⟦price:starter⟧ / ⟦price:pro⟧ / ⟦price:growth⟧ a month", "Every plan", "WhatsApp AI assistant in every plan; OTA inboxes on Pro and Growth", "iOS and Android", "⟦trial⟧ days"),
      ("Cloudbeds", "Quote only", "Depends on plan", "Unified inbox incl. WhatsApp and OTAs; AI chatbot", "Included", "Not stated"),
      ("Little Hotelier", "Published by room tier; Basics plan adds a 1% booking fee", "Included", "Guest engagement tools", "Yes", "30 days; card required"),
      ("Mews", "Quote only (per room)", "Included in Mews Pro", "AI messaging via WhatsApp and SMS (Pro)", "iOS and Android", "Not stated"),
      ("eviivo", "From $50: $10 per bedroom a month; volume pricing above 10 rooms", "Included", "Unified inbox incl. WhatsApp; AI concierge is a paid add-on", "Included", "14 days"),
      ("Sirvoy", "Published by room tier (€, $ or £)", "Pro plan only", "Automated email; SMS paid per message", "Mobile web app", "14 days"),
      ("Beds24", "Pay as you go: €12.90 base + €2.60 per room", "Add-on: €0.55 per room type per channel", "Inbox for Airbnb and Booking.com; WhatsApp messages", "iOS and Android", "Free trial"),
      ("RoomRaccoon", "Published calculator, from €164 a month", "Built in (3 channels on Entry)", "Email templates; third-party apps", "iOS only", "14 days after a demo"),
      ("WebRezPro", "$10 per unit a month, minimum $100", "Via integrations (cost not stated)", "Not detailed", "Not verified", "Not stated"),
      ("innRoad", "Quote; “around $150 per month for most properties”", "Add-on", "Text messaging add-on", "Mobile-friendly web", "Not stated"),
      ("ResNexus", "Quote only", "Direct connect to Expedia, Booking.com, Airbnb", "Text messaging add-on", "Yes", "“Try risk-free”"),
      ("ThinkReservations", "Quote only", "Available (inclusion not stated)", "SMS with templates", "Staff app", "Not stated"),
    ]
    ex = [
      ("Hostlio Pro", "⟦price:starter⟧ (Starter)", "⟦price:pro⟧ (Pro)", "Channel manager and AI messaging included"),
      ("Sirvoy Pro", "€79", "€149", "Monthly billing; yearly billing is cheaper"),
      ("Beds24", "€43.85", "€86.15", "Assumes 3 and 5 room types on 3 channels"),
      ("eviivo", "$100", "Contact sales", "Volume pricing above 10 rooms; add-ons per room"),
      ("WebRezPro", "$100", "Up to $250", "Large-property discount on request"),
      ("RoomRaccoon Entry", "€164", "€228", "Calculator figures, 9 October 2026"),
    ]
    c = f'''<div class="answer"><p><strong>Short answer:</strong> there's no single best PMS for every small hotel. For 5–50 rooms, the ones worth shortlisting in 2026 are those that include a channel manager, let you message guests from one inbox and publish a price you can check before a sales call. Among vendors that publish prices, a 10-room property pays roughly 40 to 165 a month and a 25-room property roughly 85 to 250, in euros or dollars depending on the vendor. Cloudbeds, Mews, ResNexus and ThinkReservations only quote.</p></div>
<p class="small muted">Hostlio Pro is one of the products compared here, so we're not neutral. We only used facts from each vendor's own website, checked on 10 October 2026; customer counts are the vendors' own claims. Prices change and appear in different currencies (€, $, £) that we don't convert. Check each vendor's page before you decide.</p>
<h2>How we compared</h2>
<p>We looked at what matters most to an owner-run property of 5–50 rooms: what you'll actually pay each month, whether the <a href="{U("channel")}">channel manager</a> is included, how guest messages are handled, whether there's a mobile app and whether you can try it before you sign. For the selection criteria in more depth, see <a href="{U("post-pms")}">how to choose a PMS for a small hotel</a>.</p>
<h2>Comparison table</h2>
{_tbl(["PMS", "Pricing", "Channel manager", "Guest messaging", "Mobile app", "Free trial"], rows)}
<h2>What 10 and 25 rooms cost</h2>
<p>Monthly cost from published prices and each vendor's own calculator. Quote-only vendors are left out, and Little Hotelier is left out because we couldn't load its pricing page reliably. The products don't include the same things, so don't decide on price alone.</p>
{_tbl(["PMS", "10 rooms", "25 rooms", "Note"], ex)}
<h2>The PMS one by one</h2>
<h3>Hostlio Pro</h3>
<p>Built for independent hotels and guesthouses of 1–150 rooms. Every plan includes the PMS, a certified channel manager connected to 100+ OTAs, the room rack, a mobile app and Lio, an AI assistant that answers guests on WhatsApp in their language with your hotel's information. Pro and Growth add Booking.com, Airbnb and Expedia inboxes and <a href="{U("checkin")}">online check-in</a>. Prices are published and flat: no booking fees or revenue share. What it doesn't do: POS, accounting or payroll, and it doesn't submit guest data to police registration systems for you. See <a href="{U("ai")}">how Lio works</a>.</p>
<div class="cta-row" style="margin-top:12px">{cta}</div>
<h3>Cloudbeds</h3>
<p>A broad platform for independent properties of all sizes, with a unified inbox (WhatsApp, SMS, email and OTA messages) and an AI chatbot. Distribution is included in the One plan and optional or “bring your own” in others. Pricing is quote-only. It claims 20,000+ properties in 150+ countries. More detail: <a href="{U("vs-cloudbeds")}">Hostlio Pro vs Cloudbeds</a>.</p>
<h3>Little Hotelier</h3>
<p>SiteMinder's PMS for small properties; its pricing page says it specialises in properties with 1–30 rooms. The channel manager, booking engine and mobile app are included from the entry plan. Price depends on your room tier, and the Basics plan adds a 1% booking fee, so the cost rises with your bookings. No long-term contract.</p>
<h3>Mews</h3>
<p>A cloud hospitality platform used by a wide range of hotels; it claims 15,000+ hoteliers. Pricing is per room but quote-only, and payments are charged separately. Mews Pro includes distribution to a large channel network and AI messaging via WhatsApp and SMS.</p>
<h3>eviivo</h3>
<p>For hotels, B&amp;Bs and rentals. Its calculator shows $10 per bedroom a month with a $50 minimum, and volume pricing above 10 rooms. Channel manager and mobile app are included; the AI concierge and some tools are paid add-ons per room, and there's a small fee per confirmed booking for some services. 14-day free trial. Claims 28,000+ properties in 70 countries.</p>
<h3>Sirvoy</h3>
<p>Simple, affordable and transparent. Prices are published by room tier, with no contracts or setup fees and a 14-day trial. The catch: the channel manager is only in the Pro plan, and there's no native app (it's a mobile web app).</p>
<h3>Beds24</h3>
<p>Flexible and low-cost to start (from €15.50 a month for one room); you pay per room and per channel connection, so the price grows with your setup. It has an inbox for Airbnb and Booking.com messages, WhatsApp messaging and mobile apps. Popular with technically confident owners and rentals.</p>
<h3>RoomRaccoon</h3>
<p>An all-in-one system for B&amp;Bs and independent hotels with a built-in channel manager (limited channels on the entry plan). From €164 a month in its calculator, so it sits at the higher end for very small properties. The trial starts after a demo.</p>
<h3>WebRezPro, innRoad, ResNexus and ThinkReservations</h3>
<p>Four North American PMS for independent properties. WebRezPro publishes $10 per unit a month with a $100 minimum; innRoad says its core PMS is “around $150 per month for most properties”, with channel management and text messaging as add-ons; ResNexus and ThinkReservations quote on request. Check carefully what's included, since channel management and guest texting are often extra.</p>
<h2>Which one fits you?</h2>
<ul><li><strong>Under 10 rooms, owner-run:</strong> look for a flat fee with the channel manager included and a mobile app. Booking-fee models look cheap until high season.</li>
<li><strong>10–50 rooms with a small team:</strong> prioritise one inbox for guest messages, staff roles and reliable OTA sync. Compare the full yearly cost, including add-ons.</li>
<li><strong>Many outlets (restaurant, spa) or complex groups:</strong> broader platforms with POS and payments may be worth the quote process.</li></ul>
<p>Whatever you shortlist, run a free trial with your own rooms, rates and one OTA before you commit. You can estimate the time and commission you'd save with the <a href="{U("roi")}">ROI calculator</a>.</p>
'''
    lis = "".join(f'<li><a href="{u}" rel="nofollow noopener">{html.escape(n)}</a></li>' for n, u in SRC)
    c += f'<h2>Sources</h2><p class="small muted">All sources accessed 10 October 2026. Room-count prices for Sirvoy, Beds24, eviivo and RoomRaccoon come from the calculator on each vendor\'s official pricing page.</p><ul>{lis}</ul>'
    faq = [("What is the best PMS for a small hotel?", "It depends on your size and what you need included. For 5–50 rooms, shortlist a PMS that includes a channel manager, handles guest messages in one inbox, has a mobile app and publishes its price. Then test two or three with a free trial using your own rooms and rates."),
           ("How much does a PMS cost for a 10-room hotel?", "Among vendors that publish prices, roughly 40 to 165 a month in euros or dollars (10 October 2026), depending on whether the channel manager and messaging are included. Booking fees, add-ons and setup fees can add to that. Several well-known vendors only quote."),
           ("Do I need a separate channel manager?", "Not if your PMS includes one. Some include it in every plan, some only in higher plans, and some charge per channel connection. Check this before comparing prices."),
           ("Can I try Hostlio Pro for free?", "Yes, for ⟦trial⟧ days. You add a card at signup, but nothing is charged until the trial ends. Plans cost ⟦price:starter⟧, ⟦price:pro⟧ and ⟦price:growth⟧ a month, with the channel manager and the WhatsApp AI assistant in every plan.")]
    return c, faq

FN = {"en": en}
