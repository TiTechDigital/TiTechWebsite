# -*- coding: utf-8 -*-
s = open(r'C:\Users\eneam\Downloads\TiTechWebsite\blog\quanto-costa-sito-web-italia-2026\index.html', encoding='utf-8').read()
# Show context around each footer
for pos in [42794, 46777, 50720, 67632]:
    # find the nearest preceding section or heading
    ctx = s[max(0,pos-150):pos+80]
    print('=== footer at', pos, '===')
    print(repr(ctx.replace(chr(10), ' | ')))
    print()
