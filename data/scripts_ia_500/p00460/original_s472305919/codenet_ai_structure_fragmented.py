DIV = 100000

def lire_entrees():
    return map(int, raw_input().split())

def condition_arret(n):
    return n == 0

def initialiser_dp(n, s):
    return [[0]*(s+1) for _ in range(n*n+1)]

def set_valeur_initiale(dp):
    dp[0][0] = 1

def calcule_valeur_dp_i_j(dp, i, j, m, DIV):
    if j - i >= 0:
        dp[i][j] = (dp[i][j] + dp[i-1][j-i] + dp[i][j-i]) % DIV
    if j - m - 1 >= 0:
        dp[i][j] = (dp[i][j] - dp[i-1][j-m-1] + DIV) % DIV

def boucle_interieure(dp, i, s, m, DIV):
    for j in range(s+1):
        calcule_valeur_dp_i_j(dp, i, j, m, DIV)

def boucle_exterieure(dp, n, s, m, DIV):
    for i in range(1, n*n+1):
        boucle_interieure(dp, i, s, m, DIV)

def affiche_resultat(dp, n, s):
    print dp[n*n][s]

def main():
    while 1:
        n, m, s = lire_entrees()
        if condition_arret(n):
            break
        dp = initialiser_dp(n, s)
        set_valeur_initiale(dp)
        boucle_exterieure(dp, n, s, m, DIV)
        affiche_resultat(dp, n, s)

main()