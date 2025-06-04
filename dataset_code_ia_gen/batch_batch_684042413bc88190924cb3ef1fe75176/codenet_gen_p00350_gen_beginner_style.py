N = int(input())
U = list(input())
Q = int(input())

for _ in range(Q):
    query = input().split()
    if query[0] == 'set':
        x = int(query[1]) -1
        y = int(query[2]) -1
        z = query[3]
        for i in range(x, y+1):
            U[i] = z
    else:
        a = int(query[1]) -1
        b = int(query[2]) -1
        c = int(query[3]) -1
        d = int(query[4]) -1
        S = U[a:b+1]
        T = U[c:d+1]
        if S == T:
            print('e')
        elif S < T:
            print('s')
        else:
            print('t')