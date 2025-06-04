# Définition de la fonction principale appelée "main"
def main():
    # Demande à l'utilisateur de saisir une valeur. input() attend que l'utilisateur saisisse une ligne au clavier.
    # Ensuite, cette valeur est convertie en entier avec int(), car input() retourne toujours une chaîne de caractères.
    n = int(input())
    
    # Demande à l'utilisateur de saisir une ligne de nombres séparés par des espaces.
    # input().split() retourne une liste de chaînes correspondant aux éléments séparés par des espaces.
    # La compréhension de liste [int(a) for a in input().split()] convertit chaque chaîne en entier.
    # set([...]) prend la liste obtenue et en fait un ensemble ("set") qui ne contient que des éléments uniques, supprimant les doublons.
    a = set([int(a) for a in input().split()])
    
    # Même opération que ci-dessus :
    # Saisie d'un entier représentant le nombre d'éléments dans l'ensemble b.
    m = int(input())
    # Création du set b à partir des entrées utilisateur converties en entiers.
    b = set([int(a) for a in input().split()])

    # L'opération a.symmetric_difference(b) retourne un nouvel ensemble.
    # Cet ensemble contient tous les éléments qui sont uniquement dans a ou uniquement dans b, mais pas dans les deux.
    c = a.symmetric_difference(b)
    
    # La fonction sorted(c) prend l'ensemble c et retourne une nouvelle liste contenant tous ses éléments ordonnés croissants.
    sorted_c = sorted(c)
    
    # Boucle for : pour chaque élément i dans la liste triée sorted_c...
    for i in sorted_c:
        # Affiche la valeur de i. print() écrit cette valeur dans la console et passe à la ligne suivante.
        print(i)

# Appel de la fonction main, cela lance réellement l'exécution du script si ce fichier est exécuté.
main()