# Lecture de la taille du tas (+1 pour faciliter l'utilisation d'un tableau indicé à partir de 1)
H = int(input()) + 1

# Lecture des éléments du tas et insertion d'un zéro en tête pour indexation à partir de 1
A = [0] + list(map(int, input().split()))

def h(i):
    """
    Accomplit la procédure de 'heapify-down' (entretien d'un tas max) à partir de l'indice i.
    
    Parameters
    ----------
    i : int
        L'indice du nœud courant auquel appliquer la procédure de corrélation du tas.
        
    Effet de bord
    -------------
    Modifie le tableau global A en place pour s'assurer que le tas max est respecté à partir de i.
    """
    l = 2 * i       # indice du fils gauche
    r = l + 1       # indice du fils droit
    g = i           # indice du plus grand parmi parent, fils gauche et fils droit
    
    # Vérifie si le fils gauche existe et s'il est plus grand que le parent
    if l < H and A[i] < A[l]:
        g = l
        
    # Vérifie si le fils droit existe et s'il est plus grand que le maximum actuel
    if r < H and A[g] < A[r]:
        g = r
    
    # Si l'un des enfants est plus grand, on échange et continue récursivement
    if g > i:
        A[i], A[g] = A[g], A[i]
        h(g)

# Construction du tas max en appliquant h à chaque nœud interne (à partir du milieu vers la racine)
for i in range(H // 2, 0, -1):
    h(i)

# Affichage du tas construit (sans l'élément d'indice 0), précédé d'un espace
print(' ' + ' '.join(map(str, A[1:])))