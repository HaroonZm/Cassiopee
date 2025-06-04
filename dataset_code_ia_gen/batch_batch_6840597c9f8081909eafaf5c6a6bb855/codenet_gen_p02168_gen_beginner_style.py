def double_or_increment():
    import sys
    input = sys.stdin.readline

    K = int(input())
    piles = [tuple(map(int, input().split())) for _ in range(K)]

    def nimber(n, m):
        # calc nimber for one pile
        # nimber is number of moves possible from this state
        # each move: either increment by 1 if n < m
        # or double (n*2) if n*2 <= m

        # we'll try all moves recursively, but as numbers are large,
        # this won't work straightforwardly for large inputs in practice;
        # but as requested, simple and direct implementation, non-optimal.

        # To approximate, we consider the options:
        # if n == m, no moves: nimber=0
        # else nimber is mex of nimbers after moves:
        # states: n+1 (if n+1 <= m), 2*n (if 2*n <= m)
        #
        # but to prevent infinite recursion with huge range,
        # we stop when n == m

        from functools import lru_cache

        @lru_cache(None)
        def dfs(x):
            if x == m:
                return 0
            moves = []
            if x + 1 <= m:
                moves.append(dfs(x + 1))
            if x * 2 <= m:
                moves.append(dfs(x * 2))
            # mex
            s = set(moves)
            r = 0
            while r in s:
                r += 1
            return r

        return dfs(n)

    # Compute xor of nimbers for all piles
    xor_sum = 0
    for n, m in piles:
        xor_sum ^= nimber(n, m)

    if xor_sum == 0:
        print("tubuann")
    else:
        print("mo3tthi")

if __name__ == "__main__":
    double_or_increment()