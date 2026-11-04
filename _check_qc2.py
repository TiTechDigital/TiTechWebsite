# -*- coding: utf-8 -*-
s = open(r'C:\Users\eneam\Downloads\TiTechWebsite\blog\quanto-costa-sito-web-italia-2026\index.html', encoding='utf-8').read()
i = s.find('<footer id="footer"')
j = s.find('</footer>', i) + len('</footer>')
print('first footer at', i, 'ends at', j)
print('after first footer:', repr(s[j:j+200]))
print('total len', len(s))
