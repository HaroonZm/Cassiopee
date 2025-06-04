from heapq import heappush, heappop  # Importe deux fonctions du module heapq : heappush et heappop, utilisées pour manipuler des files de priorité (min-heaps en Python)
import sys  # Importe le module sys qui permet d'interagir avec l'entrée et la sortie standard (stdin et stdout)

readline = sys.stdin.readline  # Raccourci pour lire une ligne depuis l'entrée standard efficacement
write = sys.stdout.write       # Raccourci pour écrire une chaîne de caractères vers la sortie standard

def solve():
    # Lit la première ligne et décompose en trois entiers :
    # N : nombre de sommets (ou noeuds)
    # E : nombre d'arêtes (ou d'opérations, dépend du contexte)
    # T : cible (noeud auquel on s'intéresse, la destination finale)
    N, E, T = map(int, readline().split())

    # Lit la deuxième ligne et convertit chaque entrée en entier, stocke dans W :
    # W : liste d'états initiaux des N noeuds, probablement booléens (0 ou 1).
    *W, = map(int, readline().split())  # Le '*' sert à "dépaqueter" sur la liste W

    # G est une liste vide pour chaque noeud (peut rester inutilisée ici)
    G = [[] for i in range(N)]

    # R est une liste de listes : R[i] contient les indices des opérations qui produisent ou dépendent du noeud i+1
    R = [[] for i in range(N)]

    # C sera une liste d'E entiers à 0, stocke le nombre d'antécédents (ou la condition d'exécution) de chaque opération
    C = [0]*E

    # Q contiendra un tuple pour chaque opération : (noeud généré, [sources utilisées])
    Q = [None]*E

    # On lit maintenant les E lignes, chacune décrivant une opération/génération
    for i in range(E):  # Boucle sur chaque opération/arête
        # Pour chaque ligne, on récupère :
        # g : le noeud généré par cette opération
        # c : le nombre de conditions/requêtes à satisfaire avant que l'opération soit prête
        # s : la liste des sources nécessaires pour exécuter cette opération
        g, c, *s = map(int, readline().split())
        # Pour chaque source s, on ajoute l'opération actuelle à la liste R[e-1]
        for e in s:  # s contient les indices des sources (noeuds impliqués) pour cette opération
            R[e-1].append(i)
        # On enregistre le nombre de dépendances restantes dans C[i]
        C[i] = c
        # On mémorise pour chaque opération le tuple (noeud généré, liste des sources)
        Q[i] = (g, s)

    que = []  # Initialisation d'une liste qui sera utilisée comme file de priorité/min-heap
    INF = 10**9  # Valeur utilisée comme infinité (pour initialiser/repérer les états non encore atteints)

    # Fonction locale pour calculer le coût d'exécution d'une opération à partir de ses sources
    def calc(s):
        # Trie les sources s en fonction de dp[x-1], du plus grand au plus petit
        s.sort(key = lambda x: dp[x-1], reverse=1)
        r = 0  # Stockera le coût maximum observé durant la boucle
        for i, j in enumerate(s):
            # Pour chaque source, calcule la somme de son coût d'activation (dp[j-1]) et de sa position dans la file (i)
            r = max(r, i + dp[j-1])
        # Retourne le plus grand coût trouvé (c'est la "date" à laquelle toutes les sources sont prêtes)
        return r

    dp = [INF]*N  # dp[i] représente le coût minimal pour activer ou produire le noeud i+1

    # On initialise la file de priorité (et dp) avec tous les noeuds initiaux valides
    for i in range(N):
        if W[i]:  # Si le noeud i+1 existe déjà (est "allumé"/actif)
            dp[i] = 1  # Le coût pour obtenir ce noeud est de 1 (déjà prêt)
            # Pour chaque opération dépendante de ce noeud
            for j in R[i]:
                C[j] -= 1  # On décrémente, correspondant à une condition en moins à remplir pour l'opération j
                if C[j] == 0:  # Si toutes les conditions de cette opération sont remplies
                    g0, s0 = Q[j]  # On récupère le noeud généré et les sources de l'opération
                    heappush(que, (calc(s0), j))  # On ajoute à la file de priorité avec le coût calculé

    # On traite la file de priorité tant qu'elle est non vide
    while que:
        # Extraire le tuple (coût, index d'opération) le plus prioritaire (coût minimal)
        cost, e = heappop(que)
        g, s = Q[e]  # On récupère le noeud généré et les sources de cette opération
        if dp[g-1] < cost:  # Si on a déjà atteint mieux (coût inférieur) pour ce noeud
            continue  # On saute
        if cost < dp[g-1]:  # Sinon, si ce coût est meilleur, on met à jour
            dp[g-1] = cost  # Mise à jour du coût pour ce noeud généré
            # Pour chaque opération dépendant de ce noeud nouvellement généré
            for j in R[g-1]:
                C[j] -= 1  # Décrémenter le nombre de conditions restantes
                if C[j] <= 0:  # Si prêt (toutes conditions remplies)
                    g0, s0 = Q[j]  # On récupère (à nouveau) les infos sur cette opération
                    heappush(que, (calc(s0), j))  # On pousse dans le heap pour traitement futur

    # À la fin, si on a trouvé un coût pour atteindre le noeud but T-1 (car indices Python)
    if dp[T-1] != INF:
        write("%d\n" % dp[T-1])  # Affiche le coût minimal trouvé
    else:
        write("-1\n")  # Sinon, la cible est inatteignable, affiche -1

solve()  # Appelle la fonction principale pour lancer la résolution