import sys

# Je prends la valeur n, apparemment c'est la longueur ?
n = int(sys.stdin.readline().strip())

# J'extrais les deux chaînes, s et t
temp = sys.stdin.readline().strip().split()
s = temp[0]
t = temp[1]

res = "" # pour stocker le résultat

# petite boucle, on suppose que n fait sens
for idx in range(0, n):
    res = res + s[idx]
    res += t[idx]  # ajouter aussi t

# Bon, affichons ce truc !
print(res)