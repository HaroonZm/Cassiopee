def compute_optimal_bst_expected_cost(num_nodes, P, Q):
    """
    Calcule le coût espéré du meilleur arbre de recherche binaire (BST) pour 
    une séquence de n clés, avec probabilités d'accès pondérées pour les clés (P)
    et les échecs/intervalles (Q), en utilisant la programmation dynamique optimisée.

    Args:
        num_nodes (int): Nombre de clés dans le BST.
        P (list of float): Liste des probabilités d'accès aux n clés.
        Q (list of float): Liste des probabilités d'accès aux n+1 intervalles (entre les clés).

    Returns:
        float: Coût espéré minimal d'une recherche dans le BST optimal.
    """
    # Matrice Depth : Depth[i][j] mémorise l'indice de racine optimal pour la sous-séquence (i, j)
    Depth = [[0] * (num_nodes + 1) for _ in range(num_nodes + 1)]
    # Matrice Exp : Exp[i][j] stocke le coût espéré minimal pour la sous-séquence (i, j)
    Exp = [[0.0] * (num_nodes + 1) for _ in range(num_nodes + 1)]
    # Cum_prob : tableau stockant la somme cumulée des probabilités P et Q pour éviter de recalculer à chaque itération
    Cum_prob = [0.0] * (2 * num_nodes + 2)

    # Calcul des sommes cumulées des probabilités P (pour les clés) et Q (pour les échecs)
    for i in range(2 * num_nodes + 1):
        if i % 2 == 0:
            # Q occupent les indices pairs
            Cum_prob[i + 1] = Cum_prob[i] + Q[i // 2]
        else:
            # P occupent les indices impairs
            Cum_prob[i + 1] = Cum_prob[i] + P[i // 2]

    # Initialisation des cas de base :
    # Pour chaque intervalle vide (i == j), coût = Q[i], racine fictive = i
    for i in range(num_nodes + 1):
        Exp[i][i] = Q[i]
        Depth[i][i] = i

    # Remplissage dynamique pour chaque longueur d'intervalle l de 1 à n
    for l in range(1, num_nodes + 1):
        for i in range(num_nodes + 1 - l):
            j = i + l
            # Optimisation de Knuth : la racine optimale pour (i, j) se trouve entre les racines optimales des sous-arbres gauches et droits
            d0 = Depth[i][j - 1]      # Bornes inférieures de recherche pour la racine
            d1 = Depth[i + 1][j]      # Bornes supérieures de recherche pour la racine
            min_k = -1                # Racine optimale pour l'intervalle (i, j)
            min_cost = float('inf')   # Coût minimal initialisé à l'infini

            # Recherche de la racine optimale dans la tranche d0 à d1 (inclusivement)
            for k in range(d0, min(d1 + 1, j)):
                # Coût pour choisir k comme racine = coût gauche + coût droite
                cost = Exp[i][k] + Exp[k + 1][j]
                if cost < min_cost:
                    min_k = k
                    min_cost = cost

            # Stockage de la racine optimale et du coût pour l'intervalle (i, j)
            Depth[i][j] = min_k
            # Ajout de la somme de probabilités des clés/échecs dans l'intervalle (i, j) au coût partiel
            Exp[i][j] = min_cost + Cum_prob[2 * j + 1] - Cum_prob[2 * i]

    # Retourne le coût espéré minimal global pour toutes les clés (intervalle [0, n])
    return Exp[0][num_nodes]


def main():
    """
    Point d'entrée du programme.
    Lit les entrées, prépare les tableaux de probabilités et imprime 
    le coût espéré minimal du BST optimal sous format à cinq décimales.
    """
    # Lecture du nombre de clés depuis l'entrée standard
    num_nodes = int(input())
    # Lecture et conversion des probabilités d'accès aux clés P
    P = list(map(float, input().split()))
    # Lecture et conversion des probabilités d'accès aux intervalles Q
    Q = list(map(float, input().split()))
    # Calcul et affichage du coût optimal avec cinq décimales
    expected_cost = compute_optimal_bst_expected_cost(num_nodes, P, Q)
    print(f"{expected_cost:.5f}")


if __name__ == "__main__":
    main()