import sys  # On importe le module sys pour manipuler certains aspects du système, comme la récursion et l'entrée standard.

# On défini la limite maximale de récursion pour le programme à un chiffre très élevé (10 millions).
# Cela permet d'éviter des erreurs de récursion profonde pour certains algorithmes récursifs.
sys.setrecursionlimit(10000000)

# On redéfinit la fonction input afin de lire une ligne depuis l'entrée standard (sys.stdin),
# d'enlever tout retour chariot (rstrip) à droite, pour nettoyer la donnée saisie.
input = lambda: sys.stdin.readline().rstrip()

# On démarre une boucle infinie afin de traiter plusieurs ensembles de données tant que l'utilisateur ne termine pas l'entrée.
while True:
    # On lit l'entrée pour la variable n, qui indique le nombre de livres. On convertit la saisie en entier avec int().
    n = int(input())

    # Si n vaut 0, cela signifie que l'utilisateur souhaite arrêter le programme.
    # On quitte la boucle avec break (c'est la condition d'arrêt).
    if n == 0:
        break

    # On crée une liste vide books, dans laquelle chaque élément sera un tuple représentant un livre avec ses temps de lecture et d'écriture.
    books = []

    # On initialise les variables read_t et write_t, qui vont accumuler respectivement le temps total de lecture et d'écriture de tous les livres.
    read_t = 0
    write_t = 0

    # On lance une boucle de n itérations pour lire les n livres un à un.
    for i in range(n):
        # On lit une ligne de deux entiers séparés par un espace, qui représentent les temps de lecture (r) et d'écriture (w) de chaque livre.
        r, w = map(int, input().split())
        # On ajoute le temps de lecture du livre courant à read_t.
        read_t += r
        # On ajoute le temps d'écriture du livre courant à write_t.
        write_t += w
        # On ajoute un tuple (r, w) à la liste books, représentant les temps pour ce livre.
        books.append((r, w))

    # On trie la liste books dans l'ordre croissant par défaut, c'est-à-dire selon le premier élément du tuple (le temps de lecture).
    books = sorted(books)
    # books[-1] est le dernier élément de la liste, donc le livre avec le temps de lecture maximal après le tri.

    # On vérifie si le plus grand temps de lecture n'excède pas la moitié du temps total de lecture.
    # Cela permet de gérer un cas particulier où aucune optimisation supplémentaire n'est nécessaire.
    if books[-1][0] <= read_t // 2:
        # Si la condition est vraie, on affiche alors la somme totale des temps de lecture et d'écriture.
        # On passe ensuite à la prochaine itération de la boucle while.
        print(read_t + write_t)
        continue  # On continue la boucle, donc tout le code en dessous n'est pas exécuté pour cette itération.

    # Si on arrive ici, cela signifie que le cas précédent ne s'applique pas,
    # donc on doit effectuer une optimisation avec programmation dynamique.

    # La variable sukima est calculée comme la différence entre le plus grand temps de lecture et la somme des autres temps de lecture.
    # (Cela représente un "écart" ou déséquilibre entre le plus long livre à lire et les autres).
    sukima = books[-1][0] - (read_t - books[-1][0])

    # On crée une table dp (programmation dynamique) pour mémoriser les solutions partielles.
    # dp[i][j] représentera le maximum de "bonus d'écriture" que l'on peut atteindre en choisissant parmi les i+1 premiers livres
    # avec une contrainte de "capacité" j (reliée à sukima, l'écart à combler).
    # C'est une matrice de dimensions n lignes (un pour chaque livre), et (sukima+1) colonnes (pour chaque valeur possible de bonus jusqu'à sukima).
    dp = [[0 for i in range(sukima + 1)] for i in range(n)]

    # On exécute deux boucles imbriquées :
    # Boucle sur les livres à partir du deuxième (i part de 1 jusqu'à n-1) : on traite un à un tous les livres sauf le premier.
    for i in range(1, n):
        # Boucle sur toutes les valeurs possibles de "bonus d'écriture" (j de 1 jusqu'à sukima inclus).
        for j in range(1, sukima + 1):
            # L'objectif est d'attribuer pour chaque (i,j) la meilleure valeur possible,
            # soit en ignorant le livre i-1 (mettre la valeur précédente),
            # soit en prenant le livre i-1 et en ajoutant son temps d'écriture si cela ne dépasse pas la "capacité" j.
            dp[i][j] = max(
                dp[i - 1][j],  # On ne prend pas ce livre, donc la valeur reste la même que la solution précédente sans ce livre.
                dp[i - 1][j - books[i - 1][1]] + books[i - 1][1] if j - books[i - 1][1] >= 0 else 0
                # On prend le livre courant (i-1), mais uniquement si la capacité résiduelle (j - w) reste non-négative.
                # On ajoute alors le temps d'écriture pour ce livre à l'ancienne valeur dp correspondante.
            )

    # Enfin, on calcule la réponse finale à afficher :
    # C'est la somme des temps de lecture et d'écriture, à laquelle on ajoute sukima (l'écart à combler),
    # puis on retire la meilleure valeur possible stockée dans la case de dp correspondant à tous les livres et à la capacité maximale.
    print(read_t + write_t + sukima - dp[-1][-1])
    # dp[-1][-1] est la dernière valeur de la matrice, qui correspond à la solution optimale trouvée.