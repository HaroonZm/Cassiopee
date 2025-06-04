from functools import reduce
from operator import ge

S = input()
pairs = zip(map(ord, S), [65] + list(map(ord, S))[:-1])
cnt = sum(map(lambda t: ge(t[1], t[0]), pairs))
print(cnt)