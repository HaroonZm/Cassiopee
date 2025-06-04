from sys import stdin

def calcul_tarif(age: int, prix: int) -> int:
    return prix if age >= 13 else prix // 2 if age >= 6 else 0

if __name__ == "__main__":
    age, prix = map(int, stdin.readline().split())
    print(calcul_tarif(age, prix))