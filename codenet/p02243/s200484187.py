import sys
from heapq import *

MAX_INT= 10 ** 10

n = int(input())
adj_list = []

for _ in range(n):
  commands = sys.stdin.readline().split()
  lst = [ commands[i:i+2] for i in range(2, len(commands), 2)]
  adj_list.append(lst)

def dijkstra():
  # initialization
  visited = [False] * n
  dist_arr = [MAX_INT] * n
  pq = []
  prev = [None] * n

  # append 0 to pqs
  pq = [(0, 0)]
  dist_arr[0] = 0

  while len(pq) > 0:
    dist, idx = heappop(pq)
    visited[idx] = True

    # updating current values in dist
    for edge in adj_list[idx]:
      cur_idx, cur_dist = [ int(e) for e in edge]
      if visited[cur_idx]: continue

      new_dist = dist + cur_dist

      if new_dist < dist_arr[cur_idx]:
        dist_arr[cur_idx] = new_dist
        heappush(pq, (dist_arr[cur_idx], cur_idx))

  return dist_arr

distArr = dijkstra()
for i in range(n):
  print(i, distArr[i])