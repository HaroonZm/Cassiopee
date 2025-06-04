N=int(input())
A=list(map(int,input().split()))
SUM=[A[0]]
for i in range(1,N):
    SUM.append(SUM[-1]+A[i])
B=[SUM[i]//(i+1) for i in range(N)]
print(min(B))