from itertools import accumulate

def read_input():
    """
    Lit les entrées utilisateur.
    Retourne :
        n (int) : nombre d'éléments dans la liste.
        a_list (list of int) : liste des entiers saisie par l'utilisateur.
    """
    n = int(input())
    a_list = list(map(int, input().split()))
    return n, a_list

def compute_cumulative_sum(a_list):
    """
    Calcule la somme cumulative (prefix sum) de la liste d'entrée.
    Args:
        a_list (list of int) : liste des entiers.
    Retourne :
        cumsum (list of int) : sommes cumulées de a_list.
    """
    return list(accumulate(a_list))

def build_cumulative_sum_counts(cumsum):
    """
    Construit un dictionnaire comptant les occurrences de chaque valeur de la somme cumulative.
    Le dictionnaire commence avec la clé 0 initialisée à 1 (pour le préfixe vide).
    Args:
        cumsum (list of int) : liste des sommes cumulées.
    Retourne :
        num_dict (dict) : dictionnaire associant chaque somme cumulative à son nombre d'occurrences.
    """
    num_dict = {0: 1}  # La somme cumulée 0 (avant le début de la liste) compte comme une occurrence
    for s in cumsum:
        if s in num_dict:
            num_dict[s] += 1
        else:
            num_dict[s] = 1
    return num_dict

def count_zero_sum_subarrays(num_dict):
    """
    Calcule le nombre de sous-tableaux dont la somme est nulle.
    Chaque paire d'indices ayant la même somme cumulative représente un sous-tableau de somme nulle.
    Args:
        num_dict (dict) : dictionnaire des occurrences de chacune des sommes cumulées.
    Retourne :
        res (int) : nombre total de sous-tableaux de somme nulle.
    """
    res = 0
    for count in num_dict.values():
        # Pour chaque somme cumulative apparaissant count fois,
        # le nombre de paires (i < j) possibles est count * (count-1) // 2
        res += count * (count - 1) // 2
    return res

def main():
    """
    Fonction principale. Exécute le processus de lecture d'entrée, de calcul des sommes cumulées,
    de construction du dictionnaire et de calcul du résultat final. Affiche le résultat.
    """
    n, a_list = read_input()
    cumsum = compute_cumulative_sum(a_list)
    num_dict = build_cumulative_sum_counts(cumsum)
    result = count_zero_sum_subarrays(num_dict)
    print(result)

if __name__ == "__main__":
    main()