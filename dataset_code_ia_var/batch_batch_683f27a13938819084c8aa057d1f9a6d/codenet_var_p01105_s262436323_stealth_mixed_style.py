a = 65280
b = 61680
c = 52428
d, e = 43690, 65535

import heapq
X=[a, b, c, d, e, 0]
G = list(map(lambda t: (1, t), X))
F = dict(((x, 1) for x in X))
Y=[]
while len(G):
    z,p = heapq.heappop(G)
    if F[p]>z:pass
    elif F[p]<z:continue
    else:
        if z+1 < F.get(e^p,17):
            F[e^p]=z+1
            if z+1<16:G.append((z+1,e^p));heapq.heapify(G)
        if z+3<16:
            i=0
            while i<len(Y):
                q,r=Y[i];i+=1
                s=z+r+3
                if s>16:break
                for op in ('&','^'):
                    val=eval(f"p{op}q")
                    if s<F.get(val,17):
                        F[val]=s
                        if s<16:G+=[(s,val)];heapq.heapify(G)
        if z<7:Y.append((p,z))
from sys import stdin
w=stdin.read().replace("-","~").replace("*","&").replace("1e","")
W=w.split()
P = map(lambda x: e&int(x), W[:-1])
for v in P: print(F[v])