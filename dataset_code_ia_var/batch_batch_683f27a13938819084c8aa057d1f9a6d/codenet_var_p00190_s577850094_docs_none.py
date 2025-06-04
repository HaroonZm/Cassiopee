from heapq import heappush, heappop

comp = [(1, 1), (2, 1), (3, 1),
        (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
        (1, 3), (2, 3), (3, 3)]
numbers = range(11)
zeros = (11, 12)

def manhattan(v1, v2):
  x1, y1 = v1
  x2, y2 = v2
  return abs(x2 - x1) + abs(y2 - y1)

def heuristic(state):
  return sum([manhattan(state[i], comp[i]) for i in numbers])

def swaped(state, n1, n2):
  new_state = [i for i in state]
  new_state[n1], new_state[n2] = new_state[n2], new_state[n1]
  return tuple(new_state)

def main():
  while True:
    p1 = int(input())
    if p1 == -1:
      break
    l1 = [-1, -1, p1, -1, -1]
    l2 = [-1] + list(map(int, input().split())) + [-1]
    l3 = list(map(int, input().split()))
    l4 = [-1] + list(map(int, input().split())) + [-1]
    l5 = [-1, -1, int(input()), -1, -1]
    mp = [l1, l2, l3, l4, l5]
    init_state = [None] * 13
    for y in range(5):
      for x in range(5):
        if mp[y][x] != -1:
          if mp[y][x] == 0:
            if not init_state[11]:
              init_state[11] = (x, y)
            else:
              init_state[12] = (x, y)
          else:
            init_state[mp[y][x] - 1] = (x, y)
    init_state = tuple(init_state)
    dic = {}
    dic[init_state] = True
    que = []
    heappush(que, (heuristic(init_state) + 0, 0, init_state))
    while que:
      score, count, state = heappop(que)
      if score == count:
        print(count)
        break
      for z in zeros:
        for i in numbers:
          if manhattan(state[z], state[i]) == 1:
            new_state = swaped(state, i, z)
            if new_state not in dic:
              dic[new_state] = True
              new_score = heuristic(new_state) + count + 1
              if new_score <= 20:
                heappush(que, (new_score, count + 1, new_state))
    else:
      print("NA")

main()