# -*- coding: utf-8 -*-
import sys,re # いずれも zcat tweets.txt.gz | python 01X.pyで動作
pattern=u'拡散希望'
for line in sys.stdin:
    if re.search(pattern, line.decode('utf-8')):
        print line