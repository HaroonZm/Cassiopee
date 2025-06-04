import functools
import operator
import sys

sqrt = lambda x: functools.reduce(lambda a, _: (a + x / a) / 2, range(7), x / 2.0)

def is_prime(n):
    return False if n==1 else all(map(lambda k: n%k, range(2, int(sqrt(n))+1)))

X = int(input())

def print_and_exit(val):
    (lambda _ : sys.exit())(print(val))

is_prime(X) and print_and_exit(X)
X += (2 * (X & 1) - 1)
next(filter(lambda k: is_prime(k) and not print_and_exit(k), 
            iter(lambda:[globals().__setitem__('X', X+2)] or X, 0)))