def actual(n, m, C, B, A):
    # Initialisation d'un compteur à zéro.
    # Ce compteur servira à compter le nombre de cas où la condition ab + C > 0 est vérifiée.
    cnt = 0

    # Boucle sur chaque élément de la liste A.
    # Ici, A est supposé être une liste de listes, où chaque sous-liste représente une "ligne" de valeurs.
    for A_i in A:
        # Calcul du produit scalaire (dot product) entre la ligne courante A_i et la liste B
        # zip(A_i, B) permet d'itérer simultanément sur les éléments de A_i et B,
        # renvoyant à chaque étape un tuple (a, b) composé d'un élément de A_i et un de B.
        # On multiplie chaque paire correspondante a * b.
        # La fonction sum(...), additionne tous ces produits.
        ab = sum([a * b for a, b in zip(A_i, B)])

        # Ajoute le décalage C à la somme calculée auparavant.
        # Si le résultat est strictement supérieur à 0:
        if ab + C > 0:
            # Alors on incrémente le compteur de un.
            cnt += 1

    # Une fois toutes les lignes de A traitées, on retourne le compteur.
    return cnt

# Lecture des entiers N, M et C depuis l'entrée standard via la fonction input().
# input() lit une ligne du terminal. split() sépare la chaîne en fonction des espaces.
# map(int, ...) convertit chaque élément en entier.
N, M, C = map(int, input().split())

# Lecture des valeurs de la liste B dans l'entrée standard.
# La deuxième ligne contient M entiers séparés par des espaces.
# map(int, ...) convertit chaque partie en entier, list(...) les stocke dans une liste.
B = list(map(int, input().split()))

# Initialisation de la liste A, qui contiendra N sous-listes, chacune avec M entiers.
A = []
# Boucle s'exécutant N fois (de 0 à N-1), chaque itération lit une ligne d'entrée supplémentaire.
for _ in range(N):
    # Lecture d'une ligne de M entiers, conversion en liste d'entiers et ajout à la liste A.
    A.append(list(map(int, input().split())))

# Appel de la fonction actual en lui passant les paramètres lus et calculés plus haut.
# Affichage du résultat retourné par la fonction via print() dans la sortie standard.
print(actual(N, M, C, B, A))