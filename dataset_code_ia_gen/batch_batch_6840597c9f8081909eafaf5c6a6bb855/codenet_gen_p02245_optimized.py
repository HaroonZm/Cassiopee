from collections import deque

def solve():
    start = tuple(int(x) for _ in range(3) for x in input().split())
    target = (1,2,3,4,5,6,7,8,0)
    moves = [(-1,0),(1,0),(0,-1),(0,1)]

    def neighbors(state):
        zero = state.index(0)
        x, y = divmod(zero, 3)
        for dx, dy in moves:
            nx, ny = x+dx, y+dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                nidx = nx*3 + ny
                lst = list(state)
                lst[zero], lst[nidx] = lst[nidx], lst[zero]
                yield tuple(lst)

    visited = set([start])
    queue = deque([(start,0)])
    while queue:
        state, dist = queue.popleft()
        if state == target:
            print(dist)
            return
        for nxt in neighbors(state):
            if nxt not in visited:
                visited.add(nxt)
                queue.append((nxt, dist+1))

solve()