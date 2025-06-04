from itertools import accumulate

def max_k_satisfying_condition(N, A):
    """
    Calcule le plus grand index k (0-based) pour lequel l'élément B_{k+1} de la liste triée B
    vérifie la condition : B_{k+1} > 2(B_1 + ... + B_k).
    
    Args:
        N (int): Le nombre d'éléments dans la liste A.
        A (List[int]): La liste des valeurs entières à traiter.
        
    Returns:
        int: Le résultat final correspondant à N - k, où k est le plus grand indice satisfaisant la condition.
    """
    # Étape 1 : Tri de la liste A en ordre croissant pour obtenir la liste B.
    B = sorted(A)
    
    # Étape 2 : Calcul des sommes cumulées pour B, avec un décalage de 0 au début pour gérer S[0] = 0.
    # S[i] va représenter la somme de B_0 à B_{i-1}.
    S = list(accumulate([0] + B))
    
    # Étape 3 : Parcours de k de N-1 à 0 (inversé) pour trouver le plus grand k tel que
    # B[k] > 2 * S[k].
    # On utilise next(...) pour s'arrêter à la première valeur trouvée en commençant par la fin.
    for i in reversed(range(N)):
        if B[i] > 2 * S[i]:
            max_k = i
            break
    
    # Le résultat attendu est N - k lorsque la condition est vérifiée.
    ans = N - max_k
    return ans

def main():
    """
    Fonction principale pour gérer les entrées et sorties liées à la résolution du problème.
    """
    # Lecture du nombre d'éléments
    N = int(input())
    # Lecture de la liste d'entiers séparés par des espaces
    A = list(map(int, input().split()))
    
    # Appel de la fonction principale de traitement et affichage du résultat
    print(max_k_satisfying_condition(N, A))

# Point d'entrée du script
if __name__ == "__main__":
    main()