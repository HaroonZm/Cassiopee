class DigitOperationsInterface:
    def sum_of_digits(self, number: int) -> int:
        raise NotImplementedError

class DigitOperations(DigitOperationsInterface):
    def sum_of_digits(self, number: int) -> int:
        # Highly optimized sum of digits using map and str conversion
        return sum(map(int, str(number)))

class PowerCalculatorInterface:
    def power(self, base: int, exponent: int) -> int:
        raise NotImplementedError

class PowerCalculator(PowerCalculatorInterface):
    def power(self, base: int, exponent: int) -> int:
        # Using built-in pow but wrapped for future extension possibilities
        return pow(base, exponent)

class DudeneyNumberValidatorInterface:
    def is_valid(self, x: int, a: int, n: int, digit_ops: DigitOperationsInterface, power_calc: PowerCalculatorInterface) -> bool:
        raise NotImplementedError

class DudeneyNumberValidator(DudeneyNumberValidatorInterface):
    def is_valid(self, x: int, a: int, n: int, digit_ops: DigitOperationsInterface, power_calc: PowerCalculatorInterface) -> bool:
        # Extract sum of digits from x
        y = digit_ops.sum_of_digits(x)
        # Evaluate (y + a)^n
        val = power_calc.power(y + a, n)
        # Check if val matches x
        return val == x

class DudeneyNumberEnumeratorInterface:
    def enumerate(self, a: int, n: int, m: int) -> int:
        raise NotImplementedError

class DudeneyNumberEnumerator(DudeneyNumberEnumeratorInterface):
    def __init__(self, validator: DudeneyNumberValidatorInterface,
                 digit_ops: DigitOperationsInterface,
                 power_calc: PowerCalculatorInterface):
        self.validator = validator
        self.digit_ops = digit_ops
        self.power_calc = power_calc

    def enumerate(self, a: int, n: int, m: int) -> int:
        count = 0
        # Optimization: the maximum sum of digits y we need to consider
        # must satisfy (y + a)^n <= m
        # So upper bound for y is floor of nth_root(m) - a
        # Compute nth-root integer approximation
        max_base = int(round(m ** (1 / n))) + 1
        max_y = max_base - a
        if max_y < 0:
            return 0
        
        # To avoid duplicates, keep track of found x's
        found_set = set()

        # Iterate over possible y
        for y in range(max(0, max_y + 1)):
            val = self.power_calc.power(y + a, n)
            if val > m or val <= 0:
                # Since val is increasing in y, we can break early
                break
            # Check if sum of digits of val matches y
            if self.digit_ops.sum_of_digits(val) == y:
                if val not in found_set:
                    found_set.add(val)
                    count += 1
        return count

class InputParser:
    @staticmethod
    def parse(input_string: str):
        parts = input_string.strip().split()
        if len(parts) != 3:
            raise ValueError("Input must contain exactly three integers")
        a, n, m = map(int, parts)
        if not(0 <= a <= 50):
            raise ValueError("a must be between 0 and 50")
        if not(2 <= n <= 10):
            raise ValueError("n must be between 2 and 10")
        if not(1000 <= m <= 10**8):
            raise ValueError("m must be between 1000 and 10^8")
        return a, n, m

def main():
    import sys
    input_line = sys.stdin.readline()
    a, n, m = InputParser.parse(input_line)
    digit_ops = DigitOperations()
    power_calc = PowerCalculator()
    validator = DudeneyNumberValidator()
    enumerator = DudeneyNumberEnumerator(validator, digit_ops, power_calc)
    result = enumerator.enumerate(a, n, m)
    print(result)

if __name__ == "__main__":
    main()