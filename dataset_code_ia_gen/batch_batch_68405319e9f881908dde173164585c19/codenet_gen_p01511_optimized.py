MOD = 10**9 + 9

def matmul(a, b):
    m, n, p = len(a), len(a[0]), len(b[0])
    res = [[0]*p for _ in range(m)]
    for i in range(m):
        ai = a[i]
        for k in range(n):
            aik = ai[k]
            bk = b[k]
            for j in range(p):
                res[i][j] += aik * bk[j]
        for j in range(p):
            res[i][j] %= MOD
    return res

def matpow(mat, exp):
    res = [[0]*len(mat) for _ in range(len(mat))]
    for i in range(len(mat)):
        res[i][i] = 1
    base = mat
    e = exp
    while e:
        if e & 1:
            res = matmul(res, base)
        base = matmul(base, base)
        e >>= 1
    return res

def solve():
    import sys
    input = sys.stdin.readline

    case_num = 1
    while True:
        W,H,N = map(int, input().split())
        if W == 0 and H == 0 and N == 0:
            break
        blocked = set()
        for _ in range(N):
            x,y = map(int, input().split())
            blocked.add((x,y))
        # if start or end blocked (problem says start not blocked)
        if (W,H) in blocked:
            print(f"Case {case_num}: 0")
            case_num += 1
            continue

        # Positions are from 1 to W
        # At each row, dp vector size W with dp[x-1] ways to be at cell (x,row)
        # From row y to y+1:
        # dp_next[x] = sum of dp[x-1], dp[x], dp[x+1] if in grid and not blocked at (x,y+1)
        # We want dp at row H starting from dp at row 1 = (1 at x=1, 0 else)

        # For the transitions, construct W x W matrix M:
        # M[i,j] = 1 if j in {i-1, i, i+1} and cell (j+1,row+1) not blocked
        # i, j are 0-based column index at next row and current row respectively
        # dp_next = M * dp

        # For all rows same pattern of blocked cells applied, except y varies
        # But the block depends on y, so transitions differ by row
        # Need to do matrix exponentiation of product of matrices per row
        # But H can be 10^18, so can't do one by one

        # Optimization:
        # The blocked set has cells with given coordinates.
        # We need to incorporate blocking per row
        # So for each row, we define its transition matrix M_row
        # Then dp at row H = M_{H-1} * ... * M_1 * dp_1
        # With H potentially large, but only N obstructions (at most 30)
        # For rows without any obstruction, M_row is always the same matrix (the unrestricted transitions for that row)
        # So rows with blocks change the matrix, all other rows share one "free" matrix M_free
        # We cannot multiply per row since H large
        # So we group rows into segments of consecutive rows with no obstruction and rows with obstruction

        # Let's get all rows that have obstructions
        rows_with_blocks = {}
        for (x,y) in blocked:
            if y not in rows_with_blocks:
                rows_with_blocks[y] = set()
            rows_with_blocks[y].add(x)

        # Build M_free matrix (no blocked cells in row y+1)
        def build_matrix(blocked_cells):
            M = [[0]*W for _ in range(W)]
            for i in range(W):
                # i is row index of next row (0-based for row y+1)
                for j in [i-1,i,i+1]:
                    if 0 <= j < W:
                        if (j+1) not in blocked_cells:
                            M[i][j] = 1
            return M

        M_free = build_matrix(set())

        # We process from row 1 to row H-1 transitions
        # For rows y from 1 to H-1:
        # if y+1 in rows_with_blocks: M_y = build_matrix(rows_with_blocks[y+1])
        # else M_free

        # We collect the rows with blocks inside the range 2 to H
        block_rows = [r for r in rows_with_blocks if 2 <= r <= H]

        # We include H for clarity, but no transition at row H, transitions up to H-1 only
        block_rows = [r for r in block_rows if 1 <= r-1 <= H-1]

        # Sort block_rows
        block_rows.sort()

        # We split the range 1..H-1 in segments:
        # from cur to block_row-2 : free matrix powers
        # then at block_row-1: matrix for row block_row
        # Then continue

        dp0 = [0]*W
        dp0[0] = 1

        def mat_vec_mul(M, v):
            res = [0]*len(M)
            for i in range(len(M)):
                s = 0
                Mi = M[i]
                for j in range(len(v)):
                    s += Mi[j]*v[j]
                res[i] = s%MOD
            return res

        cur = 1
        v = dp0[:]
        for r in block_rows:
            # transition at row r-1 uses M_row with blocks at row r
            # apply free matrix power from cur to r-2 if cur <= r-2
            if cur <= r-2:
                power = r-2 - cur + 1
                Mf_pow = matpow(M_free, power)
                v = mat_vec_mul(Mf_pow, v)
            # apply matrix for row r-1 = row r with blocked cells
            M_block = build_matrix(rows_with_blocks[r])
            v = mat_vec_mul(M_block, v)
            cur = r

        # After last block row handled, apply free matrix power to end (H-1)
        if cur <= H-1:
            power = H-1 - cur + 1
            Mf_pow = matpow(M_free, power)
            v = mat_vec_mul(Mf_pow, v)

        # v now contains dp at row H
        # answer is v[W-1]
        print(f"Case {case_num}: {v[W-1] % MOD}")
        case_num += 1

if __name__ == "__main__":
    solve()