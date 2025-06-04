# Lecture de deux entiers depuis l'entrée standard
# input() lit une ligne de texte depuis l'utilisateur (par défaut depuis le clavier)
# split() découpe la chaîne selon les espaces par défaut, produisant une liste de chaînes
# map(int, ...) applique la fonction int à chaque élément de la liste, convertissant les chaînes en entiers
# Enfin, on utilise la "unpacking assignment" pour stocker le premier entier dans n et le deuxième dans m
n, m = map(int, input().split())

# Vérification d'une condition spécifique :
# Si n est supérieur ou égal à m, cela signifie qu'il y a autant ou plus de groupes que d'éléments.
# Dans ce cas, la réponse doit être 0
if n >= m:
    # Affiche 0 à l'écran puisque le travail est terminé
    print(0)
    # exit() termine immédiatement le programme, aucune instruction suivante ne sera exécutée
    exit()

# Lecture d'une liste d'entiers depuis l'entrée standard
# Encore input() pour obtenir une ligne, split() pour découper cette ligne en sous-chaînes
# map(int, ...) pour convertir chaque sous-chaîne en entier
# list(...) transforme ceci en une liste d'entiers qui est ensuite stockée dans la variable "a"
a = list(map(int, input().split()))

# On trie la liste "a" par ordre croissant, car cela simplifiera le calcul des différences consécutives
a = sorted(a)

# Création d'une nouvelle liste "b" contenant (m-1) éléments, initialisés à 0
# On va y stocker les différences entre chaque paire consécutive dans la liste triée "a"
b = [0] * (m - 1)

# On parcourt les indices de 0 à (m-2) (car b doit avoir m-1 éléments)
for i in range(m - 1):
    # À chaque itération, on calcule la différence entre deux éléments consécutifs de la liste triée
    # Ces différences sont stockées dans la liste "b" à la position correspondante
    b[i] = a[i + 1] - a[i]

# On trie la liste des différences "b" elle aussi par ordre croissant
b = sorted(b)

# On garde uniquement les (m-n) plus petites différences
# (m-1-(n-1)) == (m-n) : on veut supprimer les plus grandes différences, correspondant à la création de (n-1) "coupures"
# L’expression b[:m-1-(n-1)] garde seulement le début de la liste des différences
b = b[:m - 1 - (n - 1)]

# La somme des différences restantes correspond à la solution minimale recherchée
# On affiche cette somme à l'écran
print(sum(b))