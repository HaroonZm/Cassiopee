class Modulo:
    def __init__(self, modulus):
        self.modulus = modulus

    def add(self, a, b):
        return (a + b) % self.modulus

    def sub(self, a, b):
        return (a - b) % self.modulus

    def mul(self, a, b):
        return (a * b) % self.modulus


class FenwickTree:
    def __init__(self, size, modulo):
        self.size = size
        self.mod = modulo
        self.tree = [0] * (size + 1)

    def update(self, idx, val):
        while idx <= self.size:
            self.tree[idx] = self.mod.add(self.tree[idx], val)
            idx += idx & -idx

    def query(self, idx):
        s = 0
        while idx > 0:
            s = self.mod.add(s, self.tree[idx])
            idx -= idx & -idx
        return s

    def range_query(self, left, right):
        if left > right:
            return 0
        return self.mod.sub(self.query(right), self.query(left - 1))


class RabbitGame:
    def __init__(self, n, t, difficulties):
        self.n = n
        self.t = t
        self.difficulties = difficulties
        self.MOD = 10**9 + 7
        self.mod = Modulo(self.MOD)
        self.max_difficulty = max(difficulties)
        self.fenwick = FenwickTree(self.max_difficulty, self.mod)

    def compress_difficulties(self):
        unique_sorted = sorted(set(self.difficulties))
        self.rank_map = {}
        for i, val in enumerate(unique_sorted, start=1):
            self.rank_map[val] = i
        self.compressed = [self.rank_map[d] for d in self.difficulties]
        self.max_rank = len(unique_sorted)
        # Fenwick tree size must be max_rank
        self.fenwick = FenwickTree(self.max_rank, self.mod)

    def compute_ways(self):
        self.compress_difficulties()
        ways = [0] * self.n
        for i in range(self.n):
            x = self.compressed[i]
            start = max(1, x - self.t)
            end = x - 1
            # Sum of ways for previous difficulties in [start, end]
            s = self.fenwick.range_query(start, end)
            # If no previous smaller or eligible, this stage alone counts as 1 way
            ways[i] = self.mod.add(s, 1)
            self.fenwick.update(x, ways[i])
        total = 1
        for w in ways:
            total = self.mod.mul(total, w)
        return total


def main():
    import sys
    input = sys.stdin.readline

    n, t = map(int, input().split())
    difficulties = [int(input()) for _ in range(n)]
    game = RabbitGame(n, t, difficulties)
    print(game.compute_ways())

if __name__ == '__main__':
    main()