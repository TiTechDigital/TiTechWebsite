# -*- coding: utf-8 -*-
import glob, re

# Read homepage footers
it_footer = open(r'C:\Users\eneam\Downloads\TiTechWebsite\homepage_footer.txt', encoding='utf-8').read()
en_footer = open(r'C:\Users\eneam\Downloads\TiTechWebsite\homepage_footer_en.txt', encoding='utf-8').read()

# Adapt IT footer for inner pages
it_adapted = it_footer.replace('src="assets/img/', 'src="/assets/img/')
it_adapted = it_adapted.replace('srcset="assets/img/', 'srcset="/assets/img/')
it_adapted = it_adapted.replace('href="#contact"', 'href="/contatti/"')

# Adapt EN footer for inner pages
en_adapted = en_footer.replace('src="../assets/img/', 'src="/assets/img/')
en_adapted = en_adapted.replace('srcset="assets/img/', 'srcset="/assets/img/')
en_adapted = en_adapted.replace('href="#contact"', 'href="/en/contact/"')

SKIP = {'index.html', 'brand-logo.html', 'og-card.html', 'index.original.html'}
count = 0
for path in glob.glob('**/*.html', recursive=True):
    norm = path.replace('\\', '/')
    if norm in SKIP:
        continue
    is_en = norm.startswith('en/')
    footer = en_adapted if is_en else it_adapted

    s = open(path, encoding='utf-8', newline='').read()
    # Find existing footer
    start = s.find('<footer id="footer"')
    if start == -1:
        print('NO FOOTER:', path)
        continue
    end = s.find('</footer>', start)
    if end == -1:
        print('NO CLOSE:', path)
        continue
    end += len('</footer>')

    # Replace footer, keep scripts after
    new_s = s[:start] + footer + s[end:]
    open(path, 'w', encoding='utf-8', newline='').write(new_s)
    count += 1

print('pages updated:', count)
