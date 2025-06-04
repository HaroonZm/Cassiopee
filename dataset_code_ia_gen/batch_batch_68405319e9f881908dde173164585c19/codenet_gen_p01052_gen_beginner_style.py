n = int(input())
movies = []
for _ in range(n):
    a, b = map(int, input().split())
    movies.append((a, b))

# Pour chaque jour, on va garder la liste des films disponibles
days = [[] for _ in range(32)]  # index 1 à 31 utilisé

for i, (a, b) in enumerate(movies):
    for d in range(a, b + 1):
        days[d].append(i)

seen = set()
total_happiness = 0

for d in range(1, 32):
    # Choisir un film du jour d (on prend juste le premier pour simplifier)
    # On peut essayer tous les films du jour pour maximiser, mais approche simple:
    chosen = None
    for movie in days[d]:
        chosen = movie
        break
    if chosen is not None:
        if chosen in seen:
            total_happiness += 50
        else:
            total_happiness += 100
            seen.add(chosen)

print(total_happiness)