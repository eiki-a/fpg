import sys
list1=sys.stdin.readlines()
list1[-1:]=[list1[len(list1)-1]+'\n'] # �z��̖����̗v�f�ɉ��s��������B

def qsort(arg): # �N�C�b�N�\�[�g���s���֐�qsort���`����B���X�g���̗v�f���擪�̗v�f���傫�����right�ɁA���������left�ɁA�����Ȃ��center�ɓn���Aright��left�ɍċA�I��qsort�������邱�Ƃ����ׂẴ��X�g�̗v�f����1�ȉ��ɂȂ�܂ő�����B
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

for x in qsort(list1): # �N�C�b�N�\�[�g�̌��ʂ�\������B
    print x ,