# -*- coding: utf-8 -*-
import glob
count = 0
for path in glob.glob('**/*.html', recursive=True):
    data = open(path, 'rb').read()
    if data.startswith(b'\xef\xbb\xbf'):
        open(path, 'wb').write(data[3:])
        count += 1
# Also strip BOM from footer text files
for fn in ['homepage_footer.txt', 'homepage_footer_en.txt']:
    try:
        data = open(fn, 'rb').read()
        if data.startswith(b'\xef\xbb\xbf'):
            open(fn, 'wb').write(data[3:])
            count += 1
    except FileNotFoundError:
        pass
print('stripped BOM from', count, 'files')
