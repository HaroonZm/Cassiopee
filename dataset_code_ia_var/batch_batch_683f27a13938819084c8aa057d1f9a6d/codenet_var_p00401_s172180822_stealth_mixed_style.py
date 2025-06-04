def closest_power_of_two(n):
    def helper(num, exp=0):
        while True:
            candidate = 2 ** exp
            if num < candidate:
                return 1 if exp == 0 else 2 ** (exp - 1)
            if num == candidate:
                return 2 ** exp
            exp += 1

class Wrapper:
    def __init__(self, value):
        self.v = value
    def result(self):
        return closest_power_of_two(self.v)

try:
    from functools import reduce
except:
    pass  # Pas utile ici

if __name__ == "__main__":
    x = input()
    res = Wrapper(int(x)).result()
    print(res)