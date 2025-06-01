# On commence par lire deux entiers depuis l'entrée standard
# Input attendue : deux entiers séparés par un espace, ex: "5 3"
# map(int, input().split()) applique la fonction int à chaque élément résultant du split
n, k = map(int, input().split())

# On crée une liste 'rules' qui contiendra k éléments
# Chaque élément est une map d'entiers obtenue de la même façon que pour n,k, donc k lignes sont lues ici
# Chaque ligne contient deux entiers séparés par un espace
rules = [map(int, input().split()) for _ in range(k)]

# On initialise une liste 'ans' de taille n+1 (indices de 0 à n)
# Chaque élément de ans (sauf le 0) est une liste de 7 éléments [0,1,1,1,1,1,1]
# Indice 0 dans chaque liste est toujours 0, les autres à 1 à l'initialisation
# Cela peut servir à indexer directement par 1-based indices (1 à 6) en ignorant l'indice 0
ans = [[0,1,1,1,1,1,1] for _ in range(n+1)]

# On définit un dictionnaire sous forme de liste pour correspondance d'état ou configuration
# L'indice 0 correspond à zéro, probablement inutilisé
# Indices 1,2,3 ont chacun une liste de 7 éléments (index 0 à 6)
# Ces listes ont des 0 ou des 1 qui probablement indiquent des règles ou états possibles pour chaque position
dic = [0, [0,1,0,0,1,0,0], [0,0,1,0,0,1,0], [0,0,0,1,0,0,1]]

# Parcourir chaque règle dans 'rules', qui sont des paires [d, p]
# On affecte à ans[d] une copie de la liste correspondante dans dic[p]
# list(dic[p]) force la création d'une nouvelle liste pour éviter des références partagées
for [d, p] in rules:
    ans[d] = list(dic[p])

# Modification explicite de certains éléments à l'index 1 de ans
# Indices 4,5,6 de la sous-liste ans[1] sont mis à 0
ans[1][4] = 0
ans[1][5] = 0
ans[1][6] = 0

# On boucle sur d de 2 à n inclus (intervalle [2, n])
for d in range(2, n+1):
    # Pour chaque d, on calcule la valeur ans[d][1] comme le produit entre ans[d][1] valeur actuelle
    # multipliée par la somme des valeurs ans[d-1][2], ans[d-1][3], ans[d-1][5], ans[d-1][6]
    # Semblable pour ans[d][2] et ans[d][3] mais combinaisons différentes
    # Pour ans[d][4], ans[d][5], ans[d][6], multiplication directe par un seul élément de ans[d-1]
    ans[d][1] = ans[d][1] * (ans[d-1][2] + ans[d-1][3] + ans[d-1][5] + ans[d-1][6])
    ans[d][2] = ans[d][2] * (ans[d-1][1] + ans[d-1][3] + ans[d-1][4] + ans[d-1][6])
    ans[d][3] = ans[d][3] * (ans[d-1][1] + ans[d-1][2] + ans[d-1][4] + ans[d-1][5])
    ans[d][4] = ans[d][4] *  ans[d-1][1]
    ans[d][5] = ans[d][5] *  ans[d-1][2]
    ans[d][6] = ans[d][6] *  ans[d-1][3]

# Finalement, on calcule la somme des éléments de ans[n] (c'est une liste de 7 entiers)
# On prend cette somme modulo 10000 avant de l'afficher
# Cette opération modulo est fréquemment utilisée pour éviter d'avoir un nombre trop grand à gérer
print(sum(ans[n]) % 10000)