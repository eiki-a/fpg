# -*- coding: utf-8 -*-
import sys,re # ¢¸êà zcat tweets.txt.gz | python 01X.pyÅ®ì
pat=re.compile('gUó]')
for line in sys.stdin:
    if pat.search(line):
        print line