from typing import List, Optional, Tuple
from abc import ABC, abstractmethod

class PrimeChecker(ABC):
    @abstractmethod
    def is_prime(self, num: int) -> bool:
        pass

class MillerRabinPrimeChecker(PrimeChecker):
    def is_prime(self, num: int) -> bool:
        if num < 2:
            return False
        # Base primes to test against for 32 bit integers
        bases = [2,3,5,7,11,13,17,19,23]
        d = num -1
        r = 0
        while d % 2 == 0:
            d //= 2
            r +=1
        for a in bases:
            if a >= num:
                break
            if not self._check_composite(num, a, d, r):
                return False
        return True

    def _check_composite(self, n: int, a:int, d:int, r:int) -> bool:
        x = pow(a,d,n)
        if x ==1 or x == n-1:
            return True
        for _ in range(r-1):
            x = (x*x) % n
            if x == n-1:
                return True
        return False

class NumberStringBuilder:
    def __init__(self, n:int, c: Optional[int]):
        self.n = n
        self.c = c

    def build_number(self, bs: List[int], gs: List[int]) -> int:
        if self.c is not None:
            digits = bs + [self.c] + gs
        else:
            digits = bs + gs
        # Convert list of digits to integer
        number = 0
        for d in digits:
            number = number * 10 + d
        return number

    def format_number_str(self, bs: List[int], gs: List[int]) -> str:
        if self.c is not None:
            return "".join(str(d) for d in bs) + str(self.c) + "".join(str(d) for d in gs)
        else:
            return "".join(str(d) for d in bs) + "".join(str(d) for d in gs)

class ArrangementGenerator:
    def __init__(self, n: int, c: Optional[int], prime_checker: PrimeChecker):
        self.n = n
        self.c = c
        self.prime_checker = prime_checker

    def generate_optimal_arrangement(self) -> str:
        # We know the order:
        # Boys: b1, b2, ... bn (in increasing index order)
        # Girls: gn, gn-1, ..., g1 (reverse order)
        # We select digits such that number is prime or largest possible if tie

        # Because the problem states "pairs" of boys and girls with the same digit number from 0 to 9
        # Each pair selects one digit that both boy and girl hold.

        # The arrangement digits:
        # boys in order: b1, b2, ... bn,
        # girls in reverse order: gn, gn-1, ..., g1,
        # c in the center if given

        # We must pick b_i digits from 0-9 and assign g_i digits same as b_i

        # Number formed:
        # If c given: b1 b2 ... bn c gn gn-1 ... g1
        # If no c: b1 b2 ... bn gn gn-1 ... g1

        # Constraint: leading digit != 0, last digit != 0
        # Because leading 0 or trailing zero forbidden.

        # Digit positions:
        # pos 0: b1
        # pos n-1: bn
        # pos n: c (if exists)
        # pos n+1... 2n (if c) or n... 2n-1 (if no c): girls reversed

        # The first digit of the entire number is at position 0: b1
        # If b1 == 0 => invalid
        # Also last digit is g1, position last - must != 0

        # Sophisticated approach: use backtracking with pruning and memoization of prime checks
        # Plus an abstraction for digit assignment

        # Digits index from 0 to n-1: b_i
        # Girls digits determined by same digits as boys in reverse order: g_i = b_i

        best_number_str = None
        best_number_val = -1
        best_is_prime = False

        memo_prime = {}

        def is_prime_cached(num: int) -> bool:
            if num in memo_prime:
                return memo_prime[num]
            res = self.prime_checker.is_prime(num)
            memo_prime[num] = res
            return res

        # We'll try a DFS with pruning:
        # For each pair position i, select digit d in 0..9
        # For b1 (pos 0) digit cannot be zero
        # For g1 (pos last) digit cannot be zero -> g1 = b1 (since g1 = b1) this requires b1 != 0 anyway
        # So b1 cannot be zero,
        # similarly b_i digits for i>0 can be zero, but we avoid leading/trailing zero only for first and last digits

        # We'll generate bs list incrementally, then form gs from reverse(bs)
        # For corresponding c we have c digit or None

        # We will try only digits 0-9 for each b_i with constraints

        # Because n <= 10 and digits 0..9, we can do complete search with pruning

        from functools import lru_cache

        # Check number formation rules:
        # leading zero forbidden
        # trailing zero forbidden (last digit is g1 = b1 => so this is same digit)
        # So b1 != 0

        # We'll generate all bs candidates satisfying b1 != 0

        # We want the "負けない並び方" i.e. arrangement that ensures no loss:
        # The arrangement selection criteria:
        # - If prime, wins over non-prime.
        # - If both prime or non-prime, bigger number wins

        # So we want to maximize (is_prime first, then numeric value)

        # For optimization, since last digit = b1, so last digit is same as first digit, so trailing zero means b1 == 0 forbidden

        # So b1 != 0

        @lru_cache(maxsize=None)
        def dfs(position: int, assigned_bs: Tuple[int, ...]) -> Optional[Tuple[bool, int, str]]:
            # position from 0 to n-1
            if position == self.n:
                # build full number with c and gs
                bs = list(assigned_bs)
                gs = bs[::-1]  # girls reverse of boys list
                number_str_builder = NumberStringBuilder(self.n, self.c)
                full_str = number_str_builder.format_number_str(bs, gs)
                if full_str[0] == '0' or full_str[-1] == '0':
                    # invalid leading or trailing zero
                    return None
                number_val = int(full_str)
                prime_flag = is_prime_cached(number_val)
                return (prime_flag, number_val, full_str)

            candidates = []
            start_d = 1 if position == 0 else 0
            for d in range(start_d, 10):
                # Because last digit = g1 = b1 = assigned_bs[0]
                # If position == 0, this sets the first digit and last digit
                # So no trailing zero issue if d != 0 (guaranteed by start_d = 1)
                # For other positions no additional restriction apart from digit 0..9
                # Select d for assigned_bs[position]
                nb = assigned_bs + (d,)
                res = dfs(position+1, nb)
                if res is not None:
                    candidates.append(res)
            if not candidates:
                return None
            # pick best candidate by prime > val descending
            candidates.sort(key=lambda x: (x[0], x[1]), reverse=True)
            return candidates[0]

        # Run DFS
        result = dfs(0, ())
        if result is not None:
            return result[2]
        else:
            # fallback: if no arrangement found - theoretically impossible
            # But just output minimal valid number with all ones
            bs = [1]*self.n
            gs = bs[::-1]
            if self.c is not None:
                c_digit = self.c
                number_str = "".join(str(d) for d in bs) + str(c_digit) + "".join(str(d) for d in gs)
            else:
                number_str = "".join(str(d) for d in bs) + "".join(str(d) for d in gs)
            return number_str

class InputParser:
    @staticmethod
    def parse() -> Tuple[int, Optional[int]]:
        import sys
        line = sys.stdin.readline().strip()
        n_str, c_str = line.split()
        n = int(n_str)
        c = int(c_str)
        if c < 0:
            c_val = None
        else:
            c_val = c
        return n, c_val

class OutputFormatter:
    @staticmethod
    def output(s: str) -> None:
        # Add trailing newline per instruction
        print(s)

def main():
    n, c = InputParser.parse()
    prime_checker = MillerRabinPrimeChecker()
    arrangement_generator = ArrangementGenerator(n, c, prime_checker)
    ans = arrangement_generator.generate_optimal_arrangement()
    OutputFormatter.output(ans)

if __name__ == "__main__":
    main()