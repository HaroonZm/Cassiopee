from functools import reduce
from math import gcd, isqrt

def common_divisors(*nums):
    g = reduce(gcd, nums)
    divisors = set()
    for i in range(1, isqrt(g) + 1):
        if g % i == 0:
            divisors.add(i)
            divisors.add(g // i)
    return sorted(divisors)

def main():
    _ = input()
    ns = list(map(int, input().split()))
    for d in common_divisors(*ns):
        print(d)

if __name__ == '__main__':
    main()