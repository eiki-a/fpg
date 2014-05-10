y=0
l1 = open('col1.txt', 'r')
l2 = open('col2.txt', 'r').readlines()
for x in l1:
    print(x.strip('\n') + '\t' + l2[y].strip('\n'))
    y=y+1

# wtr=open(reunion.txt w
# for fst.sec in zip(open("./col1.txt","r").readlines().open("./col2.txt","r").readlines()):
#    wtr.write(fst.strip("\n") + "\t"+sec)
# wtr.close()