def main():
    # Demander à l'utilisateur de saisir un entier et le convertir en int : c'est la valeur de X11 (première ligne, première colonne)
    X11 = int(input())
    # Demander à l'utilisateur de saisir un entier et le convertir en int : c'est la valeur de X12 (première ligne, deuxième colonne)
    X12 = int(input())
    # Demander à l'utilisateur de saisir un entier et le convertir en int : c'est la valeur de X22 (deuxième ligne, deuxième colonne, au centre)
    X22 = int(input())
    # Initialiser X13 (première ligne, troisième colonne) à 0 avant de commencer la recherche
    X13 = 0

    # Utiliser une boucle infinie (while True) qui sera interrompue par un break si la solution est trouvée
    while True:
        # Pour chaque tour de boucle, on considère que la somme cible 'v' est la somme de la première ligne :
        # v = X11 (1ère ligne, 1ère colonne) + X12 (1ère ligne, 2ème colonne) + X13 (1ère ligne, 3ème colonne)
        v = X11 + X12 + X13

        # Calcul de X31 (3ème ligne, 1ère colonne) en utilisant la somme de la diagonale secondaire :
        # sur la diagonale secondaire : X13 (1ère ligne, 3ème colonne), X22 (2ème ligne, 2ème colonne), et X31 (3ème ligne, 1ère colonne)
        # Leur somme doit aussi faire v.
        # Donc : X13 + X22 + X31 = v  =>  X31 = v - X13 - X22
        X31 = v - X13 - X22

        # Calcul de X21 (2ème ligne, 1ère colonne) à partir de la première colonne :
        # La première colonne : X11 (1ère ligne), X21 (2ème ligne), X31 (3ème ligne)
        # Leur somme doit faire v : X11 + X21 + X31 = v
        # Donc : X21 = v - X11 - X31
        X21 = v - X11 - X31

        # Calcul de X23 (2ème ligne, 3ème colonne) à partir de la deuxième ligne :
        # Deuxième ligne : X21 (2ème ligne, 1ère colonne), X22 (centre), X23 (2ème ligne, 3ème colonne)
        # Leur somme doit être v : X21 + X22 + X23 = v
        # Donc : X23 = v - X21 - X22
        X23 = v - X21 - X22

        # Calcul de X33 (3ème ligne, 3ème colonne) à partir de la troisième colonne :
        # Troisième colonne : X13 (1ère ligne, 3ème colonne), X23 (2ème ligne, 3ème colonne), X33 (3ème ligne, 3ème colonne)
        # Leur somme doit être v : X13 + X23 + X33 = v
        # Donc : X33 = v - X13 - X23
        X33 = v - X13 - X23

        # Calcul de X32 (3ème ligne, 2ème colonne) à partir de la deuxième colonne :
        # Deuxième colonne : X12 (1ère ligne, 2ème colonne), X22 (2ème ligne, 2ème colonne), X32 (3ème ligne, 2ème colonne)
        # Leur somme doit être v : X12 + X22 + X32 = v
        # Donc : X32 = v - X12 - X22
        X32 = v - X12 - X22

        # Vérifier que la somme de la troisième ligne (X31 + X32 + X33) est bien égale à v
        # ET que la diagonale principale (X11 + X22 + X33) est aussi égale à v
        # Cela garantit qu'on a un carré magique valide (pour la configuration imposée)
        if X31 + X32 + X33 == v and X11 + X22 + X33 == v:
            # Afficher la première ligne du carré magique. Utiliser map(str, ...) pour convertir chaque élément en chaîne.
            # Utiliser " ".join(...) pour obtenir une chaine avec les éléments séparés par des espaces.
            print(" ".join(map(str, [X11, X12, X13])))
            # Afficher la deuxième ligne du carré magique
            print(" ".join(map(str, [X21, X22, X23])))
            # Afficher la troisième ligne du carré magique
            print(" ".join(map(str, [X31, X32, X33])))
            # Interrompre (quitter) la boucle, car on a trouvé une solution
            break

        # Si on n'a pas encore trouvé une solution valide, on incrémente X13 (case première ligne, troisième colonne)
        # et on recommence la recherche avec cette nouvelle valeur.
        X13 += 1

# Ceci permet d'exécuter la fonction main() uniquement si le script est lancé directement
# '__name__' est une variable spéciale en Python : elle vaut '__main__' lorsque le script est exécuté
if __name__ == '__main__':
    # Appel à la fonction main définie ci-dessus pour démarrer le programme
    main()