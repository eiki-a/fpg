# -*- coding: utf-8 -*-
import sys,re
pat=re.compile('@[a-z,_]* ')
for line in sys.stdin:
    if pat.match(line):
        print pat.search(line).group()