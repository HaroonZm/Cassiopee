import sys

readline = sys.stdin.readline
write = sys.stdout.write

class RollingHash:
    """
    Classe utilitaire pour calculer rapidement le hash de sous-chaînes d'une chaîne donnée,
    en utilisant une base et un modulo spécifiés.
    """
    def __init__(self, s, base, mod):
        """
        Initialise la structure RollingHash pour une chaîne s.
        
        Args:
            s (str): La chaîne de caractères pour laquelle le hash sera calculé.
            base (int): La base utilisée pour le calcul du hash.
            mod (int): Le modulo appliqué pour éviter le dépassement.
        """
        self.mod = mod
        l = len(s)
        # Pré-calcule les puissances de la base jusqu'à la longueur de la chaîne
        self.pw = pw = [1] * (l + 1)
        # Pré-calcule les valeurs de hash des préfixes de s
        self.h = h = [0] * (l + 1)
        
        v = 0
        # Calcul du hash cumulatif pour chaque préfixe de la chaîne s
        for i in range(l):
            h[i + 1] = v = (v * base + ord(s[i])) % mod

        v = 1
        # Calcul des puissances de base (base^k % mod) pour chaque position k
        for i in range(l):
            pw[i + 1] = v = v * base % mod

    def get(self, l, r):
        """
        Renvoie le hash de la sous-chaîne s[l:r], c'est-à-dire entre les indices l inclus et r exclus.
        
        Args:
            l (int): Indice de début de la sous-chaîne.
            r (int): Indice de fin (exclu) de la sous-chaîne.
        
        Returns:
            int: La valeur de hash de la sous-chaîne.
        """
        return (self.h[r] - self.h[l] * self.pw[r - l]) % self.mod

def solve():
    """
    Fonction principale qui lit l'entrée, effectue les calculs nécessaires, et écrit le résultat.
    Elle compte le nombre de nombres dans un intervalle [A, B] qui contiennent la chaîne C
    selon un certain critère algorithmique basé sur le Rolling Hash pour comparaison efficace.
    """
    MOD = 10 ** 9 + 7  # Modulo utilisé pour toutes les opérations de résultat
    
    # Lecture des chaînes A, B, et C depuis l'entrée standard
    A, B, C = readline().strip().split()

    # Détermination de la longueur maximale entre A et B
    L = max(len(A), len(B))

    # Pré-calcul des puissances de 10 modulo MOD pour faciliter le calcul ultérieur
    pw10 = [1] * (L + 1)
    r = 1
    for i in range(1, L + 1):
        pw10[i] = r = r * 10 % MOD

    def calc(X, Y):
        """
        Calcule le nombre de chiffres dans la chaîne X qui 'contiennent' la chaîne Y
        d'après des critères spécifiques utilisant RollingHash.
        
        Args:
            X (str): La chaîne représentant la borne supérieure de l'intervalle de recherche.
            Y (str): La sous-chaîne recherchée au sein des nombres générés.
        
        Returns:
            int: Le nombre de cas où la chaîne Y est contenue selon les règles dans X.
        """
        mod = 10 ** 9 + 9  # Modulo utilisé dans RollingHash pour minimiser collisions
        N = len(X)
        M = len(Y)
        
        # Si X est plus court que Y, aucun résultat possible
        if N < M:
            return 0

        # Initialisation des RollingHash pour X et Y
        hx = RollingHash(X, 37, mod)
        hy = RollingHash(Y, 37, mod)

        # Calcul du hash de chaque préfixe de Y
        hY = [hy.get(0, i) for i in range(M + 1)]

        res = 0  # Résultat final du calcul
        cur = 0  # Compteur d'occurrences valides trouvées en cours de calcul

        # Parcours chaque chiffre de X
        for i in range(N):
            v = int(X[i])
            # Ajoute à res la contribution pour les préfixes trouvés jusqu'ici
            res += cur * v * pw10[N - (i + 1)] % MOD

            # Recherches pour chaque position possible d'occurrence de Y finissant à i
            for j in range(i - M + 1, i + 1):
                if j + M > N:
                    break  # Dépasse la chaîne, inutile de continuer
                l = i - j  # Longueur du préfixe
                # Vérifie si le préfixe correspond à celui de Y ou si la comparaison numérique échoue
                if (0 < l and hx.get(j, j + l) != hY[l]) or v <= int(Y[i - j]):
                    continue
                # Incrémente res avec la puissance correspondante de 10
                res += pw10[N - (j + M)]

            # Gestion du cas où l'ensemble du motif peut encore suivre
            if M + (i + 1) <= N:
                res += v * pw10[N - (M + i + 1)] * (N - (i + 1) - M + 1) % MOD

            # Incrémente le compteur si un motif complet vient d'être trouvé
            if i - M + 1 >= 0 and hx.get(i - M + 1, i + 1) == hY[M]:
                cur += 1

        # Comptage final pour tous les motifs Y trouvés dans X
        for j in range(N - M + 1):
            if hx.get(j, j + M) != hY[M]:
                continue
            res += 1

        # Correction pour le cas particulier où Y vaut "0"
        if Y == "0":
            for i in range(1, N):
                res -= 9 * pw10[N - i - 1] * i % MOD
            res -= N - 1

        return res % MOD

    # Calcule le nombre d'occurrences dans l'intervalle [A, B]
    ans = calc(B, C)

    # Ajuste le résultat pour A - 1 (évite le double comptage de A si inclus)
    a = int(A)
    if a > 0:
        A = str(a - 1)
        ans -= calc(A, C)

    # Écrit le résultat final sur la sortie standard
    write("%d\n" % (ans % MOD))

# Exécution de la fonction principale
solve()