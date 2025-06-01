def f():
    # Importation des fonctions heappop et heappush depuis le module heapq.
    # Ces fonctions permettent de manipuler une structure de données appelée tas (heap),
    # utilisée ici pour gérer un ensemble d'éléments triés selon une clé.
    from heapq import heappop, heappush
    
    # Lecture depuis l'entrée standard d'une valeur entière N.
    # Cette valeur N représente probablement le nombre d'entités (par exemple, d'équipes ou joueurs).
    N = int(input())
    
    # Initialisation d'une liste 'r' de taille N remplie de zéros.
    # Cette liste servira à stocker un score ou un cumul associé à chaque entité.
    r = [0] * N
    
    # Calcul du nombre de matchs ou paires à lire.
    # L'expression N*~-N//2 s'interprète comme N*(N-1)//2 en utilisant l'opérateur ~ (bitwise NOT).
    # En effet, ~a == -a-1, donc ~-N == N-1.
    # On boucle donc sur un itérable qui répète N*(N-1)//2 fois une valeur quelconque (ici 0) pour itérer le bon nombre de fois.
    for _ in [0] * (N * ~-N // 2):
        # Lecture de quatre entiers a,b,c,d correspondant probablement à deux entités (a,b) et leurs scores respectifs (c,d).
        a, b, c, d = map(int, input().split())
        
        # Mise à jour du score dans la liste 'r' pour l'entité a-1.
        # L'index a-1 est utilisé car les entités semblent être numérotées à partir de 1,
        # tandis que les indices Python commencent à 0.
        # On ajoute 3 points si c > d, 1 point si c == d, sinon 0 point.
        r[a - 1] += 3 * (c > d) + (c == d)
        
        # Mise à jour similaire pour l'entité b-1.
        # 3 points si d > c, 1 point si d == c, sinon 0.
        r[b - 1] += 3 * (d > c) + (d == c)
    
    # Initialisation d'une liste de listes 'b' contenant N*3 sous-listes vides.
    # Cette structure sera probablement utilisée pour regrouper les indices d'entités par leur score.
    b = [[] for _ in [0] * N * 3]
    
    # Pour chaque entité i dans la plage de 0 à N-1
    for i in range(N):
        # On ajoute l'indice i dans la sous-liste correspondant à son score r[i].
        # Cela sert à indexer par score les entités.
        b[r[i]] += [i]
    
    # Initialisation d'une liste vide qui servira de tas (heap) prioritaire.
    pq = []
    
    # Parcours de chaque entité avec son indice i et son score s.
    for i, s in enumerate(r):
        # Insertion dans le tas d'un tuple [-s, i].
        # On utilise -s afin d'obtenir un tas de maximum car heapq est un min-heap par défaut.
        # Ainsi, les entités avec le score le plus élevé (-s le plus faible) seront prioritaires.
        heappush(pq, [-s, i])
    
    # Initialisation de la variable rank qui indiquera le rang actuel lors du classement.
    rank = 1
    
    # Initialisation du rang qui sera affiché à l'utilisateur, servant à gérer les égalités.
    display_rank = 1
    
    # Initialisation d'une variable prev_score à l'infini pour comparer les scores lors du classement.
    prev_score = float('inf')
    
    # Boucle tant que le tas n'est pas vide : on extrait les éléments par ordre de score décroissant.
    while pq:
        # Extraction du prochain élément, qui sera celui ayant le score le plus élevé (dans l'ordre min-heap inversé).
        s, i = heappop(pq)
        
        # Si le score actuel est différent du score précédent,
        # cela signifie qu'on change de rang, donc on met à jour rank avec display_rank.
        if s != prev_score:
            rank = display_rank
        
        # Attribution du rang calculé à l'entité i dans la liste r à la position i.
        r[i] = rank
        
        # Incrémentation de display_rank pour passer au numéro suivant.
        display_rank += 1
        
        # Mise à jour du score précédent avec le score actuel.
        prev_score = s
    
    # Affichage final des rangs pour toutes les entités, un par ligne.
    # L'opérateur * dépaquette la liste r pour envoyer chaque élément à print séparément.
    # sep='\n' force un affichage avec retour à la ligne entre chaque rang.
    print(*r, sep='\n')

# Appel de la fonction f pour exécuter le programme.
f()