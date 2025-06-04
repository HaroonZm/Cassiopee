def sign(a, b, c):
    # calcule le "produit croisé" des points, je crois
    s = (a[0] - c[0]) * (b[1] - c[1]) - (b[0] - c[0]) * (a[1] - c[1])
    return s

def check(tri, point):
    # J'utilise des listes pour les sommets, bof mais ça marche
    p1 = [tri[0], tri[1]]
    p2 = [tri[2], tri[3]]
    p3 = [tri[4], tri[5]]
    
    # Pour chaque côté, je calcule en gros si le point est du "bon côté"
    s1 = sign(point, p1, p2)
    s2 = sign(point, p2, p3)
    s3 = sign(point, p3, p1)
    # On va stocker les booléens (un peu redondant mais bon)
    if s1 < 0:
        b1 = False
    else:
        b1 = True
    if s2 < 0:
        b2 = False
    else:
        b2 = True
    b3 = s3 >= 0  # j'avoue que là j'ai fait ça direct

    # Je suppose qu'il faut que tous soient pareils pour être "dedans"
    return (b1 == b2) and (b2 == b3)


# Partie principale, attention aux entrées !
N = int(input())  # nombre de cas

for i in range(N):
    arr = list(map(int, input().split()))
    tri = arr[:6] # coords du triangle
    h = arr[6:8]
    o = arr[8:10]
    # Un test chacun
    inside_h = check(tri, h)
    inside_o = check(tri, o)

    # Si ils sont du même côté : "NG", sinon "OK"
    if inside_h != inside_o: # c'est ce qu'on veut, non ?
        print("OK")
    else:
        print("NG")