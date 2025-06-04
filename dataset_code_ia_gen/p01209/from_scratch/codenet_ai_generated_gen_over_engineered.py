class BaseConverter:
    def __init__(self, base: int):
        if not (8 <= base <= 36):
            raise ValueError("Base must be between 8 and 36 inclusive.")
        self.base = base
        self.digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    def char_to_val(self, c: str) -> int:
        val = self.digits.index(c)
        if val >= self.base:
            raise ValueError(f"Digit '{c}' not valid for base {self.base}")
        return val
    
    def str_to_int(self, s: str) -> int:
        val = 0
        for c in s:
            val = val * self.base + self.char_to_val(c)
        return val
    
    def int_to_str(self, num: int) -> str:
        if num == 0:
            return "0"
        result = []
        n = num
        while n > 0:
            result.append(self.digits[n % self.base])
            n //= self.base
        return "".join(reversed(result))

class FactorialTrailingZerosCalculator:
    def __init__(self, base: int):
        self.base = base
        self.converter = BaseConverter(base)
        # Precompute prime factors of base and their exponents for factorization
        self.base_prime_factors = self.factorize_base(self.base)
    
    def factorize_base(self, base: int) -> dict:
        # Return dictionary {prime_factor: exponent}
        b = base
        factors = {}
        d = 2
        while d * d <= b:
            count = 0
            while b % d == 0:
                b //= d
                count += 1
            if count > 0:
                factors[d] = count
            d += 1 if d == 2 else 2
        if b > 1:
            factors[b] = factors.get(b, 0) + 1
        return factors

    def prime_factor_exponent_in_factorial(self, n: int, p: int) -> int:
        # Count exponent of prime p in n!
        # Legendre's formula
        count = 0
        power = p
        while power <= n:
            count += n // power
            power *= p
        return count
    
    def trailing_zeros_in_factorial(self, n: int) -> int:
        # For each prime factor of the base, find how many times it divides n!
        zeros_counts = []
        for prime, exponent in self.base_prime_factors.items():
            total_exp = self.prime_factor_exponent_in_factorial(n, prime)
            zeros_counts.append(total_exp // exponent)
        return min(zeros_counts) if zeros_counts else 0

class ICPCProblemC:
    def __init__(self):
        self.cache = {}

    def process_input_line(self, line: str) -> int:
        if line == "0 0":
            raise StopIteration
        base_str, M_str = line.strip().split()
        base = int(base_str)
        converter = BaseConverter(base)
        M = converter.str_to_int(M_str)
        calculator = FactorialTrailingZerosCalculator(base)
        return calculator.trailing_zeros_in_factorial(M)

    def run(self):
        import sys
        for line in sys.stdin:
            line = line.strip()
            if not line:
                continue
            try:
                result = self.process_input_line(line)
                print(result)
            except StopIteration:
                break

if __name__ == "__main__":
    ICPCProblemC().run()