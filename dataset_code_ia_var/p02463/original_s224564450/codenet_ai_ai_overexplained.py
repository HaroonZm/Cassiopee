# Lecture d'une ligne d'entrée utilisateur. Le résultat de input() est une chaîne de caractères, mais ici, la valeur lue n'est pas utilisée.
input()

# Lecture d'une seconde ligne d'entrée utilisateur.
# input() lit tout ce que l'utilisateur tape jusqu'à appuyer sur Entrée, et retourne une chaîne de caractères.
# split() sépare cette chaîne en une liste de sous-chaînes, en utilisant les espaces comme séparateurs par défaut.
# La compréhension de liste parcourt chaque sous-chaîne 'x' produite par split().
# Chaque 'x' est converti en un entier à l'aide de int(x).
# Le résultat est une nouvelle liste 'L' contenant tous les entiers convertis depuis la ligne d'entrée.
L = [int(x) for x in input().split()]

# Lecture d'une troisième ligne d'entrée utilisateur. Là encore, cette valeur lue n'est pas utilisée.
input()

# Lecture d'une quatrième ligne d'entrée utilisateur.
# De la même manière, on convertit chaque valeur saisie sur cette ligne en un entier.
# La liste finale 'Q' contient tous ces entiers.
Q = [int(x) for x in input().split()]

# Construction d'un ensemble à partir de la liste L.
# Un 'set' en Python est une structure de données qui ne permet de stocker chaque élément qu'une seule fois (pas de doublons).
set_L = set(L)

# Construction d'un ensemble à partir de la liste Q, éliminant aussi les doublons de Q.
set_Q = set(Q)

# L'opérateur '|' (barre verticale) effectue l'union de deux ensembles en Python.
# L'union contient tous les éléments présents dans set_L, dans set_Q, ou dans les deux.
union_set = set_L | set_Q

# La fonction sorted() prend en argument un objet itérable (par exemple, une liste ou un ensemble).
# Elle retourne une nouvelle liste contenant tous les éléments de l'objet trié dans l'ordre croissant.
# sorted() est utilisé ici pour trier les éléments de l'union de L et Q dans l'ordre numérique croissant.
sorted_union = sorted(union_set)

# Boucle 'for' permettant d'itérer (parcourir) chaque élément 'i' de la liste triée sorted_union.
for i in sorted_union:
    # Affichage de la valeur de 'i' à l'aide de la fonction print().
    # Cette instruction affiche la valeur de 'i' sur la sortie standard (écran), suivie d'un retour à la ligne (comportement par défaut de print).
    print(i)