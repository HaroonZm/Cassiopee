def op1 (p) :
    return (
        p[ 0],p[ 1],p[ 2],p[ 3],p[ 4],p[ 5],p[21],p[22],p[23],p[11],p[10],p[ 9],p[17],p[13],p[14],
        p[15],p[16],p[12],p[18],p[19],p[20],p[ 6],p[ 7],p[ 8],p[24],p[25],p[26],p[27],p[28],p[29]
    )

def op2 (p) :
    return (
        p[27],p[28],p[29],p[ 3],p[ 4],p[ 5],p[ 6],p[ 7],p[ 8],p[ 9],p[10],p[11],p[12],p[13],p[15],
        p[14],p[16],p[17],p[20],p[19],p[18],p[21],p[22],p[23],p[24],p[25],p[26],p[ 0],p[ 1],p [2]
    )

def op3 (p) :
    return (
        p[23],p[ 1],p[ 2],p[26],p[ 4],p[ 5],p[29],p[ 7],p[ 8],p[20],p[10],p[11],p[12],p[13],p[14],
        p[17],p[16],p[15],p[18],p[19],p[ 9],p[21],p[22],p[ 0],p[24],p[25],p[ 3],p[27],p[28],p[ 6]
    )

def op4 (p) :
    return (
        p[ 0],p[ 1],p[21],p[ 3],p[ 4],p[24],p[ 6],p[ 7],p[27],p[ 9],p[10],p[18],p[14],p[13],p[12],
        p[15],p[16],p[17],p[11],p[19],p[20],p[ 2],p[22],p[23],p[ 5],p[25],p[26],p[ 8],p[28],p[29]
    )

def op (p, i) :
    if (i == 1) :
        return op1(p)
    elif (i == 2) :
        return op2(p)
    elif (i == 3) :
        return op3(p)
    elif (i == 4) :
        return op4(p)

def valid (p) :
    for i in range(1, 9) :
        if (p[0] != p[i]) :
            return False

    for i in range(22, 30) :
        if (p[21] != p[i]) :
            return False

    for i in range(10, 12) :
        if (p[9] != p[i]) :
            return False

    for i in range(13, 15) :
        if (p[12] != p[i]) :
            return False

    for i in range(16, 18) :
        if (p[15] != p[i]) :
            return False

    for i in range(19, 21) :
        if (p[18] != p[i]) :
            return False

    q = (p[0], p[9], p[12], p[15], p[18], p[21])

    if (q == (0, 1, 3, 5, 4, 2)) :
        return True
    if (q == (0, 3, 5, 4, 1, 2)) :
        return True
    if (q == (0, 5, 4, 1, 3, 2)) :
        return True
    if (q == (0, 4, 1, 3, 5, 2)) :
        return True

    if (q == (2, 1, 5, 3, 4, 0)) :
        return True
    if (q == (2, 5, 3, 4, 1, 0)) :
        return True
    if (q == (2, 3, 4, 1, 5, 0)) :
        return True
    if (q == (2, 4, 1, 5, 3, 0)) :
        return True

    return False

def solve (n, p, i) :
    global minimum
    if (n > 9) :
        return

    if (n >= minimum) :
        return

    if (valid(p)) :
        minimum = min(minimum, n)
        return

    for j in range(1, 5) :
        if (i != j) :
            solve(n + 1, op(p, j), j)
    return

minimum = 100
N = int(input())
for kk in range(0, N) :
    minimum = 100
    p = tuple([int(term) - 1 for term in input().split()])
    if (valid(p)) :
        print(0)
        continue
    for i in range(1, 5) :
        solve(1, op(p, i), i)
    print(minimum)