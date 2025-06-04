from sys import stdin

def calculer(a: int, p: int) -> int:
    return (a * 3 + p) // 2

if __name__ == "__main__":
    print(calculer(*map(int, stdin.readline().split())))