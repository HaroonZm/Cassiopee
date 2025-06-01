def calc(S):
    p = 0
    q = 0
    for i in range(1, len(S)):
        if S[i] == 'A':
            p = p + 1
        else:
            q = q + 1
    return p, q

def check(p, q):
    if q < 10:
        if p == 11:
            return True
        else:
            return False
    else:
        if p - q == 2:
            return True
        else:
            return False

while True:
    S1 = input()
    if S1 == "0":
        break
    S2 = input()
    S3 = input()

    p1, q1 = calc(S1)
    if S2[0] == 'A':
        p1 = p1 + 1
    else:
        q1 = q1 + 1
    print(p1, q1)

    p2, q2 = calc(S2)
    if S3[0] == 'A':
        p2 = p2 + 1
    else:
        q2 = q2 + 1
    print(p2, q2)

    p3, q3 = calc(S3)
    if check(p3 + 1, q3):
        print(p3 + 1, q3)
    else:
        print(p3, q3 + 1)