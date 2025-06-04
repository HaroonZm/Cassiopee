# Demande à l'utilisateur de saisir deux entiers séparés par un espace
# La fonction input() renvoie la saisie de l'utilisateur sous forme de chaîne de caractères (str)
# split() divise la chaîne selon l'espace et renvoie une liste de sous-chaînes
# map(int, ...) applique la fonction int à chaque sous-chaîne, transformant chaque élément de la liste en entier
a, b = map(int, input().split())

# On veut afficher le résultat de la division entière de a par b sans utiliser le signe de division directement,
# et avec le bon signe même en cas de négatifs, imitant le comportement de la division entière de Python

# Premièrement, on calcule le signe du résultat.
# Si le produit a*b est négatif (< 0), alors les signes de a et b sont opposés,
# donc le résultat de la division doit être négatif, on utilise -1 comme multiplicateur de signe.
# Sinon (a et b ont le même signe), le résultat est positif, donc multiplicateur = 1.
if a * b < 0:
    signe = -1  # Résultat négatif si a et b ont des signes différents
else:
    signe = 1   # Résultat positif si a et b ont le même signe

# Ensuite, on calcule la priorité de la division entière.
# Pour ne pas se soucier des signes, on prend la valeur absolue de a et b
# abs(a) retourne la valeur absolue de a (toujours positive ou nulle)
# de même, abs(b) retourne la valeur absolue de b
# L'opérateur // effectue la division entière, c'est-à-dire qu'il donne le quotient sans la partie décimale
division_entiere = abs(a) // abs(b)

# On applique ensuite le signe précédemment calculé au résultat de la division entière
resultat = signe * division_entiere

# Enfin, on affiche le résultat à l'écran ; print() affiche son argument
print(resultat)