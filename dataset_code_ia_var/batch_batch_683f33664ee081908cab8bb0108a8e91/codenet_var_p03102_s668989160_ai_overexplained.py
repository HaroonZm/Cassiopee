# Lecture de trois entiers à partir de l'entrée standard (typiquement ce que l'utilisateur tape au clavier)
# La fonction input() lit une ligne de texte en entrée.
# La méthode split() découpe la chaîne de caractères en une liste de sous-chaînes séparées par des espaces.
# La fonction map() applique la fonction int() à chaque élément de la liste pour les convertir en entiers.
# Enfin, list() transforme l'objet map en une vraie liste contenant les trois entiers.
N, M, C = list(map(int, input().split()))

# Lecture d'une liste de M entiers à partir de l'entrée standard.
# On suit la même logique que ci-dessus, en litant la ligne, séparant chaque nombre, convertissant chaque nombre en int, puis plaçant les résultats dans une liste.
B = list(map(int, input().split()))

# Initialisation d'une variable ans à 0.
# Cette variable sera utilisée pour compter le nombre de fois où une certaine condition est remplie dans la boucle principale.
ans = 0

# Boucle sur un entier i allant de 0 jusqu'à N-1 inclus.
# range(N) génère une séquence de N entiers consécutifs, commençant par 0.
for i in range(N):
    # À chaque itération, on lit une liste de M entiers, similaires à la lecture de B ci-dessus.
    # Cette liste A contient les coefficients pour la ligne i.
    A = list(map(int, input().split()))
    
    # Initialisation d'une variable S à 0.
    # S va servir à stocker la valeur du produit scalaire entre le vecteur A et le vecteur B.
    S = 0
    
    # Boucle sur tous les indices de 0 à M-1 inclus pour parcourir les éléments des deux listes A et B.
    for j in range(M):
        # Multiplie l'élément d'indice j de la liste A par celui de la liste B,
        # puis l'ajoute à la somme S.
        S += A[j] * B[j]
    
    # Après la boucle interne, S contient la somme des produits correspondants de A et B (leur produit scalaire).
    # On teste si cette somme S est strictement supérieure à l'opposé de la valeur de C.
    if S > -C:
        # Si la condition est vraie, on incrémente ans de 1 (on ajoute 1 à la variable ans).
        ans += 1

# Enfin, en dehors des boucles, on affiche la valeur finale de ans.
# La fonction print() affiche la valeur à l'écran suivie d'un retour à la ligne.
print(ans)