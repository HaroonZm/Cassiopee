import sys

# Augmenter la limite de récursion pour gérer de grands graphes
sys.setrecursionlimit(10 ** 9)

# Lecture du nombre de personnes et de clubs
number_of_people, number_of_clubs = map(int, input().split())

# Initialisation de la liste d'adjacence pour représenter le graphe biparti
adjacency_list = [[] for _ in range(number_of_people + number_of_clubs)]

# Remplissage de la liste d'adjacence avec les connexions personnes-clubs
for person_index in range(number_of_people):
    input_data = list(map(int, input().split()))
    clubs_for_person = input_data[1:]
    for club_number in clubs_for_person:
        club_node_index = number_of_people + club_number - 1
        adjacency_list[person_index].append(club_node_index)
        adjacency_list[club_node_index].append(person_index)

# Tableau pour marquer les sommets visités lors du parcours en profondeur
visited_nodes = [False] * (number_of_people + number_of_clubs)

# Fonction récursive pour effectuer un DFS et marquer les sommets accessibles
def depth_first_search(node_index):
    visited_nodes[node_index] = True
    for neighbor_index in adjacency_list[node_index]:
        if not visited_nodes[neighbor_index]:
            depth_first_search(neighbor_index)

# Lancer le DFS à partir du premier individu (sommet 0)
depth_first_search(0)

# Vérifier si toutes les personnes (premiers n sommets) sont connectées
if all(visited_nodes[:number_of_people]):
    print("YES")
else:
    print("NO")