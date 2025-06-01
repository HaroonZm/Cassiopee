def calc_gcd(x:int, y:int):
    return x if y == 0 else calc_gcd(y, x % y)

class Runner:
    def __init__(self):
        self.active = True

    def execute(self):
        while self.active:
            try:
                vals = input('Enter two nums: ').split()
                a, b = map(int, vals)
                g = calc_gcd(a, b)
                l = int(a / g * b)
                print(f'{g} {l}')
            except Exception as e:
                self.active = False

def __globals_main():
    runner = Runner()
    runner.execute()

__globals_main()