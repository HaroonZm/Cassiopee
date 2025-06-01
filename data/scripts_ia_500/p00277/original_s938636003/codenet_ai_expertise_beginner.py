import sys
import heapq

def solve():
    input = sys.stdin
    first_line = input.readline()
    N, R, L = map(int, first_line.split())
    
    pq = []
    for i in range(1, N+1):
        pq.append([0, i, 0])
    heapq.heapify(pq)
    
    m = {}
    for i in range(N):
        m[pq[i][1]] = pq[i]
    
    pre_t = 0
    
    for line in input:
        d, t, x = map(int, line.split())
        
        team = pq[0]
        team[2] = team[2] + (t - pre_t)
        
        pre_t = t
        
        if team[1] == d:
            team[0] = team[0] - x
            if x < 0:
                heapq.heapreplace(pq, team)
        else:
            scored_team = m[d][:]
            scored_team[0] = scored_team[0] - x
            heapq.heappush(pq, scored_team)
            m[d][2] = -1
            m[d] = scored_team
        
        while pq[0][2] == -1:
            heapq.heappop(pq)
    
    pq[0][2] = pq[0][2] + (L - pre_t)
    
    ans_team = max(pq, key=lambda x : (x[2], -x[1]))
    print(ans_team[1])

solve()