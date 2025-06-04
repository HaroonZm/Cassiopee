# Demande à l'utilisateur d'entrer un entier n, qui représente le nombre de sommets (ou nœuds) du graphe.
n = int(input())

# Création d'une matrice d'adjacence carrée de taille n x n, initialisée avec des zéros.
# Une matrice d'adjacence est une structure de données utilisée pour représenter les connexions entre les nœuds d'un graphe.
# Ici, 'A' contient un 1 à la position [i][j] si un arc va du sommet i au sommet j, sinon 0.
A = [[0 for i in range(n)] for j in range(n)]

# On lit les arêtes du graphe à partir des entrées utilisateur.
# Pour chaque sommet, l'utilisateur entre d'abord l'indice du sommet 'u', le nombre d'arêtes sortantes 'k',
# puis la liste des sommets vers lesquels 'u' pointe (v_list).
for i in range(n):
    # On lit une ligne d'entrée(séparée par des espaces), et la convertit en une liste d'entiers.
    # 'u' est l'indice du nœud (numéroté à partir de 1), 'k' le nombre de voisins, le reste est la liste des voisins.
    u, k, *v_list = list(map(int, input().split()))
    # Pour chaque voisin 'v' dans la liste des voisins de 'u', on met A[u-1][v-1] à 1,
    # indiquant qu'il y a une arête de 'u' à 'v'.
    for v in v_list:
        A[u-1][v-1] = 1

# Initialisation des listes pour stocker les temps de découverte (d) et de fin (f) de chaque sommet.
# d[i] : temps où la première visite du nœud i a lieu lors du parcours en profondeur (DFS).
# f[i] : temps où la visite de tous les descendants du nœud i est terminée.
# On initialise d et f à 0, signifiant que les nœuds n'ont pas encore été visités.
d = [0] * n
f = [0] * n

# Déclaration de la variable t servant à compter le temps durant le DFS (exploration en profondeur).
# Au départ, ce compteur est mis à zéro.
t = 0

# Définition de la fonction récursive pour exécuter un parcours en profondeur (Depth-First Search).
# 'u' est l'indice (base zéro) du sommet à explorer depuis cet appel.
def dfs(u):
    global t  # On utilise la variable globale t pour garder le temps à travers toutes les appels récursifs.
    t += 1  # On incrémente le temps, car on découvre un nouveau sommet.
    d[u] = t  # On mémorise le temps de découverte pour ce sommet.

    # Parcourt tous les sommets du graphe pour chercher les voisins accessibles du sommet 'u'.
    for v in range(n):
        # Si un arc existe de u à v (A[u][v]==1) et que v n'a pas encore de temps de découverte (d[v]==0), on le visite.
        if A[u][v] == 1 and d[v] == 0:
            dfs(v)  # Appel récursif pour explorer le voisin v.

    # À la sortie de la boucle, on a fini de visiter tous les voisins accessibles à partir de 'u'.
    t += 1  # On incrémente à nouveau le temps, car on vient de finir d'explorer 'u' et tous ses descendants.
    f[u] = t  # On note le temps de fin pour ce sommet.

# Boucle principale pour lancer le DFS à partir de chaque sommet qui n'a pas encore été visité.
# Ceci permet de s'assurer qu'on explore tous les sommets même si le graphe n'est pas connexe.
for i in range(n):
    if d[i] == 0:  # Si le sommet i n'a pas encore été découvert.
        dfs(i)     # On lance le DFS sur ce sommet.

# Affichage des résultats à l'utilisateur.
# Pour chaque sommet (on compte à partir de 1 pour l'affichage, d'où i+1), 
# on affiche son indice, le temps de découverte et le temps de fin.
for i in range(n):
    print(i+1, d[i], f[i])