def solve():
    from sys import stdin
    f_i = stdin
    
    N = int(f_i.readline())
    U = f_i.readline()
    U
    Q = int(f_i.readline())
    
    ans = []
    for i in range(Q):
        query = f_i.readline().split()
        if query[0] == 'set':
            x, y = map(int, query[1:3])
            x -= 1
            z = query[3]
            U = U[:x] + z * (y - x) + U[y:]
        else:
            a, b, c, d = map(int, query[1:])
            S = U[a-1:b]
            T = U[c-1:d]
            if S < T:
                ans.append('s')
            elif T < S:
                ans.append('t')
            else:
                ans.append('e')
    print('\n'.join(ans))

solve()