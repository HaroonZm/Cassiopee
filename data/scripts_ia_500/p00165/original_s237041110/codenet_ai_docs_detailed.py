from itertools import accumulate

MAX = 1000000

def sieve_of_eratosthenes(limit):
    """
    Génère une liste indiquant la primalité des nombres de 0 à limit - 1
    en utilisant le crible d'Ératosthène.
    
    Args:
        limit (int): La borne supérieure (exclusive) pour la génération des nombres premiers.
        
    Returns:
        list: Une liste de int où 1 signifie un nombre premier et 0 non premier.
    """
    # Initialisation d'une liste où on suppose que tous les nombres sont premiers (1),
    # sauf 0 et 1 qui ne sont pas premiers
    is_prime = [1] * limit
    is_prime[0] = is_prime[1] = 0
    
    # On n'a besoin de tester que jusqu'à la racine carrée de la limite
    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            # On marque comme non premiers tous les multiples de i à partir de i^2
            for j in range(i * i, limit, i):
                is_prime[j] = 0
    return is_prime

def main():
    """
    Fonction principale qui :
    - Calcule la liste des nombres premiers jusqu'à MAX grâce au crible d'Ératosthène.
    - Calcule la somme cumulée de ces valeurs de primalité pour un accès rapide.
    - Lit des entrées utilisateurs répétées jusqu'à réception d'un 0.
    - Calcule pour chaque cas la somme des nombres premiers dans des intervalles spécifiés.
    - Affiche le résultat pour chaque ensemble d'entrées.
    """
    # Génération de la liste des premiers avec le crible d'Ératosthène
    is_prime = sieve_of_eratosthenes(MAX)
    
    # Calcul de la somme cumulée des valeurs 0/1 de primalité
    # acc_prime[i] = nombre de nombres premiers <= i
    acc_prime = list(accumulate(is_prime))
    
    while True:
        # Lecture du nombre d'intervalles à traiter
        n = int(input())
        if n == 0:
            # Sortie de la boucle si la valeur entrée est 0
            break
        
        ans = 0  # Variable pour accumuler le résultat total
        
        for _ in range(n):
            # Lecture des bornes p et m pour chaque intervalle
            p, m = map(int, input().split())
            
            # Calcul du nombre de nombres premiers dans l'intervalle [p - m, p + m]
            # En utilisant la somme cumulée pour obtenir rapidement le résultat
            left_index = max(0, p - m - 1)       # borne gauche - 1 pour inclusion
            right_index = min(p + m, MAX - 1)    # borne droite limitée à MAX - 1
            
            # Calcul du nombre de premiers dans l'intervalle : différence des sommes cumulées
            # On soustrait également 1 pour exclure le nombre central p
            interval_prime_count = acc_prime[right_index] - acc_prime[left_index] - 1
            
            # On ajoute le résultat de cet intervalle au total
            ans += interval_prime_count
        
        # Affichage du résultat total pour cette série d'intervalles
        print(ans)

if __name__ == "__main__":
    main()