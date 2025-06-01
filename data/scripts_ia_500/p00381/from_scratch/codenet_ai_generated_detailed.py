MOD = 10**9 + 7

def count_routes(N, s, t):
    """
    Calcule le nombre de routes possibles de l'étoile 1 à l'étoile N selon les règles
    du transport via les machines warp.
    
    Approche:
    - Pour chaque étoile i, on veut connaître le nombre de façons d'y parvenir.
    - On part de dp[1] = 1 car on commence sur l'étoile 1.
    - On sait que pour aller d'une étoile i à une étoile j (j > i), 
      on peut passer si s[i] == t[j], c'est-à-dire si le label de l'entrée de i
      est égal au label de la sortie de j.
    - Ainsi, dp[j] += somme de dp[i] pour tous i < j tels que s[i] == t[j].
    
    Optimisation importante:
    - Un calcul naïf serait O(N^2), impossible pour N=100000.
    - On remarque que dp[j] ne dépend que des dp[i] dont s[i] == t[j].
    - On peut donc regrouper les dp[i] par la lettre s[i].
    - On maintient un dictionnaire sum_by_char qui pour chaque caractère c
      garde la somme des dp[i] avec s[i] = c, pour i < j.
    - On parcourt les étoiles dans l'ordre croissant:
      * Pour étoile j, dp[j] = sum_by_char[t[j]]
      * On met ensuite à jour sum_by_char[s[j]] += dp[j].
    
    Complexité de cette méthode: O(N).
    """
    # dp[i]: nombre de façons d'atteindre l'étoile i+1 (indexation 0-based)
    dp = [0]*N
    dp[0] = 1  # on commence à l'étoile 1
    
    # Dictionnaire pour maintenir la somme des dp[i] pour chaque caractère s[i],
    # i < current index
    sum_by_char = dict()
    
    for i in range(N):
        if i > 0:
            # dp[i] = somme des dp[j] avec s[j] == t[i], j < i
            dp[i] = sum_by_char.get(t[i], 0) % MOD
        # Mettre à jour la somme associée au caractère s[i] avec dp[i]
        sum_by_char[s[i]] = (sum_by_char.get(s[i], 0) + dp[i]) % MOD

    return dp[N-1] % MOD

# Lecture input
N = int(input())
s = input().strip()
t = input().strip()

# Calcul et affichage résultat
print(count_routes(N, s, t))