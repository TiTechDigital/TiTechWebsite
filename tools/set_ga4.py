# -*- coding: utf-8 -*-
"""Switch the GA4 measurement ID on or off across every published page.

  python tools/set_ga4.py --check
  python tools/set_ga4.py G-XXXXXXXXXX
  python tools/set_ga4.py --off

Setting an ID is only half of the activation: docs/phase-6-measurement.md lists
the policy and consent steps that must happen in the same change.
"""
import glob
import re
import sys

SKIP = {'brand-logo.html', 'og-card.html', 'index.original.html'}
PATTERN = re.compile(r'(<meta name="ga4-id" content=")([^"]*)(">)')
VALID = re.compile(r'^G-[A-Z0-9]{4,20}$')


def pages():
    for path in glob.glob('**/*.html', recursive=True):
        if path.replace('\\', '/') not in SKIP:
            yield path


def read(path):
    with open(path, encoding='utf-8', newline='') as handle:
        return handle.read()


def write(path, text):
    with open(path, 'w', encoding='utf-8', newline='') as handle:
        handle.write(text)


def main():
    if len(sys.argv) != 2:
        print(__doc__.strip())
        return 2
    mode = sys.argv[1]
    if mode not in {'--check', '--off'} and not VALID.match(mode.upper()):
        print('not a GA4 measurement ID: ' + mode)
        return 2

    if mode == '--check':
        values = {}
        missing = []
        for path in pages():
            match = PATTERN.search(read(path))
            if not match:
                missing.append(path)
                continue
            values[match.group(2)] = values.get(match.group(2), 0) + 1
        for value, count in sorted(values.items()):
            print('%s: %d pages' % (value or '(empty)', count))
        for path in missing:
            print('missing meta: ' + path)
        return 1 if missing else 0

    value = '' if mode == '--off' else mode.upper()
    changed = 0
    missing = []
    for path in pages():
        text = read(path)
        if not PATTERN.search(text):
            missing.append(path)
            continue
        updated = PATTERN.sub(lambda m: m.group(1) + value + m.group(3), text, count=1)
        if updated != text:
            write(path, updated)
            changed += 1
    print('%d pages updated to "%s"' % (changed, value or '(off)'))
    for path in missing:
        print('missing meta: ' + path)
    if value:
        print('Now update /cookie, /en/cookies, /privacy and /en/privacy: the site currently '
              'promises no analytics. See docs/phase-6-measurement.md, section 7.')
    return 1 if missing else 0


if __name__ == '__main__':
    sys.exit(main())
