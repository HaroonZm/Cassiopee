from functools import lru_cache, reduce
from operator import or_, add

def main():
    from itertools import product, chain
    while True:
        try:
            n = int(input())
            if not n: break
        except:
            break

        dirs = {'R': (lambda l, r, f, b, d, u: [d, u, f, b, r, l], (1, 0)),
                'L': (lambda l, r, f, b, d, u: [u, d, f, b, l, r], (-1, 0)),
                'B': (lambda l, r, f, b, d, u: [l, r, d, u, b, f], (0, 1)),
                'F': (lambda l, r, f, b, d, u: [l, r, u, d, f, b], (0, -1))}
        
        update_lst = []
        for _ in range(n):
            (x, y), dice, rot = map(int, input().split()), list(map(int, input().split())), input()
            update_point = {(x, y): dice[-2]}
            current = (x, y)
            for d in rot:
                dice = dirs[d][0](*dice)
                current = tuple(map(add, current, dirs[d][1]))
                update_point[current] = dice[-2]
            update_lst.append(update_point)

        N = 1 << n
        keys_list = [set(dct.keys()) for dct in update_lst]
        
        used_lst = [reduce(or_, (keys_list[i] for i in range(n) if (s >> i) & 1), set())
                    for s in range(N)]
        
        add_score = dict()
        for i, up in enumerate(update_lst):
            m = 1 << i
            for s in range(N):
                if s & m: continue
                add_score[(s, m)] = sum(v for k, v in up.items() if k not in used_lst[s])

        @lru_cache(None)
        def max_score(stat):
            if stat == N - 1: return 0
            return max((add_score.get((stat, 1 << i), 0) + max_score(stat | (1 << i))
                        for i in range(n) if not ((stat >> i) & 1)), default=0)
        
        print(max_score(0))

main()