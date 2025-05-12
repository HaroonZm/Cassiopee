n, m = map(int,input().split())
l = [0 for i in range(m)]
for i in range(n):
  s = list(map(int, input().split()))
  for j in range(1, s[0]+1):
    l[s[j]-1] += 1
l = list(map(lambda x: x//n, l))
print(sum(l))