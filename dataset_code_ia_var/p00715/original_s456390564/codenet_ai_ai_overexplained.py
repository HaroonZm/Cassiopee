from collections import deque   # Importe la classe deque (double-ended queue) du module collections, utile pour la manipulation efficace de files.
import sys  # Importe le module sys pour accéder à sys.stdin et sys.stdout, permettant la lecture et l'écriture efficaces depuis/vers la console.
readline = sys.stdin.readline   # Assigne la méthode readline de sys.stdin à la variable readline pour une lecture de lignes rapide.
write = sys.stdout.write       # Assigne la méthode write de sys.stdout à la variable write pour une écriture rapide sans ajout automatique de retour à la ligne.

def solve():
    # Lecture du nombre d'arêtes (ou paires de chaînes).
    N = int(readline())  # Convertit la ligne lue en entier.
    if N == 0:
        return False  # Si N vaut 0, cela signifie la fin de l'entrée ; on quitte la boucle principale.
        
    L = 0  # Initialisation d'un compteur pour assigner un identifiant unique à chaque chaîne.
    n_map = {}  # Création d'un dictionnaire pour stocker la correspondance entre les chaînes et leur identifiant entier.

    def get(s):
        # Fonction interne qui retourne l'identifiant associé à la chaîne s.
        # Si la chaîne n'existe pas dans le dictionnaire, on lui assigne un nouvel identifiant.
        nonlocal L  # Permet de modifier la variable L définie dans la portée externe à celle de la fonction.
        if s in n_map:
            return n_map[s]  # Retourne l'identifiant de s si elle existe déjà.
        n_map[s] = L  # Sinon, on associe le prochain identifiant à la chaîne.
        L += 1         # Incrémente L pour le prochain identifiant disponible.
        return L-1     # Retourne l'identifiant qui vient d'être assigné.

    # Initialisation de 2 listes d'adjacence vides pour représenter les graphes directs et inverses.
    G = [[] for i in range(2*N)]   # G[a] contient les voisins accessibles à partir de 'a'.
    RG = [[] for i in range(2*N)]  # RG[a] contient les voisins accessibles à 'a' par arête inverse.

    # Lecture et construction du graphe.
    for i in range(N):  # Pour chaque ligne (arête), on procède comme suit :
        a, b = readline().strip().split("-")  # On lit la ligne, retire les espaces et la split au niveau du tiret, donnant deux chaînes.
        ka = get(a)  # On récupère (ou assigne) les identifiants de a et b.
        kb = get(b)
        G[ka].append(kb)     # On ajoute kb à la liste des voisins de ka (arête directe).
        RG[kb].append(ka)    # On ajoute ka à la liste des voisins de kb dans le graphe inversé.

    # Création d'une matrice F initialisée à -1 de dimension LxL.
    # F[v][w] stocke des relations spéciales entre les identifiants v et w (sera utilisé plus tard pour la construction du graphe G0).
    F = [[-1]*L for i in range(L)]
    for v in range(L):   # Pour chaque sommet du graphe
        for w1 in G[v]:         # Pour chaque voisin accessible (directement) à partir de v
            for w2 in G[v]:     # On prend tout couple de voisins directs
                F[w1][w2] = 1   # On marque une relation F[w1][w2] comme "1" (liés)
        for w1 in RG[v]:        # Pour chaque voisin accessible à v par arête inverse
            for w2 in RG[v]:    # On prend tout couple de voisins inverses
                F[w1][w2] = 1   # On marque la relation comme "1"
    for v in range(L):   # Enfin, pour des couples (voisin direct, voisin inverse)
        for w1 in G[v]:          # On prend chaque voisin direct
            for w2 in RG[v]:     # …et chaque voisin inverse
                F[w1][w2] = 0   # On force F[w1][w2] à 0
                F[w2][w1] = 0   # … idem pour l'autre ordre

    # Création d'un nouveau graphe G0 selon la matrice F.
    G0 = [[] for i in range(L)]  # Une liste d'adjacence simple pour G0.
    for v in range(L):           # On parcourt tous les sommets.
        for w in range(L):       # Pour tous les couples possibles
            if F[v][w] == 1:     # Si F[v][w] vaut 1, on ajoute une arête non orientée entre v et w dans G0.
                G0[v].append(w)  # Ajoute w comme voisin de v dans G0.
                G0[w].append(v)  # Ajoute v comme voisin de w dans G0 (arête non orientée).

    PS = []  # Liste pour stocker, pour chaque sommet, la parité des distances à tous les autres sommets ("coloration" du graphe).
    que = deque()  # Une file pour la recherche en largeur (BFS).

    # Pour chacun des sommets, on va lancer une BFS pour déterminer la parité d'accès à tous les autres.
    for i in range(L):          # Pour tous les sommets
        P = [-1]*L              # Initialise la liste de parité P : -1 indique "non visité". P[j] sera 0 ou 1 selon le niveau depuis i.
        que.append(i)           # Commence la BFS au sommet i.
        P[i] = 0                # Le sommet d'origine a la parité 0 (niveau 0).
        while que:              # On fait la BFS tant qu'il reste des sommets à traiter.
            v = que.popleft()   # On retire le sommet en tête de la file.
            p = P[v]            # On récupère sa parité/niveau.
            for w in G[v]:      # On parcourt tous les voisins directs de v (arêtes impaires)
                if P[w] != -1:
                    continue    # Si déjà visité, on saute.
                P[w] = p^1      # On affecte à w la parité opposée à celle de v, car franchir une arête directe (typiquement) change la parité.
                que.append(w)   # On ajoute w à la file pour continuer la traversal.
            for w in G0[v]:     # On parcourt tous les voisins dans G0 (arêtes qui ne changent pas la parité)
                if P[w] != -1:
                    continue    # Si déjà visité, on saute.
                P[w] = p        # La parité reste la même en suivant une arête de G0.
                que.append(w)   # On ajoute w à la file.
        PS.append(P)            # Ajoute le résultat pour le sommet i à la liste PS.

    write("%d\n" % L)  # Affiche le nombre total de sommets distincts (chaînes différentes rencontrées dans les données).

    M = int(readline())   # Nombre de requêtes/questions à traiter.
    for i in range(M):
        # Pour chaque requête, on lit deux chaînes séparées par un tiret.
        a, b = readline().strip().split("-")
        # On récupère les identifiants dans n_map, ou -1 si la chaîne n'existe pas (n'a jamais été vue).
        ka = n_map.get(a, -1)
        kb = n_map.get(b, -1)
        if ka == -1 or kb == -1:
            # Si l'une des chaînes n'a jamais été rencontrée, la réponse est forcément NO.
            write("NO\n")
            continue
        # On répond YES si PS[ka][kb] vaut 1 (accès avec une parité particulière déterminée précédemment), sinon NO.
        write("YES\n" if PS[ka][kb] == 1 else "NO\n")
    return True

while solve():
    ...  # Exécute la fonction solve tant qu'elle retourne True (lecture et traitement répétés des cas de test).