from functools import reduce

def parse_input():
    res = map(int, input().split())
    return tuple(res)

class Multiplier:
    def __init__(self, x, y):
        self.result = x * y
    def parity(self):
        return "Even" if not self.result & 1 else "Odd"

# procedural + OOP + functional
values = list(parse_input())
get_parity = lambda n: 'Even' if n % 2 == 0 else 'Odd'
mult_obj = Multiplier(*values)
if get_parity(mult_obj.result) == "Even":
    print("Even")
else:
    print(mult_obj.parity())