class PrimeLottery:
    class PrimeSet:
        def __init__(self, max_prime: int, known_primes: list):
            self._max_prime = max_prime
            self._primes = sorted(prime for prime in known_primes if prime <= max_prime)
        def count_in_range(self, left: int, right: int) -> int:
            # Count primes in [left, right] via binary search
            import bisect
            left_index = bisect.bisect_left(self._primes, max(left, 0))
            right_index = bisect.bisect_right(self._primes, min(right, self._max_prime))
            return max(0, right_index - left_index)

    class LotteryDraw:
        __slots__ = ['p', 'm']
        def __init__(self, p: int, m: int):
            self.p = p
            self.m = m
        
        def prime_count(self, prime_set: 'PrimeLottery.PrimeSet') -> int:
            left = self.p - self.m
            right = self.p + self.m
            return prime_set.count_in_range(left, right)

    class Treasury:
        def __init__(self):
            self._king_expense = 0
        def add_payout(self, prime_count: int):
            # Prize X prime: 1 prime from lottery sales, (X-1) from king's expense for X>=1,
            # if X=0, then 1 prime from sales is transferred to king's expense (no payout)
            if prime_count == 0:
                self._king_expense += 1
            else:
                self._king_expense += max(0, prime_count - 1)
        @property
        def king_expense(self) -> int:
            return self._king_expense

    class InputParser:
        def __init__(self, max_prime: int, known_primes: list):
            self._max_prime = max_prime
            self._known_primes = known_primes
        def parse_all(self):
            import sys
            input_lines = sys.stdin.read().strip().split('\n')
            idx = 0
            while True:
                if idx >= len(input_lines):
                    break
                n_line = input_lines[idx].strip()
                idx += 1
                if n_line == '0':
                    break
                n = int(n_line)
                draws = []
                for _ in range(n):
                    p_str, m_str = input_lines[idx].split()
                    idx += 1
                    p = int(p_str)
                    m = int(m_str)
                    draws.append(PrimeLottery.LotteryDraw(p, m))
                yield draws

    def __init__(self):
        # Known primes <= 1,000,000 as of Nov 1, 2007
        # The maximum prime MP is 999983
        # Known primes in [999963..1000003] are only 999979 and 999983,
        # 1000003 is not known at the time, so exclude it.
        # The full list of primes up to 999983 is huge, so let's generate it here.
        # However, prime set is fixed and only queries within [0..999983].
        # We generate using sieve once.
        self._MP = 999983
        self._primes = self._generate_primes_upto(self._MP)
        self._prime_set = self.PrimeSet(self._MP, self._primes)
        self._treasury = self.Treasury()
        self._parser = self.InputParser(self._MP, self._primes)

    def _generate_primes_upto(self, n: int) -> list:
        # Sieve of Eratosthenes
        sieve = [True]*(n+1)
        sieve[0] = False
        sieve[1] = False
        for i in range(2, int(n**0.5)+1):
            if sieve[i]:
                for j in range(i*i, n+1, i):
                    sieve[j] = False
        return [i for i, prime in enumerate(sieve) if prime]

    def solve(self):
        for draws in self._parser.parse_all():
            self._treasury = self.Treasury()  # reset for each dataset
            # Aggregate payouts per ticket number p because multiple draws can hit same p.
            from collections import defaultdict
            payout_per_ticket = defaultdict(int)
            for draw in draws:
                c = draw.prime_count(self._prime_set)
                payout_per_ticket[draw.p] += c
            # Calculate total king expense by sum of all draws' effects
            for ticket_p, total_prize in payout_per_ticket.items():
                self._treasury.add_payout(total_prize)
            # Output king's expense
            print(self._treasury.king_expense)


if __name__ == '__main__':
    PrimeLottery().solve()