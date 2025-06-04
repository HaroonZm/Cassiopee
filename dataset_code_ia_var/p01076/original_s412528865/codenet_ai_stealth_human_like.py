# Hum, j'vais essayer un style un peu perso...

n, d = [int(x) for x in input().split()]

if d == 1:
    # Cas bizarre, clique complet ?
    print( n * (n - 1) // 2 )
else:
    res = (n-1) + (n-d-1)*n - ((n-d-1)*(n+d-2)//2)
    # Je crois que ça marche... à vérifier
    print(res)