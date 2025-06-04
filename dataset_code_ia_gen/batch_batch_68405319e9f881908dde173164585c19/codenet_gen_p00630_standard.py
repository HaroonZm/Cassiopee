def split_identifier(name):
    if '_' in name:
        return name.split('_')
    elif name[0].islower():
        words, w_start = [], 0
        for i, c in enumerate(name[1:], 1):
            if c.isupper():
                words.append(name[w_start:i])
                w_start = i
        words.append(name[w_start:])
        return words
    else:
        words, w_start = [], 0
        for i, c in enumerate(name[1:], 1):
            if c.isupper():
                words.append(name[w_start:i])
                w_start = i
        words.append(name[w_start:])
        return words

while True:
    line = input().strip()
    if not line:
        continue
    name, t = line.rsplit(' ', 1)
    if t == 'X':
        break
    words = split_identifier(name)
    words = [w.lower() for w in words]
    if t == 'U':
        res = ''.join(w.capitalize() for w in words)
    elif t == 'L':
        res = words[0] + ''.join(w.capitalize() for w in words[1:])
    else:
        res = '_'.join(words)
    print(res)