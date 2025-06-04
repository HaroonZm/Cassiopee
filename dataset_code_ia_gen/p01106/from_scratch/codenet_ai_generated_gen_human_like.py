def solve():
    import sys
    sys.setrecursionlimit(10**7)

    def find_sequence(n, i, j):
        if n == 0:
            return ""
        half = 1 << (n - 1)
        if i <= half:
            # marked layer in top half => fold was from left to right 'L'
            if j <= half:
                # marked part in left half
                return "L" + find_sequence(n - 1, i, j)
            else:
                # marked part in right half
                return "L" + find_sequence(n - 1, i, j - half)
        else:
            # marked layer in bottom half => fold was from right to left 'R'
            i -= half
            if j <= half:
                # marked part in left half
                return "R" + find_sequence(n - 1, i, half - j + 1)
            else:
                # marked part in right half
                return "R" + find_sequence(n - 1, i, j - half)

    for line in sys.stdin:
        if not line.strip():
            continue
        n, i, j = map(int, line.strip().split())
        if n == 0 and i == 0 and j == 0:
            break
        print(find_sequence(n, i, j))