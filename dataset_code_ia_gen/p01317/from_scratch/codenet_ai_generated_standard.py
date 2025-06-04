import sys
import heapq

def dijkstra(graph, start):
    n = len(graph)
    dist = [float('inf')] * n
    dist[start] = 0
    hq = [(0, start)]
    while hq:
        cd, u = heapq.heappop(hq)
        if dist[u] < cd:
            continue
        for v, cost in graph[u]:
            nd = cd + cost
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(hq, (nd, v))
    return dist

def solve():
    input = sys.stdin.readline
    while True:
        N, M = map(int, input().split())
        if N == 0 and M == 0:
            break
        # build graphs
        land_graph = [[] for _ in range(N)]
        sea_graph = [[] for _ in range(N)]
        for _ in range(M):
            x, y, t, sl = input().split()
            x = int(x)-1
            y = int(y)-1
            t = int(t)
            if sl == 'L':
                land_graph[x].append((y, t))
                land_graph[y].append((x, t))
            else:  # 'S'
                sea_graph[x].append((y, t))
                sea_graph[y].append((x, t))
        R = int(input())
        seq = list(map(int, input().split()))
        seq = [z-1 for z in seq]

        # precompute all-pairs shortest using only land and only sea edges with dijkstra
        # we only need distances between points used in seq (and initial position)
        # but for simplicity precompute all nodes' distances from all points in seq plus ones needed
        # To minimize computations, precompute dijkstra from all unique cities in seq and from initial location.

        # we need to answer queries of form: from town u with ship on land or sea to town v with ship on land or sea.
        # State is: current node, whether ship is with postman (=1) or at some node with ship
        # Actually, ship can only be at a port town initially and when traveling by sea.
        # From explanation: One can travel by any path but:
        # if traveling by sea, ship moves to the destination node; if traveling by land, ship stays put at previous sea position.
        # Actually, per problem, the key is that ship is either with postman or left somewhere.
        # To travel by sea, ship must be where postman is.
        # To travel by land, postman moves alone, ship stays where it was.

        # Thus, for path from current node to next target with ship status:
        # We represent DP states: (pos, ship_pos), where ship_pos= node where ship is located (0<=ship_pos<N), or ship_pos=pos if ship is with postman.

        # But initial ship_pos = seq[0], ship at starting port.

        # For each move in delivery sequence:
        # Moving from seq[i] to seq[i+1]:

        # The postman must move from current pos to next pos, maintaining ship constraints:
        # The ship is either with postman, or in a port node.

        # For traveling on land, postman moves, ship remains at ship_pos
        # For traveling on sea, postman and ship move together; after trip ship_pos = new pos.

        # We will perform a modified dijkstra for each move, on states: (pos, ship_pos)
        # transitions:
        # - land edges: pos->pos', cost t, ship_pos unchanged
        # - sea edges: can only be used if pos == ship_pos (ship moves with postman)
        #   pos->pos', cost t, ship_pos updated to pos'

        # initial state: (start_pos, ship_pos = start_pos)
        # goal: pos = next delivery town (ship_pos any)
        # minimal cost among all states where pos = next town delivered.

        # Since N=200, state space N*N=40,000 manageable for each step, R<=1000 steps, but must be optimized.

        # We'll keep DP per step:
        # For each step, run dijkstra from (start_pos, ship_pos) to get min cost to next position pos=seq[i+1]

        # To optimize further, precompute adjacency separately:
        # land_adj[pos] = list of (neighbor, cost)
        # sea_adj[pos] = list of (neighbor, cost)

        # Then do multi-state dijkstra on (pos, ship_pos)

        # Implementation:

        # Build adjacency lists
        land_adj = land_graph
        sea_adj = sea_graph

        current_states = {(seq[0], seq[0]): 0}  # dict (pos,ship_pos):cost
        for i in range(R-1):
            start = seq[i]
            goal = seq[i+1]
            dist = {}
            hq = []
            for s, c in current_states.items():
                heapq.heappush(hq, (c, s[0], s[1]))
                dist[(s[0], s[1])] = c
            while hq:
                cd, pos, ship_pos = heapq.heappop(hq)
                if dist[(pos, ship_pos)] < cd:
                    continue
                if pos == goal:
                    # can finish early since we want min dist to goal; but can't stop early because need minimal for all states
                    pass
                # land moves
                for nx, cost in land_adj[pos]:
                    nstate = (nx, ship_pos)
                    nd = cd + cost
                    if nstate not in dist or dist[nstate] > nd:
                        dist[nstate] = nd
                        heapq.heappush(hq, (nd, nx, ship_pos))
                # sea moves (only if ship with postman)
                if pos == ship_pos:
                    for nx, cost in sea_adj[pos]:
                        nstate = (nx, nx)  # ship moves with postman to nx
                        nd = cd + cost
                        if nstate not in dist or dist[nstate] > nd:
                            dist[nstate] = nd
                            heapq.heappush(hq, (nd, nx, nx))
            # after finish dijkstra, filter only states with pos=goal
            current_states = {}
            for (p, sp), c in dist.items():
                if p == goal:
                    if (p, sp) not in current_states or current_states[(p, sp)] > c:
                        current_states[(p, sp)] = c
            # if no states at goal, no solution but per problem always possible
        ans = min(current_states.values())
        print(ans)

if __name__ == "__main__":
    solve()