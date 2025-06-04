# Débuter une boucle infinie en utilisant 'while True'.
# Cette boucle continuera de s'exécuter indéfiniment jusqu'à ce qu'une instruction break soit rencontrée.
while True:
    # Demander une saisie utilisateur via la fonction input(), lire la saisie de l'utilisateur au format chaîne de caractères.
    # Convertir cette chaîne de caractères en entier à l'aide de int().
    # Stocker cette valeur entière dans la variable 'n'.
    n = int(input())
    
    # Vérifier si la valeur entrée par l'utilisateur est égale à 0 avec une condition if.
    # En Python, l'opérateur '==' compare deux valeurs pour l'égalité.
    if n == 0:
        # Si n vaut 0, sortir de la boucle infinie grâce à l'instruction break.
        break
    
    # Initialiser une liste vide nommée 'books'. Cette liste servira à stocker des tuples de deux valeurs extraites plus tard.
    books = []
    
    # Initialiser la variable 'read_t' à 0.
    # Cette variable va accumuler le total des temps de 'lecture'.
    read_t = 0
    
    # Initialiser la variable 'write_t' à 0.
    # Cette variable va accumuler le total des temps de 'rédaction/écriture'.
    write_t = 0
    
    # Utiliser une boucle for pour répéter une séquence d'instructions 'n' fois.
    # La fonction range(n) génère une séquence d'entiers de 0 à n-1.
    for i in range(n):
        # Lire une ligne de saisie utilisateur, la découper grâce à split().
        # Utiliser map(int, ...) pour convertir chaque segment en entier.
        # Affecter le premier entier à la variable 'r' et le second à la variable 'w'.
        r, w = map(int, input().split())
        
        # Ajouter la valeur de 'r' à la variable cumulée 'read_t'.
        read_t += r
        
        # Ajouter la valeur de 'w' à la variable cumulée 'write_t'.
        write_t += w
        
        # Ajouter le couple (r, w), c'est-à-dire le tuple composé de 'r' et 'w', à la liste des 'books'.
        books.append((r, w))
    
    # Trier la liste 'books' en ordre croissant.
    # Par défaut, la méthode sorted() trie les tuples en comparant d'abord le premier élément, puis le suivant, etc.
    books = sorted(books)
    
    # Accéder au dernier élément de la liste triée avec 'books[-1]'.
    # Récupérer le premier élément du tuple de ce dernier élément avec '[0]'.
    # Vérifier si cette valeur est inférieure ou égale à la moitié entière du total de lecture (read_t // 2).
    # L'opérateur '//' effectue une division entière (sans décimale).
    if books[-1][0] <= read_t // 2:
        # Si la condition est vraie, afficher la somme totale de 'read_t' et de 'write_t' grâce à la fonction print().
        print(read_t + write_t)
        # Passer immédiatement à l'itération suivante de la boucle while.
        continue
    
    # Calculer l'écart ('sukima') en soustrayant du plus grand temps de lecture 'books[-1][0]' la somme des temps de lecture
    # de tous les autres livres, c'est-à-dire 'read_t - books[-1][0]'.
    sukima = books[-1][0] - (read_t - books[-1][0])
    
    # Construire une table de programmation dynamique (DP) représentée par une liste de listes (tableau 2D).
    # Créer une liste contenant 'n' éléments, chacun étant une liste remplie de zéros de longueur 'sukima + 1'.
    # C'est-à-dire que 'dp[i][j]' sera initialisé à zéro pour tous les indices i et j.
    dp = [[0 for i in range(sukima + 1)] for i in range(n)]
    
    # Parcourir les indices de 1 à n-1 avec une boucle for, en commençant par 1 (le premier livre est séparé du reste).
    for i in range(1, n):
        # Pour chaque valeur possible de 'j' allant de 1 à 'sukima' inclus, générer l'indice de colonne.
        for j in range(1, sukima + 1):
            # Ici, mise à jour de dp[i][j]. On prend le maximum entre deux possibilités :
            #   - Soit ne pas ajouter le livre courant et récupérer la valeur précédente 'dp[i-1][j]'.
            #   - Soit ajouter le livre, si la place restant 'j - books[i-1][1]' est suffisante,
            #     auquel cas on ajoute la valeur 'books[i-1][1]' à la configuration précédente 'dp[i-1][j-books[i-1][1]]'.
            dp[i][j] = max(
                dp[i-1][j],
                # Première possibilité : inclure ce livre si la capacité restante n'est pas négative,
                # sinon retourner zéro pour cette possibilité (conditionnelle via 'if ... else').
                dp[i-1][j-books[i-1][1]] + books[i-1][1] if j - books[i-1][1] >= 0 else 0
            )
    
    # Afficher la somme totale résultante, composée de 'read_t', 'write_t', 'sukima'
    # auquel on soustrait la valeur optimale trouvée dans la table DP 'dp[-1][-1]'.
    print(read_t + write_t + sukima - dp[-1][-1])