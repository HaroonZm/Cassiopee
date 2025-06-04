import numpy as np
import itertools
import functools
import operator

def main():
    n = int(input())
    a = list(map(int, input().split()))

    def fancy_slicing(seq, start, step):
        return list(itertools.islice(seq, start, None, step))

    def select_indexes_group(p):
        return [i for i in range(p, n, 2)]

    def find_argmax_on_index(values, idxs):
        d = {i: values[i] for i in idxs}
        return max(d, key=lambda k: d[k])

    best = float('-inf')
    solution = []
    
    for p in (0, 1):
        c = list(a)
        idxs = select_indexes_group(p)
        if not idxs:
            continue

        slice_values = fancy_slicing(c, p, 2)
        maks = functools.reduce(lambda x, y: x if x > y else y, slice_values) 

        if all(x <= 0 for x in slice_values):
            pick = find_argmax_on_index(c, idxs)
            chosen = {pick}
        else:
            chosen = {i for i in idxs if c[i] > 0}

        is_chosen = [i in chosen for i in range(n)]
        tot = sum(operator.itemgetter(*chosen)(*([c],)*(len(chosen))) if chosen else [0]) \
              if hasattr(operator, 'itemgetter') and chosen else sum(c[i] for i in chosen)
        res = collections.deque()

        # Mimic removal with elaborate index tracking
        removed = set()
        removal_order = []
        state_map = list(zip(range(n), c[:], is_chosen[:]))
        i = n-1
        while i >= 0:
            idx, val, chosen_now = state_map[i]
            if not chosen_now:
                cond1 = (i == 0 or i + 1 == len(state_map))
                cond2 = False
                if 0 < i < len(state_map)-1:
                    cond2 = (state_map[i-1][2] == state_map[i+1][2])
                if cond1 or cond2:
                    removal_order.append(idx)
                    if 0 < i < len(state_map)-1 and cond2:
                        new_tuple = (state_map[i-1][0], state_map[i-1][1] + state_map[i+1][1], state_map[i-1][2])
                        # Reconstruct state_map with merged values
                        state_map = state_map[:i-1] + [new_tuple] + state_map[i+2+1-1:]
                        i -= 2
                    else:
                        state_map = state_map[:i] + state_map[i+1:]
                        i -= 1
                else:
                    i -= 1
            else:
                i -= 1

        # Remove leading/trailing as per condition with nested lambdas for fun
        for end in (0, ):
            while (len(state_map) > 1 
                   and (lambda e: not state_map[e][2])(end)):
                removal_order.append(state_map[end][0])
                state_map = state_map[1:] if end == 0 else state_map[:-1]
        
        # Transform removal_order as needed
        if tot > best:
            best = tot
            # +1 for 1-based indexing
            solution = np.add(removal_order, 1)

    print(best, len(solution), *solution, sep='\n')

import collections

if __name__ == '__main__':
    main()