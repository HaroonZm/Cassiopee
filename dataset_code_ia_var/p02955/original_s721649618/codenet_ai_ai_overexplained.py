# Définition de la fonction yakusu qui retourne tous les diviseurs de n
def yakusu(n):
    # Création de deux listes pour stocker les diviseurs trouvés :
    # lower_divisors pour les petits diviseurs, upper_divisors pour les grands diviseurs
    lower_divisors , upper_divisors = [], []
    # Initialisation d'un compteur i qui sera utilisé pour vérifier tous les nombres de 1 à la racine carrée de n
    i = 1
    # La boucle continue tant que i * i <= n, c'est-à-dire jusqu'à la racine carrée de n
    while i*i <= n:
        # Si n est divisible par i, c'est-à-dire que le reste de la division de n par i est 0
        if n % i == 0:
            # On ajoute i à la liste des petits diviseurs
            lower_divisors.append(i)
            # Si i n'est pas égal à n//i (pour ne pas ajouter deux fois la racine carrée si n est un carré parfait)
            if i != n // i:
                # On ajoute n//i à la liste des grands diviseurs
                upper_divisors.append(n//i)
        # Incrémentation de i pour tester le nombre suivant
        i += 1
    # Retourne la liste complète des diviseurs en pratiquant une concaténation de la première avec la seconde inversée
    return lower_divisors + upper_divisors[::-1]

# Lecture de deux entiers N et K à partir de l'entrée standard, séparés par un espace
N,K=map(int,input().split())
# Lecture d'une liste de N entiers séparés par un espace et création de la liste L
L=list(map(int,input().split()))
# Calcule la somme totale de tous les entiers dans la liste L
a=sum(L)
# Obtient tous les diviseurs de la somme a, puis inverse cette liste pour traiter les grands diviseurs en premier
R=yakusu(a)[::-1]

# Boucle pour traiter chaque diviseur potentiel (chaque valeur de s dans R)
for i in range(len(R)):
    # Initialisation des variables pour compter le nombre total de modifications pour "ajouter" ou "retirer" des éléments
    add=0  # Compte le nombre total à ajouter pour que les éléments deviennent multiples de s
    minus=0  # Compte le nombre total à enlever pour arriver à un multiple de s
    s=R[i]  # Le diviseur courant à traiter
    # Création de deux listes vides pour stocker les opérations élémentaires (détails des modifications pour chaque élément)
    A=list()  # Stocke les valeurs à retirer (minus)
    B=list()  # Stocke les valeurs à ajouter (add)
    # Parcourt chaque élément dans la liste L (pour chaque participant/élément)
    for j in range(N):
        k=L[j]    # Prend la valeur de l'élément courant
        a=k%s     # Calcule le reste (modulo) de k par s pour savoir combien il faut retirer pour arriver à un multiple
        b=s-a     # Calcule combien il faudrait ajouter à k pour arriver au multiple supérieur de s
        # Si retirer a coûterait plus qu'ajouter b, on préfère ajouter
        if a>b:
            add+=b       # On incrémente le coût total à ajouter
            B.append(b)  # On ajoute la quantité ajoutée à la liste B
        # Sinon, si retirer est moins coûteux que d'ajouter, on retire
        elif a<b:
            minus+=a      # On incrémente le coût total à retirer
            A.append(a)   # On ajoute cette quantité à la liste A
        else:
            # Si les coûts d'ajouter et de retirer sont égaux, on les compte comme des additions
            add+=a
            B.append(a)
    # Trie la liste A (valeurs à retirer) par ordre croissant
    A=sorted(A)
    # Trie la liste B (valeurs à ajouter) par ordre croissant
    B=sorted(B)
    # Si le total à retirer est égal au total à ajouter
    if minus==add:
        d=minus      # On peut les appeler "d", le coût total nécessaire pour l'équilibrage
        if d<=K:     # Si ce coût total ne dépasse pas la limite permise K
            print(s) # Affiche le diviseur actuel (la réponse)
            exit()   # Arrête immédiatement l'exécution du programme (puisqu'une solution a été trouvée)
    # Si le total à retirer dépasse le total à ajouter
    elif minus>add:
        # On détermine combien d'éléments parmi les plus grands de A on peut ignorer pour "équilibrer les deux côtés"
        q=(minus-add)//s   # La différence divisée par s donne combien d'éléments on doit ignorer
        # On somme les plus petits éléments de A (en ignorant les plus grands pour équilibrage)
        d=sum(A[:len(A)-q])
        if d<=K:     # Si le coût ne dépasse pas K, c'est valide
            print(s) # Affiche la valeur de s retenue
            exit()   # Fin immédiate
    else:
        # Même logique que ci-dessus, mais on s'intéresse maintenant aux ajouts (B) car add > minus
        q=(add-minus)//s   # Nombre d'éléments à ignorer du haut de B pour équilibrer
        # On somme les plus petits éléments de B
        d=sum(B[:len(B)-q])
        if d<=K:           # Si le coût ne dépasse pas K, c'est valable
            print(s)       # On affiche s
            exit()         # Fin immédiate du programme