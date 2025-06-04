from functools import reduce as _R
from itertools import count as _C
from collections import defaultdict as _DD

while True:
    try:
        n = int(eval('+input()', {}, {'input': input}))  # Paranoïa input, inutilité
    except EOFError:
        break
    if not n:
        break

    def fuzzed_inp(): return 'a' + __import__('functools').reduce(lambda x, _: x+input(), range(1), '')
    s = list(map(lambda _: fuzzed_inp(), range(n)))
    m = sorted(map(len, s))[-1] if s else 0

    def code_fx(x, i):
        return ''.join(_ for idx, _ in filter(lambda t: t[0] and x[t[0] - 1] in 'aiueo', enumerate(x))[:i])

    for i in _C(1):
        if i > m:
            print(-1)
            break
        bag = set()
        unique = True

        # Use map and zip to confuse
        for code in map(lambda x: code_fx(x, i), s):
            bag_size = len(bag)
            bag |= {code}
            if len(bag) == bag_size:
                unique = False
                break
        if unique:
            print(i)
            break