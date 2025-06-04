# Définition d'une constante représentant une valeur maximale très grande
# Cela sert à initialiser des variables de coût que l'on souhaitera minimiser dans le programme.
MAX_V = 999999999999999999999

# On entre dans une boucle infinie, typiquement utilisée pour traiter plusieurs cas jusqu'à une condition d'arrêt explicite
while 1:
    # Lecture d'une ligne d'entrée, séparation des valeurs, conversion en entiers et affectation à n (nombre de sommets) et m (nombre d'arêtes)
    n, m = list(map(int, input().split()))
    
    # Condition d'arrêt : si n vaut 0, on sort de la boucle (et donc du programme)
    if n == 0:
        break

    # Initialisation d'un dictionnaire nommé 'costs' 
    # Chaque clé correspond à un numéro de sommet (de 1 à n)
    # Chaque valeur associée à une clé est une liste vide qui servira à stocker les arêtes et leurs coûts partant de ce sommet
    costs = {x: [] for x in range(1, n + 1)}

    # Initialisation d'une liste de listes appelée 'passed'
    # Cela sert à marquer le passage par chaque nœud (de 0 à n)
    # Chaque nœud a deux positions (pour 2 états possibles de tickets gratuits restants)
    passed = [[0 for x in range(2)] for y in range(n + 1)]

    # Initialisation de la variable 'result' qui stocke les meilleurs coûts trouvés,
    # un pour chaque état de tickets gratuits restants (2 possibilités)
    # Les deux sont initialisés à la valeur MAX_V car on cherche à minimiser
    result = [MAX_V, MAX_V]

    # Boucle pour lire les m arêtes/connexions du graphe
    for i in range(m):
        # Lecture d'une arête : a et b sont les sommets connectés, c est le coût du déplacement entre eux
        a, b, c = list(map(int, input().split()))
        # Ajout de l'arête dans les deux sens (graphe non orienté)
        costs[a].append((b, c))
        costs[b].append((a, c))

    # Initialisation d'une liste appelée 'spam' qui jouera le rôle d'une file de trajets à explorer
    # Chaque élément est un tuple : (coût accumulé, sommet actuel, nombre de tickets gratuits restants)
    # On commence (coût=0, sommet=1, 2 tickets gratuits)
    spam = [(0, 1, 2)]  # (cost, num, free tickets remaining)

    # Boucle principale d'exploration des chemins : tant qu'il reste des états à traiter
    while len(spam) > 0:
        # Sélectionne l'élément ayant le plus petit coût actuel dans 'spam' (comme dans Dijkstra)
        mc = min(spam)
        # Puis on le retire de la liste pour traitement
        spam.remove(mc)

        # Détermination de l'indice dans 'passed' et 'result' selon le nombre de tickets gratuits restants
        # Si on a encore 2 tickets gratuits, tic_i=0, sinon tic_i=1
        tic_i = 0 if mc[2] == 2 else 1

        # Si le nombre de tickets gratuits restants n'est pas 1 et si on est déjà passé par ce nœud dans cet état, on saute ce chemin (évite doublons)
        if mc[2] != 1 and passed[mc[1]][tic_i] != 0:
            continue

        # Si on n'est pas dans l'état "1 ticket gratuit restant"
        if mc[2] != 1:
            # On marque ce nœud comme visité dans cet état
            passed[mc[1]][tic_i] = 1
            # Si on est arrivé au nœud final (n), on stocke le coût trouvé dans result
            if n == mc[1]:
                result[tic_i] = mc[0]

        # Si on a trouvé un chemin vers la fin (nœud n) avec un coût inférieur à MAX_V, on arrête l'exploration
        if max(result) < MAX_V:
            break

        # Explore tous les voisins accessibles à partir du nœud actuel (mc[1])
        for cv in costs[mc[1]]:
            # Première possibilité : avancer sans utiliser de ticket gratuit (on paye le coût)
            # Ceci n'est possible que si le nombre de tickets restants n'est pas 1
            if mc[2] != 1:
                # On ajoute à 'spam' un nouveau potentiel chemin résultant en payant le coût de l'arête
                spam.append((mc[0] + cv[1], cv[0], mc[2]))

            # Deuxième possibilité : utiliser un ticket gratuit si on en a encore (nombre de tickets > 0), donc pas de coût supplémentaire
            if mc[2] > 0:
                # On utilise un ticket gratuit pour aller vers le voisin, diminuant le nombre de tickets restants de 1
                spam.append((mc[0], cv[0], mc[2] - 1))

    # À la fin de tous les traitements, on affiche le coût minimum trouvé entre les deux options ('result')
    print(min(result))