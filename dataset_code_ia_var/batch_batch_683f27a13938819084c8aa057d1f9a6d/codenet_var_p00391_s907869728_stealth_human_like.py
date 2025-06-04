import sys

# On prend largeur et hauteur (je me rappelle plus si c'est largeur x hauteur ou l'inverse, mais ça devrait aller)
w, h = map(int, input().split())

sumC = 0 # somme des colonnes ?
sumR = 0

col = list(map(int, input().split()))
row = list(map(int, input().split()))

# Ok, on fait la somme "à l'ancienne"
for x in col:
    sumC += x

for y in row:
    sumR += y

# Bon, si les totaux sont pas égaux, on peut rien faire
if sumR != sumC:
    print(0)
    sys.exit()  # je crois que ça fonctionne sans argument aussi

# On commence à remplir
for i in range(w):
    # On trie à chaque fois... je suis pas sûr que ce soit optimal, mais ça marche
    row = sorted(row, reverse=True)
    for j in range(h):
        # Si y'a plus rien à donner ou à prendre, on arrête là pour cette colonne
        if col[i] == 0 or row[j] == 0:
            break
        row[j] -= 1  # on prend un
        col[i] -= 1  # on donne un
    if col[i] > 0:
        print(0)
        sys.exit()
print(1)  # ça passe !