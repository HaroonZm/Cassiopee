import re  # Importe le module 're' de la bibliothèque standard de Python, qui permet de travailler avec les expressions régulières

n = int(input())  # Demande à l'utilisateur de saisir une entrée, puis convertit cette entrée en un entier en utilisant la fonction 'int', et assigne la valeur à la variable 'n'

s = input()  # Demande à l'utilisateur une nouvelle saisie, cette fois une chaîne de caractères, stockée dans la variable 's'

res = 10**10  # Initialise la variable 'res' avec une valeur très grande (10 à la puissance 10 = 10000000000) afin d'avoir une borne supérieure suffisante pour les comparaisons ultérieures

# Recherche au début de la chaîne 's' (grâce à l'accent circonflexe '^' de l'expression régulière) une séquence quelconque (y compris vide) de caractères '<' consécutifs
# La fonction 're.search' retourne un objet de correspondance représentant la première occurrence trouvée
# La méthode '.group()' retourne la correspondance retrouvée (en tant que chaîne de caractères)
# La fonction 'len' détermine la longueur de cette séquence, c'est-à-dire le nombre de '<' initiaux (ou 0 si ce n'est pas trouvé)
# La fonction 'min' permet de choisir la plus petite valeur entre la valeur déjà présente dans 'res' et ce nouveau résultat
res = min(res, len(re.search(r'^<*', s).group()))

# Recherche à la fin de la chaîne 's' (grâce au symbole '$' de l'expression régulière) une séquence (y compris vide) de caractères '>' consécutifs
# Ce fonctionnement est similaire à la recherche précédente mais concerne cette fois les '>' finaux
res = min(res, len(re.search(r'>*$', s).group()))

# La fonction 'print' affiche le résultat à l'écran
# L'expression 'n-res' calcule la différence entre la longueur totale (n) de la chaîne et la plus petite séquence trouvée soit au début (des '<'), soit à la fin (des '>')
# Cela correspond généralement à l'indice de la première position qui n'est pas dans le bloc bordant de '<' ou de '>'
print(n - res)