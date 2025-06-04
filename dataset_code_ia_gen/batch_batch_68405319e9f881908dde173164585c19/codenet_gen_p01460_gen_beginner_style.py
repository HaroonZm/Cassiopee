import sys
sys.setrecursionlimit(10**7)

N, Q, A, B, C, D, E, F, G = map(int, input().split())

# initial matrix function
def get_val(r, c):
    return (r * A + c * B) % C

# We will simulate the matrix by storing the 
# operations on indices and values written
# Because N and Q can be large, but we do a simple approach

# We keep track of transformations:
# row_map and col_map: maps from position in transformed matrix to initial matrix

row_map = list(range(1, N+1))
col_map = list(range(1, N+1))

# For rotations and reflections we will update row_map and col_map accordingly
# For written cells we keep a dictionary {(r,c):v}
written = {}

def swap_rows(r1, r2):
    row_map[r1-1], row_map[r2-1] = row_map[r2-1], row_map[r1-1]

def swap_cols(c1, c2):
    col_map[c1-1], col_map[c2-1] = col_map[c2-1], col_map[c1-1]

def rotate_left():
    # rotate counter clockwise 90
    # new row r = old col c
    # new col c = N - old row r + 1
    # so we build new row_map and col_map:
    new_row_map = [0]*N
    new_col_map = [0]*N
    for i in range(N):
        new_row_map[i] = col_map[i]
        new_col_map[i] = N - row_map[i] + 1
    return new_row_map, new_col_map

def rotate_right():
    # rotate clockwise 90
    # new row r = N - old col c + 1
    # new col c = old row r
    new_row_map = [0]*N
    new_col_map = [0]*N
    for i in range(N):
        new_row_map[i] = N - col_map[i] + 1
        new_col_map[i] = row_map[i]
    return new_row_map, new_col_map

def reflect_horizontal():
    # reverse rows
    new_row_map = [0]*N
    for i in range(N):
        new_row_map[i] = row_map[N - i - 1]
    return new_row_map

def reflect_vertical():
    # reverse columns
    new_col_map = [0]*N
    for i in range(N):
        new_col_map[i] = col_map[N - i - 1]
    return new_col_map

for _ in range(Q):
    line = input().split()
    op = line[0]
    if op == 'WR':
        r, c, v = map(int, line[1:])
        # map (r,c) to initial position
        ri = row_map[r-1]
        ci = col_map[c-1]
        written[(ri, ci)] = v
    elif op == 'CP':
        r1, c1, r2, c2 = map(int, line[1:])
        ri1 = row_map[r1-1]
        ci1 = col_map[c1-1]
        ri2 = row_map[r2-1]
        ci2 = col_map[c2-1]
        # get value from (ri1, ci1)
        if (ri1, ci1) in written:
            val = written[(ri1, ci1)]
        else:
            val = get_val(ri1, ci1)
        written[(ri2, ci2)] = val
    elif op == 'SR':
        r1, r2 = map(int, line[1:])
        swap_rows(r1, r2)
    elif op == 'SC':
        c1, c2 = map(int, line[1:])
        swap_cols(c1, c2)
    elif op == 'RL':
        row_map, col_map = rotate_left()
    elif op == 'RR':
        row_map, col_map = rotate_right()
    elif op == 'RH':
        row_map = reflect_horizontal()
    elif op == 'RV':
        col_map = reflect_vertical()

mod = 1000000007
h = 314159265

for r in range(D, E+1):
    for c in range(F, G+1):
        ri = row_map[r-1]
        ci = col_map[c-1]
        if (ri, ci) in written:
            val = written[(ri, ci)]
        else:
            val = get_val(ri, ci)
        h = (31 * h + val) % mod

print(h)