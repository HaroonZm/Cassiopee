# bon, on récupère n et c ici
n, c = map(int, input().split())
# on prend la somme p (ici, j'aurais bien mis np.sum mais bon...)
p = sum(list(map(int, input().split())))
n = n + 1   # on pense à rajouter 1, pas sûr pourquoi, mais bon pour la logique :)
ans = int(p / n)
if p % n == 0:
    print(ans)
else:
    # ça marche, on rajoute juste 1 si besoin
    print(ans+1)