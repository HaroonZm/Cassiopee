import sys
from collections import deque

# Pyonkichi's jump relative moves
JUMP_MOVES = [(2, 1), (2, -1), (-2, 1), (-2, -1),
              (1, 2), (1, -2), (-1, 2), (-1, -2)]

# Check in range 0~9 for park field
def in_park(x, y):
    return 0 <= x <= 9 and 0 <= y <= 9

# Sprinkler's water coverage relative moves including itself
WATER_COVERAGE = [
    (0,0),(0,1),(0,-1),(1,0),(-1,0),
    (1,1),(1,-1),(-1,1),(-1,-1)
]

def solve(px, py, n, sprinklers):
    # Compute sprinkler water coverage sets for each sprinkler
    water_areas = []
    for (sx, sy) in sprinklers:
        area = set()
        for dx, dy in WATER_COVERAGE:
            nx, ny = sx + dx, sy + dy
            if in_park(nx, ny):
                area.add((nx, ny))
        water_areas.append(area)
    # BFS state: index in sprinklers, position of Pyonkichi
    # At sprinkler i, Pyonkichi jumps once from previous pos to pos in water area of sprinkler i
    # For i=0, Pyonkichi jumps from initial pos to pos in water area of first sprinkler
    # At transition from sprinkler i to i+1, one jump allowed, then stay fixed at that pos until next sprinkler start
    # Whether there is a path that for all sprinklers Pyonkichi can be within water coverage by single jump at each transition.

    # Since Pyonkichi's jump is always one of the 8 L-shaped knight moves with length fixed,
    # from previous position, he must jump exactly one of JUMP_MOVES and land inside the sprinkler coverage

    # We'll use a queue for BFS, storing (index_sprinkler, x, y)
    # index_sprinkler is the sprinklers step 0-based
    # For first step, Pyonkichi jumps from initial position to some pos in water_areas[0] reachable by one jump move

    queue = deque()
    visited = [set() for _ in range(n)]  # visited positions per sprinkler index

    # For first sprinkler, jump from initial pos to reachable watering pos
    for dx, dy in JUMP_MOVES:
        nx, ny = px + dx, py + dy
        if in_park(nx, ny) and (nx, ny) in water_areas[0]:
            queue.append((0, nx, ny))
            visited[0].add((nx, ny))

    while queue:
        i, x, y = queue.popleft()
        if i == n - 1:
            # Reached last sprinkler with valid position
            return "OK"
        # Next sprinkler index
        ni = i + 1
        # From current position (x, y), Pyonkichi can jump once to pos inside water_areas[ni]
        for dx, dy in JUMP_MOVES:
            nx, ny = x + dx, y + dy
            if in_park(nx, ny) and (nx, ny) in water_areas[ni]:
                if (nx, ny) not in visited[ni]:
                    visited[ni].add((nx, ny))
                    queue.append((ni, nx, ny))
    # No path found
    return "NA"

def main():
    input_lines = sys.stdin.read().split()
    idx = 0
    while True:
        if idx + 2 > len(input_lines):
            break
        px = int(input_lines[idx]); py = int(input_lines[idx+1])
        idx += 2
        if px == 0 and py == 0:
            break
        n = int(input_lines[idx])
        idx += 1
        sprinklers = []
        for _ in range(n):
            x = int(input_lines[idx]); y = int(input_lines[idx+1])
            idx += 2
            sprinklers.append((x, y))
        print(solve(px, py, n, sprinklers))

if __name__ == "__main__":
    main()