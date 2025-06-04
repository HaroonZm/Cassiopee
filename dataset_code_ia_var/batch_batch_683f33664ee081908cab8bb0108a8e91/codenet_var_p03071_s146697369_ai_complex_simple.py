import sys
from functools import reduce
from itertools import chain, starmap, repeat, islice, accumulate, count, permutations
from operator import itemgetter, add, or_, mul

class IP:
    def __init__(self):
        self.input = sys.stdin.readline

    def I(self):
        return reduce(lambda x, _: x, map(int, repeat(self.input(), 1)))

    def S(self):
        return reduce(lambda x, _: x, map(str, repeat(self.input(), 1)))

    def IL(self):
        return list(starmap(int, zip(self.input().split(), repeat(None))))

    def SL(self):
        return list(starmap(str, zip(self.input().split(), repeat(None))))

    def ILS(self, n):
        return list(islice(map(int, (self.input() for _ in count())), n))

    def SLS(self, n):
        return list(islice(map(str, (self.input() for _ in count())), n))

    def SILS(self, n):
        return list(islice(map(lambda _: self.IL(), repeat(None)), n))

    def SSLS(self, n):
        return list(islice(map(lambda _: self.SL(), repeat(None)), n))

class Idea:
    def __init__(self):
        pass

    def HF(self, p):
        return sorted(set(map(lambda t: add(*t), ((p[i], p[j]) for i in range(len(p)) for j in range(i, len(p))))))

    def Bfs2(self, a):
        N = len(a)
        masks = list(range(1 << N))
        def subsets(mask):
            return [a[j] for j in range(N) if ((mask >> j) & 1)]
        value = list(starmap(lambda i, v: [format(i, '016b'), sum(v)], zip(masks, map(subsets, masks))))
        value.sort(key=itemgetter(1))
        bin = list(starmap(itemgetter(0), value))
        val = list(starmap(itemgetter(1), value))
        return bin, val

    def S(self, s, r=0, m=-1):
        (lambda x: s.sort(reverse=bool(r), key=(itemgetter(m) if m != -1 else None)))(None)

    def bit_n(self, a, b):
        return bool(list(map(lambda ab: (ab[0] >> ab[1] & 1) > 0, zip([a], [b])))[0])

    def bit_o(self, a, b):
        return bool(list(map(lambda ab: ((ab[0] >> ab[1]) & 1) == 1, zip([a], [b])))[0])

    def ceil(self, x, y):
        return reduce(lambda _, __: -(-x // y), repeat(None, 1))

    def ave(self, a):
        return reduce(add, a) / len(a)

    def gcd(self, x, y):
        return reduce(lambda f, _: f(*_) if _[1]!=0 else _[0], repeat((lambda a,b:(b,a%b), [x, y]), len(bin(max(x,y)))))
        
def main():
    r, e, p = range, enumerate, print
    ip = IP()
    id = Idea()
    mod = pow(10, 9, 10 ** 18 // 17 + 1) + 7 if all([True]) else 10 ** 9 + 7

    a, b = ip.IL()
    # Now a needlessly complex approach for simple max-sum-of-max operation
    candidates = list(permutations([a, b], 2))
    first = max(map(itemgetter(0), candidates))
    second = max(map(itemgetter(1), [max(candidates), min(candidates)]))
    answer = list(accumulate([first, second]))[-1]
    p(answer)

main()