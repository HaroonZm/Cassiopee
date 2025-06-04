def read_input():
    """
    Lit la taille du graphe et construit la matrice d'adjacence en lisant les données d'entrée.
    
    Retourne :
        N (int) : nombre de sommets du graphe.
        G (list de list d'entiers) : matrice d'adjacence représentant le graphe.
    """
    # Lecture du nombre de sommets
    N = int(input())
    # Initialisation d'une matrice N x N avec des zéros
    G = [[0 for _ in range(N)] for _ in range(N)]

    # Parcours de chaque ligne de description des arêtes
    for _ in range(N):
        # Lecture de la liste d'adjacence pour un sommet, sous la forme : u k v1 v2 ... vk
        ls = list(map(int, input().split()))
        u = ls[0] - 1  # Le sommet de départ, ajusté pour correspondre à l'indexation à partir de zéro
        # Parcours de tous les voisins à partir de la 3ème valeur
        for v in ls[2:]:
            G[u][v - 1] = 1  # Mise à jour de la matrice d'adjacence pour indiquer l'existence d'une arête
    return N, G

def print_adjacency_matrix(G):
    """
    Affiche la matrice d'adjacence ligne par ligne, les éléments d'une ligne étant séparés par des espaces.
    
    Argument :
        G (list de list d'entiers) : matrice d'adjacence à afficher.
    """
    for row in G:
        print(' '.join(map(str, row)))

def main():
    """
    Fonction principale orchestrant la lecture des données et l'affichage de la matrice d'adjacence.
    """
    N, G = read_input()
    print_adjacency_matrix(G)

if __name__ == "__main__":
    main()