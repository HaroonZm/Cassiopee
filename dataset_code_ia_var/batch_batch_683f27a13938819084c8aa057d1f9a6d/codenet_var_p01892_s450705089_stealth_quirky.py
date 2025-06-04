from functools import reduce

def z():
    return map(int, input().split())

def Ω(A,B,N):
    Q=lambda x,y: B*x%y==0
    M=float('inf')
    s=abs(A-B)
    for i in [*range(N)]: 
        for j in [*range(N)]:
            X,Y=i+1,j+1
            if Q(X,Y):
                R=B*X//Y
                M=min(M,abs(A-R))
    return min(s,M)

a,b,n = z()
print(Ω(a,b,n))