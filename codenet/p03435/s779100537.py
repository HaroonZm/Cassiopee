def ans():
    C = []
    C.append([])
    C.append(list(map(int, ('0 ' + input()).split())))
    C.append(list(map(int, ('0 ' + input()).split())))
    C.append(list(map(int, ('0 ' + input()).split())))

    A = [0] * 4
    B = [0] * 4
    A[1] = 0

    for i in range(1,4):
        B[i] = C[1][i] - A[1]

    for i in range(2, 4):
        A[i] = C[i][1] - B[1]

    for i in range(1,4):
        for j in range(1, 4):
            if C[i][j] == (A[i] + B[j]):
                pass
            else:
                return print('No')
    return print('Yes')
ans()