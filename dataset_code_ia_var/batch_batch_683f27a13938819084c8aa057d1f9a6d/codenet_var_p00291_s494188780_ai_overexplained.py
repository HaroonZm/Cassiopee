# Demander à l'utilisateur de saisir une ligne de texte avec des nombres séparés par des espaces
# La fonction input() attend que l'utilisateur saisisse des données et appuie sur Entrée
# La méthode split() divise cette chaîne de caractères en une liste de sous-chaînes (chaque nombre comme texte)
# Ensuite, map(int, ...) applique la fonction int() à chaque sous-chaîne pour convertir chaque chaîne en entier
# Enfin, la fonction list() transforme l'objet map en liste contenant tous les entiers donnés par l'utilisateur
lst = list(map(int, input().split()))

# Nous allons calculer une somme pondérée des éléments de lst correspondant à la valeur et à la quantité de chaque type de pièce (ou billet)
# lst[0] correspond au nombre d'unités de valeur 1
# lst[1] au nombre d'unités de valeur 5
# lst[2] au nombre d'unités de valeur 10
# lst[3] au nombre d'unités de valeur 50
# lst[4] au nombre d'unités de valeur 100
# lst[5] au nombre d'unités de valeur 500
# On multiplie chaque quantité par la valeur de sa monnaie pour obtenir le montant total que l'utilisateur possède
total = lst[0] + lst[1] * 5 + lst[2] * 10 + lst[3] * 50 + lst[4] * 100 + lst[5] * 500

# On utilise une instruction if pour comparer le montant total possédé avec la valeur 1000
# Si total est supérieur ou égal à 1000...
if total >= 1000:
    # ... on affiche la valeur 1 avec print(), ce qui indique que la somme est suffisante
    print(1)
# Sinon, si la condition précédente n'est pas vraie, c'est que total < 1000
else:
    # Donc, on affiche la valeur 0 avec print(), ce qui indique que la somme n'est pas suffisante
    print(0)