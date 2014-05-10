import sys
list=[0]
def search(arg, var, con): # リストargの中にconと同じ数が含まれていなければargにconを追加する関数searchを定義。「conより大きな要素がargにあれば、その直前に追加」とすることで小さい順に並べていく。
    if (arg[var]<con and var+1<len(arg)):
        search(arg, var+1, con)
    elif arg[var]==con:
        pass
    else:
        arg.insert(var, con)

for x in sys.stdin.readlines():
    search(list, 0, len(x.split('\t')[0])) # 1コラム目の文字列の長さをsplitで拾い、search関数に渡す。

print len(list)-1 # listには最初から要素が1つ入っていたため-1した値が答えとなる。