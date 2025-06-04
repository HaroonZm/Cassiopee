def calc(S):
    p = q = 0
    for c in S[1:]:
        if c == 'A':
            p += 1
        else:
            q += 1
    return p, q
def check(p, q):
    if q < 10:
        return p == 11
    return p - q == 2
while 1:
    S1 = input()
    if S1 == "0":
        break
    S2 = input()
    S3 = input()
    p1, q1 = calc(S1)
    if S2[0] == 'A':
        p1 += 1
    else:
        q1 += 1
    print(p1, q1)
    p2, q2 = calc(S2)
    if S3[0] == 'A':
        p2 += 1
    else:
        q2 += 1
    print(p2, q2)
    p3, q3 = calc(S3)
    if check(p3+1, q3):
        print(p3+1, q3)
    else:
        print(p3, q3+1)