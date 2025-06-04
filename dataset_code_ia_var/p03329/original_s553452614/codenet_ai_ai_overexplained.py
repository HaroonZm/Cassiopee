def read_input():
    # Demander à l'utilisateur de saisir une valeur via l'entrée standard (clavier)
    # input() renvoie une chaîne de caractères, donc on convertit en entier avec int()
    n = int(input())
    # On retourne la valeur entière saisie par l'utilisateur
    return n

def count_coin(x, op, min_op):
    # Cette fonction détermine le nombre minimum de pièces nécessaires pour atteindre la somme x
    # x : la somme à atteindre
    # op : liste des valeurs disponibles pour les pièces
    # min_op : dictionnaire de mémoïsation pour stocker les résultats déjà calculés

    # Si la somme à atteindre est 0, aucune pièce n'est nécessaire donc on retourne 0
    if x == 0:
        return 0

    # Vérifier si la solution pour x a déjà été calculée
    # Cela permet de ne pas recalculer plusieurs fois le même résultat et d'optimiser l'algorithme
    if x in min_op.keys():
        return min_op[x]

    # On initialise min_count à une très grande valeur (ici 10 000 000)
    # Cela permet de toujours trouver une valeur minimale plus petite au premier passage
    min_count = 10000000

    # On parcourt chaque valeur de pièce disponible dans op
    for o in op:
        # On vérifie que l'on peut soustraire la pièce "o" de la somme "x" (on ne veut pas de somme négative)
        if x >= o:
            # On effectue l'appel récursif en soustrayant la valeur de la pièce "o" à "x"
            # On ajoute 1 pour la pièce actuellement utilisée
            count = 1 + count_coin(x - o, op, min_op)
            # Si le nombre de pièces total calculé est inférieur au min_count, on met à jour min_count
            if count < min_count:
                min_count = count

    # On mémorise le résultat pour la valeur "x" (mémoïsation) pour ne pas le recalculer plus tard
    min_op[x] = min_count
    # On retourne le nombre minimal de pièces trouvées
    return min_count

def submit():
    # Fonction principale orchestrant la solution au problème

    # On lit la somme cible saisie par l'utilisateur
    n = read_input()

    # On initialise la liste des valeurs de pièces disponibles
    # Il y a toujours une pièce de valeur 1, 6 et 9 disponibles initialement
    ops = [1, 6, 9]

    # Pour chaque valeur de pièce de base (ici après la première, c'est-à-dire 6 et 9)
    # On cherche toutes les puissances de ces valeurs inférieures ou égales à n
    for op in ops[1:]:
        i = 1  # On commence à la puissance 1 (c'est-à-dire op^1)
        t = op ** i  # On calcule la puissance (op élevé à i)
        # Tant que la puissance est inférieure ou égale à n (notre cible)
        while t <= n:
            # On l'ajoute à la liste des pièces disponibles
            ops.append(t)
            # On passe à la puissance suivante
            t *= op  # En multipliant à chaque fois par op, on évite de recalculer la puissance avec **
            # (par exemple 6, 36, 216, ...)

    # On supprime les doublons de la liste des pièces disponibles en les transformant en set puis en liste
    ops = list(set(ops))
    # On trie la liste des pièces par ordre décroissant, ce n'est pas obligatoire pour l'algorithme mais cela peut accélérer certains calculs dans des variantes gloutonnes
    ops.sort(reverse=True)
    # On affiche le résultat du calcul du nombre minimal de pièces pour atteindre la somme n
    # On passe un dictionnaire vide {} au début pour la mémoïsation lors du premier appel
    print(count_coin(n, ops, {}))

# Point d'entrée principal du script Python
# __name__ est une variable spéciale qui contient le nom du module courant
# Lorsque le script est exécuté directement (et non importé depuis un autre module), __name__ vaut '__main__'
# Donc ce bloc garantit que submit() ne sera appelé que si ce fichier est exécuté comme programme principal
if __name__ == '__main__':
    submit()