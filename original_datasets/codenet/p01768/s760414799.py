n = int(input())
dic = {}
price = []
for i in range(n):
  a, x = input().split()
  dic[a] = i
  price.append(int(x))

parent = [i for i in range(n)]

def find(x):
  if parent[x] == x:return x
  parent[x] = find(parent[x])
  return parent[x]

m = int(input())
for _ in range(m):
  s, t = input().split()
  si, ti = dic[s], dic[t]
  ps = find(si)
  pt = find(ti)
  parent[ps] = parent[pt]

groups = {}
for i in range(n):
  if find(i) in groups:
    min_price, cnt = groups[find(i)]
    groups[find(i)] = (min(min_price, price[i]), cnt + 1)
  else:
    groups[find(i)] = (price[i], 1)

print(sum([v[0] * v[1] for _, v in groups.items()]))