import sys

def rotate(pattern):
    m = len(pattern)
    return [[pattern[m - j - 1][i] for j in range(m)] for i in range(m)]

def get_actual_positions(pattern):
    positions = []
    for i,row in enumerate(pattern):
        for j,val in enumerate(row):
            if val != -1:
                positions.append((i,j,val))
    return positions

def matches_at(scenery, pattern_positions, x, y):
    for i, j, val in pattern_positions:
        if scenery[x + i][y + j] != val:
            return False
    return True

def find_matches(scenery, pattern_positions, n, m):
    matches = []
    for x in range(n - m + 1):
        for y in range(n - m + 1):
            if matches_at(scenery, pattern_positions, x, y):
                matches.append((x,y))
    return matches

input = sys.stdin.readline
while True:
    line = ''
    while line.strip() == '':
        line = input()
        if line == '':
            break
    if line == '':
        break
    n,m = map(int,line.split())
    if n == 0 and m == 0:
        break
    scenery = [list(map(int,input().split())) for _ in range(n)]
    pattern = [list(map(int,input().split())) for _ in range(m)]

    variants = []
    p = pattern
    for _ in range(4):
        variants.append(get_actual_positions(p))
        p = rotate(p)

    all_matches = []
    for variant in variants:
        all_matches.extend(find_matches(scenery, variant, n, m))

    if not all_matches:
        print('NA')
    else:
        # Find min top row; if tie, min left column
        all_matches.sort(key=lambda x: (x[0], x[1]))
        x,y = all_matches[0]
        print(x+1,y+1)