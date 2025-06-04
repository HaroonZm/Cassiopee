from functools import reduce
import operator

# Lecture des entrées
H, W = map(lambda x: int(''.join(reversed(x))), map(str, input().split()))
P = list(map(lambda _: input(), range(H)))

# Générateur de lignes pleines de points
make_row = lambda char: list(map(lambda _: char, range(W)))

# Construction via compréhensions et chaînes d'opérations paresseuses
red = list(map(lambda y: make_row('.'), range(H)))
blue = list(map(lambda y: make_row('.'), range(H)))

# Marquage colonne 0 et W-1 par manipulation de tableaux
list(map(lambda t: (operator.setitem(red[t[0]], 0, '#'), operator.setitem(blue[t[0]], W-1, '#'), [
    (operator.setitem(red[t[0]], j, '#') if t[0] % 2 == 0 else operator.setitem(blue[t[0]], j, '#')) 
    for j in range(1, W-1)
]), enumerate(range(H))))

# Dédoublonnage plein centre si # détecté
[list(map(lambda ij: (operator.setitem(red[ij[0]], ij[1], '#'), operator.setitem(blue[ij[0]], ij[1], '#')) if P[ij[0]][ij[1]] == '#' else None,
      [(i,j) for i in range(1, H-1) for j in range(1, W-1)]))]

# Affichage des grilles
print('\n'.join(list(map(lambda r: reduce(lambda a,b: a+b, r), red))))
print()
print('\n'.join(list(map(lambda r: ''.join(map(str, r)), blue))))