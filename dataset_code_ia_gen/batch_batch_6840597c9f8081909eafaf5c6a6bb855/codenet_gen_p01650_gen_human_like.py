from collections import deque

def solve_maze(H, W, grid):
    # Directions: right (0,1), down (1,0)
    directions = [(0,1),(1,0)]
    
    # Map letters to indices: a-z and A-Z -> 0-51
    def char_to_index(c):
        if 'a' <= c <= 'z':
            return ord(c) - ord('a')
        else:
            return ord(c) - ord('A') + 26
    
    # We'll represent jewels in stack by counts for each type up to 10
    # State: (row, col, tuple(counts)) where counts is 52-length tuple of jewels in stack.
    # But max 10 per letter, so we can use small ints.
    # Since stack restriction applies (LIFO), we must remember the stack order.
    # So instead, store the stack as tuple of letters.
    # Max length of stack can be up to 2500 theoretically (all steps), but that is huge.
    # But since at most 10 occurrences per letter, stack max length is 10*52=520 in worst.
    # Too big for visited set.
    
    # To handle stack as state is costly.
    # Observation: Because picking and placing must follow LIFO stack order,
    # we can store the stack as a tuple:
    # But to keep it within feasible memory, use bitmask per letter counts up to 10,
    # and store stack as a string? This is big.
    
    # Alternative approach:
    # Because of constraints, it's safe to store stack as string (tuple of letters),
    # but we can prune states visited at (r,c) with same stack.
    
    # Let's try BFS with visited as dict with (r,c,stack) keys.
    
    start = (0,0)
    if grid[0][0] == '#':
        return -1  # Cannot start
    
    queue = deque()
    visited = dict()
    
    # initial state: position (0,0), empty stack, placed jewels count=0
    queue.append( (0, 0, tuple(), 0) )
    visited[(0,0,tuple())] = 0
    
    max_placed = -1
    
    while queue:
        r, c, stack, placed = queue.popleft()
        # If reached goal:
        if r == H-1 and c == W-1:
            if placed > max_placed:
                max_placed = placed
            continue
        
        for dr, dc in directions:
            nr, nc = r+dr, c+dc
            if 0 <= nr < H and 0 <= nc < W:
                cell = grid[nr][nc]
                if cell == '#':
                    continue
                
                # Possible actions depending on cell content:
                states_to_add = []
                # If free cell '.'
                if cell == '.':
                    # just move as is
                    states_to_add.append( (stack, placed) )
                # Jewel lowercase?
                elif 'a' <= cell <= 'z':
                    # Option1: don't pick jewel
                    states_to_add.append( (stack, placed) )
                    # Option2: pick jewel -> add this jewel on top of stack
                    states_to_add.append( (stack + (cell,), placed) )
                # Hole uppercase?
                elif 'A' <= cell <= 'Z':
                    # Option1: don't place jewel
                    states_to_add.append( (stack, placed) )
                    # Option2: place jewel if top of stack matches lowercase of this uppercase
                    if stack and stack[-1] == cell.lower():
                        new_stack = stack[:-1]
                        new_placed = placed + 1
                        states_to_add.append( (new_stack, new_placed) )
                else:
                    # Just move as is
                    states_to_add.append( (stack, placed) )
                
                for new_stack, new_placed in states_to_add:
                    key = (nr, nc, new_stack)
                    if key not in visited or visited[key] < new_placed:
                        visited[key] = new_placed
                        queue.append( (nr, nc, new_stack, new_placed) )
    
    return max_placed

def main():
    import sys
    input = sys.stdin.readline
    
    while True:
        line = ''
        while line.strip() == '':
            line = sys.stdin.readline()
            if line == '':
                return
        H, W = map(int, line.strip().split())
        if H == 0 and W == 0:
            break
        grid = []
        while len(grid) < H:
            row = sys.stdin.readline().rstrip('\n')
            if row == '':
                continue
            grid.append(row)
        
        result = solve_maze(H, W, grid)
        print(result)

if __name__ == "__main__":
    main()