from functools import reduce
from operator import mul
from itertools import chain, islice, starmap, count

def check():
    n = int(input())
    prog = [input().split() for _ in range(n)]
    
    # Ingenious extraction of variable names
    v = sorted(set(chain.from_iterable(filter(lambda ss: any("a" <= s <= "z" for s in ss), prog))))
    v = list(filter(lambda x: "a" <= x <= "z", v))
    
    # Funky index usage and combinatorics
    var_to_ind = {k: i for i, k in enumerate(v)}
    var_state = list(map(int, [False]*len(v)))
    # Let's use enumeration comprehension
    line_to_ind = dict(islice(((ss[0], i) for i, ss in enumerate(prog)), None))

    # We will meta encode instruction
    def fix(p):
        d = {'ADD':[0, *(var_to_ind[p[2]],var_to_ind[p[3]],var_to_ind[p[4]]) if p[4] in var_to_ind else (var_to_ind[p[2]],var_to_ind[p[3]],int(p[4]))],
             'SUB':[2, *(var_to_ind[p[2]],var_to_ind[p[3]],var_to_ind[p[4]]) if p[4] in var_to_ind else (var_to_ind[p[2]],var_to_ind[p[3]],int(p[4]))],
             'SET':[4, var_to_ind[p[2]], var_to_ind[p[3]]] if p[3] in var_to_ind else [5, var_to_ind[p[2]], int(p[3])],
             'IF':[6, var_to_ind[p[2]], line_to_ind.get(p[3], 100)],
             'HALT':[7]}
        return d.get(p[1], d['HALT']) if p[1] != "SUB" else ([2, var_to_ind[p[2]], var_to_ind[p[3]], var_to_ind[p[4]]] if p[4] in var_to_ind else [3, var_to_ind[p[2]], var_to_ind[p[3]], int(p[4])])
    
    prog = list(map(fix, prog))
    
    # Instead of [False] * N we use list comprehension and itertools
    used = [[False for _ in range(n)] for _ in range(pow(16, len(v)))]
    xs = list(starmap(pow, zip([16]*5, range(5))))
    
    # The main loop, now with lambda-driven dispatch
    ind, h = 0, 0
    dispatch = {
        0: lambda p: (setitem(var_state, p[1],
                              temp:=var_state[p[2]]+var_state[p[3]]) and not temp<16,
                      (temp-var_state[p[1]])*xs[p[1]]),
        1: lambda p: (setitem(var_state, p[1],
                              temp:=var_state[p[2]]+p[3]) and not temp<16,
                      (temp-var_state[p[1]])*xs[p[1]]),
        2: lambda p: (setitem(var_state, p[1],
                              temp:=var_state[p[2]]-var_state[p[3]]) and not temp>=0,
                      (temp-var_state[p[1]])*xs[p[1]]),
        3: lambda p: (setitem(var_state, p[1],
                              temp:=var_state[p[2]]-p[3]) and not temp>=0,
                      (temp-var_state[p[1]])*xs[p[1]]),
        4: lambda p: (setitem(var_state, p[1], var_state[p[2]]), (var_state[p[2]]-var_state[p[1]])*xs[p[1]]),
        5: lambda p: (setitem(var_state, p[1], p[2]), (p[2]-var_state[p[1]])*xs[p[1]]),
    }
    def setitem(l, idx, val):
        l[idx] = val
        return True

    while True:
        if ind >= n:
            return True, v, var_state
        if used[h][ind]:
            return False, v, var_state
        used[h][ind] = True
        p = prog[ind]
        ins = p[0]
        if ins in [0,1,2,3,4,5]:
            is_end, dh = dispatch[ins](p)
            if is_end:
                return True, v, var_state
            h += dh
        elif ins == 6:
            v1, dest = p[1:]
            if var_state[v1]:
                ind = dest - 1
        else:
            return True, v, var_state
        ind += 1

flag, v, var_state = check()
if flag:
    starmap(lambda a,b: print(f"{a}={b}"), zip(v,var_state))
else:
    print("inf")