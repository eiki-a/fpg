# -*- coding: utf-8 -*-
import sys,re # ������� zcat tweets.txt.gz | python 01X.py�œ���
pat=re.compile('�g�U��]')
for line in sys.stdin:
    if pat.search(line):
        print line