# Demande à l'utilisateur d'entrer une valeur, lit cette valeur depuis l'entrée standard (le clavier)
# La valeur lue est une chaîne de caractères, donc elle doit être convertie (castée) en entier avec int()
# Cet entier représente le nombre d'éléments qu'on va saisir ensuite pour l'ensemble 'a'
n = int(input())

# Demande à l'utilisateur de saisir des nombres séparés par des espaces sur une seule ligne
# input().split() va lire la ligne entière et la découper (split) en une liste de sous-chaînes de caractères selon les espaces
# map(int, ...) applique la fonction int() à chaque sous-chaîne de caractères pour les convertir en entiers
# set(...) prend l'itérable et le transforme en un objet de type 'set' (ensemble non ordonné, sans doublons)
# Ainsi, on obtient un ensemble 'a' contenant tous les entiers entrés par l'utilisateur, par conversion et sans doublons
a = set(map(int, input().split()))

# De la même manière qu'au début, on demande à l'utilisateur le nombre d'éléments de l'ensemble 'b'
m = int(input())

# On crée l'ensemble 'b' exactement comme pour 'a', c'est-à-dire avec conversion en entiers puis en ensemble
b = set(map(int, input().split()))

# On crée un nouvel ensemble qui est l'union de l'ensemble 'a' et de l'ensemble 'b'
# L'union de deux ensembles contient tous les éléments présents dans l'un ou l'autre sans doublons
# .union() retourne un nouvel ensemble qui contient tous les éléments distincts des deux ensembles
s_union = a.union(b)

# sorted() prend n'importe quel itérable (ici notre ensemble union) et retourne une nouvelle liste contenant les éléments triés
# * (splat) devant la liste la "dépaquette" : chaque élément de la liste est passé séparément comme argument à print()
# sep="\n" signifie que print va afficher chaque argument sur une nouvelle ligne (un saut de ligne entre chaque)
print(*sorted(s_union), sep="\n")