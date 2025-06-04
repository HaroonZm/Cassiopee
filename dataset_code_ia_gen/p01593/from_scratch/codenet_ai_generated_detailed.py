import sys
import math

# Fonction pour calculer la probabilité de gagner le jeu
def earn_big_probability(N, M):
    # Le problème revient à calculer la probabilité qu'un permutation aléatoire de N éléments
    # ne contienne pas de cycle de longueur strictement supérieure à M.
    #
    # En effet, chaque participant pi suit un cycle dans la permutation :
    # Il part de sa boîte i, regarde le nom dans cette boîte,
    # puis ouvre la boîte indiquée par ce nom, etc.
    # S'il retrouve son nom dans au plus M ouvertures (longueur du cycle <= M),
    # il réussit.
    #
    # La condition que tout le monde réussisse est que tous les cycles dans la permutation
    # aient une longueur <= M.
    #
    # La probabilité cherchée est donc la proportion des permutations de N éléments
    # qui ne contiennent pas de cycle de longueur > M.
    #
    # Cette probabilité peut être calculée avec la formule basée sur les nombres de Stirling
    # de première espèce signés (qui comptent le nombre de permutations selon leur nombre et leur taille de cycles),
    # mais ici nous utilisons une approche dynamique adaptée.
    #
    # Soit dp[n] la proportion des permutations de n éléments ne contenant que des cycles
    # de longueur au plus M.
    #
    # On a la relation de récurrence pour les permutations restreintes :
    # dp[0] = 1 (permutation vide)
    # dp[n] = sum_{k=1 to min(n,M)} (1/n!)*(nombre de façons de former un cycle de longueur k)*dp[n-k] * (nombre de permutations des autres éléments)
    #
    # En calculant en terme absolu, on a la formule :
    # Nombre de permutations avec cycles ≤ M = sum_{k=1}^min(n,M) C(n-1,k-1)(k-1)! * nombre de telles permutations sur les n-k éléments.
    #
    # Pour éviter les grandes valeurs on gère en double précision et calcule la quantité souhaitée.
    #
    # On peut exprimer la formule diffusée sur :
    # https://en.wikipedia.org/wiki/Permutations_with_restricted_cycle_length
    #
    # Ici, on calcule le nombre de permutations où tous les cycles ont longueur ≤ M par DP :
    #
    # dp[0] = 1
    # dp[n] = sum_{k=1}^{min(n,M)} (dp[n-k] * combinaison(n-1,k-1) * (k-1)!) 
    #
    # Pour éviter la combinatoire lourde, on remarque que le nombre de cycles de longueur k est (k-1)!,
    # la combinatoire est "n-1 choose k-1" pour choisir les éléments du cycle avec i fixe.
    #
    # Finalement, on divise par n! la valeur dp[N] pour avoir la proportion.
    #
    # Comme dp[n] comptabilise le nombre de permutations restreintes en combinant cycles dont on a réglé la combinatoire,
    # on doit utiliser une formulation correcte avec fact(), comb().

    # Pour éviter d'utiliser directement combinatoire lourde, on utilise une relation combinatoire classique:
    # Le nombre de permutations de n éléments dont tous les cycles ont une taille ≤ M est donné par la fonction e.g.f :
    # C'est le terme coefficient du polynôme e^{x + x^2/2 + ... + x^M/M!} multiplié par n!.
    # On peut calculer dp[n] récursivement avec:
    # dp[0] = 1
    # dp[n] = sum_{k=1}^{min(n,M)} dp[n-k] * factorial(k-1)

    # Mais attention, ce dp[n] correspond à un nombre non divisé par n!.
    # Le coefficient de permutations est dp[n]*comb(n-1,k-1)*factorial(k-1) en combinatoire, mais ça complexifie.

    # Pour résoudre ce problème de manière efficace:
    # On utilise la relation classique suivante, appelée formule d'exclusion pour la décomposition en cycles :
    # Soit D[n] le nombre de permutations de n éléments avec des cycles tous de longueur ≤ M.
    # Les D[n] vérifient la relation:
    # D[0] = 1
    # D[n] = sum_{k=1 to min(n,M)} (k-1)! * D[n-k] * C(n-1, k-1)

    # Pour calculer C(n-1,k-1) on utilisera une pré-calcul de combinaisons.

    # Enfin, la probabilité = D[N] / factorial(N)

    # ----------------------------------------------
    # Calculs préparatoires :

    # Pré-calcul des factoriels et combinaisons
    fact = [1] * (N + 1)
    for i in range(1, N + 1):
        fact[i] = fact[i - 1] * i

    # Pré-calcul des combinaisons C(n,k) via formule : C(n,k) = fact[n]/(fact[k]*fact[n-k])
    def comb(n, k):
        return fact[n] / (fact[k] * fact[n - k])

    D = [0.0] * (N + 1)
    D[0] = 1.0

    for n in range(1, N + 1):
        s = 0.0
        upper = min(n, M)
        for k in range(1, upper + 1):
            # (k-1)! * D[n-k] * C(n-1, k-1)
            val = fact[k - 1] * D[n - k] * comb(n - 1, k - 1)
            s += val
        D[n] = s

    # La probabilité est D[N] / N!
    probability = D[N] / fact[N]

    return probability

def main():
    input_line = sys.stdin.readline().strip()
    N, M = map(int, input_line.split())
    prob = earn_big_probability(N, M)

    # Affichage avec précision demandée (au moins 10^-8)
    print(f"{prob:.8f}")

if __name__ == "__main__":
    main()