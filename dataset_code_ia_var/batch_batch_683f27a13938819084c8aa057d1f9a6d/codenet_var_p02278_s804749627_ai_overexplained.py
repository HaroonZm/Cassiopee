# Demander à l'utilisateur d'entrer un entier, le nombre d'éléments à lire
# La fonction input() lit une chaîne de caractères de l'entrée standard (le clavier)
# int(...) convertit cette chaîne en entier
n = int(input())

# Demander à l'utilisateur d'entrer une séquence d'entiers séparés par des espaces
# input().split() découpe la chaîne d'entrée en une liste de chaînes, une pour chaque nombre entré
# map(int, ...) applique la fonction int à chaque chaîne de la liste, convertissant chaque élément en entier
# list(...) crée une liste de ces entiers
w = list(map(int, input().split()))

# Créer une copie triée de la liste w, pour servir de référence à la position "correcte" de chaque élément
# sorted(w) retourne une nouvelle liste contenant les mêmes éléments que w, mais triés dans l'ordre croissant
s = sorted(w)

# Initialiser la variable cost à 0 pour suivre le coût total (cumulé) des échanges effectués
cost = 0

# Début d'une boucle qui va de i=0 à i=n-1 (en Python, range(n) génère [0, 1, ..., n-1])
for i in range(n):
    # Prendre la valeur qui devrait être à la position i dans une liste triée,
    # c'est-à-dire le i-ème plus petit élément
    now_v = s[i]
    
    # Trouver l'indice actuel de cette valeur now_v dans la liste w (qui est possiblement non triée à cette étape)
    now_idx = w.index(s[i])
    
    # Initialiser un compteur j à 0 pour suivre combien de fois une opération d'échange (swap) a été effectuée
    j = 0
    
    # Effectuer des échanges jusqu'à ce que l'élément now_v arrive à sa position correcte (i)
    # Tant que l'indice actuel de now_v (now_idx) est strictement supérieur à la position d'arrivée (i)
    while now_idx > i:
        # Incrémenter le nombre d'échanges effectués
        j += 1
        
        # Trouver la valeur (target_v) devant être à la place where now_v se trouve
        # On la récupère dans la liste triée, à l'index now_idx
        target_v = s[now_idx]
        
        # Trouver l'indice actuel de cette valeur cible dans w
        target_idx = w.index(target_v)
        
        # Ajouter à cost la valeur de l'élément cible (celle qui va être déplacée), ceci est la "pénalité" de l'échange
        cost += w[target_idx]
        
        # Échanger les deux éléments dans la liste w :
        # w[now_idx], w[target_idx] = w[target_idx], w[now_idx] réalise un échange in-place
        temp = w[now_idx]
        w[now_idx] = w[target_idx]
        w[target_idx] = temp
        
        # Mettre à jour now_idx pour pointer vers la nouvelle position de now_v après l'échange
        now_idx = target_idx
    
    # À ce point :
    # - now_v : la valeur à placer
    # - j     : le nombre d’échanges effectués pour ce now_v
    # Analyser deux stratégies pour minimiser le coût :
    # 1. Effectuer j échanges directs, coût total : now_v * j (à chaque mouvement, on paye la valeur déplacée)
    # 2. Utiliser la valeur minimale globale s[0] pour aider à l'échange (moyennant certains échanges supplémentaires)
    #    Ceci consiste à : swap now_v avec s[0] (coût : now_v + s[0]), effectuer les (j) échanges en utilisant s[0],
    #    puis remettre now_v et s[0] à leur place (encore now_v + s[0])
    #    Coût : now_v*2 + s[0]*(j+2)
    # On choisit le coût minimal entre ces deux stratégies et on l’ajoute au coût total
    cost += min(now_v * j, now_v * 2 + s[0] * (j + 2))

# Afficher le coût final total, c'est-à-dire le coût minimum nécessaire pour trier la liste par ces échanges
print(cost)