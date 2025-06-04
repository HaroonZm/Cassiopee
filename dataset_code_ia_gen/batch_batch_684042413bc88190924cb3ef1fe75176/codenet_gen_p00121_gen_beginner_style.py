from collections import deque
import sys

goal = (0,1,2,3,4,5,6,7)

moves = {
    0: [1,4],
    1: [0,2,5],
    2: [1,3,6],
    3: [2,7],
    4: [0,5],
    5: [1,4,6],
    6: [2,5,7],
    7: [3,6]
}

def bfs(start):
    start = tuple(start)
    if start == goal:
        return 0
    visited = set([start])
    queue = deque()
    queue.append((start,0))
    while queue:
        state, dist = queue.popleft()
        zero_pos = state.index(0)
        for nxt in moves[zero_pos]:
            new_state = list(state)
            new_state[zero_pos], new_state[nxt] = new_state[nxt], new_state[zero_pos]
            new_state_t = tuple(new_state)
            if new_state_t == goal:
                return dist+1
            if new_state_t not in visited:
                visited.add(new_state_t)
                queue.append((new_state_t, dist+1))
    return -1  # should not happen as problem states solvable

for line in sys.stdin:
    line=line.strip()
    if not line:
        continue
    cards = list(map(int,line.split()))
    print(bfs(cards))