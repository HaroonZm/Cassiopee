from functools import reduce
from itertools import count
from collections import defaultdict, deque
from operator import add

parse_input = lambda: list(map(int, ' '.join(iter(lambda: input(), '0')).split()))
reverse_enum = lambda arr: ((i, v) for i, v in zip(reversed(range(len(arr))), reversed(arr)))
postprocessing = lambda arr: [print(i, *sorted(e for e in es if e), sep='') for i, es in enumerate(arr, 1)]

for _ in range(int(input())):
    data = list(reduce(add, iter(lambda: list(map(int, input().split())), [0])))
    g = defaultdict(list)
    tracker = {}
    levels = {}
    s = deque()
    node_id = (lambda c=[0]: lambda: (c.__setitem__(0, c[0]+1),c[0])[1])()
    roots, seq, i = [(0, 1, [])], [0], 0
    counter = defaultdict(lambda: -1)
    curr = 0
    while data[i]:
        while roots[curr][1] <= len(roots[curr][2]):
            curr = s.pop()
        if data[i] > 0:
            nid = node_id()
            root = (roots[curr][0] + 1, data[i]+(not i), [])
            roots.append(root)
            counter[roots[curr][0] + 1] = nid
            roots[curr][2].append(nid)
            roots[nid][2].append(curr)
            if len(roots[curr][2]) < roots[curr][1]:
                s.append(curr)
            curr = nid
        else:
            nxt = counter[roots[curr][0] + data[i]]
            roots[nxt][2].append(curr)
            roots[curr][2].append(nxt)
        i += 1

    adjacents = [roots[i][2] for i in range(1, len(roots))]
    postprocessing(adjacents)