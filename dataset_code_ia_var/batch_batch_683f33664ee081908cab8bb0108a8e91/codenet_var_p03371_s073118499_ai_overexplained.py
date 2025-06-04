# On utilise la fonction map pour appliquer la fonction int à chaque élément obtenu par input().split()
# input() permet à l'utilisateur de saisir des valeurs séparées par des espaces sur une seule ligne.
# split() divise l'entrée utilisateur en une liste de chaînes en se basant sur les espaces.
# map(int, ...) convertit chaque chaîne en un entier.
# a, b, c, x, y reçoivent respectivement les 5 entiers fournis par l'utilisateur.
a, b, c, x, y = map(int, input().split())

# On initialise une variable nommée ans. Elle sert à stocker la valeur minimale du coût trouvé jusqu'à présent.
# 10**18 représente un nombre entier très grand qui garantit que toute valeur trouvée sera plus petite.
ans = 10 ** 18

# La boucle for sert à envisager toutes les quantités paires possibles de l'achat du produit mixte (option c).
# range(0, 2*max(x, y)+2, 2):
#   - commence à 0,
#   - va jusqu'à 2 fois le maximum entre x et y, plus 2, pour s'assurer de couvrir tous les scénarios possibles,
#   - s'incrémente de 2 à chaque itération pour ne parcourir que les nombres pairs (car on achète 2 produits mixtes à la fois).
for i in range(0, 2 * max(x, y) + 2, 2):
    # On crée deux nouvelles variables X et Y pour représenter les quantités restantes du produit de type 1 (x) et de type 2 (y)
    # après avoir potentiellement utilisé i unités de produit mixte.
    X, Y = x, y

    # Chaque unité de produit mixte permet d'obtenir un de chaque type, donc i//2 produits mixtes couvrent i//2 de x et i//2 de y.
    # On soustrait cette quantité de X et Y respectivement.
    X -= i // 2  # Retirer la quantité couverte par les produits mixtes du total requis pour X
    Y -= i // 2  # Retirer la quantité couverte par les produits mixtes du total requis pour Y

    # Il n'est pas possible d'acheter une quantité négative d'un produit, donc on corrige les valeurs à 0 si elles sont devenues négatives.
    X = max(0, X)  # Si X est négatif, on le met à 0
    Y = max(0, Y)  # Si Y est négatif, on le met à 0

    # On calcule le coût total pour la configuration actuelle:
    # - On paie 'a' pour chaque unité de produit de type 1 non couverte par le mixte.
    # - On paie 'b' pour chaque unité de produit de type 2 non couverte par le mixte.
    # - On paie 'c' pour chaque unité de produit mixte (et on en a acheté 'i').
    cost = a * X + b * Y + c * i

    # On met à jour ans en gardant le minimum entre la valeur actuelle de ans et le coût calculé ci-dessus.
    ans = min(ans, cost)

# Après avoir examiné toutes les possibilités, on affiche le coût minimum trouvé.
print(ans)