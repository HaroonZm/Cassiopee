# Lecture du nombre d'éléments et du nombre de requêtes
N, Q = map(int, raw_input().split())

# Lecture de la liste des entiers
c = map(int, raw_input().split())

# Détermination de la valeur maximale dans la liste c
mxc = max(c)

# Initialisation d'une liste p pour marquer la présence des entiers dans c
# p[i] vaudra 1 si i est dans c, 0 sinon
p = [0] * (mxc + 1)
for i in c:
    p[i] = 1

# Construction de la liste l qui stocke l'indice du plus grand entier présent dans c
# inférieur ou égal à l'indice actuel
l = [0] * (mxc + 1)
num = 0  # num garde en mémoire la plus grande valeur rencontrée jusqu'à présent
for i in range(mxc + 1):
    l[i] = num
    if p[i]:
        num = i

def traiter_requete(q):
    """
    Calcule la plus grande valeur résiduelle possible de sp % q, 
    où sp est un élément de c obtenu en naviguant à travers le tableau l.
    
    L'algorithme commence à partir de la valeur maximale mxc et cherche des valeurs plus petites en
    fonction de la présence dans la liste c.
    
    Args:
        q (int): La valeur modulo pour laquelle on veut trouver la plus grande reste.
        
    Returns:
        int: La plus grande valeur de sp % q obtenue selon la procédure décrite.
    """
    sp = mxc  # point de départ initial
    ans = 0   # initialisation du maximum de reste trouvé
    while True:
        r = sp % q  # calcul du reste de sp divisé par q
        if r > ans:
            ans = r  # mise à jour du maximum si ce reste est supérieur
        if sp - r <= 0:
            break   # si on ne peut plus descendre, sortie de la boucle
        # passage à la plus grande valeur présente dans c inférieure ou égale à sp - r
        sp = l[sp - r]
    return ans

# Traitement des Q requêtes
for _ in range(Q):
    q = int(raw_input())
    # Impression de la réponse pour chaque requête
    print traiter_requete(q)