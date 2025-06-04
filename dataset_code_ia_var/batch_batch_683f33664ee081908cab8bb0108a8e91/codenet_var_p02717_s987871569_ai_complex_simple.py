from functools import reduce
from operator import itemgetter

# Lecture et conversion en entier via une compréhension à un seul élément dans une map avec lambda
a = list(map(lambda x: int(x), filter(lambda x: len(x) > 0, input().split())))

# Récupérer les indices 2,0,1 mais en utilisant itemgetter sur les indices fournis par une permutation
indices = reduce(lambda x, y: x + [y], [[2],[0],[1]], [])

print(*itemgetter(*indices)(a))