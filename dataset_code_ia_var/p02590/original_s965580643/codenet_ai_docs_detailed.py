import numpy as np
from scipy import signal
import pprint

def initialize_lookup_tables(p, g):
    """
    Initialise les tables de correspondance pour le logarithme discret et son inverse dans Z_p^*.

    Args:
        p (int): Un nombre premier utilisé comme modulo.
        g (int): Un générateur primitif modulo p.

    Returns:
        tuple:
            - c (np.ndarray): Table des logarithmes discrets, c[k] donne l'exposant pour lequel g^c[k] ≡ k mod p.
            - d (np.ndarray): Table des puissances, d[i] donne g^i mod p.
    """
    c = np.zeros(p, dtype=np.int64)
    d = np.zeros(p, dtype=np.int64)
    k = 1
    for i in range(p - 1):
        c[k] = i            # c[k]: log_g(k) dans Z_p^*
        d[i] = k            # d[i]: g^i mod p
        k = k * g % p       # Génère la prochaine puissance de g
    return c, d

def compute_frequency_vector(a, c, p):
    """
    Construit un vecteur de fréquences représentant la distribution des logarithmes discrets des éléments de a.

    Args:
        a (np.ndarray): Tableau d'entiers à analyser.
        c (np.ndarray): Table des logarithmes discrets.
        p (int): Modulo premier.

    Returns:
        np.ndarray: Vecteur b où b[i] est le nombre d'éléments de a tels que log_g(a_j) = i.
    """
    b = np.zeros(p, dtype=np.float64)
    for x in a:
        if x > 0:
            w = int(c[x])  # log_g(x) dans Z_p^*
            b[w] += 1      # Incrémente la fréquence du logarithme
    return b

def count_valid_pairs(b, d, res, p):
    """
    Calcule la somme pondérée de d[i % (p-1)] selon les résultats de la convolution.

    Args:
        b (np.ndarray): Vecteur de fréquences.
        d (np.ndarray): Table des puissances.
        res (np.ndarray): Résultat de la convolution (auto-convolution de b).
        p (int): Modulo premier.

    Returns:
        int: Somme totale des paires valides (pondérées selon leur multiplicité).
    """
    ans = 0
    for i in range(len(res)):
        if res[i] > 0.5:  # Seuil pour traiter la précision flottante
            w = int(round(res[i]))    # Nombre de paires pour log_g(x1) + log_g(x2) = i
            ans += w * d[i % (p - 1)] # d[i % (p-1)] = g^{i % (p-1)} mod p
    return ans

def adjust_ans(ans, a, p):
    """
    Soustrait la contribution des paires de la forme (x, x) et divise par 2 pour compter chaque paire une fois.

    Args:
        ans (int): Somme totale initiale.
        a (np.ndarray): Tableau d'entrée.
        p (int): Modulo premier.

    Returns:
        int: Résultat final corrigé.
    """
    for x in a:
        ans -= x * x % p       # Retire les cas (x, x) (où x1 == x2)
    ans = ans // 2             # Chaque paire (x1, x2) et (x2, x1) est comptée deux fois
    return ans

def main():
    """
    Programme principal qui lit l'entrée, prépare les tables, calcule la solution puis imprime le résultat.
    """
    # Lecture du nombre d'éléments (inutile dans la suite mais lu pour compatibilité)
    n = input()
    # Lecture du tableau d'entiers
    a = np.array(list(map(int, input().split())), dtype=np.int64)

    # Définition du modulo premier et du générateur
    p = 200003
    g = 2

    # Initialisation des tables de correspondance logarithme discret <-> puissance
    c, d = initialize_lookup_tables(p, g)

    # Construction du vecteur de fréquences des logarithmes discrets pour les entiers non nuls de a
    b = compute_frequency_vector(a, c, p)

    # Convolution rapide pour compter efficacement les combinaisons de logarithmes discrets s'annulant dans Z_{p-1}
    res = signal.fftconvolve(b, b, mode='full')

    # Calcule la somme pondérée des résultats de la convolution via la table d'inverse des puissances
    ans = count_valid_pairs(b, d, res, p)

    # Ajustement pour retirer les auto-paires et décompter les paires inversées
    ans = adjust_ans(ans, a, p)

    # Affichage du résultat final
    print(ans)

if __name__ == "__main__":
    main()