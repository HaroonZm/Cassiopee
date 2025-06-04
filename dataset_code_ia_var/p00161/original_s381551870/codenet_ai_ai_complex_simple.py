from functools import cmp_to_key, reduce
from operator import itemgetter, add
from itertools import islice, chain

def flatten(l): return list(chain.from_iterable(l))

while True:
    try:
        n = int(eval('input()'))
    except:
        break
    if not n:
        break

    buffer = []
    for _ in iter(lambda: n > len(buffer), True):
        s = input()
        x = list(map(int, s.split()))
        i, y = x[0], x[1:]
        t = sum(map(lambda a: a[0]*60 + a[1], zip(y[::2], y[1::2])))
        buffer.append((i, t))

    sorted_buffer = sorted(buffer, key=cmp_to_key(lambda a, b: (a[1]-b[1]) or (a[0]-b[0])))

    def extr(buffer, idx): return buffer[idx][0]
    print('\n'.join(map(str, map(lambda k: extr(sorted_buffer, k), [0,1,-2]))))