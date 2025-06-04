from operator import itemgetter

def read_input():
    """
    Lis les entrées utilisateur pour obtenir les valeurs de N et M, ainsi que la liste des paires AB.
    N : nombre de types d'objets ou de transactions disponibles.
    M : nombre total d'objets à choisir ou quantité souhaitée.
    AB : liste de N sous-listes, chacune contenant deux entiers :
         AB[i][0] : coût unitaire ou prix pour l’i-ème objet/transaction.
         AB[i][1] : quantité disponible pour l’i-ème objet/transaction.
    Returns:
        N (int): nombre d’éléments/transactions.
        M (int): quantité totale à acquérir.
        AB (list of list of int): liste des coûts unitaires et quantités disponibles.
    """
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    return N, M, AB

def min_total_cost(N, M, AB):
    """
    Calcule le coût minimum pour acquérir une quantité totale M en choisissant parmi N types d’objets,
    chacun ayant un coût unitaire et une quantité disponible. Les objets sont triés en fonction de leur coût
    unitaire croissant pour minimiser le coût total.

    Args:
        N (int): nombre de types d’objets/transactions.
        M (int): quantité totale d’objets à acquérir.
        AB (list of list of int): chaque élément [prix unitaire, quantité disponible].

    Returns:
        int: le coût total minimum pour acquérir M objets.
    """
    # Trie les objets/lignes selon leur coût unitaire (clé = premier élément de chaque sous-liste)
    AB.sort(key=itemgetter(0))

    total_cost = 0  # Initialisation du coût total

    # Parcours chaque objet/transaction dans l’ordre des coûts croissants
    for i in range(N):
        price_per_unit = AB[i][0]   # Coût unitaire pour le type i
        available_units = AB[i][1]  # Quantité disponible pour le type i

        if available_units >= M:
            # Si la quantité disponible suffit à satisfaire la demande restante,
            # achète seulement ce qui manque et quitte la boucle
            total_cost += price_per_unit * M
            return total_cost
        else:
            # Sinon, achète toute la quantité disponible et soustrait du reste à acquérir
            M -= available_units
            total_cost += price_per_unit * available_units

    # Si la boucle se termine ici, cela signifie que tous les objets/transactions ont été utilisés
    return total_cost

def main():
    """
    Fonction principale qui exécute la lecture des entrées, le calcul du coût et l'affichage du résultat.
    """
    N, M, AB = read_input()
    result = min_total_cost(N, M, AB)
    print(result)

# Appelle la fonction principale si ce script est exécuté directement
if __name__ == '__main__':
    main()