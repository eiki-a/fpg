import sys
line = sys.stdin.readlines()
f1 = open('col1.txt', 'w')
f2 = open('col2.txt', 'w')
for x in line:
    f1.write(x.split('\t')[0]+'\n')
    f2.write(x.split('\t')[1])