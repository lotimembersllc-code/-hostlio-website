"""Ödeme / kayıt sayfası — /xx/signup/ (6 dil, statik metin o dilde) ve /signup/ (dil algılayan).

Mantık: src/assets/signup.js (signup-checkout çağrısı, ülke → para birimi → saat dilimi
tablosu, oda limiti, attribution, ?checkout= dönüşü, sunucu hata kodlarının çevirisi).
Fiyatlar: pricing.py (tek kaynak) → prices.js; sayfa açılınca canlı `plans` ucundan tazelenir,
early_bird=false gelirse Early Bird metni gizlenir ve normal fiyat gösterilir (Y2).
Satır içi betik ve on* özniteliği YOK (O4 CSP). Alanlar gerçek bir <form> içinde (O8).
⛔ Element id'leri (firstName, email, plan-starter …, error-msg, submit-btn) korunuyor.
Dil (/signup/): ?lang= → localStorage 'hostlio_lang' → yönlendiren sayfanın dili → tarayıcı → en.
"""
import json, html
from pathlib import Path
import pricing

LANGS = ["en", "tr", "es", "it", "pt", "fr"]

S = {
 "en": dict(
  kicker="7-day free trial", h="Start your Hostlio Pro trial", sub="Create your account in minutes and connect your channels the same day.",
  your_plan="Your plan", card_note="Your card is collected at signup. Nothing is charged until your 7-day trial ends, and you can cancel anytime before then.",
  secure="Secure payment by Stripe", t1="Used by independent hotels in 20+ countries", t2="Account ready in minutes, channels connected the same day", t3="No long-term contract",
  eb="Early-bird price for the first 50 customers, locked in while you stay subscribed.",
  form_h="Create your account", form_p="Fill in your details, then you’ll continue to secure payment.",
  choose="Choose your plan", monthly="Monthly", annual="Annual", save="Save 20%", mo="/mo", mo_ann="/mo, billed annually", regular="Regularly",
  first="First name", last="Last name", email="Email address", hotel="Hotel name", rooms="Number of rooms", phone="Phone (optional)",
  country="Country", select_country="Select your country…", other="Other / not listed…", other_ph="2-letter country code (e.g. IS)",
  currency="Guest currency", currency_hint="What your guests pay in — not your Hostlio Pro subscription (billed in USD). Must match the currency you use on Booking.com and other channels. This can’t be changed later.",
  tz="Time zone", tz_hint="Used to send your daily summary at 08:00 local time.",
  terms='By signing up you agree to our <a href="{t}">Terms of Service</a> and <a href="{p}">Privacy Policy</a>.',
  submit="Continue to secure payment", starting="Starting checkout…", back="Back to home", login="Already have an account?", login_a="Log in",
  e_required="Please fill in all required fields.", e_code="Please enter a valid 2-letter country code (e.g. IS).", e_country="Please select your country.",
  e_currency="Please select the currency your guests pay in.", e_tz="Please select your time zone.", e_email="Please enter a valid email address.",
  r_starter="Starter supports up to 10 rooms. Please choose Pro or Growth.", r_pro="Pro supports up to 50 rooms. Please choose Growth.", r_growth="Growth supports up to 150 rooms. Contact us for larger properties.",
  e_checkout="Sorry, we couldn’t start checkout. Please try again.", e_network="Network error. Please check your connection and try again.",
  ok_paid="Payment received. Check your email to set your password and finish setup.", cancelled="Checkout cancelled. You can try again whenever you’re ready.",
  lang="Language"),
 "tr": dict(
  kicker="7 gün ücretsiz deneme", h="Hostlio Pro denemenizi başlatın", sub="Hesabınızı dakikalar içinde oluşturun, kanallarınızı aynı gün bağlayın.",
  your_plan="Planınız", card_note="Kartınız kayıt sırasında alınır. 7 günlük deneme bitene kadar ücret çekilmez; bu süre içinde istediğiniz zaman iptal edebilirsiniz.",
  secure="Stripe ile güvenli ödeme", t1="20+ ülkede bağımsız oteller kullanıyor", t2="Hesap dakikalar içinde hazır, kanallar aynı gün bağlı", t3="Uzun süreli sözleşme yok",
  eb="İlk 50 müşteriye özel erken kayıt fiyatı, abonelik boyunca sabit.",
  form_h="Hesabınızı oluşturun", form_p="Bilgilerinizi girin, ardından güvenli ödeme adımına geçin.",
  choose="Planınızı seçin", monthly="Aylık", annual="Yıllık", save="%20 tasarruf", mo="/ay", mo_ann="/ay, yıllık faturalandırılır", regular="Normal fiyat",
  first="Ad", last="Soyad", email="E-posta adresi", hotel="Otel adı", rooms="Oda sayısı", phone="Telefon (isteğe bağlı)",
  country="Ülke", select_country="Ülkenizi seçin…", other="Diğer / listede yok…", other_ph="2 harfli ülke kodu (ör. IS)",
  currency="Misafir para birimi", currency_hint="Misafirlerinizin ödediği para birimi — Hostlio Pro aboneliğiniz değil (USD faturalandırılır). Booking.com ve diğer kanallarda kullandığınız para birimiyle aynı olmalı. Sonradan değiştirilemez.",
  tz="Saat dilimi", tz_hint="Günlük özetinizi yerel saatle 08:00'de göndermek için kullanılır.",
  terms='Kaydolarak <a href="{t}">Kullanım Şartları</a> ve <a href="{p}">Gizlilik Politikası</a>’nı kabul etmiş olursunuz.',
  submit="Güvenli ödemeye devam et", starting="Ödeme başlatılıyor…", back="Ana sayfaya dön", login="Hesabınız var mı?", login_a="Giriş yapın",
  e_required="Lütfen tüm zorunlu alanları doldurun.", e_code="Lütfen geçerli 2 harfli bir ülke kodu girin (ör. IS).", e_country="Lütfen ülkenizi seçin.",
  e_currency="Lütfen misafirlerinizin ödediği para birimini seçin.", e_tz="Lütfen saat diliminizi seçin.", e_email="Lütfen geçerli bir e-posta adresi girin.",
  r_starter="Starter en fazla 10 odayı destekler. Lütfen Pro veya Growth seçin.", r_pro="Pro en fazla 50 odayı destekler. Lütfen Growth seçin.", r_growth="Growth en fazla 150 odayı destekler. Daha büyük tesisler için bize yazın.",
  e_checkout="Ödeme başlatılamadı. Lütfen tekrar deneyin.", e_network="Bağlantı hatası. İnternet bağlantınızı kontrol edip tekrar deneyin.",
  ok_paid="Ödeme alındı. Şifrenizi belirleyip kurulumu tamamlamak için e-postanızı kontrol edin.", cancelled="Ödeme iptal edildi. Hazır olduğunuzda tekrar deneyebilirsiniz.",
  lang="Dil"),
 "es": dict(
  kicker="Prueba gratis de 7 días", h="Empieza tu prueba de Hostlio Pro", sub="Crea tu cuenta en minutos y conecta tus canales el mismo día.",
  your_plan="Tu plan", card_note="Tu tarjeta se registra al darte de alta. No se cobra nada hasta que terminen los 7 días de prueba y puedes cancelar antes cuando quieras.",
  secure="Pago seguro con Stripe", t1="Lo usan hoteles independientes en más de 20 países", t2="Cuenta lista en minutos, canales conectados el mismo día", t3="Sin permanencia",
  eb="Precio de lanzamiento para los primeros 50 clientes, fijo mientras sigas suscrito.",
  form_h="Crea tu cuenta", form_p="Completa tus datos y continúa al pago seguro.",
  choose="Elige tu plan", monthly="Mensual", annual="Anual", save="Ahorra 20 %", mo="/mes", mo_ann="/mes, facturado anualmente", regular="Precio habitual",
  first="Nombre", last="Apellidos", email="Correo electrónico", hotel="Nombre del hotel", rooms="Número de habitaciones", phone="Teléfono (opcional)",
  country="País", select_country="Selecciona tu país…", other="Otro / no aparece…", other_ph="Código de país de 2 letras (p. ej. IS)",
  currency="Moneda de los huéspedes", currency_hint="La moneda en la que pagan tus huéspedes, no tu suscripción a Hostlio Pro (facturada en USD). Debe coincidir con la moneda que usas en Booking.com y otros canales. No se puede cambiar después.",
  tz="Zona horaria", tz_hint="Se usa para enviarte el resumen diario a las 08:00 hora local.",
  terms='Al registrarte aceptas nuestros <a href="{t}">Términos del servicio</a> y la <a href="{p}">Política de privacidad</a>.',
  submit="Continuar al pago seguro", starting="Iniciando el pago…", back="Volver al inicio", login="¿Ya tienes cuenta?", login_a="Inicia sesión",
  e_required="Completa todos los campos obligatorios.", e_code="Introduce un código de país válido de 2 letras (p. ej. IS).", e_country="Selecciona tu país.",
  e_currency="Selecciona la moneda en la que pagan tus huéspedes.", e_tz="Selecciona tu zona horaria.", e_email="Introduce un correo electrónico válido.",
  r_starter="Starter admite hasta 10 habitaciones. Elige Pro o Growth.", r_pro="Pro admite hasta 50 habitaciones. Elige Growth.", r_growth="Growth admite hasta 150 habitaciones. Escríbenos para alojamientos más grandes.",
  e_checkout="No hemos podido iniciar el pago. Inténtalo de nuevo.", e_network="Error de conexión. Revisa tu conexión e inténtalo de nuevo.",
  ok_paid="Pago recibido. Revisa tu correo para crear tu contraseña y terminar la configuración.", cancelled="Pago cancelado. Puedes volver a intentarlo cuando quieras.",
  lang="Idioma"),
 "it": dict(
  kicker="Prova gratuita di 7 giorni", h="Inizia la prova di Hostlio Pro", sub="Crea il tuo account in pochi minuti e collega i canali in giornata.",
  your_plan="Il tuo piano", card_note="La carta viene registrata all’iscrizione. Non viene addebitato nulla fino alla fine dei 7 giorni di prova e puoi disdire in qualsiasi momento prima.",
  secure="Pagamento sicuro con Stripe", t1="Usato da hotel indipendenti in oltre 20 paesi", t2="Account pronto in pochi minuti, canali collegati in giornata", t3="Nessun vincolo a lungo termine",
  eb="Prezzo di lancio per i primi 50 clienti, bloccato finché resti abbonato.",
  form_h="Crea il tuo account", form_p="Inserisci i tuoi dati, poi prosegui al pagamento sicuro.",
  choose="Scegli il piano", monthly="Mensile", annual="Annuale", save="Risparmi il 20%", mo="/mese", mo_ann="/mese, fatturato annualmente", regular="Prezzo standard",
  first="Nome", last="Cognome", email="Indirizzo email", hotel="Nome dell’hotel", rooms="Numero di camere", phone="Telefono (facoltativo)",
  country="Paese", select_country="Seleziona il tuo paese…", other="Altro / non in elenco…", other_ph="Codice paese di 2 lettere (es. IS)",
  currency="Valuta degli ospiti", currency_hint="La valuta in cui pagano i tuoi ospiti, non il tuo abbonamento Hostlio Pro (fatturato in USD). Deve corrispondere alla valuta che usi su Booking.com e sugli altri canali. Non si può modificare in seguito.",
  tz="Fuso orario", tz_hint="Serve per inviarti il riepilogo giornaliero alle 08:00 ora locale.",
  terms='Iscrivendoti accetti i <a href="{t}">Termini di servizio</a> e l’<a href="{p}">Informativa sulla privacy</a>.',
  submit="Prosegui al pagamento sicuro", starting="Avvio del pagamento…", back="Torna alla home", login="Hai già un account?", login_a="Accedi",
  e_required="Compila tutti i campi obbligatori.", e_code="Inserisci un codice paese valido di 2 lettere (es. IS).", e_country="Seleziona il tuo paese.",
  e_currency="Seleziona la valuta in cui pagano i tuoi ospiti.", e_tz="Seleziona il tuo fuso orario.", e_email="Inserisci un indirizzo email valido.",
  r_starter="Starter supporta fino a 10 camere. Scegli Pro o Growth.", r_pro="Pro supporta fino a 50 camere. Scegli Growth.", r_growth="Growth supporta fino a 150 camere. Scrivici per strutture più grandi.",
  e_checkout="Non è stato possibile avviare il pagamento. Riprova.", e_network="Errore di rete. Controlla la connessione e riprova.",
  ok_paid="Pagamento ricevuto. Controlla la tua email per impostare la password e completare la configurazione.", cancelled="Pagamento annullato. Puoi riprovare quando vuoi.",
  lang="Lingua"),
 "pt": dict(
  kicker="Teste grátis de 7 dias", h="Comece seu teste do Hostlio Pro", sub="Crie sua conta em minutos e conecte seus canais no mesmo dia.",
  your_plan="Seu plano", card_note="Seu cartão é registrado no cadastro. Nada é cobrado até o fim dos 7 dias de teste, e você pode cancelar quando quiser antes disso.",
  secure="Pagamento seguro com Stripe", t1="Usado por hotéis independentes em mais de 20 países", t2="Conta pronta em minutos, canais conectados no mesmo dia", t3="Sem contrato de fidelidade",
  eb="Preço de lançamento para os primeiros 50 clientes, garantido enquanto você for assinante.",
  form_h="Crie sua conta", form_p="Preencha seus dados e siga para o pagamento seguro.",
  choose="Escolha seu plano", monthly="Mensal", annual="Anual", save="Economize 20%", mo="/mês", mo_ann="/mês, cobrado anualmente", regular="Preço normal",
  first="Nome", last="Sobrenome", email="E-mail", hotel="Nome do hotel", rooms="Número de quartos", phone="Telefone (opcional)",
  country="País", select_country="Selecione seu país…", other="Outro / não listado…", other_ph="Código do país com 2 letras (ex.: IS)",
  currency="Moeda dos hóspedes", currency_hint="A moeda em que seus hóspedes pagam, não a sua assinatura do Hostlio Pro (cobrada em USD). Deve ser a mesma que você usa no Booking.com e nos outros canais. Não pode ser alterada depois.",
  tz="Fuso horário", tz_hint="Usado para enviar seu resumo diário às 08:00 no horário local.",
  terms='Ao se cadastrar, você concorda com os <a href="{t}">Termos de serviço</a> e a <a href="{p}">Política de privacidade</a>.',
  submit="Continuar para o pagamento seguro", starting="Iniciando o pagamento…", back="Voltar ao início", login="Já tem uma conta?", login_a="Entrar",
  e_required="Preencha todos os campos obrigatórios.", e_code="Informe um código de país válido com 2 letras (ex.: IS).", e_country="Selecione seu país.",
  e_currency="Selecione a moeda em que seus hóspedes pagam.", e_tz="Selecione seu fuso horário.", e_email="Informe um e-mail válido.",
  r_starter="O Starter suporta até 10 quartos. Escolha Pro ou Growth.", r_pro="O Pro suporta até 50 quartos. Escolha Growth.", r_growth="O Growth suporta até 150 quartos. Fale conosco para propriedades maiores.",
  e_checkout="Não foi possível iniciar o pagamento. Tente novamente.", e_network="Erro de conexão. Verifique sua internet e tente novamente.",
  ok_paid="Pagamento recebido. Confira seu e-mail para criar sua senha e concluir a configuração.", cancelled="Pagamento cancelado. Você pode tentar de novo quando quiser.",
  lang="Idioma do site"),
 "fr": dict(
  kicker="Essai gratuit de 7 jours", h="Démarrez votre essai Hostlio Pro", sub="Créez votre compte en quelques minutes et connectez vos canaux le jour même.",
  your_plan="Votre forfait", card_note="Votre carte est enregistrée à l’inscription. Rien n’est débité avant la fin des 7 jours d’essai, et vous pouvez résilier à tout moment d’ici là.",
  secure="Paiement sécurisé par Stripe", t1="Utilisé par des hôtels indépendants dans plus de 20 pays", t2="Compte prêt en quelques minutes, canaux connectés le jour même", t3="Sans engagement de longue durée",
  eb="Tarif de lancement pour les 50 premiers clients, garanti tant que vous restez abonné.",
  form_h="Créez votre compte", form_p="Renseignez vos informations, puis passez au paiement sécurisé.",
  choose="Choisissez votre forfait", monthly="Mensuel", annual="Annuel", save="Économisez 20 %", mo="/mois", mo_ann="/mois, facturé annuellement", regular="Prix normal",
  first="Prénom", last="Nom", email="Adresse e-mail", hotel="Nom de l’hôtel", rooms="Nombre de chambres", phone="Téléphone (facultatif)",
  country="Pays", select_country="Sélectionnez votre pays…", other="Autre / non listé…", other_ph="Code pays à 2 lettres (ex. IS)",
  currency="Devise des clients", currency_hint="La devise dans laquelle paient vos clients, pas votre abonnement Hostlio Pro (facturé en USD). Elle doit correspondre à celle utilisée sur Booking.com et vos autres canaux. Elle ne pourra pas être modifiée ensuite.",
  tz="Fuseau horaire", tz_hint="Sert à envoyer votre résumé quotidien à 08 h, heure locale.",
  terms='En vous inscrivant, vous acceptez nos <a href="{t}">Conditions d’utilisation</a> et notre <a href="{p}">Politique de confidentialité</a>.',
  submit="Continuer vers le paiement sécurisé", starting="Démarrage du paiement…", back="Retour à l’accueil", login="Vous avez déjà un compte ?", login_a="Connexion",
  e_required="Veuillez remplir tous les champs obligatoires.", e_code="Veuillez saisir un code pays valide à 2 lettres (ex. IS).", e_country="Veuillez sélectionner votre pays.",
  e_currency="Veuillez sélectionner la devise de vos clients.", e_tz="Veuillez sélectionner votre fuseau horaire.", e_email="Veuillez saisir une adresse e-mail valide.",
  r_starter="Starter prend en charge jusqu’à 10 chambres. Choisissez Pro ou Growth.", r_pro="Pro prend en charge jusqu’à 50 chambres. Choisissez Growth.", r_growth="Growth prend en charge jusqu’à 150 chambres. Contactez-nous pour les établissements plus grands.",
  e_checkout="Impossible de démarrer le paiement. Veuillez réessayer.", e_network="Erreur réseau. Vérifiez votre connexion et réessayez.",
  ok_paid="Paiement reçu. Consultez vos e-mails pour définir votre mot de passe et terminer la configuration.", cancelled="Paiement annulé. Vous pouvez réessayer quand vous voulez.",
  lang="Langue"),
}


# Eklenen metinler: sunucu hata kodları (O1), deneme dönüşü (D12), yıllık toplam (Y2), sayfa başlıkları.
MORE = {
 "en": dict(title="Start Your Free Trial | Hostlio Pro", desc="Create your Hostlio Pro account in minutes and connect your channels the same day. 7-day free trial.",
  srv_hotel="Please enter your hotel name (under 200 characters).", srv_plan="Please choose a valid plan.", srv_billing="Please choose monthly or annual billing.",
  srv_rooms="Please enter a room count between 1 and 500.", srv_rate="Too many signup attempts. Please wait a few minutes and try again.",
  ok_paid="Your card is saved and your 7-day free trial has started. Check your email to set your password and finish setup.",
  nojs="Signup needs JavaScript. Please enable it, or email us and we’ll set up your account."),
 "tr": dict(title="Ücretsiz Denemeyi Başlatın | Hostlio Pro", desc="Hostlio Pro hesabınızı dakikalar içinde oluşturun, kanallarınızı aynı gün bağlayın. 7 gün ücretsiz deneme.",
  srv_hotel="Lütfen otel adınızı girin (200 karakterden kısa).", srv_plan="Lütfen geçerli bir plan seçin.", srv_billing="Lütfen aylık ya da yıllık ödemeyi seçin.",
  srv_rooms="Lütfen 1 ile 500 arasında bir oda sayısı girin.", srv_rate="Çok fazla kayıt denemesi yapıldı. Lütfen birkaç dakika bekleyip tekrar deneyin.",
  ok_paid="Kartınız kaydedildi ve 7 günlük ücretsiz denemeniz başladı. Şifrenizi belirleyip kurulumu tamamlamak için e-postanızı kontrol edin.",
  nojs="Kayıt için JavaScript gerekiyor. Lütfen açın ya da bize e-posta gönderin, hesabınızı biz kuralım."),
 "es": dict(title="Empieza tu prueba gratuita | Hostlio Pro", desc="Crea tu cuenta de Hostlio Pro en minutos y conecta tus canales el mismo día. Prueba gratuita de 7 días.",
  srv_hotel="Introduce el nombre de tu hotel (menos de 200 caracteres).", srv_plan="Elige un plan válido.", srv_billing="Elige facturación mensual o anual.",
  srv_rooms="Introduce un número de habitaciones entre 1 y 500.", srv_rate="Demasiados intentos de registro. Espera unos minutos e inténtalo de nuevo.",
  ok_paid="Tu tarjeta se ha guardado y tu prueba gratuita de 7 días ha empezado. Revisa tu correo para crear tu contraseña y terminar la configuración.",
  nojs="El registro necesita JavaScript. Actívalo o escríbenos por email y crearemos tu cuenta."),
 "it": dict(title="Inizia la prova gratuita | Hostlio Pro", desc="Crea il tuo account Hostlio Pro in pochi minuti e collega i canali in giornata. Prova gratuita di 7 giorni.",
  srv_hotel="Inserisci il nome dell’hotel (meno di 200 caratteri).", srv_plan="Scegli un piano valido.", srv_billing="Scegli la fatturazione mensile o annuale.",
  srv_rooms="Inserisci un numero di camere tra 1 e 500.", srv_rate="Troppi tentativi di iscrizione. Attendi qualche minuto e riprova.",
  ok_paid="La tua carta è stata registrata e la prova gratuita di 7 giorni è iniziata. Controlla la tua email per impostare la password e completare la configurazione.",
  nojs="L’iscrizione richiede JavaScript. Attivalo oppure scrivici via email e creeremo noi il tuo account."),
 "pt": dict(title="Comece seu teste grátis | Hostlio Pro", desc="Crie sua conta do Hostlio Pro em minutos e conecte seus canais no mesmo dia. Teste grátis de 7 dias.",
  srv_hotel="Informe o nome do hotel (menos de 200 caracteres).", srv_plan="Escolha um plano válido.", srv_billing="Escolha a cobrança mensal ou anual.",
  srv_rooms="Informe um número de quartos entre 1 e 500.", srv_rate="Muitas tentativas de cadastro. Aguarde alguns minutos e tente novamente.",
  ok_paid="Seu cartão foi registrado e seu teste grátis de 7 dias começou. Confira seu e-mail para criar sua senha e concluir a configuração.",
  nojs="O cadastro precisa de JavaScript. Ative-o ou envie um e-mail e nós criamos sua conta."),
 "fr": dict(title="Démarrez votre essai gratuit | Hostlio Pro", desc="Créez votre compte Hostlio Pro en quelques minutes et connectez vos canaux le jour même. Essai gratuit de 7 jours.",
  srv_hotel="Veuillez saisir le nom de votre hôtel (moins de 200 caractères).", srv_plan="Veuillez choisir un forfait valide.", srv_billing="Veuillez choisir une facturation mensuelle ou annuelle.",
  srv_rooms="Veuillez saisir un nombre de chambres entre 1 et 500.", srv_rate="Trop de tentatives d’inscription. Patientez quelques minutes puis réessayez.",
  ok_paid="Votre carte est enregistrée et votre essai gratuit de 7 jours a commencé. Consultez vos e-mails pour définir votre mot de passe et terminer la configuration.",
  nojs="L’inscription nécessite JavaScript. Activez-le ou écrivez-nous par e-mail et nous créerons votre compte."),
}
for _l in LANGS: S[_l].update(MORE[_l])

NATIVE = {"en": "English", "tr": "Türkçe", "es": "Español", "it": "Italiano", "pt": "Português", "fr": "Français"}


def render(build, lang=None):
    """lang=None → /signup/ (dil tarayıcıda seçilir, statik metin İngilizce); lang='xx' → /xx/signup/."""
    import importlib
    L = lang or "en"
    s = S[L]
    I = build.icon
    fill = pricing.fill
    plan_txt = {l: json.loads(fill(json.dumps(importlib.import_module("content_" + l).PLAN_TXT, ensure_ascii=False), l)) for l in LANGS}
    for l in LANGS:
        S[l]["ann_total"] = build.UI[l]["billed_line_a"]

    plans = ""
    for p in pricing.PLANS:
        pid = p["id"]
        checked = " checked" if pid == "starter" else ""
        plans += (f'<div class="plan-option"><input type="radio" name="plan" id="plan-{pid}" value="{pid}"{checked}>'
                  f'<label for="plan-{pid}"><span class="plan-name">{p["name"]}</span>'
                  f'<span class="plan-price num">⟦price:{pid}⟧<small>{s["mo"]}</small></span>'
                  f'<span class="plan-old num"><span data-t="regular">{s["regular"]}</span> <s>⟦regular:{pid}⟧</s></span></label></div>')

    feats = "".join(f"<li>{build.CHECK}<span>{f}</span></li>" for f in plan_txt[L]["starter"][1])
    tpath, ppath = build.url("terms", L), build.url("privacy", L)
    langopts = "".join(f'<option value="{l}"{" selected" if l == L else ""}>{NATIVE[l]}</option>' for l in LANGS)
    self_url = build.SITE + (build.signup_url(lang) if lang else "/signup/")

    data = {"S": S, "PLAN_TXT": plan_txt, "fixed": lang,
            "TERMS": {l: build.url("terms", l) for l in LANGS}, "PRIVACY": {l: build.url("privacy", l) for l in LANGS},
            "HOME": {l: build.url("home", l) for l in LANGS}, "SIGNUP": {l: build.signup_url(l) for l in LANGS},
            # prices.js yüklenemezse kullanılan statik kopya (aynı kaynak: pricing.py)
            "PLANS": pricing.js_config(L, "", "")["plans"], "EARLY_BIRD": pricing.EARLY_BIRD}
    co_json = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")

    head_extra = build.analytics_head()
    foot = {"en": ("Terms of Service", "Privacy Policy")}.get(L) or (build.UI[L]["terms"], build.UI[L]["privacy"])

    doc = f'''<!doctype html>
<html class="nojs" lang="{"pt-BR" if L == "pt" else L}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(s["title"])}</title>
<meta name="description" content="{html.escape(s["desc"])}">
<link rel="canonical" href="{self_url}">
<meta name="robots" content="noindex,follow">
<meta property="og:type" content="website"><meta property="og:site_name" content="Hostlio Pro"><meta property="og:locale" content="{build.LOCALE[L]}">
<meta property="og:url" content="{self_url}"><meta property="og:title" content="{html.escape(s["title"])}">
<meta property="og:description" content="{html.escape(s["desc"])}">
<meta property="og:image" content="{build.SITE}/assets/og-{L}.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#1B2B4B">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
{build.font_preloads(L)}<link rel="stylesheet" href="{build.asset('/assets/style.css')}">
{head_extra}</head>
<body class="co-body">
<header class="co-head"><div class="wrap co-head-in">
<a class="brand" href="{build.url("home", L)}" data-home aria-label="Hostlio Pro">{build.LOGO}<span>Hostlio <span class="pro">Pro</span></span></a>
<div class="co-head-end">
<span class="co-secure">{I("lock-simple") if (build.ROOT / "icons/lock-simple.svg").exists() else I("check")}<span data-t="secure">{s["secure"]}</span></span>
<label class="co-lang"><span class="sr-only" data-t="lang">{s["lang"]}</span>{I("globe-simple")}<select id="co-lang">{langopts}</select></label>
</div></div></header>

<main id="main" class="co-main"><div class="wrap co-grid">
<aside class="co-aside on-dark">
<p class="co-kicker"><span data-t="kicker">{s["kicker"]}</span></p>
<h1 data-t="h">{s["h"]}</h1>
<p class="co-sub" data-t="sub">{s["sub"]}</p>
<div class="co-summary">
<div class="co-sum-top"><span data-t="your_plan">{s["your_plan"]}</span><b id="sum-name">Starter</b></div>
<div class="co-sum-price num"><b id="sum-price">⟦price:starter⟧</b><span id="sum-suffix">{s["mo"]}</span></div>
<p class="co-sum-total small num" id="sum-total" hidden></p>
<ul class="co-feats" id="sum-feats">{feats}</ul>
</div>
<p class="co-note">{I("identification-card")}<span data-t="card_note">{s["card_note"]}</span></p>
<ul class="co-trust">
<li>{I("globe-simple")}<span data-t="t1">{s["t1"]}</span></li>
<li>{I("rocket-launch")}<span data-t="t2">{s["t2"]}</span></li>
<li>{I("check")}<span data-t="t3">{s["t3"]}</span></li>
</ul>
<p class="co-eb" data-eb>{I("sparkle")}<span data-t="eb">{s["eb"]}</span></p>
</aside>

<section class="co-card" aria-labelledby="form-h">
<h2 id="form-h" data-t="form_h">{s["form_h"]}</h2>
<p class="co-form-p" data-t="form_p">{s["form_p"]}</p>
<noscript><p class="co-alert">{s["nojs"]} <a href="mailto:{build.EMAIL}">{build.EMAIL}</a></p></noscript>
<div class="error-msg co-alert" id="error-msg" role="alert" hidden></div>

<form id="signup-form" action="#" method="post" aria-describedby="error-msg" novalidate>
<fieldset class="co-plans"><legend data-t="choose">{s["choose"]}</legend>
<div class="billing co-billing" role="group" aria-labelledby="co-bill-l"><span id="co-bill-l" class="sr-only">{s["monthly"]} / {s["annual"]}</span><button type="button" class="on" aria-pressed="true" data-bill="m" data-t="monthly">{s["monthly"]}</button><button type="button" aria-pressed="false" data-bill="a"><span data-t="annual">{s["annual"]}</span> <span class="save" data-t="save">{s["save"]}</span></button></div>
<div class="plan-grid">{plans}</div>
</fieldset>

<div class="co-row">
<label class="co-field"><span data-t="first">{s["first"]}</span> <em aria-hidden="true">*</em><input type="text" id="firstName" name="firstName" autocomplete="given-name" required aria-describedby="error-msg"></label>
<label class="co-field"><span data-t="last">{s["last"]}</span> <em aria-hidden="true">*</em><input type="text" id="lastName" name="lastName" autocomplete="family-name" required aria-describedby="error-msg"></label>
</div>
<label class="co-field"><span data-t="email">{s["email"]}</span> <em aria-hidden="true">*</em><input type="email" id="email" name="email" autocomplete="email" required aria-describedby="error-msg"></label>
<label class="co-field"><span data-t="hotel">{s["hotel"]}</span> <em aria-hidden="true">*</em><input type="text" id="hotelName" name="hotelName" autocomplete="organization" maxlength="200" placeholder="Seaside Boutique Hotel" required aria-describedby="error-msg"></label>
<div class="co-row">
<label class="co-field"><span data-t="rooms">{s["rooms"]}</span> <em aria-hidden="true">*</em><input type="number" id="rooms" name="rooms" inputmode="numeric" min="1" max="500" required aria-describedby="rooms-error">
<span id="rooms-error" class="co-err" role="alert" hidden></span></label>
<label class="co-field"><span data-t="phone">{s["phone"]}</span><input type="tel" id="phone" name="phone" autocomplete="tel"></label>
</div>
<label class="co-field"><span data-t="country">{s["country"]}</span> <em aria-hidden="true">*</em>
<select id="country" name="country" required aria-describedby="locale-error"><option value="" data-t="select_country">{s["select_country"]}</option></select>
<input type="text" id="countryOther" name="countryOther" maxlength="2" pattern="[A-Za-z]{{2}}" hidden style="text-transform:uppercase" data-tph="other_ph" placeholder="{s["other_ph"]}" aria-label="{s["other_ph"]}" aria-describedby="locale-error"></label>
<div class="co-row">
<label class="co-field"><span data-t="currency">{s["currency"]}</span> <em aria-hidden="true">*</em><select id="currency" name="currency" required aria-describedby="currency-hint locale-error"></select><small class="co-warn" id="currency-hint" data-t="currency_hint">{s["currency_hint"]}</small></label>
<label class="co-field"><span data-t="tz">{s["tz"]}</span> <em aria-hidden="true">*</em><select id="timezone" name="timezone" required aria-describedby="tz-hint locale-error"></select><small id="tz-hint" data-t="tz_hint">{s["tz_hint"]}</small></label>
</div>
<span id="locale-error" class="co-err" role="alert" hidden></span>

<p class="terms co-terms" id="co-terms">{s["terms"].format(t=tpath, p=ppath)}</p>
<button type="submit" class="btn btn-primary co-submit" id="submit-btn">{s["submit"]}</button>
<p class="co-login"><span data-t="login">{s["login"]}</span> <a href="{build.LOGIN_URL}" data-t="login_a">{s["login_a"]}</a></p>
</form>
</section>
</div></main>

<footer class="co-foot"><div class="wrap"><span>© {UPD_YEAR(build)} Hostlio Pro, Loti Members LLC</span>
<a href="{tpath}" id="co-f-terms">{foot[0]}</a><a href="{ppath}" id="co-f-privacy">{foot[1]}</a><a href="mailto:{build.EMAIL}">{build.EMAIL}</a></div></footer>

<script type="application/json" id="co-data">{co_json}</script>
{build.pricing_block(L)}<script src="{build.asset('/assets/signup.js')}" defer></script>
<script src="{build.asset('/attribution.js')}" defer></script>
</body>
</html>'''
    return pricing.fill(doc, L)


def UPD_YEAR(build):
    import datetime
    return datetime.date.fromisoformat(build.UPDATED).year
