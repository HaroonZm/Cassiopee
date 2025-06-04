N=int(input())
A=list(map(int,input().split()))
def trier(L):
    L2=[]
    while L:
        m=min(L)
        L2.append(m)
        L.remove(m)
    return L2
A=trier(A)
i=0
total=0
while i<N:
    total=total+(A[i]-i-1)
    i+=1
print(total)