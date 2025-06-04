from collections import deque

def solve_cleaning_robot():
    # Directions for robot movement: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while True:
        w, h = map(int, input().split())
        if w == 0 and h == 0:
            break

        room = [list(input()) for _ in range(h)]
        # List to store positions of dirty tiles and robot start position
        dirty_positions = []
        robot_pos = None

        # Parse the map, identify robot and dirty tiles
        for y in range(h):
            for x in range(w):
                if room[y][x] == 'o':
                    robot_pos = (y, x)
                elif room[y][x] == '*':
                    dirty_positions.append((y, x))

        # If no dirty tiles, 0 moves required
        if not dirty_positions:
            print(0)
            continue

        # Assign indices to dirty tiles and store positions in order:
        # index 0: robot start position, index 1..n: dirty tiles
        points = [robot_pos] + dirty_positions
        n = len(dirty_positions)

        # Precompute shortest distances between all points of interest using BFS
        dist = [[-1]*(n+1) for _ in range(n+1)]

        def bfs(start_y, start_x):
            # BFS to find minimum moves to all accessible tiles from (start_y, start_x)
            queue = deque()
            queue.append((start_y, start_x))
            visited = [[-1]*w for _ in range(h)]
            visited[start_y][start_x] = 0
            while queue:
                y, x = queue.popleft()
                for dy, dx in directions:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < h and 0 <= nx < w:
                        if room[ny][nx] != 'x' and visited[ny][nx] == -1:
                            visited[ny][nx] = visited[y][x] + 1
                            queue.append((ny, nx))
            return visited

        # For each point of interest, run BFS and store distances to others
        visited_list = []
        for i in range(n+1):
            y, x = points[i]
            visited_list.append(bfs(y, x))

        # Fill dist matrix with point-to-point distances
        possible = True
        for i in range(n+1):
            for j in range(n+1):
                if i == j:
                    dist[i][j] = 0
                else:
                    py, px = points[j]
                    dist[i][j] = visited_list[i][py][px]
                    if dist[i][j] == -1 and j != 0:
                        # If any dirty tile is unreachable from a point, problem has no solution
                        possible = False

        if not possible:
            print(-1)
            continue

        # We need to find minimum moves to cover all dirty tiles starting from robot_pos (index 0)
        # This is a Travelling Salesman Problem (TSP) variant with up to 10 dirty tiles
        # State: bitmask of visited dirty tiles and current position
        # DP to store minimal cost to cover visited tiles ending at position pos
        max_state = 1 << n  # bitmask for n dirty tiles
        dp = [[-1]*(n+1) for _ in range(max_state)]
        # Initialize dp: starting position, no dirty tiles cleaned yet
        dp[0][0] = 0

        for state in range(max_state):
            for pos in range(n+1):
                if dp[state][pos] == -1:
                    continue
                # Try to visit a new dirty tile next
                for next in range(1, n+1):
                    if not (state & (1 << (next-1))):
                        # If not visited this dirty tile yet
                        if dist[pos][next] != -1:
                            next_state = state | (1 << (next-1))
                            new_cost = dp[state][pos] + dist[pos][next]
                            if dp[next_state][next] == -1 or dp[next_state][next] > new_cost:
                                dp[next_state][next] = new_cost

        # Find minimal cost to visit all dirty tiles (all bits set)
        ans = -1
        final_state = max_state - 1
        for pos in range(1, n+1):
            if dp[final_state][pos] != -1:
                if ans == -1 or ans > dp[final_state][pos]:
                    ans = dp[final_state][pos]

        print(ans)