# bon, on lit les valeurs - normal en concours...
x, a, b = map(int, input().split())
delta = -a + b  # c'est le calcul clé je crois

# j'utilise un peu trop de if imbriqués, mais bon, c'est lisible non ?
if delta <= 0:
    print("delicious")
else:
    if delta > 0 and delta <= x:  # un peu verbeux peut-être
        print("safe")
    else:
        print("dangerous")  # genre, danger !