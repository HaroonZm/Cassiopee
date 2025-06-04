# Demande à l'utilisateur de saisir une ligne de texte (par exemple '1 0 1'),
# puis récupère cette saisie sous forme de chaîne de caractères
user_input = raw_input()

# Utilise la fonction split() pour découper la chaîne de caractères en une liste de sous-chaînes,
# chaque sous-chaîne correspondant à une valeur séparée par un espace
input_list = user_input.split()

# Utilise la fonction map() pour appliquer la fonction int (qui convertit une chaîne en entier)
# à chaque élément de la liste input_list. Cela retourne un itérable contenant les valeurs converties.
# Déstructure l'itérable ainsi obtenu dans trois variables : b1, b2, b3.
b1, b2, b3 = map(int, input_list)

# Premiers tests logiques :
# La première condition vérifie si b1 est vrai (différent de 0), b2 est vrai, et b3 est faux (égal à 0)
# Ceci est possible grâce à Python où 0 est faux, et tout nombre différent de 0 est vrai.
# La deuxième condition vérifie si b1 est faux, b2 est faux et b3 est vrai.
# L'opérateur 'not' inverse la valeur de vérité de la variable (not b3 est vrai si b3 est faux, etc).
# Les deux conditions sont reliées par 'or', ce qui veut dire que si l'une OU l'autre est vraie,
# l'ensemble de l'expression devient vraie.
# On utilise ensuite une expression conditionnelle (ternaire en Python) pour afficher soit "Open"
# si la condition précédente est vraie, soit "Close" si elle est fausse.

if (b1 and b2 and (not b3)) or ((not b1) and (not b2) and b3):
    # Si la condition est vraie, affiche "Open"
    print "Open"
else:
    # Sinon, affiche "Close"
    print "Close"