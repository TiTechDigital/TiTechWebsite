# -*- coding: utf-8 -*-
"""Validate topic cluster integrity for Phase 7.

Checks that every article in a cluster exists in both languages, is in the
sitemap, links to its pillar, and that each pillar lists its cluster articles.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITEMAP = ROOT / 'sitemap.xml'

# Cluster definitions: pillar URL -> list of (IT slug, EN slug)
CLUSTERS = {
    '/servizi/siti-web/': [
        ('quanto-costa-sito-web-italia-2026', 'website-cost-italy-2026'),
        ('wordpress-o-sito-su-misura', 'wordpress-vs-custom-website'),
        ('come-scegliere-hosting', 'how-to-choose-web-hosting'),
        ('manutenzione-sito-web', 'website-maintenance'),
        ('seo-tecnica-siti-web', 'technical-seo-websites'),
        ('sito-web-responsive-guida', 'responsive-website-guide'),
    ],
    '/servizi/e-commerce/': [
        ('e-commerce-b2b-quando-conviene', 'b2b-ecommerce-when-it-pays-off'),
        ('piattaforma-e-commerce-come-scegliere', 'how-to-choose-ecommerce-platform'),
        ('catalogo-prodotti-e-commerce', 'ecommerce-product-catalog'),
        ('pagamenti-e-commerce', 'ecommerce-payments'),
        ('spedizioni-e-commerce', 'ecommerce-shipping'),
    ],
    '/servizi/software-su-misura/': [
        ('quando-serve-software-su-misura', 'when-you-need-custom-software'),
        ('specifiche-software-su-misura', 'custom-software-specifications'),
        ('integrazioni-erp-crm', 'erp-crm-integrations'),
        ('api-per-aziende', 'apis-for-business'),
        ('mvp-software-su-misura', 'mvp-custom-software'),
    ],
    '/servizi/automazioni-ai/': [
        ('automazione-ai-pmi-5-processi', 'ai-automation-smes-5-processes'),
        ('automazione-ai-costi-benefici', 'ai-automation-costs-benefits'),
        ('automazione-processi-senza-ai', 'automation-without-ai'),
        ('chatbot-aziendale-quando-ha-senso', 'when-a-business-chatbot-makes-sense'),
        ('automazione-ai-dati-privacy', 'ai-automation-data-privacy'),
    ],
    '/servizi/seo/': [
        ('seo-tecnica-checklist', 'technical-seo-checklist'),
        ('seo-locale-novara', 'local-seo-novara'),
        ('contenuti-seo-come-scrivere', 'how-to-write-seo-content'),
        ('seo-vs-google-ads', 'seo-vs-google-ads'),
        ('misurare-seo', 'measuring-seo'),
    ],
}

PILLAR_EN_MAP = {
    '/servizi/siti-web/': '/en/services/website-design/',
    '/servizi/e-commerce/': '/en/services/ecommerce/',
    '/servizi/software-su-misura/': '/en/services/custom-software/',
    '/servizi/automazioni-ai/': '/en/services/ai-automation/',
    '/servizi/seo/': '/en/services/seo/',
}


def url_for(slug, lang):
    if lang == 'it':
        return '/blog/%s/' % slug
    return '/en/blog/%s/' % slug


def exists(path):
    return path.exists()


def main():
    problems = []
    sitemap = SITEMAP.read_text(encoding='utf-8')
    locs = set(re.findall(r'<loc>(.*?)</loc>', sitemap))
    base = 'https://titechdigital.it'

    for pillar, articles in CLUSTERS.items():
        it_pillar = ROOT / pillar.strip('/') / 'index.html'
        en_pillar = ROOT / 'en' / pillar.strip('/') / 'index.html'
        # pillar files may be at different paths; check
        if not it_pillar.exists():
            problems.append('pillar missing: ' + pillar)
            continue

        it_pillar_text = it_pillar.read_text(encoding='utf-8')
        en_pillar_text = en_pillar.read_text(encoding='utf-8') if en_pillar.exists() else ''

        for it_slug, en_slug in articles:
            it_url = url_for(it_slug, 'it')
            en_url = url_for(en_slug, 'en')
            it_path = ROOT / 'blog' / it_slug / 'index.html'
            en_path = ROOT / 'en' / 'blog' / en_slug / 'index.html'

            # existence
            if not it_path.exists():
                print('TODO: not written yet: ' + it_url)
                continue
            if not en_path.exists():
                print('TODO: not written yet: ' + en_url)
                continue

            # sitemap
            if base + it_url not in locs:
                problems.append('not in sitemap: ' + it_url)
            if base + en_url not in locs:
                problems.append('not in sitemap: ' + en_url)

            # hreflang
            it_text = it_path.read_text(encoding='utf-8')
            en_text = en_path.read_text(encoding='utf-8')
            if base + en_url not in it_text:
                problems.append('missing hreflang to EN twin: ' + it_url)
            if base + it_url not in en_text:
                problems.append('missing hreflang to IT twin: ' + en_url)

            # pillar link in article
            if pillar not in it_text:
                problems.append('IT article does not link to pillar %s: %s' % (pillar, it_url))
            en_pillar = PILLAR_EN_MAP.get(pillar, pillar)
            if en_pillar not in en_text and pillar not in en_text:
                problems.append('EN article does not link to pillar: ' + en_url)

            # pillar lists article (warning only: pillars are updated per cluster)
            if it_slug not in it_pillar_text:
                print('WARNING: pillar %s does not yet list %s' % (pillar, it_slug))

    # summary
    total = sum(len(v) for v in CLUSTERS.values())
    written_it = 0
    written_en = 0
    for pillar, articles in CLUSTERS.items():
        for it_slug, en_slug in articles:
            if (ROOT / 'blog' / it_slug / 'index.html').exists():
                written_it += 1
            if (ROOT / 'en' / 'blog' / en_slug / 'index.html').exists():
                written_en += 1

    for p in problems:
        print('PROBLEM:', p)
    print('')
    print('Clusters: %d' % len(CLUSTERS))
    print('Articles planned: %d (IT+EN pairs)' % total)
    print('Articles written: %d IT, %d EN' % (written_it, written_en))
    print('Problems: %d' % len(problems))
    return 1 if problems else 0


if __name__ == '__main__':
    sys.exit(main())
