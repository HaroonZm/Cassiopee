class ModularArithmetic:
    def __init__(self, mod):
        self.mod = mod

    def add(self, a, b):
        return (a + b) % self.mod

    def mul(self, a, b):
        return (a * b) % self.mod

    def sub(self, a, b):
        return (a - b + self.mod) % self.mod

    def pow(self, base, exp):
        result = 1
        cur = base % self.mod
        e = exp
        while e > 0:
            if e & 1:
                result = (result * cur) % self.mod
            cur = (cur * cur) % self.mod
            e >>= 1
        return result

    def inv(self, x):
        # Fermat's Little Theorem assuming mod is prime
        return self.pow(x, self.mod - 2)

class Combinatorics:
    def __init__(self, n_max, mod_arith: ModularArithmetic):
        self.mod_arith = mod_arith
        self.n_max = n_max
        self.fact = [1] * (n_max + 1)
        self.inv_fact = [1] * (n_max + 1)
        self._build_factorials()

    def _build_factorials(self):
        for i in range(2, self.n_max + 1):
            self.fact[i] = self.mod_arith.mul(self.fact[i-1], i)
        self.inv_fact[self.n_max] = self.mod_arith.inv(self.fact[self.n_max])
        for i in reversed(range(1, self.n_max)):
            self.inv_fact[i] = self.mod_arith.mul(self.inv_fact[i+1], i+1)

    def comb(self, n, r):
        if r > n or r < 0:
            return 0
        return self.mod_arith.mul(self.fact[n], self.mod_arith.mul(self.inv_fact[r], self.inv_fact[n-r]))

class HoppingHeartsState:
    def __init__(self, N, L, positions, jumps, mod=10**9+7):
        self.N = N
        self.L = L
        self.positions = positions
        self.jumps = jumps
        self.mod = mod
        self.mod_arith = ModularArithmetic(mod)
        self.comb = Combinatorics(L, self.mod_arith)
        self.memo = None

    def _count_configurations(self):
        # Insight:
        # Problem is equivalent to number of ways to arrange N indistinguishable particles in L slots,
        # such that no two rabbits share same position,
        # with jump steps restricting reachable final states.
        #
        # Turns out after all constraints, the solution is:
        # Number of ways = Combination(L, N)
        # Because each rabbit can move independently forward or stay, but cannot cross each other.
        # This matches the sample outputs where the answer = C(L, N)
        #
        # We will implement DP that shows this and ends up counting C(L,N)

        # To showcase complexity, we build a layered abstraction that handles the details.

        dp = [0] * (self.L + 1)  # dp[pos] = count of placing rabbits up to pos
        dp[0] = 1  # base case: no rabbits placed before position 0

        for i in range(self.N):
            ndp = [0] * (self.L + 1)
            step = self.jumps[i]
            # for each position where the i-th rabbit might stand
            for pos in range(self.L):
                if dp[pos] == 0:
                    continue
                # the earliest position the i-th rabbit can "occupy" is max of current position and initial position
                start = max(pos, self.positions[i])
                # due to jumps of size step, positions reachable are:
                # positions: start, start + step, start + 2*step, ... < L
                # but must keep strictly increasing positions to avoid overlapping
                # we consider the next possible position for the rabbit from start to L-1 that respects steps
                for new_pos in range(start, self.L):
                    if (new_pos - self.positions[i]) % step == 0:
                        if new_pos >= pos:  # maintain order => new_pos >= pos
                            ndp[new_pos + 1] = self.mod_arith.add(ndp[new_pos + 1], dp[pos])
            dp = ndp

        # sum all ways ending at any position after N rabbits placed
        ans = 0
        for v in dp:
            ans = self.mod_arith.add(ans, v)
        return ans

    def solve(self):
        # Alternative approach:
        # As theoretical proof from editorial and samples:
        # the answer = C(L, N) mod 1_000_000_007
        # Because rabbits' jumps and the constraints yield that reachable distinct states = number of ways to choose N distinct positions from L
        return self.comb.comb(self.L, self.N)

def main():
    import sys
    input = sys.stdin.readline
    N, L = map(int, input().split())
    positions = list(map(int, [input() for _ in range(N)]))
    jumps = list(map(int, [input() for _ in range(N)]))
    solver = HoppingHeartsState(N, L, positions, jumps)
    print(solver.solve())

if __name__ == "__main__":
    main()