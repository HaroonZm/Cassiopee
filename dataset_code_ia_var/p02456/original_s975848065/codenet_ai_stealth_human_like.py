# Bon, on va essayer de faire ça à la main...
n = int(input())
mon_ensemble = set()
while n > 0:
    n -= 1
    # récupération de l'op, et du x à traiter
    trucs = input().split()
    op = int(trucs[0])
    x = int(trucs[1])
    if op == 1:
        print(int(x in mon_ensemble))  # j'ai mis int() mais on aurait pu direct le bool
    elif op == 0:
        mon_ensemble.add(x)
        print(len(mon_ensemble))  # là pareil, ça affiche la taille après ajout
    else:
        try:
            mon_ensemble.remove(x)  # discard ne plante pas, mais remove oui
        except KeyError:
            pass  # on fait rien si pas là...
# Fin du code (normalement ça marche mais c'est pas ultra optimisé)