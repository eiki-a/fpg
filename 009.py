import sys
list1=sys.stdin.readlines()
list1[-1:]=[list1[len(list1)-1]+'\n']

def qsort(arg): # 008.py��qsort�ɂ�����center�ɐU�蕪�����Ă������̂̂����A1�ڂ̗v�f�Ŕ�r���đ傫�����̂�left�A���������̂�right�ɐU�蕪����悤�ɂ����B
    if (len(arg)<=1):
        return arg
    else:
        left = []
        right = []
        center = []
        for var in arg:
            if len(var.split('\t'))<=1:
                pass
            elif (var.split('\t')[1] < arg[0].split('\t')[1]):
                left.insert(0, var)
            elif (var.split('\t')[1] == arg[0].split('\t')[1]):
                if (var.split('\t')[0] < arg[0].split('\t')[0]):
                    left.insert(0, var)
                elif (var.split('\t')[0] == arg[0].split('\t')[0]):
                    center.insert(0,var)
                else:
                    right.insert(0, var)
            else:
                right.insert(0, var)
        return qsort(right) + center + qsort(left) # 008.py�Ƃ͋t���ɂȂ�悤�ɁA�߂�l�𒲐�����B

for x in qsort(list1):
    print x ,