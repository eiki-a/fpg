import sys
list1=sys.stdin.readlines()
list1[-1:]=[list1[len(list1)-1]+'\n']

def qsort(arg): # 008.pyのqsortにおいてcenterに振り分けられていたもののうち、1つ目の要素で比較して大きいものをleft、小さいものをrightに振り分けるようにした。
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
        return qsort(right) + center + qsort(left) # 008.pyとは逆順になるように、戻り値を調整する。

for x in qsort(list1):
    print x ,