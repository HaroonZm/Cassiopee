from functools import reduce
from operator import mul

gcd = lambda a, b: reduce(lambda x, y: y if x % y == 0 else gcd(y, x % y), [(a, b)], b)

def main():
    a, b = map(int, raw_input().split())
    print((lambda x, y: reduce(lambda f, _: f(), [lambda: gcd(x, y)], None))(a, b))

if __name__ == '__main__':
    main()