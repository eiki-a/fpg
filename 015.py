# -*- coding: utf-8 -*-
import sys,re
pat=re.compile('@[\w]* ') # @(�����A�����A�Q)�i�󔒁j
for line in sys.stdin:
    if pat.match(line):
        usrname=pat.search(line).group()
        sys.stdout.write(line.replace(usrname,'<a href="https://twitter.com/#!/' + usrname.lstrip('@').rstrip() + '">' + usrname.rstrip() + '</a> '))