# Demande à l'utilisateur de saisir une valeur via le clavier (input renvoie une chaîne de caractères)
# Utilise la fonction int() pour convertir cette chaîne de caractères en un entier
n = int(input())

# Demande à l'utilisateur de saisir plusieurs valeurs séparées par des espaces et récupère la ligne complète comme une chaîne de caractères
# La fonction input() retourne toujours une chaîne de caractères
# La méthode split() permet de scinder cette chaîne en une liste de sous-chaînes, chaque sous-chaîne représentant un nombre saisi séparé par un espace
# La fonction map() applique la fonction int à chaque élément de la liste pour les convertir de texte (str) à entier (int)
# Enfin, la fonction list() transforme l'objet map en une liste réelle d'entiers
a = list(map(int, input().split()))

# Utilise la fonction max() pour trouver la valeur maximale présente dans la liste a
# Utilise également la fonction min() pour trouver la valeur minimale de cette même liste
# Soustrait la valeur minimale de la valeur maximale afin de calculer l'écart maximal entre deux éléments de la liste
# Affiche ce résultat à l'écran grâce à la fonction print()
print(max(a) - min(a))