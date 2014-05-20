# -*- coding: utf-8 -*-
import sys,re,codecs

file1=open('test.txt', mode='w')
pattern=u'[（\(][DTOodbqpm9ノのワくゞー´・ω・`；：＠Д⊂⊃ヽＡﾟ∀＝=≡＊＃@#\^\-><＞＜＿_。;:/\\\.\)\*]{2,7}'
for line in sys.stdin:
    if re.search(pattern, line.decode('utf-8')):
        particle=re.search(pattern, line.decode('utf-8'))
#        try:
        wtext=particle.group().encode('utf-8')
        file1.write(wtext+'\n')
#        except:
#            print'error.'

file1.close()