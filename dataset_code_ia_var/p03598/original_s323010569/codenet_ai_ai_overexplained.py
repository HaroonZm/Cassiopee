# Demande à l'utilisateur de saisir un nombre entier.
# Ce nombre représente probablement la taille de la liste ou une borne supérieure.
N = int(input())  # Conversion explicite de la saisie utilisateur (str) en entier (int)

# Demande à l'utilisateur de saisir un autre nombre entier.
# Cela pourrait être une sorte de valeur de seuil ou de limite pour les traitements suivants.
K = int(input())  # Conversion explicite de la saisie utilisateur (str) en entier (int)

# Demande à l'utilisateur d'entrer une ligne contenant N valeurs séparées par des espaces.
# 'input()' retourne une chaîne de caractères, par exemple "1 2 3"
# 'split()' divise cette chaîne en une liste de sous-chaînes ['1', '2', '3']
# 'map(int, ...)' applique la fonction int à chaque élément de cette liste pour la transformer en entiers [1, 2, 3]
# 'list(...)' convertit l'objet map en une liste d'entiers.
A = list(map(int, input().split()))

# Initialise une variable nommée 'ans' qui servira à cumuler le résultat calculé.
# Elle commence à 0 car on n'a encore rien additionné.
ans = 0

# On parcourt la liste des entiers A élément par élément.
# 'x' prendra successivement la valeur de chaque élément de la liste A.
for x in A:
    # Pour chaque élément x, on calcule la différence K-x.
    # On prend également la valeur minimale entre x et K-x avec min(x, K-x).
    # Ceci permet de choisir la valeur la plus petite entre x et la différence K-x.
    # Puis on multiplie ce minimum par 2, ce qui a pour effet de doubler ce minimum.
    # On ajoute ce résultat à la variable accumulatrice 'ans'.
    ans += min(x, K - x) * 2

# Après la boucle, on affiche la valeur finale de 'ans' à l'écran.
# Cela donne le résultat global du calcul effectué sur la liste initiale.
print(ans)