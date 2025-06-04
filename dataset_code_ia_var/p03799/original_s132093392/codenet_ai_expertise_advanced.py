from sys import stdin

def solve():
    n, m = map(int, stdin.readline().split())
    # Utilisation d'une expression ternaire optimisée et d'une seule instruction print
    print(n + (m - 2 * n) // 4 if 2 * n <= m else m // 2)

solve()