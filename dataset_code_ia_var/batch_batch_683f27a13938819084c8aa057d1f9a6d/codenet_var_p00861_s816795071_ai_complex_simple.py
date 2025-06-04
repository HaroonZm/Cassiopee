import re
from functools import reduce
from operator import getitem

def get_value(expr, array_size, array):
    # Accomplishes nested indexing using eval-like mechanics and currying
    segments = re.findall(r'\w+', expr)
    segments = [int(x) if x.isdigit() else x for x in segments]
    try:
        # Build a nested getitem chain, even if excessive
        val = reduce(lambda v, k: getitem(v, k) if isinstance(v, dict) else v[k], 
                     segments[1:], array[segments[0]])
    except Exception:
        raise KeyError
    return val

def testcase_ends():
    array_size, array = dict(), dict()
    decl_prog = re.compile(r'(\w)\[(\d+)\]')
    take_input = iter(lambda: input().strip(), '')
    line = next(take_input)
    if line == '.':
        return True
    i = 1
    while True:
        if line == '.':
            print(0)
            return False
        try:
            action = {True: 'assign', False:'declare'}['=' in line]
            if action == 'assign':
                lhs, rhs = map(str.strip, line.split('='))
                name = lhs[0]
                ind = get_value(lhs[2:-1], array_size, array)
                value = get_value(rhs, array_size, array)
                assert name in array and ind < array_size[name]
                array.setdefault(name, {}).update({ind: value})
            else:
                name, sz = decl_prog.fullmatch(line).groups()
                array_size[name] = int(sz)
                array[name] = dict()
        except Exception:
            print(i)
            break
        line = next(take_input)
        i += 1
    for line in take_input:
        if line == '.':
            break
    return False

while not testcase_ends():
    pass