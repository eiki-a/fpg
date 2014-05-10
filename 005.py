line = open('col2.txt').readlines()
num = int(raw_input())
x=0
while x < num:
    print(line[x])
    x = x + 1

# import sys
# N = int(sys.argv[1])
# f = open("./address.txt","r")
# lines = f.readlines()
# for num in range(0,N):
#     print lines[num]
# f.close()
# fairu ha chanto tojiyou