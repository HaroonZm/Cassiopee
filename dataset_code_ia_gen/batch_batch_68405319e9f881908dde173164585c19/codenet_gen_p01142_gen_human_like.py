import sys
sys.setrecursionlimit(10**7)

# Directions: Up(0), Right(1), Down(2), Left(3)
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def turn_left(d):
    return (d + 3) % 4

def turn_right(d):
    return (d + 1) % 4

def find_start_and_dir(grid, W, H, target):
    # Find target position and direction (facing floor side)
    for y in range(H):
        for x in range(W):
            if grid[y][x] == target:
                # Find direction where it's floor ('.')
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < W and 0 <= ny < H:
                        if grid[ny][nx] == '.':
                            return (x, y, d)
    return None

def get_next_pos_until_wall(grid, W, H, x, y, d):
    # Move forward until hit wall
    while True:
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < W and 0 <= ny < H and grid[ny][nx] != '#':
            x, y = nx, ny
        else:
            break
    return x, y

def simulate(grid, W, H, start_x, start_y, start_dir, commands, reverse=False):
    # If reverse, commands to run:
    # - reversed order
    # - left turns become right, right turns become left
    # Left is 'L', Right is 'R'
    if reverse:
        commands = commands[::-1]
        commands_mapped = []
        for c in commands:
            if c == 'L':
                commands_mapped.append('R')
            else:
                commands_mapped.append('L')
        commands = commands_mapped
        
    x, y, d = start_x, start_y, start_dir
    n = len(commands)
    for i in range(n):
        # Move forward until wall
        x2, y2 = get_next_pos_until_wall(grid, W, H, x, y, d)
        x, y = x2, y2
        # If can't move it means wall right in front,
        # turn accordingly
        c = commands[i]
        # Turn at the point of wall collision (no move)
        if c == 'L':
            d2 = turn_left(d)
        else:
            d2 = turn_right(d)
        # Check if after turn we can move forward at least 1 step
        nx = x + dx[d2]
        ny = y + dy[d2]
        if 0 <= nx < W and 0 <= ny < H and grid[ny][nx] != '#':
            d = d2
        else:
            # Can't move after turn, keep d unchanged, but move on to next command
            d = d2
            # but the problem states that even if can't move, we execute next command
    # last move forward when hits wall triggers turn and then stop
    # after last command stop at current position
    return (x, y)

def reachable_positions(grid, W, H, start_x, start_y, start_dir, max_steps=2000):
    # BFS or DFS to find all reachable end states after running some cmd sequence (possibly empty),
    # because the instructions finite and execute until stop at last cmd, 
    # states are the position and direction plus step count cannot exceed commands length.
    # here we want to find all possible end positions of the doll after running a program of length <= max_steps
    # but max_steps is large, so we limit length and do BFS to find all reachable states after exactly running one program
    # of length n, for all n<=max_steps: too big,
    # better is to BFS over states (x, y, d, index_of_next_command) where index_of_next_command runs from 0 to max_steps.
    # Actually, since the problem says "any program", it means any finite sequence of L and R.
    # We want to find if exists a program (sequence of L,R) so that starting from given start pos dir,
    # after executing the program the doll stops on a given cell.
    #
    # We try BFS over states (x, y, d, i), where i is command index, but we try all possible commands L or R at each step,
    # limit max program length to W*H*4 about 4096 is big but maybe feasible.
    # we'll do BFS from initial state with i=0, and at each step try turning L or R,
    # after hitting wall, move forward then turn (or turn in place if can't move forward after turn)
    # i increases by 1 per applied command
    #
    # We do this until we find a position that matches the goal or no new states.
    from collections import deque
    visited = set()
    q = deque()
    q.append((start_x, start_y, start_dir, 0))
    visited.add((start_x, start_y, start_dir, 0))
    max_prog_len = W*H*4+10
    positions_after_exec = set()
    # Also collect end positions reached when commands finished (i.e. after full program)
    while q:
        x, y, d, i = q.popleft()
        if i == max_prog_len:
            positions_after_exec.add((x, y))
            continue
        # we can stop at this point if want
        positions_after_exec.add((x, y))
        for c in ['L', 'R']:
            # simulate one command starting at (x,y,d), but here we do the same logic as in simulate for one step
            x2, y2 = get_next_pos_until_wall(grid, W, H, x, y, d)
            # turn
            if c == 'L':
                d2 = turn_left(d)
            else:
                d2 = turn_right(d)
            # check if can move forward after turn
            nx = x2 + dx[d2]
            ny = y2 + dy[d2]
            if 0 <= nx < W and 0 <= ny < H and grid[ny][nx] != '#':
                d_next = d2
            else:
                d_next = d2
            state = (x2, y2, d_next, i+1)
            if state not in visited:
                visited.add(state)
                q.append(state)
    return positions_after_exec

def can_reach(grid, W, H, start_x, start_y, start_dir, goal_x, goal_y):
    # We want to know if there is a program that leads from start to goal.
    # Use BFS over state space (like reachable_positions)
    # with early stop when reach (goal_x, goal_y)
    from collections import deque
    visited = set()
    q = deque()
    q.append((start_x, start_y, start_dir, 0))
    visited.add((start_x, start_y, start_dir, 0))
    max_prog_len = W*H*4+10
    while q:
        x, y, d, i = q.popleft()
        if (x, y) == (goal_x, goal_y) and i>0:
            return True
        if i == max_prog_len:
            continue
        for c in ['L', 'R']:
            x2, y2 = get_next_pos_until_wall(grid, W, H, x, y, d)
            if c == 'L':
                d2 = turn_left(d)
            else:
                d2 = turn_right(d)
            nx = x2 + dx[d2]
            ny = y2 + dy[d2]
            if 0 <= nx < W and 0 <= ny < H and grid[ny][nx] != '#':
                d_next = d2
            else:
                d_next = d2
            state = (x2, y2, d_next, i+1)
            if state not in visited:
                visited.add(state)
                q.append(state)
    return False

def can_reach_exact(grid, W, H, start_x, start_y, start_dir, goal_x, goal_y):
    # The problem states the doll executes the full program, stops at last command
    # So previously, the BFS accepts any stopping position regardless of command length
    # But actually, a program's length is finite, so some maximum.
    # We'll assume large max_prog_len like W*H*4+10 to cover all states
    return can_reach(grid, W, H, start_x, start_y, start_dir, goal_x, goal_y)

def main():
    input = sys.stdin.readline
    while True:
        W,H = map(int,input().split())
        if W==0 and H==0:
            break
        grid = [input().rstrip('\n') for _ in range(H)]
        # find kitchen (K) and master (M)
        sx, sy, sdir = find_start_and_dir(grid, W, H, 'K')
        gx, gy, gdir = find_start_and_dir(grid, W, H, 'M')
        # Check forward direction, the robot starts on K facing floor side (sdir)
        # We want to know if there exists a program so that starting at (K,sdir) the doll stops on M
        # Then from M facing floor direction (gdir), with reverse execution, doll stops on K
        # Problem: can doll reach M going forward with some program? Then can doll return to K going reverse?
        # To reverse, execute reversed program with left/right swapped commands
        # So need path from K to M forward, path from M to K backward
        
        # First, test forward reachability
        # We'll do BFS over states with arbitrary commands
        # But we want to know if exists a program causing doll to stop at (gx,gy).
        # We use can_reach: returns True if possible to reach goal by some program (of length ≤some max)
        if not can_reach_exact(grid, W, H, sx, sy, sdir, gx, gy):
            print("He cannot bring tea to his master.")
            continue
        
        # Now check reverse route from M to K, with reversed commands and swapped L/R
        # So we do the same function but different start and goal, and reverse=True
        if not can_reach_exact(grid, W, H, gx, gy, gdir, sx, sy):
            # even if doll can reach the master, cannot return to kitchen
            print("He cannot return to the kitchen.")
            continue
        
        # If both forward and backward reachable
        print("He can accomplish his mission.")

if __name__ == "__main__":
    main()