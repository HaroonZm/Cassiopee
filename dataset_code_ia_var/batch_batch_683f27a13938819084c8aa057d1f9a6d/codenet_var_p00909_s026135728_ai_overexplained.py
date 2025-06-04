def solve():
    # Définition d'une fonction pour traiter une opération de mesure entre deux éléments (a et b) avec une différence de poids w.
    def measurement(a, b, w):
        # Récupérer la racine de l'ensemble (le représentant) pour l'élément a.
        a_root = root[a]
        # Récupérer la racine de l'ensemble (le représentant) pour l'élément b.
        b_root = root[b]
        # Vérifier si a et b ne sont pas déjà dans le même ensemble.
        if a_root != b_root:
            # Récupérer la liste des membres de l'ensemble contenant a.
            a_member = member[a_root]
            # Récupérer la liste des membres de l'ensemble contenant b.
            b_member = member[b_root]
            # Calculer le décalage (offset) à appliquer lors de la fusion des ensembles.
            # Offset représente la correction nécessaire pour maintenir la contrainte de poids (différence équivalente à w).
            offset = w - (weight[b] - weight[a])
            # Vérifier quel ensemble est le plus grand pour minimiser le coût de fusion (union by size).
            if len(a_member) > len(b_member):
                # Si l'ensemble de a est plus grand, on y ajoute les membres de l'ensemble de b.
                a_member.extend(b_member)
                # Pour chaque membre n de l'ancien ensemble de b :
                for n in b_member:
                    # On change sa racine (représentant) pour qu'il pointe désormais vers celle de a.
                    root[n] = a_root
                    # On met à jour le poids relatif de n pour maintenir la cohérence de la contrainte.
                    weight[n] += offset
            else:
                # Si l'ensemble de b est plus grand ou de même taille, on fait la fusion inverse.
                b_member.extend(a_member)
                # Pour chaque membre n de l'ancien ensemble de a :
                for n in a_member:
                    # On change sa racine (représentant) pour qu'il pointe désormais vers celle de b.
                    root[n] = b_root
                    # On met à jour le poids relatif de n, ici en soustrayant l'offset.
                    weight[n] -= offset

    # Fonction qui traite une requête (question) sur la différence de poids entre deux éléments donnés.
    def inquiry(a, b):
        # Vérifie si a et b sont dans le même ensemble (c'est-à-dire qu'ils sont reliés).
        if root[a] == root[b]:
            # Si oui, retourne la différence de poids relative entre b et a.
            return weight[b] - weight[a]
        else:
            # Sinon, il est impossible de savoir donc on retourne le mot-clé requis.
            return 'UNKNOWN'

    # Fonction qui traite une ligne d'entrée correspondant à une opération ou une question.
    def operation(line):
        # Si la ligne commence par '!', c'est une opération d'ajout de contrainte ('! a b w').
        if line[0] == '!':
            # On récupère les entiers a, b, w à partir du texte de la ligne (en ignorant le symbole et l'espace).
            a, b, w = map(int, line[2:].split())
            # On appelle la fonction measurement correspondante.
            measurement(a, b, w)
        else:
            # Sinon, c'est une question de requête ('? a b').
            a, b = map(int, line[2:].split())
            # On retourne le résultat de la fonction inquiry.
            return inquiry(a, b)

    # Import de la bibliothèque système pour la gestion des entrées/sorties.
    import sys
    # Lecture de toutes les lignes fournies sur l'entrée standard, cela retourne une liste de chaînes de caractères.
    file_input = sys.stdin.readlines()

    # On entre dans une boucle infinie qui s'arrêtera quand il n'y aura plus de données à traiter.
    while True:
        # On lit le nombre N (nombre d'éléments) et M (nombre d'opérations) à partir de la première ligne du fichier d'entrée.
        N, M = map(int, file_input[0].split())
        # Si N vaut 0, cela indique la fin des données. On sort alors de la boucle.
        if N == 0:
            break

        # Initialisation d'une liste 'root' contenant la racine de chaque élément (au début chaque élément est sa propre racine).
        root = [i for i in range(N + 1)]  # Les indices vont de 0 à N inclus, mais dans le problème 0 n'est pas utilisé.
        # Initialisation d'une liste 'member' contenant pour chaque représentant la liste des membres de l'ensemble.
        member = [[i] for i in range(N + 1)]
        # Initialisation d'une liste 'weight' qui stocke, pour chaque élément, la différence de poids cumulée par rapport à la racine.
        weight = [0] * (N + 1)

        # Génération de tous les résultats pour les M lignes suivantes par compréhension.
        # Ces résultats correspondent soit à une valeur entière, soit à None si ce n'était pas une question.
        ans = (operation(line) for line in file_input[1:M+1])
        # On ne garde que les résultats non None (c'est-à-dire uniquement les réponses aux requêtes).
        ans = filter(lambda x: x != None, ans)
        # Affichage de toutes les réponses, chacune sur une nouvelle ligne.
        print(*ans, sep='\n')

        # On enlève du fichier d'entrée les M lignes d'opérations qu'on vient de traiter ainsi que la ligne de paramètres (totale M+1).
        del file_input[:M+1]

# Appel à la fonction principale pour lancer la résolution du problème.
solve()