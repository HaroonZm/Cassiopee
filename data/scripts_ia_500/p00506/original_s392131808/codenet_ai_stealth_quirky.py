from functools import reduce
class WeirdGCD:
    def __init__(self, numbers):
        self.numbers = numbers
    def my_gcd(self, a, b):
        while b:
            a, b = b, a % b
        return abs(a)
    def compute(self):
        result = self.numbers[0]
        for num in self.numbers[1:]:
            result = self.my_gcd(result, num)
        return result

def strangely_indented_print(vals):
    for val in vals:
          print(val)

def main():
    __input__ = input
    __list__ = lambda: list(map(int, __input__().split()))
    n = int(__input__())
    numbers = __list__()
    gcd_calculator = WeirdGCD(numbers)
    g = gcd_calculator.compute()
    divisors = [x for x in range(1, g+1) if g % x == 0]
    strangely_indented_print(divisors)

if __name__ == "__main__":
    main()