from sys import stdin

def solve():
    n, a, b = map(int, stdin.readline().split())
    match (n, a > b, a == b):
        case (1, _, True):
            print(1)
        case (1, _, _) | (_, True, _):
            print(0)
        case _:
            print((n - 2) * (b - a) + 1)

solve()