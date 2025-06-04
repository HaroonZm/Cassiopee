MOD = 10**9 + 7

def count_palindromic_subsequences(S: str) -> int:
    n = len(S)
    # dp[i][j] : nombre de sous-suites palindromiques distinctes dans S[i:j+1]
    dp = [[0] * n for _ in range(n)]
    
    # last[c] : liste des positions de la lettre c dans S, pour optimisation
    # ici on n'en a pas besoin explicitement, la méthode classique suffit.
    
    # Initialisation : pour i==j, chaque caractère est un palindrome unique
    for i in range(n):
        dp[i][i] = 1  # Sous-suite palindrome d'une lettre = 1
    
    # Parcours des sous-chaînes de longueur croissante
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            
            if S[i] == S[j]:
                # Si les caractères aux extrémités sont égaux,
                # on regarde l'intervalle intérieur (i+1,j-1)
                left_index = i + 1
                right_index = j - 1
                
                # Recherche des positions des occurrences de S[i] dans S[left_index:right_index+1]
                # Trouver la première occurrence à droite de i et la dernière occurrence à gauche de j
                l = left_index
                r = right_index
                while l <= r and S[l] != S[i]:
                    l += 1
                while r >= l and S[r] != S[i]:
                    r -= 1
                
                if l > r:
                    # Pas d'autre occurrence de S[i] dans la région intérieure
                    # On double les palindromes intérieurs et on ajoute 2 (pour les palindromes de 1 caractère S[i], S[j])
                    dp[i][j] = dp[i+1][j-1] * 2 + 2
                elif l == r:
                    # Une seule occurrence de S[i] dans la région intérieure
                    # On double les palindromes intérieurs et on ajoute 1
                    dp[i][j] = dp[i+1][j-1] * 2 + 1
                else:
                    # Plus d'une occurrence de S[i] dans la région intérieure
                    # On double les palindromes intérieurs et on soustrait les doublons
                    dp[i][j] = dp[i+1][j-1] * 2 - dp[l+1][r-1]
            else:
                # Si les caractères aux extrémités sont différents,
                # on additionne les résultats des deux sous-ensembles
                # en enlevant les doublons comptés deux fois
                dp[i][j] = dp[i+1][j] + dp[i][j-1] - dp[i+1][j-1]
            
            # Pour éviter les valeurs négatives, on ajuste modulo MOD
            dp[i][j] %= MOD
    
    return dp[0][n-1] % MOD

if __name__ == "__main__":
    S = input().strip()
    print(count_palindromic_subsequences(S))