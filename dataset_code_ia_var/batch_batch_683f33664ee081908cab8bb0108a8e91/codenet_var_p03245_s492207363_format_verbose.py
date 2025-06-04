nombre_de_points = int(input())

liste_coordonnees_points = [
    [int(valeur) for valeur in input().split()]
    for _ in range(nombre_de_points)
]

modulo_parite_initiale = (liste_coordonnees_points[0][0] + liste_coordonnees_points[0][1]) % 2

for abscisse, ordonnee in liste_coordonnees_points:
    if (abscisse + ordonnee) % 2 != modulo_parite_initiale:
        print(-1)
        exit()

if modulo_parite_initiale == 1:
    print(31)
    print(" ".join([str(2 ** exposant) for exposant in range(31)]))
else:
    print(32)
    print("1 " + " ".join([str(2 ** exposant) for exposant in range(31)]))

for abscisse, ordonnee in liste_coordonnees_points:

    abscisse_modifiee = abscisse
    ordonnee_modifiee = ordonnee
    
    if modulo_parite_initiale == 0:
        abscisse_modifiee -= 1
        print("R", end="")

    somme_coordonnees = abscisse_modifiee + ordonnee_modifiee
    difference_coordonnees = abscisse_modifiee - ordonnee_modifiee
    
    bits_direction = [[0] * 31 for _ in range(2)]
    
    if somme_coordonnees < 0:
        bits_direction[0] = [1] * 31
        bits_direction[0][30] = 0
    else:
        bits_direction[0][30] = 1

    if difference_coordonnees < 0:
        bits_direction[1] = [1] * 31
        bits_direction[1][30] = 0
    else:
        bits_direction[1][30] = 1

    for indice_bit in range(30):
        if somme_coordonnees >= 0 and (abs(somme_coordonnees) // 2 >> indice_bit) & 1:
            bits_direction[0][indice_bit] = 1
        if somme_coordonnees < 0 and (abs(somme_coordonnees) // 2 >> indice_bit) & 1:
            bits_direction[0][indice_bit] = 0
        if difference_coordonnees >= 0 and (abs(difference_coordonnees) // 2 >> indice_bit) & 1:
            bits_direction[1][indice_bit] = 1
        if difference_coordonnees < 0 and (abs(difference_coordonnees) // 2 >> indice_bit) & 1:
            bits_direction[1][indice_bit] = 0

    for bit_somme, bit_difference in zip(bits_direction[0], bits_direction[1]):
        if bit_somme == 1 and bit_difference == 1:
            print("R", end="")
        elif bit_somme == 0 and bit_difference == 0:
            print("L", end="")
        elif bit_somme == 1 and bit_difference == 0:
            print("U", end="")
        elif bit_somme == 0 and bit_difference == 1:
            print("D", end="")

    print("")