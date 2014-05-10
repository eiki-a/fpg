list1=open('address', 'r').readlines()
list1[-1:]=[list1[len(list1)-1]+'\n']
list2=[]

def qsort(arg): # 008.pyとほぼ同じもの。逆順なので戻り値のみ調整してある。
    if (len(arg)<=1):
        return arg
    else:
        left = []
        right = []
        center = []
        for var in arg:
            if len(var)<=1:
                pass
            elif (var[1] < arg[0][1]):
                left.insert(0, var)
            elif (var[1] == arg[0][1]):
                center.insert(0,var)
            else:
                right.insert(0, var)
        return qsort(right) + center + qsort(left)

for x in list1[:]: # まずはリストの各要素に0を付与し、リスト内に同じ要素があるたびに1ずつ増やしていくようにした。
    x=[x,0]
    for y in list1[:]:
        if x[0]==y:
            x[1]=x[1]+1
        else:
            pass
    list2.insert(0, x)

for z in qsort(list2): # qsortにて付与した数字が大きい順に並び替え、結果を表示する。
    print z[0] ,