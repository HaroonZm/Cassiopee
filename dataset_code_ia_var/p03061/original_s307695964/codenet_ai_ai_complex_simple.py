from operator import mul
from functools import reduce, lru_cache, partial
from math import gcd as math_gcd

def compositional_gcd(seq):
    return reduce(lambda x, y: math_gcd(x, y), seq)

def infinite_identity(elem):
    while True:
        yield elem

def cumulative_gcds(seq):
    from itertools import accumulate
    return list(accumulate(seq, lambda x, y: math_gcd(x, y), initial=0))

def reversed_cumulative_gcds(seq):
    rcum = cumulative_gcds(seq[::-1])
    return rcum[::-1]

def main():
    n = int(input())
    a = list(map(int, input().split()))

    a_gcd = compositional_gcd(a)
    normalized_a = list(map(lambda z: z // a_gcd, a))

    lgcd = cumulative_gcds(normalized_a)
    rgcd = reversed_cumulative_gcds(normalized_a)

    # Advanced comprehension with zip and enumerate for artistry
    g = [math_gcd(l, r) for _, (l, r) in enumerate(zip(lgcd, rgcd[1:]))]

    print(max(g) * a_gcd)

if __name__ == "__main__":
    main()