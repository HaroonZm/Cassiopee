m,n=map(int,input().split())
print(max(sum(map(int,input().split())) for _ in range(m)))