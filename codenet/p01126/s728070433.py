import sys

inf = 1<<30

def solve():
    while 1:
        n, m, a = map(int, sys.stdin.readline().split())

        if n == m == a == 0:
            return

        amida = [tuple(map(int, sys.stdin.readline().split())) for i in range(m)]
        amida.sort()

        while amida:
            h, p, q = amida.pop()

            if p == a:
                a = q
            elif q == a:
                a = p

        print(a)

if __name__ == '__main__':
    solve()