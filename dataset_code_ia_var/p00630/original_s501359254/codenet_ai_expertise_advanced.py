from sys import stdin

def to_camel(s):
    it = iter(s.split('_'))
    return next(it).lower() + ''.join(word.capitalize() for word in it)

def to_pascal(s):
    return ''.join(word.capitalize() for word in s.split('_'))

def to_snake(s):
    out = []
    for c in s:
        if c.isupper():
            if out:
                out.append('_')
            out.append(c.lower())
        else:
            out.append(c)
    return ''.join(out)

for line in map(str.strip, stdin):
    if not line:
        continue
    w, mode = line.split()
    match mode:
        case 'X':
            break
        case 'U':
            if '_' in w:
                print(to_pascal(w))
            else:
                print(w[0].upper() + w[1:])
        case 'L':
            if '_' in w:
                print(to_camel(w))
            else:
                print(w[0].lower() + w[1:])
        case _:
            print(to_snake(w))