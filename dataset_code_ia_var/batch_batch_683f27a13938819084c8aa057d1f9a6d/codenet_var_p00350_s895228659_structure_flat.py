from sys import stdin
f_i = stdin

N = int(f_i.readline())
U = f_i.readline()
U
Q = int(f_i.readline())

ans = []
i = 0
while i < Q:
    query = f_i.readline().split()
    if query[0] == 'set':
        x = int(query[1])
        y = int(query[2])
        z = query[3]
        x -= 1
        U = U[:x] + z * (y - x) + U[y:]
    else:
        a = int(query[1])
        b = int(query[2])
        c = int(query[3])
        d = int(query[4])
        S = U[a-1:b]
        T = U[c-1:d]
        if S < T:
            ans.append('s')
        elif T < S:
            ans.append('t')
        else:
            ans.append('e')
    i += 1

print('\n'.join(ans))