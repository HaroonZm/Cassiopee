import sys
import heapq

def read_ints():
    return list(map(int, sys.stdin.readline().split()))

def solve(H, W, A):
    max_dist = H * W
    # Create a 3D list initialized with None
    visited = [[[None] * (max_dist + 1) for _ in range(W)] for _ in range(H)]

    best_cost = 1 << 63
    queue = []
    heapq.heappush(queue, (0, 0, 0, 0))  # cost, distance, x, y

    while queue:
        cost, dist, x, y = heapq.heappop(queue)

        if x == W - 1 and y == H - 1:
            if cost - dist < best_cost:
                best_cost = cost - dist

        if visited[y][x][dist] is not None:
            continue

        for d in range(dist, max_dist + 1):
            if visited[y][x][d] is not None:
                break
            visited[y][x][d] = cost

        if cost - max_dist >= best_cost:
            break

        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            nx = x + dx
            ny = y + dy

            if nx < 0 or nx >= W or ny < 0 or ny >= H:
                continue

            ndist = dist + 1
            if ndist > max_dist:
                continue

            ncost = cost + A[ny][nx] * (1 + dist * 2) + 1

            if visited[ny][nx][ndist] is None:
                heapq.heappush(queue, (ncost, ndist, nx, ny))

    return best_cost

def main():
    H, W = read_ints()
    A = []
    for _ in range(H):
        row = read_ints()
        A.append(row)

    result = solve(H, W, A)
    print(result)

if __name__ == "__main__":
    main()