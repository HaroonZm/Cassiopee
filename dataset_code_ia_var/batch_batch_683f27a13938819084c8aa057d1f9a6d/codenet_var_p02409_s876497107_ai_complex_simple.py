from functools import reduce
from itertools import chain,repeat,starmap,product
import operator

court = list(map(lambda _:list(map(lambda __:list(repeat(0,10)),range(3))),range(4)))
n = int(input())
list(starmap(lambda _:operator.setitem(
    court[_[0]-1][_ [1]-1], _[2]-1, court[_[0]-1][_ [1]-1][_ [2]-1]+_ [3]),
    (map(int, input().split()) for _ in range(n))))
print('\n'.join('\n'.join(' '+''.join(map(lambda x: x+' ',
    map(str,f)))[:-1] for f in court[b]) + ('\n'+20*'#' if b!=3 else '')
    for b in range(4)))