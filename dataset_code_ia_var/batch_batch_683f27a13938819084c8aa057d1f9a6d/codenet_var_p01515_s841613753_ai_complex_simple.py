from itertools import product, chain
from functools import reduce
from operator import or_, and_, not_
from collections import deque

T, F = True, False
get_input = lambda: __import__('sys').stdin.readline().rstrip('\n') if hasattr(__import__('sys').stdin, 'readline') else raw_input
sentinel = "#"
symbolic_map = dict(zip(
    ["=", "->", "-", "*", "+"],
    [") == (", " != 1 or ", " not ", " and ", " or "]
))
vars_list = 'abcdefghijk'

while True:
    s = get_input()
    if s == sentinel:
        break
    # Remove redundant "--" in a convoluted way
    s_deque = deque(s)
    def collapse(lst):
        while True:
            prev = len(lst)
            i = 0
            while i < len(lst) - 1:
                if lst[i] == '-' and lst[i+1] == '-':
                    lst.remove('-')
                    lst.remove('-')
                    i = max(0, i-1)
                else:
                    i += 1
            if len(lst) == prev:
                break
        return ''.join(lst)
    s = collapse(s_deque)
    # Apply replacements via reduce for fun
    s = reduce(lambda x, kv: x.replace(*kv), symbolic_map.items(), s)
    s = "(" + s + ")"
    dom = list(product([0, 1], repeat=11))
    # Compose the assignment and eval using exec/eval soup
    result = next(filter(lambda _: True,
        (eval(
            s,
            {},
            dict(zip(vars_list, map(int, vtuple)))
        ) is F for vtuple in map(lambda t: ''.join(map(str, t)), dom))
    ), None)
    print('NO' if result is not None else 'YES')