def main():
    # Demande à l'utilisateur de saisir la longueur de la première liste de mots.
    # Cela lit une ligne depuis l'entrée utilisateur avec raw_input(), ce qui retourne toujours une chaîne.
    s_length = raw_input()
    
    # Demande à l'utilisateur de saisir les mots de la première liste, séparés par des espaces.
    # raw_input() récupère la saisie complète de l'utilisateur en tant que chaîne.
    # .strip() supprime les espaces et les sauts de ligne en trop au début et à la fin de la chaîne.
    # .split(' ') divise la chaîne en une liste, en utilisant le caractère espace comme séparateur.
    # set(...) convertit cette liste en un ensemble (set), c'est-à-dire une collection qui ne contient que des éléments uniques.
    s = set(raw_input().strip().split(' '))

    # Demande à l'utilisateur la longueur de la seconde liste de mots, lit la chaîne fournie mais ne l'utilise pas.
    t_length = raw_input()
    
    # Récupère la seconde liste de mots auprès de l'utilisateur, puis la convertit directement :
    # - Lecture avec raw_input()
    # - Nettoyage avec .strip()
    # - Découpage en mots individuels avec .split(' ')
    # - Conversion en set pour obtenir les mots uniques.
    t = set(raw_input().strip().split(' '))

    # Calcule l'intersection des deux ensembles, c'est-à-dire l'ensemble des éléments présents à la fois dans s et dans t.
    # L'opérateur & est utilisé pour trouver les éléments communs entre deux ensembles.
    # len(...) calcule la taille, c'est-à-dire le nombre d'éléments de l'ensemble issu de cette intersection.
    # print affiche le nombre d'éléments communs à l'écran.
    print len(s & t)

# Le code suivant vérifie si le fichier est exécuté comme un programme principal et non importé comme module.
# __name__ est une variable spéciale qui prend la valeur '__main__' uniquement lorsque le fichier est le script principal.
if __name__ == '__main__':
    # Appelle la fonction main définie ci-dessus.
    main()