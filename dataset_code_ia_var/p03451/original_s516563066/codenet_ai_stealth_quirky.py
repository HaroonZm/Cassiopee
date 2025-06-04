import sys
N = int(sys.stdin.readline())

def R(): return list(map(int, sys.stdin.readline().split()))
class Acc:
    def __call__(self,lst):
        s=0
        res=[]
        for x in lst:
            s+=x
            res.append(s)
        return res

U = R()
V = R()[::-1]

acc = Acc()
U_acc = acc(U)
V_acc = acc(V)[::-1]

ans = None
for i,j in zip(U_acc,V_acc):
    cur = i+j
    if ans is None or cur > ans:
        ans = cur

print(ans)