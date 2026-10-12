"""Tur 2 (8 Ekim 2026): çok dilli rehber kaydı.
- post-pms-vs-cm: "PMS vs channel manager" (SEO fikri #20) — EN, IT, PT, FR (rehber_pms_cm.py)
- post-whatsapp: "WhatsApp for hotels" — EN yazısı genişletildi (eski /en/blog/whatsapp-hotel-guest-communication/ adresi
  korunur, legacy_posts.json'daki eski gövde artık kullanılmaz), ES/IT/FR sürümleri (SEO fikri #14) (rehber_whatsapp.py)
Blog listesi: content_<dil>.POSTS bu modülün meta(L) çıktısını başa ekler. Kapaklar COVER'da."""
import importlib
import rehber_pms_cm, rehber_whatsapp, rehber_precios, rehber_best_pms, rehber_alloggiati, rehber_gestionali, rehber_booking_tr, rehber_cm_fr, rehber_cm_it, rehber_costo_it, rehber_custo_pt

MODS = [rehber_custo_pt, rehber_costo_it, rehber_cm_it, rehber_cm_fr, rehber_booking_tr, rehber_gestionali, rehber_alloggiati, rehber_best_pms, rehber_precios, rehber_pms_cm, rehber_whatsapp]
COVER = {"post-costpt": ("cover-custo-sistema-pt", 1600, 800), "post-costit": ("cover-costo-gestionale-it", 1600, 800), "post-cmit": ("cover-channel-manager-it", 1600, 800), "post-cmfr": ("cover-channel-manager-fr", 1600, 800), "post-bookingkom": ("cover-booking-komisyon", 1600, 800), "post-gestionali": ("cover-gestionali-it", 1600, 800), "post-alloggiati": ("cover-alloggiati-it", 1600, 800), "post-bestpms": ("cover-best-pms-en", 1600, 800), "post-cost": ("cover-precios-software-es", 1600, 800), "post-pms-vs-cm": ("gen-support-call", 1080, 1350), "post-whatsapp": ("gen-terrace-phone", 1080, 1350)}


def meta(L):
    return [dict(m.META[L]) for m in MODS if L in m.META and L in m.FN]


def pages(L, url):
    """url: build.url — her yazı o dilin content_<dil>.article() şablonuyla üretilir."""
    art = importlib.import_module("content_" + L).article
    U = lambda k: url(k, L)
    out = []
    for m in MODS:
        if L in m.FN:
            c, faq = m.FN[L](U)
            if L == "fr":   # FR tipografi: « : ; ? ! » öncesi bölünmez boşluk (ozellik_ekleri ile aynı kural)
                from ozellik_ekleri import _fr_typo
                c, faq = _fr_typo(c), _fr_typo(faq)
            out.append(art(dict(m.META[L]), c, faq))
    return out
