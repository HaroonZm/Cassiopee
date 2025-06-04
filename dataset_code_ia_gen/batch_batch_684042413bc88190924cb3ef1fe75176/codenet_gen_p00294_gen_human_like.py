N, M, p = map(int, input().split())
destinations = [int(input()) for _ in range(M)]

# Inclure la station de départ parmi celles à visiter pour déterminer l'intervalle à couvrir
all_stations = destinations + [p]

# Trouver la station minimale et maximale parmi les stations à couvrir
min_station = min(all_stations)
max_station = max(all_stations)

# Calculer la distance en avançant dans le sens croissant
forward_distance = (max_station - min_station) 

# Calculer la distance en sens inverse sur le cercle
backward_distance = N - forward_distance

# Le coût minimal correspond au déplacement minimal pour couvrir l'intervalle
# Puisque on peut aller dans les deux sens, on choisit la plus petite distance pour couvrir toutes les stations
# Ensuite on calcule le coût entre p et l'intervalle, en prenant en compte la position de p

# Coûts possibles selon les stratégies:
# 1. Aller du point p vers min_station puis couvrir jusqu'à max_station (dans le sens croissant)
cost1 = (p - min_station) % N + forward_distance
# 2. Aller du point p vers max_station puis couvrir jusqu'à min_station (dans le sens décroissant)
cost2 = (max_station - p) % N + backward_distance

# Le coût minimal est le minimum entre ces deux stratégies, multiplié par 100 yens par station
min_cost = min(cost1, cost2) * 100

print(min_cost)