import sys
import math

def main():
    # Lecture de l'entrée : un entier N
    N = int(sys.stdin.readline().strip())

    # Étape 1 : Créer un tableau pour tester la primalité jusqu'à N (même si N peut être grand)
    # On utilisera le crible d'Ératosthène, efficace pour N <= 10^7
    sieve = [True] * (N + 1)
    sieve[0] = False
    sieve[1] = False

    # Crible d'Ératosthène pour identifier les nombres premiers <= N
    for i in range(2, int(math.sqrt(N)) + 1):
        if sieve[i]:
            for j in range(i * i, N + 1, i):
                sieve[j] = False

    # Récupérer la liste des nombres premiers <= N
    primes = [i for i in range(2, N+1) if sieve[i]]

    # Étape 2 : Préparer un crible pour tester la primalité jusqu'à 2 * N,
    # car p + q peut aller jusqu'à 2N
    max_sum = 2 * N
    sieve_sum = [True] * (max_sum + 1)
    sieve_sum[0] = False
    sieve_sum[1] = False
    for i in range(2, int(math.sqrt(max_sum)) + 1):
        if sieve_sum[i]:
            for j in range(i * i, max_sum + 1, i):
                sieve_sum[j] = False

    # Étape 3 : Compter les p, q (primes <= N) tels que p + q est premier
    # Le problème ne spécifie pas que p <= q, ou que la paire est unique, donc on compte toutes les p,q
    # Il y a potentiellement beaucoup de p,q, donc il faut être efficace.
    # Une solution efficace est d'utiliser un hash set pour les primes, et pour chaque p, vérifier q dans primes
    # Toutefois, ça donnerait O(#primes^2) ~ trop lent pour N=10^7.

    # Une solution optimisée :
    # - convertir la liste primes en un set pour recherche rapide
    # - pour chaque p dans primes:
    #   - on veut compter le nombre de q dans primes tel que p+q est premier
    # Puisque primes est ordonné, on peut utiliser deux indices en style "two pointers"
    # Mais il faut compter tous les couples (p,q), ordre compte (car dans l'exemple (2,3) et (3,2) sont comptés)

    # On peut parcourir tous p,q avec p,q dans primes, p et q <= N
    # Max #primes ~664579 pour N=10^7
    # La doublure O(#primes^2) est trop grande.
    # On doit trouver une autre approche.

    # Observons la contrainte : Si on crée un tableau "prime_flag" pour les nombres jusqu'à N,
    # ensuite on prépare un tableau "count_prime_sum" pour les nombres jusqu'à 2N qui compte
    # combien de façons la somme s peut être écrite comme p+q avec p,q premiers <= N
    # Mais ça demande O(N^2), impossible.

    # Alternative efficace: On peut compter en utilisant la convolution (par exemple FFT),
    # mais la FFT est compliquée ici et pas demandée.

    # Alternative astucieuse:
    # Les sommes p+q sont uniquement dans [4, 2N], avec p,q premiers <= N
    # On peut représenter les premiers par un tableau binaire "A" de taille N+1 où A[x]=1 si x premier sinon 0
    # Le nombre de façons d'écrire s = somme des produits A[p]*A[s-p] pour p dans [2,s-2]
    # Cela correspond à la convolution de A par elle-même, évaluée en s.

    # En Python, on peut faire cette convolution avec numpy FFT, en précisant suffisamment de précision.
    # Cela permet d'obtenir en O(N log N) le nombre de p,q tels que p+q = s.

    import numpy as np

    A = np.array(sieve, dtype=np.int64)
    # taille pour la FFT, puissance de deux > 2N+1
    size = 1 << (2 * N).bit_length()
    # FFT rapide pour entiers
    FA = np.fft.fft(A, size)
    # Convolution = produit point par point
    FC = FA * FA
    # transformée inverse
    conv = np.fft.ifft(FC).real.round().astype(np.int64)

    # conv[s] = nombre de p,q tels que p+q=s avec p,q premiers <= N

    # Étape 4 : Compter la somme des conv[s] pour les s premiers (s premiers entiers)
    # mais on veut compter uniquement les p,q tel que p+q est premier
    # Donc on compte pour tous s <= 2N où s est premier, la valeur conv[s]

    # conv est de taille size, on regarde indices jusqu'à 2N
    result = 0
    for s in range(2, 2*N+1):
        if sieve_sum[s]:
            # conv[s] peut être très grand, il représente le nombre de p,q premiers <= N avec p+q=s
            result += conv[s]

    # Affichage du résultat : nombre de p,q avec p,q<=N premiers et p+q premiers
    print(result)

if __name__ == "__main__":
    main()