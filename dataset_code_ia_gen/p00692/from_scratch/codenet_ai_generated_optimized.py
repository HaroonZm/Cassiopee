import sys
sys.setrecursionlimit(10**7)
 
# directions for adjacency including diagonals
D = [-5, -4, -3, -1, 1, 3, 4, 5]
 
def compress(state):
    # remove zeros and keep order
    return tuple(x for x in state if x != 0)
 
def neighbors(i, state):
    # Return neighbors indices of card at index i in the current state
    # with boundary checks according to 5x4 layout
    r, c = divmod(i, 4)
    res = []
    for d in D:
        j = i + d
        if 0 <= j < len(state):
            rr, cc = divmod(j,4)
            # adjacency rules: rows differ at most by 1 and cols by at most 1
            if abs(r - rr) <= 1 and abs(c - cc) <= 1:
                res.append(j)
    return res
 
from functools import lru_cache
 
@lru_cache(None)
def dfs(state):
    state = compress(state)
    if not state:
        return 0
    n = len(state)
    min_penalty = n
    for i in range(n):
        v = state[i]
        for j in neighbors(i, state):
            if j > i and state[j] == v:
                # remove the pair i,j
                new_state = list(state)
                new_state[i] = 0
                new_state[j] = 0
                new_state = compress(new_state)
                res = dfs(tuple(new_state))
                if res < min_penalty:
                    min_penalty = res
    return min_penalty
 
input_iter = iter(sys.stdin.read().strip().split())
out = []
while True:
    try:
        N = int(next(input_iter))
    except StopIteration:
        break
    if N == -1:
        break
    for _ in range(N):
        cards = [int(next(input_iter)) for __ in range(20)]
        out.append(str(dfs(tuple(cards))))
print('\n'.join(out))