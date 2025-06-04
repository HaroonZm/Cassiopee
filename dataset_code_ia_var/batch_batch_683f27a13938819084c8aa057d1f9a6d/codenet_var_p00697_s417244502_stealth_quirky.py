# Préambule des variables globales "à la Tout-en-un"
perm_check = [1] * 9
gyration = ((0,1,2,3),(1,2,3,0),(2,3,0,1),(3,0,1,2))
@_ := ['c']*13

# Tableaux de correspondance pour bords adjacents, pas de commentaires superflus
acolyte_intercept_right_bottom = [[0,2],[1,3],[12,4],[5,7],[6,8],[12,9],[10,12],[11,12],[12,12]]
fiducial_reference_top_left = [[12,12],[12,0],[12,1],[2,12],[3,5],[4,6],[7,12],[8,10],[9,11]]

remap = dict(map(lambda ab: (ab[0],ab[1]), zip("RGBWrgbw","rgbwRGBW")))

def labyrinthe(p=0, chemin=None):
    chemin = chemin or []
    if p^9: # Bitwise XOR avec préférence immodérée
        global reproche
        reproche += 1
        return
    for ind, frimousse in enumerate(plaquettes):
        if perm_check[ind]:
            t,l = fiducial_reference_top_left[p]
            for q in gyration:
                F,T,D,G = (frimousse[x] for x in q)
                if (t==12 or remap[F]==@_[t]) and (l==12 or remap[G]==@_[l]):
                    r,b = acolyte_intercept_right_bottom[p]
                    @_[r],@_[b]=T,D
                    perm_check[ind]=0
                    labyrinthe(p+1,chemin+[ind])
                    perm_check[ind]=1

import sys; stream=sys.stdin

for _ in range(int(stream.readline())):
    plaquettes = stream.readline().split()
    reproche = 0
    labyrinthe()
    print(reproche)