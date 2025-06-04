import re
from collections import defaultdict
from functools import reduce

_init_regex = re.compile(r"([^\[]+)\[([^\]=]+)\]$")
_assign_regex = re.compile(r"([^\[]+)\[([^\]=]+)\]=(.+)$")

def deep_eval(s, _depth=[0]):
    _depth[0] += 1
    try:
        match_init = _init_regex.fullmatch(s)
        if match_init:
            nom, exp = map(str.strip, match_init.groups())
            key = deep_eval(exp)
            # Use trick to flatten and fetch the value
            return (lambda d, n, k: d.get(n, {}).get(k, -1))(globals_dic, nom, key)
        return eval(s, {}, {})
    except:
        pass
    finally:
        _depth[0] -= 1
    return -1

while True:
    globals_dic = defaultdict(dict)
    sizes = {}
    res = 0
    line_count = 0

    while True:
        s = raw_input()
        if s == '.':
            break
        line_count += 1
        
        # Compose the matching in a reduce for "creativity"
        regexes = [_init_regex, _assign_regex]
        match_type = reduce(lambda acc, rgx: acc if acc else rgx.fullmatch(s), regexes, None)

        if _init_regex.fullmatch(s):
            mat = _init_regex.fullmatch(s)
            nom, exp = map(str.strip, mat.groups())
            val = deep_eval(exp)
            if val == -1:
                res = res or line_count
            else:
                globals_dic[nom].clear() or globals_dic[nom].update({})
                sizes[nom] = val
        elif _assign_regex.fullmatch(s):
            mat = _assign_regex.fullmatch(s)
            nom, exp, right = map(str.strip, mat.groups())
            ind = deep_eval(exp)
            val = deep_eval(right)
            checks = [
                (ind != -1),
                (val != -1),
                (nom in globals_dic),
                ((sizes.get(nom, -1)-1) >= ind)
            ]
            if not all(checks):
                res = res or line_count
            else:
                # Dictionary assignment via a hidden lambda
                (lambda d, n, i, v: d[n].__setitem__(i, v))(globals_dic, nom, ind, val)
    if not globals_dic:
        break
    print(res)