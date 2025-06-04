from collections import deque  # Importation du module deque depuis collections, permettant de créer une file (queue) efficace pour l’accès et la suppression des éléments à ses extrémités.

# Définition de la classe Graph pour représenter un graphe orienté (directed graph).
class Graph():
    # Méthode spéciale d'initialisation d'une instance de la classe.
    def __init__(self, n, edge, indexed=1):
        # n : nombre de sommets (nodes/vertices) dans le graphe.
        self.n = n  # Stockage du nombre de sommets dans l'attribut d'instance self.n.
        
        # Création d'une liste d'adjacence vide pour chaque sommet afin de représenter l’orientation originale du graphe.
        self.graph = [[] for _ in range(n)]  # Chaque élément correspond à un sommet. À l’index i, la liste contient les voisins accessibles directement depuis i.
        
        # Création d'une liste d'adjacence pour le graphe inversé (reverse graph), utile dans certains algorithmes.
        self.rev = [[] for _ in range(n)]  # Chaque élément contient les antécédents du sommet correspondant.
        
        # Création d’une liste pour compter le degré entrant (in-degree) de chaque sommet.
        self.deg = [0 for _ in range(n)]  # À l'index i, cette liste compte combien d'arêtes entrent dans le sommet i.
        
        # Remplissage du graphe avec les arêtes à partir de la liste d’arêtes passée en argument.
        for e in edge:  # La liste edge contient des couples de la forme (origine, destination).
            # On retire 'indexed' pour permettre d'utiliser des index de sommets soit 0-based (commence à 0), soit 1-based (commence à 1).
            start = e[0] - indexed  # Calcul de l'index de départ (origine) pour s'assurer de l'indice correct.
            end = e[1] - indexed  # Calcul de l'index de fin (destination).
            self.graph[start].append(end)  # Ajoute le sommet d'arrivée à la liste d'adjacence du sommet de départ (pour le graphe normal).
            self.rev[end].append(start)  # Ajoute le sommet de départ à la liste d’adjacence du graphe inversé (pour le sommet d’arrivée).
            self.deg[end] += 1  # Incrémente le degré entrant du sommet d’arrivée.
    
    # Méthode pour effectuer un tri topologique sur le graphe.
    def topological_sort(self):
        # Création d’une copie de la liste des degrés entrants : ainsi on ne modifie pas l’attribut original lors du traitement.
        deg = self.deg[:]  # deg[:] réalise une copie superficielle de la liste self.deg.
        
        # Initialisation de la liste des résultats avec tous les sommets ayant un degré entrant égal à zéro.
        res = [i for i in range(self.n) if deg[i] == 0]  # Ce sont les sommets sans prérequis.
        
        # Création d'une file (queue) à partir des sommets sources (degré entrant nul). On utilise deque pour des opérations efficaces.
        queue = deque(res)  # On met tous les sommets de res dans la file d’attente.
        
        # Liste pour marquer les sommets déjà utilisés / traités, initialement tous à False. Non utilisé dans cette implémentation en pratique.
        used = [False for _ in range(self.n)]  # Peut servir à éviter de repasser sur un sommet.
        
        # Boucle principale du tri topologique : on traite les sommets de la file un à un.
        while queue:  # Tant qu’il reste un sommet à traiter dans la queue...
            node = queue.popleft()  # Retirer le premier sommet de la file et le stocker dans node.
            
            # Parcourir tous les voisins accessibles directement depuis le sommet actuel.
            for adj in self.graph[node]:
                # Réduire le degré entrant du voisin car on enlève l’arête sortante du sommet courant vers ce voisin.
                deg[adj] -= 1  # On a "traité" une arête entrante.
                
                # Si ce voisin n’a plus aucune arête entrante après la modification, il est éligible pour être traité à son tour.
                if deg[adj] == 0:
                    queue.append(adj)  # Ajouter le voisin à la queue pour traitement futur.
                    res.append(adj)    # Ajouter le voisin à la liste des sommets triés.
        # Retourner la liste des sommets dans l'ordre topologique.
        return res

import sys  # Importe le module sys pour l'accès aux fonctionnalités système.
input = sys.stdin.readline  # Redéfinit la fonction input pour utiliser la lecture optimisée par ligne complète depuis l'entrée standard.

# Lecture de deux entiers depuis l’entrée standard, séparés par des espaces, qui représentent respectivement le nombre de sommets (N) et d’arêtes (M).
N, M = map(int, input().split())  # Conversion directe en entiers par unpacking.

# Création de la liste des arêtes, en lisant M lignes contenant chacune deux entiers, qui représentent l’origine et la destination des arêtes.
E = [tuple(map(int, input().split())) for _ in range(M)]  # Pour chaque ligne, créer un tuple (origine, destination).

# Instanciation de la classe Graph avec N sommets, les arêtes E, et un indexage commençant à 0 (cf. indexed = 0).
g = Graph(N, E, 0)  # On crée un graphe dont les sommets sont indexés de 0 à N-1.

# Appel de la méthode de tri topologique sur l’instance de Graph, conversion du résultat en chaînes de caractères, puis affichage ligne par ligne.
print('\n'.join(map(str, g.topological_sort())))  # Joint tous les éléments du tri topologique en une unique chaîne, chaque sommet sur une nouvelle ligne.