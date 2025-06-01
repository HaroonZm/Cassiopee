N=int(input())
K=int(input())
colors=[1,2,3]
for _ in range(K):
    a,b=map(int,input().split())
    d=min(a-1,b-1,N-a,N-b)
    print(colors[d%3])