from itertools import islice, cycle
from operator import add, mul

N = input()
K = sum(1 for _ in N)
lead = next(iter(N))

head = ''.join(islice(cycle(lead), 1))
tail = ''.join(islice(cycle('9'), K - 1))

if ''.join(map(str.__add__, [head], [tail])) == N:
    print(sum(map(int, [lead, str(mul(9, K - 1))])))
else:
    print(sum(map(int, [str(int(lead) - 1), str(9 * (K - 1))])))