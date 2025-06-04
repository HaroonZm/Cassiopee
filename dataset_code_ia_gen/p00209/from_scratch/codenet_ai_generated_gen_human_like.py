def rotate_90(mat):
    m = len(mat)
    res = [[0]*m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            res[j][m-1-i] = mat[i][j]
    return res

def get_pattern_positions(p):
    positions = []
    for i,row in enumerate(p):
        for j,val in enumerate(row):
            if val != -1:
                positions.append((i,j,val))
    return positions

def match_at(w, p_positions, x, y):
    for i,j,val in p_positions:
        if w[x+i][y+j] != val:
            return False
    return True

def main():
    import sys
    input = sys.stdin.readline

    while True:
        line = ''
        while line.strip() == '':
            line = input()
            if not line:
                return
        n,m = map(int,line.split())
        if n == 0 and m == 0:
            break
        w = [list(map(int,input().split())) for _ in range(n)]
        p = [list(map(int,input().split())) for _ in range(m)]

        # Precompute rotations of p
        patterns = [p]
        for _ in range(3):
            patterns.append(rotate_90(patterns[-1]))

        # For each pattern, precompute positions of cells with >=0 values
        patterns_pos = [get_pattern_positions(pt) for pt in patterns]

        candidates = []
        for k in range(4):
            ppos = patterns_pos[k]
            max_i = n - m
            max_j = n - m
            for i in range(max_i+1):
                for j in range(max_j+1):
                    if match_at(w, ppos, i, j):
                        # find top-left cell in pattern with value >=0
                        min_r = min(pos[0] for pos in ppos)
                        min_c = min(pos[1] for pos in ppos)
                        # the coordinate in scenery top-left is (i + min_r, j + min_c)
                        candidates.append((i+min_r, j+min_c))

        if not candidates:
            print('NA')
        else:
            candidates.sort()
            print(candidates[0][0], candidates[0][1])

if __name__ == '__main__':
    main()