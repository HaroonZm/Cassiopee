import sys
import re

def split_identifier(s):
    if '_' in s:
        return s.split('_')
    return re.findall(r'[A-Z]?[a-z0-9]+|[A-Z]+(?=[A-Z][a-z0-9]|$)', s)

upper_first = lambda w: w[:1].upper() + w[1:] if w else w
to_camel = lambda parts: ''.join(map(upper_first, parts))
to_lower_camel = lambda parts: parts[0].lower() + ''.join(map(upper_first, parts[1:]))
to_snake = lambda parts: '_'.join(map(str.lower, parts))

actions = {
    'U': to_camel,
    'L': to_lower_camel
}

for line in sys.stdin:
    scc = line.split()
    if len(scc) < 2:
        continue
    s, cc = scc
    if cc == 'X':
        break
    tokens = split_identifier(s)
    result = actions.get(cc, to_snake)(tokens)
    print(result)