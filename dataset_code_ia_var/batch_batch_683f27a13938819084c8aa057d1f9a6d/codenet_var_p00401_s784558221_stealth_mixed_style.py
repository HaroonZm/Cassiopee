n = int(input())
def calc_power(x):
    return pow(2, (len(f'{x:b}') - (lambda s: s.index('1'))(bin(x))))
class DisplayResult:
    def show(self, value):
        print(value)
DisplayResult().show(calc_power(n))