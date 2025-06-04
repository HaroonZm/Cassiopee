def bubble_sort(num_list):
    """
    Trie une liste de nombres en utilisant l'algorithme de tri à bulles.

    Args:
        num_list (list of int): Liste des entiers à trier.

    Returns:
        tuple: Une paire contenant :
            - La liste triée (list of int)
            - Le nombre total de permutations effectuées (int)
    """
    # Déterminer l'indice maximal pour les comparaisons.
    list_length = len(num_list) - 1
    # Compteur pour le nombre total d'inversions (permutations).
    cnt = 0

    # Boucle sur les passes nécessaires (n-1 passes).
    for i in range(list_length):
        # Parcourt la liste de la fin vers l'élément i+1.
        for j in range(list_length, i, -1):
            # Si l'élément courant est inférieur à l'élément précédent, on les échange.
            if num_list[j] < num_list[j - 1]:
                num_list[j], num_list[j - 1] = num_list[j - 1], num_list[j]
                cnt += 1  # Incrémente le nombre de permutations effectuées.
    # Retourne la liste triée et le nombre de permutations.
    return num_list, cnt

def main():
    """
    Fonction principale qui lit les entrées, effectue le tri à bulles,
    puis affiche la liste triée et le nombre de permutations.
    """
    # Lit la taille de la liste depuis l'entrée standard (non utilisé, pour conformité).
    n = int(input())
    # Lit la liste des nombres séparés par un espace puis la convertit en entiers.
    num_list = list(map(int, input().split()))
    # Trie la liste et récupère le nombre de permutations.
    ans_list, cnt = bubble_sort(num_list)
    # Convertit chaque entier de la liste triée en chaîne de caractères pour l'affichage.
    str_ans_list = [str(i) for i in ans_list]
    # Affiche la liste triée, les éléments séparés par un espace.
    print(' '.join(str_ans_list))
    # Affiche le nombre total de permutations effectuées.
    print(cnt)

if __name__ == "__main__":
    main()