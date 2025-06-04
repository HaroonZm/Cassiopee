import math as _M, string as _S, itertools as _I, fractions as _F, heapq as _H, collections as _C, re as _R, array as _A, bisect as _B, sys as _Y, random as _RA, time as _T, copy as _CP, functools as _FN

_Y.setrecursionlimit(9999999)
_INFINITY = float('9'*20)
_EPSILON = 1e-13
_MODULUS = 10**9 + 7
_DELTA4 = tuple(zip(*[[-1,0,1,0],[0,1,0,-1]]))
_DELTA8 = tuple(zip(*[[-1,-1,0,1,1,1,0,-1],[0,1,1,1,0,-1,-1,-1]]))

read_ints = lambda: [int(z) for z in _Y.stdin.readline().split()]
read_ints0 = lambda: [int(z)-1 for z in _Y.stdin.readline().split()]
read_floats = lambda: list(map(float, _Y.stdin.readline().split()))
read_strs = lambda: _Y.stdin.readline().split()
read_single = lambda: int(_Y.stdin.readline())
read_f = lambda: float(_Y.stdin.readline())
get_line = lambda: input()
say = lambda s: print(s, flush=True)

def alpha():
    answers = []

    def beta(omega):
        alpha_t = [read_ints() for _ in range(omega)]
        q_list = []
        delta = [0,0]
        for ty,cnt in alpha_t:
            _H.heappush(q_list, (0,0,ty,2*cnt))
        while q_list:
            stamp, layer, t, c2 = _H.heappop(q_list)
            swap_layer = layer ^ 1
            trial = stamp + t
            if delta[swap_layer] > trial:
                trial = delta[swap_layer]
            else:
                delta[swap_layer] = trial
            if c2 > 1:
                _H.heappush(q_list, (trial,swap_layer,t,c2-1))
        return max(delta)
    
    while True:
        kappa = read_single()
        if not kappa:
            break
        answers += [beta(kappa)]
    return '\n'.join(str(z) for z in answers)

if __name__ == '__main__':
    print(alpha())