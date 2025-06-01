N,M = map(int,input().split())
P = list(map(int,input().split()))
cs = [0] * N
prices = []
for _ in range(N-1):
  prices.append(list(map(int,input().split())))
for i in range(M-1):
  cur = P[i]
  nxt = P[i+1]
  cs[min(nxt-1, cur-1)] += 1
  cs[max(nxt-1, cur-1)] -= 1  
for i in range(N-1):
  cs[i+1] += cs[i]
res = 0
for i in range(N-1):
  times = cs[i]
  a,b,c = prices[i]
  res += min(a*times, b*times+c)
print(res)