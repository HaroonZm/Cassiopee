from collections import defaultdict
from functools import reduce
from operator import itemgetter

def play(line, N):
    C = defaultdict(int)
    B = [0]

    def update_c(i):
        return i % N

    def process_char(idx, ch, state):
        c_dict, b_list = state
        p = update_c(idx)

        def inc_c():
            c_dict[p] += 1

        def s_case():
            inc_c()
            b_list[0] += c_dict[p]
            c_dict[p] = 0

        def l_case():
            c_dict[p] += b_list[0] + 1
            b_list[0] = 0

        {'M': inc_c, 'S': s_case, 'L': l_case}.get(ch, lambda:None)()
        return (c_dict, b_list)

    final_c, final_b = reduce(lambda st, ix: process_char(ix[0], ix[1], st), enumerate(line), (C, B))
    sorted_c = sorted(final_c.items(), key=itemgetter(0))
    vals = [v for k,v in sorted_c] + [final_b[0]]
    print(*vals)

import sys
for line in sys.stdin:
    try:
        N = int(line.strip())
        if N == 0:
            break
        ln = next(sys.stdin).strip()
        play(ln, N)
    except StopIteration:
        break