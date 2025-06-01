import sys
from heapq import heappush, heappop

def main():
    input = sys.stdin.readline
    INF = 10**9
    directions = [(-1,0),(1,0),(0,-1),(0,1)]

    while True:
        X, Y = map(int, input().split())
        if X == 0 and Y == 0:
            break

        grid = [input().split() for _ in range(Y)]
        N = int(input())
        intervals = [[] for _ in range(10)]

        for i in range(N):
            g, d, s, e = map(int, input().split())
            if s < e:
                intervals[g].append((i, d, s, e))
        for lst in intervals:
            lst.sort(key=lambda x: x[1])

        max_state = 1 << N
        values = [0] * max_state
        for state in range(max_state):
            total = 0
            for lst in intervals:
                last_d = 0
                for i_, d_, s_, e_ in lst:
                    if state & (1 << i_):
                        last_d = d_
                total += last_d
            values[state] = total

        useful = [[None]*X for _ in range(Y)]
        start_x = start_y = 0
        for y in range(Y):
            for x in range(X):
                c = grid[y][x]
                if c.isdigit():
                    continue
                if c == 'P':
                    start_x, start_y = x, y
                s = set()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < X and 0 <= ny < Y:
                        nc = grid[ny][nx]
                        if nc.isdigit():
                            for iv in intervals[int(nc)]:
                                s.add(iv)
                useful[y][x] = s

        dist = [[[INF]*max_state for _ in range(X)] for _ in range(Y)]
        dist[start_y][start_x][0] = 0
        heap = [(0, 0, start_x, start_y)]

        while heap:
            cost, state, x, y = heappop(heap)
            if dist[y][x][state] < cost:
                continue

            for i_, d_, s_, e_ in useful[y][x]:
                if (state & (1 << i_)) == 0 and cost < e_:
                    new_cost = max(cost, s_)
                    new_state = state | (1 << i_)
                    if dist[y][x][new_state] > new_cost:
                        dist[y][x][new_state] = new_cost
                        heappush(heap, (new_cost, new_state, x, y))

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < X and 0 <= ny < Y and useful[ny][nx] is not None:
                    next_cost = cost + 1
                    if dist[ny][nx][state] > next_cost:
                        dist[ny][nx][state] = next_cost
                        heappush(heap, (next_cost, state, nx, ny))

        answer = 0
        for y in range(Y):
            for x in range(X):
                for state in range(max_state):
                    if dist[y][x][state] < INF:
                        if values[state] > answer:
                            answer = values[state]
        print(answer)

if __name__ == "__main__":
    main()