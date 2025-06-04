from functools import reduce
from itertools import combinations, repeat, chain, starmap, product
from operator import mul, itemgetter
import sys

def era(n):
    flag = bytearray(n+1)
    # List comprehension nested in a reduce to build primes by crossing off non-primes in a clever way
    def sieve(acc, x):
        flag, p = acc
        if not flag[x]:
            flag[x*x::x] = repeat(1, ((n - x*x)//x)+1)
            return (flag, p + [x])
        return (flag, p)
    if n < 2: return []
    return reduce(sieve, range(2, n+1), (flag, []))[1]

def f(n):
    # map/lambda, sum, clever key extraction with itemgetter
    return sum(map(lambda x: x>=n-1, map(itemgetter(1), data)))

try:
    N = int(sys.stdin.readline())
except:
    N = int(input())

s = era(N)
data = list(
    map(lambda i: [
        i, 
        sum(
            map(
                lambda power: N // power,
                takewhile(lambda x: x <= N, 
                    starmap(pow, zip(repeat(i), count(1)))))
        )],
    s
    )
)

# define takewhile and count inline to avoid imports
def count(start=1):
    n = start
    while True:
        yield n
        n += 1

def takewhile(pred, iterable):
    for x in iterable:
        if not pred(x): 
            break
        yield x

calc = lambda: (
    f(75)+
    f(15)*(f(5)-1)+
    f(25)*(f(3)-1)+
    f(5)*(f(5)-1)*(f(3)-2)//2
)

print(calc())