def Q(x):
    print("?",x,flush=True)
    return int(input())

x=Q("A")
if x==128:
    L=128
else:    
    y=Q("A"*x)
    z=Q("A"*(x+1))

    if z==y:
        L=x+1
    else:
        L=x

S=[chr(i) for i in range(48,58)]+[chr(i) for i in range(65,91)]+[chr(i) for i in range(97,123)]
K=[-1]*62

for i in range(62):
    K[i]=L-Q(S[i]*L)

import heapq
A=[(K[i],S[i]*K[i]) for i in range(62)]
heapq.heapify(A)

while len(A)>1:
    x,y=heapq.heappop(A)
    if x==0:
        continue
    z,w=heapq.heappop(A)

    ind=0
    for i in range(len(w)):
        while Q(y[:ind]+w[i]+y[ind:])>=L-x-i:
            ind+=1
        y=y[:ind]+w[i]+y[ind:]
        ind+=1
    heapq.heappush(A,(x+z,y))
    
print("!",A[0][1],flush=True)