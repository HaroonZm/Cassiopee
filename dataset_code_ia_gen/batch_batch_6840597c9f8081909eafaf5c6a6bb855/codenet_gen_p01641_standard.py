s = input()
res = []
cur = 0
for c in s:
    t = ord(c)
    diff = t - cur
    if diff > 0:
        res.append('+' * diff)
    elif diff < 0:
        res.append('-' * (-diff))
    res.append('.')
    cur = t
print(''.join(res))