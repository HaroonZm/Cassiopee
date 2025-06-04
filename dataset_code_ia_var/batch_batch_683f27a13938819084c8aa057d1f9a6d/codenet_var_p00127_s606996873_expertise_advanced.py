from sys import stdin

table = {
    **{r * 10 + c: chr(96 + (r - 1) * 5 + c) for r in range(1, 7) for c in range(1, 6)
       if (val := (r - 1) * 5 + c) <= 26},
    62: '.', 63: '?', 64: '!', 65: ' '
}

for line in map(str.strip, stdin):
    if not line:
        break
    try:
        chunks = [int(line[i:i+2]) for i in range(0, len(line), 2)]
        print(''.join(table[x] for x in chunks))
    except Exception:
        print('NA')