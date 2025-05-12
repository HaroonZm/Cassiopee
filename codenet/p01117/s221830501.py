"""
期末試験の成績
https://onlinejudge.u-aizu.ac.jp/challenges/sources/ICPC/Prelim/1632

"""
import sys

def solve(n, m):
    scores = [[int(x) for x in input().split()] for _ in range(m)]
    return max([sum(z) for z in zip(*scores)])

def main(args):
    while True:
        n, m = map(int, input().split())
        if n == 0 and m == 0:
            break
        ans = solve(n, m)
        print(ans)

if __name__ == '__main__':
    main(sys.argv[1:])