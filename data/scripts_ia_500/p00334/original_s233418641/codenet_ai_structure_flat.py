N=int(input())
A=[]
for _ in range(N):
    a=list(map(int,input().split()))
    a.sort()
    if a not in A:
        A.append(a)
print(N-len(A))