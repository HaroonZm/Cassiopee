# On utilise une approche de type "fenêtre glissante" (sliding window) pour résoudre ce problème efficacement.
# L'idée est de maintenir deux indices (début et fin de la sous-partie) et d'ajuster la fenêtre pour trouver 
# la sous-partie la plus petite avec une somme >= S.
#
# Complexité : O(N), où N est la taille du tableau, car chaque élément est visité au plus deux fois (une fois en entrant dans la fenêtre, 
# et une fois en sortant).
#
# Étapes :
# 1. Initialiser deux indices, start et end, à 0, et une variable current_sum à 0.
# 2. Avancer 'end' en ajoutant a[end] à current_sum.
# 3. Tant que current_sum >= S, on met à jour la taille minimale de la fenêtre, et on retire a[start] de current_sum, puis on incrémente start.
# 4. Répéter jusqu'à ce que end atteigne la fin du tableau.
# 5. Si aucune fenêtre valide n'a été trouvée, retourner 0.

def smallest_window_size(N, S, arr):
    start = 0
    current_sum = 0
    min_length = N + 1  # Un nombre plus grand que la taille maximale possible
    
    for end in range(N):
        current_sum += arr[end]  # Ajouter l'élément courant à la somme
        
        # Réduire la fenêtre tant que la somme est suffisante pour essayer de minimiser la taille
        while current_sum >= S:
            # Mettre à jour la longueur minimale trouvée
            current_length = end - start + 1
            if current_length < min_length:
                min_length = current_length
            # Retirer l'élément start de la somme et avancer start pour rétrécir la fenêtre
            current_sum -= arr[start]
            start += 1
    
    # Si aucune sous-partie valide n'a été trouvée, retourner 0
    if min_length == N + 1:
        return 0
    else:
        return min_length

# Lecture des entrées
def main():
    N, S = map(int, input().split())
    arr = list(map(int, input().split()))
    result = smallest_window_size(N, S, arr)
    print(result)

if __name__ == "__main__":
    main()