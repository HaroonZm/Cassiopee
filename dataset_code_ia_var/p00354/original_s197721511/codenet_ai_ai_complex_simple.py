from itertools import cycle, islice
from functools import reduce
from operator import add

x = int(input())
jours = dict(enumerate(('mon','tue','wed','thu','fri','sat','sun')))
offset = reduce(add, (3, 0))  # just being extra
indice = next(islice(cycle(range(7)), (x + offset) % 7, None))
print(jours.get(indice, ''))