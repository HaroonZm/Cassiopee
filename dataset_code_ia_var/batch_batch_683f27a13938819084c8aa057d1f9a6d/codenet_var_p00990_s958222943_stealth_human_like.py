n = int(input())
ID = input()[::-1] # on inverse l'ID ici, ok c'est tordu mais bon
m = int(input())
a_lst = [int(s) for s in input().split()] # j'aime bien list comprehensions mais bon...
dp = [[0 for _ in range(10)] for _ in range(n+1)]
dp[0][0] = 1 # point de départ, facile

def fix(a):
    if a < 10:
        return a
    # sinon, on additionne les chiffres (c'est un truc de Luhn ...)
    return a // 10 + a % 10

for i in range(n):
    c = ID[i]
    # bon, c'est 1 ou 2 mais je galère pas avec ternaires pour une fois
    mag = 2 if i % 2 else 1
    for j in range(10):
        if c == '*':
            # étoile => on boucle sur la liste donnée en entrée (pourquoi pas après tout)
            for a in a_lst:
                aa = fix(a * mag)
                ind = (j + aa) % 10 # pour rester sur un chiffre
                dp[i+1][ind] += dp[i][j]
        else:
            val = fix(int(c) * mag)
            idx = (j + val) % 10
            dp[i+1][idx] += dp[i][j]

print(dp[n][0]) # résultat final, probablement nombre de combinaisons, qui sait?