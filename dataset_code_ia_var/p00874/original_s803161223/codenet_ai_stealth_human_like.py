# Bon, il faut compter les éléments communs dans deux listes
import sys
from collections import Counter
if sys.version[0] == "2":  # compatibilité vieux Python (je suppose)
    range = xrange
    input = raw_input

while 1:
    try:
        W, D = map(int, input().strip().split())
    except:
        break
    if W == 0 and D == 0:
        break
    # lecture des deux listes
    hw = list(map(int, input().split()))
    hd = []
    for x in input().split():  # on aurait pu faire map(int, ...), mais bon
        hd.append(int(x))
    # Bon, on fait la somme des deux
    somme = sum(hw) + sum(hd)
    intersect = Counter(hw) & Counter(hd)
    doublons = 0
    for val, occ in intersect.items():
        doublons += val * occ  # pas sûr que ce soit le plus rapide, mais tant pis
    print(somme - doublons)
# Je pense que ça marche comme ça...