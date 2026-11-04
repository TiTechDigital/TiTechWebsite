# -*- coding: utf-8 -*-
s = open(r'C:\Users\eneam\Downloads\TiTechWebsite\blog\quanto-costa-sito-web-italia-2026\index.html', encoding='utf-8').read()
i = s.find('<footer id="footer"')
j = s.find('</footer>', i) + len('</footer>')
print(repr(s[j:j+300]))
