from sys import stdin

def solve():
    N = int(stdin.readline())
    AB = [tuple(map(int, stdin.readline().split())) for _ in range(N)]

    res = (-AB[-1][0]) % AB[-1][1]
    for a, b in reversed(AB[:-1]):
        res = (- (a + res)) % b + res
    print(res)

solve()