# Je prends les deux dates, un peu à l'arrache :)
a, b = map(int, input().split())
c, d = map(int, input().split())

# Bon ici je compare juste les mois, ça devrait suffire
if a == c:
    print(0)
else:
    print(1)  # On veut 1 si les mois sont différents, logique non ?