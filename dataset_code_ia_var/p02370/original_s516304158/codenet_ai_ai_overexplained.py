from collections import deque  # Import de la classe deque depuis le module collections, nécessaire pour la file d'attente efficace

def topologicalSort(v, e):
    # Déclaration de variables globales pour les utiliser dans d'autres fonctions
    global color, out, indeg

    # Initialisation du tableau 'color'
    # Ce tableau va contenir la couleur de chaque sommet pour savoir s'il a été visité ou non
    # "white" signifie non visité, "gray" signifie que le sommet est en cours de traitement
    color = ["white" for _ in range(v)]

    # Initialisation de la liste 'indeg'
    # Chaque élément correspond à un sommet et c'est une liste contenant deux éléments :
    #   0 : le nombre d'arêtes sortantes depuis ce sommet (on l'utilise comme degré inverse pour cet algorithme)
    #   1 : la liste des sommets vers lesquels il existe une arête entrante (parents)
    indeg = [[0, []] for _ in range(v)]

    # Initialisation de la liste 'out' qui stockera le résultat du tri topologique dans l'ordre de visite
    out = []

    # Lecture des 'e' arêtes du graphe
    for i in range(e):
        # Lecture d'une arête de s à t (s est la source, t la destination)
        s, t = map(int, input().split())
        # Incrémentation du compteur d'arêtes sortantes de s
        indeg[s][0] += 1
        # Ajout du sommet 's' à la liste des parents de 't'
        indeg[t][1] += [s]

    # Parcours de tous les sommets du graphe
    for i in range(v):
        # Si le sommet n'a aucune arête sortante et n'a pas encore été visité ("white")
        # On lance une recherche BFS à partir de ce sommet
        if indeg[i][0] == 0 and color[i] == "white":
            BFS(i)

    # On retourne le résultat dans l'ordre inverse de l'ordre dans lequel ils ont été ajoutés
    # pour obtenir le tri topologique correct
    return out[::-1]

def BFS(s):
    # Création d'une file d'attente vide Q pour parcourir le graphe en largeur
    Q = deque([])

    # Ajout du sommet de départ 's' dans la file d'attente
    Q.append(s)
    # Marquage de ce sommet comme en cours de traitement ("gray")
    color[s] = "gray"

    # Boucle tant que la file d'attente Q n'est pas vide
    while len(Q) != 0:
        # On enlève et récupère (pop) le premier élément de la file d'attente
        u = Q.popleft()
        # Ajout du sommet 'u' à la liste du tri topologique
        out.append(u)

        # Parcours de la liste des parents de 'u'
        for i in indeg[u][1]:
            # On diminue de 1 le nombre d'arêtes sortantes du parent
            indeg[i][0] -= 1
            # Si ce parent n'a plus d'arêtes sortantes et qu'il n'a pas encore été visité
            if indeg[i][0] == 0 and color[i] == "white":
                # On le marque comme en cours de traitement ("gray")
                color[i] = "gray"
                # On l'ajoute dans la file d'attente pour traitement ultérieur
                Q.append(i)

# Lecture du nombre de sommets (v) et du nombre d'arêtes (e) au format "v e" depuis l'entrée standard (input clavier)
v, e = map(int, input().split())

# Exécution du tri topologique et affichage de chaque sommet dans le bon ordre
for i in topologicalSort(v, e):
    print(i)  # Affichage de l'identifiant du sommet, un par ligne