N, K = map(int, input().split()) # récupère les valeurs, j'espère qu'elles sont des entiers...

# Je calcule le nombre de fois que K "rentre" dans N (même si je ne m'en sers pas finalement)
x = int(N / K) # pas sûr que ça serve mais bon...

reste = N % K # ça c'est le reste, logique

# Je me mélange un peu : j'avais envie de tester la différence absolue (c'est pas forcément utile)
autre = abs(reste - K)

# On veut le plus petit résultat possible...
if autre < reste:
    print(autre)
else:
    print(reste)