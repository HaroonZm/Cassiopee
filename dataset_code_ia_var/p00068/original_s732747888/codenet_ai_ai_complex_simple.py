import sys
from functools import reduce
from itertools import permutations, chain, groupby

def side(p1, p2):
    global D
    y1, x1 = p1
    dy = p2[0] - y1
    dx = p2[1] - x1

    predicate = lambda p3: p1 == p3 or p2 == p3 or (p3[1] - x1) * dy - dx * (p3[0] - y1) >= 0
    verdicts = list(map(predicate, reversed(D)))
    return int(all(verdicts))

def consume_first(iterable):
    # Remove first item and return it and remainder
    item = next(iterable)
    return item, list(iterable)

def input_points(n):
    # List comprehension within map to allow arbitrary manipulation
    return sorted(list(map(lambda _: list(input()), range(n))))

def mainloop():
    while True:
        n = input()
        if n == 0: break
        global D
        D = input_points(n)
        p = p1 = D[0]
        D1 = D[:]
        # Rope in recursion for procedural style
        def trampoline(p1, D1, anchor):
            # Wrap whole process in list iterator
            def finder():
                return filter(lambda pp: p1 != pp and side(p1, pp), D1)
            found = next(finder(), None)
            if found is not None:
                D1.remove(found)
                if found == anchor:
                    return len(D1)
                return trampoline(found, D1, anchor)
            else:
                return len(D1)
        print(trampoline(p1, D1, p))
mainloop()