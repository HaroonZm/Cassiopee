from collections import deque
h,w,n = map(int,input().split())
factrys = [None] * (n + 1)
ss = ["X" * (w + 2)]
append = ss.append
for i in range(h):
  s = "X" + input() + "X"
  if "S" in s:
    factrys[0] = (i + 1, s.index("S"))
  for j in range(len(s)):
    if s[j] != 'S' and s[j] != '.' and s[j] != 'X':
      factrys[int(s[j])] = (i + 1, j)
  append(s)
append("X" * (w + 2))

def bfs(i):
  mp = [[None] * (w + 2) for j in range(h + 2)]
  x,y = factrys[i]
  que = deque()
  append = que.append
  popleft = que.popleft
  append((x, y))
  for count in range(10000000):
    sz = len(que)
    for loop in range(sz):
      (x,y) = popleft()
      if ss[x][y] == 'X' or mp[x][y] is not None:
        continue
      if (x,y) == factrys[i + 1]:
        return count
      mp[x][y] = count
      append((x + 1, y))
      append((x - 1, y))
      append((x, y + 1))
      append((x, y - 1))

ans = 0
for i in range(n):
  ret = bfs(i)
  if ret is not None:
    ans += ret
print(ans)