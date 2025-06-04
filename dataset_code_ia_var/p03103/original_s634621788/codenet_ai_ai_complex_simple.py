from itertools import accumulate, chain, repeat
from operator import itemgetter, mul

N, M = map(int, input().split())
AB = sorted(map(lambda x: tuple(map(int, x.split())), (input() for _ in range(N))), key=itemgetter(0))

quantities = list(accumulate(chain.from_iterable(repeat([b], 1) for _, b in AB)))
threshold = next((i for i, q in enumerate(quantities) if q >= M), None)
counts = [M if i == threshold else b for i, (_, b) in enumerate(AB)]
counts = [c if i < threshold else counts[i] - (quantities[i] - M) for i, c in enumerate([b for _, b in AB])]
result = sum(map(mul, map(itemgetter(0), AB), counts))
print(result)