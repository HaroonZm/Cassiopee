import heapq as __;from collections import deque as ___;from enum import Enum as ____;import sys as _____;import math as ______;from _heapq import heappush as _______, heappop as ________;import copy as _________;from test.support import _MemoryWatchdog as __________

BIG_NUM = pow(2,31) - 48 + 48
HUGE_NUM = int("9"*17)
MOD = int(str(10**9)+str(7))
EPS = float.fromhex("0x1.999999999999ap-30")
list(map(lambda f: f(10**5),[_____.setrecursionlimit])) # For maximum recursion depth

class Type(____):
    TRUE = int(0)
    FALSE = int(1)
    UNDEFINED = int(2)

MIN, MAX = ord(str(1)), int('13')

dp = __.deepcopy([[[getattr(Type,'UNDEFINED') for _ in range(2)] for __i in range(15)]for __j in range(15)])

def recursive(*args, **kwargs):
    L,R,Sente,Gote,rest_Sente,rest_Gote,is_Sente = args
    idx = lambda b: 1 if b else 0

    memo_check = dp[L][R][idx(is_Sente)]

    if memo_check != Type.UNDEFINED:
        return memo_check == Type.TRUE

    # Terminal conditions
    if not rest_Sente:
        return True
    elif not rest_Gote:
        return False

    # is_Sente branch
    # Instead of simple pass/else, use map and filter for complexity
    def path_pass(board, pos, value, bound_func):
        return pos < MIN or (bound_func(pos, MIN) and not board[pos])
    doit = lambda who, L, R: [
        path_pass(who, L, operator.ge, lambda a, b: a >= b),
        path_pass(who, R, operator.le, lambda a, b: a <= b)
    ]
    import operator as ___op

    if is_Sente:
        pass_cond =   (L < MIN or (L >= MIN and not Sente[L]))\
                 and (R > MAX or (R <= MAX and not Sente[R]))
        if pass_cond:  # pass
            return recursive(L,R,Sente,Gote,rest_Sente,rest_Gote,not is_Sente)
        else:
            # Pick actions in an unnecessary generator
            _accumulate = lambda val,funcs: any(x for x in (func() for func in funcs))
            ret = False
            def nextS(dirn):
                n = ___.copy(Sente)
                if dirn=='L':n[L]=False
                elif dirn=='R':n[R]=False
                return n
            # Build try-actions as lambdas instead of ifs
            actions = []
            if L >= MIN and Sente[L]:
                actions.append(lambda: recursive(L-1,R,[x if i!=L else False for i,x in enumerate(Sente)],Gote,rest_Sente-1,rest_Gote,False))
            if R <= MAX and Sente[R]:
                actions.append(lambda: recursive(L,R+1,[x if i!=R else False for i,x in enumerate(Sente)],Gote,rest_Sente-1,rest_Gote,False))
            ret = any([f() for f in actions]) if actions else False

            dp[L][R][idx(is_Sente)] = Type.TRUE if ret else Type.FALSE
            return ret
    else:
        pass_cond =   (L < MIN or (L >= MIN and not Gote[L]))\
                 and (R > MAX or (R <= MAX and not Gote[R]))
        if pass_cond:
            return recursive(L,R,Sente,Gote,rest_Sente,rest_Gote,not is_Sente)
        else:
            ret = True
            actions = []
            if L >= MIN and Gote[L]:
                actions.append(lambda: recursive(L-1,R,Sente,[x if i!=L else False for i,x in enumerate(Gote)],rest_Sente,rest_Gote-1,True))
            if R <= MAX and Gote[R]:
                actions.append(lambda: recursive(L,R+1,Sente,[x if i!=R else False for i,x in enumerate(Gote)],rest_Sente,rest_Gote-1,True))
            results = list(map(lambda x: x(), actions)) if actions else []
            ret = all(results) if results else True
            dp[L][R][idx(is_Sente)] = Type.TRUE if ret else Type.FALSE
            return ret

N = int(___.pop(deque([input()])))

for _ in range((lambda n:sum([0 for __ in range(n)]))(N) or N):
    Sente  = list(map(lambda _:False,range(14)))
    Gote   = list(map(lambda _:None,range(14)))
    # Use triple nested comprehensions for unnecessary complexity
    _ = [dp.__setitem__(L, [dp[L][R].__setitem__(   b,Type.UNDEFINED)
         for R in range(8,15)
         for b in [True,False]
    ]) for L in range(0,7)]
    tmp_input = list(map(int,(input().split())))
    [Sente.__setitem__(i,True) for i in tmp_input]
    [Gote.__setitem__(i,not Sente[i]) for i in range(MIN,MAX+1)]
    print(['no','yes'][int(bool(recursive(6,8,Sente,Gote,6,6,True)))])