"""ROI hesaplayıcı (rapor: güçlendirme önerileri). Varsayımların hepsi ziyaretçinin girdisidir; sitede
ölçülmüş bir "Lio şu kadar mesajı cevaplar" iddiası YOK — oran kullanıcının seçtiği değerdir."""
import json

T = {
 "en": dict(title="Hotel AI Messaging ROI Calculator | Hostlio Pro", desc="Estimate how many staff hours and how much money AI guest messaging could save your hotel each month. Enter your rooms, daily messages and staff cost.",
  h1="How much time could Lio save you?", lead="Enter a few numbers about your property. The calculator estimates the hours and staff cost that answering guest messages takes today, and how much of it you could hand to Lio.",
  f_rooms="Rooms", f_msgs="Guest messages per day", f_min="Minutes to answer one message", f_share="Share of messages you would let Lio answer", f_night="Share that arrives at night (22:00–08:00)", f_cost="Staff cost per hour (USD)",
  r_hours="Staff hours saved per month", r_cost="Staff cost saved per month", r_night="Night messages answered per month", r_plan="Suggested plan", r_net="Saving after the plan price",
  per_mo="/mo", msgs="messages", h="h", over="More than 150 rooms: contact us",
  note="Estimates only, based on the numbers you enter and 30 days a month. Your results depend on your guests, your settings and how many topics you let Lio answer automatically. Plan prices are early-bird monthly prices in USD.",
  cta="Try Hostlio Pro free for 7 days"),
 "tr": dict(title="Otel AI Mesajlaşma Tasarruf Hesaplayıcı | Hostlio Pro", desc="Yapay zekâ ile misafir mesajlaşmasının otelinize ayda kaç personel saati ve ne kadar maliyet kazandırabileceğini hesaplayın. Oda sayınızı, günlük mesajınızı ve personel maliyetinizi girin.",
  h1="Lio size ne kadar zaman kazandırır?", lead="Tesisinizle ilgili birkaç rakam girin. Hesaplayıcı, misafir mesajlarını cevaplamanın bugün kaç saat ve ne kadar personel maliyeti tuttuğunu ve bunun ne kadarını Lio’ya bırakabileceğinizi tahmin eder.",
  f_rooms="Oda sayısı", f_msgs="Günlük misafir mesajı", f_min="Bir mesajı cevaplama süresi (dakika)", f_share="Lio’ya bırakacağınız mesaj oranı", f_night="Gece gelen mesaj oranı (22:00–08:00)", f_cost="Saatlik personel maliyeti (USD)",
  r_hours="Ayda kazanılan personel saati", r_cost="Ayda tasarruf edilen personel maliyeti", r_night="Ayda cevaplanan gece mesajı", r_plan="Önerilen plan", r_net="Plan ücreti düşüldükten sonra kazanç",
  per_mo="/ay", msgs="mesaj", h="sa", over="150’den fazla oda: bize yazın",
  note="Yalnızca tahmindir; girdiğiniz rakamlara ve ayda 30 güne dayanır. Sonuçlar misafirlerinize, ayarlarınıza ve Lio’nun otomatik cevapladığı konulara göre değişir. Plan fiyatları ABD doları cinsinden erken kayıt aylık fiyatlarıdır.",
  cta="Hostlio Pro’yu 7 gün ücretsiz deneyin"),
 "es": dict(title="Calculadora de ROI de mensajería con IA para hoteles | Hostlio Pro", desc="Calcula cuántas horas de personal y cuánto dinero podría ahorrar tu hotel cada mes con la mensajería con IA. Introduce habitaciones, mensajes diarios y coste del personal.",
  h1="¿Cuánto tiempo podría ahorrarte Lio?", lead="Introduce algunos datos de tu alojamiento. La calculadora estima las horas y el coste de personal que hoy te lleva responder a los huéspedes, y cuánto podrías delegar en Lio.",
  f_rooms="Habitaciones", f_msgs="Mensajes de huéspedes al día", f_min="Minutos para responder un mensaje", f_share="Porcentaje de mensajes que dejarías a Lio", f_night="Porcentaje que llega de noche (22:00–08:00)", f_cost="Coste del personal por hora (USD)",
  r_hours="Horas de personal ahorradas al mes", r_cost="Coste de personal ahorrado al mes", r_night="Mensajes nocturnos respondidos al mes", r_plan="Plan recomendado", r_net="Ahorro tras el precio del plan",
  per_mo="/mes", msgs="mensajes", h="h", over="Más de 150 habitaciones: contáctanos",
  note="Solo son estimaciones, basadas en tus datos y en meses de 30 días. El resultado depende de tus huéspedes, tu configuración y los temas que dejes responder a Lio automáticamente. Los precios son mensuales de lanzamiento en USD.",
  cta="Prueba Hostlio Pro gratis 7 días"),
 "it": dict(title="Calcolatore ROI dei messaggi AI per hotel | Hostlio Pro", desc="Stima quante ore di personale e quanto denaro i messaggi AI con gli ospiti potrebbero far risparmiare al tuo hotel ogni mese. Inserisci camere, messaggi al giorno e costo del personale.",
  h1="Quanto tempo può farti risparmiare Lio?", lead="Inserisci qualche dato sulla tua struttura. Il calcolatore stima le ore e il costo del personale che oggi richiede rispondere agli ospiti, e quanto potresti affidarne a Lio.",
  f_rooms="Camere", f_msgs="Messaggi degli ospiti al giorno", f_min="Minuti per rispondere a un messaggio", f_share="Quota di messaggi che lasceresti a Lio", f_night="Quota che arriva di notte (22:00–08:00)", f_cost="Costo orario del personale (USD)",
  r_hours="Ore di personale risparmiate al mese", r_cost="Costo del personale risparmiato al mese", r_night="Messaggi notturni gestiti al mese", r_plan="Piano consigliato", r_net="Risparmio al netto del piano",
  per_mo="/mese", msgs="messaggi", h="h", over="Oltre 150 camere: contattaci",
  note="Solo stime, basate sui dati inseriti e su mesi di 30 giorni. I risultati dipendono dai tuoi ospiti, dalle impostazioni e dagli argomenti a cui lasci rispondere Lio in automatico. Prezzi mensili early bird in USD.",
  cta="Prova Hostlio Pro gratis per 7 giorni"),
 "pt": dict(title="Calculadora de ROI de mensagens com IA para hotéis | Hostlio Pro", desc="Estime quantas horas de equipe e quanto dinheiro as mensagens com IA podem economizar no seu hotel por mês. Informe quartos, mensagens por dia e custo da equipe.",
  h1="Quanto tempo a Lio pode economizar para você?", lead="Informe alguns números da sua propriedade. A calculadora estima as horas e o custo de equipe que responder hóspedes exige hoje, e quanto disso você poderia passar para a Lio.",
  f_rooms="Quartos", f_msgs="Mensagens de hóspedes por dia", f_min="Minutos para responder uma mensagem", f_share="Parcela de mensagens que você deixaria com a Lio", f_night="Parcela que chega à noite (22:00–08:00)", f_cost="Custo da equipe por hora (USD)",
  r_hours="Horas de equipe economizadas por mês", r_cost="Custo de equipe economizado por mês", r_night="Mensagens noturnas respondidas por mês", r_plan="Plano sugerido", r_net="Economia após o preço do plano",
  per_mo="/mês", msgs="mensagens", h="h", over="Mais de 150 quartos: fale conosco",
  note="São apenas estimativas, com base nos números informados e em meses de 30 dias. O resultado depende dos seus hóspedes, das configurações e dos assuntos que você deixa a Lio responder sozinha. Preços mensais early bird em USD.",
  cta="Teste o Hostlio Pro grátis por 7 dias"),
 "fr": dict(title="Calculateur de ROI de la messagerie IA pour hôtels | Hostlio Pro", desc="Estimez combien d’heures de personnel et d’argent la messagerie IA pourrait faire gagner à votre hôtel chaque mois. Saisissez vos chambres, vos messages par jour et le coût du personnel.",
  h1="Combien de temps Lio peut-il vous faire gagner ?", lead="Saisissez quelques chiffres sur votre établissement. Le calculateur estime les heures et le coût de personnel que demandent aujourd’hui les réponses aux clients, et la part que vous pourriez confier à Lio.",
  f_rooms="Chambres", f_msgs="Messages clients par jour", f_min="Minutes pour répondre à un message", f_share="Part des messages confiée à Lio", f_night="Part reçue la nuit (22 h – 8 h)", f_cost="Coût horaire du personnel (USD)",
  r_hours="Heures de personnel gagnées par mois", r_cost="Coût de personnel économisé par mois", r_night="Messages de nuit traités par mois", r_plan="Forfait conseillé", r_net="Économie après le prix du forfait",
  per_mo="/mois", msgs="messages", h="h", over="Plus de 150 chambres : contactez-nous",
  note="Il s’agit d’estimations fondées sur vos chiffres et sur des mois de 30 jours. Le résultat dépend de vos clients, de vos réglages et des sujets auxquels vous laissez Lio répondre automatiquement. Prix mensuels early bird en USD.",
  cta="Essayez Hostlio Pro gratuitement pendant 7 jours"),
}

def roi_page(L, build):
    t = T[L]; url = build.url
    plans = [{"id": p["id"], "name": p["name"], "price": p["price"], "rooms": {"starter": 10, "pro": 50, "growth": 150}[p["id"]]} for p in build.PLANS]
    def field(k, name, val, mn, mx, step, suffix=""):
        return (f'<label class="co-field roi-f"><span>{t[k]}</span><span class="roi-in"><input type="number" name="{name}" value="{val}" min="{mn}" max="{mx}" step="{step}" inputmode="decimal">'
                + (f'<span class="roi-suf">{suffix}</span>' if suffix else "") + '</span></label>')
    form = (field("f_rooms", "rooms", 20, 1, 500, 1) + field("f_msgs", "msgs", 40, 0, 2000, 1) + field("f_min", "min", 4, 0.5, 60, 0.5)
            + field("f_share", "share", 50, 0, 100, 5, "%") + field("f_night", "night", 30, 0, 100, 5, "%") + field("f_cost", "cost", 15, 0, 500, 1, "$"))
    res = "".join(f'<div class="roi-r"><span>{t[k]}</span><b id="roi-{i}">–</b></div>' for k, i in [("r_hours", "hours"), ("r_cost", "cost"), ("r_night", "night"), ("r_plan", "plan"), ("r_net", "net")])
    cfg = json.dumps({"plans": plans, "per_mo": t["per_mo"], "msgs": t["msgs"], "h": t["h"], "over": t["over"],
                      "locale": {"tr": "tr-TR", "en": "en-US", "es": "es-ES", "it": "it-IT", "pt": "pt-BR", "fr": "fr-FR"}[L]}, ensure_ascii=False)
    body = f'''<section class="page-hero"><div class="wrap"><h1>{t["h1"]}</h1><p class="lead">{t["lead"]}</p></div></section>
<section style="padding-top:0"><div class="wrap roi">
<form class="roi-form" id="roi-form" onsubmit="return false">{form}</form>
<div class="roi-out on-dark" aria-live="polite">{res}<div class="cta-row" style="margin-top:18px">{build.btn(t["cta"], build.SIGNUP_URL)}</div></div>
</div><div class="wrap"><p class="small muted" style="margin-top:16px;max-width:70ch">{t["note"]}</p></div></section>
<script>(function(){{var C={cfg},f=document.getElementById('roi-form');if(!f)return;
var nf=function(n,d){{return n.toLocaleString(C.locale,{{maximumFractionDigits:d||0}})}},$=function(n){{return '$'+nf(Math.round(n))}};
function v(n){{var x=parseFloat(f.elements[n].value);return isFinite(x)&&x>=0?x:0}}
function calc(){{var rooms=v('rooms'),m=v('msgs')*30,share=Math.min(v('share'),100)/100,night=Math.min(v('night'),100)/100;
var hrs=m*share*v('min')/60,cost=hrs*v('cost'),p=null;for(var i=0;i<C.plans.length;i++){{if(rooms<=C.plans[i].rooms){{p=C.plans[i];break}}}}
document.getElementById('roi-hours').textContent=nf(hrs,1)+' '+C.h;document.getElementById('roi-cost').textContent=$(cost)+C.per_mo;
document.getElementById('roi-night').textContent=nf(Math.round(m*share*night))+' '+C.msgs;
document.getElementById('roi-plan').textContent=p?p.name+' · $'+p.price+C.per_mo:C.over;
document.getElementById('roi-net').textContent=p?$(cost-p.price)+C.per_mo:'–'}}
f.addEventListener('input',calc);calc()}})();</script>'''
    return {"key": "roi", "title": t["title"], "desc": t["desc"], "trail": [(t["h1"], url("roi", L))], "body": body}
