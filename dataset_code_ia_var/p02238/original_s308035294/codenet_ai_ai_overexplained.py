# Définition de la fonction DFS (Depth-First Search)
def dfs(index):
    # On indique que la variable 'count' utilisée ici est la même que celle définie au niveau global
    global count

    # On marque le temps de découverte (moment où le noeud 'index' est exploré pour la première fois)
    d[index] = count
    # On incrémente la variable compteur pour qu'elle indique le prochain instant disponible
    count += 1

    # Parcours de tous les voisins du noeud courant (index)
    for i in field[index]:
        # Si le noeud voisin 'i' a déjà été découvert (d[i] != 0)
        if d[i]:
            # On saute ce noeud, pour éviter de le visiter à nouveau
            continue
        # Appel récursif de DFS sur le voisin 'i'
        # On met à jour la variable 'count' après l'exploration complète de 'i'
        count = dfs(i)

    # Une fois que tous les voisins ont été explorés, on indique le temps de fin (fin de l'exploration de ce noeud)
    f[index] = count
    # On retourne la prochaine valeur de 'count', donc on ajoute 1
    return count + 1


# Lecture du nombre de noeuds dans le graphe
n = int(input())

# Initialisation de la liste des voisins pour chaque noeud
# On insère une liste factice à l'indice 0 parce que les noeuds sont indexés depuis 1
field = [[0, 0]]
# Pour chaque noeud du graphe (on répète 'n' fois)
for _ in range(n):
    # On lit une ligne, on la transforme en entiers
    # Le premier entier 'u' est l'index du noeud
    # Le deuxième entier 'k' indique le nombre de voisins de 'u'
    # Les entiers suivants, stockés dans 'v', sont les indices des voisins
    u, k, *v = map(int, input().split())
    # On ajoute la liste des voisins ('v') à la liste d'adjacence 'field'
    # L'indice du noeud 'u' correspond à la position de cette liste
    field.append(v)

# Création et initialisation de la liste des temps de découverte pour chaque noeud
# Tous les éléments sont initialement mis à 0 (aucun noeud n'a été visité)
d = [0 for _ in range(n + 1)]
# Création et initialisation de la liste des temps de fin pour chaque noeud
# Tous les éléments sont initialement mis à 0
f = [0 for _ in range(n + 1)]

# Initialisation du compteur qui servira à numéroter les moments de découverte et de fin
count = 1

# Parcours de tous les noeuds du graphe (les indices vont de 1 à n inclus)
for i in range(1, n + 1):
    # Si le noeud 'i' a déjà été visité (donc d[i] != 0), on passe au suivant
    if d[i]:
        continue
    # Si le noeud n'a pas encore été visité, on lance une exploration DFS à partir de ce noeud
    count = dfs(i)

# Après l'exploration DFS complète, on affiche les résultats
# Pour chaque noeud (de 1 à n inclus)
for i in range(1, n + 1):
    # On affiche l'indice du noeud, son instant de découverte et son instant de fin
    print(i, d[i], f[i])