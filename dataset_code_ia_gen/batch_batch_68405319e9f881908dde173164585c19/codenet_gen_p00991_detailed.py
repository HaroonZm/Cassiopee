import sys
from collections import deque

def main():
    input_data = sys.stdin.read().strip().split()
    r, c = int(input_data[0]), int(input_data[1])
    a1, a2 = int(input_data[2]), int(input_data[3])
    b1, b2 = int(input_data[4]), int(input_data[5])
    MOD = 100000007

    # Directions for movements: up, down, left, right
    # We'll consider wrapping for left-right and up-down edges
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Distance and ways arrays to store the shortest distance from start and
    # the number of shortest paths to each cell respectively
    dist = [[-1]*c for _ in range(r)]
    ways = [[0]*c for _ in range(r)]

    dist[a1][a2] = 0
    ways[a1][a2] = 1

    queue = deque()
    queue.append((a1, a2))

    while queue:
        x, y = queue.popleft()
        current_dist = dist[x][y]

        for dx, dy in directions:
            nx = (x + dx) % r  # wrapping in vertical direction
            ny = (y + dy) % c  # wrapping in horizontal direction

            # If this cell hasn't been visited yet, set distance and ways and enqueue it
            if dist[nx][ny] == -1:
                dist[nx][ny] = current_dist + 1
                ways[nx][ny] = ways[x][y]
                queue.append((nx, ny))
            # If we found another shortest path to an already visited cell,
            # add the number of ways accordingly
            elif dist[nx][ny] == current_dist + 1:
                ways[nx][ny] = (ways[nx][ny] + ways[x][y]) % MOD

    print(ways[b1][b2] % MOD)

if __name__ == "__main__":
    main()