# Demander à l'utilisateur d'entrer une valeur à l'aide de la fonction input().
# La valeur entrée est lue sous forme de chaîne de caractères (string).
# La fonction int() convertit cette chaîne en un nombre entier (int).
# Le résultat est stocké dans la variable "n", qui représentera le nombre de lignes à lire ensuite.
n = int(input())

# Création d'une liste vide nommée "v".
# Cette liste contiendra plusieurs sous-listes d'entiers, à raison d'une sous-liste par ligne d'entrée.
v = []

# Boucle for utilisant une comprehension list, itérant "n" fois grâce à la structure "range(n)".
# Pour chaque itération : 
#   - input() attend que l'utilisateur saisisse une ligne.
#   - input().split() sépare la ligne en différentes sous-chaînes de caractères au niveau des espaces.
#   - map(int, ...) applique la fonction int() à chaque élément de la liste résultante, les convertissant tous en entiers.
#   - list(...) transforme l'objet map en une vraie liste Python d'entiers.
#   - v.append(...) ajoute cette liste à la fin de la liste principale 'v'.
# La comprehension list est utilisée uniquement pour son effet de bord (remplir v), pas pour produire une nouvelle liste.
[v.append(list(map(int, input().split()))) for _ in range(n)]

# Boucle for utilisant encore une comprehension list pour afficher toutes les sous-listes, une par ligne, après tri.
# sorted(v) trie les sous-listes de v dans l'ordre croissant selon les valeurs des éléments (comportement par défaut).
# Pour chaque sous-liste "a" du résultat trié :
#   - map(str, a) transforme chaque entier de la sous-liste "a" en chaîne de caractères.
#   - " ".join(...) assemble ces chaînes en une seule chaîne, séparée par des espaces, pour produire un format lisible.
#   - print(...) affiche cette chaîne à l'écran.
# Ici aussi, la comprehension list est utilisée pour réaliser l'affichage, même si le résultat n'est pas stocké.
[print(" ".join(map(str,a))) for a in sorted(v)]