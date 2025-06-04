class IntegerRange:
    def __init__(self, start: str, end: str):
        self.start = BigInteger(start)
        self.end = BigInteger(end)

    def __iter__(self):
        current = self.start
        while current <= self.end:
            yield current
            current = current.increment()

class BigInteger:
    def __init__(self, value: str):
        self.value = value.lstrip('0') or '0'

    def __str__(self):
        return self.value

    def __le__(self, other: 'BigInteger'):
        if len(self.value) != len(other.value):
            return len(self.value) < len(other.value)
        return self.value <= other.value

    def increment(self) -> 'BigInteger':
        # Increment big integer string by 1
        digits = list(map(int, self.value))
        i = len(digits) - 1
        while i >= 0:
            if digits[i] < 9:
                digits[i] += 1
                break
            digits[i] = 0
            i -= 1
        if i < 0:
            digits.insert(0, 1)
        return BigInteger(''.join(map(str, digits)))

class OccurrenceCounter:
    def __init__(self, pattern: str):
        self.pattern = pattern
        self.mod = 10**9 + 7

    def count_in(self, number: str) -> int:
        # Counts overlapping occurrences of pattern in number string
        count = 0
        start = 0
        while True:
            idx = number.find(self.pattern, start)
            if idx == -1:
                break
            count += 1
            start = idx + 1
        return count

    def count_in_range_brute_force(self, interval: IntegerRange) -> int:
        # Brute force method for relatively small intervals
        total = 0
        for num in interval:
            total += self.count_in(str(num))
            total %= self.mod
        return total

class ProblemSolver:
    def __init__(self, A: str, B: str, C: str):
        self.A = BigInteger(A)
        self.B = BigInteger(B)
        self.C = C
        self.counter = OccurrenceCounter(C)
        self.mod = 10**9 + 7

    def solve(self) -> int:
        # Due to potentially extremely large inputs, brute force is infeasible.
        # We will use digit-DP to count how many times C appears in all numbers in [0, X].
        # Then use count(X) difference for interval [A,B].
        return (self.count_up_to(self.B) - self.count_up_to(self.A.increment()) + self.mod) % self.mod

    def count_up_to(self, X: BigInteger) -> int:
        digits = list(map(int, X.value))
        pattern = list(map(int, self.C))
        plen = len(pattern)
        mod = self.mod

        # Build KMP automaton to efficiently track pattern matching
        kmp_next = [0] * plen
        j = 0
        for i in range(1, plen):
            while j > 0 and pattern[i] != pattern[j]:
                j = kmp_next[j-1]
            if pattern[i] == pattern[j]:
                j += 1
            kmp_next[i] = j

        from functools import lru_cache

        @lru_cache(None)
        def dp(pos: int, matched: int, smaller: bool, started: bool) -> int:
            if pos == len(digits):
                return 0
            res = 0
            limit = digits[pos] if not smaller else 9
            for dig in range(0, limit + 1):
                nm = matched
                while nm > 0 and dig != pattern[nm]:
                    nm = kmp_next[nm-1]
                if dig == pattern[nm]:
                    nm += 1
                add = 1 if nm == plen else 0
                nsmaller = smaller or (dig < limit)
                nstarted = started or dig > 0
                res += add + dp(pos + 1, nm if nz else 0, nsmaller, nstarted)
                res %= mod
            return res % mod

        # correction: for initial zero prefix handling, pattern might appear starting at position 0 even with leading zeros
        # So just run dp and sum all occurrences counted during number generation.
        # The dp returns occurrences for suffix from pos, so we count total occurrences when matched == plen.

        @lru_cache(None)
        def dp2(pos: int, matched: int, smaller: bool, started: bool) -> int:
            if pos == len(digits):
                return 0
            res = 0
            limit = digits[pos] if not smaller else 9
            for dig in range(0, limit + 1):
                nm = matched
                while nm > 0 and dig != pattern[nm]:
                    nm = kmp_next[nm-1]
                if dig == pattern[nm]:
                    nm += 1
                add = 1 if nm == plen else 0
                nsmaller = smaller or (dig < limit)
                nstarted = started or dig > 0
                res += add + dp2(pos + 1, nm if not (nm == plen) else kmp_next[nm-1], nsmaller, nstarted)
                res %= mod
            return res % mod
        
        # Because dp above counted occurrences multiple times at each step over count recursion,
        # Use dp2 which resets matched after full match to allow overlapping.
        return dp2(0, 0, False, False)

def main():
    A, B, C = input().split()
    solver = ProblemSolver(A, B, C)
    print(solver.solve())

if __name__ == "__main__":
    main()