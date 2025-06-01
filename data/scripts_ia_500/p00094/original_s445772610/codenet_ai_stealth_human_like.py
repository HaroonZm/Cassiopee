import sys
# Bon, je lis direct depuis l'entrée standard
f = sys.stdin

a, b = map(int, f.readline().split())  # récupère deux entiers sur la même ligne
res = a * b / 3.305785  # un truc bizarre, sûrement un conversion de surface ?

print(f"{res:.6f}")  # voilà le résultat formaté, 6 décimales c'est précis assez je trouve