# Demande à l'utilisateur de saisir un nombre entier et convertit l'entrée en un entier
n = int(input())  # La fonction input() lit une chaîne au clavier, int() convertit cette chaîne en entier

# Calcule la valeur maximale d'un entier non signé sur 32 bits
# 1 << 32 effectue un décalage binaire à gauche du nombre 1 par 32 positions, ce qui donne 2^32
# En soustrayant 1, on obtient un nombre dont les 32 bits sont à 1 : 0b11111111111111111111111111111111 (soit 4294967295)
m = (1 << 32) - 1

# Affiche la représentation binaire sur 32 bits de n, avec des zéros non significatifs si nécessaire
# {:032b} est un format de chaîne : 0 signifie de compléter avec des zéros, 32 pour la largeur, b pour binaire
print("{:032b}".format(n))

# Calcule le complément binaire de n avec l'opérateur ~ (NON binaire), puis fait un "et" binaire(&) avec m 
# Cela permet de ne garder que les 32 bits de poids faible (efface les bits de signe et de débordement pour la visualisation sur 32 bits)
print("{:032b}".format(~n & m))

# Effectue un décalage binaire à gauche de n, c'est-à-dire multiplie n par 2^1 (n * 2)
# Ensuite, applique un "et" binaire(&) avec m pour ne conserver que les 32 bits de poids faible, important pour une représentation stricte sur 32 bits
print("{:032b}".format((n << 1) & m))

# Effectue un décalage binaire à droite de n, c'est-à-dire divise n par 2^1 (n // 2)
# On affiche la représentation binaire sur 32 bits
print("{:032b}".format(n >> 1))