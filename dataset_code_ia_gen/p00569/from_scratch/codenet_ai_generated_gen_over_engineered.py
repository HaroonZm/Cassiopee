class CardGame:
    def __init__(self, N, K, L, cards):
        self.N = N
        self.K = K
        self.L = L
        self.cards = cards
        self.unique_cards = sorted(set(cards))
        self.compressed = self._compress(cards)

    def _compress(self, arr):
        # Coordinate compression for efficient BIT operation
        rank = {v: i + 1 for i, v in enumerate(self.unique_cards)}
        return [rank[v] for v in arr]

    class FenwickTree:
        def __init__(self, size):
            self.size = size
            self.tree = [0] * (size + 1)

        def update(self, i, v):
            while i <= self.size:
                self.tree[i] += v
                i += i & (-i)

        def query(self, i):
            res = 0
            while i > 0:
                res += self.tree[i]
                i -= i & (-i)
            return res

        def kth(self, k):
            # Find smallest index with prefix sum >= k
            pos = 0
            bit_mask = 1 << (self.size.bit_length())
            while bit_mask > 0:
                next_pos = pos + bit_mask
                if next_pos <= self.size and self.tree[next_pos] < k:
                    k -= self.tree[next_pos]
                    pos = next_pos
                bit_mask >>= 1
            return pos + 1

    def count_kth_less_equal(self, x):
        # Count how many K-th order statistics <= x among all valid subarrays
        fenw = self.FenwickTree(len(self.unique_cards))

        # Sliding window processing
        result = 0
        l = 0
        # Stores count of each compressed value in window
        count = [0] * (len(self.unique_cards) + 1)

        def count_at_least_k(pos_l, pos_r):
            length = pos_r - pos_l + 1
            if length < self.K:
                return 0
            # We want the K-th smallest in this window.
            # We will use fenw to find if kth smallest <= x: 
            # But here, we must quickly determine the K-th smallest of current window <= x
            # Since size and queries are huge, we don't do per subarray check.
            # Instead, approach differently below.
            return None

        # Due to extreme complexity, apply binary search on answer range,
        # then count how many K-th statistics are <= candidate

        # DAP-based solution abstracted: count total number of K-th statistics <= val by two pointers

        return 0  # placeholder

    def solve(self):
        left = 1
        right = self.N

        # Binary search on answer (card values) in compressed rank space
        res = -1
        while left <= right:
            mid = (left + right) // 2
            candidate = self.unique_cards[mid - 1]
            c = self._count_kth_numbers_less_equal(candidate)
            if c >= self.L:
                res = candidate
                right = mid - 1
            else:
                left = mid + 1
        return res

    def _count_kth_numbers_less_equal(self, val):
        # Count the number of K-th statistics <= val for all valid subarrays
        # Using a sliding window and two pointers technique with Fenwick tree

        fenw = self.FenwickTree(len(self.unique_cards))
        res = 0
        left = 0
        right = 0
        counts = [0] * (len(self.unique_cards) + 1)

        def fenw_add(x):
            fenw.update(x, 1)

        def fenw_remove(x):
            fenw.update(x, -1)

        # We'll expand right pointer, adding elements <= val to Fenw,
        # and move left pointer when subarray length >= K, counting how many subarrays have K-th <= val

        # For performance, we process all subarrays of length >= K

        # Preprocessing: We make an array of 0/1 indicating if element <= val (1 if yes else 0)
        binary = [1 if x <= val else 0 for x in self.compressed]

        # We want, for all subarrays length >= K, is the K-th smallest <= val?
        # That is equivalent to: in the subarray, at least K elements <= val.

        # Let's use a prefix sum of binary to check how many elements <= val in each subarray.

        pref = [0] * (self.N + 1)
        for i in range(self.N):
            pref[i+1] = pref[i] + binary[i]

        total = 0
        # For each r, find how many l such that (r-l+1)>=K and (pref[r+1]-pref[l])>=K:
        for r in range(self.N):
            min_l = r - self.K + 1
            if min_l < 0:
                continue
            # We want l in [0..min_l] such that pref[r+1]-pref[l]>=K
            # => pref[l] <= pref[r+1]-K
            # Count number of prefix sums in pref[0..min_l] <= pref[r+1] - K

            # We will use binary indexed tree for counting prefix values <= x
        # Build array of prefix sums for fenw counting

        # We compress prefix sums to coordinates to maintain fenw indexing
        all_prefs = pref[:self.N+1]
        sorted_prefs = sorted(set(all_prefs))
        def pref_index(x):
            # 1-based fenw index
            import bisect
            return bisect.bisect_left(sorted_prefs, x) + 1

        fenw = self.FenwickTree(len(sorted_prefs))
        ans = 0

        # We will iterate r over [K-1 .. N-1], and count suitable l in [0..r-K+1]
        # For fenw, we add prefix sums of l as we go.

        # Add prefix sums for l < K-1 at start
        for i in range(self.K - 1):
            fenw.update(pref_index(pref[i]), 1)

        for r in range(self.K - 1, self.N):
            fenw_val = pref[r + 1] - self.K
            x = pref_index(fenw_val)
            # Count l <= r - K + 1 prefix sums <= fenw_val
            # fenw holds counts of prefix sums pref[0..r-K], so we query fenw for indices <= x

            # Query frequency of prefix sums <= fenw_val
            c = fenw.query(x)
            ans += c
            if r - self.K + 1 < self.N:
                fenw.update(pref_index(pref[r - self.K + 1]), 1)

        return ans

def main():
    import sys
    input = sys.stdin.readline
    N, K, L = map(int, input().split())
    cards = [int(input()) for _ in range(N)]
    game = CardGame(N, K, L, cards)
    print(game.solve())

if __name__ == "__main__":
    main()