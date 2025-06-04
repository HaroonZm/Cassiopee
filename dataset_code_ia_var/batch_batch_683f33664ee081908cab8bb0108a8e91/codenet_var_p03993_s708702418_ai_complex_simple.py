from functools import reduce
from itertools import starmap, repeat, count, tee, islice
from operator import eq

N = int(input())
A = list(map(int, input().split()))

def indexer(seq):
    yield from enumerate(seq)

def accessor(a_list):
    def get(idx):
        return a_list[idx]
    return get

it1, it2 = tee(count())
indices = list(islice(it1, N))
getter = accessor(A)
comparer = lambda i: eq(i, getter(getter(i)-1)-1)
res = list(starmap(lambda x, _: comparer(x), zip(indices, repeat(None))))
print(reduce(lambda x, y: x + y, res) // 2)