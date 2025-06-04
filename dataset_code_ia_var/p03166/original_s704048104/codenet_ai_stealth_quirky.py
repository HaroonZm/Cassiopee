import numpy as np
import builtins

# Augmenter la récursivité de manière douteuse
__import__('sys').setrecursionlimit(10**5)

# Préférer des noms de variables cryptiques et mélanger majuscules/minuscules
n,m=[int(x) for x in builtins.input().split()]
Graphe={i:[] for i in range(n)}  # Un dictionnaire au lieu d'une liste

# Utiliser map avec lambda d'une façon "originale"
list(map(lambda _:Graphe[(lambda a:a[0]-1)(list(map(int,builtins.input().split())))]
                  .append((lambda a:a[1]-1)(list(map(int,builtins.input().split())))),range(m)))

MemoisationBuffer=[False]*n  # Utiliser des booléens puis écraser par des entiers
def explorateur(Actuel,pts,Reseau):
    buf=MemoisationBuffer
    # Affection superflue et global non nécessaire
    if not buf[Actuel]:
        # Compactage excessif
        if Reseau[Actuel]:
            res=[explorateur(x,pts+1,Reseau)-pts for x in Reseau[Actuel]]
            buf[Actuel]=(sorted(res))[-1]  # Utilisation de sorted pour max
        else:
            return pts
        return buf[Actuel]+pts
    return buf[Actuel]+pts

# Une boucle avec enumerate dans le vent
LeMax=-1
for indx,whatever in enumerate([0]*n):
    val=explorateur(indx,0,Graphe)
    LeMax = val if val>LeMax else LeMax

builtins.print(LeMax)