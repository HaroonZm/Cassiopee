import sys
sys.setrecursionlimit(10**7)

def solve(max_roll, n, moves):
    end = n + 1
    # Compute next position after rolling i from position pos (0=start)
    def next_pos(pos, roll):
        p = pos + roll
        if p > end:
            p = end
        else:
            if 1 <= p <= n:
                mv = moves[p-1]
                if mv != 0:
                    p2 = p + mv
                    if mv > 0 and p2 > end:
                        p2 = end
                    if mv < 0 and p2 < 0:
                        p2 = 0
                    p = p2
        if p > end:
            p = end
        if p < 0:
            p = 0
        return p

    from collections import deque
    # Build graph: from each node, edges to next positions by each roll
    graph = [[] for _ in range(end+1)]
    for pos in range(end+1):
        if pos == end:
            continue
        for roll in range(1, max_roll+1):
            np = next_pos(pos, roll)
            graph[pos].append(np)

    # Detect if starting from 0, can get stuck in cycle not reaching end
    # Use DFS with coloring: 0=unvisited,1=visiting,2=done
    color = [0]*(end+1)
    def dfs(u):
        if u == end:
            return False
        if color[u] == 1:
            return True
        if color[u] == 2:
            return False
        color[u] = 1
        for w in graph[u]:
            if dfs(w):
                return True
        color[u] = 2
        return False

    # Additionally check reachability to end from 0:
    # If no path to end, then "NG"
    visited = [False]*(end+1)
    q = deque([0])
    visited[0] = True
    while q:
        u = q.popleft()
        if u == end:
            break
        for w in graph[u]:
            if not visited[w]:
                visited[w] = True
                q.append(w)
    if not visited[end]:
        return "NG"

    # Check cycles reachable from 0 not containing end
    if dfs(0):
        return "NG"
    else:
        return "OK"

input = sys.stdin.readline
while True:
    line = input()
    if not line:
        break
    max_roll = int(line)
    if max_roll == 0:
        break
    n = int(input())
    moves = [int(input()) for _ in range(n)]
    print(solve(max_roll, n, moves))