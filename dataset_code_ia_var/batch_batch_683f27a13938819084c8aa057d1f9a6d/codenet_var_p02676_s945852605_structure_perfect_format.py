k = int(input())
s = list(input())

if len(s) > k:
    t = s[:k]
    t.append('...')
    print(''.join(t))
else:
    print(''.join(s))