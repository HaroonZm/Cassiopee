from functools import lru_cache

def solve_problem():
    while True:
        n = int(input())
        if n == 0:
            break

        entries = [input().split() for _ in range(n)]
        data = sorted(((int(w), int(s), name) for name, w, s in entries))
        W, S, Name = zip(*data)
        N = tuple(range(n))

        @lru_cache(maxsize=None)
        def backtrack(placed, w1, w2):
            non_placed = tuple(e for e in N if e not in placed)
            if not non_placed:
                return (list(placed), w1) if w1 < backtrack.best_weight else (backtrack.best_D, backtrack.best_weight)
            best_D, best_weight = backtrack.best_D, backtrack.best_weight
            n_left = len(non_placed)
            for e in non_placed:
                w = W[e]
                if w2 + w > S[e]:
                    continue
                total_weight = w1 + w * n_left
                if total_weight > best_weight:
                    continue
                candidate_placed = placed + (e,)
                D_res, wt_res = backtrack(candidate_placed, total_weight, w2 + w)
                if wt_res < best_weight or (wt_res == best_weight and len(D_res) > len(best_D)):
                    best_D, best_weight = D_res, wt_res
            backtrack.best_D, backtrack.best_weight = best_D, best_weight
            return best_D, best_weight

        backtrack.best_D, backtrack.best_weight = (), float('inf')
        res_D, _ = backtrack((), 0, 0)
        for e in reversed(res_D):
            print(Name[e])

solve_problem()