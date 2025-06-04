# Demande à l'utilisateur d'entrer une valeur entière et l'affecte à la variable N.
# La fonction input() lit une ligne depuis l'entrée standard sous forme de chaîne de caractères (string).
# int() convertit cette chaîne de caractères représentant un nombre en un entier (integer).
N = int(input())

# Demande à l'utilisateur d'entrer une ligne de nombres séparés par des espaces.
# input() lit la ligne sous forme de string.
# split() divise la chaîne en une liste de sous-chaînes, chacune correspondant à un nombre, en utilisant l'espace comme séparateur par défaut.
# map(int, ...) applique la fonction int() à chaque élément de la liste résultante, convertissant chaque sous-chaîne en un entier.
# list() convertit l'objet itérable retourné par map() en une véritable liste Python d'entiers.
a = list(map(int, input().split()))

# Trie la liste a par ordre décroissant (du plus grand au plus petit).
# La méthode sort() réordonne la liste sur place.
# reverse=True signifie que la liste sera triée dans l'ordre inverse du tri croissant par défaut.
a.sort(reverse=True)

# Initialise la variable ans à 0.
# Cette variable servira à stocker la somme des différences successives des éléments de la liste.
ans = 0

# Initialise la variable before avec la première valeur de la liste triée a, c'est-à-dire la plus grande valeur.
# Cela servira de référence pour la première soustraction dans la prochaine boucle.
before = a[0]

# Boucle for qui parcourt chaque élément i dans la liste a, en commençant à partir du deuxième élément (a[1:]).
# a[1:] signifie une tranche de la liste a du deuxième élément jusqu'à la fin.
for i in a[1:]:
    # Soustrait la valeur actuelle i de before et ajoute le résultat à la variable ans.
    # Cela calcule l'écart positif entre la valeur précédente (before) et la valeur courante (i).
    ans += before - i
    # Met à jour before avec la valeur courante i pour le prochain tour de boucle.
    before = i

# Affiche la valeur finale de ans.
# print() affiche la valeur sur la sortie standard, généralement à l'écran.
print(ans)