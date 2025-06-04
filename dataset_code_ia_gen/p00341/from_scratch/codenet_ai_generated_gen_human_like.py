sticks = list(map(int, input().split()))
sticks.sort()

if len(sticks) != 12:
    print("no")
    exit()

# Vérifier que chaque longueur apparaît exactement 4 fois (pour un cube)
from collections import Counter
count = Counter(sticks)
if len(count) == 3 and all(v == 4 for v in count.values()):
    print("yes")
    exit()

# Pour un parallélépipède rectangle, il doit y avoir exactement 3 longueurs différentes,
# chacune apparaissant exactement 4 fois
if len(count) == 3 and all(v == 4 for v in count.values()):
    print("yes")
else:
    print("no")