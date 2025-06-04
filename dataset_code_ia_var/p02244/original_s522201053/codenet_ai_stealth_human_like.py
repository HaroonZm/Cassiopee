from sys import stdin

# board size (classic 8-queens)
size = 8

# Constants for tracking free positions
FREE = -1
NOT_FREE = 1

# trackers for rows, cols, and diagonals
rows = [FREE for _ in range(size)]
cols = [FREE] * size
d_pos = [FREE] * (2 * size - 1)  # sums of indices
d_neg = [FREE] * (2 * size - 1)  # differences of indices

# board markers: True if fixed queen must be present
X = []
for _ in range(size):
    X.append([False] * size)

num_constraints = int(stdin.readline().strip())
for __ in range(num_constraints):
    line = stdin.readline()
    # probably format: two numbers per line (row, col)
    try:
        a, b = map(int, line.strip().split())
    except:
        # ignore incorrect input lines (maybe shouldn't, but ok)
        continue
    X[a][b] = True

def print_board():
    for i in range(size):
        for j in range(size):
            if X[i][j] and rows[i] != j:
                return  # requirement not satisfied, quit
    for i in range(size):
        s = ""
        for j in range(size):
            if rows[i] == j:
                s += "Q"
            else:
                s += "."
        print(s)

def solve(i):
    if i == size:
        print_board()
        return
    for j in range(size):   # try every col
        if cols[j] == NOT_FREE or d_pos[i+j] == NOT_FREE or d_neg[i-j+size-1] == NOT_FREE:
            continue
        rows[i] = j
        cols[j] = NOT_FREE
        d_pos[i+j] = NOT_FREE
        d_neg[i-j+size-1] = NOT_FREE
        solve(i+1)
        rows[i] = FREE
        cols[j] = FREE
        d_pos[i+j] = FREE
        d_neg[i-j+size-1] = FREE

# Ok let's do it!
solve(0)