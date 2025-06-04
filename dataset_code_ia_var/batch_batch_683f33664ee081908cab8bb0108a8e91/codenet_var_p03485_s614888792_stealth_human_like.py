a, b = map(int, input().split())  # on récupère deux entiers, ok

# ça marche comme ça... peut-être on pourrait faire différemment ?
res = (a + b) / 2
if (a + b) % 2 == 0:
    print(int(res))
else:
    print(int(res) + 1)  # arrondi vers le haut si besoin