# Demande à l'utilisateur de saisir une valeur et la stocke dans la variable n
# input() retourne une chaîne de caractères (str), même si l'utilisateur saisit un nombre
n = input()

# Demande à l'utilisateur de saisir deux entiers séparés par un espace sur la même ligne, sous Python 2.x
# raw_input() lit la ligne saisie, .split() la découpe en une liste de deux strings
# map(int, ...) convertit chaque élément de la liste en entier
# L'affectation multiple a, b = ... stocke le premier entier dans a, le second dans b
a, b = map(int, raw_input().split())

# Demande à l'utilisateur de saisir une valeur (nombre ou chaîne) et la stocke dans ca
ca = input()

# Calcule le ratio de ca divisé par a, stocke le résultat dans la variable max
# En Python 2, l'opérateur / effectue une division entière si les deux opérandes sont des entiers,
# donc si ca et a sont entiers, il faut s'assurer qu'on souhaite bien ce comportement.
max = ca / a

# Construit une liste cb contenant n éléments, chacun issu d'un appel à input()
# [input() for i in range(n)] construit une liste en parcourant chaque valeur de i dans range(n)
# range(n) génère une séquence de nombres de 0 à n-1
# Pour chaque i, input() est appelé pour demander à l'utilisateur une entrée et la stocke dans cb
cb = [input() for i in range(n)]

# Initialise la variable sum_b avec la valeur de a, qui servira à accumuler les b à chaque itération
sum_b = a
# Initialise la variable sum_cb avec la valeur de ca, qui servira à accumuler les t à chaque itération
sum_cb = ca

# Trie la liste cb, puis l'inverse (pour décroissant), puis itère sur chaque élément t de cette liste
for t in reversed(sorted(cb)):
    # Ajoute la valeur de b à sum_b (incrémente la somme totale avec b à chaque nouvel élément)
    sum_b += b
    # Ajoute la valeur courante t à sum_cb (incrémente la somme totale avec t correspondant)
    sum_cb += t
    # Vérifie si le ratio max est inférieur ou égal à sum_cb divisé par sum_b
    if max <= sum_cb / sum_b:
        # Si c'est le cas, met à jour max avec le nouveau ratio sum_cb / sum_b
        max = sum_cb / sum_b
    else:
        # Sinon (si le ratio n'a pas augmenté), interrompt la boucle avec break
        break

# Affiche la valeur finale de max pour l'utilisateur
print max