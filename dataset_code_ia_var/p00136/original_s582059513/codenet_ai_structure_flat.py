C = [0] * 6
_n = int(raw_input())
for _ in [0] * _n:
    ab = raw_input().split('.')
    a = int(ab[0])
    b = int(ab[1])
    if a < 165:
        C[0] += 1
    else:
        idx = (a - 160) // 5
        C[idx] += 1
i = 0
while i < 6:
    print '%d:%s' % (i+1, '*'*C[i])
    i += 1