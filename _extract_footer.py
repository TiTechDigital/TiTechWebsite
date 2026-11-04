# -*- coding: utf-8 -*-
s = open(r'C:\Users\eneam\Downloads\TiTechWebsite\index.html', encoding='utf-8').read()
start = s.index('<footer id="footer"')
end = s.index('</footer>', start) + len('</footer>')
footer = s[start:end]
with open(r'C:\Users\eneam\Downloads\TiTechWebsite\homepage_footer.txt', 'w', encoding='utf-8') as f:
    f.write(footer)
print('chars', len(footer))
print(footer)
