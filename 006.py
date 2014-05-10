line = open('address').readlines()
x=len(line)
num = int(raw_input())
while num > 0:
    print(line[x-num])
    num = num - 1