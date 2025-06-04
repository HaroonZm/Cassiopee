from collections import deque
from sys import stdin

def print_table(t):
    print('\n'.join(''.join(map(str, row)) for row in t))

def play(t, x, y):
    n, m = len(t), len(t[0])
    directions = [(dx, 0) for dx in range(-3, 4) if dx] + [(0, dy) for dy in range(-3, 4) if dy]
    q = deque([(x, y)])
    while q:
        cx, cy = q.popleft()
        t[cy][cx] = 0
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < m and 0 <= ny < n and t[ny][nx] == 1:
                t[ny][nx] = 0
                q.append((nx, ny))
    return t

def main():
    get_input = iter(stdin.read().split())
    n = int(next(get_input))
    for i in range(1, n + 1):
        next(get_input)  # skip line
        t = [[int(c) for c in next(get_input)] for _ in range(8)]
        x = int(next(get_input)) - 1
        y = int(next(get_input)) - 1
        tt = play(t, x, y)
        print(f'Data {i}:')
        print_table(tt)

if __name__ == "__main__":
    main()