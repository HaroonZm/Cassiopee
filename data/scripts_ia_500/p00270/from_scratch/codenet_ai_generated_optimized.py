import sys
import heapq
sys.setrecursionlimit(10**9)
input=sys.stdin.readline

S,R= map(int,input().split())
graph=[[] for _ in range(S+1)]
for _ in range(R):
    u,v,w= map(int,input().split())
    graph[u].append((v,w))
    graph[v].append((u,w))

a,b,Q= map(int,input().split())

def dijkstra(start):
    dist=[float('inf')]*(S+1)
    dist[start]=0
    h=[(0,start)]
    while h:
        cd,c=node=heapq.heappop(h)
        if dist[c]<cd:
            continue
        for nx,w in graph[c]:
            nd=cd+w
            if nd<dist[nx]:
                dist[nx]=nd
                heapq.heappush(h,(nd,nx))
    return dist

# plus court chemin de a et de b
distA=dijkstra(a)
distB=dijkstra(b)
# pour une question c,d
# vérifier:
# - chemin a->b minimal contenant c et d dans cet ordre avec segment c->d minimal
# Soit distA[c] + distCd + distB[d] == distA[b]
# ou encore distA[c] + distCd + distB[d] == distA[b]
# Ici distC->d minimal est distC[d]
# Dist depuis c nécessaire:
distC_list = [float('inf')] * (S+1)
# On va calculer dist depuis tous points ? Trop cher
# On doit calculer dist depuis c seulement Q fois => 40000 max
# 40000 fois dijkstra trop lourd
# Optimisation:
# Préparer dist depuis b pour vérif ordre et distance finale
# On note que ci et di changent à chaque question
# Autre idée : pré-calculer les distances entre tous les noeuds impossible S=1e5
# Solution: dijkstra multiple à la demande
# Pour chaque question, calculer dist c->d avec dijkstra. Q=40000 max sur R=200k OK si ok code.

# On peut pré-calculer dist c->d en faisant dijkstra à chaque question depuis c
# Ce sera valide car Q=40000 et dijkstra O(R log S), soit 200000 log100000 *40000 c'est trop lourd.

# Une autre façon:
# Vérifier équivalence:
# distA[b] == distA[c] + distC[d] + distB[d]

# mais nous n'avons pas distC[d] pré-calculé.
# Observons que distC[d] est nécessaire.

# Si on inverse les graph en un second graphe avec (v,u,w) on pourrait faire une dijkstra depuis d aussi.

# Donc on doit faire dijkstra depuis chaque c et fouiller distC[d].

# C est problématique.

# Une autre approche:
# On peut faire le calcul de dist depuis chaque c en ligne, mais vérifier à la volée pensée trop lourde.

# Solution: Précalculer les distances avec bidirectional Dijkstra modifié pour répondre en O(log n) par requête ? Complexe.

# Autre idée: Si on note:
# distA[b], distA[c], distB[d]
# et on a le segment c->d minimal, ie distC[d]=distC[d] calculé par dijkstra depuis c.

# Premier simplification possible:
# calculer une fois shortest path tree pour a et pour b
# voir si le chemin a->b passant par c,d existe

# Mais la question impose que le chemin p est shortest path from a to b, passant c then d, et segment c->d is shortest path.

# Cette condition est équivalente (avec triangle ineq strict) à:
# distA[b] == distA[c]+distC[d]+distB[d]

# Or distC[d] est inconnu sauf à faire dijkstra depuis c.

# Comme Q assez important, il faut accélérer.

# Autre idée:

# Precompute la distance depuis a et b.

# Calculer la distance entre c et d en utilisant un arbre de chemins minimum.

# Or tous chemins shortest path dans un graphe général n'est pas un arbre.

# Par contre, si on considère comme un arbre de chemins Dijkstra, on peut penser que cest un DAG.

# Solution possible: On ne sait pas éloigner des heures.

# En fait, on peut procéder comme suit :

# Faire un "visited check" simple :

# Pour chaque requête c,d:

# 1) Vérifier distA[b] == distA[c]+distC[d]+distB[d]

# distA[b], distA[c], distB[d] connus

# distC[d] : calculer sur place avec Dijkstra ou A*

# Cependant, on peut penser à la deuxième note, permettant de valider plus rapidement.

# Si on remarque que c,d doivent être sur le shortest path de a->b

# Une propriété intéressante : Le chemin doit être de longueur distA[b], imparfaite.

# Calculons l'écart:

# distA[b]-(distA[c]+distB[d]) == distC[d]

# Donc,  distC[d] = distA[b]-distA[c]-distB[d]

# Si la valeur est <0, impossible.

# Si c==d, toujours impossible car c!=d

# Avec cette formule, on peut testait si existe un chemin de c->d de poids (distC[d]) sans rechercher.

# Finalement si on suppose que le graphe est sans cycle négatif (non indiqué mais les poids sont positifs),

# et la distance distC[d] == distA[b]-distA[c]-distB[d]

# Donc on peut répondre au plus vite.

# Pour chaque requête, il faut vérifier:

# 1) distA[b] == distA[c] + distC[d] + distB[d]

# 2) distC[d] == distA[b] - distA[c] - distB[d]

# Donc on doit vérifier que distC[d] = cette valeur

# But on ne connaît pas distC[d]

# D'après la troisième condition, distC[d] est la distance entre c and d

# Donc on vérifie distC[d]== val

# On fait un dijkstra depuis c pour détecter distC[d], mais pour 40k requêtes c'est cher

# Alternative: Préparer un index permettant la distance c->d prompte

# On peut inverser tout le graphe et faire un dijkstra de tout, mais impossible.

# Autre idée importante:

# Le trajet p doit contenir c puis d selon ordre chemin a->b is shortest with c,d on it

# Or if distA[c] + distC[d] + distB[d]== distA[b]

# et que distC[d] == distC[d]

# alors oui

# On peut reécrire

# distA[c] + distC[d] + distB[d] == distA[b]

# => distC[d] == distA[b] - distA[c] - distB[d]

# Donc, la distance c->d doit valoir distA[b] - distA[c] - distB[d]

# Or les distances sont positives, donc on cherche si existe dist c->d = val

# Observation :

# Par inégalité trianglaire, on sait que dist c->d >= abs(distA[c] - distA[d]) à cause des longueurs positive

# Donc si distC[d] == distA[b] - distA[c] - distB[d] et ce dernier est >=0,

# On peut considérer répondre aux requêtes suivant avec un dijkstra à la volée.

# Mais q=40000 dijkstra trop cher

# Nouvelle idée :

# On fait un dijkstra inversé à partir de b pour déterminer distB[]

# On recherche un moyen de tester rapidement si distance c->d == x

# En raison de S, on envisage un index de proximité.

# Alternative: Pour ce problème, la solution donnée par AtCoder editorial pour ce problème "Railway Ticket" est :

# 1) Calculer dista = dist depuis a à chaque noeud

# 2) Calculer distb = dist depuis b à chaque noeud

# 3) Q queries: pour chaque c,d

#    - Si dista[b] == dista[c] + dist(c,d) + distb[d] and dist(c,d) == dist from c to d, alors Yes else No

# Pour dist(c,d), on exploite le fait que le graph est sans cycle negatif + positif distances

# Si pour les données on peut faire un 2eme Dijkstra depuis c demandé pour chaque question, ça marche pour Q=40k.

# Sinon on modifie code pour faire Dijkstra depuis tous c réunis

# C'est possible en raison de la borne Q=4e4

# On fait Dijkstra depuis c sur le graphe restreint 

# En Python optimisé, on peut réussir.

from collections import defaultdict

queries=[]
for _ in range(Q):
    c,d= map(int,input().split())
    queries.append((c,d))

# fonction dijkstra limitée dans le temps:

def dijkstra_c(source, targets):
    dist=[float('inf')]*(S+1)
    dist[source]=0
    h=[(0,source)]
    target_set = set(targets)
    cnt= len(target_set)
    while h and cnt>0:
        cd,c=node=heapq.heappop(h)
        if dist[c]<cd:
            continue
        if c in target_set:
            cnt-=1
            if cnt==0:
                break
        for nx,w in graph[c]:
            nd=cd+w
            if nd<dist[nx]:
                dist[nx]=nd
                heapq.heappush(h,(nd,nx))
    return dist

# on va grouper les queries par c afin d'optimiser l'appel de dijkstra_c
from collections import defaultdict

group_c = defaultdict(list)
for i,(c,d) in enumerate(queries):
    group_c[c].append((d,i))

res=["No"]*Q

for c, lst in group_c.items():
    targets = [d for d,_ in lst]
    distC = dijkstra_c(c, targets)
    for d,i in lst:
        # conditions à vérifier:
        # distA[b] == distA[c] + distC[d] + distB[d]
        if distA[b] == distA[c] + distC[d] + distB[d]:
            res[i]="Yes"

print("\n".join(res))