# Demande à l'utilisateur d'entrer une valeur au clavier.
# La fonction input() récupère la saisie de l'utilisateur sous forme de chaîne (string).
# La fonction int() convertit cette chaîne en un entier (integer).
n = int(input())

# Initialise une liste vide appelée 's' pour stocker les valeurs lues ensuite.
s = []

# Utilise une boucle for pour répéter les instructions qui suivent exactement n fois.
# La fonction range(n) génère une séquence de valeurs de 0 jusqu'à n-1 inclus.
for i in range(n):
    # Pour chaque itération, lit une ligne de l'entrée standard (le clavier).
    # La fonction input() renvoie une chaîne de caractères saisie par l'utilisateur.
    # La méthode split() sépare cette chaîne en sous-chaînes selon les espaces.
    # La fonction map(int, ...) applique la conversion int() à chaque sous-chaîne, transformant chacune en entier.
    # x et y recevront successivement ces valeurs sous forme d'entiers.
    x, y = map(int, input().split())
    # Ajoute à la liste 's' un tuple constitué des deux entiers lus (x, y).
    s.append((x, y))

# Trie la liste 's' sur place (modifie la liste sans en créer une nouvelle).
# Le tri se fait par défaut dans l'ordre croissant, d'abord sur le premier élément de chaque tuple,
# en cas d'égalité, sur le second.
s.sort()

# Parcourt à nouveau la liste 's', cette fois pour afficher les éléments.
for i in range(n):
    # Récupère le couple d'entiers stocké à l'indice i de la liste 's'.
    # s[i][0] désigne le premier élément du tuple (x) et s[i][1] le second (y).
    # La fonction print() affiche ces deux nombres sur la même ligne, séparés par un espace.
    print(s[i][0], s[i][1])