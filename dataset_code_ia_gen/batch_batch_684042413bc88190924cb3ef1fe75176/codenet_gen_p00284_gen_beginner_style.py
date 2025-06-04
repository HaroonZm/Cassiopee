N = int(input())
for _ in range(N):
    s, d = map(int, input().split())
    time = 10**9  # grand nombre arbitraire pour minimiser
    diff = d - s
    for n in range(31):  # essayer les niveaux 0 à 30
        step = 2**n
        # trouver le plus petit arrêt >= s sur cette ligne
        if s % step == 0:
            start = s
        else:
            start = s + (step - s % step)
        # vérifier que cet arrêt est <= d
        if start <= d:
            # temps = nombre d'intervalles entre start et d
            t = (d - start) // step + 1
            if t < time:
                time = t
    print(time)