def main():
    """
    Fonction principale pour calculer l'intersection de deux ensembles d'entrées saisis par l'utilisateur.

    Elle demande à l'utilisateur d'entrer deux listes d'éléments (par exemple, des entiers sous forme de chaînes),
    puis affiche le nombre d'éléments communs aux deux ensembles.
    """
    # Lire le nombre d'éléments du premier ensemble (non utilisé par la suite, mais gardé pour conformité)
    n = input()
    # Lire les éléments du premier ensemble, les séparer par des espaces puis les convertir en ensemble
    set_n = set(raw_input().split())

    # Lire le nombre d'éléments du second ensemble (non utilisé par la suite, mais gardé pour conformité)
    q = input()
    # Lire les éléments du second ensemble, les séparer par des espaces puis les convertir en ensemble
    set_q = set(raw_input().split())

    # Calculer l'intersection des deux ensembles (éléments communs)
    answer = set_n & set_q

    # Afficher le nombre d'éléments dans l'intersection
    print(len(answer))

if __name__ == "__main__":
    main()