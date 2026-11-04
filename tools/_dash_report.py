import glob, re, sys

SKIP = ('.qoder', 'node_modules', 'tools', 'og-card', 'brand-logo', 'index.original')
exts = sys.argv[1] if len(sys.argv) > 1 else 'html'
out = []
for p in sorted(glob.glob('**/*.' + exts, recursive=True)):
    if p.startswith(SKIP):
        continue
    text = open(p, encoding='utf-8').read()
    for m in re.finditer(r'\u2014|\u2013', text):
        a = max(0, m.start() - 110)
        b = min(len(text), m.end() + 110)
        frag = ' '.join(text[a:b].split())
        out.append('%s|%d|%s|%s' % (p, m.start(), m.group(0), frag))
print(len(out))
print('\n'.join(out))
