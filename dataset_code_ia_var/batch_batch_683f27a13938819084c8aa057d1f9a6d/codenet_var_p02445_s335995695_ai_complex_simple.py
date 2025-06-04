from functools import reduce
from itertools import chain, accumulate, islice, repeat, zip_longest
from operator import itemgetter

n = int(input())
a = list(map(int, input().split()))
q = int(input())
actions = [tuple(map(int, input().split())) for _ in range(q)]

def segment_lst(lst, indexes):
    """Découpe lst selon la liste sorted(indexes+[0,len(lst)]) puis renvoie segments."""
    idx = sorted(set(indexes + [0, len(lst)]))
    return [lst[i:j] for i, j in zip(idx, idx[1:])]

def transmute(a, b, e, t):
    s = t + e - b
    # Génère la liste des "breakpoints" pour découper
    # Selon t > b, la permutation des segments change subtilement
    idxs = (0, b, t, s, e, len(a)) if t > b else (0, t, b, e, s, len(a))
    segs = segment_lst(a, list(idxs))
    if t > b:
        # Quand t > b: [a[:b], a[t:s], a[e:t], a[b:e], a[s:]]
        order = [0,2,3,1,4]
    else:
        # sinon: [a[:t], a[b:e], a[s:b], a[t:s], a[e:]]
        order = [0,1,4,2,3]
    # Concaténation par flattening
    return list(chain.from_iterable(map(segs.__getitem__, order)))

def iterate(fn, data, acts):
    return reduce(lambda acc, params: fn(acc, *params), acts, data)

print(*iterate(transmute, a, actions))