# Solution au problème Maximum Sum Sequence en Python
# Le but est de trouver la somme maximale d'une sous-séquence contiguë dans une séquence donnée.
# La technique utilisée est l'algorithme de Kadane qui résout ce problème en O(n).
# Entrées multiples jusqu'à ce qu'une ligne contenant 0 soit rencontrée.

def max_sum_subsequence(arr):
    """
    Calcule la somme maximale d'une sous-séquence contiguë dans la liste arr.
    Utilisation de l'algorithme de Kadane.
    """
    max_ending_here = arr[0]  # somme max se terminant à la position actuelle
    max_so_far = arr[0]       # somme max trouvée jusqu'ici
    for x in arr[1:]:
        # Met à jour la somme max se terminant ici:
        # Soit on commence une nouvelle sous-séquence à x, soit on continue l'actuelle
        max_ending_here = max(x, max_ending_here + x)
        # Met à jour la somme max globale
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

def main():
    import sys
    input_lines = sys.stdin.read().strip().split('\n')
    idx = 0
    while True:
        if idx >= len(input_lines):
            break
        n_line = input_lines[idx].strip()
        idx += 1
        if n_line == '0':  # Fin de tous les datasets
            break
        n = int(n_line)
        
        # Lire les n nombres suivants
        arr = []
        for _ in range(n):
            arr.append(int(input_lines[idx].strip()))
            idx += 1
        
        # Calculer et afficher la somme maximale
        print(max_sum_subsequence(arr))

if __name__ == "__main__":
    main()