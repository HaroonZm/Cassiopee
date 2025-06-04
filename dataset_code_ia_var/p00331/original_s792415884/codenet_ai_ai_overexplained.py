# Demande à l'utilisateur de saisir deux valeurs séparées par un espace,
# puis récupère cette ligne de texte grâce à la fonction input().
# Par exemple, si l'utilisateur entre "3 5", la variable input() contiendra la chaîne "3 5".
user_input = input()

# Utilise la méthode split() sur la chaîne entrée par l'utilisateur pour découper cette chaîne en une liste de sous-chaînes,
# chaque fois qu'un espace est trouvé. Ainsi, "3 5" devient ["3", "5"].
split_input = user_input.split()

# Applique la fonction map() pour transformer chaque sous-chaîne en entier (int),
# en itérant sur chaque élément de la liste résultat de split().
# L'appel map(int, split_input) retourne un itérable contenant [3, 5].
mapped_integers = map(int, split_input)

# Utilise l'affectation multiple pour extraire les deux valeurs de l'itérable 'mapped_integers'
# et les assigner respectivement aux variables h et r.
h, r = mapped_integers

# Condition 1 :
# Utilise l'instruction if pour exécuter un bloc de code si une certaine condition est vraie.
# Vérifie si h est supérieur ou égal à 0 (h >= 0).
# Si la condition est vraie, on entre dans le bloc et exécute l'instruction print(1).
if h >= 0:
    # Affiche la valeur 1 à l'utilisateur en utilisant print().
    print(1)

# Condition 2 :
# L'instruction elif (else if) permet de tester une seconde condition si la première est fausse.
# Ici, on teste si la somme de h et r est exactement égale à 0.
elif h + r == 0:
    # Affiche la valeur 0 à l'utilisateur si la condition précédente est vraie.
    print(0)

# Condition 3 :
# L'instruction else permet de gérer tous les cas où aucune des conditions précédentes n'est satisfaite.
# Aucune condition n'est placée à côté de else : il s'exécute par défaut si le if et le elif sont tous faux.
else:
    # Affiche la valeur -1 à l'utilisateur si aucune des conditions précédentes n'a été remplie.
    print(-1)