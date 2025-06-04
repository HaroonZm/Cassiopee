from collections import deque
import sys

goal = "01234567"
moves = {
    0: [1, 4],
    1: [0, 2, 5],
    2: [1, 3, 6],
    3: [2, 7],
    4: [0, 5],
    5: [1, 4, 6],
    6: [2, 5, 7],
    7: [3, 6],
}

def bfs(start):
    if start == goal:
        return 0
    visited = set([start])
    queue = deque([(start, start.index('0'), 0)])
    while queue:
        state, zero_pos, dist = queue.popleft()
        for nxt in moves[zero_pos]:
            lst = list(state)
            lst[zero_pos], lst[nxt] = lst[nxt], lst[zero_pos]
            new_state = ''.join(lst)
            if new_state == goal:
                return dist + 1
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, nxt, dist + 1))

for line in sys.stdin:
    s = line.strip()
    if not s:
        continue
    start = ''.join(s.split())
    print(bfs(start))