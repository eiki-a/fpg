# -*- coding: utf-8 -*-
import sys,re,codecs

file1=open('test.txt', mode='w')
pattern=u'(宮城県)?仙台市.{1,3}区.{2,6}([0-9０-９－‐の\-]{3,8}|.+号)'
for line in sys.stdin:
    if re.search(pattern, line.decode('utf-8')):
        particle=re.search(pattern, line.decode('utf-8'))
#        try:
        wtext=particle.group().encode('utf-8')
        file1.write(wtext+'\n')
#        except:
#            print'error.'

file1.close()