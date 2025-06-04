def read_input():
    """
    Lit les entrées standard pour obtenir la taille et les paires.

    Returns:
        int: Le nombre de paires N.
        list of list of int: La liste des paires P sous forme [[a1, b1], [a2, b2], ..., [aN, bN]].
    """
    N = int(input())
    P = [list(map(int, input().split())) for _ in range(N)]
    return N, P

def process_pairs(P):
    """
    Calcule la valeur maximale selon la règle (su + b - a - S), où S est la valeur minimale rencontrée de (su - a).

    Args:
        P (list of list of int): Liste des paires, chaque paire étant de la forme [a, b] et triée sur a.

    Returns:
        int: La valeur maximale calculée selon la règle donnée.
    """
    # Initialisation des variables
    su = 0   # Somme cumulée de tous les b rencontrés jusqu'à présent
    S = -P[0][0]  # Initialisation de S avec l'opposé du premier a
    ans = -10**19 # Initialisation de la réponse maximale à une très petite valeur

    # Parcourir chaque paire triée
    for a, b in P:
        # Mettre à jour S avec le minimum entre S et (su - a) courant
        S = min(S, su - a)
        # Calcul de la valeur et mise à jour de la réponse maximale
        ans = max(ans, su + b - a - S)
        # Mettre à jour la somme cumulée de b
        su += b

    return ans

def main():
    """
    Fonction principale qui gère l'exécution complète de la logique :
    - Lecture de l'entrée
    - Tri des paires par ordre croissant de a
    - Calcul de la réponse
    - Affichage du résultat
    """
    # Lecture de l'entrée utilisateur
    N, P = read_input()
    # Trier les paires en fonction de leur premier élément (a)
    P.sort()
    # Exécuter l'algorithme de calcul principal
    answer = process_pairs(P)
    # Afficher le résultat calculé
    print(answer)

if __name__ == "__main__":
    main()