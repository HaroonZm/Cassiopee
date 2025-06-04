import sys
sys.setrecursionlimit(10**7)

def parse_sequence(s, n):
    i = 0
    length = len(s)

    def parse_number():
        nonlocal i
        num = 0
        while i < length and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1
        return num

    def parse_op():
        nonlocal i
        shift = s[i]
        i += 1
        num = parse_number()
        return [(shift, num)]

    def parse_seq():
        nonlocal i
        res = []
        while i < length:
            if s[i] == '(':
                i += 1
                inner = parse_seq()
                if i >= length or s[i] != ')':
                    # should not happen due to problem guarantee
                    return res
                i += 1
                rep = parse_number()
                # multiply inner
                if rep > 0:
                    # to avoid huge repetition, we will store repetitions as (pattern, count)
                    res.append(('rep', inner, rep))
            elif s[i] in "LRUD":
                op = parse_op()
                res.extend(op)
            else:
                break
        return res

    return parse_seq()

def flatten(ops):
    # Flatten nested repetitions into a list of operations with counts, without repeating huge times explicitly
    # We'll represent ops as a list:
    # - ('rep', pattern, count)
    # - (shift,char)
    # We want to flatten into a list of operations as (shift, index, count)
    # But count only applies when we have repetitions; for simple operations count=1
    # We'll flatten so that repetitions are explicit in count, but the pattern stays as list of ops (not repeated)

    res = []

    def helper(ops, times):
        for op in ops:
            if isinstance(op, tuple) and op[0] == 'rep':
                pattern = op[1]
                count = op[2]
                helper(pattern, times * count)
            else:
                # op is (shift, idx)
                res.append((op[0], op[1], times))

    helper(ops, 1)
    return res

def mod_shift(shift, idx, times, N):
    times %= N
    return (shift, idx, times)

def apply_operations(N, operations):
    # Initialize arrays for row shifts and column shifts
    # row_shifts[i]: net right shifts applied to row i (0-based)
    # col_shifts[j]: net down shifts applied to column j (0-based)
    row_shifts = [0]*N
    col_shifts = [0]*N

    for op in operations:
        shift, idx, times = op
        # idx is 1-based in input
        i = idx - 1
        times %= N  # circular shifts modulo N
        if times == 0:
            continue
        if shift == 'L':
            # left shift i: equivalent to right shift by N - times
            row_shifts[i] = (row_shifts[i] - times) % N
        elif shift == 'R':
            row_shifts[i] = (row_shifts[i] + times) % N
        elif shift == 'U':
            # up shift j: equivalent to down shift by N - times
            col_shifts[i] = (col_shifts[i] - times) % N
        elif shift == 'D':
            col_shifts[i] = (col_shifts[i] + times) % N

    # Build the resulting matrix
    A = [[(i*N + j + 1) for j in range(N)] for i in range(N)]

    res = [[0]*N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            # The element originally at (r,c) moves according to:
            # row r shifted right by row_shifts[r], so element from (r, (c - row_shifts[r])%N)
            # column c shifted down by col_shifts[c], so element from ((r - col_shifts[c])%N, c)
            # Combining these two:
            # The final position (r,c) stores original element at ((r - col_shifts[c])%N, (c - row_shifts[r])%N)
            rr = (r - col_shifts[c]) % N
            cc = (c - row_shifts[r]) % N
            res[r][c] = A[rr][cc]

    return res


def main():
    import sys
    input = sys.stdin.readline

    N, L = map(int, input().split())
    S = input().strip()

    parsed = parse_sequence(S, N)
    ops = flatten(parsed)
    # condense ops of same (shift, idx):
    from collections import defaultdict
    count_map = defaultdict(int)
    for o in ops:
        count_map[(o[0], o[1])] += o[2]

    ops_final = []
    for (shift, idx), times in count_map.items():
        times_mod = times % N if shift in 'LR' else times % N
        if times_mod != 0:
            ops_final.append((shift, idx, times_mod))

    res = apply_operations(N, ops_final)

    for row in res:
        print(' '.join(map(str, row)))

if __name__ == "__main__":
    main()