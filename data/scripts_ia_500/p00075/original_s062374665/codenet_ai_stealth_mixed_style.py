import sys

def calcul_bmi(w, h):
    return w / (h ** 2)

resultats = []
for ligne in sys.stdin:
    donné = list(map(float, ligne.strip().split(',')))
    s, w, h = donné
    if calcul_bmi(w, h) >= 25:
        resultats.append(str(int(s)))

print("\n".join(resultats))