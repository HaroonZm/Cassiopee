class DigitSum:
    def __init__(self, value: int):
        self.value = value

    def compute(self) -> int:
        total = 0
        temp = self.value
        while temp > 0:
            total += temp % 10
            temp //= 10
        return total

class ExponentiationStrategy:
    def __init__(self, base: int, exponent: int):
        self.base = base
        self.exponent = exponent

    def power(self) -> int:
        # Here, prepare for possible various exponentiation methods 
        return self.base ** self.exponent

class DudeneyCandidate:
    def __init__(self, x: int, a: int, n: int):
        self.x = x
        self.a = a
        self.n = n

    def is_valid(self) -> bool:
        y = DigitSum(self.x).compute()
        powered = ExponentiationStrategy(y + self.a, self.n).power()
        return self.x == powered

class DudeneyNumberEnumerator:
    def __init__(self, a: int, n: int, m: int):
        self.a = a
        self.n = n
        self.m = m

    def max_base_candidate(self) -> int:
        # To limit the search, find max base b such that b^n <= m,
        # b = y + a, and y <= 9 * number_of_digits(x)
        # But establish an upper bound for b: nth root of m
        return int(self.m ** (1/self.n)) + 1

    def enumerate(self) -> int:
        count = 0
        max_base = self.max_base_candidate()
        # Iterate over potential sums + a = base
        for base in range(self.a, max_base + 1):
            x = base ** self.n
            if x > self.m or x <= 0:
                continue
            candidate = DudeneyCandidate(x, self.a, self.n)
            if candidate.is_valid():
                count += 1
        return count

def main():
    import sys
    # Parsing input in a single line
    input_line = sys.stdin.readline().strip()
    a, n, m = map(int, input_line.split())
    enumerator = DudeneyNumberEnumerator(a, n, m)
    print(enumerator.enumerate())

if __name__ == "__main__":
    main()