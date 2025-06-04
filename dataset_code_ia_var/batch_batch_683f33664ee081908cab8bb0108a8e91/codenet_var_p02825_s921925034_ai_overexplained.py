# Début du programme Python

# Lecture d'un entier à partir de l'entrée standard.
# input() capture l'entrée en tant que chaîne de caractères (string), 
# donc int(...) la convertit explicitement en entier.
n = int(input())

# Déclaration d'une liste s3, qui est une liste de chaînes de caractères.
# Chaque élément de cette liste est une chaîne explicitement écrite.
s3 = ["abb", "a.d", "ccd"]

# Déclaration d'une liste nommée 's', qui elle-même contient plusieurs sous-listes.
# Chaque sous-liste contient des chaînes de caractères, 
# donc 's' est une liste de listes de chaînes (liste 2D).
# Chaque sous-liste correspond à un cas particulier utilisé dans la logique ultérieure.
s = [
    ["abcc", "abdd", "ddba", "ccba"],
    ["dccdd", "daa.c", "c..bc", "c..bd", "ddccd"],
    ["abbc..", "a.ac..", "bba.cc", "a..aab", "a..b.b", ".aabaa"],
    ["aba....", "aba....", "bab....", "bab....", "a..bbaa", "a..aabb", ".aabbaa"]
]

# Premier test conditionnel pour vérifier si la variable 'n' contient la valeur 2.
# Le double égal vérifie l'égalité entre deux valeurs.
if n == 2:
    # Si n vaut exactement 2, on affiche la valeur entière -1.
    print(-1)
# Deuxième test conditionnel pour vérifier si 'n' vaut 3.
elif n == 3:
    # Si n vaut 3, on parcourt chaque élément (chaîne) dans la liste s3,
    # et pour chacun, on l'affiche séparément avec print.
    # Cette syntaxe correspond à une compréhension de liste 
    # utilisée uniquement pour ses effets de bord (affichage).
    [print(x) for x in s3]
# Si aucun des cas précédents n'est vrai (n != 2 et n != 3),
# donc pour tous les autres cas où n > 3 en particulier.
else:
    # Utilisation de la fonction divmod() pour effectuer à la fois
    # une division entière et obtenir le reste de la division de n par 4.
    # divmod(n, 4) retourne un tuple (quotient, reste), qui est 
    # ici, décompressé en deux variables : d et m.
    d, m = divmod(n, 4)
    # On décrémente la variable d de 1. Cela équivaut à d = d - 1.
    d -= 1
    # On incrémente la variable m de 4 pour ajuster le reste.
    # Cela correspond à m = m + 4.
    m += 4
    
    # On effectue une boucle for, indexée par 'i' allant de 0 à d-1 inclus.
    # range(d) génère une séquence de valeurs entières de 0 inclus à d exclus.
    for i in range(d):
        # Pour chaque valeur de 'i', on parcourt tous les éléments dans la première sous-liste de 's'.
        # s[0] correspond à ["abcc", "abdd", "ddba", "ccba"].
        # Pour chaque élément 'x' de cette sous-liste, on construit et affiche une nouvelle chaîne :
        # - "." * 4 * i produit une suite de points dont la longueur est 4 fois la valeur de i.
        # - x ajoute la chaîne courante.
        # - "." * (4 * (d - i - 1) + m) produit une autre suite de points,
        #   ici la longueur dépend de d, i, et m.
        # L'utilisation de la compréhension de liste ici est détournée pour ses effets secondaires avec print.
        [print("." * 4 * i + x + "." * (4 * (d - i - 1) + m)) for x in s[0]]

    # À la fin de la boucle précédente (ou si d vaut 0, la boucle n'est pas exécutée),
    # on cherche à afficher une sous-liste de 's', exactement la (m - 4)-ième sous-liste.
    # On parcourt maintenant chaque élément 'x' dans cette sous-liste.
    # On affiche chaque élément précédé de "." * 4 * d, c'est-à-dire une suite de points de longueur 4*d.
    [print("." * 4 * d + x) for x in s[m - 4]]

# Fin du programme