import sys
import heapq

input = sys.stdin.readline

N, R, L = map(int, input().split())
events = []
scores = [0]*(N+1)
appear = [0]*(N+1)
# Initially max is (score, -team_id) = (0, -1)
max_heap = []
for i in range(1, N+1):
    heapq.heappush(max_heap, (0, -i))
current_team = 1
last_time = 0

for _ in range(R):
    d,t,x = map(int, input().split())
    events.append((t,d,x))
events.append((L+1,0,0))  # sentinel to handle last segment easily

for t,d,x in events:
    duration = t - last_time
    appear[current_team] += duration
    last_time = t
    if d == 0:
        break
    # update the score of team d
    old_score = scores[d]
    new_score = old_score + x
    scores[d] = new_score
    # add new score to heap
    heapq.heappush(max_heap, (-new_score, -d))
    # pop out invalid top elements
    while True:
        s, neg_id = max_heap[0]
        team_id = -neg_id
        if scores[team_id] == -s:
            current_team = team_id
            break
        else:
            heapq.heappop(max_heap)

max_time = max(appear[1:])
res = 0
for i in range(1, N+1):
    if appear[i] == max_time:
        res = i
        break
print(res)