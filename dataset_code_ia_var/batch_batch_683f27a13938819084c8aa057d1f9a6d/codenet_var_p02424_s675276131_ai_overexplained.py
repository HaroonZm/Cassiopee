# Demander à l'utilisateur de saisir deux nombres entiers séparés par un espace
# La fonction input() lit une ligne de texte entrée par l'utilisateur au clavier
# La méthode split() sépare la chaîne de caractères sur chaque espace et retourne une liste de chaînes
# La fonction map(int, ...) applique la conversion int à chaque élément de la liste (chaînes de caractères) pour transformer chaque chaîne en entier
# L'affectation multiple (x, y =) sert à affecter respectivement les deux premiers éléments retournés à x et y
x, y = map(int, input().split())

# Calcul du "et" bit à bit entre x et y avec l'opérateur &
# Par exemple, si x=5 (000...0101) et y=3 (000...0011), alors x & y = 1 (000...0001)
# La fonction format(valeur, '032b') convertit la valeur en une chaîne binaire sur 32 bits complétée de zéros à gauche (la représentation classique d'un int 32 bits)
# Ici, on stocke dans bin_x la chaîne binaire correspondant à x & y
bin_x = format(x & y, '032b')

# Calcul du "ou" bit à bit entre x et y avec l'opérateur |
# Cela renvoie un nombre dont chaque bit est à 1 si au moins un des bits correspondants de x ou y vaut 1
# Ensuite, on convertit le résultat en une chaîne binaire de 32 caractères, complétée de zéros
bin_x1 = format(x | y, '032b')

# Calcul du "ou exclusif" (XOR) bit à bit entre x et y avec l'opérateur ^
# Chaque bit du résultat vaut 1 si les bits correspondants de x et y sont différents, et 0 s'ils sont identiques
# Le résultat est également converti en chaîne binaire de longueur 32
bin_x2 = format(x ^ y, '032b')

# Affiche la chaîne binaire représentant le résultat du "et" bit à bit
print(bin_x)
# Affiche la chaîne binaire représentant le résultat du "ou" bit à bit
print(bin_x1)
# Affiche la chaîne binaire représentant le résultat du "ou exclusif" (XOR) bit à bit
print(bin_x2)