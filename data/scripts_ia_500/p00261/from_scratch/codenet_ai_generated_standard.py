transitions = {
    'A': {'0': 'X', '1': 'Y'},
    'X': {'0': 'Z', '1': 'X'},
    'Y': {'0': 'Z', '1': 'B'},
    'Z': {'0': 'W', '1': 'B'},
    'W': {'0': 'B', '1': 'W'},
    'B': {'0': 'X', '1': 'Z'}
}
while True:
    p = input().strip()
    if p == '#':
        break
    city = 'A'
    for ch in p:
        if ch in transitions.get(city, {}):
            city = transitions[city][ch]
        else:
            city = None
            break
    print('Yes' if city == 'B' else 'No')