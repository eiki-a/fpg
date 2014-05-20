# -*- coding: utf-8 -*-
import sys,re,codecs

file1=open('test.txt', mode='w')
post=u'[^0-9‐－\-][0-9０-９]{3,3}[‐－\-][0-9０-９]{4,4}'
pref=u'(.{2,3}県|東京都|大阪府|京都府|北海道)'
city=u'[一-龠あ-んア-ン]{1,6}(市|町|村)'
for line in sys.stdin:
    if re.search(post, line.decode('utf-8')):
        try:
            wtext1=re.search(post, line.decode('utf-8')).group().encode('utf-8')
            wtext2=re.search(pref, line.decode('utf-8')).group().encode('utf-8')
            wtext3=re.search(city, line.decode('utf-8')).group().encode('utf-8')
            file1.write('('+wtext1+'\t'+wtext2+'\t'+wtext3+')\n')
        except:
            pass

file1.close()