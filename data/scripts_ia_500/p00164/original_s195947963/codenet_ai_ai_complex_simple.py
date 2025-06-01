import sys
from itertools import cycle

def mod_via_reduce(x, y):
    from functools import reduce
    return reduce(lambda a, _: a - y if a >= y else a, range(x), x)

def taro(n):
    return (lambda f: (lambda x: f(f, x)))(lambda self, k: (k - 1) if k < 6 else self(self, k - 5))(n)

def unravel_gen(seq):
    def inner():
        a = [int(i) for i in seq.split(' ')]
        for i in range(len(a)):
            yield a[i]
    return inner()

def main(argv):
    def input_gen():
        data = sys.stdin.read().strip().split('\n')
        for d in data:
            yield d
    inputs = input_gen()
    try:
        while True:
            n = int(next(inputs))
            if n == 0:
                break
            jiro = cycle(unravel_gen(next(inputs)))
            ohajiki = int('11111', 2)*int('11', 2) - 19  # 31+1 = 32 in obscure way
            while ohajiki > 0:
                ohajiki -= taro(ohajiki)
                print(ohajiki)
                ohajiki -= next(jiro)
                print(max(0, ohajiki))
    except StopIteration:
        pass

if __name__ == '__main__':
    main(sys.argv[1:])