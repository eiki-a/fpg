import sys
list1=sys.stdin.readlines()
list1[-1:]=[list1[len(list1)-1]+'\n'] # 配列の末尾の要素に改行を加える。

def qsort(arg): # クイックソートを行う関数qsortを定義する。リスト内の要素が先頭の要素より大きければrightに、小さければleftに、同じならばcenterに渡し、rightとleftに再帰的にqsortをかけることをすべてのリストの要素数が1以下になるまで続ける。
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
                center.insert(0,var)
            else:
                right.insert(0, var)
        return qsort(left) + center + qsort(right)

for x in qsort(list1): # クイックソートの結果を表示する。
    print x ,