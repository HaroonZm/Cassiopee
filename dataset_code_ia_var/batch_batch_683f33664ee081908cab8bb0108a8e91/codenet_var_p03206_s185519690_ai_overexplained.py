# Demander à l'utilisateur de saisir une valeur via le clavier
# La fonction input() affiche une invite vide, attend que l'utilisateur entre une valeur puis appuie sur Entrée
# input() retourne une chaîne de caractères (str), donc nous devons la convertir en entier pour comparaison
d = int(input())  # Conversion explicite de la chaîne en int, pour permettre la comparaison dans les conditions suivantes

# Vérification si la valeur saisie est exactement égale à 25
if d == 25:
    # Si d vaut 25, on affiche "Christmas"
    print("Christmas")
# Vérification alternative si la valeur saisie est exactement égale à 24
elif d == 24:
    # Si d vaut 24, on affiche "Christmas Eve"
    print("Christmas Eve")
# Vérification alternative si la valeur saisie est exactement égale à 23
elif d == 23:
    # Si d vaut 23, on affiche "Christmas Eve Eve"
    print("Christmas Eve Eve")
# Si aucune des conditions précédentes n'est satisfaite
else:
    # On suppose que dans ce cas la valeur saisie est 22 (ou toute autre valeur différente de 23, 24, 25, selon logique du programme)
    # On affiche "Christmas Eve Eve Eve"
    print("Christmas Eve Eve Eve")