import copy  # Importe le module copy pour permettre la copie profonde des objets (pour éviter les modifications sur l'original)

n = int(input())  # Lit une ligne de l'entrée utilisateur, convertit la chaîne de caractères en entier, et assigne la valeur à n, qui représente la taille de la liste

# Lit une entrée utilisateur sous forme de chaîne, la découpe en éléments grâce à split() (qui retourne une liste de chaînes), 
# puis utilise map() pour convertir chaque chaîne en entier. Enfin, transforme le map en liste et l'assigne à a.
a = list(map(int, input().split()))

# Crée une copie profonde de la liste 'a' en utilisant copy.deepcopy, pour que b soit une nouvelle liste indépendante (même pour les objets internes).
b = copy.deepcopy(a)

# Trie (modifie) la liste 'b' sur place par ordre croissant, de sorte que b contienne maintenant les mêmes éléments que a, mais triés.
b.sort()

# Crée une liste vide, 'loop', destinée à contenir des listes représentant des cycles de permutation trouvés dans a en fonction de b.
loop = []

# Calcule la valeur minimale de la liste a en utilisant la fonction min(), puis l’assigne à la variable minp.
minp = min(a)

# Crée une liste t de taille n, remplie de zéros. Cette liste va servir à marquer les indices déjà visités lors de la détection des cycles.
t = [0 for i in range(n)]

# Commence une boucle 'while' infinie : elle ne s'arrêtera que par un 'break' à l'intérieur si une certaine condition est remplie.
while True:
    # Cherche l'indice du premier élément de t qui vaut 0, c'est-à-dire le premier indice non traité.
    i = t.index(0)
    
    # Initialise j comme la taille actuelle de la liste loop, pour savoir dans quelle sous-liste on ajoute les éléments du cycle courant.
    j = len(loop)
    
    # Ajoute une nouvelle sous-liste à loop, qui contiendra pour l'instant juste l'élément a[i], pour commencer à former un cycle à partir de ce point.
    loop.append([a[i]])
    
    # Marque cet indice 'i' comme traité, en mettant t[i] à 1.
    t[i] = 1
    
    # Commence une boucle interne pour parcourir ce cycle spécifique.
    while True:
        # Trouve l'indice dans la liste triée b qui correspond à la valeur en a[i] (c'est-à-dire, où cet élément devrait aller après tri).
        i = b.index(a[i])
        
        # Si cet indice dans t est déjà traité (c'est-à-dire t[i] == 1), alors le cycle est fermé et on sort de cette boucle interne.
        if t[i] == 1:
            break
        
        # Sinon, on marque l'indice comme traité.
        t[i] = 1
        
        # On ajoute la valeur correspondante de a[i] dans le cycle courant (la sous-liste loop[j]).
        loop[j].append(a[i])
    
    # Après avoir complété un cycle, on vérifie si tous les éléments de t ont été traités (leur somme vaut n si tous sont 1).
    # Si oui, on sort de la boucle principale (tous les cycles sont trouvés).
    if sum(t) == n:
        break
    # On incrémente j (même si en fait cela ne sert à rien ici puisque j sera recalculé à la prochaine itération).
    j += 1

# Initialisation de la variable cost à 0, elle servira à accumuler le coût minimal total de tous les cycles.
cost = 0

# On parcourt chaque sous-liste i (chaque cycle) dans loop.
for i in loop:
    # Si le cycle n'a qu'un seul élément, il n'est pas nécessaire de faire des opérations (déjà bien placé), donc on continue.
    if len(i) == 1:
        continue
    
    # On calcule la somme de tous les éléments du cycle et l'assigne à la variable ps.
    ps = sum(i)
    
    # La longueur du cycle (nombre d’éléments à permuter).
    pl = len(i)
    
    # L’élément de valeur minimale dans ce cycle.
    pm = min(i)
    
    # Coût de méthode 1 : effectuer les permutations en utilisant le plus petit élément du cycle (méthode du cycle standard)
    # ps  = la somme des valeurs, (pl - 2) * pm = coût additionnel pour replacer tous sauf deux éléments
    p1 = ps + (pl - 2) * pm
    
    # Coût de méthode 2 : utiliser la plus petite valeur globale (minp) comme pivot (méthode du swap "universel")
    # ps = somme, pm = min du cycle, (pl + 1) * minp = coût de plusieurs passages par le plus petit élément global
    p2 = ps + pm + (pl + 1) * minp
    
    # On ajoute au coût total le minimum entre les deux méthodes calculées.
    cost += min(p1, p2)

# Affiche le coût minimal total calculé pour réarranger la liste d'origine en ordre croissant via les cycles optimisés.
print(cost)