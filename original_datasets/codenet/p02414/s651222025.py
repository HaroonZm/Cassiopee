A=[]
B=[]
n,m,l=map(int,input().split())
for i in range(n):
    A.append(list(map(int,input().split())))
for j in range(m):
    B.append(list(map(int,input().split())))
for i in range(n):
    C=[]
    for j in range(l):
        a=0
        for k in range(m):
            a+=A[i][k]*B[k][j]
        C.append(a)
    print(' '.join(map(str,C)))