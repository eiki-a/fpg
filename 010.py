list1=open('address', 'r').readlines()
list1[-1:]=[list1[len(list1)-1]+'\n']
list2=[]

def qsort(arg): # 008.py�Ƃقړ������́B�t���Ȃ̂Ŗ߂�l�̂ݒ������Ă���B
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

for x in list1[:]: # �܂��̓��X�g�̊e�v�f��0��t�^���A���X�g���ɓ����v�f�����邽�т�1�����₵�Ă����悤�ɂ����B
    x=[x,0]
    for y in list1[:]:
        if x[0]==y:
            x[1]=x[1]+1
        else:
            pass
    list2.insert(0, x)

for z in qsort(list2): # qsort�ɂĕt�^�����������傫�����ɕ��ёւ��A���ʂ�\������B
    print z[0] ,