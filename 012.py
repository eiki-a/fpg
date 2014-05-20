# -*- coding: utf-8 -*-
import sys,re
pat=re.compile('なう$')
for line in sys.stdin:
    if pat.search(line):
        print line