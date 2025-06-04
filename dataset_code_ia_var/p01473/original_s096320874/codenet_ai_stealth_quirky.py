import math
import sys

Z = sys.stdin.readline().rstrip('\n')
LL = lambda X: sum(1 for _ in X)
QQ = set(tuple(Z))
AA = [Z.count(j) for j in QQ]
PP = list(map(lambda k: k % 2, AA))
nn = LL(Z)
bb = sum(PP)
final_word = lambda x, y: 0 if (x%2==0 and y!=0) or (x%2==1 and y!=1) else None

if (result := final_word(nn, bb)) is not None:
    print(result)
else:
    fudge = 1
    for aaa in AA:
        fudge *= math.factorial(aaa//2)
    print(math.factorial(nn//2)//fudge)