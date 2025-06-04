# Lecture du nombre entier 't' à partir de l'entrée standard via input().
# La fonction input() lit une ligne de texte depuis l'entrée standard (souvent le clavier).
# La fonction int() convertit cette chaîne de caractères en un entier (int).
t = int(input())

# Initialisation d'une liste vide nommée 'arr' qui va contenir les valeurs saisies par l'utilisateur.
# Cette liste va finalement stocker 't' listes de trois éléments entiers chacune.
arr = []

# Boucle for allant de 0 à t - 1 (soit t itérations au total).
# La variable 'x' va prendre successivement toutes les valeurs entières comprises entre 0 (inclus) et t (exclu).
for x in range(t):
    # input() lit une ligne depuis l'entrée standard.
    # split() divise cette ligne de texte en une liste de chaînes séparées selon les espaces (par défaut).
    # map(int, ...) applique la fonction int() à chaque élément de la liste produite par split(), transformant chaque chaîne de caractères en entier.
    # list(...) convertit l'objet map en une vraie liste Python contenant trois entiers.
    a = list(map(int, input().split()))
    # Ajout de la liste de trois entiers 'a' à la liste 'arr' à la fin (méthode append()).
    arr.append(a)

# Création de la table de programmation dynamique 'dp'.
# 'dp' est une liste de listes : chaque dp[y] contiendra une liste de trois entiers.
# dp est initialisée pour avoir t sous-listes (autant que le nombre d'entrées 't').
# Chaque sous-liste contient trois zéros au départ (car range(3) génère trois éléments : 0, 1, 2).
dp = [[0 for x in range(3)] for y in range(t)]

# Initialisation de la première ligne de la table 'dp' avec les valeurs du premier jour (ou élément).
# Cela remplit chaque colonne de la première ligne de 'dp' avec la valeur correspondante dans 'arr'.
# dp[0][0] reçoit la première valeur du premier sous-tableau dans 'arr'.
dp[0][0] = arr[0][0]
# dp[0][1] reçoit la deuxième valeur du même sous-tableau.
dp[0][1] = arr[0][1]
# dp[0][2] reçoit la troisième valeur du même sous-tableau.
dp[0][2] = arr[0][2]

# Boucle sur chaque jour/élément du deuxième (index 1) jusqu'au dernier (index t-1).
for x in range(1, t):
    # Pour chaque choix du jour courant (trois colonnes : 0, 1, 2), on maximise la somme possible
    # en choisissant la meilleure option parmi les deux autres choix du jour précédent (cela évite de répéter le même choix consécutivement).
    
    # Pour la colonne 0 : on ajoute la valeur courante arr[x][0] et le maximum des deux autres colonnes du jour précédent.
    dp[x][0] = arr[x][0] + max(dp[x - 1][1], dp[x - 1][2])
    # Pour la colonne 1 : on ajoute la valeur courante arr[x][1] et le maximum des colonnes 0 et 2 du jour précédent.
    dp[x][1] = arr[x][1] + max(dp[x - 1][0], dp[x - 1][2])
    # Pour la colonne 2 : on ajoute la valeur courante arr[x][2] et le maximum des colonnes 0 et 1 du jour précédent.
    dp[x][2] = arr[x][2] + max(dp[x - 1][0], dp[x - 1][1])

# À la fin, on veut connaître la valeur maximale atteignable le dernier jour (dernier sous-tableau de dp).
# On prend donc le maximum des trois possibilités du dernier jour ('dp[t-1]' est la dernière sous-liste).
print(max(dp[t - 1]))