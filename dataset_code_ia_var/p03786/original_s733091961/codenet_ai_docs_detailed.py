def read_input():
    """
    Lit les entrées utilisateur.
    Retourne :
        n (int) : Le nombre d'éléments dans la liste.
        A (List[int]) : La liste triée des entiers fournie par l'utilisateur.
    """
    n = int(input())
    # Lecture et conversion des valeurs, puis tri de la liste.
    A = sorted(list(map(int, input().split())))
    return n, A

def compute_suffix_cumsum(A):
    """
    Calcule et retourne la somme cumulée suffixée (de droite à gauche) d'une liste.
    Arguments :
        A (List[int]) : Liste d'entiers.
    Retourne :
        cumsum (List[int]) : Liste des sommes cumulées suffixées, la première valeur est la somme totale.
    """
    from itertools import accumulate
    # Effectue une somme cumulative classique, puis inverse l'ordre pour obtenir la somme suffixée.
    cumsum = list(reversed(list(accumulate(A))))
    return cumsum

def count_elements_satisfying_condition(A, cumsum):
    """
    Compte le nombre maximal d'éléments consécutifs à partir de la fin de la liste A
    vérifiant la condition : chaque élément <= 2 * (somme des éléments suivants).
    Arguments :
        A (List[int]) : Liste triée d'entiers.
        cumsum (List[int]) : Liste des sommes cumulées suffixées.
    Retourne :
        ans (int) : Nombre d'éléments consécutifs satisfaisant la condition depuis la fin.
    """
    ans = 1  # Au moins le dernier élément compte toujours
    # Parcours simultané de A inversée (sauf le dernier élément), et cumsum en décalant d'un vers la droite
    for a, cs in zip(reversed(A), cumsum[1:]):
        # Si l'élément est au plus le double de la somme des suivants, on l'inclut
        if a <= 2 * cs:
            ans += 1
        else:
            # Si la condition échoue, on arrête immédiatement
            break
    return ans

def main():
    """
    Fonction principale orchestrant la lecture des entrées, le calcul de la somme cumulée suffixée,
    le comptage des éléments satisfaisant la condition, puis affichant le résultat.
    """
    n, A = read_input()  # Lecture des entrées
    cumsum = compute_suffix_cumsum(A)  # Calcul des sommes cumulées suffixées
    ans = count_elements_satisfying_condition(A, cumsum)  # Comptage selon la condition donnée
    print(ans)  # Affichage du résultat

if __name__ == "__main__":
    main()