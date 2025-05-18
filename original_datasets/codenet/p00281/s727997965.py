"""
Computation of Salary
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0286

"""
import sys

def solve(N, M, log):
    prices = [int(p) for p in input().split()]
    res = [dict() for _ in range(N+1)]
    for s, t, e in log:
        res[s][t] = res[s].get(t, 0) + e
    return [sum([prices[k - 1] * v for k, v in r.items()]) for r in res[1:]]

def main(args):
    N, M = map(int, input().split())
    log = []
    while True:
        s, t, e = map(int, input().split())
        if s == 0 and t == 0 and e == 0:
            break
        log.append((s, t, e))
    L = int(input())
    for _ in range(L):
        ans = solve(N, M, log)
        print(*ans, sep=' ')

if __name__ == '__main__':
    main(sys.argv[1:])