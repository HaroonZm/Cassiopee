while True:
    po = input()
    if po == "0":
        break
    A = 0
    B = 0
    i = 1
    while i < len(po):
        if po[i] == "A":
            A = A + 1
        else:
            B = B + 1
        i = i + 1
    if A > B:
        A = A + 1
    else:
        B = B + 1
    print(A, B)