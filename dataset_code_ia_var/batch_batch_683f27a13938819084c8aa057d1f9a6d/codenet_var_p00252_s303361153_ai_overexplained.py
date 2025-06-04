# Demande à l'utilisateur d'entrer trois valeurs séparées par espace.
# La fonction input() lit une ligne au clavier sous forme de chaîne (string).
# La méthode split() divise cette chaîne en une liste de sous-chaînes, ici selon les espaces.
# La fonction map(int, ...) applique la fonction int à chacun des éléments de la liste résultante,
# convertissant chaque chaîne en un entier (integer).
# Les trois entiers obtenus sont affectés aux variables b1, b2 et b3 respectivement.
b1, b2, b3 = map(int, input().split())

# Commence une structure conditionnelle "if" pour évaluer les valeurs des variables b1, b2 et b3.
# L'opérateur == vérifie l'égalité entre deux valeurs.
# L'opérateur "and" renvoie True si toutes les conditions combinées sont vraies.
# Ici, on vérifie si b1 vaut 1, b2 vaut 1 et b3 vaut 0 simultanément.
if b1 == 1 and b2 == 1 and b3 == 0:
    # Si la condition précédente est vraie, on exécute l'instruction suivante.
    # print("Open") affiche la chaîne de caractères "Open" à l'écran.
    print("Open")
# "elif" permet de proposer une condition alternative si la première est fausse.
# On vérifie ici un autre ensemble de conditions : b1 vaut 0, b2 vaut 0 et b3 vaut 1.
elif b1 == 0 and b2 == 0 and b3 == 1:
    # Si cette deuxième condition est vraie, affiche "Open".
    print("Open")
# "else" attrape tous les autres cas possibles, c'est-à-dire quand aucune des conditions précédentes n'est remplie.
else:
    # Si ni la première ni la deuxième condition n'est vraie, affiche "Close".
    print("Close")