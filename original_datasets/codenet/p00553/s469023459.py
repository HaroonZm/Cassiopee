"""
Microwave
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0630

"""
import sys

def solve(a, b, c, d, e):
    ans = 0
    while a < b:
        if a < 0:
            a += 1
            ans += c
        elif a == 0:
            a += 1
            ans += (d + e)
        else:
            a += 1
            ans += e
    return ans

def main(args):
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    ans = solve(a, b, c, d, e)
    print(ans)

if __name__ == '__main__':
    main(sys.argv[1:])