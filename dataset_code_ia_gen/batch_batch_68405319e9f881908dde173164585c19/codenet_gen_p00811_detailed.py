import sys
import math

# Fonction pour générer la liste des nombres premiers jusqu'à une limite max
def sieve_of_eratosthenes(max_limit):
    # Initialisation d'une liste pour marquer les nombres premiers
    sieve = [True] * (max_limit + 1)
    sieve[0], sieve[1] = False, False  # 0 et 1 ne sont pas premiers
    for i in range(2, int(math.sqrt(max_limit)) + 1):
        if sieve[i]:
            for j in range(i*i, max_limit + 1, i):
                sieve[j] = False
    # Retourner la liste des nombres premiers sous forme d'une liste
    return [num for num, is_prime in enumerate(sieve) if is_prime]

# Lecture et traitement de chaque ligne d'entrée jusqu'à ce que la ligne "0 0 0" soit rencontrée
def main():
    # Limite maximale pour m
    MAX_M = 100000
    # Pré-calcul des nombres premiers jusqu'à MAX_M pour éviter de recalculer à chaque cas
    primes = sieve_of_eratosthenes(MAX_M)

    # Pour un accès rapide, transformation en set
    primes_set = set(primes)

    for line in sys.stdin:
        if line.strip() == "0 0 0":
            break
        m, a, b = map(int, line.strip().split())

        # Ratio minimal a/b (fraction)
        min_ratio = a / b  # 0 < a/b <= 1

        # La plupart des solutions utilisent p (width) <= q (height) ou inversement.
        # Puisque le ratio p/q est entre a/b et 1, on a p/q <= 1 => p <= q.
        # Donc on cherchera p et q avec p <= q.

        # On cherche les p et q premiers tels que:
        # p * q <= m
        # min_ratio <= p/q <= 1
        # p et q premiers
        # maximiser p * q.

        max_area = 0
        best_p = 2
        best_q = 2

        # Parcourir q dans la liste des premiers plus petits ou égaux à m
        # q >= p car p/q <= 1 avec p <= q
        # On parcourt q en ordre décroissant car on cherche un max d'aire
        # pour plus d'efficacité

        # Trouvons les indices dans primes pour q <= m
        # On parcourt q décroissant pour trouver max area rapidement
        # On arrêtera la boucle quand q*q < max_area car q*q est max possible avec p=q

        idx_q_max = 0
        # Trouve l'indice maximum de q <= m
        # primes est trié croissant
        # on utilise une recherche binaire
        left, right = 0, len(primes)-1
        while left <= right:
            mid = (left + right) // 2
            if primes[mid] <= m:
                idx_q_max = mid
                left = mid + 1
            else:
                right = mid -1

        # Parcourir q décroissant
        for i in range(idx_q_max, -1, -1):
            q = primes[i]
            # Si q*q < max_area connu, on peut arrêter la boucle
            if q * q < max_area:
                break
            # Calculer borne minimale pour p en fonction du ratio et de p <= q
            # On a a/b <= p/q <= 1 => p >= a*q/b
            p_min = math.ceil(min_ratio * q)
            # Chercher parmi les premiers p tel que:
            # p <= q (car p/q <= 1)
            # p >= p_min
            # p premier
            # p*q <= m
            # la plus grande aire possible.
            # On parcours p décroissant de q à p_min pour maximiser p*q
            # p doit être premier
            found_p = None
            for j in range(i, -1, -1):  # p dans les premiers <= q (indice i) en décroissant
                p = primes[j]
                if p < p_min:
                    break
                area = p * q
                if area <= m:
                    # area déjà <= m, vérifier si meilleur
                    if area > max_area:
                        max_area = area
                        best_p = p
                        best_q = q
                    break  # on a trouvé le plus grand p possible pour ce q
        print(best_p, best_q)

if __name__ == "__main__":
    main()