class PlushToyOrganizer:
    class PlushToy:
        def __init__(self, kind: int):
            self.kind = kind

        def __repr__(self):
            return f"PlushToy({self.kind})"

    class Shelf:
        def __init__(self, toys: list):
            self.toys = toys  # list of PlushToy objects
            self.N = len(toys)

        def kinds(self):
            return [toy.kind for toy in self.toys]

    class KindData:
        def __init__(self, kind: int):
            self.kind = kind
            self.positions = []  # positions of this kind in shelf, 0-based index
            self.count = 0

        def add_position(self, pos: int):
            self.positions.append(pos)
            self.count += 1

    class DPTable:
        def __init__(self, M: int):
            self.M = M
            # Initialize dp table for bitmask states: minimum removals
            self.dp = [float('inf')] * (1 << M)
            self.dp[0] = 0

        def update(self, mask, cost):
            if cost < self.dp[mask]:
                self.dp[mask] = cost

        def __getitem__(self, index):
            return self.dp[index]

        def __setitem__(self, index, value):
            self.dp[index] = value

    def __init__(self, N: int, M: int, toy_kinds: list[int]):
        self.N = N
        self.M = M
        self.shelf = PlushToyOrganizer.Shelf([PlushToyOrganizer.PlushToy(k) for k in toy_kinds])
        self.kind_data = [PlushToyOrganizer.KindData(kind) for kind in range(1, M+1)]
        self.total_count = 0
        self._aggregate_data()

    def _aggregate_data(self):
        for i, toy in enumerate(self.shelf.toys):
            self.kind_data[toy.kind-1].add_position(i)
        self.total_count = self.N

    def _count_ones(self, bits: int) -> int:
        # Brian Kernighan’s Algorithm
        count = 0
        while bits:
            bits &= bits - 1
            count += 1
        return count

    def _precompute_suffix_counts(self):
        # Precompute count of kind k in the whole shelf (already done)
        # Precompute prefix sums of kind counts at each possible position
        self.prefix_kind_counts = [[0]*(self.N+1) for _ in range(self.M)]
        for i in range(self.N):
            kind = self.shelf.toys[i].kind - 1
            for k in range(self.M):
                self.prefix_kind_counts[k][i+1] = self.prefix_kind_counts[k][i]
            self.prefix_kind_counts[kind][i+1] += 1

    def _compute_cost_for_arrangement(self, order: list[int]):
        # For an order of kinds, compute how many toys must be moved out minimally
        # The contiguous blocks in order:
        # compute the segment lengths for each kind from the counts
        # then, for each block interval, we count how many of that kind are inside
        # the cost to keep correct is the total count of that kind minus those already positioned in that block

        pos = 0
        cost = 0
        # prefix counts are useful to compute how many of kind k are in [l, r)
        for kind in order:
            c = self.kind_data[kind].count
            l = pos
            r = pos + c
            # count of kind in this segment = prefix_kind_counts[kind][r] - prefix_kind_counts[kind][l]
            in_segment = self.prefix_kind_counts[kind][r] - self.prefix_kind_counts[kind][l]
            cost += c - in_segment  # how many need to be moved out to get a block fully of that kind
            pos += c
        return cost

    def solve(self) -> int:
        self._precompute_suffix_counts()
        # Bit DP: State = which kinds have been placed (0..M-1)
        # For each dp state, maintain minimal cost of removals for placing those kinds contiguous in some order.
        dp = [float('inf')] * (1 << self.M)
        dp[0] = 0
        # pre-store counts for kind indices
        counts = [self.kind_data[k].count for k in range(self.M)]

        for mask in range(1 << self.M):
            if dp[mask] == float('inf'):
                continue
            pos = sum(counts[k] for k in range(self.M) if (mask & (1 << k)))
            # Try to place any kind not in mask next
            for nxt in range(self.M):
                if (mask & (1 << nxt)) != 0:
                    continue
                c = counts[nxt]
                l, r = pos, pos + c
                in_segment = self.prefix_kind_counts[nxt][r] - self.prefix_kind_counts[nxt][l]
                cost_to_add = c - in_segment
                next_mask = mask | (1 << nxt)
                new_cost = dp[mask] + cost_to_add
                if new_cost < dp[next_mask]:
                    dp[next_mask] = new_cost
        return dp[(1 << self.M) - 1]

def main():
    import sys
    sys.setrecursionlimit(10**7)

    class Reader:
        def __init__(self):
            self.buffer = sys.stdin.read().split()
            self.idx = 0

        def int(self):
            val = int(self.buffer[self.idx])
            self.idx += 1
            return val

    reader = Reader()
    N = reader.int()
    M = reader.int()
    toy_kinds = [reader.int() for _ in range(N)]

    organizer = PlushToyOrganizer(N, M, toy_kinds)
    answer = organizer.solve()
    print(answer)

if __name__ == "__main__":
    main()