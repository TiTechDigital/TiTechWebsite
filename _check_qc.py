# -*- coding: utf-8 -*-
s = open(r'C:\Users\eneam\Downloads\TiTechWebsite\blog\quanto-costa-sito-web-italia-2026\index.html', encoding='utf-8').read()
print('footer tag count:', s.count('<footer'))
print('footer id count:', s.count('id="footer"'))
print('len:', len(s))
i = s.find('<footer')
j = s.find('</footer>', i) + len('</footer>')
print('first footer:', s[i:i+60].replace(chr(10), ' '))
print('second footer at:', s.find('<footer', i+1))
