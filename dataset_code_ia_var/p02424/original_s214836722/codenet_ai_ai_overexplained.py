# Demande à l'utilisateur de saisir deux nombres entiers séparés par un espace
# La fonction input() lit la ligne entrée par l'utilisateur sous forme de chaîne de caractères (string)
# La méthode split() divise cette chaîne de caractères en une liste de sous-chaînes (chaque mot séparé par un espace)
# La fonction map(int, ...) applique la fonction int (pour convertir en entier) à chaque élément de la liste résultante
# Les deux valeurs sont assignées respectivement aux variables a et b
a, b = map(int, input().split())

# Création d'un masque binaire sur 32 bits
# L'opérateur << effectue un décalage binaire à gauche
# 1 << 32 décale le bit '1' de 32 positions vers la gauche, donnant un nombre dont un seul bit est à '1' en 33ème position (suivi de 32 zéros)
# On soustrait 1 pour obtenir 32 bits tous à '1', c'est-à-dire 0b11111111111111111111111111111111 ou 4294967295 en décimal
MASK = (1 << 32) - 1

# Opération ET binaire entre a et b (chaque bit du résultat est à 1 seulement si le bit correspondant de a ET de b est à 1)
# a & b effectue cette opération bit à bit
# La fonction format() permet d'afficher un nombre sous forme binaire
# "{:032b}" indique qu'on veut afficher le nombre sous forme binaire (b) sur 32 caractères (avec des zéros ajoutés à gauche si nécessaire)
# Le résultat de format(a & b, ...) est une chaîne de caractères représentant a & b en binaire sur 32 bits
# print() affiche cette chaîne à l'écran
print("{:032b}".format(a & b))

# Opération OU binaire entre a et b (chaque bit du résultat est à 1 si au moins l'un des bits de a ou de b est à 1)
# a | b effectue cette opération bit à bit
# On affiche le résultat en binaire sur 32 bits avec format(), comme précédemment
print("{:032b}".format(a | b))

# Opération OU exclusif (XOR) binaire entre a et b (chaque bit du résultat est à 1 si les bits correspondants de a et b sont différents)
# a ^ b effectue ce XOR bit à bit
# Affichage du résultat sous forme binaire, toujours sur 32 positions, y compris les zéros non significatifs
print("{:032b}".format(a ^ b))