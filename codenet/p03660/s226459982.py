import queue

N = int(input())
ab = [list(map(int, input().split())) for _ in range(N - 1)]

T = {}
for a, b in ab:
  if a not in T:
    T[a] = [b]
  else:
    T[a].append(b)
  if b not in T:
    T[b] = [a]
  else:
    T[b].append(a)

R = [-1] * (N + 1)
q = queue.Queue()
put = q.put
get = q.get
put(1)
R[1] = 1
while not q.empty(): 
  t = get()
  if t in T:
    for i in T[t]:
      if R[i] == -1:
        R[i] = R[t] + 1
        put(i)

L = [N]
t = N
while t != 1:
  for i in T[t]:
    if R[i] < R[t]:
      L.append(i)
      t = i
      break

k = L[len(L) // 2 - 1]

cnt = 1
put(k)
while not q.empty(): 
  t = get()
  if t in T:
    for i in T[t]:
      if R[i] > R[t]:
        cnt += 1
        put(i)

Ans = ["Fennec", "Snuke"]
print(Ans[cnt >= N - cnt])