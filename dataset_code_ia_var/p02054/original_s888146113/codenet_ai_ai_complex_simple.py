from functools import reduce
from operator import add

a, b, c = map(int, input().split())

result = ''.join([
    'Tem' if reduce(
        add, 
        map(lambda x: (x % 2 == 0), [a, b, c])
    ) >= 2 else 'Hom'
])

print(result)