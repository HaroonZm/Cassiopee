def find_minimal_multiple(A, B):
    """
    Trouve le plus petit multiple de A supérieur à B pour lequel la somme
    des chiffres dans la représentation B-aire et A-aire et le reste dépasse le quotient k.

    Args:
        A (int): Le premier entier fourni par l'utilisateur, doit être positif.
        B (int): Le deuxième entier fourni par l'utilisateur.

    Returns:
        int: Le plus petit multiple valide de A répondant aux conditions, 
             ou -1 s'il n'existe pas dans la plage considérée.
    """
    # Si B est un multiple de A, il n'existe pas de solution valide
    if B % A == 0:
        return -1

    # Calcule l'entier minimal k tel que k*A > B. 
    # Ceci équivaut à l'arrondi plafond de B/A.
    _k = -(-B // A)

    # On parcourt les valeurs possibles de k à partir de _k jusqu'à _k + 10^7
    for k in range(_k, _k + 10**7):
        # Calcule la division euclidienne de k*A par B : bn est le quotient, rem est le reste
        bn, rem = divmod(k * A, B)
        # Décompose le reste (rem) en quotient et reste par A : an est le quotient, rem est le reste final
        an, rem = divmod(rem, A)
        # On somme tous les quotients et le reste
        n = bn + an + rem
        # Si cette somme est strictement supérieure à k, la condition est satisfaite
        if n > k:
            return k * A
    # Si aucune valeur ne satisfait la condition dans la plage donnée, retourne -1
    return -1

def main():
    """
    Fonction principale : lit deux entiers au clavier et affiche la réponse selon la logique du problème.
    """
    # Lecture et décomposition de l'entrée utilisateur
    A, B = map(int, input().split())

    # Recherche du plus petit multiple répondant à la condition donnée
    result = find_minimal_multiple(A, B)

    # Affiche le résultat, -1 si aucune solution
    print(result)

if __name__ == "__main__":
    main()