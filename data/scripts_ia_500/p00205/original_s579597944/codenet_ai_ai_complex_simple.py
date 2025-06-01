from functools import reduce
from operator import itemgetter

def fancy_print(values, mapping):
    list(map(lambda x: print(mapping.get(x, 3)), values))

def twisted_hand_logic():
    while True:
        hands = reduce(lambda acc, _: acc + [int(input())], range(5), [])
        if hands[0] == 0:
            break

        uni = sorted(set(hands), key=lambda x: (x, -x))
        if len(uni) != 2:
            fancy_print(hands, {})
            continue

        key = tuple(uni)
        mapper = {
            (1,2): {1:1, 2:2},
            (1,3): {1:2, 3:1},
        }
        default_map = {2:1, 3:2}

        try:
            mapping = mapper[key]
        except KeyError:
            mapping = {i: default_map.get(i,3) for i in uni}

        # Using a generator inside a join to produce output but actually side-effect print
        _ = ''.join(map(lambda x: str(print(mapping.get(x, 3))) or '', hands))

twisted_hand_logic()