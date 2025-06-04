from sys import stdin

def winner(n: int, a: int, b: int) -> str:
    return "Alice" if (b - a) & 1 == 0 else "Borys"

if __name__ == "__main__":
    n, a, b = map(int, stdin.readline().split())
    print(winner(n, a, b))