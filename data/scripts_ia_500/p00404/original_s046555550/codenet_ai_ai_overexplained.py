# AOJ 0409
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0409

# Lecture de deux entiers depuis l'entrée standard, séparés par un espace.
# input() retourne une chaîne de caractères saisie par l'utilisateur.
# split() découpe cette chaîne en une liste de sous-chaînes (mots) sur les espaces.
# map(int, ...) convertit chaque sous-chaîne (nombre en string) en entier.
# list() transforme le résultat en liste pour pouvoir désaffecter dans xx, yy.
xx, yy = list(map(int, input().split()))

# Initialisation de la liste 'fib' contenant les deux premiers termes de la suite de Fibonacci.
# Cette suite commence généralement par 1, 1 pour ce problème.
fib = [1, 1]

# Variable 'a' pour stocker chaque nouveau terme calculé de la suite de Fibonacci.
a = 0

# Boucle while qui continue tant que le dernier terme calculé est inférieur à 10 millions.
# Cette limite est fixée pour éviter de générer une liste trop longue.
while a < 10000000:
    # Calcul du terme Fibonacci suivant en sommant les deux derniers termes de 'fib'.
    a = fib[-1] + fib[-2]
    # Ajout du nouveau terme à la fin de la liste 'fib'.
    fib += [a]

# Initialisation de la liste 'area' qui contiendra les données de chaque "zone" ou étage.
# Chaque élément est une liste [x, y, a] où (x, y) est un point de référence
# et 'a' est la taille (longueur ou largeur) associée à cet étage.
# On commence par un étage initial positionné à (0, 0) avec taille 1.
area = [[0, 0, 1]]

# Variables pour suivre la position actuelle (x,y) du dernier étage ajouté.
x, y = 0, 0

# Variables pour stocker les deux dernières tailles de Fibonacci (f1 et f2),
# initialisées avec les deux premiers termes connus.
f1 = 0
f2 = 1

# Boucle itérant sur les indices des termes Fibonacci issus de la liste 'fib',
# en commençant à 1 car le premier étage est déjà ajouté.
for n in range(1, len(fib)):
    # On récupère la taille actuelle de l'étage dans la variable 'a'.
    a = fib[n]
    # Selon le reste de la division de n par 4, on oriente différemment la position (x,y)
    # du nouvel étage à ajouter:
    if n % 4 == 1:
        # Si n modulo 4 == 1, on déplace x vers la droite de f2
        # et y vers le haut de f1, la taille est a.
        area += [[x + f2, y + f1, a]]
    elif n % 4 == 2:
        # Si n modulo 4 == 2, on déplace x vers la gauche de f1,
        # y vers le haut de a, taille a.
        area += [[x - f1, y + a, a]]
    elif n % 4 == 3:
        # Si n modulo 4 == 3, on déplace x vers la gauche de a,
        # y reste inchangé ; taille a.
        area += [[x - a, y, a]]
    elif n % 4 == 0:
        # Si n modulo 4 == 0, x reste inchangé,
        # y descend de f2, taille a.
        area += [[x, y - f2, a]]

    # Mise à jour des variables f1 et f2 pour préparer l'itération suivante.
    # f1 devient l'ancien f2, f2 devient le nouveau terme a.
    f1 = f2
    f2 = a

    # Mise à jour des coordonnées x, y à la position du dernier étage ajouté.
    # area[-1] récupère le dernier élément de la liste 'area',
    # [0:2] récupère uniquement la partie (x,y).
    x, y = area[-1][0:2]

# Parcours de chaque étage (zone) stocké dans 'area' avec leur indice n.
for n, floor in enumerate(area):
    # Décomposition des coordonnées et taille de l'étage en x, y, a.
    x, y, a = floor
    # Vérification si le point (xx, yy), fourni en entrée, se situe dans la zone de l'étage.
    # La condition vérifie que xx est dans l'intervalle [x, x+a)
    # et yy dans l'intervalle (y - a, y].
    if x <= xx < x + a and y - a < yy <= y:
        # En cas de position dans la zone, on imprime (n % 3 + 1).
        # Ce calcul donne un nombre dans {1, 2, 3} selon la position modulo 3,
        # correspondant probablement à un type ou un label d'étage.
        print(n % 3 + 1)
        # On arrête la boucle dès qu'on a trouvé la zone correcte.
        break