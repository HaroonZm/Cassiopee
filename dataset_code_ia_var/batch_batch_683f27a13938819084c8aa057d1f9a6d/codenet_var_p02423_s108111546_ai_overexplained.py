# Demande à l'utilisateur de saisir une valeur entière via le clavier.
# La fonction input() récupère une chaîne de caractères saisie par l'utilisateur.
# On la convertit en entier (int) car input retourne toujours une chaîne.
x = int(input())

# Convertit l'entier x en chaîne binaire (sans préfixe '0b').
# format(x, "b") crée une chaîne binaire du nombre x.
# .zfill(10) ajoute des zéros au début pour que la chaîne fasse au moins 10 caractères.
y = format(x, "b").zfill(10)

# Calcule la longueur de la chaîne binaire obtenue.
ly = len(y)

# On veut un format sur 32 bits : on calcule combien de zéros sont encore requis pour obtenir 32 caractères.
# Soustraction ly à 32 permet de savoir combien il manque de caractères.
ly = 32 - ly

# Crée une chaîne de zéros 'pady' de longueur ly pour compléter à gauche jusqu'à 32 caractères au total.
pady = "0" * ly

# Affiche le résultat final, qui est la concénation du paddind de zéros et da la représentation binaire initiale.
# Cela donne la représentation binaire de x sur 32 bits exactement.
print(pady + y)

# Calcule le complément à un sur 32 bits de x.
# 2**32-1 est le nombre maximal possible sur 32 bits (soit 4294967295 en décimal).
# On soustrait x de cette valeur pour obtenir la valeur inversée de x.
rev = 2 ** 32 - 1 - x

# Convertit ce complément à un (rev) en chaîne binaire, sur au moins 10 caractères (avec remplissage de zéros).
z = format(rev, "b").zfill(10)

# Calcule la longueur de la chaîne binaire obtenue.
lz = len(z)

# Calcule le nombre de zéros nécessaires pour compléter à 32 bits.
lz = 32 - lz

# Crée une chaîne de zéros 'padz' de longueur lz pour atteindre 32 bits.
padz = "0" * lz

# Affiche la version 32 bits de la valeur complémentaire.
print(padz + z)

# Calcule la valeur obtenue en multipliant x par 2 (décalage à gauche en binaire).
left = x * 2

# Si le résultat est supérieur ou égal à 2**32 (c'est-à-dire dépasse ce qui peut être représenté sur 32 bits),
# on retire 2**32 (soit on garde que les 32 bits de poids faible).
if left >= 2 ** 32:
    left -= 2 ** 32

# Formate cette valeur (left) en chaîne binaire, sur au moins 10 caractères avec remplissage de zéros.
u = format(left, "b").zfill(10)

# Longueur de la chaîne obtenue de la représentation binaire.
lu = len(u)

# Calcule le nombre de zéros à ajouter en préfixe pour faire 32 bits.
lu = 32 - lu

# Crée un padding de zéros pour compléter à 32 bits.
padu = "0" * lu

# Affiche la chaîne binaire sur 32 bits qui représente x décalé à gauche d'un bit (multiplication par 2).
print(padu + u)

# Calcule la valeur de x divisé par 2, division entière (//), équivalent à un décalage à droite en binaire.
right = x // 2

# Formate cette valeur (right) en chaîne binaire sur au moins 10 caractères avec remplissage.
v = format(right, "b").zfill(10)

# Longueur de la chaîne binaire obtenue.
lv = len(v)

# Nombre de zéros nécessaires pour compléter à 32 bits.
lv = 32 - lv

# Chaîne de padding composée de zéros pour préfixer la chaîne binaire.
padv = "0" * lv

# Affiche la représentation binaire sur 32 bits de x décalé à droite d'un bit (division entière par 2).
print(padv + v)