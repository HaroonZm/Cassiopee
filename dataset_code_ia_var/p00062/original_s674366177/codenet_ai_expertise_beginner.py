import sys

for ligne in sys.stdin:
    result = 0
    facteurs = [1, 9, 36, 84, 126]
    for i in range(5):
        t = int(ligne[i])
        u = int(ligne[9 - i])
        s = facteurs[i]
        result += s * (t + u)
    print(result % 10)