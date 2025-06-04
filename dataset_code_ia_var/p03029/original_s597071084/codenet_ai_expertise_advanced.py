from sys import stdin

def calculer_resultat(a: int, p: int) -> int:
    return (a * 3 + p) // 2

if __name__ == "__main__":
    print(calculer_resultat(*map(int, stdin.readline().split())))