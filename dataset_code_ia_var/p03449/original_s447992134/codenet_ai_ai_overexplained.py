# Demander à l'utilisateur un nombre entier depuis la console, cela va lire une ligne, la convertir en int, et l'assigner à la variable N
N = int(input())

# Créer une liste A contenant deux sous-listes, chaque sous-liste étant le résultat de input().split()
# input().split() lit une ligne de texte et la coupe en différents éléments en utilisant les espaces comme séparateurs. Cela fournit des listes de chaînes de caractères
A = [input().split(), input().split()]

# Faire deux boucles imbriquées pour accéder à chaque élément de la matrice/listes A.
# La première boucle parcourt les deux lignes de A (i allant de 0 à 1)
for i in range(2):
    # La seconde boucle parcourt chaque élément de la ligne (j allant de 0 à N-1)
    for j in range(N):
        # On convertit explicitement chaque chaîne de caractères en entier.
        # Ceci est nécessaire pour pouvoir effectuer des opérations mathématiques ensuite
        A[i][j] = int(A[i][j])

# Création de la liste B sous forme de matrice 2 × N, initialisée avec des 0
# Cela se fait avec une liste en compréhension double :
# Pour chaque i de 0 à 1 (donc 2 lignes),
# à chaque fois on crée une sous-liste de N éléments tous mis à 0 avec [0 for j in range(N)]
B = [[0 for j in range(N)] for i in range(2)]

# On initialise B[0][0], c'est-à-dire l'élément tout en haut à gauche, à la valeur du premier élément de la première ligne de A
B[0][0] = A[0][0]

# On initialise B[1][0], c'est-à-dire l'élément tout en bas à gauche,
# à la somme du premier élément de chaque ligne de A (A[0][0] + A[1][0])
B[1][0] = A[0][0] + A[1][0]

# On s'occupe maintenant de remplir la première ligne de B, c'est-à-dire B[0][j]
# On commence à la colonne 1 (c'est-à-dire 2e colonne, car la colonne 0 a déjà été remplie lors de l'initialisation)
for j in range(1, N):
    # À chaque case, on ajoute au contenu précédent de la ligne la valeur correspondante de A
    # C'est donc une somme cumulative le long de la première ligne
    B[0][j] = B[0][j-1] + A[0][j]

# Maintenant on remplit la seconde ligne de B (B[1][j]), on part aussi de la colonne 1
for j in range(1, N):
    # On prend la valeur la plus grande atteinte jusqu'ici soit en restant dans la 2ème ligne (B[1][j-1]),
    # soit en venant de la première ligne au même index de colonne (B[0][j])
    # On ajoute à cela la valeur correspondante de la deuxième ligne de A
    B[1][j] = max(B[1][j-1], B[0][j]) + A[1][j]

# Enfin, on affiche le dernier élément calculé de la matrice B, c'est-à-dire le résultat de la parcours optimal
# La variable i ici correspond à la dernière valeur de la boucle précédente (i=1 à la fin)
# Donc B[1][N-1] est ce qu'on souhaite imprimer. Cependant, pour une plus grande clarté, on peut explicitement écrire : print(B[1][N-1])
print(B[i][N-1])