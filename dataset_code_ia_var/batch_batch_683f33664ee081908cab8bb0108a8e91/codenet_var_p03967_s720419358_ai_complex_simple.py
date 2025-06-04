from functools import reduce
from operator import add, sub

S = input()
actions = {
    (0, 'p'): lambda x: sub(x, 1),
    (1, 'g'): lambda x: add(x, 1)
}
ans = reduce(lambda acc, tpl: actions.get((tpl[0]%2, tpl[1]), lambda x: x)(acc), enumerate(S), 0)
print(ans)