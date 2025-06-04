# Demande à l'utilisateur de saisir une ligne de texte et lit cette entrée.
# La fonction input() capture tout ce que l'utilisateur tape jusqu'à l'appui sur Entrée.
# Ensuite, la méthode split(" ") sépare cette ligne de texte en éléments distincts en utilisant l'espace " " comme séparateur.
# La liste résultante contient des chaînes de caractères représentant les nombres saisis.
# Pour chaque élément de cette liste, int(i) convertit la chaîne de caractères en entier.
# [int(i) for i in ...] construit une nouvelle liste d'entiers à partir de la liste de chaînes.
abc = [int(i) for i in input().split(" ")]

# La fonction sorted(abc) retourne une nouvelle liste contenant les mêmes éléments que 'abc',
# mais triés du plus petit au plus grand, c'est-à-dire en ordre croissant.
# Cela signifie que abc[0] sera le plus petit nombre, abc[1] le nombre intermédiaire, et abc[2] le plus grand.
abc = sorted(abc)

# On assigne à la variable 'a' la valeur du premier élément de la liste ordonnée (le plus petit nombre).
a = abc[0]
# On assigne à la variable 'b' la valeur du deuxième élément de la liste (le nombre intermédiaire).
b = abc[1]
# On assigne à la variable 'c' la valeur du troisième élément de la liste (le plus grand nombre).
c = abc[2]

# On vérifie si 'a' et 'b' sont égaux grâce à l'opérateur de comparaison ==.
if a == b:
    # Si 'a' est égal à 'b', on calcule la différence entre 'c' et 'a'.
    # str() convertit ce nombre entier en chaîne de caractères pour pouvoir l'afficher avec print().
    print(str(c - a))
else:
    # Si 'a' n'est pas égal à 'b', on effectue un autre test :
    # On calcule la différence (a-b).
    # Ensuite, on utilise l'opérateur modulo % pour vérifier si cette différence est un nombre pair.
    if (a - b) % 2 == 0:
        # Si la différence (a-b) est paire, on calcule ((b-a)/2 + c - b).
        # (b-a)/2 représente la moitié de la différence d'écart entre 'a' et 'b'.
        # c-b est la différence entre le plus grand et l'intermédiaire.
        # int() assure que le résultat est un entier, car la division peut donner un nombre à virgule flottante.
        # str() convertit ce nombre entier en chaîne pour l'affichage.
        print(str(int((b - a) / 2 + c - b)))
    else:
        # Si la différence (a-b) est impaire, on effectue un autre calcul :
        # (b-a-1)/2 calcule la moitié de 'b-a-1', qui fait en sorte d'obtenir un nombre entier inférieur en cas d'écart impair.
        # +1 ajuste cet écart pour compenser l'arrondi à l'entier inférieur.
        # c+1-b est similaire à c-b, mais on ajoute 1 pour ajuster la différence pour le cas impair.
        # int() force le résultat à être un entier.
        print(str(int((b - a - 1) / 2 + 1 + c + 1 - b)))