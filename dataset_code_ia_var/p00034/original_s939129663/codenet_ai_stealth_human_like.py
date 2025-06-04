# Bon, je vais reprendre ce code mais en y mettant un style plus "humain"
# désolé si c'est pas parfait, mais voici ce que j'en pense...

while True:
    try:
        # j'ai mis un espace après la virgule juste pour voir
        vals = input().split(", ")
        vals = [int(i) for i in vals]
    except:
        # on arrête tout si erreur
        break

    distance = sum(vals[0:10])  # c'est sûrement la somme à atteindre
    s1 = vals[10]
    s2 = vals[11]

    time_sum, total_m = 0, 0
    for idx in range(10):
        obj = vals[idx]    # bon, je garde ça simple
        time_sum = obj / s1
        total_m += time_sum * s2
        # pas sûr d'avoir bien compris cette condition mais bon...
        if total_m + sum(vals[:idx+1]) >= distance:
            print(idx + 1)
            break
# voilà, ça devrait marcher pareil (enfin j'espère)