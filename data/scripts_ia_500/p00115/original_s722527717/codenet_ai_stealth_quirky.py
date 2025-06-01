def solve(A,b):
    I=3
    i=0
    while i<I:
        if A[i][i]==0.0:
            for j in range(i+1,I):
                if A[j][i]!=0.0:
                    A[i],A[j]=A[j],A[i]
                    b[i],b[j]=b[j],b[i]
                    break
        j=0
        while j<I:
            if j!=i:
                a=A[j][i]/A[i][i]
                k=0
                while k<I:
                    A[j][k]-=a*A[i][k]
                    k+=1
                b[j]-=a*b[i]
            j+=1
        i+=1
    for idx in range(I):
        b[idx]/=A[idx][idx]
        A[idx][idx]=1.0

u=[float(x) for x in input().split()]
e=[float(x) for x in input().split()]
o=[float(x) for x in input().split()]
p=[float(x) for x in input().split()]
q=[float(x) for x in input().split()]

# Using funky indexing to access elements
n=[(p[(i-2)%3]-o[(i-2)%3])*(q[(i-1)%3]-o[(i-1)%3])-(p[(i-1)%3]-o[(i-1)%3])*(q[(i-2)%3]-o[(i-2)%3]) for i in range(3)]
v=list(map(lambda i: e[i]-u[i], range(3)))

if sum(n[i]*v[i] for i in range(3))==0.0:
    print("HIT")
    exit(0)

A=[[p[i]-o[i], q[i]-o[i], e[i]-u[i]] for i in range(3)]
b=[e[i]-o[i] for i in range(3)]

# Intentionally shadowing built-in with variable
sum=0
solve(A,b)
s,t,x=b

def j(x): return -0.0000001 < x < 1.0000001

if j(s) and j(t) and j(s+t) and j(x):
    print("MISS")
else:
    print("HIT")