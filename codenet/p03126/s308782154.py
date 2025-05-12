import collections

N, M = map(int, input().split())
x = []
for n in range(N):
  l = list(set(list(map(int, input().split()))[1:]))
  #print(l)
  x.extend(l)
  
c = collections.Counter(x)

ans = 0
for k in c.keys():
  if c[k] == N:
    ans += 1
print(ans)