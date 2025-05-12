from collections import deque
from math import log2
ans = []
while True:
    N, M = map(int, input().split())
    if (N,M) == (0,0):
        break
    a,b,c = 0,0,0
    for i in range(3):
        A = list(map(int, input().split()))
        if A[0]!=0:
            if i==0:
                for j in range(A[0]):
                    a += 1<<(A[1+j]-1)
            elif i==1:
                for j in range(A[0]):
                    b += 1<<(A[1+j]-1)
            else:
                for j in range(A[0]):
                    c += 1<<(A[1+j]-1)

    d = deque([(0,a,b,c,'')])

    while len(d)>0:
        cnt,a,b,c,prev = d.popleft()
        if cnt>M:
            ans.append(-1)
            break
        if a+b==0 or b+c==0:
            ans.append(cnt)
            break
        if a==0:
            amax = -1
        else:
            amax = int(log2(a))
        if b==0:
            bmax = -1
        else:
            bmax = int(log2(b))
        if c==0:
            cmax = -1
        else:
            cmax = int(log2(c))
        if amax>bmax and prev!='ba':
            d.append((cnt+1,a-(1<<amax),b+(1<<amax),c,'ab'))
        elif amax<bmax and prev!='ab':
            d.append((cnt+1,a+(1<<bmax),b-(1<<bmax),c,'ba'))
        if cmax>bmax and prev!='bc':
            d.append((cnt+1,a,b+(1<<cmax),c-(1<<cmax),'cb'))
        elif cmax<bmax and prev!='cb':
            d.append((cnt+1,a,b-(1<<bmax),c+(1<<bmax),'bc'))
print(*ans, sep='\n')