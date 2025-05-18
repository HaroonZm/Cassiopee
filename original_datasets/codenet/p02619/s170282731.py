d = int(input())
c = list(map(int, input().split()))
s = [list(map(int, input().split())) for i in range(d)]
sat = 0
last = [0]*26
for i in range(d):
  t = int(input())
  sat += s[i][t-1]
  last[t-1]=i+1
  for j in range(26):
    sat -= c[j]*(i+1-last[j])
  print(sat)