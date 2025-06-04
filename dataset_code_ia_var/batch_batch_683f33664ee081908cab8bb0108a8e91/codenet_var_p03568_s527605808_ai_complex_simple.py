from functools import reduce
from operator import mul
from itertools import compress, repeat, starmap, count

def main():
    N = int(__import__('builtins').input())
    ans = pow(3, N)

    seq = list(map(int, __import__('builtins').input().split()))
    mask = tuple(map(lambda x: x % 2 == 0, seq))
    doubled = list(compress(repeat(2), mask))
    odd = reduce(mul, doubled, 1) if doubled else 1

    print((lambda x, y: x - y)(ans, odd))

if __name__ == '__main__':
    main()