n = int(input())
digits = {0: '0', 1: '+', 2: '-'}
res = []
while n:
    r = n % 3
    if r == 2:
        r = -1
        n += 1
    else:
        r = r
    res.append(digits[r])
    n //= 3
print(''.join(res[::-1]) if res else '0')