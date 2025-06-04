# Demander à l'utilisateur de saisir un entier. Cela lira la saisie utilisateur depuis l'entrée standard
# avec input(), puis convertira la chaîne obtenue en entier à l'aide de int(), et stockera ce résultat dans la variable n.
n = int(input())

# Initialisation de la liste des listes d'adjacence, qui représentera le graphe sous forme de listes de voisins.
# La première case adj[0] est initialisée à None pour permettre un accès direct avec des indices à partir de 1.
adj = [None]

# On va lire les n lignes correspondant à la description de chaque sommet du graphe.
# La boucle for s’exécutera n fois, pour i allant de 0 à n-1 (comprise).
for i in range(n):
    # input() lit une ligne de l'entrée standard.
    # split() sépare la chaîne obtenue en une liste de chaînes, sur les espaces.
    # input().split()[2:] extrait la sous-liste à partir du 3e élément, car les 2 premiers sont inutiles (numéro du sommet et son degré).
    # map(int, ...) applique l'opération int() à chaque élément pour convertir les chaînes en entiers.
    # list() convertit l'objet map en une liste d'entiers.
    adji = list(map(int, input().split()[2:]))
    # On ajoute cette liste à la liste d'adjacence principale. Elle représente les voisins du sommet numéro i+1.
    adj.append(adji)

# Initialisation d'une liste pour garder trace des sommets déjà visités lors du parcours BFS.
# isSearched[0] est positionné à None car on ne considère pas l'indice 0. Les indices 1 à n sont initialisés à False,
# signifiant qu'aucun sommet n'a encore été visité.
isSearched = [None] + [False] * n

# Initialisation du tableau des distances, qui contiendra la distance du sommet source à chaque sommet.
# distance[0] est None pour les mêmes raisons que précédemment. Les autres valeurs sont initialisées à -1,
# indiquant qu'aucune distance n'est encore connue.
distance = [None] + [-1] * n

# Définition d'une fonction nommée BFS (pour Breadth-First Search, ou recherche en largeur)
# qui prend en paramètre 'u', le sommet de départ.
def BFS(u):
    # Initialisation du compteur de distance à 0. Cela correspond à la distance du sommet source à lui-même.
    d = 0
    # Marquage du sommet de départ comme visité pour éviter de le traiter à nouveau plus tard.
    isSearched[u] = True
    # Définition de la distance du sommet de départ comme 0, car il est à lui-même.
    distance[u] = d
    # Initialisation de la liste des sommets de frontière à explorer, qui contient au début uniquement le sommet de départ.
    edge = [u]
    # Boucle principale du BFS : tant qu'il y a des sommets à explorer à ce niveau,
    # on continue le traitement.
    while edge:
        # Création d'une nouvelle liste contenant les sommets du niveau courant.
        # On copie la liste edge dans q pour la traverser, puis edge sera réinitialisé juste après.
        q = list(edge)
        # Réinitialisation de edge à une liste vide pour le prochain niveau.
        edge = []
        # Incrémentation du compteur de distance : chaque itération de la boucle while correspond à un niveau de profondeur supplémentaire.
        d += 1
        # Boucle sur tous les sommets du niveau courant.
        for ce in q:
            # Boucle sur tous les voisins (nœuds adjacents) du sommet courant ce.
            for ne in adj[ce]:
                # On vérifie si ce voisin ne 'ne' n'a pas encore été visité.
                if not isSearched[ne]:
                    # Si ce voisin n'a pas été visité, on le marque comme visité tout de suite pour éviter les doublons.
                    isSearched[ne] = True
                    # On l'ajoute à la liste 'edge' des sommets à explorer au prochain niveau (la prochaine itération de la boucle while).
                    edge.append(ne)
                    # On enregistre la distance depuis le sommet source jusqu'à ce sommet voisin 'ne' comme d, le niveau courant.
                    distance[ne] = d

# On appelle la fonction BFS en commençant par le sommet numéro 1 (supposé être la racine ou le point de départ du graphe).
BFS(1)

# Parcours de la liste des distances pour les afficher.
# La fonction enumerate permet d’obtenir à la fois l’indice i (allant de 1 à n, car on saute le premier élément) et la valeur x de distance correspondante.
for i, x in enumerate(distance[1:], start=1):
    # Affichage de l'indice du sommet suivi de la distance calculée.
    print(i, x)