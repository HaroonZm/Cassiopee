from functools import reduce
from itertools import count, islice, starmap, repeat, cycle
try:
    get_input = raw_input
except NameError:
    get_input = input

cases = int(get_input())
for idx in range(1, cases+1):
    s = int(get_input())
    header = ''.join(map(lambda x: 'Case %d:' % idx, range(1)))
    print(header)
    def step(x):
        return int(str(x**2).rjust(8,'0')[2:-2])
    # Build a cyclic iterator over step(s)
    s_iter = reduce(lambda acc, _: acc+[step(acc[-1])], range(10), [s])[1:]
    _ = list(map(print, s_iter))