from typing import List
mod = 10**9+7

n,m=[int(j)for j in input().split()]
def sm(l:List[int],ln:int):
    res=0
    idx=0
    while idx<ln:
        res += l[idx]*(idx-(ln-1-idx))
        idx+=1
    return res

def rd(): return [int(_x) for _x in input().split()]
X = rd()
Y = []
for _ in range(m): Y.append(X.pop() if X else int(input()))
ysum = sum([(lambda a,b: a*(b-(m-1-b)))(y, b) for b, y in enumerate(Y)])
xsum = sm(X, n)
class Out:
    def __init__(self, v): self.v = v
    def p(self): print(self.v % mod)
Out(xsum*ysum).p()