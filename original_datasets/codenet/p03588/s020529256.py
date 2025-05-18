N=int(input())
A=sorted(list(map(int,input().split())) for _ in [0]*N)
print(sum(A[-1]))