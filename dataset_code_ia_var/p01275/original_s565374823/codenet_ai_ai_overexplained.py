def solve():
    # Cette fonction principale encapsule toute la logique du programme.
    # Elle ne prend aucun argument car l'entrée sera lue directement depuis stdin (entrée standard).

    def bfs(k):
        # La fonction 'bfs' prend en entrée un entier 'k'.
        # 'k' indique le nombre de digits à traiter pour chaque nombre du problème.
        # Elle implémente une recherche en largeur (Breadth First Search) sur des états représentés par des listes de différences de digits.

        # Lit une ligne de l'entrée standard via file_input et la sépare en deux chaînes, start et goal.
        start, goal = file_input.readline().split()

        # Si la chaîne de départ est déjà égal à la chaîne d'arrivée, alors il n'est pas nécessaire de faire d'opération.
        # On retourne donc immédiatement 0.
        if start == goal:
            return 0

        # Convertit chaque caractère (chiffre) des chaînes 'start' et 'goal' en entiers avec map(int, ...).
        # Par exemple, '123' -> (1, 2, 3)
        start = map(int, start)
        goal = map(int, goal)

        # Calcule la différence modulo 10 pour chaque chiffre de 'goal' et 'start', ainsi la différence est toujours comprise entre 0 et 9.
        # zip(goal, start) crée un itérable de paires (g, s) où g provient de 'goal' et s de 'start'.
        # Pour chaque paire, soustrait s de g, puis fait le modulo 10.
        # Résultat : liste avec la différence entre chaque chiffre des deux nombres.
        diff = [(g - s) % 10 for g, s in zip(goal, start)]

        # Initialise la file (pour BFS) avec un seul élément : notre état initial 'diff'.
        # La file q est une liste de listes de longueurs k, où chaque liste représente une configuration courante des différences de chiffres.
        q = [diff]

        # Crée un dictionnaire 'checked' dont les clés sont des tuples représentant les configurations déjà visitées,
        # pour éviter de traiter un même état plusieurs fois (marque les états déjà visités, car BFS peut y repasser).
        checked = {tuple(diff): True}

        # Initialise le compteur de niveaux ou d'opérations à 0.
        ans = 0

        # Commence la boucle principale de BFS.
        # À chaque itération, nous essayons toutes les transitions possibles à partir des états de 'q'.
        while q:
            # Incrémente le nombre d'opérations effectuées à chaque niveau de la BFS (chaque "profondeur").
            ans += 1

            # Crée une nouvelle liste vide 't_q' qui contiendra les états du prochain niveau de BFS.
            t_q = []

            # Parcourt chaque configuration 'd' actuelle dans la file 'q'.
            for d in q: 
                # Pour chaque configuration, trouve le premier chiffre (à l'index i) qui n'est pas déjà à 0
                # (c'est-à-dire qui doit encore être modifié pour atteindre la configuration finale).
                for i, r in enumerate(d):
                    # 'i' est l'indice et 'r' la valeur à cet endroit.
                    # Si r != 0, on a trouvé le premier chiffre à traiter, donc on s'arrête.
                    if r != 0:
                        break

                # Pour chaque position 'j' de i à k - 1 (c'est-à-dire de la première position non nulle jusqu'au dernier chiffre),
                # essaye une opération : soustraire la différence 'r' à tous les chiffres de d[i] à d[j] inclus.
                for j in range(i, k):
                    # On modifie directement la liste d, d'où le rétablissement ultérieur par copie de liste.
                    d[j] -= r         # Soustrait r
                    d[j] %= 10        # On reste dans l'intervalle [0,9] grâce au modulo

                    key = tuple(d)    # Convertit la liste d en tuple car il est hashable, prêt à être utilisé comme clé dans le dict.

                    if key in checked:
                        # Si cette configuration a déjà été visitée, on ne fait rien et on passe à la suivante.
                        continue

                    # Si tous les chiffres de cette configuration sont désormais à 0, cela signifie que la cible est atteinte.
                    if sum(d) == 0:
                        # On retourne le nombre d'opérations effectuées ('ans').
                        return ans

                    # Sinon, on marque cette configuration comme visitée.
                    checked[key] = True

                    # On ajoute une copie de la configuration actuelle à la nouvelle file 't_q'.
                    t_q.append(d[:])  # d[:] crée une copie superficielle de la liste d.

                # Après avoir généré tous les enfants du nœud courant, on passe au prochain dans q.

            # Remplace la file de niveau courant par celle du niveau suivant.
            q = t_q

        # Si la boucle sort sans avoir trouvé la solution, cela signifie que l'état cible n'est pas atteignable (ce qui ne devrait pas arriver).
        # (Pas explicitement géré ici, donc None sera renvoyé par défaut.)

    # Importe stdin pour la lecture depuis l'entrée standard.
    from sys import stdin

    # 'file_input' est simplement un alias pour stdin, qu'on utilisera pour les lectures de lignes.
    file_input = stdin

    # Boucle principale du programme.
    while True:
        # Lit un entier 'k' sur une ligne de l'entrée standard.
        k = int(file_input.readline())

        # Si l'entier lu est 0, alors cela indique qu'il faut terminer l'exécution du programme.
        if k == 0:
            break

        # Appelle la fonction bfs(k) pour traiter une instance du problème,
        # puis imprime le résultat (nombre minimal d'opérations nécessaires).
        print(bfs(k))

# Appel à la fonction principale pour démarrer le programme.
solve()