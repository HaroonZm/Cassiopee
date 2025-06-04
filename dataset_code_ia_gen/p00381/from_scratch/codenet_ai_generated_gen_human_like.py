MOD = 10**9 + 7

def main():
    N = int(input())
    s = input().strip()
    t = input().strip()

    # dp[i]: number of routes to reach star i+1 (0-based)
    dp = [0] * N
    dp[0] = 1  # start from star 1

    # For each letter 'a' to 'z', track cumulative count of dp for stars whose entrance is c and dp[j] is computed
    # For optimization, we will maintain prefix sums per letter to quickly compute sums of dp[j] where s[j] == c and j < i
    from collections import defaultdict

    # positions_by_letter: for each letter in s, store indices sorted ascending
    positions_by_letter = defaultdict(list)
    for i, c in enumerate(s):
        positions_by_letter[c].append(i)

    # To facilitate quick queries of sum dp[j] for j < i and s[j] == c,
    # we use Fenwick tree (BIT) per letter
    class Fenwick:
        def __init__(self, size):
            self.N = size
            self.tree = [0] * (size + 1)

        def update(self, i, v):
            i += 1
            while i <= self.N:
                self.tree[i] = (self.tree[i] + v) % MOD
                i += i & (-i)

        def query(self, i):
            # sum from 0 to i-1
            res = 0
            while i > 0:
                res = (res + self.tree[i]) % MOD
                i -= i & (-i)
            return res

        def query_less(self, pos):
            # sum of values with index < pos
            return self.query(pos)

    # For each letter, create a Fenwick tree of size = number of occurrences
    fenwicks = {}
    for c in positions_by_letter:
        fenwicks[c] = Fenwick(len(positions_by_letter[c]))

    # To locate for star i, the index of i in positions_by_letter[s[i]] list (for fenwicks)
    index_in_letter = {}
    for c in positions_by_letter:
        for idx, pos in enumerate(positions_by_letter[c]):
            index_in_letter[pos] = idx

    for i in range(1, N):
        c = t[i]
        # We want sum of dp[j] for all j < i and s[j] == c
        # Use fenwicks[c], get sum of dp for positions less than i
        # Need to find among positions_by_letter[c], all positions < i
        pos_list = positions_by_letter[c]
        # Binary search to find how many positions < i
        import bisect
        cnt = bisect.bisect_left(pos_list, i)
        if cnt == 0:
            val = 0
        else:
            val = fenwicks[c].query_less(cnt)
        dp[i] = val % MOD

        # After dp[i] computed, update fenwicks for letter s[i] at position of i
        fenwicks_s = fenwicks.get(s[i])
        if fenwicks_s is not None:
            idx_in_s = index_in_letter[i]
            fenwicks_s.update(idx_in_s, dp[i])

    print(dp[N-1] % MOD)

if __name__ == "__main__":
    main()