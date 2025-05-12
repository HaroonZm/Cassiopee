N = int(input())
K = int(input())

A = list(map(int, input().split() ))

ans = 0

for x in A:
  ans += min(x, K-x) * 2
  
print(ans)