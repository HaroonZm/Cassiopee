from functools import reduce
from collections import deque
from operator import add, mul
from itertools import product, combinations as C, permutations as P

import sys

class HeapQ(list):
    def __init__(self, *a): super().__init__(*a); self.heapified=False
    def push(self, x): super().append(x); from heapq import heappush; heappush(self, super().pop()) if self.heapified else None
    def pop(self): from heapq import heappop; return heappop(self) if self.heapified else super().pop()
    def heapify(self): from heapq import heapify as H; H(self); self.heapified=True

def _fast_input():
    global _fast
    try: return _fast
    except: pass
    import sys
    return sys.stdin.readline

def _fast_output(x):
    sys.stdout.write(str(x))

def solve():
    I = iter(lambda: _fast_input(), None)
    N = next(I)
    N = int(N.strip()) if hasattr(N,'strip') else int(N)
    S = next(I).strip()
    L = sum(map(lambda _:1, S))
    S+='+'
    if not(L&1) and N<10:
        _fast_output("-1\n"); return
    pw10 = reduce(lambda a,_,i=iter([1]):a+[a[-1]*10], range(10), [1])
    INF = N+1
    dist = [[INF for _ in range(L+2)] for _ in range(L+1)]
    ques = [HeapQ() for _ in range(L+1)]
    ques[0].append((0,0))
    dist[0][0]=0

    for k in range(L+1):
        que = ques[k]
        dist0 = dist[k]
        if not getattr(que,"heapified",False): que.heapify()
        while que:
            cost,i = que.pop()
            if dist0[i]<cost or i>L:continue
            p=S[i]
            if i+1!=L-1:
                if p!="+": 
                    v=int(p)
                    if S[i+1]!='+':
                        if cost+v < dist[k+1][i+2]:
                            dist[k+1][i+2]=cost+v;ques[k+1].append((cost+v,i+2))
                    else:
                        if cost+v<dist0[i+2]:
                            dist0[i+2]=cost+v
                            que.push((cost+v,i+2))
                if p!="0":
                    nk=k+1+(S[i+1]!='+')
                    if cost<dist[nk][i+2]:
                        dist[nk][i+2]=cost
                        ques[nk].append((cost,i+2))
            def calc(c0,p):
                for j in range(i+2,min(i+10,L+1)):
                    if j==L-1:continue
                    p1=p+S[i+1:j];l=j-i
                    c=c0+reduce(add,(x=="+" for x in p1),0)
                    v=int("".join(map(lambda x:[x],p1)).replace(*"+0"))
                    if v<=N:
                        nk=k+c+(S[j]!='+')
                        if cost+v<dist[nk][j+1]:
                            dist[nk][j+1]=cost+v; ques[nk].append((cost+v,j+1))
                    b=pw10[l-2]
                    for e in range(l-2,-1,-1):
                        a=(v//b)%10
                        if a:
                            v-=a*b;c+=1
                            if v<=N:
                                nk=k+c+(S[j]!='+')
                                if cost+v<dist[nk][j+1]:
                                    dist[nk][j+1]=cost+v
                                    ques[nk].append((cost+v,j+1))
                        b//=10
            if p not in "0+": calc(0,p)
            if p!="1": calc(1,"1")
        if dist0[L+1]<=N:
            _fast_output("%d\n"%k)
            break
solve()