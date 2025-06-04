W,H,w,h,x,y=map(int,input().split())
total=W*H-(w*h) # aire reste
from math import sqrt
def area(slope):
    # zone où y = slope*x divise le donut
    # aire à gauche (y <= slope*x)
    # intégration par parties basée sur la géométrie
    # aire totale à gauche (x<0) + part dans rectangle coupée

    # aire carré total sous y=slope*x
    if slope>=0:
        # La ligne coupe le carré entre (-H/slope, -H) and (W, slope*W)
        # calculer l'aire des deux triangles
        # formule (W*H)/2 or plus complexe selon pente
        # mais le donut est rectangle sauf le trou

        # On utilise la formule du trapèze:
        # Aire sous y=slope*x dans rectangle total
        # aire sous la droite = (W*H)/2 + correction selon slope positive

        left_total= (W*H)/2
    else:
        # si pente négative
        left_total= (W*H)/2

    # calcul aire sous la découpe dans trou (le rectangle w*h centré en (x,y))
    # On calcule l'aire de l'intersection du trou à gauche de la droite

    # coordonnées du trou bornes
    x0 = x - w/2
    x1 = x + w/2
    y0 = y - h/2
    y1 = y + h/2

    # fonction pour calculer aire à gauche dans le trou
    # on calcule l'aire de la partie de trou où y <= slope*x
    # intégration simple, on calcule intersection entre la droite et le trou

    def area_hole():
        # pour x dans [x0,x1], y limite = slope*x
        # définir les bornes de y: y0 à y1
        # pour chaque section, aire sous la droite

        # cas selon la relation de slope*x avec y0,y1

        # On considère les x où slope*x >= y0
        # et slope*x <= y1

        # bornes sur x selon y0,y1:
        if slope==0:
            # alors droite y=0
            if 0<y0:
                # toute la zone du rectangle est au dessus de la droite
                return 0
            elif 0>y1:
                return w*h
            else:
                return (y1-0)*w
        else:
            x_low=max(x0,min(x1,max(x0,min(x1,y0/slope if slope!=0 else x0))))
            x_high=max(x0,min(x1,max(x0,min(x1,y1/slope if slope!=0 else x0))))

            if slope>0:
                xa=max(x0,y0/slope)
                xb=min(x1,y1/slope)

                if xa>=xb:
                    if slope*x0>y1:
                        return 0
                    else:
                        return w*h
                xa = max(x0, xa)
                xb = min(x1, xb)

                base = xb - xa
                # aire triangulaire part
                # intégrale de y0 à slope*x sur x
                a = (y1 - y0)/w

                # approx: aire = int_{xa}^{xb} min(y1, slope*x) - y0 dx
                # car foré y0 ≤ y ≤ y1

                b=0

                # on intègre segment:
                # intégrale de slope*x - y0 dx = slope*(x²/2) - y0*x
                res=0
                # Clamping sur la limite droite
                x_left=xa
                x_right=xb
                res= slope*(x_right**2 - x_left**2)/2 - y0*(x_right - x_left)
                return max(0,min(w*h,res))
            else:
                # slope < 0
                # même calcul mais inverse
                xa=max(x0,y1/slope)
                xb=min(x1,y0/slope)
                if xa>=xb:
                    if slope*x0>y0:
                        return w*h
                    else:
                        return 0
                xa = max(x0, xa)
                xb = min(x1, xb)

                res= slope*(xb**2 - xa**2)/2 - y0*(xb - xa)
                return max(0,min(w*h,res))

    return (left_total - area_hole()) - (total - left_total + area_hole())

l,r = -1e6,1e6
for _ in range(60):
    m = (l+r)/2
    if area(m)>0:
        r=m
    else:
        l=m
print((l+r)/2)