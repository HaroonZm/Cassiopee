# Définition de la fonction make_cycle, qui construit la structure des cycles nécessaires au calcul du coût minimal de tri
def make_cycle(A):
    # Crée une nouvelle liste B qui est une copie de la liste d'entrée A
    # Ceci permet de manipuler B sans modifier A directement
    B = list(A)
    
    # Trie la copie B afin que ses éléments soient dans l'ordre croissant
    B.sort()
    
    # La variable cycle_list est initialisée avec le plus petit élément de B (c'est-à-dire le plus petit élément de A)
    # Cela permettra de comparer facilement les valeurs minimales dans les cycles par la suite
    cycle_list = [B[0]]
    
    # Parcourt chaque élément b de la liste triée B et son indice i
    for i, b in enumerate(B):
        # Vérifie que l'élément courant n'est pas None (c'est-à-dire qu'il n'a pas déjà été utilisé dans un cycle)
        if b != None:
            # Initialise une nouvelle liste représentant le cycle courant
            new_cycle = []
            # Ajoute le premier élément de ce cycle (b) à la liste new_cycle
            new_cycle.append(b)
            
            # Marque l'élément b dans la liste triée B comme utilisé en le remplaçant par None
            # Cela évite d'utiliser deux fois un même élément dans les cycles
            B[i] = None

            # Trouve l'indice si de b dans la liste originale A. C'est la position de b dans A.
            si = A.index(b)

            # Boucle tant que la position courante (si) n'est pas celle de l'élément dans B (i)
            # Cela permet d'explorer toutes les permutations/cycles jusqu'à revenir au point de départ
            while si != i:
                # Prend l'élément de B à la position si
                st = B[si]
                # Ajoute cet élément au cycle en construction
                new_cycle.append(st)
                # Marque cet élément de B comme utilisé (None)
                B[si] = None
                # Met à jour la position si pour continuer le cycle, en cherchant la position de st dans l'original A
                si = A.index(st)

            # Ajoute le cycle courant trouvé à la liste de tous les cycles
            cycle_list.append(new_cycle)
    # Retourne la liste complète de cycles et la valeur minimale initiale
    return cycle_list

# Définition de la fonction min_sorting_cost, qui calcule le coût minimal pour trier la liste
def min_sorting_cost(A):
    # Appelle la fonction make_cycle pour obtenir les cycles nécessaires au calcul
    cycles = make_cycle(A)
    # Le premier élément des cycles est le plus petit élément de tous (la valeur minimale de A)
    min_w = cycles[0]
    # Initialise la variable cost à 0, qui stockera le coût total minimal du tri
    cost = 0

    # Parcourt tous les cycles sauf le premier (c'est-à-dire cycles[1:], car cycles[0] est juste le minimum global)
    for c in cycles[1:]:
        # Calcule le nombre d'éléments n dans le cycle courant
        n = len(c)
        # Le premier élément de c est le plus petit de ce cycle (grâce à make_cycle)
        min_cw = c[0]
        # Calcule une différence "dec" comme (n-1) multiplié par la différence des minimums
        # Cela représente une technique différente de permutation à considérer
        dec = (n - 1) * (min_cw - min_w)
        # Calcule une valeur "inc" qui est deux fois la somme des deux minimums
        # C'est une variante pour permuter plus efficacement les cycles longs
        inc = 2 * (min_w + min_cw)

        # Compare dec et inc pour choisir la méthode de permutation la plus économique
        if dec < inc:
            # Si dec est inférieur à inc, on utilise la première méthode de permutation
            # Ajoute au coût la somme des éléments du cycle plus (n-2) fois le minimum du cycle
            cost += sum(c) + min_cw * (n - 2)
        else:
            # Sinon, on utilise la deuxième technique en ajustant le coût différemment
            # Le coût inclut la somme du cycle, (n-2) fois le minimum du cycle, moins dec plus inc
            cost += sum(c) + min_cw * (n - 2) - dec + inc
    # Retourne le coût total calculé pour trier la liste
    return cost

# Lit un nombre entier depuis l'entrée standard, ce nombre représente la longueur de la liste à trier
n = int(input())

# Lit une ligne de texte depuis l'entrée standard, la coupe en éléments, convertit chaque élément en entier,
# et les range dans la liste A
A = list(map(int, input().split()))

# Calcule le coût minimal de tri de la liste A en appelant min_sorting_cost
ans = min_sorting_cost(A)

# Affiche la réponse (le coût minimal de tri) à la sortie standard
print(ans)