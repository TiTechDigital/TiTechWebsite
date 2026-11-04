# -*- coding: utf-8 -*-
s1 = open(r'C:\Users\eneam\Downloads\TiTechWebsite\index.html', encoding='utf-8').read()
i1 = s1.index('<footer id="footer"')
j1 = s1.index('</footer>', i1) + len('</footer>')
f1 = s1[i1:j1]

s2 = open(r'C:\Users\eneam\Downloads\TiTechWebsite\chi-siamo\index.html', encoding='utf-8').read()
i2 = s2.index('<footer id="footer"')
j2 = s2.index('</footer>', i2) + len('</footer>')
f2 = s2[i2:j2]

# Find differences
import difflib
diff = difflib.unified_diff(f1.splitlines(), f2.splitlines(), lineterm='')
for line in diff:
    print(line)
