def count_mutual_pairs(n, a):
    """
    Compte le nombre de paires mutuelles dans une permutation donnée.
    
    Une paire mutuelle est définie comme deux indices i et j tels que a[a[i]] == i,
    chaque paire n'est comptée qu'une seule fois.
    
    Args:
        n (int): La taille de la permutation.
        a (list of int): Une liste contenant la permutation, indexée à partir de 1.
        
    Returns:
        int: Le nombre de paires mutuelles trouvées.
    """
    # Initialiser le compteur pour les paires mutuelles.
    ans = 0

    # Parcourir chaque indice de 1 à n inclusivement.
    for i in range(1, n + 1):
        # Vérifier si la paire (i, a[i]) est mutuelle et n'a pas déjà été comptée.
        if a[a[i]] == i:
            ans += 1  # Incrémenter le compteur de paires mutuelles.
            a[a[i]] = 0  # Marquer l'élément comme utilisé pour éviter les doubles comptages.
    return ans

def main():
    """
    Fonction principale pour lire l'entrée utilisateur, exécuter le comptage, et afficher le résultat.
    """
    # Lire le nombre d'éléments de la permutation.
    n = int(input())

    # Lire la permutation en tant que liste d'entiers, ajouter 0 au début pour l'indexation à partir de 1.
    a = [0] + list(map(int, input().split()))

    # Appeler la fonction pour compter les paires mutuelles et afficher le résultat.
    print(count_mutual_pairs(n, a))

if __name__ == '__main__':
    main()