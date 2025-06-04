import sys
from collections import deque

def read_maze(h, w, lines):
    # We represent the maze as a grid of rooms, each room can connect to neighbors by doors (cost 1) or no door (no connection).
    # We'll build adjacency info with costs: 0 means no door, 1 means door (cost to pass = 1)
    # Input lines alternate: horizontal doors lines and vertical doors lines
    # h rows, w columns of rooms
    
    # horizontal doors: between (r, c) and (r, c+1)
    # vertical doors: between (r, c) and (r+1, c)
    # For no door (1), no edge is added.
    horizontal = []
    vertical = []
    idx = 0
    for i in range(2*h -1):
        line = lines[i].strip('\n')
        # horizontal lines start with space, vertical lines not (but we just split anyway)
        vals = list(map(int, line.strip().split()))
        if i % 2 == 0:
            horizontal.append(vals)  # length w-1
        else:
            vertical.append(vals)    # length w
    # Build the graph with edges and door indices
    # Each door has an ID for identification
    # We'll keep: for each room, edges to neighbors with door id and cost 1
    door_id = 0
    graph = [[[] for _ in range(w)] for __ in range(h)]
    door_positions = dict()  # door_id -> ((r1,c1),(r2,c2))
    # horizontal doors
    for r in range(h):
        for c in range(w-1):
            if horizontal[r][c] == 0:
                # door exists
                graph[r][c].append((r, c+1, door_id))
                graph[r][c+1].append((r, c, door_id))
                door_positions[door_id] = ((r, c), (r, c+1))
                door_id += 1
    # vertical doors
    for r in range(h-1):
        for c in range(w):
            if vertical[r][c] == 0:
                graph[r][c].append((r+1, c, door_id))
                graph[r+1][c].append((r, c, door_id))
                door_positions[door_id] = ((r, c), (r+1, c))
                door_id += 1
    return graph, door_positions

def bfs_with_cost(graph, h, w, blocked_door=None):
    # Return minimum number of doors (cards) needed to go from entry (0,0) to exit (h-1,w-1).
    # blocked_door: door id that cannot be passed.
    # Standard BFS with cost: each door = 1 cost, no door = no edge (edges only when door)
    # since all edges have equal cost 1, simple BFS works.
    dist = [[-1]*w for _ in range(h)]
    dist[0][0] = 0
    q = deque()
    q.append((0,0))
    while q:
        r,c = q.popleft()
        if r == h-1 and c == w-1:
            return dist[r][c]
        for nr,nc,did in graph[r][c]:
            if did == blocked_door:
                # door is broken, can't pass
                continue
            if dist[nr][nc] == -1:
                dist[nr][nc] = dist[r][c] + 1
                q.append((nr,nc))
    return -1

def bfs_path(graph, h, w):
    # BFS from entry to exit, return dist and previous room and door id (for shortest path)
    dist = [[-1]*w for _ in range(h)]
    prev = [[None]*w for _ in range(h)]  # (r,c,door_id)
    dist[0][0] = 0
    q = deque()
    q.append((0,0))
    while q:
        r,c = q.popleft()
        if r == h-1 and c == w-1:
            break
        for nr,nc,did in graph[r][c]:
            if dist[nr][nc] == -1:
                dist[nr][nc] = dist[r][c] + 1
                prev[nr][nc] = (r,c,did)
                q.append((nr,nc))
    path = []
    if dist[h-1][w-1] == -1:
        return -1, []
    # reconstruct path doors
    r,c = h-1,w-1
    while (r,c) != (0,0):
        pr,pc,did = prev[r][c]
        path.append(did)
        r,c = pr,pc
    path.reverse()
    return dist[h-1][w-1], path

def solve_one_maze(h, w, lines):
    graph, doors = read_maze(h, w, lines)
    # shortest path from entry to exit (without blocked door)
    shortest_dist, shortest_path = bfs_path(graph, h, w)
    if shortest_dist == -1:
        # no path even if no broken door
        return -1
    # If no broken door, we need shortest_dist cards
    # Now, consider broken door unknown.
    # Strategy: find a path that can find which door is broken and then reroute.
    # We simulate the idea described: we try to find worst case minimal cards needed,
    # which is max over all broken doors:
    # cost = cards spent until broken door found + cards needed from there to exit avoiding that broken door
    #
    # So one way:
    # 1) For each door on shortest path:
    #    simulate broken door = that door
    #    find path from entry to exit avoiding that door: cost2
    #    find cost1 = distance along shortest path until broken door (index + 1)
    #    total = cost1 + cost2
    # take max over all door broken in the maze (only those reachable?)
    #
    # But problem: currently shortest_path only covers one path, but broken door can be anywhere in the maze in theory.
    #
    # The problem states: "If there exists no path to pass through when a door is broken, output -1"
    # So broken door can be any door in the maze, not only those on shortest path.
    #
    # So let's do:
    # For every door in the maze:
    #   Check if buying cards along shortest path until encountering the broken door (count how many doors until that door in the shortest path)
    #   plus cost of shortest path from start to exit avoiding that broken door
    # But broken door that is not on shortest path, we can't find it until we try to use it.
    #
    # So worst case is max over all doors:
    # cost_when_broken = cards used until broken door found + shortest path avoiding that broken door
    # If door not on shortest path, broken door found at start 0 cards + shortest path avoiding door
    #
    # To get cards until broken door: find earliest usage of door on the path finding strategy.
    # The problem says "You should follow path in figure G-5 until find broken door; after find broken door re-route without it".
    #
    # Because problem states a strategy: find broken door on some path, then reroute avoiding that door.
    #
    # We assume the initial path is the shortest path.
    #
    # So for doors not on shortest path, cards until find broken door = infinity? no, you never use the door, so no cards lost, cost is path avoiding broken door.
    #
    # So minimal cards needed for broken door = min over all paths that can find that door first + reroute after.
    #
    # To keep simple (beginner approach):
    # We'll try shortest path as initial path:
    # For each door:
    #   If door on shortest path at position i, cost_until=find door = i+1 (1-based),
    #   else cost_until=some large number (e.g. shortest_dist+10)
    #   then cost_avoid = bfs_with_cost(blocked door)
    # total cost = cost_until + cost_avoid
    # Finally, answer = max over all doors total cost.
    #
    # If for some door cost_avoid == -1 no path avoiding broken door, then answer=-1

    # For doors not in shortest path, to be safe, consider cost_until as shortest_dist (traveling whole shortest path without door)
    # aka we only find door on use, so if door not used on path, cost_until = shortest_dist (assuming we try all doors)
    # But if door not on path we never need to traverse it, so cards until find broken door = 0? Because we never try it.
    # But then do we find broken door? Problem says broken door cannot be found if we do not try door.
    # So broken door not on path means we never try to open it, so broken door can't block us.
    #
    # So cost_until = position on shortest path if door on path else 0
    # total cost = cost_until + cost_avoid

    # Let's build a set of door indices on shortest path
    doors_on_path = set(shortest_path)

    ans = shortest_dist  # minimum if no door broken blocks path
    for d in doors.keys():
        cost_until = 0
        if d in doors_on_path:
            # find position
            cost_until = shortest_path.index(d) + 1
        # cost to bypass broken door d
        cost_avoid = bfs_with_cost(graph, h, w, blocked_door=d)
        if cost_avoid == -1:
            return -1
        total_cost = cost_until + cost_avoid
        if total_cost > ans:
            ans = total_cost
    return ans

def main():
    lines = sys.stdin.readlines()
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if line == '':
            i += 1
            continue
        h_w = line.split()
        if len(h_w) < 2:
            i += 1
            continue
        h, w = map(int, h_w)
        if h == 0 and w == 0:
            break
        # read 2*h-1 lines
        needed = 2*h -1
        maze_lines = lines[i+1:i+1+needed]
        output = solve_one_maze(h, w, maze_lines)
        print(output)
        i += 1 + needed

if __name__ == '__main__':
    main()