# Définition de la fonction principale du programme.
def main():
    # Lecture de la première ligne d'entrée utilisateur, qui représente le nombre de nœuds (ou sommets) dans le graphe/arbre.
    # la fonction input() demande une entrée utilisateur sous forme de chaîne de caractères,
    # int() convertit cette chaîne en un entier.
    n = int(input())

    # Lecture des n-1 arêtes (car un arbre de n nœuds possède n-1 arêtes).
    # On utilise une compréhension de liste pour traiter chaque ligne d'entrée correspondante à une arête.
    # Pour chaque arête, qui est composée de deux valeurs séparées par un espace, on les transforme en entiers.
    # Ensuite, on trie la liste de ces deux entiers pour garantir un ordre croissant (facilite le travail ultérieur).
    # [0]*(n-1) crée une liste de n-1 zéros pour pouvoir itérer exactement n-1 fois sans se servir des valeurs 0, seulement pour le nombre de répétitions.
    ab = [sorted(list(map(int, input().split()))) for _ in [0]*(n-1)]

    # Lecture de la liste 's', composée de n entiers, qui sont tous les entiers lus sur une seule ligne d'entrée utilisateur.
    # map(int, ...) transforme chaque chaîne en entier, list(...) les rassemble dans une liste.
    s = list(map(int, input().split()))

    # Création de la structure de données représentant le graphe sous forme de liste d'adjacence.
    # [ [] for _ in [0]*n ] crée une liste de n sous-listes vides, une pour chaque nœud.
    g = [[] for _ in [0]*n]

    # Pour chaque arête (a, b), ajouter b-1 dans la liste des voisins de a-1.
    # On soustrait 1 à chaque extrémité pour passer de l'indexation 1-based (souvent dans les entrées) à la 0-based (Python).
    [g[a-1].append(b-1) for a, b in ab]
    # Pareil mais dans l'autre sens, pour que le graphe soit non-orienté : on ajoute a-1 dans la liste des voisins de b-1.
    [g[b-1].append(a-1) for a, b in ab]

    # Définir root comme étant le nœud racine, ici 0 (premier nœud, convention).
    root = 0  # 根

    # d va contenir la distance (nombre d'arêtes) entre la racine et chaque nœud, initialisée à -1 (inconnu).
    d = [-1] * n  # 根からの距離

    # La distance de la racine à elle-même est 0.
    d[root] = 0

    # Initialisation de la file de nœuds à explorer, commence avec la racine.
    q = [root]

    # Un compteur pour suivre le niveau du parcours (utilisé pour attribuer la distance).
    cnt = 0

    # Début du parcours en largeur (BFS, Breadth-First Search).
    while q:
        # Chaque fois qu'on augmente de niveau, cnt augmente de 1.
        cnt += 1

        # Nouvelle file d'attente pour le niveau suivant.
        qq = []

        # On examine chaque nœud du niveau actuel.
        while q:
            # Retire un nœud de la file q (ici on utilise pop() donc la file fonctionne comme une pile, mais cela ne change rien pour BFS avec qq).
            i = q.pop()

            # Pour chaque voisin j de i, on va voir si on l'a déjà visité.
            for j in g[i]:
                # Si l'on n'a pas encore défini la distance du voisin j (donc il n'a pas encore été visité).
                if d[j] == -1:
                    # La distance depuis la racine de j est le niveau actuel, soit cnt.
                    d[j] = cnt
                    # On ajoute le voisin à la nouvelle file d'attente qq.
                    qq.append(j)
        # Passe au niveau suivant en mettant qq comme nouvelle file d'attente.
        q = qq

    # On crée une liste des paires [distance, index_du_nœud], 
    # pour chaque nœud (i, j = distance depuis la racine, i = index).
    dd = [[j, i] for i, j in enumerate(d)]
    # On trie les paires par ordre décroissant de distance, ainsi les nœuds plus loin de la racine sont en premier.
    dd.sort(key=lambda x: -x[0])
    # On extraie uniquement l'index du nœud (on ignore la distance) pour obtenir la séquence des nœuds du plus éloigné au plus proche de la racine.
    dd = [j for i, j in dd]

    # Initialisation d'un tableau dp où chaque valeur est 1, de taille n; dp[i] représentera le nombre de descendants de i, y compris i.
    dp = [1] * n

    # Pour chaque nœud, commençant par les plus éloignés de la racine, on met à jour dp.
    for i in dd:
        # On regarde tous les voisins de i.
        for j in g[i]:
            # Si le voisin j est plus loin de la racine que i,
            # cela signifie que j est un enfant de i dans l'arbre.
            if d[j] > d[i]:
                # Ajouter le nombre de descendants de j à celui de i.
                dp[i] += dp[j]

    # Initialisation de la liste des réponses.
    ans = []

    # Pour chaque arête (a, b), on procède à des calculs selon la problématique (notamment pour retrouver des poids donnés des arêtes).
    for a, b in ab:
        a -= 1  # Ajustement à l'indice Python (0-based)
        b -= 1
        # On veut toujours que a soit le plus proche de la racine que b.
        if d[a] > d[b]:
            a, b = b, a

        # ay représente le nombre de nœuds dans le sous-arbre qui s'éloigne de la racine à partir du fils (b),
        # moins 1 car on ne compte pas la racine du sous-arbre lui-même.
        ay = dp[b] - 1

        # ax est le nombre de nœuds dans le reste de l'arbre sauf ceux du sous-arbre.
        # n-2-ay : on enlève le nœud a et tous les descendants de b.
        ax = n - 2 - ay

        # Si la différence ax - ay vaut zéro, alors le problème est sous-déterminé (division par zéro, information insuffisante).
        if ax - ay == 0:
            # On marque la réponse au moyen d'une valeur imaginaire spéciale (1j) qui sert de drapeau plus loin.
            ans.append(1j)
        else:
            # Calcul de la valeur demandée pour cette arête, à l'aide des valeurs de s sur les extrémités ajustées par la différence ax-ay.
            ans.append(abs(s[a] - s[b]) // abs(ax - ay))

    # On crée un dictionnaire pour retrouver rapidement quelle est la valeur que l'on a calculée pour chaque arête (a, b).
    ab_dict = {(ab[i][0] - 1, ab[i][1] - 1): ans[i] for i in range(n - 1)}

    # Si "1j" (notre drapeau pour indétermination) se trouve dans ans, il faut résoudre ce cas spécial.
    if 1j in ans:
        # On compte combien de fois se produit ce cas spécial.
        cnt = 0
        for i in ans:
            if i == 1j:
                cnt += 1
        # Si plus d'un cas spécial, impossibilité de résoudre, donc on arrête la fonction.
        if cnt > 1:
            return

        # On trouve l'indice p de l'arête indéterminée (celle qui a 1j).
        p = ans.index(1j)
        # Réinitialisation de la file d'attente pour un nouveau parcours à partir de la racine.
        q = [root]

        # temp_1 et temp_2 vont servir à accumuler des valeurs pour le calcul de l'arête indéterminée.
        temp_1 = 0
        temp_2 = 0
        while q:
            qq = []
            while q:
                i = q.pop()
                for j in g[i]:
                    # Même logique que précédemment pour parcourir l'arbre de la racine vers les feuilles.
                    if d[j] > d[i]:
                        a, b = min(i, j), max(i, j)
                        # On récupère la valeur précédemment calculée pour l'arête (a, b).
                        temp = ab_dict[(a, b)]
                        # Si cette arête est celle qui était indéterminée, on accumule le nombre de descendants dans temp_2.
                        if temp == 1j:
                            temp_2 = dp[j]
                        else:
                            # Sinon, temp_1 accumule la somme pondérée par le nombre de descendants.
                            temp_1 += dp[j] * temp
                        qq.append(j)
            q = qq

        # On "devine" la valeur manquante à partir de la formule du problème et des sommes accumulées.
        ans[p] = (s[0] - temp_1) // temp_2

    # Affiche chaque résultat calculé pour chaque arête (un par ligne, dans l'ordre d'entrée des arêtes).
    for i in ans:
        print(i)

# Appel de la fonction main afin de démarrer le traitement lorsque le script est exécuté.
main()