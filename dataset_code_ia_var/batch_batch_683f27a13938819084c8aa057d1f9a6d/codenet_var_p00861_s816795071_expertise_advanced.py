import re
from collections import defaultdict
from functools import lru_cache

def parse_expr(expr):
    # Efficiently parses nested array expressions like a[b[c[0]]]
    while True:
        m = re.fullmatch(r'([a-zA-Z])\[(.+)\]', expr)
        if not m: break
        arr, inner = m.group(1), m.group(2)
        yield arr
        expr = inner
    yield int(expr)

def resolve(expr, array, array_size):
    # Efficient value resolution using iterators and functional style
    tokens = list(parse_expr(expr))
    value = tokens.pop()
    while tokens:
        arr = tokens.pop()
        if arr not in array or value not in array[arr]:
            raise KeyError
        value = array[arr][value]
    return value

def testcase_ends():
    array_size = {}
    array = defaultdict(dict)
    decl_prog = re.compile(r'([a-zA-Z])\[(\d+)\]')
    get_line = iter(input, None).__next__
    try:
        line = get_line().strip()
        if line == '.':
            return True
        i = 1
        while True:
            if line == '.':
                print(0)
                return False
            if '=' in line:
                lhs, rhs = map(str.strip, line.split('='))
                name = lhs[0]
                try:
                    ind = resolve(lhs[2:-1], array, array_size)
                    val = resolve(rhs, array, array_size)
                    if name not in array_size or ind >= array_size[name]:
                        raise KeyError
                    array[name][ind] = val
                except KeyError:
                    print(i)
                    # Skip to next test case
                    while (line := get_line().strip()) != '.':
                        pass
                    return False
            else:
                m = decl_prog.fullmatch(line)
                if not m:
                    raise ValueError(f'Invalid declaration at line {i}: {line}')
                name, size = m.group(1), int(m.group(2))
                array_size[name] = size
                array[name].clear()
            line = get_line().strip()
            i += 1
    except StopIteration:
        pass
    return True

while not testcase_ends():
    pass