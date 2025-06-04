# Commence par lire une ligne de texte saisie par l'utilisateur via le clavier
# La fonction input() affiche une invite et attend l'entrée d'une valeur sous forme de chaîne de caractères (string)
# Ensuite, input().split() sépare cette chaîne en une liste de chaînes en découpant là où un espace apparaît
# On applique map(int, ...) pour convertir chaque chaîne de cette liste en un entier (int)
# map() applique la fonction int à chaque élément de la liste obtenue par split()
# Cela produit un itérable qui donne chaque entier correspondant à chaque valeur saisie

# Créons un tuple contenant les valeurs des différents types de pièces, dans l'ordre spécifié
# (1, 5, 10, 50, 100, 500) signifie : 1 unité, 5 unités, etc., jusqu'à 500 unités pour chaque type de pièce
pieces = (1, 5, 10, 50, 100, 500)

# On zippe (associe) chaque type de pièce avec la quantité correspondante fournie par l'utilisateur
# zip(a, b) forme des paires (i, j) où i provient de a et j de b simultanément
# Cela donne un itérable de couples : (valeur de la pièce, quantité saisie)

# Pour chaque couple (i, j), on calcule le produit i * j :
# - i : valeur d'un type de pièce
# - j : nombre de pièces de ce type
# i * j donne le montant total pour ce type de pièce

# La compréhension génératrice (i * j for i, j in zip(...)) calcule le produit pour chacun des six types de pièces

# sum(...) additionne tous ces produits, donnant la somme totale d'argent détenue

# On vérifie si la somme ainsi calculée est supérieure ou égale à 1000
# (sum(...) >= 1000) produit alors True ou False (valeurs booléennes en Python)

# L'opérateur ternaire (if ... else ...) permet de retourner 1 si la somme est au moins 1000 ; sinon 0

# Enfin, print(...) affiche la valeur 1 ou 0 obtenue en sortie à l'écran

# Appelons donc le code complet, assorti de tous ces commentaires :
print(
    # Affiche 1 si la somme de l'argent est supérieure ou égale à 1000, sinon 0
    1
    if
        # Calcule la somme totale d'argent
        sum(
            # Génère chaque montant total pour chaque type de pièce
            (i * j       # i = valeur de la pièce, j = nombre de pièces
             for i, j in
             zip(        # Associe chaque valeur de pièce à son nombre saisi
                 (1, 5, 10, 50, 100, 500),  # Tuple des valeurs des pièces
                 map(
                     int,                # Convertit chaque saisie en entier
                     input().split()     # Récupère la saisie, la découpe par espaces
                 )
             )
            )
        )
        >= 1000   # Vérifie si la somme est supérieure ou égale à 1000
    else
        0         # Sinon, retourne 0
)