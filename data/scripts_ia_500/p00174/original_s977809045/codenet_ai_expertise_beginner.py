while True:
    s = input()
    if s == '0':
        break
    A = 0
    B = 0
    i = 1
    while i < len(s):
        if s[i] == 'A':
            A = A + 1
        else:
            B = B + 1
        i = i + 1
    if A == 10 and B < 10:
        A = A + 1
    elif B == 10 and A < 10:
        B = B + 1
    elif A > B:
        A = A + 1
    else:
        B = B + 1
    print(A, B)