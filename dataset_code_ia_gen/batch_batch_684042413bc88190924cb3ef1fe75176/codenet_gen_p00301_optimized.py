w = int(input())
res = []
while w != 0:
    r = w % 3
    w //= 3
    if r == 2:
        r = -1
        w += 1
    res.append('0' if r == 0 else '+' if r == 1 else '-')
print(''.join(res[::-1]))