from collections import deque
n = input()
a = map(int, raw_input().split())

res = deque()

for i in range(n):
  if i % 2 == 0:
    res.appendleft(a[i])
  else:
    res.append(a[i])
if n % 2 == 0:
  print ' '.join(map(str, reversed(res)))
else:
  print ' '.join(map(str, res))