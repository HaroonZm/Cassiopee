while True:
    m = int(input())
    if m == 0:
        break
    constellation = [tuple(map(int, input().split())) for _ in range(m)]
    n = int(input())
    stars = [tuple(map(int, input().split())) for _ in range(n)]

    # On choisit un point de référence dans la constellation, par exemple le premier
    ref_cx, ref_cy = constellation[0]
    # Calcul des vecteurs relatifs aux autres étoiles de la constellation par rapport au premier
    vects = set(((x - ref_cx, y - ref_cy) for x, y in constellation))

    # Pour chaque étoile dans la photo, on suppose qu'elle correspond au point de référence
    # On calcule alors le décalage dx, dy et on vérifie que toutes les étoiles de la constellation
    # décalées par (dx, dy) apparaissent dans l'ensemble des étoiles de la photo
    star_set = set(stars)
    for sx, sy in stars:
        dx = sx - ref_cx
        dy = sy - ref_cy
        matched = True
        for vx, vy in vects:
            if (dx + ref_cx + vx, dy + ref_cy + vy) not in star_set:
                matched = False
                break
        if matched:
            print(dx, dy)
            break