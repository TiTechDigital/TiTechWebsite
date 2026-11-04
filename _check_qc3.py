# -*- coding: utf-8 -*-
s = open(r'C:\Users\eneam\Downloads\TiTechWebsite\blog\quanto-costa-sito-web-italia-2026\index.html', encoding='utf-8').read()
i = s.find('<footer id="footer"')
print(repr(s[i-200:i+100]))
