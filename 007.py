import sys
list=[0]
def search(arg, var, con): # ���X�garg�̒���con�Ɠ��������܂܂�Ă��Ȃ����arg��con��ǉ�����֐�search���`�B�ucon���傫�ȗv�f��arg�ɂ���΁A���̒��O�ɒǉ��v�Ƃ��邱�Ƃŏ��������ɕ��ׂĂ����B
    if (arg[var]<con and var+1<len(arg)):
        search(arg, var+1, con)
    elif arg[var]==con:
        pass
    else:
        arg.insert(var, con)

for x in sys.stdin.readlines():
    search(list, 0, len(x.split('\t')[0])) # 1�R�����ڂ̕�����̒�����split�ŏE���Asearch�֐��ɓn���B

print len(list)-1 # list�ɂ͍ŏ�����v�f��1�����Ă�������-1�����l�������ƂȂ�B