# Importation du module Counter à partir de collections pour compter les occurrences d'éléments hachables
from collections import Counter
# Importation de product à partir de itertools pour générer le produit cartésien de plusieurs itérables,
# ce qui permet de parcourir toutes les combinaisons possibles de 0 et 1 pour N éléments
from itertools import product

# Lecture d'un entier N depuis l'entrée standard. La fonction input() collecte l'entrée de l'utilisateur sous forme de chaîne.
# int() convertit cette chaîne en un entier.
N = int(input())

# Lecture d'une chaîne de caractères comme entrée. input() retourne une chaîne,
# list() transforme chaque caractère de cette chaîne en un élément de liste : ['a', 'b', 'c']
S = list(input())

# Prendre la partie droite de la chaîne en considérant les caractères depuis l'indice N jusqu'à la fin.
# reversed() retourne un itérable qui lit la séquence à l'envers.
# list() transforme cet itérable en une liste de caractères inversée.
# Cela permet de traiter la moitié droite de S, mais en la lisant de droite à gauche.
S_rev = list(reversed(S[N:]))

# Création d'une liste vide pour stocker toutes les manières de diviser la moitié gauche (première moitié des caractères)
# en deux groupes différents (par exemple, "rouge" et "bleu").
leftlist = []

# Même chose pour la moitié droite, pour stocker toutes les combinaisons possibles de répartition de cette moitié en deux groupes.
rightlist = []

# Parcours de toutes les combinaisons possibles pour N éléments où chaque élément peut être 0 ou 1.
# range(2) produit les valeurs 0 et 1.
# repeat=N pour obtenir toutes les suites de longueur N de 0 et 1.
# product() va donc générer toutes les répartitions possibles.
# Par exemple, pour N=2 : (0,0), (0,1), (1,0), (1,1)
for bit in product(range(2), repeat=N):
    # Initialisation des chaînes de caractères vides pour les groupes "rouge" et "bleu" de la moitié gauche.
    red_left = ''
    blue_left = ''
    # Initialisation des chaînes de caractères vides pour les groupes "rouge" et "bleu" de la moitié droite (mais dans le sens inversé).
    red_right = ''
    blue_right = ''

    # Parcours de chaque position possible dans la moitié du tableau, c'est-à-dire de 0 à N-1
    for j in range(N):
        # Si à la position j, le bit vaut 1, alors :
        if bit[j] == 1:
            # On ajoute le caractère de la moitié gauche à la chaîne "rouge" côté gauche
            red_left += S[j]
            # On ajoute le caractère du même rang dans la moitié droite inversée à la chaîne "bleue" côté droit
            blue_right += S_rev[j]
        else:
            # Sinon, le caractère de la moitié gauche va dans la chaîne "bleue" côté gauche
            blue_left += S[j]
            # Et le caractère associé de la moitié droite inversée va dans la chaîne "rouge" côté droit
            red_right += S_rev[j]

    # On combine les deux groupes ("rouge" et "bleu") de la moitié gauche séparés par "|" et on les ajoute à la liste leftlist
    leftlist.append("".join(red_left + "|" + blue_left))
    # On combine les deux groupes ("bleu" et "rouge") de la moitié droite séparés par "|" (l'ordre est inversé par rapport à la gauche)
    rightlist.append("".join(blue_right + "|" + red_right))

# Utilisation de Counter pour compter le nombre d'occurrences de chaque façon de répartir la moitié gauche
left = Counter(leftlist)
# Idem pour la moitié droite
right = Counter(rightlist)

# Initialisation de la variable qui va contenir la réponse finale.
answer = 0

# Parcours de chaque manière distincte de répartir la moitié gauche, ainsi que de leur nombre d'occurrences
for key, value in left.items():
    # Pour chaque tel "key" (combinaison de répartition), on multiplie le nombre de façons dont on l'obtient dans la moitié gauche (value)
    # par le nombre de façons où la moitié droite a la même répartition (right[key]).
    # Cela donne le nombre de combinaisons globales où la répartition est identique sur les deux moitiés
    answer += value * right[key]

# Affichage de la réponse calculée, c'est-à-dire le nombre total de combinaisons correspondantes
print(answer)