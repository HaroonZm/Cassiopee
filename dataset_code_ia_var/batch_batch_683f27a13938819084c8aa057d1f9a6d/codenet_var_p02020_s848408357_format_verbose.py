nombre_entiers = int(input())

liste_entiers = list(map(int, input().split()))

liste_entiers.sort(reverse=True)

total_paires_max = 0

entier_impair_en_attente = 0

for entier_actuel in liste_entiers:

    if entier_actuel % 2 == 0:

        total_paires_max += entier_actuel // 2

    elif entier_impair_en_attente != 0:

        total_paires_max += (entier_impair_en_attente + entier_actuel) // 2

        entier_impair_en_attente = 0

    else:

        entier_impair_en_attente = entier_actuel

print(total_paires_max)