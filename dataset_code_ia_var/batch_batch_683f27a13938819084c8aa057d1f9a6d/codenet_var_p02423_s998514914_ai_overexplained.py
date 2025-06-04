# Demande à l'utilisateur d'entrer une valeur entière via la fonction input(), puis convertit la chaîne de caractères obtenue en entier avec int()
x = int(input())  

# Définit une constante nommée BITMASK
# (1 << 32) signifie que l'on décale le nombre 1, 32 fois vers la gauche, ce qui revient à obtenir 2^32
# On soustrait 1, ce qui permet d'obtenir un nombre dont les 32 bits de poids faibles sont tous à 1, c'est-à-dire 0b11111111111111111111111111111111 (ou 4294967295 en décimal)
# Cette valeur sera utilisée comme masque pour limiter les opérations aux 32 bits de poids faibles
BITMASK = (1 << 32) - 1

# Affiche la représentation binaire sur 32 bits du nombre x
# "{:032b}".format(x) convertit la valeur entière x en chaîne binaire de longueur 32, en complétant par des zéros à gauche si besoin
# La commande print() affiche cette chaîne
print("{:032b}".format(x))

# Affiche la représentation binaire sur 32 bits de la négation bit-à-bit (~) de x ANDée avec BITMASK pour ne garder que les 32 bits les moins significatifs
# L'opérateur ~ effectue une négation bit-à-bit, inversant chaque bit
# On fait ensuite ~x & BITMASK pour ne pas avoir de bits perdus ou de dépassement : on ne garde que les 32 derniers bits
# Ensuite, on formate le résultat en chaîne de 32 bits binaires et on affiche
print("{:032b}".format(~x & BITMASK))

# Affiche la représentation binaire sur 32 bits du résultat du décalage à gauche (shift left) de x d'un bit, ET bit-à-bit avec BITMASK pour couper à 32 bits
# L'opérateur << effectue un décalage binaire à gauche, ce qui multiplie par 2
# Comme un entier Python n'a pas de longueur fixe binaire, on applique un & BITMASK pour garder uniquement 32 bits
# On convertit le résultat en une chaîne binaire de 32 caractères avant d'afficher
print("{:032b}".format((x << 1) & BITMASK))

# Affiche la représentation binaire sur 32 bits du résultat du décalage à droite (shift right) de x d'un bit, ET bit-à-bit avec BITMASK pour couper à 32 bits
# L'opérateur >> effectue un décalage binaire à droite, ce qui revient à diviser par 2 de façon entière
# On applique un & BITMASK pour ne garder que les 32 bits de poids faible
# On convertit enfin le résultat en 32 bits avec des zéros à gauche pour l'affichage
print("{:032b}".format((x >> 1) & BITMASK))