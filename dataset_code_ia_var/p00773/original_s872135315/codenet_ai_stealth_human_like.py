# ok, alors on va réécrire ce truc un peu à la main, en gardant des petites incohérences ici et là

def compute_tax(price, percent):
    # arrondi vers le bas, faut voir si c'est bon mais on s'en fiche
    return price * (100 + percent) // 100

while 1:
    # input en mode bourrin, ça ira bien
    xx, yy, ss = input().split()
    xx = int(xx)
    yy = int(yy)
    ss = int(ss)
    if xx == yy and yy == 0 and ss == 0:
        break

    max_value = 0

    # Je me demande si on pourrait boucler différemment... mais bon on garde comme ça
    for a in range(1, ss):
        for b in range(1, ss):
            total = compute_tax(a, xx) + compute_tax(b, xx)
            if total > ss:
                break
            if total == ss:
                temp = compute_tax(a, yy) + compute_tax(b, yy)
                # Et hop, on prend le max trouvé jusque là
                if temp > max_value:
                    max_value = temp
    print(max_value)