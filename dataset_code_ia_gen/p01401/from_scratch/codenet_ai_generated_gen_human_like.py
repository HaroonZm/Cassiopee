from collections import deque

def solve():
    while True:
        line = input()
        if line == '':
            continue
        w_h = line.split()
        if len(w_h) < 2:
            w_h += input().split()
        w, h = map(int, w_h)
        if w == 0 and h == 0:
            break

        grid = [input().split() for _ in range(h)]

        # Find S and G and max seal number
        max_seal = 0
        start = None
        goal = None
        for y in range(h):
            for x in range(w):
                c = grid[y][x]
                if c == 'S':
                    start = (y, x)
                elif c == 'G':
                    goal = (y, x)
                else:
                    if c.isdigit():
                        n = int(c)
                        if n > max_seal:
                            max_seal = n

        # BFS states: position (y,x) and current seal step (0..max_seal)
        # Because we must destroy seals in order: can't touch seal n+1 before all n sealed.
        visited = [[[False]*(max_seal+1) for _ in range(w)] for __ in range(h)]
        q = deque()
        # start with seal_step=0 means no seals destroyed yet
        q.append((start[0], start[1], 0, 0))  # y, x, seal_step, time
        visited[start[0]][start[1]][0] = True

        while q:
            y, x, step, t = q.popleft()
            c = grid[y][x]

            # If on seal number equal to step+1, destroy it by touching it, advance step
            if c.isdigit():
                num = int(c)
                if num == step + 1:
                    step += 1

            if (y, x) == goal and step == max_seal:
                print(t)
                break

            for dy, dx in ((1,0), (-1,0), (0,1), (0,-1)):
                ny, nx = y+dy, x+dx
                if 0 <= ny < h and 0 <= nx < w:
                    nc = grid[ny][nx]
                    nstep = step
                    if nc.isdigit():
                        num = int(nc)
                        # can only touch seals up to step+1, can't touch the next ones before previous destroyed
                        # but in logic, we only update step if we stand on it
                        # so here, must not enter seal number > step+1
                        if num > step +1:
                            continue
                    # Else ok to move
                    if not visited[ny][nx][nstep]:
                        visited[ny][nx][nstep] = True
                        q.append((ny, nx, nstep, t+1))

if __name__ == '__main__':
    solve()