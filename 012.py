# -*- coding: utf-8 -*-
import sys,re
pat=re.compile('�Ȃ�$')
for line in sys.stdin:
    if pat.match(line):
        print line