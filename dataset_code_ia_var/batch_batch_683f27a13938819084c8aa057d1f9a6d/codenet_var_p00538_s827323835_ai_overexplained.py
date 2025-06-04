import sys  # Le module 'sys' fournit des fonctions et des variables utilisées pour manipuler différentes parties de l'environnement d'exécution du système

# Définir la limite maximale de récursion autorisée dans ce programme.
# Par défaut, Python fixe une limite faible (~1000), ce qui pourrait provoquer une erreur de récursion pour de gros 'n'. On l'augmente ici.
sys.setrecursionlimit(10000)

# Lire un entier depuis l'entrée standard (l'utilisateur ou un fichier en entrée).
# La fonction 'input()' lit une ligne sous forme de chaîne de caractères.
# 'int()' convertit cette chaîne en entier.
n = int(input())

# Créer une liste A qui contiendra des entiers lus ligne par ligne depuis l'entrée utilisateur.
# La liste de compréhension permet de répéter une opération (ici 'int(input())') n fois, pour remplir A de n entiers.
A = [int(input()) for i in range(n)]

# On multiplie la liste A par 3 pour la répéter 3 fois à la suite.
# Ceci est souvent fait avec des tableaux circulaires pour gérer des cas où l'on veut considérer les éléments de la fin comme voisins du début.
A = A * 3

# Déclarer une table de programmation dynamique (DP) qui aidera à mémoïser les résultats de calculs récursifs.
# C'est une liste de listes, initialisée avec -1 pour signaler que la case n'a pas encore été calculée.
# Il y a n*2 lignes et n*2 colonnes puisque les indices 'i' et 'j' vont de 0 à n*2 - 1.
dp = [[-1 for i in range(n * 2)] for j in range(n * 2)]

# Définir une fonction de recherche récursive en profondeur (DFS) qui prend en argument deux indices i et j.
# Cette fonction sert à calculer la valeur optimale entre les indices i et j pour un certain jeu.
def dfs(i, j):
    # Vérifier si le sous-problème pour les indices (i, j) a déjà été calculé.
    # Si dp[i][j] != -1, cela veut dire que le calcul a déjà été fait et on peut juste le réutiliser sans refaire le travail.
    if dp[i][j] != -1:
        pass  # On ne fait rien ici, car la valeur sera renvoyée à la fin.
    # Cas de base : si la longueur du segment considéré est égale à n (soit j - i == n - 1), alors il n'y a plus de coup à jouer.
    # On initialise donc la valeur avec 0, signifiant que plus aucun point ne peut être marqué à partir de là.
    elif (j - i == n - 1):
        dp[i][j] = 0
    # Si le nombre d'éléments restants entre i et j (inclus) est pair ((j - i) % 2 == 0), alors c'est au tour de l'adversaire (joueur fictif).
    # On simule que l'adversaire retire judicieusement une extrémité, pour minimiser notre résultat final.
    elif (j - i) % 2 == 0:
        # On compare la valeur de l'élément juste avant i avec celle juste après j.
        # L'adversaire enlève le plus grand pour nous gêner le plus possible.
        # 'A[i - 1]' est l'élément avant i ; 'A[j + 1]' est l'élément juste après j.
        if A[i - 1] > A[j + 1]:
            # L'adversaire enlève à gauche : on appelle dfs en décalant i d'une case à gauche.
            dp[i][j] = dfs(i - 1, j)
        else:
            # L'adversaire enlève à droite : on appelle dfs en décalant j d'une case à droite.
            dp[i][j] = dfs(i, j + 1)
    # Sinon, c'est à nous de jouer (nombre impair d'éléments restants).
    # On choisit la meilleure option entre prendre à gauche ou à droite, et on ajoute à notre score la valeur de l'élément pris.
    else:
        # Option 1 : on prend à gauche (i-1), donc on appelle dfs sur (i-1, j) et on ajoute la valeur d'A[i-1].
        # Option 2 : on prend à droite (j+1), donc on appelle dfs sur (i, j+1) et on ajoute la valeur d'A[j+1].
        # On choisit la solution qui donne le maximum pour nous.
        dp[i][j] = max(dfs(i - 1, j) + A[i - 1], dfs(i, j + 1) + A[j + 1])
    # On retourne la valeur calculée ou récupérée dans dp[i][j].
    return dp[i][j]

# Initialiser la réponse (le score maximal possible) à 0.
ans = 0

# Boucle sur tous les points de départ possibles (choix du premier élément à prendre) dans la séquence initiale de longueur n.
# Puisque A a été triplée, on peut commencer à n'importe quel indice i de 0 à n-1.
for i in range(n):
    # On considère la situation où l'on prend l'élément A[i] comme premier choix,
    # puis on calcule de façon optimale le reste avec dfs(i, i).
    # L'appel dfs(i, i) considère les indices entre i et i : il reste donc tous les éléments à choisir après A[i].
    # On ajoute la valeur de A[i] à la valeur retournée, car on prend immédiatement cet élément.
    ans = max(ans, dfs(i, i) + A[i])

# Afficher le score maximal possible que le premier joueur peut obtenir en optimisant ses choix.
print(ans)