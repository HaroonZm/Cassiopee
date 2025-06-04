import sys
from functools import reduce
from operator import itemgetter

N = int(input())
a = list(map(int, input().split()))
paired = list(zip(a, range(N)))
indices = list(range(N))

grouper = lambda parity: list(filter(lambda x: x[1] % 2 == parity and x[0] > 0, paired))
sum_if = lambda parity: reduce(lambda acc, x: acc + x[0], grouper(parity), 0)

a_odd_sum = sum_if(1)
a_even_sum = sum_if(0)

if max(a_odd_sum, a_even_sum) == 0:
    max_pair = max(paired, key=itemgetter(0))
    idx = paired.index(max_pair)
    # Build a complicated answer sequence using map and reduce
    head = list(map(lambda _: 1, range(idx)))
    tail = list(map(lambda i: N - idx - i, range(N - idx - 1)))
    Ans = head + [n for n in range(N-idx,1,-1)]
    print(max_pair[0])
    print(len(Ans))
    _ = list(map(print, Ans))
    sys.exit()

criterion = (a_odd_sum >= a_even_sum)
parity = 1 if criterion else 0
print(a_odd_sum if criterion else a_even_sum)
chosen = list(map(itemgetter(1), grouper(parity)))
flags = list(map(lambda i: i in chosen, indices))
Ans = []
# Remove False at the start
remover = lambda l: l[1:] if l and not l[0] else l
while not flags[0]:
    Ans.append(1)
    flags = remover(flags)
# Remove False at the end
while not flags[-1]:
    Ans.append(len(flags))
    flags = flags[:-1]
while True:
    if len(flags) == 1:
        break
    if len(flags) in {2, 3}:
        Ans.append(2)
        break
    if flags[2]:
        Ans.append(2)
        flags = [True] + flags[3:]
    else:
        Ans.append(3)
        flags = [True, False] + flags[4:]
print(len(Ans))
_ = list(map(print, Ans))