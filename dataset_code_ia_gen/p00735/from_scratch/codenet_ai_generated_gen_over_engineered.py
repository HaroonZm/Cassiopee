from typing import List, Dict, Set

class MondaySaturdayNumber:
    MOD_VALUES = {1, 6}
    MOD_BASE = 7

    def __init__(self, value: int):
        if value <= 1:
            raise ValueError("Monday-Saturday numbers must be greater than 1")
        if value % self.MOD_BASE not in self.MOD_VALUES:
            raise ValueError(
                f"Number {value} is not a Monday-Saturday number (mod 7 must be 1 or 6)"
            )
        self.value = value

    def is_monday_saturday(self) -> bool:
        return self.value % self.MOD_BASE in self.MOD_VALUES

    def __mul__(self, other: "MondaySaturdayNumber") -> "MondaySaturdayNumber":
        product = self.value * other.value
        return MondaySaturdayNumber(product)

    def __floordiv__(self, other: "MondaySaturdayNumber") -> "MondaySaturdayNumber":
        if self.value % other.value != 0:
            raise ValueError(f"{other.value} does not divide {self.value}")
        quotient = self.value // other.value
        return MondaySaturdayNumber(quotient)

    def divides(self, other: "MondaySaturdayNumber") -> bool:
        return other.value % self.value == 0

class MondaySaturdayPrime(MondaySaturdayNumber):
    _composite_cache: Dict[int, bool] = {}

    @classmethod
    def _is_prime_usual(cls, n: int) -> bool:
        if n < 2:
            return False
        if n in (2, 3):
            return True
        if n % 2 == 0:
            return False
        r = int(n**0.5)
        for i in range(3, r + 1, 2):
            if n % i == 0:
                return False
        return True

    @classmethod
    def is_monday_saturday_prime(cls, n: int) -> bool:
        # Memoization to save repeated checks
        if n in cls._composite_cache:
            return cls._composite_cache[n]
        # Must be Monday-Saturday number > 1
        if n <= 1 or n % 7 not in MondaySaturdayNumber.MOD_VALUES:
            cls._composite_cache[n] = False
            return False
        # If usual prime and MS number -> MS prime
        if cls._is_prime_usual(n):
            cls._composite_cache[n] = True
            return True
        # Else check if divisible by any smaller MS prime (other than 1 and n)
        # Check all proper MS divisors
        # The key property:
        # a MS prime has no MS divisors other than 1 and itself.
        # We iterate over all Monday-Saturday divisors to detect composite.
        limit = int(n ** 0.5) + 1
        for candidate in _generate_monday_saturday_numbers_up_to(limit):
            if candidate == 1 or candidate == n:
                continue
            if n % candidate == 0:
                # check if candidate is MS prime, if yes then n is not MS prime
                if cls.is_monday_saturday_prime(candidate):
                    cls._composite_cache[n] = False
                    return False
        # no MS prime divisor found, is MS prime
        cls._composite_cache[n] = True
        return True

def _generate_monday_saturday_numbers_up_to(limit: int) -> List[int]:
    # Generate all integers <= limit that are Monday-Saturday numbers
    result = []
    for k in range(1, limit // 7 + 2):
        for rem in MondaySaturdayNumber.MOD_VALUES:
            n = 7 * k + rem
            if n <= limit:
                result.append(n)
    result = list(set(result))
    result.sort()
    return result


class MondaySaturdayFactorizer:
    def __init__(self):
        self._ms_prime_cache: Dict[int, bool] = {}

    def factorize(self, number: MondaySaturdayNumber) -> Set[int]:
        # Return set of MS prime factors of number.value
        n = number.value
        factors = set()
        self._factorize_recursive(n, factors)
        return factors

    def _factorize_recursive(self, n: int, factors: Set[int]) -> None:
        if n == 1:
            return
        if n in self._ms_prime_cache:
            if self._ms_prime_cache[n]:
                factors.add(n)
            else:
                # composite in cache, continue factoring
                pass
        else:
            is_msp = MondaySaturdayPrime.is_monday_saturday_prime(n)
            self._ms_prime_cache[n] = is_msp
            if is_msp:
                factors.add(n)
                return
        # Find a MS prime divisor other than n itself
        limit = int(n ** 0.5) + 1
        for d in _generate_monday_saturday_numbers_up_to(limit):
            if d >= n:
                break
            if n % d == 0:
                if MondaySaturdayPrime.is_monday_saturday_prime(d):
                    factors.add(d)
                    self._factorize_recursive(n // d, factors)
                    return
        # If no divisor found, it must be MS prime itself
        factors.add(n)

def main():
    import sys
    factorizer = MondaySaturdayFactorizer()
    for line in sys.stdin:
        line = line.strip()
        if line == "1":
            break
        n = int(line)
        try:
            ms_number = MondaySaturdayNumber(n)
        except ValueError:
            # Input number does not qualify as Monday-Saturday number per problem statement
            # According to problem constraints, all inputs (except last '1') are MS numbers
            # So we may just ignore or raise
            continue

        factors = factorizer.factorize(ms_number)
        # Output factors sorted ascending
        factors_sorted = sorted(factors)
        print(f"{n}:" + "".join(f" {f}" for f in factors_sorted))

if __name__ == "__main__":
    main()