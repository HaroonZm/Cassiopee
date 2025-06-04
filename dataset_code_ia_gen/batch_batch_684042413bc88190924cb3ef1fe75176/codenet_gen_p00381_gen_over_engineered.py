class WarpMachineRouting:
    MOD = 10**9 + 7

    class LetterIndexMapper:
        def __init__(self):
            # Maps character to list of indices (1-based)
            self._map = {chr(c): [] for c in range(ord('a'), ord('z') + 1)}

        def add(self, ch: str, index: int):
            self._map[ch].append(index)

        def get_indices(self, ch: str):
            return self._map[ch]

    class FenwickTree:
        def __init__(self, size: int):
            self.size = size
            self.tree = [0] * (size + 1)

        def update(self, index: int, value: int):
            while index <= self.size:
                self.tree[index] = (self.tree[index] + value) % WarpMachineRouting.MOD
                index += index & (-index)

        def query(self, index: int):
            s = 0
            while index > 0:
                s = (s + self.tree[index]) % WarpMachineRouting.MOD
                index -= index & (-index)
            return s

        def range_query(self, left: int, right: int):
            if right < left:
                return 0
            return (self.query(right) - self.query(left - 1)) % WarpMachineRouting.MOD

    def __init__(self, N: int, s: str, t: str):
        self.N = N
        self.s = s
        self.t = t
        self.s_mapper = self.LetterIndexMapper()
        self.dp = [0] * (N + 1)
        self.fenwicks = {ch: self.FenwickTree(N) for ch in set(s)}

        # Preprocess indices by entrance letter s[i]
        for i, ch in enumerate(s, start=1):
            self.s_mapper.add(ch, i)

    def compute_routes(self):
        # Base case: from star 1, 1 way to start
        self.dp[1] = 1
        # Initialize Fenwick Trees for dp updates
        self.fenwicks[self.s[0]].update(1, 1)

        for i in range(2, self.N + 1):
            # For planet i, t[i-1] is the exit letter
            exit_letter = self.t[i - 1]
            # For all entrances with s_j == exit_letter and j < i
            fenw = self.fenwicks.get(exit_letter)
            if fenw is None:
                self.dp[i] = 0
                continue
            # sum dp[j] over j < i and s_j == exit_letter
            self.dp[i] = fenw.query(i - 1) % self.MOD
            # Update fenwicks for s[i] with dp[i]
            self.fenwicks[self.s[i - 1]].update(i, self.dp[i])

        return self.dp[self.N] % self.MOD


def main():
    import sys
    sys.setrecursionlimit(10**7)
    N = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()
    t = sys.stdin.readline().strip()
    routing = WarpMachineRouting(N, s, t)
    print(routing.compute_routes())

if __name__ == "__main__":
    main()