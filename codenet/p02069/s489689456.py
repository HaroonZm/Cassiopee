import heapq
import sys
from operator import itemgetter

input = sys.stdin.readline
N, L = map(int, input().split())
LR = []
LR_set = []
for _ in range(N):
  l, r = map(int, input().split())
  LR.append((l, r))
  LR_set.append(l)
  LR_set.append(r)
LR_set = sorted(set(LR_set))
mapping = {}
# zahyou asshuku
for i, lr in enumerate(LR_set):
  mapping[lr] = i

imos = [0] * (len(mapping)+1)

LR.sort(key=itemgetter(0))
q = []
ans_x = 0
right = 0
for i, (l, r) in enumerate(LR, 1):
  # x
  heapq.heappush(q, -r)
  #print(q, right, ans_x)
  if i<N and LR[i][0] > right:
    rr = heapq.heappop(q)
    rr = -rr
    right = rr
    ans_x += 1

  # y
  imos[mapping[l]] += 1
  imos[mapping[r]] -= 1

if L > right:
  ans_x += 1

for i in range(1, len(imos)):
  imos[i] += imos[i-1]

ans_y = N + 1 - min(imos[:mapping[L]])

print(ans_x, ans_y)