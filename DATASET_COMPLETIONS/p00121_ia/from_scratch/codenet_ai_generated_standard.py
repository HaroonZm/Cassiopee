from collections import deque
import sys

goal = (0, 1, 2, 3, 4, 5, 6, 7)
neighbors = {
    0: [1,4],
    1: [0,2,5],
    2: [1,3,6],
    3: [2,7],
    4: [0,5],
    5: [1,4,6],
    6: [2,5,7],
    7: [3,6],
}

def bfs(start):
    start = tuple(start)
    if start == goal:
        return 0
    queue = deque([(start, start.index(0), 0)])
    visited = {start}
    while queue:
        state, zero_pos, steps = queue.popleft()
        for nxt in neighbors[zero_pos]:
            new_state = list(state)
            new_state[zero_pos], new_state[nxt] = new_state[nxt], new_state[zero_pos]
            new_state = tuple(new_state)
            if new_state == goal:
                return steps + 1
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, nxt, steps+1))

for line in sys.stdin:
    if line.strip():
        puzzle = list(map(int, line.strip().split()))
        print(bfs(puzzle))