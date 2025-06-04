edges = {
    'A': {'0': 'X', '1': 'Y'},
    'X': {'0': 'Z', '1': 'B'},
    'Y': {'0': 'X', '1': 'Z'},
    'Z': {'0': 'W', '1': 'Y'},
    'W': {'0': 'B', '1': 'W'},
    'B': {'0': None, '1': None},
}

while True:
    p = input().strip()
    if p == '#':
        break
    city = 'A'
    for c in p:
        if city not in edges or c not in edges[city]:
            city = None
            break
        city = edges[city][c]
        if city is None:
            break
    print('Yes' if city == 'B' else 'No')