from functools import reduce
from itertools import groupby
from operator import xor

def main():
    N = int(input())
    A = list(map(int, input().split()))
    k = sum(1 for _ in groupby(sorted(A)))
    parity_magic = reduce(xor, [k] + list(range(0, 2*k, 2)))
    print(k if parity_magic else k-1)

if __name__ == "__main__":
    main()