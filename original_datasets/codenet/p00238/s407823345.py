"""
Time to Study
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0238

"""
import sys

def solve(t):
    n = int(input())
    for _ in range(n):
        s, f = map(int, input().split())
        t -= (f-s)
    return 'OK' if t <= 0 else t

def main(args):
    while True:
        t = int(input())
        if t == 0:
            break
        ans = solve(t)
        print(ans)

if __name__ == '__main__':
    main(sys.argv[1:])