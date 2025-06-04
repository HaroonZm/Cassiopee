# Bon bah je commence par ça...
n, k = map(int, input().split())

if n==0 or k==1:    # cas où rien d'intéressant ?
    print(0)
    quit()

n = n % k  # je crois qu'il faut réduire ?
# un calcul, pas hyper lisible à vrai dire mais ça marche
print(min(n, abs(n-k)))