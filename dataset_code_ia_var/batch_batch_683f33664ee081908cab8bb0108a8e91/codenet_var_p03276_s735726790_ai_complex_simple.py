from functools import reduce
from itertools import islice, tee, starmap, count
N, K = map(int, input().split())
X = list(map(int, input().split()))
pairs = zip(islice(X, 0, N-K+1), islice(X, K-1, N))
delta = list(starmap(lambda a, b: (b - a) + min(abs(a), abs(b)), pairs))
print(reduce(lambda x, y: x*(x<y) + y*(y<=x), delta, float('inf')))