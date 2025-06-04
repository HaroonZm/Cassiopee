def solve():
    # Importation du module 'sys' pour accéder à la lecture d'entrée standard (stdin)
    from sys import stdin
    # Création d'un alias 'f_i' pour 'stdin', ce qui permet de lire facilement les lignes d'entrée
    f_i = stdin

    # Lecture de la première ligne de l'entrée, qui contient deux entiers séparés par un espace : N et C
    # N est le nombre total d'équipes (teams), C est le nombre total de commandes à traiter
    # 'readline()' lit une ligne entière et 'split()' la divise en une liste de strings sur les espaces
    # 'map(int, ...)' convertit chaque string en un entier
    N, C = map(int, f_i.readline().split())

    # Construction de la liste 'ranking' qui va contenir des tuples constitués de deux éléments :
    # (score, numéro de l'équipe). Initialement, chaque équipe a un score de 0.
    # La liste de compréhension parcourt les numéros d'équipe de 1 à N inclus, et place 0 comme score initial
    ranking = [(0, i) for i in range(1, N + 1)]

    # Insertion d'un élément fictif tout au début de la liste 'ranking'.
    # Cet élément a pour score un nombre très négatif pour s'assurer qu'il reste au début de la liste.
    # '(-1000000000 * C, 0)' crée un tuple avec une valeur très négative comme score et 0 comme identifiant d'équipe.
    # Cela sert d'ancre/sentinelle technique pour des raisons liées à la gestion de l'indexation lors des requêtes de classement.
    ranking.insert(0, (-1000000000 * C, 0))

    # Création d'une liste 'score' de taille N + 1 (pour inclure l'indice 0 inutile) initialisée à 0,
    # où score[t] stocke le score courant (en valeur négative) de l'équipe numéro t.
    # Ceci permet de retracer rapidement le score actuel d'une équipe pour les mises à jour
    score = [0] * (N + 1)

    # Importation de deux fonctions depuis le module 'bisect' : 'bisect_left' et 'insort'.
    # 'bisect_left' permet de trouver rapidement la position d'un élément dans une liste triée.
    # 'insort' insère un élément dans la liste tout en maintenant son ordre trié.
    from bisect import bisect_left, insort

    # Création d'une liste vide 'ans' pour stocker les résultats des commandes de type requête.
    ans = []

    # Itération sur la plage de C pour traiter chaque commande une à une.
    for i in range(C):
        # Lecture d'une commande sous forme de liste de strings via 'split()'.
        # Chaque commande peut être de deux types : modification de score (type 0) ou requête (type 1).
        cmd = f_i.readline().split()

        # Si le premier élément de 'cmd' est '0', il s'agit d'une commande de modification du score d'une équipe.
        if cmd[0] == '0':
            # Récupération depuis la commande du numéro d'équipe t et des points p à soustraire.
            t, p = map(int, cmd[1:])

            # Récupération du score courant de l'équipe t, stocké dans la liste 'score'.
            pre_score = score[t]
            # Création d'un tuple '(pre_score, t)' représentant l'entrée actuelle à supprimer dans 'ranking'.
            pre_rec = (pre_score, t)
            # Recherche de l'indice où se trouve 'pre_rec' dans la liste triée 'ranking' à l'aide de 'bisect_left'.
            idx = bisect_left(ranking, pre_rec)
            # Suppression de l'entrée actuelle de l'équipe t dans la liste des classements pour mettre à jour sa position ensuite.
            ranking.pop(idx)
            # Calcul du nouveau score temporaire : on soustrait p au score précédent.
            # Remarque : les scores sont stockés avec le signe négatif, donc on "soustrait" p pour obtenir un score plus bas.
            new_score = pre_score - p  # score is stored as a negative value
            # Mise à jour dans le tableau des scores du score de l'équipe t.
            score[t] = new_score
            # Insertion dans la liste triée du nouveau tuple (nouveau score, numéro d'équipe).
            # Cela garantira que l'ordre de la liste des classements reste correct.
            insort(ranking, (new_score, t))

        # Si le premier élément de 'cmd' n'est pas '0', cela correspond à une commande de requête classements
        else:
            # Récupération depuis la commande de l'indice de classement m désiré.
            m = int(cmd[1])
            # On récupère depuis la liste 'ranking' l'entrée à la position m (tuple (score, team_number))
            p, t = ranking[m]
            # On ajoute à la liste 'ans' une string composée du numéro d'équipe et du score positif associé.
            # p est un score négatif, donc on l'inverse de signe pour l'affichage.
            ans.append(' '.join(map(str, (t, -p))))
    # Après traitement de toutes les commandes, on affiche les résultats des requêtes, un par ligne.
    print('\n'.join(ans))

# Appel de la fonction principale pour exécuter l'ensemble du code ci-dessus
solve()