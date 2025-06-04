import sys
import heapq

# Directions are encoded as integers:
# 0: East, 1: South, 2: West, 3: North
# We'll represent movements accordingly.

# Movement vectors for each direction (dr, dc)
directions = [
    (0, 1),  # East
    (1, 0),  # South
    (0, -1), # West
    (-1, 0)  # North
]

def turn_from(direction, cmd):
    # Returns new direction after applying a turn command.
    # cmd: 0=Straight (no turn),
    #      1=Right (90 deg clockwise),
    #      2=Back (180 deg),
    #      3=Left (90 deg counterclockwise)
    return (direction + [0,1,2,3][cmd]) % 4

def solve():
    input_lines = sys.stdin.read().strip().split('\n')
    idx = 0
    # Parse input dataset by dataset
    while True:
        if idx >= len(input_lines):
            break
        w_h = input_lines[idx].split()
        idx += 1
        if len(w_h) < 2:
            continue
        w, h = map(int, w_h)
        if w == 0 and h == 0:
            break

        # Read the board commands: h rows each with w commands
        board = []
        for _ in range(h):
            row = list(map(int, input_lines[idx].split()))
            idx += 1
            board.append(row)

        # Read costs for commands Straight, Right, Back, Left
        costs = list(map(int, input_lines[idx].split()))
        idx += 1
        # costs[i]: cost for player's explicit command i
        # commands: 0=Straight,1=Right,2=Back,3=Left

        # The robot starts at (0,0) facing east (direction 0)
        # Goal is at (h-1, w-1). Halt command at goal square.

        # We want minimum cost to reach goal (h-1, w-1),
        # possibly overriding commands assigned to squares by explicit commands with costs.
        # No explicit Halt command allowed.

        # We model the state as (row, col, direction)
        # We use Dijkstra's algorithm to find minimal cost path.

        # Priority queue elements: (total_cost, r, c, direction)
        pq = []
        heapq.heappush(pq, (0, 0, 0, 0))  # start with cost 0

        # We'll keep a distance/cost array:
        # dist[r][c][d] = minimal cost to reach (r,c) facing d
        dist = [[[float('inf')] * 4 for _ in range(w)] for __ in range(h)]
        dist[0][0][0] = 0

        while pq:
            cost, r, c, d = heapq.heappop(pq)
            if dist[r][c][d] < cost:
                # Already found better path
                continue

            # If we reached goal at (h-1,w-1) and current square command is Halt (4),
            # the robot stops here successfully
            if r == h-1 and c == w-1:
                # The problem states a Halt command is assigned to goal square.
                # Because robot executes Halt automatically unless player overrides,
                # we can stop and print minimal cost.
                # We do NOT pay anything for Halt command since player can't give it.
                # So arriving at goal means we can output the cost.
                print(cost)
                break

            # Current square assigned command
            square_cmd = board[r][c]

            # We can either:
            # 1) Execute assigned command (no cost, no override)
            # 2) Override with one of (Straight, Right, Back, Left) commands (except Halt),
            #    paying the cost of the explicit command.

            # First, try executing assigned command as is:
            if square_cmd != 4:
                # If assigned command is Halt (4) but not goal position => fail scenario, don't move
                # Robot halts before goal -> lose -> don't consider this path further.
                # So only proceed if command != Halt (4)

                nd = turn_from(d, square_cmd)
                dr, dc = directions[nd]
                nr, nc = r + dr, c + dc

                # Check bounds
                if 0 <= nr < h and 0 <= nc < w:
                    if dist[nr][nc][nd] > cost:
                        dist[nr][nc][nd] = cost
                        heapq.heappush(pq, (cost, nr, nc, nd))
                # Else out of board => lose (discard path)

            # Second, try overriding with explicit command from player (except Halt)
            for player_cmd in range(4):
                # player_cmd: 0=Straight,1=Right,2=Back,3=Left
                nd = turn_from(d, player_cmd)
                dr, dc = directions[nd]
                nr, nc = r + dr, c + dc

                if 0 <= nr < h and 0 <= nc < w:
                    # Pay cost for overriding command
                    newcost = cost + costs[player_cmd]

                    if dist[nr][nc][nd] > newcost:
                        dist[nr][nc][nd] = newcost
                        heapq.heappush(pq, (newcost, nr, nc, nd))
                # else: out of board => lose

# Run the solver function
if __name__ == "__main__":
    solve()