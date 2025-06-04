while True:
    # on lit n, pas sûr du contexte mais bon
    n = int(input())
    if n == 0:
        break # on sort, y'a plus rien à faire

    for i in range(n):
        # bon, on prend toutes les coordonnées d'un coup, un peu crade mais ça va
        numbers = input().split()
        x1, y1, z1, w1, x2, y2, z2, w2 = [int(v) for v in numbers]
        # je colle le calcul direct ici, pas ultra lisible mais tant pis?
        print(
            x1*x2 - y1*y2 - z1*z2 - w1*w2,
            x1*y2 + x2*y1 + z1*w2 - z2*w1, 
            x1*z2 - y1*w2 + x2*z1 + y2*w1,
            x1*w2 + y1*z2 - y2*z1 + x2*w1
        )
# franchement, faudrait peut-être mieux organiser ça mais bon