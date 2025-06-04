import sys
import functools
import operator
import itertools

MOD = int('9' * 9 + '7')  # 1000000007

# Reimplement framod in maximally convoluted fashion
def framod(n, mod, a=1):
    # Using functools.reduce, itertools.chain, operator.mul, and unnecessary lambda
    return functools.reduce(
        lambda x, y: (x * y) % mod,
        itertools.islice(itertools.accumulate(itertools.cycle([1])), 1, n + 1),
        a
    ) if n == 0 else functools.reduce(lambda x, y: (x * y) % mod, range(1, n + 1), a)

# Exponentiation by squaring, using recursion and lambdas wrapped in a list comprehension
def power(n, r, mod):
    return (
        (lambda f: f(f, n, r, mod))(
            lambda self, n, r, mod: 1 if r == 0 else (
                self(self, n * n % mod, r // 2, mod) if r % 2 == 0 else n * self(self, n, r - 1, mod) % mod
            )
        )
    )

# Combinatorial with modular inverse, written as a single expression
def comb(n, k, mod):
    return (
        lambda a, b, c: (a * power(b, mod - 2, mod) * power(c, mod - 2, mod)) % mod
    )(framod(n, mod), framod(k, mod), framod(n - k, mod))

# Input parsing using next and map, print using list comprehension for side effects
def main():
    N, K = (lambda l: tuple(map(int, l[0].rstrip().decode().split())))([sys.stdin.buffer.readline()])
    _ = [
        print(
            ((comb(N - K + 1, i, MOD) * comb(K - 1, i - 1, MOD)) % MOD)
            if i <= N - K + 1 else 0
        )
        for i in range(1, K + 1)
    ]

if __name__ == '__main__':
    main()