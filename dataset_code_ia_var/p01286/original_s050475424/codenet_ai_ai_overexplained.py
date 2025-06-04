import sys  # Le module sys permet d'accéder aux objets utilisés ou maintenus par l'interpréteur, ici pour gérer les entrées/sorties standard.
readline = sys.stdin.readline  # readline est une fonction pour lire une ligne depuis l'entrée standard (typiquement, stdin du terminal).
write = sys.stdout.write  # write est une fonction pour écrire des chaînes de caractères sur la sortie standard.

from collections import deque  # deque est une structure de données de type file doublement enchaînée, ici utilisée pour le BFS (recherche en largeur).

# Définition d'une classe pour l'algorithme de flot maximum : Push-Relabel (pousser/re étiqueter)
class PushRelabel:
    # Constructeur de la classe prenant le nombre total de sommets N
    def __init__(self, N):
        self.N = N  # Nombre total de sommets du graphe.
        self.G = [[] for i in range(N)]  # Liste d'adjacence: pour chaque sommet, liste de ses arêtes sortantes.
        self.initial = [N]*N  # Tableau initialisant les hauteurs (labels) de chaque sommet à N (pour BFS).
        self.zeros = [0]*N  # Tableau initialisant à zéro (pour compter des sommets par niveau).

    # Ajouter une arête du sommet fr à to avec capacité cap
    def add_edge(self, fr, to, cap):
        # Structure d'arête : [destination, capacité résiduelle, arête réciproque]
        forward = [to, cap, None]  # Arête directe
        # L'arête précédente réciproque (backward) : [origine, cap inverse, lien réciproque]
        forward[2] = backward = [fr, 0, forward]  # Capacité inverse 0, lien vers l'autre arête
        self.G[fr].append(forward)  # Ajoute l'arête directe au sommet d'origine
        self.G[to].append(backward)  # Ajoute l'arête inverse au sommet destination
    
    # Ajouter deux arêtes entre v1 et v2 (multiarête) avec des capacités respectives cap1 et cap2
    def add_multi_edge(self, v1, v2, cap1, cap2):
        # Multiarête 1 : de v1 à v2, capacité cap1
        edge1 = [v2, cap1, None]
        # Multiarête 2 : de v2 à v1, capacité cap2, les arêtes réciproques se pointent l'une l'autre
        edge1[2] = edge2 = [v1, cap2, edge1]
        self.G[v1].append(edge1)  # Ajoute vers v2
        self.G[v2].append(edge2)  # Ajoute retour vers v1

    # Parcours BFS (exploration en largeur) pour initialiser les labels/hauteurs et brancher les sommets actifs
    def bfs(self, H, D, active, t, que=deque()):
        N = self.N  # Nombre de sommets
        B = [[] for i in range(N)]  # Liste pour stocker les sommets par hauteur (pour branch & bound du PR)
        que.append(t)  # Ajoute le sommet terminal t à la file pour commencer le BFS
        G = self.G  # Raccourci pour la liste d'adjacence
        
        H[:] = self.initial  # Initialisation des labels des sommets à N (=non visités)
        H[t] = 0  # Le terminal prend la hauteur zéro
        D[:] = self.zeros  # Compte le nombre de sommets à chaque hauteur
        D[0] = 1  # Un sommet au niveau 0 (=le terminal)
        cur = 0  # Hauteur courante la plus haute contenant des sommets actifs

        # Boucle principale du BFS
        while que:
            v = que.popleft()  # Défile de la file : sommet courant à traiter
            d = H[v] + 1  # On examine la prochaine hauteur
            for w, cap, backward in G[v]:  # Parcourt toutes les arêtes à partir de v
                # Si le sommet w a déjà une hauteur plus basse ou égale (déjà visité) ou
                # l'arête réciproque n'a pas de capacité (pas de résidu à repousser), passe
                if H[w] <= d or backward[1] == 0:
                    continue
                H[w] = d  # Attribue la nouvelle hauteur à w 
                if active[w] and d < N:  # Active w si possible et pas au-dessus du max
                    B[d].append(w)  # Regroupe w parmi les sommets d'altitude d
                    cur = d  # Met à jour la hauteur courante la plus élevée
                if d < N:
                    D[d] += 1  # Incrémente nombre de sommets à cette hauteur
                que.append(w)  # Ajoute w à la file pour poursuite du BFS
        return B, cur, d  # Retourne la structure de niveaux, la plus haute hauteur, la dernière visitée

    # Fonction principale pour calculer le flot de s (source) à t (puit)
    def flow(self, s, t):
        N = self.N  # Nombre de sommets
        H = [0]*N  # Labels/Hauteurs des sommets, initialisés à 0
        F = [0]*N  # Flot excédentaire à chaque sommet, initialisé à 0
        D = [0]*(N+1)  # Nombre de sommets pour chaque niveau de hauteur possible
        active = [0]*N  # Tableau marqueur des sommets actifs (où l'on doit pousser du flot)

        G = self.G  # Alias de la liste des arêtes

        F[s] = 10**18  # On injecte un très grand excédent de flot à la source
        active[s] = 1  # On marque la source comme active

        # BFS pour initialiser la structure par niveau depuis le terminal
        B, cur, gap = self.bfs(H, D, active, t)
        B[cur].append(s)  # On ajoute la source à la liste du niveau le plus élevé

        cnt = 0  # Compteur des opérations (pour relancer BFS périodiquement)
        while 1:
            # Descend jusqu'au niveau le plus haut qui a encore des sommets à traiter
            while cur >= 0 and not B[cur]:
                cur -= 1
            if cur < 0:
                break  # Si plus aucun sommet n'est actif à aucun niveau : terminé
            v = B[cur].pop()  # Prend un sommet actif au niveau courant
            if v == t:
                continue  # On n'agit pas sur le terminal

            hv = H[v]  # Hauteur/label actuel du sommet v
            if hv > gap:
                # Si hauteur de v dépasse le gap actuel, il ne peut pas atteindre t
                if hv < N:
                    D[hv] -= 1  # Diminue le nombre de sommets à cette hauteur
                hv = H[v] = N  # Relègue v à la hauteur max (désactive)
                continue

            rest = F[v]  # Quantité de flot qu'il nous reste à pousser à partir de v
            for e in G[v]:  # Pour chaque arête sortante de v
                w, cap, backward = e  # Arête vers w, capacité résiduelle, lien inverse
                # Si la capacité existe et si la hauteur permet de pousser
                if cap and hv > H[w] < gap:
                    d = min(rest, cap)  # Pousse le minimum entre le flot excédentaire restant et la capacité
                    e[1] -= d  # Réduit la capacité résiduelle
                    backward[1] += d  # Augmente la capacité résiduelle de l'arête réciproque
                    rest -= d  # Réduit le flot à pousser
                    F[w] += d  # Ajoute le flot nouvellement injecté à w
                    if not active[w]:  # Si w n'est pas encore dans sa liste de traitement
                        hw = H[w]  # Hauteur de w
                        B[hw].append(w)  # Insère dans la bonne hauteur
                        if cur < hw:
                            cur = hw  # Met à jour la hauteur max à traiter
                        active[w] = 1  # Marque w comme actif
                    if rest == 0:  # Si tout le flot a été poussé, termine cette boucle
                        break
            F[v] = rest  # Ce qu'il reste à pousser éventuellement au cycle suivant

            if rest == 0:
                active[v] = 0  # Désactive v si plus de flot à pousser
                continue

            h0 = H[v]  # Hauteur de départ
            hv = N  # Recherche une meilleure hauteur candidate pour relabel
            for w, cap, backward in G[v]:
                # Si une arête résiduelle existe, tente de réétiqueter v
                if cap and hv > H[w] + 1 <= gap:
                    hv = H[w] + 1  # Nouvelle hauteur candidate (loi du PR)
            if h0 != hv:  # Si la hauteur change, met à jour les comptes
                D[h0] -= 1
                if D[h0] == 0 and h0 < gap:  # Gap heuristic : coupe si plus de sommets à ce niveau
                    gap = h0  # Gap devient la nouvelle hauteur limite
                    hv = N  # On éloigne v du flux
                elif hv == gap:  # Si on atteint le gap, incrémente le gap pour l'itération suivante
                    gap += 1
                if hv < N:
                    D[hv] += 1

            H[v] = hv  # Relabel de v à sa nouvelle hauteur/rang
            if hv < N:
                B[hv].append(v)  # Replace v dans la liste du bon niveau
                if cur < hv:
                    cur = hv  # Met à jour cur si besoin
            else:
                active[v] = 0  # Désactive v si mis hors course

            cnt += 1
            if cnt % N == 0:  # Pour réinitialiser périodiquement (efficacité, résout la dégradation cumulative)
                B, cur, gap = self.bfs(H, D, active, t)
        return F[t]  # Le flot maximal atteint le terminal, on le retourne

# Fonction de résolution du problème d'affectation via le graphe de flot orienté
def solve():
    # Lecture des sept entiers en entrée principale (dimensions et cardinalités diverses)
    H, W, C, M, NW, NC, NM = map(int, readline().split())
    if H == -1:  # Condition d'arrêt (problème terminé)
        return False

    # Création d'un objet PushRelabel avec un nombre suffisant de sommets pour représenter le problème
    # Les différents indices sont soigneusement décalés pour séparer les "blocs" de sommets de chaque catégorie
    pr = PushRelabel(2 + H + 2*(W + NW) + 2*(C + NC) + (M + NM))
    # Définition des indices de début pour chaque partie du graphe, pour gérer les groupes de sommets par type (a, b, c, d)
    a0 = 2  # Début des sommets a (par exemple, des candidats)
    b0 = 2+H  # Début des premiers sommets de groupe b (par exemple, formations, etc.)
    b1 = 2+H+(W+NW)  # Début des deuxièmes sommets de groupe b (pour gestion multi-arêtes)
    c0 = 2+H+2*(W+NW)  # Début des premiers sommets c (pour un autre niveau de séparation)
    c1 = 2+H+2*(W+NW)+(C+NC)  # Début du deuxième sous-groupe de c
    d0 = 2+H+2*(W+NW)+2*(C+NC)  # Début du groupe d

    # Création des arêtes (chaque boucle gère un ensemble d'arêtes entre deux groupes du graphe)
    for i in range(H):  # Pour chaque sommet du groupe H
        pr.add_edge(0, a0+i, 1)  # Connecte la source (0) à chaque sommet a, capacité 1

    for i in range(W):  # Pour chacun des W éléments (premier groupe b)
        # Lecture de la ligne associée : premier nombre inutile (k), le reste contient les indices utiles (ws)
        k, *ws = map(int, readline().split())
        for w in ws:  # Pour chaque index de ws
            pr.add_edge(a0+w-1, b0+i, 1)  # Crée une arête de a vers b0+i
        pr.add_edge(b0+i, b1+i, 1)  # Connecte b0 à b1, capacité 1

    for i in range(W, W+NW):  # Pour les éléments du groupe NW, considérés comme "nouveaux"
        for j in range(H):  # Connecte chacun aux a existants
            pr.add_edge(a0+j, b0+i, 1)
        for j in range(C):  # Connecte sortant à chaque sommet c existant
            pr.add_edge(b1+i, c0+j, 1)
        pr.add_edge(b0+i, b1+i, 1)  # Lien entre sous-blocs b0 & b1

    for i in range(C):  # Pour chaque sommet c standard
        k, *cs = map(int, readline().split())
        for c in cs:
            pr.add_edge(b1+c-1, c0+i, 1)  # Connecte b1 vers c0
        pr.add_edge(c0+i, c1+i, 1)

    for i in range(C, C+NC):  # Pour les nouveaux c ("optionnels")
        for j in range(W):  # Connecte à tous les b existants
            pr.add_edge(b1+j, c0+i, 1)
        for j in range(M):  # Connecte à tous les d possibles
            pr.add_edge(c1+i, d0+j, 1)
        pr.add_edge(c0+i, c1+i, 1)  # Relie partie avant et partie arrière du nœud c

    for i in range(M):  # Pour chacun des M sommets d standard
        k, *ms = map(int, readline().split())
        for m in ms:  # Connecte les c1 relatifs à ces indices à d0+i
            pr.add_edge(c1+m-1, d0+i, 1)
        pr.add_edge(d0+i, 1, 1)  # Relie à la sortie (1 = puits)

    for i in range(M, M+NM):  # Pour les NM nouveaux "finaux"
        for j in range(C):  # Connecte à tous les c existants
            pr.add_edge(c1+j, d0+i, 1)
        pr.add_edge(d0+i, 1, 1)  # Relie au puits

    # Exécution de l'algorithme de flot max, sortie du résultat
    write("%d\n" % pr.flow(0, 1))
    return True

# Boucle principale : on appelle "solve" jusqu'à ce qu'une entrée -1 soit rencontrée (cas d'arrêt)
while solve():
    ...  # Le code "..." n'a pas d'effet, il s'agit d'un passe-passe pour la syntaxe Python 3.