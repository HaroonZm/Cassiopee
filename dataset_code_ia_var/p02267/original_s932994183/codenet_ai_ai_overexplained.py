# Demande à l'utilisateur de saisir une valeur, la convertit en entier et l'assigne à la variable 'n'
# Cela représente le nombre d'éléments dans l'ensemble S, bien que cette variable ne soit pas explicitement utilisée plus loin
n = int(input())

# Lit une ligne de texte au clavier (l'utilisateur doit saisir des éléments séparés par des espaces)
# La méthode .split() divise la chaîne en une liste de sous-chaînes (chaque sous-chaîne est un élément saisi)
# La fonction set() prend cette liste et la convertit en un ensemble (structure de données qui n'accepte pas de doublons)
# L'ensemble ainsi créé est stocké dans la variable S
S = set(input().split())

# Demande à l'utilisateur de saisir une valeur, la convertit en entier et l'assigne à la variable 'q'
# Ceci représente le nombre d'éléments dans l'ensemble T, bien que cette variable ne soit pas non plus explicitement utilisée par la suite
q = int(input())

# Comme précédemment, lit une ligne de texte, la découpe en sous-chaînes grâce à .split(), puis crée un ensemble avec ces éléments
# L'ensemble constitué est assigné à la variable T
T = set(input().split())

# Calcule l'intersection des deux ensembles S et T en utilisant l'opérateur & (qui renvoie les éléments communs aux deux ensembles)
# len() renvoie le nombre d'éléments dans cette intersection, i.e. le nombre d'éléments que S et T ont en commun
# La fonction print() affiche ce nombre à l'écran
print(len(S & T))