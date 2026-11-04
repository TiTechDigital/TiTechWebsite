# -*- coding: utf-8 -*-
s = open(r'C:\Users\eneam\Downloads\TiTechWebsite\blog\quanto-costa-sito-web-italia-2026\index.html', encoding='utf-8').read()
pos = 0
while True:
    i = s.find('<footer', pos)
    if i == -1:
        break
    print('footer at', i, ':', repr(s[i:i+60].replace(chr(10), ' ')))
    pos = i + 1
