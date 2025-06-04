def count_unique_increasing_sequences():
    """
    Lit une séquence d'entiers entrée par l'utilisateur (sur une seule ligne après un prompt input),
    puis calcule combien de nouveaux nombres distincts apparaissent dans une séquence strictement croissante 
    simulée suivant un algorithme de pile. A chaque fois qu'une valeur plus petite ou égale à la précédente
    apparaît, le haut de la pile est retiré jusqu'à ce que la pile soit vide ou que la valeur du haut soit 
    inférieure ou égale à l'élément en cours. Si l'élément n'est pas présent au sommet de la pile, il est ajouté 
    et le compteur incrémenté.
    Affiche le résultat final.
    """
    n = input()  # Lecture du premier input (taille éventuelle, ignorée ensuite)
    try:
        # Pour Python 2, raw_input lit une ligne d'entiers séparés, map les convertit en int
        a = map(int, raw_input().split())
    except NameError:
        # Pour Python 3, raw_input n'existe pas, mais input fait le même travail
        a = map(int, input().split())

    q = []  # Initialisation de la pile pour stocker les éléments de la séquence croissante
    ans = 0 # Compteur du nombre de nouveaux éléments uniques ajoutés à la séquence croissante

    # Parcours de chaque nombre dans la séquence
    for i in a:
        # Tant que la pile n'est pas vide et que le sommet de la pile est supérieur à l'élément courant,
        # on retire l'élément du sommet (on maintient l'ordre croissant dans la pile)
        while len(q) and q[-1] > i:
            q.pop()
        # Si la pile est vide ou que l'élément courant n'est pas déjà présent au sommet de la pile,
        # on considère qu'il s'agit d'un nouvel ajout unique
        if (not len(q)) or q[-1] != i:
            ans += 1           # Incrémente le compteur pour ce nouvel élément unique
            q.append(i)        # Ajoute l'élément courant au sommet de la pile
    print(ans)  # Affiche le nombre total de nouveaux éléments uniques dans la séquence croissante

# Appel de la fonction principale
count_unique_increasing_sequences()