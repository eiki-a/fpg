# -*- coding: utf-8 -*-
import sys,re,codecs

file1=open('test.txt', mode='w')
pattern=u'(?P<kanji>[一-龠]+)[（\(](?P<rubi>[A-Z]+)[）\)]'
for line in sys.stdin:
    if re.search(pattern, line.decode('utf-8')):
        particle=re.search(pattern, line.decode('utf-8'))
#        try:
        wtext1=particle.group('kanji').encode('utf-8')
        wtext2=particle.group('rubi').encode('utf-8')
        file1.write(wtext1+'\t'+wtext2+'\n')
#        except:
#            print'error.'

file1.close()