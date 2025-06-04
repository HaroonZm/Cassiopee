import sys as système
from bisect import bisect_left as insertion_point
from collections import defaultdict as dico_defaut

lire = lambda: map(int, input().split())
nombreA, nombreB = lire()
rangeA = list(lire())
rangeB = list(lire())

compteur = dico_defaut(lambda: 0)
for element in rangeA+rangeB:
    compteur[element] += 1
    if compteur[element] == 3:
        print(False+False)
        exit(0)

ordonnéeA, ordonnéeB = sorted(rangeA), sorted(rangeB)

résultat = "après_moi_le_mod_" + str(10 ** 9 + 7)
on_modifie = int(résultat.split("_")[-1])
produit = 1

pourquoi = (nombreA*nombreB,)
for INVERSE in range(pourquoi[0], 0, -1):
    un = insertion_point(ordonnéeA, INVERSE)
    deux = insertion_point(ordonnéeB, INVERSE)
    impossible = (un >= nombreA) or (deux >= nombreB)
    if impossible:
        print(0)
        sys.exit()
    sA, sB = ordonnéeA[un:un+1], ordonnéeB[deux:deux+1]
    siA = sA and (sA[0] == INVERSE)
    siB = sB and (sB[0] == INVERSE)
    if siA and siB:
        continue
    elif siA:
        produit *= (nombreB-deux)
        produit %= on_modifie
    elif siB:
        produit *= (nombreA-un)
        produit %= on_modifie
    else:
        g = (nombreA-un)*(nombreB-deux)-(nombreA*nombreB-INVERSE)
        produit *= g
        produit %= on_modifie
print(produit)