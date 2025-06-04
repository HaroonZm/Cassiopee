# Demande à l'utilisateur de saisir deux entiers séparés par un espace sur une seule ligne
# La fonction input() attend une entrée de l'utilisateur sous forme de chaîne de caractères (par exemple : "7 10")
# La méthode split() divise la chaîne saisie là où il y a des espaces, cela renvoie une liste de chaînes
# map(int, ...) applique la conversion en entier à chaque valeur de la liste obtenue avec split()
# Le résultat du map est converti en deux variables a et b à l'aide d'un unpacking
a, b = map(int, input().split())

# Calcul du "ET" bit à bit (AND opérateur &)
# a & b fait un AND binaire entre chaque bit de a et chaque bit de b
# 0b11111111111111111111111111111111 est un littéral binaire représentant 32 uns (équivalent à (2**32)-1)
# "& 0b11111111111111111111111111111111" permet de ne conserver que les 32 bits de poids faible (droite) du résultat
c = a & b & 0b11111111111111111111111111111111

# Calcul du "OU" bit à bit (OR opérateur |)
# a | b effectue un OR binaire entre chaque bit correspondant de a et b
# Le "AND" final avec 0b111...111 permet ici aussi de conserver seulement les 32 bits de poids faible
d = (a | b) & 0b11111111111111111111111111111111

# Calcul du "XOR" bit à bit (OU exclusif, opérateur ^)
# a ^ b met à 1 chaque bit là où a et b sont différents
# "& 0b111...111" conserve les 32 bits de droite comme auparavant
e = (a ^ b) & 0b11111111111111111111111111111111

# Affiche la variable c dans sa représentation binaire sur 32 bits, complétée avec des zéros à gauche si besoin
# format(c, '032b') convertit c en une chaîne binaire de longueur exactement 32, avec des zéros devant si nécessaire
print(format(c, '032b'))

# Affiche la variable d dans sa représentation binaire sur 32 bits, toujours avec des zéros à gauche
print(format(d, '032b'))

# Affiche la variable e dans sa représentation binaire sur 32 bits de la même façon
print(format(e, '032b'))