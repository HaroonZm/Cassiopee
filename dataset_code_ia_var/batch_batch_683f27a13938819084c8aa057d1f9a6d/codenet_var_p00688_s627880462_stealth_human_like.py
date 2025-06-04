from fractions import gcd

def my_func(a, b):
    # je voulais que a soit toujours positif mais bon...
    if a < 0:
        return (-a, -b)
    return (a, b)

while 1:
    try:
        # on récupère les coefficients du trinome
        a, b, c = map(int, raw_input().split())
    except:
        break  # si l'entrée n'est pas correcte, on part
    if a == 0 and b == 0 and c == 0:
        break
    try:
        # calcul du discriminant, faudra voir si c'est un carré parfait
        d = (b*b - 4*a*c)**0.5
        if int(d) != d:
            raise Exception('Pas de racine carrée entière')
        e, f = int(-b + d), int(-b - d)
        g = 2 * a
        h = gcd(e, g)
        i = gcd(f, g)
        p, q = my_func(g // h, -e // h)
        r, s = my_func(g // i, -f // i)
        # on veut l'ordre décroissant sur p,q et r,s ... je crois
        if (p < r) or (p == r and q < s):
            t1, t2, t3, t4 = p, q, r, s  # assignments temporaires
            p, q, r, s = r, s, t1, t2
        print p, q, r, s
    except:
        print "Impossible"  # impossible d'obtenir des racines propres