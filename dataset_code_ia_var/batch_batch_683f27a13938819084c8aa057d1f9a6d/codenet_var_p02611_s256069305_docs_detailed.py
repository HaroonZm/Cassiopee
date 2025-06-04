import numpy as np

MOD = 10 ** 9 + 7  # Constante pour l'opération modulo, couramment utilisée pour éviter les débordements numériques

def create_transition_matrix():
    """
    Crée et retourne une matrice de transition 32x32 spécifique utilisée pour des calculs dynamiques.
    Cette matrice encode des relations récurrentes particulières entre les états.
    
    Returns:
        np.ndarray: Une matrice carrée 32x32 de type uint64 avec les transitions spécifiées.
    """
    l_matrix = np.zeros((32, 32), np.uint64)

    # Liens croisés entre les 16 premiers et 16 seconds éléments
    for i in range(16):
        l_matrix[i+16][i] = 1
        l_matrix[i][i+16] = 1

    # Transitions entre éléments consécutifs dans les 15 premiers états
    for i in range(15):
        l_matrix[i+1][i] = 1

    # Transitions additionnelles pour des indices spécifiques
    for i in range(5, 15):
        l_matrix[i+1][i+16] = 1

    return l_matrix

def compute_doubling_powers(l_matrix, max_power=30):
    """
    Précalcule les puissances successives (par doublement) de la matrice de transition modulo MOD.
    doubling[i] = l_matrix ** (2**i) % MOD

    Args:
        l_matrix (np.ndarray): La matrice de transition de base.
        max_power (int): Le nombre maximal d'exposants à calculer. Par défaut 30.

    Returns:
        List[np.ndarray]: Liste des puissances par doublement de la matrice modulo MOD.
    """
    doubling = [l_matrix.copy()]  # Première puissance, à la fois **1
    for _ in range(max_power):
        next_matrix = doubling[-1] @ doubling[-1] % MOD  # Matrice précédente au carré modulo MOD
        doubling.append(next_matrix)
    return doubling

def matrix_binary_exponentiation(dp, doubling, N):
    """
    Effectue une exponentiation binaire de la matrice via le vecteur dp,
    selon la représentation binaire de N.

    Args:
        dp (np.ndarray): Vecteur d'état initial (dimension 32)
        doubling (List[np.ndarray]): Puissances de la matrice de transition selon chaque bit
        N (int): Nombre d'étapes (correspond à la puissance à appliquer)

    Returns:
        np.ndarray: Vecteur d'état final après multiplication matricielle.
    """
    N_bin = format(N, 'b')[::-1]  # Conversion binaire inversée pour itérer sur les bits du LSB au MSB
    for i, c in enumerate(N_bin):
        if c == '1':
            # Multiplie uniquement si le bit est activé
            dp = doubling[i] @ dp
            dp %= MOD  # Réduire modulo MOD pour chaque étape afin d'éviter les débordements
    return dp

def solve():
    """
    Fonction principale qui lit les entrées, initialise les structures, 
    traite chaque cas de test et affiche le résultat.
    """
    l_matrix = create_transition_matrix()
    doubling = compute_doubling_powers(l_matrix)  # Pré-calcule les puissances par doublement

    T = int(input())  # Nombre de cas de test
    for _ in range(T):
        N = int(input())
        N += 10  # Décalage de 10 sur N selon la logique métier métier propre au problème

        dp = np.zeros(32, np.uint64)
        dp[0] = 1  # État initial (uniquement le premier état actif)

        dp_final = matrix_binary_exponentiation(dp, doubling, N)

        # Affiche la somme de dp[15] et dp[31] modulo MOD comme demandé
        print(int((dp_final[15] + dp_final[31]) % MOD))

if __name__ == "__main__":
    solve()