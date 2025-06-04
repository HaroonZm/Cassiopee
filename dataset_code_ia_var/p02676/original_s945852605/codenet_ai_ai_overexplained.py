# Demande à l'utilisateur de saisir un entier via la fonction input()
# input() lit une ligne de texte au clavier et retourne une chaîne de caractères (str)
# int() convertit cette chaîne de caractères en un entier (int)
k = int(input())

# Demande à l'utilisateur de saisir une chaîne de caractères via la fonction input()
# input() lit une ligne de texte au clavier et retourne une chaîne de caractères (str)
# list() convertit cette chaîne de caractères en une liste où chaque élément correspondra à un caractère de la chaîne
s = list(input())

# Vérifie si la longueur de la liste s (c'est-à-dire le nombre de caractères saisis) est strictement supérieure à k
if len(s) > k:
    # Si c'est le cas, la chaîne est trop longue et il faut la tronquer
    # s[:k] permet d'extraire une sous-liste contenant les k premiers éléments (caractères) de la liste s
    t = s[:k]
    # .append('...') ajoute l'élément '...' (trois points de suspension sous forme de chaîne) à la fin de la liste t
    t.append('...')
    # ''.join(t) fusionne tous les éléments de la liste t en une seule chaîne de caractères
    # La méthode .join() prend un itérable (ici, la liste t) et concatène tous ses éléments en insérant la chaîne vide '' entre eux,
    # ce qui, dans ce cas, colle simplement tous les caractères les uns à la suite des autres sans séparateur
    print(''.join(t))
else:
    # Si la longueur de la liste s n'est pas strictement supérieure à k (donc inférieure ou égale à k),
    # alors il suffit d'afficher la chaîne telle quelle sans la tronquer
    # ''.join(s) reconstruit la chaîne de caractères à partir de la liste de caractères s
    print(''.join(s))