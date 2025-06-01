from heapq import heappop as pop
from heapq import heappush as push

def main():
  n, k = map(int, input().split())
  
  clst = []
  rlst = []
  
  for i in range(n):
    c, r = map(int, input().split())
    clst.append(c)
    rlst.append(r)
  
  edges = [[] * n for i in range(n)]
  
  for i in range(k):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append(b)
    edges[b].append(a)
  
  costs = [None] * n
  used = [False] * n
  
  def make_to_lst(s_num):
    loop = rlst[s_num]
    temp = set(edges[s_num])
    ret = set()
    while loop and temp:
      new = set()
      for p in temp:
        pto = set(edges[p])
        new = new | pto
      ret = ret | temp
      temp = new - ret
      loop -= 1
    return ret
  
  used[0] = True
  costs[0] = 0
  que = [(clst[0], 0)]
  
  while que:
    next_cost, s_num = pop(que)
    to_lst = make_to_lst(s_num)

    for num in to_lst:
      if num == n - 1:
        print(next_cost)
        return

      costs[num] = next_cost

      if not used[num]:
        push(que, (next_cost + clst[num], num))
        used[num] = True
  

main()