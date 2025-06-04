import sys
import heapq

def roll(dice, direction):
    top, south, east = dice
    north = 7 - south
    west = 7 - east
    bottom = 7 - top
    if direction == 'N':
        # Roll north:
        # top becomes south
        # south becomes bottom
        # bottom becomes north
        # north becomes top
        return (south, bottom, east)
    elif direction == 'S':
        # Roll south
        # top becomes north
        # north becomes bottom
        # bottom becomes south
        # south becomes top
        return (north, top, east)
    elif direction == 'E':
        # Roll east
        # top becomes west
        # west becomes bottom
        # bottom becomes east
        # east becomes top
        return (west, south, top)
    elif direction == 'W':
        # Roll west
        # top becomes east
        # east becomes bottom
        # bottom becomes west
        # west becomes top
        return (east, south, bottom)

def main():
    input_lines = sys.stdin.read().splitlines()
    i = 0
    while True:
        if i >= len(input_lines):
            break
        line = input_lines[i].strip()
        if not line:
            i += 1
            continue
        h, w = map(int, line.split())
        if h == 0 and w == 0:
            break
        i += 1
        grid = []
        for _ in range(h):
            row = list(map(int, input_lines[i].split()))
            i += 1
            grid.append(row)
        sr, sc = map(int, input_lines[i].split())
        i += 1
        gr, gc = map(int, input_lines[i].split())
        i += 1

        # dice state: (top, south, east)
        # Initially top=1, south=2, east=3 as in problem statement
        start_state = (sr, sc, 1, 2, 3)

        # distance dictionary: key = (r, c, top, south, east), value = cost
        dist = {}

        # priority queue: (cost, r, c, top, south, east)
        pq = []
        heapq.heappush(pq, (0, sr, sc, 1, 2, 3))
        dist[(sr, sc, 1, 2, 3)] = 0

        directions = [('N', -1, 0), ('S', 1, 0), ('E', 0, 1), ('W', 0, -1)]

        while pq:
            cost, r, c, top, south, east = heapq.heappop(pq)
            if (r, c) == (gr, gc):
                print(cost)
                break
            if dist.get((r, c, top, south, east), 10**9) < cost:
                continue
            for d, dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < h and 0 <= nc < w:
                    new_top, new_south, new_east = roll((top, south, east), d)
                    bottom = 7 - new_top
                    penalty = grid[nr][nc] * bottom
                    new_cost = cost + penalty
                    state = (nr, nc, new_top, new_south, new_east)
                    if dist.get(state, 10**9) > new_cost:
                        dist[state] = new_cost
                        heapq.heappush(pq, (new_cost, nr, nc, new_top, new_south, new_east))

if __name__ == "__main__":
    main()