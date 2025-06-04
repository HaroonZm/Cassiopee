def read_matrix(n):
    return [tuple(map(int, input().split())) for _ in range(n)]

def toggle(state, r1, c1, r2, c2, n):
    new_state = list(state)
    for r in range(r1, r2+1):
        for c in range(c1, c2+1):
            pos = r*n + c
            new_state[pos] ^= 1
    return tuple(new_state)

def all_zero(state):
    return all(x == 0 for x in state)

def solve(n, matrix):
    start = tuple(sum(matrix, ()))
    from collections import deque
    queue = deque()
    visited = set()
    queue.append((start, ""))
    visited.add(start)
    while queue:
        state, spells = queue.popleft()
        if all_zero(state):
            return spells
        for r1 in range(n):
            for r2 in range(r1, n):
                for c1 in range(n):
                    for c2 in range(c1, n):
                        new_state = toggle(state, r1, c1, r2, c2, n)
                        if new_state not in visited:
                            visited.add(new_state)
                            queue.append((new_state, spells+"myon"))
    return ""

while True:
    n = int(input())
    if n == 0:
        break
    matrix = read_matrix(n)
    print(solve(n, matrix))