# -*- coding: utf-8 -*-
import sys,re,codecs

file1=open('test.txt', mode='w')
pattern=u'(?P<name>[一-龠]{1,3}([あ-ん]{2-6}|[一-龠]{1,3}))(?P<gobi>(さん|ちゃん｜くん))'
for line in sys.stdin:
    if re.search(pattern, line.decode('utf-8')):
        particle=re.search(pattern, line.decode('utf-8'))
#        try:
        wtext1=particle.group('name').encode('utf-8')
        wtext2=particle.group('gobi').encode('utf-8')
        file1.write(wtext1+'\t'+wtext2+'\n')
#        except:
#            print'error.'

file1.close()