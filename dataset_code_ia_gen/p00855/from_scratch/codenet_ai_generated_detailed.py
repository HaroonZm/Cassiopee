import sys
import math

def sieve(n):
    """
    Génère un tableau booléen is_prime jusqu'à n inclus,
    indiquant si chaque nombre est premier ou non.
    Utilisation du crible d'Ératosthène pour efficacité.
    """
    is_prime = [True] * (n + 1)
    is_prime[0], is_prime[1] = False, False
    for i in range(2, int(math.sqrt(n)) + 1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    return is_prime

def prime_gaps_and_lengths(n, is_prime):
    """
    Parcours des nombres premiers jusqu'à n, calcul des gaps.
    Pour chaque gap détecté entre deux premiers p et q, 
    on remplit un tableau gap_length où chaque nombre dans le gap
    reçoit la longueur du gap (q-p).
    """
    gap_length = [0] * (n + 1)
    prev_prime = 2
    # Parcours tous les nombres à partir de 3 jusqu'à n
    for current in range(3, n + 1):
        if is_prime[current]:
            gap = current - prev_prime
            if gap > 1:
                # longueur du gap = gap
                # remplissage dans gap_length des nombres entre prev_prime et current
                for x in range(prev_prime + 1, current):
                    gap_length[x] = gap
            prev_prime = current
    return gap_length

def main():
    MAX_N = 1299709  # borne maximale (100000e nombre premier)
    is_prime = sieve(MAX_N)
    gap_length = prime_gaps_and_lengths(MAX_N, is_prime)

    for line in sys.stdin:
        k = line.strip()
        if k == "0":
            break
        k = int(k)
        # Si k est premier, alors longueur gap = 0
        if is_prime[k]:
            print(0)
        else:
            # Si k est composite, print la longueur du gap qui le contient
            print(gap_length[k])

if __name__ == "__main__":
    main()