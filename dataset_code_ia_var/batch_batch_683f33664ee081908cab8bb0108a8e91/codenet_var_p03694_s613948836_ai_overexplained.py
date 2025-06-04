# Demander à l'utilisateur de saisir une valeur via le clavier
# La fonction input() permet de récupérer ce que l'utilisateur tape sous forme de texte (chaîne de caractères)
n = int(input())  # On convertit ce texte en un entier grâce à int(), et on l'affecte à la variable n

# Demander à l'utilisateur de saisir plusieurs valeurs séparées par des espaces
# input() retourne la saisie sous forme de chaîne de caractères
# split() découpe cette chaîne en une liste de sous-chaînes, en utilisant un espace comme séparateur par défaut
# map(int, ...) applique la fonction int() à chaque sous-chaîne obtenue, convertissant chacune en entier
# list(...) transforme l'objet résultat de map en une véritable liste Python
a = list(map(int, input().split()))  # On stocke la liste finale dans la variable a

# Trier la liste a dans l'ordre croissant (du plus petit au plus grand)
# La méthode sort() modifie la liste a en place, c'est-à-dire qu'elle ré-arrange les éléments déjà présents
a.sort()

# Calculer la différence entre le dernier et le premier élément de la liste triée
# a[-1] fait référence au dernier élément de la liste a. En Python, les indices négatifs partent de la fin
# a[0] est le premier élément de la liste
# On fait la soustraction pour connaître l'écart entre la plus grande et la plus petite valeur de la liste
result = a[-1] - a[0]

# Afficher le résultat calculé à l'écran
# print() envoie la valeur de result vers la sortie standard (généralement l'écran)
print(result)