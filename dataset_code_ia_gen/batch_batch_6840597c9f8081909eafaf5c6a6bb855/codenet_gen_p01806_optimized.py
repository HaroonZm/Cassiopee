import sys
sys.setrecursionlimit(10**7)

def rotate(dice, c):
    # dice: (l,r,f,b,d,u)
    l,r,f,b,d,u = dice
    if c=='L':  # x軸負方向
        # rotate around x axis negative: top->front, front->bottom, bottom->back, back->top
        # update f,b,d,u accordingly
        return (d,u,f,b,r,l) if False else (l,r,b,f,u,d)
    if c=='R':  # x軸正方向
        return (l,r,f,b,u,d)
    if c=='F':  # y軸負方向
        # rotate around y axis negative: top->left, left->bottom, bottom->right, right->top
        return (u,d,f,b,r,l)
    if c=='B':  # y軸正方向
        return (d,u,f,b,l,r)
    # Above are incorrect according to problem statement; need actual correct rotations:
    # The problem statement says rotations are along x and y axis only, in 4 directions L,R,F,B:
    # We model dice orientation as dictionary {l,r,f,b,d,u}
    # After rotation, the faces change position.
    # Let's define per rotation how faces move.

def rotate(d,direction):
    l,r,f,b,dn,up=d
    if direction=='L':
        # rotate around x axis negative: (left face towards bottom)
        # new faces after rotate L:
        # top -> front, front -> bottom, bottom -> back, back -> top
        # left,right unchanged
        return (l,r,b,f,up,dn)
    elif direction=='R':
        # rotate around x axis positive
        # inverse of L
        return (l,r,f,b,dn,up)  # placeholder wrong
    elif direction=='F':
        # rotate around y axis negative: (front face towards bottom)
        # left->top, top->right, right->bottom, bottom->left
        return (up, dn, f, b, r, l)
    elif direction=='B':
        # rotate around y axis positive, inverse of F
        return (dn, up, f, b, l, r)
    # The above is inconsistent, let's do correct method:
    # We'll represent dice orientation and define rotations properly:

def rotate(dice, c):
    l,r,f,b,dn,up = dice
    if c=='L':  # rotate x-axis negative direction
        # top->front, front->bottom, bottom->back, back->top
        return (l,r,b,f,up,dn)
    if c=='R':  # rotate x-axis positive direction
        # inverse of L
        return (l,r,f,b,dn,up)  # fix later
    if c=='F':  # rotate y-axis negative direction
        # left->top, top->right, right->bottom, bottom->left
        return (up,dn,f,b,r,l)  # fix later
    if c=='B':  # rotate y-axis positive direction
        return (dn,up,f,b,l,r)  # fix later

# After reconsideration, let's assign dice faces as standard:

# Faces dictionary:

# l - left
# r - right
# f - front
# b - back
# d - down (bottom)
# u - up (top)

# Rotations:

# rotate L: x-axis negative direction
# top->front, front->bottom, bottom->back, back->top
# So new faces:
# up->f, f->dn, dn->b, b->up
# left,right unchanged

# rotate R: x-axis positive direction
# inverse of L
# up->b, b->dn, dn->f, f->up

# rotate F: y-axis negative direction
# left->up, up->right, right->down, down->left
# front, back unchanged

# rotate B: y-axis positive direction
# inverse of F

def rotate(dice, c):
    l,r,f,b,dn,u = dice
    if c=='L':
        return (l, r, u, dn, b, f)
    if c=='R':
        return (l, r, b, f, u, dn)
    if c=='F':
        return (u, dn, f, b, r, l)
    if c=='B':
        return (dn, u, f, b, l, r)

def main():
    input=sys.stdin.readline
    while True:
        N=int(input())
        if N==0:
            break
        dice_info=[]
        for _ in range(N):
            x,y= map(int,input().split())
            l,r,f,b,dn,u= map(int,input().split())
            rot=input().rstrip('\n')
            # compute the sequence of down faces during rotations - initial and after each rotation
            # initial bottom face number is dn
            # At each rotation, update dice and record bottom face number and position
            # positions are fixed for each dice: x,y
            dice=(l,r,f,b,dn,u)
            bottom_numbers=[]
            bottom_positions=[]
            bottom_numbers.append(dice[4]) # dn
            bottom_positions=[]
            bottom_positions.append((x,y))
            for c in rot:
                dice=rotate(dice,c)
                bottom_numbers.append(dice[4])
                bottom_positions.append((x,y))
            # the dice after rotations is removed so no more updates
            dice_info.append((bottom_positions,bottom_numbers))
        
        # N steps of placing dice in some order
        # Each dice writes down number on the cell its bottom face touches
        # The problem: choosing order of pressing buttons to get max sum of board
        
        # Since each dice is placed at fixed positions and rotations, and all dice placements have fixed sequences of (pos,number)
        # applying one dice overwrites numbers on the board with dice's bottom numbers on its positions
        # only keep last overwrite on a cell during the whole sequence of N dice placements
        # pressing order matters: last write at a cell is from last dice to write cell
        
        # Because pressing order can repeat dice multiple times, and total N presses,
        # we want the order of length N from dice 0..N-1 (allow repeats) to maximize sum of board's cells after all placements.
        # But input N is number of dice, and also number of presses [ exactly N presses, may use buttons multiple times? Yes]
        # From statement: N buttons, N presses
        # different dice can be repeated in presses in any order
        
        # At end, cells have the number from last dice to write at that cell, sum over all cells

        # Key: final cell value is from last dice that wrote cell
        # so each press overwrites cell values at its sequences

        # To maximize sum, minimize overwriting of large values by later dice with small values
        # so we want an order of presses to maximize sum of final board after N presses.

        # N ≤ 15, number of dice ≤15

        # Cells visited per dice limited, small rotations (max 30), so we can store cells per dice presses as dict or list

        # Try all permutations of dice presses length N with repetition: 15^15 huge, infeasible

        # But each button can be pressed multiple times,
        # input is N dice and N presses, so number of sequences = N^N, too big

        # But constraints can be addressed by DP with bitmasks? no dice usage limit, so no bitmask on used dice

        # Alternatively, because after N presses (each press chooses dice i), order matters

        # We can consider DP by order:

        # State: number of presses done (0..N)

        # The board after presses done is represented by mapping cells to value (last write)

        # But number of possible boards huge

        # Alternative approach:

        # Because cells visited by dice are limited (positions)

        # Let's get all positions visited by any dice (<=N*31 max), max 465 cells

        # For these M cells, we can store for each press what overwrites which cell with what value

        # The problem reduces to arranging order of N presses from dice 0..N-1 (length N sequence) to maximize sum of final board values

        # But still large

        # Since dice can only overwrite positions they visit, and we know the sequence of positions and values per dice press

        # But each dice placed once only? No, dice can be used multiple times (buttons can be pressed multiple times)

        # No usage limit per dice: yes, freedom of pressing any dice any number of times as long as total presses = N

        # Since dice can be repeated arbitrarily, repeated placement is allowed

        # Given complex, the problem is classic "Last write wins" over cells with multiple overlapping writes

        # Because order matter, and last write at a cell dominates

        # For each cell, the last dice to write it sets its value

        # So final sum = sum over all cells of value from last dice placing that cell

        # Reformulate:

        # For each cell, track which presses write it and what values

        # So the problem can be considered as Sorted Search with backtracking or DP over orderings

        # Since N ≤15, we can attempt backtracking with memo or pruning

        # Implement backtracking:

        # State: # of presses done (k), current board (dict cell->value)

        # At each step, try pressing any dice (0..N-1) not limited

        # Apply dice's cell writes, overwrite board cells at visited positions with dice's bottom numbers

        # Recursively proceed until N presses done

        # Store best score among all sequences

        # To avoid repeated states:

        # But board size big, cannot memorize all boards

        # Prune by upper bound estimation

        # Implement backtracking with pruning and memoization of limited states (such as top cells used)

        # Or order dice by score to prune

        # Implement greedy first though:

        # For each dice i, sum of bottom numbers is sum_i

        # Press all dice with max sum_i

        # But this may be suboptimal because of overwrites

        # Alternatively, since last dice writes count more, pressing dice whose cells are not overwritten later better

        # Thus pressing dice with high values later in order to overwrite previous is beneficial

        # So try all permutations of dice indexes, but N! = big

        # Instead, approximate by sorting dice by total sum of bottom face values and check permutations of their order (small N)

        # But this might still be big.

        # As a heuristic, since problem is interactive, implement a greedy method:

        # For all permutations of dice orderings (N small), try permutations without repetitions (because N dice, N presses)

        # But statement allows pressing same button multiple times

        # So total number of sequences huge, cannot enumerate.

        # Finally, as per sample data, N small up to 15 (and T up to 40)

        # Let's implement:

        # For each dice i, precompute map of cells visited and their final bottom number for each:

        # That is, in the rotational sequence, which positions, which numbers at those positions writes can be precomputed

        # Actually each dice writes several times during its rotations

        # But dice writes to same cell many times during rotations => last write at the position during dice placement is final on that dice placement

        # So from dice placement, we keep only last write at each cell.

        # So for dice i, get dict cell->value (last write at that cell during dice placement)

        # Then pressing dice i once writes these values on board, overwrite existing.

        # Now model game as:

        # Start empty board

        # Press dice d1,d2,...dn

        # For each press, update board with dice_i's writes: overwrite values of cells in dice_i's dict

        # At end sum all board cell values

        # So we want to pick sequence d1..dn to maximize final sum, considering overwrites.

        # Since N ≤15, positions per dice up to ~31, max unique cells ~465

        # Trying all N^N sequences impossible.

        # Instead, model as DP where state is number of presses done and the ordering of presses as sequences.

        # Try backtracking with caching but huge.

        # Since order matters and same dice can be pressed more than once, but max N is small (15), implement backtracking with pruning:

        # At each level, try all dice, update board, proceed

        # Cache memoization by (level, tuple of values at each cell) is impossible because large.

        # So implement pruning:

        # For each level, order dice by their total sum to try promising first

        # Keep global best

        # If current board sum + max possible vals * remaining presses <= best, prune

        # So precompute max bottom number per dice

        # Implement backtracking with pruning

        # Because problem is complicated, let's implement solution accordingly:

        from collections import defaultdict

        Mcells=set()
        dices_cells_vals=[]
        max_val_per_dice=[]
        for poslst,valuelst in dice_info:
            dcv=dict()
            for pos,val in zip(poslst,valuelst):
                dcv[pos]=val
                Mcells.add(pos)
            dices_cells_vals.append(dcv)
            max_val_per_dice.append(sum(dcv.values()))
        Mcells=list(Mcells)
        idx_cell={c:i for i,c in enumerate(Mcells)}
        M=len(Mcells)

        # represent board as array of length M with initial 0
        board=[0]*M

        best=[0]
        Np=N

        total_max_val=max(max_val_per_dice) if max_val_per_dice else 0

        def dfs(k):
            if k==Np:
                s=sum(board)
                if s>best[0]:
                    best[0]=s
                return
            # Upper bound pruning
            s=sum(board)
            remain=Np-k
            if s+remain*total_max_val<=best[0]:
                return
            # try all dice
            for i in range(N):
                dcv=dices_cells_vals[i]
                updated=[]
                for c,v in dcv.items():
                    idx=idx_cell[c]
                    updated.append((idx,board[idx]))
                    board[idx]=v
                dfs(k+1)
                for idx,oldv in updated:
                    board[idx]=oldv

        dfs(0)
        print(best[0])

if __name__=='__main__':
    main()