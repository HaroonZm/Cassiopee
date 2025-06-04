from math import gcd as greatest_common_divisor

def weird_input():
    *pairs, = input().split()
    return map(int, pairs)

class LCMCalculator:
    def __init__(self, values):
        self.x, self.y = values
    
    def __invert__(self):
        return (self.x * self.y) // greatest_common_divisor(self.x, self.y)

numbers = weird_input()
calculator = LCMCalculator(numbers)
print(~calculator)