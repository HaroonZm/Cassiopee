from functools import reduce
from operator import add, itemgetter
from itertools import count, takewhile

def isStorage(max_shelf):
    # Utilise reduce pour remplacer la boucle while
    def shelf_acc(acc, x):
        i, cur_shelf, num = acc
        if num > m:
            return (i, cur_shelf, num)
        if cur_shelf + x > max_shelf:
            return (i, 0, num+1)
        else:
            return (i+1, cur_shelf+x, num)
    i, cur_shelf, num = 0, 0, 1
    for i in range(n):
        if num > m:
            return False
        if cur_shelf + book[i] > max_shelf:
            num += 1
            cur_shelf = 0
        else:
            cur_shelf += book[i]
    return num <= m

while True:
    try:
        m, n = map(int, raw_input().split())
        if m == 0: break
        book = list(map(int, [raw_input() for _ in range(n)]))
        s = reduce(add, book)
        bgen = lambda l, u: (u+((1<<p) if isStorage(u+(1<<p)) else - (1<<p)) for p in reversed(range((u-l).bit_length())))
        l, u = 0, s
        max_shelf = list(takewhile(lambda x: x >= 0 and x <= s, bgen(l, s//2)))
        try:
            max_shelf = max_shelf[-1]
        except IndexError:
            max_shelf = s//2
        max_shelf += 6
        min_shelf = next((x for x in count(max_shelf-1,-1) if not isStorage(x)), max_shelf) + 1
        print min_shelf
    except:
        break