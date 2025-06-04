import sys
import heapq

input = sys.stdin.readline
N, C = map(int, input().split())
scores = [0]*(N+1)
heap = []
# Initialize heap with all teams: (-score, team_id)
for i in range(1, N+1):
    heapq.heappush(heap, (0, i))

for _ in range(C):
    cmd = input().split()
    if cmd[0] == '0':
        t, p = int(cmd[1]), int(cmd[2])
        scores[t] += p
        # Push new state
        heapq.heappush(heap, (-scores[t], t))
    else:
        m = int(cmd[1])
        # Using a heap with lazy deletion, pop until find the latest score for team
        tmp = []
        cnt = 0
        while cnt < m:
            s, t = heapq.heappop(heap)
            # Check if this is latest score for t
            if -s == scores[t]:
                cnt += 1
                if cnt == m:
                    ans = (t, scores[t])
                    tmp.append((s, t))
                    break
            tmp.append((s, t))
        # Push back all popped items
        for item in tmp:
            heapq.heappush(heap, item)
        print(ans[0], ans[1])