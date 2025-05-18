N, Q =map(int, input().split())

data = [0]*(N+1)
def add(k, x):
  while k <= N:
    data[k] += x
    k += k & -k
def get(k):
  s = 0
  while k:
    s += data[k]
    k -= k & -k
  return s

ans = []
for q in range(Q):
  a = input()
  if a[0] == "1":
    ans.append(str(get(int(a[2:]))))
  else:
    s, t, x = map(int, a[2:].split())
    add(s, x)
    if t < N:
      add(t+1, -x)
for i in ans:
  print(i)