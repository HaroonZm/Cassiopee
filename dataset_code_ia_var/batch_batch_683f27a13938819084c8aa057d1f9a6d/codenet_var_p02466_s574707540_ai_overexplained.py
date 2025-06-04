# Demande une entrée de l'utilisateur et la stocke dans la variable 'n'.
# Ici, il s'agit très probablement de la taille de l'ensemble, mais la valeur n'est pas utilisée par la suite.
n = input()

# Demande à l'utilisateur de saisir une ligne de nombres séparés par des espaces.
# La saisie utilisateur (une chaîne de caractères) est découpée en une liste de sous-chaînes à chaque espace.
# La fonction map applique la fonction int à chaque élément de la liste pour les convertir en entiers.
# La fonction set transforme la liste d'entiers en un ensemble, ce qui supprime les doublons et ignore l'ordre.
# L'ensemble obtenu est stocké dans la variable 'a'.
a = set(map(int, input().split()))

# Demande une seconde entrée de l'utilisateur et la stocke dans la variable 'n'.
# Encore une fois, la valeur saisie n'est pas utilisée.
n = input()

# Demande une seconde ligne de nombres à l'utilisateur, séparés par des espaces.
# Même procédé que précédemment : découpage, conversion des chaînes en entiers, création d'un ensemble.
# L'ensemble résultant est stocké dans la variable 'b'.
b = set(map(int, input().split()))

# Calcule la différence symétrique entre les ensembles 'a' et 'b' à l'aide de l'opérateur ^ (XOR ensembliste).
# La différence symétrique contient tous les éléments présents dans 'a' ou dans 'b' mais pas dans les deux à la fois.
# On transforme ensuite l'ensemble résultant par la fonction 'set', mais c'est redondant car l'opération ^ donne déjà un ensemble.
# La fonction sorted() trie les éléments de cet ensemble dans l'ordre croissant et retourne une liste triée des éléments uniques.
# Pour chaque élément x dans cette liste triée, on utilise une boucle for pour l'envoyer à la fonction print, qui affiche l'élément à l'écran.
# L'ensemble de compréhension {print(x) for x in ...} exécute print(x) pour chaque x, mais ne collecte pas les valeurs significatives (print renvoie None).
# L'utilisation d'un set pour l'affichage est atypique, car l’ordre d’évaluation n’est pas garanti et le set contient uniquement des 'None', mais ici c'est utilisé uniquement pour le side effect d'afficher les valeurs.

c = {print(x) for x in sorted(set(a ^ b))}