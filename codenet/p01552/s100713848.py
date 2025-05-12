#! /usr/bin/env python3

import re

gkey = input()

yaml = {}
opening_key = ['']
opening_ind = [-1]
space_prog = re.compile(r' *')
key_prog = re.compile(r'[a-z\d]+')
while True:
    try:
        line = input()
    except EOFError:
        break

    indent = len(space_prog.match(line).group())
    while opening_ind[-1] >= indent:
        opening_ind.pop()
        opening_key.pop()

    key = key_prog.search(line).group()
    if not line.endswith(':'):
        yaml['.'.join(opening_key+[key])] = (
            'string "{}"'.format(line[line.index(':')+2:])
        )
        continue

    opening_key.append(key)
    opening_ind.append(indent)

    yaml['.'.join(opening_key)] = 'object'

print(yaml.get(gkey, 'no such property'))