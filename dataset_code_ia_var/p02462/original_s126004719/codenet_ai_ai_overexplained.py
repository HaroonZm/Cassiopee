# Importation des modules nécessaires.
# 'bisect' est un module qui fournit des fonctions pour gérer des listes triées.
import bisect  # Nous importons le module complet pour l'utiliser si besoin.
from bisect import bisect_left, bisect_right, insort_left  
# 'bisect_left' retourne l'indice d'insertion pour garder la liste triée.
# 'bisect_right' fait de même mais insère après toute occurrence existante.
# 'insort_left' insère l'élément à gauche pour garder la liste triée.

# Création d'un dictionnaire vide qui va agir comme multi-map,
# c'est-à-dire une structure de données où une clé peut être associée à plusieurs valeurs.
dict = {}

# Création d'une liste vide pour stocker toutes les clés des entrées du dictionnaire.
# Cette liste va rester triée à chaque insertion.
keytbl = []

# Lecture du nombre de requêtes à traiter.
# La fonction input() lit une ligne de l'entrée standard. int() convertit la chaîne en entier.
q = int(input())

# Boucle sur toutes les requêtes reçues.
# La variable 'i' prend toutes les valeurs de 0 à q-1 mais, ici, 'i' n'est pas utilisée.
for i in range(q):

    # Lecture d'une requête. Chaque ligne d'entrée est découpée selon les espaces.
    # Cela crée une liste de chaînes.
    a = list(input().split())

    # Récupération de la clé (de type chaîne) dans la requête.
    # La clé se situe toujours à la deuxième position (indice 1) dans la liste d'arguments 'a'.
    ki = a[1]

    # Vérification du type de requête selon le premier élément de la liste 'a'.
    # Si ce n'est pas le bon type, elle n'est pas traitée ici.

    # Cas 0 : insertion d'une valeur pour une clé.
    if a[0] == '0':
        # Si la clé 'ki' n'est pas déjà dans le dictionnaire,
        # Il faut initialiser la liste des valeurs pour cette clé.
        if ki not in dict:
            # Initialise une nouvelle entrée dans le dictionnaire.
            # La valeur associée à la clé 'ki' est une liste vide.
            dict[ki] = []

            # On insert la clé dans la liste triée des clés.
            # 'insort_left' insère la clé tout en gardant keytbl trié.
            insort_left(keytbl, ki)

        # Maintenant, on ajoute la valeur à la liste correspondant à la clé.
        # La valeur à stocker est le troisième argument, il est converti en entier.
        dict[ki].append(int(a[2]))

    # Cas 1 : impression (affichage) des valeurs associées à une clé.
    elif a[0] == '1' and ki in dict and dict[ki] != []:
        # On vérifie que la clé existe dans le dictionnaire et que sa liste de valeurs n'est pas vide.
        # On affiche chaque valeur sur sa propre ligne.
        # *dict[ki] "dépaquette" la liste pour passer chaque élément individuellement à print().
        # 'sep' spécifie le séparateur entre les éléments, ici un retour à la ligne.
        print(*dict[ki], sep='\n')

    # Cas 2 : suppression de toutes les valeurs associées à une clé.
    elif a[0] == '2' and ki in dict:
        # Si la clé existe, on vide simplement la liste de valeurs pour cette clé.
        dict[ki] = []

    # Cas 3 : impression de toutes les paires 'clé valeur' pour les clés dans un intervalle [L, R).
    elif a[0] == '3':
        # L'intervalle commence à la clé a[1] et finit à la clé a[2] (non inclus).
        # On cherche leurs positions respectives dans la liste triée keytbl.

        # La fonction bisect_left retourne l'indice à partir duquel on peut insérer a[1] pour garder la liste keytbl triée.
        L = bisect_left(keytbl, a[1])

        # bisect_right retourne l'indice OÙ insérer a[2] pour garder la liste ordonnée. C'est donc l'extrémité supérieure exclusive.
        R = bisect_right(keytbl, a[2])

        # On parcourt toutes les clés dans l'intervalle voulu, via leurs indices dans keytbl.
        for j in range(L, R):
            # Pour chaque clé, on parcourt sa liste de valeurs dans le dictionnaire.
            for k in dict[keytbl[j]]:
                # On affiche la clé puis la valeur, séparées par un espace (par défaut).
                print(keytbl[j], k)