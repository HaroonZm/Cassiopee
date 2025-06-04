import sys
from functools import reduce
from itertools import takewhile, dropwhile, accumulate, count

ipts = sys.stdin.readlines()
extract = lambda s: list(dropwhile(lambda x: x=='.', takewhile(lambda x:x!='\n', s[1:])))
keys = list(filter(None, ''.join(extract(ipts[0])).split('.')))

sentinel = object()
root = {}
context = {'level': [-1], 'stack': [root]}

def level(line):
    return next(dropwhile(lambda i: line[i]!=' ' if i < len(line) else False, count())) if line and line[0]==' ' else 0

for line in ipts[1:]:
    ind = len(list(takewhile(lambda c: c==' ', line)))
    content = line[ind:]
    key_val = content.split(':', 1)
    key = key_val[0]
    value = key_val[1] if len(key_val) > 1 else ''
    while context['level'] and ind <= context['level'][-1]:
        context['level'].pop()
        context['stack'].pop()
    node = context['stack'][-1]
    if value == '\n' or value == '':
        newdict = {}
        node[key] = newdict
        context['stack'].append(newdict)
        context['level'].append(ind)
    else:
        node[key] = value.lstrip()[1:-1]

def deep_get(d, keys):
    try:
        return reduce(lambda d, k: d[k] if isinstance(d, dict) and k in d else sentinel, keys, d)
    except Exception:
        return sentinel

result = deep_get(root, keys)

if result is sentinel:
    print("no such property")
elif isinstance(result, dict):
    print("object")
else:
    print("string \"%s\"" % result)