# Demander à l'utilisateur de saisir un entier, qui sera converti à partir de la chaîne saisie par l'utilisateur via input().
# L'appel à int() transforme la saisie de type texte en un entier (par exemple, "3" devient 3).
n = int(input())

# Demander à l'utilisateur de saisir une série de nombres séparés par des espaces sous forme de texte.
# input() lit la ligne d'entrée et retourne une chaîne de caractères.
# split() sépare cette chaîne en une liste de chaînes selon les espaces (par défaut).
# map(int, ...) applique la fonction int à chaque élément de la liste, convertissant ainsi chaque chaîne en entier.
# set(...) crée un ensemble (structure de données qui ne contient que des éléments distincts) à partir de ces entiers, éliminant les doublons s'il y en a.
nums = set(map(int, input().split()))

# Lire un autre entier depuis l'entrée utilisateur, identique à la première lecture.
m = int(input())

# Lire une nouvelle série d'entiers depuis l'entrée, séparés par des espaces, traitée de la même manière que précédemment :
# - input(): lit la ligne.
# - split(): sépare la ligne en liste de chaînes.
# - map(int, ...): convertit chaque chaîne en entier.
# - set(...): crée un ensemble des entiers, éliminant les doublons dans cette série.
# nums.update(...): ajoute tous les éléments du nouvel ensemble à l'ensemble existant nums, de sorte que nums contiendra tous les éléments uniques provenant des deux ensembles (ceci est une union d'ensembles, mais modifie directement nums).
nums.update(set(map(int, input().split())))

# sorted(nums) prend l'ensemble nums et le transforme en une nouvelle liste contenant tous les éléments de nums triés dans l'ordre croissant.
# for n in ...: va itérer sur chaque élément (ici nommé n pour la boucle), 
# de cette liste triée, un à un, dans l'ordre défini par sorted().
for n in sorted(nums):
    # Imprime chaque élément n sur une seule ligne, l'un après l'autre.
    # print() par défaut ajoute un saut de ligne après l'élément imprimé, 
    # donc chaque valeur sera affichée sur une nouvelle ligne.
    print(n)