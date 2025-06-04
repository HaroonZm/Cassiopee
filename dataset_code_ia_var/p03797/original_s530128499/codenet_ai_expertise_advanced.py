from sys import stdin

def solve():
    S, C = map(int, stdin.readline().split())
    if S * 2 >= C:
        print(C // 2)
    else:
        print((C + 2 * S) // 4)

solve()