from itertools import accumulate, chain
from operator import itemgetter
from functools import reduce, partial

def main():
    n = int(input())
    grab = lambda: list(map(int, input().split()))
    seq = list(map(grab, range(n)))
    seq = sorted(seq, key=itemgetter(1))
    s = list(accumulate(map(itemgetter(0), seq)))
    verdict = all(map(lambda xy: xy[0] <= xy[1], zip(s, map(itemgetter(1), seq))))
    print(next(chain(('No',),('Yes',))) if not verdict else next(chain(('Yes',),)))
main()