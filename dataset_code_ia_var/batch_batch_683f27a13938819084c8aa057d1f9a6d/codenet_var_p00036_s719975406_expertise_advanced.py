from operator import itemgetter

ANS = 'ABCDEFG'
# Patterns: (list of (deltas), return index)
PATTERNS = [
    ([(0,0), (1,0), (0,1), (1,1)],           0),  # 2x2 square
    ([(0,0), (1,0), (2,0), (3,0)],           1),  # vertical 4
    ([(0,0), (0,1), (0,2), (0,3)],           2),  # horizontal 4
    ([(0,0), (1,0), (1,-1), (2,-1)],         3),  # L left-down
    ([(0,0), (0,1), (1,1), (1,2)],           4),  # step
    ([(0,0), (1,0), (1,1), (2,1)],           5),  # S
    ([(0,0), (0,1), (1,0), (1,-1)],          6),  # T
]

def in_bounds(i, j, deltas):
    # Returns True if all (i+di, j+dj) stay within board
    return all(0 <= i+di < 8 and 0 <= j+dj < 8 for di,dj in deltas)

def check_pattern(x, i, j, deltas):
    # Fast pattern check using all()
    try:
        return all(x[i+di][j+dj] == '1' for di, dj in deltas)
    except IndexError:
        return False

def get(x):
    # For each cell, try each pattern only if in bounds
    for i in range(8):
        for j in range(8):
            for deltas, idx in PATTERNS:
                if in_bounds(i, j, deltas) and check_pattern(x, i, j, deltas):
                    return idx

def main():
    import sys
    input_fn = raw_input if 'raw_input' in globals() else input
    while True:
        l = []
        try:
            l = [input_fn() for _ in range(8)]
            print(ANS[get(l)])
            input_fn()
        except Exception:
            break

if __name__ == "__main__":
    main()