while True:
    s = input()
    if s == '0':
        break
    A = 0
    B = 0
    for i in range(1, len(s)):
        if s[i] == 'A':
            A += 1
        else:
            B += 1
    if A == 10 and B < 10:
        A += 1
    elif B == 10 and A < 10:
        B += 1
    elif A > B:
        A += 1
    else:
        B += 1
    print(A, B)