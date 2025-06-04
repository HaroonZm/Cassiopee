def solve():
    import sys

    sys.setrecursionlimit(10000)
    
    def find_folds(n, i, j):
        # n: number of folds
        # i: marked layer (from top)
        # j: marked part (from left)
        if n == 0:
            return ""
        half = 2 ** (n - 1)
        if i <= half and j > half:
            # mark in left half (bottom fold goes on top)
            # fold was from Left to Right (L)
            return 'L' + find_folds(n - 1, i, j - half)
        elif i <= half and j <= half:
            # mark in right half (top fold goes on bottom)
            # fold was from Right to Left (R)
            return 'R' + find_folds(n - 1, i, j)
        elif i > half and j <= half:
            # mark in left half (bottom fold goes on top)
            # fold was from Left to Right (L)
            return 'L' + find_folds(n - 1, i - half, j)
        else:
            # i > half and j > half
            # fold was from Right to Left (R)
            return 'R' + find_folds(n - 1, i - half, j - half)

    for line in sys.stdin:
        n, i, j = map(int, line.split())
        if n == 0 and i == 0 and j == 0:
            break
        print(find_folds(n, i, j))