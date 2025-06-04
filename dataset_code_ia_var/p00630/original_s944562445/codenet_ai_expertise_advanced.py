import re
from itertools import islice, cycle

def parse_words(s):
    if '_' in s:
        return s.split('_')
    return re.findall(r'[a-z]+|[A-Z][a-z]*', s)

actions = {
    'D': lambda words: '_'.join(map(str.lower, words)),
    'L': lambda words: (tmp := ''.join(map(str.capitalize, words))) and tmp[0].lower() + tmp[1:],
    'U': lambda words: ''.join(map(str.capitalize, words)),
}

for n, t in iter(lambda: tuple(input().split()), ('', 'X')):
    if t == 'X':
        break
    words = parse_words(n)
    print(actions.get(t, actions['U'])(words))