droit = set('yuiophjklnm')
tordu = lambda x: x in droit
continuer = lambda x: x != '#'
while continuer((E := input())):
    compte = 0
    for p, q in zip(E, E[1:]):
        if tordu(p) ^ tordu(q): compte = compte + True
    print(compte)