# -*- coding: utf-8 -*-
import re
s = open(r'C:\Users\eneam\Downloads\TiTechWebsite\index.html', encoding='utf-8').read()
m = re.search(r'"telephone": "[^"]*"', s)
print('homepage JSON-LD telephone:', m.group(0) if m else 'NOT FOUND')
s2 = open(r'C:\Users\eneam\Downloads\TiTechWebsite\contatti\index.html', encoding='utf-8').read()
m2 = re.search(r'"telephone": "[^"]*"', s2)
print('contact JSON-LD telephone:', m2.group(0) if m2 else 'NOT FOUND')
