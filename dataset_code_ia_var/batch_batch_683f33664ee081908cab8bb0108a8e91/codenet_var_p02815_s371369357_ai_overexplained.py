# Demander à l'utilisateur de saisir un nombre entier.
# La fonction input() lit une ligne entrée par l'utilisateur sous forme de chaîne de caractères.
# La fonction int() convertit cette chaîne en entier.
n = int(input())

# Lire une ligne de nombres entiers séparés par des espaces depuis l'entrée utilisateur.
# input() retourne la ligne sous forme de chaîne de caractères.
# split() divise la chaîne en une liste de sous-chaînes selon les espaces.
# map(int, ...) applique la fonction int() à chaque sous-chaîne, les convertissant en entiers.
# list(...) convertit le map en une liste d'entiers.
c = list(map(int, input().split()))

# Définir la constante mod, qui servira à effectuer des opérations modulo un grand nombre premier pour éviter les débordements d'entiers.
mod = 10**9 + 7

# Trier la liste c en ordre décroissant.
# sort() trie la liste sur place.
# reverse=True spécifie de trier du plus grand au plus petit.
c.sort(reverse=True)

# Initialiser la variable de réponse à 0. Elle contiendra le résultat final de nos calculs.
ans = 0

# Boucler sur la liste c pour calculer une somme pondérée.
# enumerate(c) donne à chaque itération un couple (k, num)
# où k est l'indice dans la liste (commençant à 0)
# et num est la valeur de l'élément à cet indice.
for k, num in enumerate(c):
    # Ajouter à ans le produit de (k + 2) et num.
    # (k + 2) augmente de 2 à chaque élément, car k commence à 0.
    ans += (k + 2) * num
    # Ensuite, prendre le reste modulo mod pour éviter les débordements.
    ans %= mod

# Répéter une opération un certain nombre de fois.
# range(2 * n - 2) génère une séquence allant de 0 à (2 * n - 2) - 1.
for _ in range(2 * n - 2):
    # Multiplier ans par 2.
    ans *= 2
    # Prendre le résultat modulo mod pour rester dans les limites autorisées et éviter les grands nombres.
    ans %= mod

# Afficher le résultat final.
# print() affiche la valeur de ans dans la sortie standard.
print(ans)