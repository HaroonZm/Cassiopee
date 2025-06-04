import sys
sys.setrecursionlimit(10**7)

MOD = 998244353

class ModInt:
    def __init__(self, value):
        self.value = value % MOD

    def __add__(self, other):
        if isinstance(other, ModInt):
            return ModInt(self.value + other.value)
        else:
            return ModInt(self.value + other)
    def __sub__(self, other):
        if isinstance(other, ModInt):
            return ModInt(self.value - other.value)
        else:
            return ModInt(self.value - other)
    def __mul__(self, other):
        if isinstance(other, ModInt):
            return ModInt(self.value * other.value)
        else:
            return ModInt(self.value * other)
    def __pow__(self, exponent):
        return ModInt(pow(self.value, exponent, MOD))
    def inv(self):
        return ModInt(pow(self.value, MOD - 2, MOD))
    def __truediv__(self, other):
        if isinstance(other, ModInt):
            return self * other.inv()
        else:
            return self * ModInt(other).inv()
    def __int__(self):
        return self.value
    def __repr__(self):
        return f"ModInt({self.value})"

class ProbabilityModel:
    def __init__(self, N, K, A):
        self.N = N
        self.K = K
        self.A = A
        self.mod = MOD
        self.p_head = ModInt(A) / 100
        self.p_tail = ModInt(100 - A) / 100
        self.invN = ModInt(self.N).inv()
        # probabilities dp[i] = probability to clear game from score i
        self.dp = [ModInt(0)] * (K + N + 1)
        self.prefix = [ModInt(0)] * (K + N + 2)
        self._compute_dp()

    def _compute_dp(self):
        # dp[i] = probability to clear game starting at score i
        
        K = self.K
        N = self.N
        p_head = self.p_head
        p_tail = self.p_tail
        invN = self.invN
        
        max_index = K + N
        dp = [ModInt(0) for _ in range(max_index + 1)]
        prefix = [ModInt(0) for _ in range(max_index + 2)]

        # For states >= K, probability is 1 (game cleared)
        for i in range(K, max_index + 1):
            dp[i] = ModInt(1)
        # Build prefix sum
        # prefix[i] = sum_{j=i}^{max_index} dp[j]
        prefix[max_index + 1] = ModInt(0)
        for i in range(max_index, -1, -1):
            prefix[i] = prefix[i+1] + dp[i]

        # Iterative DP from K-1 down to 0
        for i in range(K - 1, -1, -1):
            # Expected probability if succeed coin toss and roll die:
            # sum of dp[i+x] for x=1..N divided by N
            # This is prefix[i+1] - prefix[i+1+N] all divided by N
            segment_sum = prefix[i+1] - prefix[i+1+N]
            # dp[i] = p_tail * 0 + p_head * (average dp of next states)
            dp[i] = p_head * (segment_sum * invN) + p_tail * ModInt(0)
            prefix[i] = prefix[i+1] + dp[i]

        self.dp = dp

    def get_result(self):
        # The probability starting at 0 score is dp[0]
        # dp[0] = P/Q mod with P and Q coprime
        # Result = R where R * Q % MOD == P
        p = self.dp[0].value
        # Represent dp[0] as p/q mod MOD. Here dp[0] is already mod int,
        # so p = dp[0].value, q = 1 (since dp is ModInt)
        # But dp[0] may represent a fraction internally,
        # So we need to find p/q such that dp[0] = p/q mod MOD.
        # Actually, dp[i] values are ModInt, but internally stored as value mod MOD.
        # The issue is that dp[i] is computed by ModInt ops -> p/q mod MOD only implicitly
        #
        # To comply exactly with the requirement,
        # since all operations are mod inverses, dp[0].value represents R directly.
        # Actually, dp[0] as ModInt is already the integer R to output.
        #
        # So just output dp[0].value, which satisfies R * 1 = R = dp[0].value mod MOD
        return p

class InputParser:
    def __init__(self):
        self.N = None
        self.K = None
        self.A = None

    def parse(self):
        line = sys.stdin.readline()
        self.N, self.K, self.A = map(int, line.strip().split())

class CoinAndDieGame:
    def __init__(self):
        self.input_parser = InputParser()
        self.model = None

    def solve(self):
        self.input_parser.parse()
        self.model = ProbabilityModel(self.input_parser.N, self.input_parser.K, self.input_parser.A)
        ans = self.model.get_result()
        print(ans)

if __name__ == "__main__":
    game = CoinAndDieGame()
    game.solve()