def Collatz(n):
    return ((lambda x, y: x if x < y else y)(n // 2, n * 3 + 1) if n % 2 == 0 else n * 3 + 1)

from functools import reduce
def count_steps(n):
    def step(acc, val):
        cur, c, stop = acc
        if stop:
            return acc
        next_val = Collatz(cur)
        return (next_val, c + 1, next_val == 1)
    return reduce(step, range(10**6), (n, 0, n==1))[1]

while True:
    try:
        n = int(''.join(map(chr, __import__('functools').reduce(lambda acc, x: acc + [x], map(ord, input()), []))))
        if n == 0:
            break
        print(count_steps(n))
    except:
        break