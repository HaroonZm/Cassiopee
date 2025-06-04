# Demande à l'utilisateur de saisir une entrée (par exemple, le nombre d'éléments à lire)
# Cette entrée est lue, mais sa valeur n'est pas stockée dans une variable, donc elle est ignorée pour la suite du programme
input()

# Demande une deuxième entrée à l'utilisateur, attendue comme une séquence d'entiers séparés par des espaces
# La fonction input() lit la ligne saisie par l'utilisateur et retourne une chaîne de caractères représentant cette ligne

# La méthode split() est appelée sur cette chaîne de caractères
# split() sans argument sépare la chaîne au niveau des espaces (ou tout caractère d'espacement)
# Le résultat est une liste de sous-chaînes, chacune correspondant normalement à un nombre saisi par l'utilisateur

# Une liste en compréhension est utilisée pour itérer sur chaque élément x de la liste résultant du split()
# int(x) convertit chaque sous-chaîne x en un entier (classe int)
# Cela produit une nouvelle liste composée des versions entières de chaque sous-chaîne

# La fonction sum() prend en argument la liste créée et calcule la somme de tous ses éléments
# sum() additionne chaque entier contenu dans la liste pour donner le total

# Enfin, print() affiche cette somme totale à la sortie standard (typiquement, l'écran)
print(sum([int(x) for x in input().split()]))