# Lecture d'une valeur entière depuis l'entrée standard (typiquement le clavier)
# La fonction input() lit une chaîne de caractères, on la convertit donc en entier avec int()
n = int(input())

# Lecture d'une chaîne de caractères depuis l'entrée standard
s = input()

# Initialisation de compteurs pour différentes sous-séquences ou caractères spécifiques dans la chaîne
jo_cnt = 0  # compteur pour le nombre de paires "JO" rencontrées indirectement
oi_cnt = 0  # compteur pour le nombre de paires "OI"
j_cnt = 0   # compteur du nombre de caractères 'J' rencontrés jusqu'ici
o_cnt = 0   # compteur du nombre de caractères 'O' rencontrés jusqu'ici
i_cnt = 0   # compteur du nombre de caractères 'I' rencontrés jusqu'ici
joi_cnt = 0 # compteur pour le nombre de triplets "JOI"

# Listes qui vont accumuler les comptages de 'J', 'O' et 'I' au fur et à mesure qu'on parcourt la chaîne
j_acc = []
o_acc = []
i_acc = []

# Parcours de chaque caractère 'c' dans la chaîne 's'
for c in s:
    # Si le caractère est 'J', on incrémente le compteur de 'J'
    if c == "J":
        j_cnt += 1
    # Sinon, si le caractère est 'O'
    elif c == "O":
        # On incrémente le compteur de 'O'
        o_cnt += 1
        # On ajoute la quantité de 'J' déjà rencontrés pour compter les occurrences de "JO"
        jo_cnt += j_cnt
    else:
        # Sinon c'est 'I' (on suppose que la chaîne ne contient que 'J','O','I')
        # On incrémente le compteur de 'I'
        i_cnt += 1
        # On ajoute la quantité de 'O' déjà rencontrés pour compter les occurrences de "OI"
        oi_cnt += o_cnt
        # On ajoute aussi la quantité de "JO" déjà comptées pour compter les occurrences de "JOI"
        joi_cnt += jo_cnt

    # On conserve les compteurs actuels à chaque position pour une utilisation ultérieure
    j_acc.append(j_cnt)
    o_acc.append(o_cnt)
    i_acc.append(i_cnt)

# Calcul d'une quantité particulière appelée ji_cnt :
# Pour chaque position i (allant de 0 à n-1),
# on multiplie le nombre de 'J' rencontrés jusqu'à i par le nombre d''I' rencontrés après i
# Puis on garde la valeur maximale de ce produit
ji_cnt = max(j_acc[i] * (i_acc[-1] - i_acc[i]) for i in range(n))

# Résultat final à afficher :
# On additionne le nombre total de triplets "JOI" complets
# avec le maximum parmi trois quantités : le nombre de "JO", le nombre de "OI", ou cette quantité ji_cnt calculée auparavant
print(joi_cnt + max(jo_cnt, oi_cnt, ji_cnt))