MOD = 10**9 + 7

def modinv(a, m=MOD):
    return pow(a, m-2, m)

def main():
    d = int(input())
    l = [int(input()) for _ in range(d)]
    s = int(input())

    max_s = s
    # dp[i][j] = nombre de façons de choisir x_1,...,x_i avec somme j
    dp = [0] * (s + 1)
    dp[0] = 1

    for length in l:
        new_dp = [0] * (s + 1)
        # Préfixe pour optimisation des sommes
        prefix = [0] * (s + 2)
        for j in range(s + 1):
            prefix[j+1] = (prefix[j] + dp[j]) % MOD
        for j in range(s + 1):
            left = j - length
            if left < 0:
                left = 0
            new_dp[j] = (prefix[j+1] - prefix[left]) % MOD
        dp = new_dp

    # Calculer la factorielle d! modulo MOD
    fact = 1
    for i in range(1, d + 1):
        fact = (fact * i) % MOD

    # dp[j] représente le nombre d'entiers points dans l'hypercube avec somme <= s exactement à j
    # la somme des dp[0]+...+dp[s] donne le décompte des points dont la somme est <= s
    count = sum(dp) % MOD

    # Le volume V est le nombre de points divisé par produit des l[i], car c'est un volume discret
    # mais ici on cherche d! * V selon l'énoncé, et d! * V correspond au nombre calculé par dp multiplié par d!/Π l_i
    # Or la méthode par programmation dynamique calcule le nombre de points entiers dans la région
    # Le volume V = nombre de points / produit des l_i

    # Il se trouve que d! * V modulo MOD = d! * (nombre de points / prod l_i) modulo MOD
    # Ce qui revient à : (d! * nombre de points) * modinv(prod l_i)
    prod_l = 1
    for li in l:
        prod_l = (prod_l * li) % MOD

    ans = (fact * count) % MOD
    ans = (ans * modinv(prod_l)) % MOD
    print(ans)

if __name__ == "__main__":
    main()