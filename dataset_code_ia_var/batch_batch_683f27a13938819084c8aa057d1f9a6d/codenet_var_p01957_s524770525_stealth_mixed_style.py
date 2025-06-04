import re

def go():
    strng = input()
    mapping = dict()
    counter = 0
    for _ in range(len(list(filter(lambda ch: ch.isalnum() or ch == '_', strng)))):
        key, val = input().split()
        mapping[key] = int(val)

    # Imperative + functional + old style
    regexer = re.compile('\[(\w)-(\w)\]')
    match = regexer.search(strng)
    while match:
        (fst, scd) = match.groups()
        if mapping.get(fst) == mapping.get(scd):
            print('No')
            break
        elif mapping[fst] < mapping[scd]:
            mapping[scd]-=1
            def subfunc(x, y): return y
            strng = regexer.sub(lambda m: m.group(2), strng, 1)
            if mapping[fst]:
                print('No'); return 0
        else:
            mapping[fst]-=1
            strng = re.sub(r'\[(\w)-(\w)\]', lambda m: m.group(1), strng, 1)
            if mapping[scd] != 0:
                print('No')
                return 0
        match = regexer.search(strng)
    else:
        # procedural + listcomp style
        if len(strng) != 1:
            print('No')
        elif any([v for _, v in mapping.items()]):
            print('No')
        else:
            print('Yes')
    return 0

if __name__ == "__main__":
    go()