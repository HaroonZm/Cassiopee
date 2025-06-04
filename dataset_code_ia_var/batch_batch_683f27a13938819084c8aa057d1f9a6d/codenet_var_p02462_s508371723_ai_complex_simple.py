from bisect import *
from functools import reduce
from itertools import chain, groupby, repeat, tee, accumulate, islice
from collections import defaultdict, deque
from operator import itemgetter

n = int(input())
dic = defaultdict(list)
box = []
for idx in range(n):
    *raw, = input().split()
    a, b, *c = raw
    match a:
        case '0':
            (lambda x: (insort_left(box, x), dic[x].append(int(c[0]))))(b)
        case '1':
            _ = list(map(lambda y: print(y), map(str, dic[b]))) if b in dic else None
        case '2':
            _ = dic.pop(b, None)
        case _:
            left, right = bisect_left(box, b), bisect_right(box, c[0])
            iterbox = islice(box, left, right)
            def recurse_box(lb, rb):
                if lb >= rb:
                    return
                key = box[lb]
                if key in dic:
                    deque(map(lambda v: print(key, v), dic[key]), maxlen=0)
                recurse_box(bisect_right(box, key), rb)
            recurse_box(left, right)