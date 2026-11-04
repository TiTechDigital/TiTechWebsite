import glob, io, re, sys

pat = re.compile(r'\u2014')
for p in sys.argv[1:]:
    text = io.open(p, encoding='utf-8', newline='').read()
    for i, line in enumerate(text.split('\n'), 1):
        if pat.search(line):
            for m in pat.finditer(line):
                a = max(0, m.start() - 95)
                print('%s:%d| %s' % (p, i, line[a:m.end() + 95].strip()))
