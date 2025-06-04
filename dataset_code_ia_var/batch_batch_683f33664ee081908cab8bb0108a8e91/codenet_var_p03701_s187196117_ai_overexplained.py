# Demande à l'utilisateur d'entrer un nombre entier qui sera stocké dans N.
N = int(input())  # N représente le nombre d'éléments dans la liste S.

# Crée une liste S qui va contenir des entiers lus à partir des prochaines saisies utilisateur.
# La compréhension de liste va itérer N fois pour remplir la liste.
S = [int(input()) for _ in range(N)]

# Crée une liste 'table' de taille suffisamment grande pour stocker tous les états possibles de la somme d'éléments.
# Ici, 200 * 200 + 1 est utilisé comme borne supérieure, car chaque élément de S ne dépassera probablement pas 200.
# Chaque élément de 'table' est initialisé à False, ce qui veut dire 'cette somme n'est pas encore atteignable'.
table = [False] * (200 * 200 + 1)

# Marquer la somme 0 comme atteignable, car sans choisir aucun élément, la somme obtenue est 0.
table[0] = True

# Variable 'ma' qui va contenir la somme totale des éléments traités jusqu'à maintenant (maximal courant atteignable).
ma = 0

# Parcourt chaque élément 's' dans la liste S.
for s in S:
    # Augmente 'ma' de la valeur de 's'. Cela signifie que la somme maximale possible augmente à chaque ajout.
    ma += s

    # Pour chaque somme possible 'i' actuellement atteignable (de la plus grande vers 0),
    # vérifie si la somme (i+s) devient maintenant atteignable.
    # On commence de 'ma' et on diminue jusqu'à 0 pour éviter de compter plusieurs fois la valeur d'un même 's'.
    for i in range(ma, -1, -1):
        # L'opérateur '|=' met table[i+s] à True si table[i] est True (ou si c'était déjà True).
        # Cela signifie que si la somme 'i' est atteignable, alors la somme 'i+s' l'est aussi en ajoutant 's'.
        table[i + s] |= table[i]

# Recherche de la somme atteignable maximale 'i' inférieure ou égale à 'ma' telle que
# 'i' n'est pas un multiple de 10, et pour laquelle table[i] est True (donc réalisable).
for i in range(ma, -1, -1):
    # Vérifie deux conditions :
    # 1. 'i' n'est pas un multiple de 10 (i % 10 != 0), donc il reste un reste non nul lorsqu'on divise i par 10.
    # 2. 'table[i]' est True, c'est-à-dire que cette somme peut être obtenue à partir d'une combinaison d'éléments de S.
    if i % 10 != 0 and table[i]:
        # Si les deux conditions sont remplies, afficher la valeur de 'i'.
        print(i)
        # Sort de la boucle car on recherche la somme maximale qui remplit ces critères.
        break
# Si la boucle n'a jamais exécuté le 'break', cela signifie aucune somme ne remplit les critères demandés.
else:
    # Affiche 0 pour signaler qu'il n'existe aucune somme réalisable qui ne soit pas un multiple de 10.
    print(0)