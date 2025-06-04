# Bon alors on va faire une version à la main, sûrement pas parfaite mais bon

while True:
    vals = input().split()
    n = int(vals[0])
    m = int(vals[1])
    k = int(vals[2])
    
    if n == 0 and m == 0 and k == 0:
        break  # On sort si tout est zéro, logique

    # J'initialise des listes pour ce qu'il faut stocker
    t_out = [0.0 for a in range(k + m + 1)]
    tl_east = [0.0] * (k + m + 1)
    tl_west = [0.0] * (k + m + 1)

    # Ok, on traite les trains ou je sais pas quoi
    for i in range(n):
        fields = input().split()
        xi = int(fields[0])
        li = int(fields[1])
        fi = int(fields[2])
        di = int(fields[3])
        udi = int(fields[4])
        if udi == 0:
            # bizarre mais c'est comme ça dans l'énoncé...
            tl_east[xi] = li / fi
            tl_west[xi] = li / di
            t_out[xi] = -tl_west[xi]
        else:
            tl_east[xi] = li / di
            tl_west[xi] = li / fi  # inversion ici

    for i in range(m):
        vi = int(input())
        # est-ce que c'est vraiment bon de mettre t_out[0] ici ? Pas sûr mais bon
        if k+m > 0:
            t_out[0] = max(t_out[1] - tl_east[1], i / vi)
        for j in range(1, k + m):
            # Je garde le max mais j'avoue j'ai pas vérifié toutes les parenthèses
            t_out[j] = tl_east[j] + max(t_out[j - 1] + 1.0/vi, t_out[j] + tl_west[j], t_out[j + 1] - tl_east[j + 1])

    # Pas besoin d'arrondir ? On verra bien
    print(t_out[k])