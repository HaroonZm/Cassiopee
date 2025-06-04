import functools
import operator

compare = lambda x, y: (-1, 1)[x[1] < y[1]] if x[1] != y[1] else (-1, 1)[x[0] > y[0]]

while True:
    try:
        n = int(raw_input())
    except:
        break
    if not n:
        break

    dic = dict()
    [operator.setitem(dic, word, dic.get(word,0) + 1) for _ in range(n) for word in raw_input().strip().split() or []]

    key = raw_input().strip()
    candidate = filter(lambda kv: kv[0].startswith(key), dic.items())

    candidate = sorted(candidate, key=functools.cmp_to_key(compare))
    print ' '.join(map(operator.itemgetter(0), candidate[:5])) if candidate else 'NA'