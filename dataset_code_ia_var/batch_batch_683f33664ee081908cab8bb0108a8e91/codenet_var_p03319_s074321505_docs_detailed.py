def calculate_minimum_steps(N, K):
    """
    Calcule le nombre minimum d'étapes nécessaires pour parcourir une suite de N éléments
    en avançant jusqu'à K éléments par étape, sauf pour la première position.
    
    Args:
        N (int): Le nombre total d'éléments/allers à parcourir.
        K (int): Le nombre maximum d'éléments parcourus en une étape (au-delà du premier).
    
    Returns:
        int: Le nombre minimal d'étapes nécessaires pour parcourir tous les éléments.
    """
    # Le déplacement commence à la première position, puis avance de (K-1) pas à chaque étape.
    # On calcule le nombre d'avancées nécessaires pour couvrir les (N-1) positions restantes.
    ans = (N - 1) // (K - 1)  # Division entière pour le nombre minimal d'étapes complètes
    if (N - 1) % (K - 1) != 0:
        # Si division non exacte, il reste des positions à couvrir, donc une étape supplémentaire
        ans += 1
    return ans

# Lecture des entrées utilisateur
N, K = map(int, input().split())
a = input()  # Lecture de la chaîne d'entrée, inutilisée dans le calcul (peut être une liste d'éléments)

# Calcul et affichage du résultat
print(calculate_minimum_steps(N, K))