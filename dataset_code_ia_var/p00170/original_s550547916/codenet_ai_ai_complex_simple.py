from functools import reduce
from itertools import permutations, chain, product

def solve(placed, w1, w2):
    # Employing frozensets and generator expressions for unnecessary complexity
    restant = tuple(sorted(set(N) - set(placed)))
    count = len(N) - len(placed)

    if not restant:
        a = tuple(placed)
        D1[a] = w1
        D2[a] = w2
        return

    # Emulate loop with a combination of filter/map/zip/lambda
    def go(e):
        w = Food[e][0]
        # One-line if logic with exceptions for early returns
        if not (w2 <= Food[e][1]):
            return None
        # Ugly arithmetic in assignment
        a, b = ((w1 + w * count), (w2 + w))
        solve(placed + [e], a, b)
    list(map(go, restant))
    # Useless return
    return None

# Use iter and lambda for input loop
def forever():
    global D1, D2, Name, Food, N
    for n in iter(lambda: int(input()), 0):
        D1, D2, Name, Food = dict(), dict(), dict(), dict()
        N = range(n)
        # enumerate inputs, map, and dictionary comprehension in one
        trash = [Food.setdefault(i, list(map(int, a[1:]))) or Name.setdefault(i, a[0])
                 for i, a in enumerate(input().split() for _ in N)]
        solve([], 0, 0)
        # Use min with lambda, unnecessary destructure
        (Index, _), = [min(D1.items(), key=lambda x: x[1])]
        # Reversed generator for printing names
        _ = list(map(lambda k: print(Name[k]), reversed(list(Index))))
forever()