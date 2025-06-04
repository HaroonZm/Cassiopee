# Définition de la fonction principale nommée "main"
def main():
    # Appel de la fonction input() pour demander à l'utilisateur d'entrer une valeur.
    # Cette valeur représente un nombre entier et sera convertie en entier grâce à int().
    # La variable 'n' contiendra donc le nombre d'éléments qui suivront dans la prochaine entrée utilisateur.
    n = int(input())

    # Appel de la fonction input() une nouvelle fois pour permettre à l'utilisateur de saisir des valeurs sur une ligne.
    # La méthode split() coupe la chaîne de caractères en morceaux (éléments) là où il y a des espaces.
    # On parcourt chaque élément obtenu dans la liste temporaire grâce à une compréhension de liste.
    # Chaque élément de la chaîne (qui est un nombre sous forme de chaîne de caractères) est converti en entier par int().
    # La liste finale est entourée par set() pour obtenir un ensemble.
    # Un ensemble (set) ne contient pas de doublons : tous les éléments seront uniques entre eux.
    a = set([int(a) for a in input().split()])

    # On répète exactement le même processus pour la variable 'm', qui indique combien de valeurs comprendra 'b'.
    # Encore une fois, int() convertit la chaîne de caractères entrée par l'utilisateur en nombre entier.
    m = int(input())

    # Nouvelle saisie par l'utilisateur, fractionnée en éléments grâce à split(), puis chaque élément est converti en entier.
    # Tous les éléments sont stockés de façon unique dans un nouvel ensemble 'b'.
    b = set([int(a) for a in input().split()])

    # La méthode union() d'un set retourne un nouvel ensemble contenant tous les éléments présents dans soit le set 'a', soit le set 'b', soit les deux (pas de doublons).
    # Ainsi, 'c' sera l'ensemble de tous les éléments uniques contenus dans 'a' ou 'b' ou les deux.
    c = a.union(b)

    # La fonction sorted() prend en argument n'importe quel objet itérable et renvoie une nouvelle liste contenant tous ses éléments triés par ordre croissant.
    # Ici, on trie l'ensemble 'c' (qui ne garantit pas l'ordre des éléments).
    # Le résultat, 'sorted_c', est donc une liste de tous les éléments uniques réunis, triés du plus petit au plus grand.
    sorted_c = sorted(c)

    # Pour chaque élément 'i' dans la liste triée 'sorted_c'
    for i in sorted_c:
        # Affichage de l'élément 'i' à l'écran grâce à print()
        print(i)

# Appel direct de la fonction main() pour démarrer le programme lorsque ce fichier est exécuté.
main()