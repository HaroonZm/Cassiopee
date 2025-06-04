import sys
from functools import partial

def query(num, *, _input=input, _print=print):
    _print(f"? {num}", flush=True)
    return _input()

# --- Below: faster, more idiomatic, more functional-style ---

def solve(query_fn):
    ans = []
    append = ans.append
    length_limit = 17  # matches the semiglobal length constraints
    while len(ans) < 20:
        min_lim = 1 if not ans else 0

        probe = (''.join(ans) + str(min_lim) + '9' * 9)
        probe = probe[:length_limit]

        if query_fn(probe) == 'Y':
            # If so, check if next digit would overflow
            if query_fn(''.join(ans) + '2') == 'N':
                append(str(min_lim))
                continue
            # Corner case: check if ans + [min_lim] is "minimal"
            probe_10n = '1' + '0' * len(ans)
            if query_fn(probe_10n) == 'Y':
                append(str(min_lim))
                res = ''.join(ans)
                print(f"! {res}")
                return
            else:
                print(f"! {''.join(ans)}")
                return

        # Binary search for the next digit
        ok, ng = 10, min_lim
        while ok - ng > 1:
            mid = (ok + ng) // 2
            probe = (''.join(ans) + str(mid) + '9' * 9)[:length_limit]
            if query_fn(probe) == 'Y':
                ok = mid
            else:
                ng = mid
        append(str(ok))

N = 10**9

# For local testing: you can replace query with partial(query, _input=...)
solve(query)