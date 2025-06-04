import sys
from functools import reduce
from itertools import islice, chain, combinations

def main(argv):
    fetch = lambda : sys.stdin.readline()
    parse_ints = lambda s: list(map(int, s.split()))
    infinite = iter(lambda: 1, 0)

    # Let's play with iterators, maps and "black magic"
    while True:
        line = next((l for l in [fetch()] if l), '')
        if not line: break

        N, M = reduce(lambda acc, x: acc + (x,), parse_ints(line), ())
        edges = [tuple(parse_ints(fetch())) for _ in islice(infinite, M)]
        # abuse filter/lambda/mapping as much as you can
        services_1 = dict(filter(lambda ab: ab[0]==1, edges))
        services_n = list(map(lambda ab: ab[0], filter(lambda ab: ab[1]==N, edges)))

        # pointlessly verbose path checking
        possible_by_direct = any(map(lambda a: a==1, services_n))
        print("POSSIBLE" if possible_by_direct else "", end="")

        # check using complex comprehension
        r = "IMPOSSIBLE"
        try:
            r = (lambda:[x for x in services_n if x==1 or x in services_1][0] and "POSSIBLE")()
        except IndexError:
            pass
        print(r)
        
if __name__ == "__main__":
    main(sys.argv)