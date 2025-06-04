# Demande à l'utilisateur d'entrer deux entiers sur la même ligne, séparés par un espace.
# input() attend la saisie clavier.
# split() sépare la chaîne de caractères sur les espaces, produisant une liste de sous-chaînes.
# map(int, ...) applique la fonction int à chaque élément de la liste retournée par split(),
# convertissant ainsi les sous-chaînes en entiers.
# Les deux valeurs résultantes sont affectées respectivement à h et w.
h, w = map(int, input().split())

# Initialise une variable appelée ans à zéro.
# Cette variable servira à compter le nombre total de '#' présents dans la grille.
ans = 0

# Utilise une boucle for pour itérer h fois (une fois pour chaque ligne de la grille).
# La fonction range(h) produit une séquence de nombres de 0 jusqu'à h-1.
for i in range(h):
    # input() lit une ligne de texte saisie par l'utilisateur, représentant une ligne de la grille.
    # La méthode count('#') compte le nombre de fois où le caractère '#' apparaît dans la chaîne lue.
    # On ajoute ce compte à la variable ans avec l'opérateur d'affectation +=.
    ans += input().count("#")

# À la sortie de la boucle, ans contient le nombre total de '#' trouvés dans toutes les lignes saisies.

# Condition ternaire pour afficher un résultat selon que la condition suivante est vraie ou fausse :
# h + w - 1 == ans vérifie si le nombre total de '#' est exactement égal à h + w - 1.
# Si c'est le cas, la chaîne "Possible" est affichée ; sinon, la chaîne "Impossible" est affichée.
print("Possible" if h + w - 1 == ans else "Impossible")