"""
Dangerous Bridge
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0231

"""
import sys

def solve(n):
    events = []
    for _ in range(n):
        m, a, b = map(int, input().split())
        events.append([a, m])
        events.append([b, -m])

    weight = 0
    for t, m in sorted(events):
         weight += m
         if weight > 150:
             return 'NG'
    return 'OK'

def main(args):
    while True:
        n = int(input())
        if n == 0:
            break
        ans = solve(n)
        print(ans)

if __name__ == '__main__':
    main(sys.argv[1:])