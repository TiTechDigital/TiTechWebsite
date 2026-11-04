# -*- coding: utf-8 -*-
import subprocess
r = subprocess.run(['git', 'show', '5f7a851:blog/quanto-costa-sito-web-italia-2026/index.html'], capture_output=True, text=True)
s = r.stdout
print('len', len(s))
print('footer count', s.count('<footer'))
print('exit', r.returncode)
