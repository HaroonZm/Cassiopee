from heapq import heappush, heappop
from string import digits
import sys

readline = sys.stdin.readline  # Function to read a line from stdin efficiently
write = sys.stdout.write       # Function to write output to stdout efficiently

# Directions for movement: up, left, down, right
dd = ((-1, 0), (0, -1), (1, 0), (0, 1))

INF = 10**9  # A large number representing infinity for initialization


def main():
    """
    Main function that reads multiple test cases representing a grid with special digits,
    processes intervals assigned to digits, and computes the maximum possible sum 
    of distances collected by visiting certain positions under time and interval constraints.
    
    The program reads until a line with two zeros is encountered, which signals the end.
    The core logic uses a shortest path search with bitmask dynamic programming and a priority queue.
    """
    while True:
        # Read grid dimensions: X is width, Y is height
        X, Y = map(int, readline().split())
        if X == 0 and Y == 0:
            # End of input
            break
        
        # Read the grid map as a list of lists of strings (each cell content)
        MP = [readline().split() for _ in range(Y)]
        
        # Number of intervals
        N = int(readline())
        
        # List of intervals associated with each digit from 0 to 9
        # I[g] will store a list of tuples (interval_index, distance, start_time, end_time)
        I = [[] for _ in range(10)]
        
        for i in range(N):
            # Read the interval information:
            # g: digit associated with the interval
            # d: distance value of the interval
            # s: start time (inclusive)
            # e: end time (exclusive)
            g, d, s, e = map(int, readline().split())
            if s < e:
                # Only consider valid intervals where start < end
                I[g].append((i, d, s, e))
        
        # Sort intervals associated with each digit by their distance d in ascending order
        for ss in I:
            ss.sort(key=lambda x: x[1])
        
        # Precompute the total distance for each subset of intervals, represented by a bitmask 'state'
        # V[state] will store the sum of distances considering the intervals included in 'state'
        V = [0] * (1 << N)
        for state in range(1 << N):
            total_distance = 0
            # For each digit's intervals
            for ss in I:
                x = 0
                # Traverse intervals of this digit, check if the current state includes the interval index
                for interval_index, d, s, e in ss:
                    if state & (1 << interval_index):
                        # Update x with d (distance) of the highest d interval enabled in this digit group
                        # Because intervals are sorted by d, this picks the greatest d for enabled intervals in this digit
                        x = d
                total_distance += x
            V[state] = total_distance
        
        # Prepare data structure U to store nearby intervals for each cell that does not contain a digit directly
        # U[y][x] will be a set of intervals (tuples) that can be triggered by stepping next to digits on the map
        U = [[None] * X for _ in range(Y)]
        
        # Variables to store start position (coordinates) where 'P' is found on the map
        sx = 0
        sy = 0
        
        # Analyze the grid to fill U and find the starting position
        for i in range(Y):
            for j in range(X):
                c = MP[i][j]
                # Skip cells that are digits because you cannot stand directly on digit cells
                if c in digits:
                    continue
                if c == 'P':
                    # Record starting position of player
                    sy = i
                    sx = j
                
                # Set of intervals triggered by standing at this cell (adjacent to digit cells)
                s = set()
                # Check adjacent cells for digits to gather intervals from
                for dx, dy in dd:
                    nx = j + dx
                    ny = i + dy
                    if not (0 <= nx < X and 0 <= ny < Y):
                        continue
                    c_adj = MP[ny][nx]
                    # If adjacent cell contains a digit, add all intervals for that digit to the set
                    if c_adj in digits:
                        digit_index = int(c_adj)
                        for e in I[digit_index]:
                            s.add(e)
                
                U[i][j] = s
        
        # Distance array D holds shortest time (distance) to reach each cell with any subset of intervals collected
        # Dimensions: Y x X x 2^N (for all subsets of intervals)
        # Initialized to INF
        D = [[[INF] * (1 << N) for _ in range(X)] for _ in range(Y)]
        
        # Priority queue for Dijkstra-like search on states (cost, state, x, y)
        que = []
        
        # Starting state: at position (sx, sy), no intervals collected, cost = 0
        D[sy][sx][0] = 0
        heappush(que, (0, 0, sx, sy))
        
        # Main loop: shortest path search over the augmented graph with bitmasks
        while que:
            cost, state, x, y = heappop(que)
            D0 = D[y][x]
            current_dist = D0[state]
            if current_dist < cost:
                # Already found better path to this state
                continue
            
            # Try to pick up new intervals that are available at this position and not yet picked
            for i_interval, d_interval, s_interval, e_interval in U[y][x]:
                # If current time is less than interval end and interval not collected in current state
                if current_dist < e_interval and (state & (1 << i_interval)) == 0:
                    # New time after waiting if needed; must wait until start time s_interval if current time is less
                    new_time = max(s_interval, current_dist)
                    new_state = state | (1 << i_interval)
                    if new_time < D0[new_state]:
                        # Update and push new state to queue
                        D0[new_state] = new_time
                        heappush(que, (new_time, new_state, x, y))
            
            # Try to move in all 4 directions if possible
            for dx, dy in dd:
                nx = x + dx
                ny = y + dy
                if not (0 <= nx < X and 0 <= ny < Y):
                    continue
                # Only move into cells where U is not None (not digit cells)
                if U[ny][nx] is None:
                    continue
                if current_dist + 1 < D[ny][nx][state]:
                    # Update distance with +1 time unit for moving
                    D[ny][nx][state] = current_dist + 1
                    heappush(que, (current_dist + 1, state, nx, ny))
        
        # After completion, find the maximum sum of distances (values in V) achievable on any cell with any subset of intervals
        ans = 0
        for x in range(X):
            for y in range(Y):
                D0 = D[y][x]
                for state in range(1 << N):
                    # If the cell is reachable with the subset 'state'
                    if D0[state] < INF:
                        ans = max(ans, V[state])
        
        # Output the result for this test case
        write("%d\n" % ans)


if __name__ == "__main__":
    main()