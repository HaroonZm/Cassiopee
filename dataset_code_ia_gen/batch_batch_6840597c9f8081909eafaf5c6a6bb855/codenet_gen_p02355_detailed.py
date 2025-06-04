# Solution Python pour le problème "The Smallest Window II"
# L'objectif est de trouver la taille minimale d'une sous-partie continue du tableau contenant tous les entiers de 1 à K.
# Si aucun segment ne contient tous ces éléments, on retourne 0.

def smallest_window_with_all_k_elements(N, K, arr):
    # Si K est plus grand que N, il est impossible de trouver un tel sous-tableau
    if K > N:
        return 0
    
    # On utilise deux pointeurs pour délimiter une fenêtre glissante
    left = 0
    min_length = float('inf')  # On cherche à minimiser cette valeur
    
    # Dictionnaire pour compter combien de fois chaque entier de 1..K apparaît dans la fenêtre actuelle
    count = {}
    
    # Nombre d'entiers distincts rencontrés dans la fenêtre (qui appartiennent à l'intervalle 1..K)
    distinct_count = 0
    
    for right in range(N):
        # Si l'élément est dans la plage [1..K], on met à jour son compte
        if 1 <= arr[right] <= K:
            count[arr[right]] = count.get(arr[right], 0) + 1
            # Si c'est la première fois que cet entier apparait dans la fenêtre, on augmente distinct_count
            if count[arr[right]] == 1:
                distinct_count += 1
        
        # Quand la fenêtre contient tous les entiers de 1..K, on essaie de la réduire à gauche
        while distinct_count == K:
            # Mettre à jour la taille minimale si nécessaire
            current_length = right - left + 1
            if current_length < min_length:
                min_length = current_length
            
            # On va réduire la fenêtre à gauche, on doit mettre à jour les comptes
            if 1 <= arr[left] <= K:
                count[arr[left]] -= 1
                # Si en enlevant cet élément on perd un entier, on réduit distinct_count
                if count[arr[left]] == 0:
                    distinct_count -= 1
            left += 1
    
    # Si on n'a jamais trouvé une fenêtre contenant tous les entiers 1..K, retourner 0
    if min_length == float('inf'):
        return 0
    else:
        return min_length


# Lecture des entrées
N, K = map(int, input().split())
arr = list(map(int, input().split()))

# Calcul et affichage du résultat
print(smallest_window_with_all_k_elements(N, K, arr))