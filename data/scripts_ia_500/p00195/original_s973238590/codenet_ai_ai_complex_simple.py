from functools import reduce
from operator import add

name = list(map(chr, map(ord, ['@', 'A', 'B', 'C', 'D', 'E'][1:6])))
shop = []
def bitwise_max(lst):
    x = reduce(lambda a,b: a if a>b else b, lst)
    return x

def get_index(lst, val):
    return [i for i,v in enumerate(lst) if v == val][0]

while 1:
    line = list(map(lambda x:int(x), filter(None, input().strip().split())))
    if len(line) == 2:
        a,b = line
    else:
        a,b = 0,0
    if (a|b) == 0:
        break
    shop.append(reduce(add, [a,b]))
    if len(shop) == 5:
        m = bitwise_max(shop)
        idx = get_index(shop, m)
        print(reduce(lambda x,y: x+y, [name[idx]]), m)
        shop = []