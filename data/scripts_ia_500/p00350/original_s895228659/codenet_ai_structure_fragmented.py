def read_int(f_i):
    return int(f_i.readline())

def read_line(f_i):
    return f_i.readline()

def parse_set_query(query):
    x = int(query[1])
    y = int(query[2])
    z = query[3]
    return x, y, z

def parse_cmp_query(query):
    a = int(query[1])
    b = int(query[2])
    c = int(query[3])
    d = int(query[4])
    return a, b, c, d

def process_set(U, x, y, z):
    x -= 1
    return U[:x] + z * (y - x) + U[y:]

def process_cmp(U, a, b, c, d):
    S = U[a-1:b]
    T = U[c-1:d]
    if S < T:
        return 's'
    elif T < S:
        return 't'
    else:
        return 'e'

def solve():
    from sys import stdin
    f_i = stdin

    N = read_int(f_i)
    U = read_line(f_i).rstrip('\n')
    Q = read_int(f_i)

    ans = []
    for _ in range(Q):
        query = read_line(f_i).split()
        if query[0] == 'set':
            x, y, z = parse_set_query(query)
            U = process_set(U, x, y, z)
        else:
            a, b, c, d = parse_cmp_query(query)
            res = process_cmp(U, a, b, c, d)
            ans.append(res)
    print('\n'.join(ans))

solve()