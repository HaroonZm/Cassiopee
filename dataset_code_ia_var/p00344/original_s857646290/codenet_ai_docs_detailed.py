def count_cyclic_nodes():
    """
    Lit la taille de la liste et la liste des entiers depuis l'entrée standard,
    puis calcule combien de positions forment des cycles complètement contenus
    dans eux-mêmes via une règle particulière de déplacement à partir de chaque indice.

    Cette fonction utilise un algorithme de parcours par détection de cycles sur un graphe fonctionnel
    défini par les transitions de la forme p -> (p + A[p]) % n, où A est la liste d'entiers.
    Une liste auxiliaire `l` garde la trace des états des sommets :
        - 0 : non visité
        - 1 : en cours de parcours (dans le chemin courant)
        - 2 : confirmé membre d'un cycle valide fermé (tous les sommets atteints sont strictement à l'intérieur du cycle)

    Le résultat final est le nombre de positions appartenant à au moins un tel cycle.
    """
    # Lecture du nombre d'éléments dans la liste
    n = int(input())
    # Lecture de la liste d'entiers, décompressée dans A
    *A, = map(int, input().split())

    # Initialisation d'une liste de marqueurs pour suivre les états des indices
    l = [0] * n  # 0: non visité ; 1: en cours ; 2: membre d'un cycle validé

    # Pour chaque indice du tableau
    for i in range(n):
        # Si cet indice n'a pas déjà été marqué
        if l[i] == 0:
            s = set()      # Ensemble des indices visités dans cette exploration
            p = i          # Position actuelle
            can = 1        # Drapeau indiquant si le parcours peut constituer un cycle

            # Parcours jusqu'à retomber sur un indice déjà dans s (cycle), ou croiser un membre déjà exploré
            while p not in s:
                if l[p] == 1:
                    # On croise un chemin déjà traité, non-cycle, donc le cycle n'est pas possible
                    can = 0
                    break
                s.add(p)   # Ajoute la position aux indices du chemin courant
                l[p] = 1   # Marque comme "en cours de parcours"
                # Avance à la prochaine position selon la règle définie
                p = (p + A[p]) % n

            if can:
                # Si un cycle est détecté (retour sur s sans avoir croisé d'extérieur),
                # marque tous ses membres par 2 pour signaler qu'ils appartiennent à un cycle fermé
                while l[p] == 1:
                    l[p] = 2
                    p = (p + A[p]) % n

    # Compte et affiche le nombre de membres du tableau qui sont dans des cycles fermés
    print(sum(e == 2 for e in l))


# Appel principal de la fonction
count_cyclic_nodes()