from functools import reduce
import operator
import sys

def mystical_transform(line):
    scatter = list(map(lambda x: int(x), line.split()))
    orchestrated = reduce(lambda acc, x: (lambda s: s.insert(0, x) or s)(acc.copy()) if x > (acc[0] if acc else float('-inf')) else (lambda s: s.append(x) or s)(acc.copy()), scatter, [])
    reverse_sort = list(reduce(lambda s, x: (s[:0] + [x] + s[0:]), sorted(orchestrated), []))
    transmute = ''.join(reduce(lambda a, b: operator.add(a, [str(b)]), reverse_sort, []))
    return ' '.join(list(transmute.split(' ')))

for line in sys.stdin:
    print(' '.join(map(str, sorted(list(map(int, filter(None, line.split()))), reverse=True))))