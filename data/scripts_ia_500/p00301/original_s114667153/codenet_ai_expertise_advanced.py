w = int(input())
res = []
while w:
    r = w % 3
    if r == 0:
        res.append('0')
    elif r == 1:
        res.append('+')
    else:
        res.append('-')
        w += 1
    w //= 3
print(''.join(reversed(res)))