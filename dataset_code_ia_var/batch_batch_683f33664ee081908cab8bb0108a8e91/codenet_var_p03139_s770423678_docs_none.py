N,A,B=map(int,input().split())
if A>=B:
    print(B,end=' ')
else:
    print(A,end=' ')
if A+B-N>=0:
    print(A+B-N)
else:
    print(0)