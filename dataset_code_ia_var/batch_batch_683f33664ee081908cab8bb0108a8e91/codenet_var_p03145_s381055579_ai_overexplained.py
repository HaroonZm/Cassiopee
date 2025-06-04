# Demande à l'utilisateur de saisir une ligne de texte au clavier via la fonction input().
# L'utilisateur doit saisir trois nombres entiers séparés par des espaces.
# La méthode rstrip() enlève les éventuels espaces blancs à la fin de la chaîne saisie.
# La méthode split() découpe la chaîne de caractères en une liste de sous-chaînes, en utilisant par défaut l'espace comme séparateur.
# map(int, ...) applique la fonction int (conversion en entier) à chaque élément de la liste issue du split().
# list(...) transforme l'objet map en une liste contenant les trois entiers.
# L'affectation avec la syntaxe AB,BC,CA = ... permet de stocker les trois entiers dans les variables AB, BC et CA respectivement.
AB, BC, CA = list(map(int, input().rstrip().split()))

# Calculer l'aire du triangle avec AB et BC comme base et hauteur respectivement.
# L'opérateur * effectue la multiplication : AB est multiplié par BC.
# La division /(slash) divise le produit par 2 pour obtenir le résultat.
# int(...) convertit le résultat de la division en entier, tronquant la partie décimale si besoin.
# La méthode format() insère la valeur calculée à l'emplacement "{}" de la chaîne.
# La fonction print() affiche la chaîne finale à l'écran.
print("{}".format(int((AB * BC) / 2)))