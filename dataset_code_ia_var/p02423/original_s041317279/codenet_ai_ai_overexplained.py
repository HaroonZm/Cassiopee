# Demander à l'utilisateur de saisir une valeur à partir du clavier.
# La valeur saisie est une chaîne de caractères, donc il faut la convertir en entier.
x = int(input())

# Afficher la représentation binaire de x sur 32 bits.
# La fonction 'format' permet de formater un nombre en chaîne de caractères selon un format donné.
# Ici, "032b" signifie :
# - '0' : compléter avec des zéros à gauche si besoin
# - '32' : la largeur totale de la chaîne sera de 32 caractères
# - 'b' : convertir en binaire (0 et 1)
print(format(x, "032b"))

# Calculer le complément à 1 de x, c'est-à-dire inverser tous ses bits.
# L'opérateur '~' applique le NOT bit à bit (inversion des 0 et des 1)
# Cependant, en Python, les entiers peuvent être de taille arbitraire et '~x' donne des représentations infinies.
# Pour obtenir uniquement les 32 derniers bits, on effectue un AND bit à bit (&) avec 0b11111111111111111111111111111111 (suite de 32 bits à 1).
# Ainsi, seuls les 32 bits de poids faible sont conservés.
# Ensuite, on affiche cette valeur en binaire sur 32 bits, comme précédemment.
print(format(~x & 0b11111111111111111111111111111111, "032b"))

# Décaler les bits de x vers la gauche d'un cran en utilisant l'opérateur '<<'
# Cela ajoute un 0 à droite et déplace chaque bit d'une position vers la gauche
# En Python, cela peut donner un nombre de plus de 32 bits.
# On convertit donc ce nombre en binaire et on ne garde que les 32 derniers caractères avec [-32:]
# Cela simule un décalage dans un registre de 32 bits.
print(format(x << 1, "032b")[-32:])

# Décaler les bits de x vers la droite d'un cran avec l'opérateur '>>'
# Cela supprime le bit de poids faible (à droite) et ajoute un 0 à gauche pour les entiers positifs.
# Ensuite on affiche la représentation binaire du résultat, sans tronquer à 32 bits.
print(format(x >> 1, "032b"))