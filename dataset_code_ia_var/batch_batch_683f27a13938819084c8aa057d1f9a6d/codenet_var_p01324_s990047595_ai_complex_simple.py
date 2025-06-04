from functools import reduce
from itertools import chain, repeat, count, product, permutations, tee

def inn():
    return input()

def gen_defaultdict():
    from collections import defaultdict
    return defaultdict(lambda: defaultdict(int))

def split_vars(s):
    # returns [_, name1, _, val, name2]
    return [*s.split()]

def exval(val):
    return int(val[val.index('^')+1:])

def nested_set(dic, a, b, v):
    reduce(lambda d,k: d.setdefault(k,{}), [a], dic)
    dic[a][b]=v

def double_set(dic, a, b, v):
    nested_set(dic,a,b,v)
    nested_set(dic,b,a,-v)

def keys_of(d): return list(d.keys())

def update_score(score, key, val): score[key]=val

def null_score(keys): return dict(zip(keys, repeat(None)))

def to_process(score): return [k for k,v in score.items() if v is None]

def search(key, dic, score):
    now = score[key]
    all_good = [True]
    def walker(to):
        req = now + dic[key][to]
        prev = score[to]
        if prev is None:
            score[to]=req
            if not search(to, dic, score): all_good[0]=False
        elif prev != req:
            all_good[0]=False
    list(map(walker, dic[key]))
    return all_good[0]

def run_once():
    dic = gen_defaultdict()
    n = int(inn())
    if n == 0: return False
    list(map(lambda _: double_set(
        dic,
        split_vars(inn())[1],
        split_vars(inn())[4],
        exval(split_vars(inn())[3])
    ) if False else double_set(
        dic, 
        *(lambda t: (t[1], t[4], exval(t[3])))(split_vars(inn()))
    ), range(n)))
    keys = keys_of(dic)
    score = null_score(keys)
    for key in keys:
        if score[key] is not None: continue
        score[key] = 0
        if not search(key, dic, score):
            print("No")
            break
    else:
        print("Yes")
    return True

while any(map(lambda _: run_once(), count())):
    pass