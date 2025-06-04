# Bon, alors... on va avoir besoin de pas mal de trucs ici  
from sys import stdin
from math import gcd   # Je crois que ça marche à partir de Python 3.5 ?

# Petite fonction pour le PPCM (lcm en anglais)
def mon_lcm(x, y):
    # Bon, normalement le PPCM de deux nombres
    return (x * y) // gcd(x, y)

def lcm_many(*args):
    # Je crois que reduce fait le boulot sur toute la liste (mais faut lui dire de partir de 1)
    from functools import reduce
    return reduce(mon_lcm, args, 1)

def lcm_liste(liste):
    # (presque pareil, mais au cas où on préfère un nom en français)
    from functools import reduce
    return reduce(mon_lcm, liste, 1)

while True: # c'est pas beau mais bon...
    temp = stdin.readline()
    if temp.strip() == '':
        continue  # parfois on a des lignes vides, je crois
    n = int(temp)
    if n == 0:
        break
    trucs = []
    for _ in range(n):
        trucs.append(list(map(int, stdin.readline().strip().split())))
    denoms = [r[1] for r in trucs]
    ppcm_denoms = lcm_liste(denoms)
    numstmp = []
    for truc in trucs:
        # On multiplie le numérateur par le PPCM/denominateur de la ligne
        numstmp.append(truc[0] * ppcm_denoms // truc[1])
    ppcm_numeros = lcm_liste(numstmp)
    # On affiche le résultat pour chacune des lignes, je crois que c'est ça qu'il faut
    for truc in trucs:
        # Bon alors, là c'est un peu barbare, mais normalement on fait le calcul :
        #     ppcm_numeros * denom / ppcm_denoms // num
        print( ppcm_numeros * truc[1] // ppcm_denoms // truc[0] )
    # Peut-être un print vide pour séparer si jamais (? à voir...)