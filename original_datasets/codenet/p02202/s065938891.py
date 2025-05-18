n=int(input())
v=list(map(int,input().split()))
print(sum(v)-(n*(n+1)//2))