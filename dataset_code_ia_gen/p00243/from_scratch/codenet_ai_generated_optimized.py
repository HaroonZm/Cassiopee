from collections import deque

def main():
    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    colors = ['R','G','B']

    while True:
        X, Y = map(int, input().split())
        if X == 0 and Y == 0:
            break
        grid = [input().split() for _ in range(Y)]

        # BFS to find connected component of the top-left cell with its color
        def flood_fill(g, target_color):
            visited = [[False]*X for _ in range(Y)]
            q = deque()
            q.append((0,0))
            visited[0][0] = True
            component = [(0,0)]
            while q:
                x,y = q.popleft()
                for dx, dy in directions:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < X and 0 <= ny < Y and not visited[ny][nx] and g[ny][nx] == target_color:
                        visited[ny][nx] = True
                        q.append((nx, ny))
                        component.append((nx, ny))
            return component

        def is_uniform(g):
            c = g[0][0]
            for row in g:
                for cell in row:
                    if cell != c:
                        return False
            return True

        start = tuple(tuple(row) for row in grid)
        visited_states = set([start])
        queue = deque()
        queue.append( (grid, 0) )

        while queue:
            g, steps = queue.popleft()
            if is_uniform(g):
                print(steps)
                break
            cur_color = g[0][0]
            comp = flood_fill(g, cur_color)
            for c in colors:
                if c == cur_color:
                    continue
                new_g = [row[:] for row in g]
                for x,y in comp:
                    new_g[y][x] = c
                ng_tuple = tuple(tuple(row) for row in new_g)
                if ng_tuple not in visited_states:
                    visited_states.add(ng_tuple)
                    queue.append((new_g, steps+1))

if __name__ == '__main__':
    main()