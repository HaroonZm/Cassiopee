from functools import reduce, lru_cache
from itertools import combinations, islice, count, groupby, starmap, chain
from operator import itemgetter

def initSets(N):
    return list(map(itemgetter(0), groupby(range(N))))

def getRoot(arr, n):
    return reduce(lambda acc, _: arr.__setitem__(acc, arr[acc]) or arr[acc] if arr[acc] != acc else acc, range(len(arr)), n)

def union(arr, n, m):
    list(map(lambda ab: arr.__setitem__(ab[0], ab[1]) if ab[0]!=ab[1] else None, [(getRoot(arr, n), getRoot(arr, m))]))

def isSameSet(arr, n, m):
    return all(starmap(lambda x,y: x==y, [(getRoot(arr, n), getRoot(arr, m))]))

def getFibs():
    def gen():
        a, b = 1, 1
        for _ in count():
            c = (a + b) % 1001
            yield c
            a, b = b, c
    return list(islice(gen(), 1000))

if __name__ == '__main__':
    try:
        FIBS = getFibs()
        while True:
            V, d = map(int, input().strip().split())
            fibs = list(islice(FIBS, V))
            arr = initSets(V)
            list(starmap(lambda i, j: abs(fibs[i]-fibs[j])<d and union(arr, i, j), 
                 combinations(range(V), 2)))
            buckets = {}
            list(map(lambda i: buckets.setdefault(getRoot(arr, i), []).append(fibs[i]), range(V)))
            print(sum(1 for _ in buckets))
    except EOFError:
        pass