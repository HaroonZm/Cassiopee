import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

MOD = 10**9+7

N,Q,A,B,C,D,E,F,G = map(int,input().split())

# Initialize matrix values using formula; but as N can be up to 40000*40000, store only deltas and generate on demand
# We will keep track of transformations, so no need to store entire matrix.

# We'll represent the matrix as logical indices with these transformations:
# row_map and col_map represent current mapping from logical index to original index
# We'll not store arrays of size N because N can be huge. Instead, we store the transformations as parameters.
# For rows and columns, store offsets, reversals, swaps through variables.

# Because of performance, we cannot simulate each operation on entire matrix, but only track transformations.

# We'll maintain:
# - orientation: current rotation state (0=normal,1=rotated 90 clockwise,2=rotated 180,3=rotated 270)
# - row_reverse: if rows are reversed
# - col_reverse: if cols are reversed
# - row_swap_map: dictionary of swapped rows (maps from logical row to other logical row) for SR operations
# - col_swap_map: dictionary of swapped cols
# - overrides: dictionary for overwritten cells, key=(r,c), value=v; these override computed values
# The same for CP: updates on (r2,c2) from (r1,c1).

# Because Q can be large, but we do at most 40,000 queries which is manageable.

# We store the matrices logical indices as 1-based.

orientation = 0
row_rev = False
col_rev = False

row_swap = dict()
col_swap = dict()

# overridden cells, keys are (r,c), values are the written integer
overrides = dict()

def transform_pos(r, c):
    # transform (r,c) according to orientation and reflections
    # all logical indices are 1-based, from 1 to N
    # apply row_rev, col_rev, row_swap and col_swap after rotation

    # Step 1: apply rotation inverse to find original cell mapping before transformations
    # Since orientation tells how the matrix is oriented, to get original cell, we reverse it.

    or_r, or_c = r, c
    if orientation == 0:
        rr, cc = r, c
    elif orientation == 1:
        rr = c
        cc = N - r +1
    elif orientation == 2:
        rr = N - r +1
        cc = N - c +1
    else:
        rr = N - c +1
        cc = r

    # Apply row reverse if needed
    if row_rev:
        rr = N - rr +1
    if col_rev:
        cc = N - cc +1

    # Apply swaps if any
    if rr in row_swap:
        rr = row_swap[rr]
    if cc in col_swap:
        cc = col_swap[cc]

    return rr, cc

def reverse_transform_pos(rr, cc):
    # transform original (rr,cc) into current position after transformations
    # inverse of transform_pos for output purposes
    r, c = rr, cc

    # inverse of swaps:
    # row_swap maps positions, so invert the dictionary:
    if r in row_swap.values():
        for k,v in row_swap.items():
            if v == r:
                r = k
                break
    if c in col_swap.values():
        for k,v in col_swap.items():
            if v == c:
                c = k
                break

    # inverse of reversals:
    if row_rev:
        r = N - r +1
    if col_rev:
        c = N - c +1

    # inverse of orientation:
    if orientation == 0:
        rr2, cc2 = r, c
    elif orientation ==1:
        rr2 = N - c +1
        cc2 = r
    elif orientation ==2:
        rr2 = N - r +1
        cc2 = N - c +1
    else:
        rr2 = c
        cc2 = N - r +1
    return rr2, cc2

def get_val(r,c):
    # returns the value at transformed cell (r,c) after all ops
    # first get original position of cell before transforms
    rr, cc = transform_pos(r,c)
    if (r,c) in overrides:
        return overrides[(r,c)]
    # else compute default A_{rr,cc}
    return (rr*A + cc*B) % C

for _ in range(Q):
    parts = input().split()
    op = parts[0]

    if op == 'WR':
        # WR r c v: write integer v into (r,c)
        r,c,v = map(int,parts[1:])
        # just write at logical position (r,c): we need to map user given to actual current index because WR is on current matrix
        overrides[(r,c)] = v

    elif op == 'CP':
        # CP r1 c1 r2 c2: copy cell (r1,c1) to (r2,c2)
        r1,c1,r2,c2 = map(int,parts[1:])
        val = get_val(r1,c1)
        overrides[(r2,c2)] = val

    elif op == 'SR':
        # SR r1 r2: swap rows r1 and r2 in current matrix
        r1,r2 = map(int,parts[1:])
        # swap rows in row_swap dict: apply to swap map
        # we must update row_swap mappings
        for k,v in list(row_swap.items()):
            # if key or value is swapped, remap accordingly before inserting swapped
            if k == r1:
                del row_swap[k]
                break
            if k == r2:
                del row_swap[k]
                break
        v1 = row_swap.pop(r1,r1)
        v2 = row_swap.pop(r2,r2)
        row_swap[r1] = v2
        row_swap[r2] = v1

        # If rows are reversed or orientation affects, need no extra here because we work always on logical indexes

    elif op == 'SC':
        # SC c1 c2: swap columns c1 and c2
        c1,c2 = map(int,parts[1:])
        for k,v in list(col_swap.items()):
            if k==c1:
                del col_swap[k]
                break
            if k==c2:
                del col_swap[k]
                break
        v1 = col_swap.pop(c1,c1)
        v2 = col_swap.pop(c2,c2)
        col_swap[c1] = v2
        col_swap[c2] = v1

    elif op == 'RL':
        # Rotate Left (90 deg ccw)
        # orientation cycles counter clockwise: 0->3->2->1->0
        orientation = (orientation - 1) %4

        # after rotation swap row and column swap maps
        row_swap, col_swap = col_swap, row_swap
        # after rotation, row_rev and col_rev swap and invert
        row_rev, col_rev = col_rev, row_rev

    elif op == 'RR':
        # Rotate Right (90 deg cw)
        orientation = (orientation + 1)%4
        row_swap, col_swap = col_swap, row_swap
        row_rev, col_rev = col_rev, row_rev

    elif op == 'RH':
        # reflect horizontal: reverse rows
        row_rev = not row_rev

    elif op == 'RV':
        # reflect vertical: reverse columns
        col_rev = not col_rev

# Finally compute hash over D..E and F..G on final matrix B

h = 314159265
for r in range(D,E+1):
    for c in range(F,G+1):
        val = get_val(r,c)
        h = (31*h + val) % MOD

print(h)