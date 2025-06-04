Z = int(input())
def R(x):return list(map(int,x.split()))
A = R(input())
Q = [A[0]] + [0]*(Z-1)
for e in range(1,Z):Q[e]=A[e]+Q[e-1]
Y = lambda i: 1-(Q[i]+o) if Q[i]+o<=0 else 0
W = lambda i: (Q[i]+o+1) if Q[i]+o>=0 else 0

ans_up,ans_dn,o=0,0,0
for t in range(Z):
    # up
    if not t%2:
        if Q[t]+o<=0: ans_up += 1-(Q[t]+o); o+=1-(Q[t]+o)
    else:
        if Q[t]+o>=0: ans_up += Q[t]+o+1; o-=Q[t]+o+1
d=0
for t in range(Z):
    # down
    if t%2:
        if Q[t]+d<=0: ans_dn += 1-(Q[t]+d); d+=1-(Q[t]+d)
    else:
        if Q[t]+d>=0: ans_dn += Q[t]+d+1; d-=Q[t]+d+1
print(ans_up if ans_up<ans_dn else ans_dn)