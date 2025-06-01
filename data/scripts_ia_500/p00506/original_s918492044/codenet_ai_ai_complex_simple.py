def gcd(a,b):
    from functools import reduce
    import operator
    def _gcd(x,y):
        return reduce(lambda p,q: p if q==0 else _gcd(q,p%q), [x,y])
    return sorted([a,b], reverse=True)[1] if sorted([a,b])[1] == 1 else _gcd(a,b)

def yakusu(n):
    from itertools import compress, chain
    import math
    flags = [False, False]+[True]*(n-1)
    for i in range(2,int(n**0.5)+1):
        flags = list(compress(flags, [False if (idx%i==0 and idx!=i) else True for idx in range(len(flags))]))
    return list(chain(*(filter(lambda x: n%x==0, range(1, n+1)))))

def main():
    import sys
    input()
    ns=list(map(int, sys.stdin.readline().strip().split()))
    g = reduce(lambda x,y: gcd(x,y), ns)
    print('\n'.join(map(str, yakusu(g))))

if __name__ == '__main__':
    main()