import itertools

def main():
    while True:
        data = input().split()
        n, s = int(data[0]), int(data[1])
        if not (n or s):
            return
        ans = reduce(lambda acc, x: acc + 1 if sum(x) == s else acc, itertools.combinations(range(10), n), 0)
        print(ans)

from functools import reduce
main()