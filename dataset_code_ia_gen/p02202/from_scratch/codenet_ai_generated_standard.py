n=int(input())
v=sorted(map(int,input().split()),reverse=True)
print(sum(v[i]-i for i in range(n)))