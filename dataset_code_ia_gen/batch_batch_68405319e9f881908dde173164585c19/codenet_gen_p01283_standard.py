from math import log2
def entropy(arr):
    n=len(arr)
    if n==0:return 0
    freq=[0]*256
    for x in arr: freq[x]+=1
    h=0
    for c in freq:
        if c>0:
            p=c/n
            h-=p*log2(p)
    return h
while True:
    N=int(input())
    if N==0: break
    I=list(map(int,input().split()))
    M=256
    minH=float('inf')
    res=(0,0,0)
    for S in range(16):
        for A in range(16):
            for C in range(16):
                R=[0]*N
                R[0]=S
                for i in range(1,N): R[i]=(A*R[i-1]+C)%M
                O=[(I[i]^R[i]) for i in range(N)]
                h=entropy(O)
                if h<minH or (h==minH and (S,A,C)<res):
                    minH=h
                    res=(S,A,C)
    print(*res)