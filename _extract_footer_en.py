# -*- coding: utf-8 -*-
s = open(r'C:\Users\eneam\Downloads\TiTechWebsite\en\index.html', encoding='utf-8').read()
i = s.index('<footer id="footer"')
j = s.index('</footer>', i) + len('</footer>')
footer = s[i:j]
with open(r'C:\Users\eneam\Downloads\TiTechWebsite\homepage_footer_en.txt', 'w', encoding='utf-8') as f:
    f.write(footer)
print('chars', len(footer))
