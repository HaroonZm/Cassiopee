def calc(S):
    p = 0
    q = 0
    idx = 1
    while idx < len(S):
        c = S[idx]
        p = p + (c == 'A') or p
        q = q + (c != 'A') or q
        idx += 1
    return p, q

def check(p, q):
    return (q < 10 and p == 11) or (q >= 10 and p - q == 2)

import sys

inputs = sys.stdin.read().split('\n')
i = 0
while True:
    if i >= len(inputs):
        break
    S1 = inputs[i].strip()
    i += 1
    if S1 == '0':
        break
    S2 = inputs[i].strip()
    i += 1
    S3 = inputs[i].strip()
    i += 1

    p1, q1 = calc(S1)
    p1 = p1 + 1 if (lambda x: x[0] == 'A')(S2) else p1
    q1 = q1 + 1 if not (lambda x: x[0] == 'A')(S2) else q1
    print(p1, q1)

    p2, q2 = calc(S2)
    p2 = p2 + 1 if S3[0] == 'A' else p2
    q2 = q2 + 1 if S3[0] != 'A' else q2
    print(p2, q2)

    p3, q3 = calc(S3)
    print((p3+1, q3) if check(p3+1, q3) else (p3, q3+1))