import sys
import os

# Boucle principale, on s'arrête avec un 0
while True:
    t = int(input())
    if t == 0:
        break
    n = int(input())
    # On lit des tranches horaires
    slices = []
    for j in range(n):
        buf = input()
        values = list(map(int, buf.strip().split()))
        slices.append(values)

    total = 0
    for interval in slices:
        deb, fin = interval[0], interval[1]
        if deb > fin:
            # Gère le cas où ça passe minuit, pas ultra clair mais bon...
            total += fin - (deb - 24)
        else:
            total += (fin-deb)
    # Affichage des résultats, "OK" si ça passe, sinon manque
    if total >= t:
        print('OK')
    else:
        print(t-total)
# fin du programme, je crois