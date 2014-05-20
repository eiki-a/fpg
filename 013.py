# -*- coding: utf-8 -*-
import sys,re
pat=re.compile('.*RT ')
for line in sys.stdin:
    if pat.match(line):
        print pat.search(line).group()