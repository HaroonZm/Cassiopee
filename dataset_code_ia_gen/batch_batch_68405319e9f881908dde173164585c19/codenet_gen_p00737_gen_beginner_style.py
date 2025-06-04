import sys
from collections import deque

# Directions: 0=East,1=South,2=West,3=North
dx = [1,0,-1,0]
dy = [0,1,0,-1]

def turn(dir, cmd):
    # cmd: 0=Straight,1=Right,2=Back,3=Left
    if cmd == 0:
        return dir
    elif cmd == 1:
        return (dir + 1) % 4
    elif cmd == 2:
        return (dir + 2) % 4
    elif cmd == 3:
        return (dir + 3) % 4

def main():
    input = sys.stdin.readline
    while True:
        line = input()
        if not line:
            break
        w,h = map(int,line.split())
        if w == 0 and h == 0:
            break
        board = []
        for _ in range(h):
            row = list(map(int,input().split()))
            board.append(row)
        costs = list(map(int,input().split()))

        # state: (x,y,direction)
        # initial: at (0,0), direction east (0)
        # need to reach (w-1,h-1)
        # We'll use BFS with cost tracking (Dijkstra would be better but problem constraints allow BFS with cost)

        from heapq import heappush, heappop
        inf = 10**9
        dist = [[[inf]*4 for _ in range(w)] for __ in range(h)]
        dist[0][0][0] = 0
        heap = []
        heappush(heap,(0,0,0,0)) # cost,x,y,dir

        while heap:
            cost,x,y,dir = heappop(heap)
            if dist[y][x][dir] < cost:
                continue
            if x == w-1 and y == h-1:
                # goal square, must Halt here, no extra cost as Halt is automatic and no player cost
                print(cost)
                break

            # Command assigned on current square
            square_cmd = board[y][x]

            # The robot executes the command of the square if no player command is given
            # The player can override by giving Straight, Right, Back, or Left command.
            # Player cannot give Halt command.
            # We try all options: no change (use square_cmd), or override with any of 0..3 if different from square_cmd

            cmds_to_try = [square_cmd] # default command from square

            # add override commands different from square_cmd and not Halt (4)
            for c in range(4):
                if c != square_cmd:
                    cmds_to_try.append(c)

            for c in cmds_to_try:
                # If c == 4 (Halt), player can't give it, so it can only come from the square command
                # but if c == 4, and not goal square, robot loses (game ends early) skip
                if c == 4:
                    # Halt command: can only halt at goal square
                    if x == w-1 and y == h-1:
                        # done, already handled above, so no move, no cost
                        continue
                    else:
                        # losing state, skip
                        continue

                ndir = turn(dir,c)
                nx = x + dx[ndir]
                ny = y + dy[ndir]

                if nx < 0 or nx >= w or ny < 0 or ny >= h:
                    # out of board, lose, ignore
                    continue

                ncost = cost
                # if override command (player gave command) and c != square_cmd, pay cost[c] else 0
                if c != square_cmd:
                    ncost += costs[c]

                if dist[ny][nx][ndir] > ncost:
                    dist[ny][nx][ndir] = ncost
                    heappush(heap,(ncost,nx,ny,ndir))

if __name__ == "__main__":
    main()