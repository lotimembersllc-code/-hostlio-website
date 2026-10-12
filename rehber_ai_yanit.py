"""'AI ile misafir mesajlarını yanıtlamak' (post-ai) — 6 dilde genişletilmiş gövde (12 Ekim 2026).
Neden: EN sürümü 'Tarandı – dizine eklenmedi' (358 kelime; AI Front Desk rehberiyle çakışma). Açı: pratik — 10 örnek soru,
bilgi tabanı, kurulum, WhatsApp/OTA farkı, ölçüm, hatalar. Ürün iddiaları yalnız canlı özellikler (AI sayfası + llms.txt):
30+ dil, WhatsApp her planda, OTA gelen kutuları Pro/Growth, onay modu, devretme, eksik bilgi uyarısı, Lio'yu dene,
kota %80/%100/~%110. Lio rezervasyonu kendisi ONAYLAMAZ. Diller: en (burada), tr, es, it, pt, fr (ai_yanit_<dil>.py)."""
import importlib

def en(U):
    c = f'''<div class="answer"><p><strong>Short answer:</strong> most messages a hotel receives are the same dozen questions: check-in times, parking, breakfast, transfers, luggage, Wi-Fi. An AI assistant that only uses your hotel's own information can answer them in seconds, in the guest's language, at any hour. Decisions stay with you: discounts, complaints, refunds, exceptions and anything you are not sure about. Start in approval mode, fill the gaps the assistant flags, then let it answer information questions on its own.</p></div>
<h2>What guests actually ask</h2>
<p>At independent hotels and guesthouses the same topics come back every day, on WhatsApp and in the Booking.com, Airbnb and Expedia inboxes. Before arrival guests ask about getting there and arrival times; during the stay about breakfast, Wi-Fi and the area; after check-out about invoices and lost items. The answers already exist at your property. What goes wrong is timing and language: a question sent at 23:40 in German waits until morning, and the guest books a taxi you could have sold them.</p>
<h2>10 typical messages and how AI should handle them</h2>
<div class="table-wrap"><table><thead><tr><th>Guest message</th><th>Good AI handling</th></tr></thead><tbody>
<tr><td>"We land at 23:00, can we still check in?"</td><td>Answer with your late check-in rule and how to get the key; offer the airport transfer if you have one.</td></tr>
<tr><td>"Is there parking?"</td><td>Free or paid, on site or nearby, price and whether to reserve.</td></tr>
<tr><td>"What time is breakfast?"</td><td>Hours, where it is served, and whether it is included in their rate.</td></tr>
<tr><td>"Can we leave our bags after check-out?"</td><td>Yes or no, until what time, any fee.</td></tr>
<tr><td>"Do you allow dogs?"</td><td>Your pet policy, size limits and any extra charge.</td></tr>
<tr><td>"How do we get from the airport?"</td><td>Distance, taxi time and price range, public transport, your transfer offer.</td></tr>
<tr><td>"Can we check in early?"</td><td>Explain the rule; if it depends on availability or a fee, hand it to staff to confirm.</td></tr>
<tr><td>"Can you give us a better price?"</td><td>Hand to staff. Discounts are a decision, not information.</td></tr>
<tr><td>"The air conditioning doesn't work."</td><td>Acknowledge, tell the guest the team has been alerted, and hand it to staff immediately.</td></tr>
<tr><td>"Please send the invoice to our company."</td><td>Collect the company details if your process allows, then hand to staff.</td></tr>
</tbody></table></div>
<p>The pattern is simple: if the answer is a fact you have written down, the assistant replies; if it needs a decision, money or empathy, a person does.</p>
<h2>What the assistant needs to know</h2>
<p>An AI assistant is only as good as the information behind it. Before switching it on, write down:</p>
<ul><li>Check-in and check-out times, early arrival and late departure rules</li>
<li>How late arrivals get in (reception hours, key box, door code process)</li>
<li>Parking, breakfast, Wi-Fi, pets, smoking, children and extra beds</li>
<li>Airport and station distances, taxi times, your transfer prices</li>
<li>Room types and what is in each room</li>
<li>Cancellation and payment rules as stated in your terms</li>
<li>Nearby restaurants, beaches, sights and pharmacies</li>
<li>Extras you sell: transfers, tours, late check-out</li></ul>
<p>Write it the way you would explain it to a new receptionist. Short, concrete sentences work better than marketing copy.</p>
<h2>Setting it up in five steps</h2>
<ol><li><strong>Fill in your hotel information.</strong> Use the list above; leave nothing as "ask reception".</li>
<li><strong>Bring your channels into one inbox.</strong> WhatsApp plus the OTA inboxes you use, so every conversation is matched to its reservation.</li>
<li><strong>Start in approval mode.</strong> For the first days, read each reply before it is sent and correct the wording where needed.</li>
<li><strong>Set handover rules.</strong> Decide which topics always come to you: discounts, complaints, refunds, group requests, anything medical or about safety.</li>
<li><strong>Let it answer on its own.</strong> Once replies are consistent, let the assistant close information questions automatically and keep the drafts for the topics you chose.</li></ol>
<h2>WhatsApp and OTA inboxes are not the same</h2>
<p>On WhatsApp you talk to the guest directly, and you can share links, phone numbers and your own website. WhatsApp also has its own rules: a business can reply freely within 24 hours of the guest's last message, and outside that window it needs an approved message template. OTA inboxes such as Booking.com and Airbnb have their own rules about what you may share, and booking platforms generally expect communication about a booking to stay on the platform. A good assistant adapts its answer to the channel. Our <a href="{U("post-whatsapp")}">WhatsApp for hotels guide</a> covers the WhatsApp side in detail, and the <a href="{U("post-autoreply")}">Booking.com auto-reply guide</a> has ready-made templates.</p>
<h2>Replying in the guest's language</h2>
<p>Guests who can write in their own language ask more precisely and trust the answer more. An assistant that replies in 30+ languages means a Japanese or Polish guest gets the same quality of answer as an English one, even when nobody at reception speaks the language. You should still be able to read every conversation in your own language, so you always know what was promised.</p>
<h2>How to tell if it is working</h2>
<ul><li><strong>Response time:</strong> how long guests wait for a first answer, especially at night.</li>
<li><strong>Share answered automatically:</strong> how many conversations closed without staff.</li>
<li><strong>Handovers:</strong> which topics still come to you, and whether some could be answered with better information.</li>
<li><strong>Missing information:</strong> questions the assistant could not answer point to gaps in your setup.</li>
<li><strong>Extras sold:</strong> transfers and tours offered at the right moment.</li></ul>
<h2>Common mistakes</h2>
<ul><li><strong>Vague hotel information.</strong> "Breakfast is available" leads to vague answers; "07:30–10:30 in the garden, included in all rates" doesn't.</li>
<li><strong>Letting AI negotiate.</strong> Prices, discounts and compensation belong to you.</li>
<li><strong>Skipping approval mode.</strong> A few days of reading drafts catches wording you would not use.</li>
<li><strong>Two systems.</strong> If WhatsApp lives on one phone and OTA messages in another tab, nobody sees the whole picture.</li>
<li><strong>Never reviewing.</strong> Check the handovers once a week and add what was missing.</li></ul>
<h2>How it works in Hostlio Pro</h2>
<p>Hostlio Pro's assistant, <a href="{U("ai")}">Lio</a>, replies to guests on WhatsApp in every plan, and in the Booking.com, Airbnb and Expedia inboxes on Pro and Growth. It uses only your hotel information and the guest's reservation, answers in the guest's language (30+ languages) and shows you a translation of its reply in yours; replies you type yourself are sent exactly as written. You choose which topics it closes on its own and which it hands to you, and during the first days you can approve every reply. If it cannot answer a question, it flags the missing information in your setup. During setup you can try Lio with your own questions before going live. Lio never confirms a booking on its own: on Pro and Growth it collects booking requests and you approve them. Plans include ⟦quota:starter⟧ to ⟦quota:growth⟧ AI messages a month; you are warned at 80% and 100%, and automatic replies pause at about 110%.</p>
<p>For the bigger picture of what AI can do at the front desk, read the <a href="{U("post-aifrontdesk")}">AI front desk guide</a>.</p>'''
    faq = [("Can AI give guests wrong information?", "The risk is small when the assistant only uses information the hotel provides and hands uncertain questions to staff. Start in approval mode, and fill in the gaps it flags."),
           ("Which messages should stay with a person?", "Discounts and price negotiation, complaints and compensation, refunds, group and event requests, and anything medical or about safety."),
           ("Will guests know they're talking to AI?", "Replies are written in the hotel's name and tone. For transparency, you can mention in your welcome message that an AI assistant answers outside reception hours."),
           ("Does it work with Booking.com and Airbnb messages?", "In Hostlio Pro, yes, on the Pro and Growth plans. WhatsApp is included in every plan."),
           ("How much does it cost?", "Lio is included in every Hostlio Pro plan: Starter ⟦price:starter⟧, Pro ⟦price:pro⟧ and Growth ⟦price:growth⟧ a month, with ⟦quota:starter⟧ to ⟦quota:growth⟧ AI messages a month.")]
    return c, faq

def get(L, U):
    """L için gövde + SSS. en burada; diğer diller ai_yanit_<L>.py modülünden."""
    if L == "en": return en(U)
    return importlib.import_module("ai_yanit_" + L).body(U)
