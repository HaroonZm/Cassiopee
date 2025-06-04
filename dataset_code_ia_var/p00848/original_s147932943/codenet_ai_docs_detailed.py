def generate_primes(limit):
    """
    Génère une liste de nombres premiers jusqu'à une limite donnée incluse.

    Args:
        limit (int): La borne supérieure (incluse) jusqu'à laquelle générer les nombres premiers.

    Returns:
        list: Une liste contenant tous les nombres premiers entre 2 et limit inclus.
    """
    primes = []
    for i in range(2, limit + 1):
        is_prime = True
        # Vérifie la primalité en testant les diviseurs jusqu'à la racine carrée de i
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes

def build_dp_table(primes, max_k, max_sum):
    """
    Construit une table DP pour compter les représentations d'un nombre comme somme
    de k nombres premiers distincts.

    Args:
        primes (list): Liste des nombres premiers dont on dispose.
        max_k (int): Nombre maximum de termes (nombres premiers) dans la somme.
        max_sum (int): Somme maximale possible à atteindre.

    Returns:
        list: Table DP où dp[k][n] représente le nombre de façons d'écrire n comme
              somme de k nombres premiers distincts.
    """
    # Initialisation de la table DP remplie de zéros
    dp = [[0] * (max_sum + 1) for _ in range(max_k + 1)]
    dp[0][0] = 1  # Une façon de faire la somme 0 avec 0 terme

    # Remplissage de la table en considérant chaque nombre premier
    for idx, prime in enumerate(primes):
        # On itère à rebours sur le nombre de termes pour éviter les doubles comptes
        for k in range(min(idx + 1, max_k), 0, -1):
            for s in range(prime, max_sum + 1):
                # Ajoute le nombre de solutions en utilisant prime dans la somme
                dp[k][s] += dp[k - 1][s - prime]
    return dp

def main():
    """
    Fonction principale qui gère la lecture des entrées et affiche les résultats attendus.
    Permet de déterminer pour chaque couple (n, k) le nombre de façons d'écrire n comme
    somme de k nombres premiers distincts.
    """
    # Génération des nombres premiers jusqu'à 1120 inclus, comme dans le code original
    primes = generate_primes(1120)
    # Construction de la table DP pour au plus 14 termes et une somme maximale de 1120
    dp = build_dp_table(primes, 14, 1120)

    while True:
        # Lecture des entrées séparées par un espace
        n, k = map(int, input().split())
        if n == 0:
            break
        # Affichage du nombre de façons de représenter n comme somme de k nombres premiers distincts
        print(dp[k][n])

# Lancement du programme principal
if __name__ == '__main__':
    main()