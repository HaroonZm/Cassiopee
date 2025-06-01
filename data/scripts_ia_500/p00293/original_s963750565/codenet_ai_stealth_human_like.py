import sys
import itertools

fd = sys.stdin

# Bon ici on récupère deux listes de paires je crois
first_pair, second_pair = [map(int, fd.readline().split()) for _ in range(2)]
n = next(first_pair)
m = next(second_pair)

# C’est censé être des horaires ou un truc du genre, donc on emballe ça en tuples
times1 = list(zip(*[first_pair]*2))
times2 = list(zip(*[second_pair]*2))

# On fait une liste unique, triée des deux ensembles combinés
all_times = sorted(list(set(times1 + times2)))

# Puis on formate à l’ancienne, style HH:MM avec 2 chiffres pour les minutes (pas plus)
formatted_times = ['{}:{:02d}'.format(hour, minute) for hour, minute in all_times]

# Euh voilà, on affiche tout en une seule ligne séparée par des espaces
print(*formatted_times)