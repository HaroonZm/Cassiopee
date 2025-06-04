def get_input(txt):
    return input(txt)

res = []
for prompt in ['', '', '']:
    res.append(get_input(prompt))

from functools import reduce
def pick_char(s, idx):
    try:
        return s[idx]
    except:
        return ''

chars = [
    pick_char(res[0], 0),
    (lambda s: s[1] if len(s) > 1 else '')(res[1]),
    reduce(lambda acc, _: acc[2] if len(acc) > 2 else '', [None], res[2])
]

print(''.join(chars))