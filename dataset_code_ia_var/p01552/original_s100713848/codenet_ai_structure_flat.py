import re

gkey = input()

yaml = {}
opening_key = ['']
opening_ind = [-1]
space_prog = re.compile(r' *')
key_prog = re.compile(r'[a-z\d]+')
try:
    while True:
        try:
            line = input()
        except EOFError:
            break

        indent = 0
        m = space_prog.match(line)
        if m:
            indent = len(m.group())
        while opening_ind[-1] >= indent:
            opening_ind.pop()
            opening_key.pop()
        k = ''
        m = key_prog.search(line)
        if m:
            k = m.group()
        else:
            k = ''
        if not line.endswith(':'):
            idx = line.find(':')
            v = ''
            if idx != -1:
                v = line[idx+2:]
            yaml['.'.join(opening_key+[k])] = 'string "{}"'.format(v)
            continue
        opening_key.append(k)
        opening_ind.append(indent)
        yaml['.'.join(opening_key)] = 'object'
except Exception:
    pass

if gkey in yaml:
    print(yaml[gkey])
else:
    print('no such property')