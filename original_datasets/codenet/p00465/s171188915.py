from heapq import heappop as pop
from heapq import heappush as push
INF = 1000000000000

def bfs(lst, used, que, w, h):
  v, y, x  = pop(que)
  if y > 0 and not used[y - 1][x]:
    push(que, (lst[y - 1][x], y - 1, x))
    used[y - 1][x] = True
  if h > y + 1 and not used[y + 1][x]:
    push(que, (lst[y + 1][x], y + 1, x))
    used[y + 1][x] = True
  if x > 0 and not used[y][x - 1]:
    push(que, (lst[y][x - 1], y, x - 1))
    used[y][x - 1] = True
  if w > x + 1 and not used[y][x + 1]:
    push(que, (lst[y][x + 1], y, x + 1))
    used[y][x + 1] = True
  return v

def make_dic(lst, w, h, x, y):
  que = [(1, y, x)]
  used = [[False] * w for _ in range(h)]
  used[y][x] = True
  dic = [[0, 0]]
  app = dic.append
  Max = 0
  acc = 0

  while que:
    v = bfs(lst, used, que, w, h)
    acc += 1
    if v > Max:
      app([v, acc])
      Max = v
    else:
      dic[-1][1] += 1
  return dic

def solve():
  while True:

    R = int(input())
    if not R:
      break

    w1, h1, x1, y1 = map(int, input().split())
    x1 -= 1
    y1 -= 1
    lst1 = [list(map(int, input().split())) for _ in range(h1)]
    used1 = [[False] * w1 for _ in range(h1)]
  
    w2, h2, x2, y2 = map(int, input().split())
    x2 -= 1
    y2 -= 1
    lst2 = [list(map(int, input().split())) for _ in range(h2)]
    used2 = [[False] * w2 for _ in range(h2)]
  
    dic1 = make_dic(lst1, w1, h1, x1, y1)
    dic2 = make_dic(lst2, w2, h2, x2, y2)
  
    end1 = len(dic1)
    end2 = len(dic2)
    ind1 = 0
    ind2 = end2 - 1
    ans = INF
  
    while ind1 < end1 and ind2 > 0:
      r1, sum1 = dic1[ind1]
      r2, sum2 = dic2[ind2]
  
      if sum1 + sum2 < R:
        ind1 += 1
        continue
  
      while ind2 > 0 and sum1 + sum2 >= R:
        ind2 -= 1
        r2, sum2 = dic2[ind2]
  
      if ind2 == 0 and sum1 + sum2 >= R:
        rs = r1 + r2
        if rs < ans:
          ans = rs
        break
  
      else:
        if ind2 < end2 - 1:
          ind2 += 1
        r2 = dic2[ind2][0]
        rs = r1 + r2
        if rs < ans:
          ans = rs
  
      ind1 += 1
    print(ans)
 
solve()