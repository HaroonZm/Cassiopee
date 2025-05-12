def solve():
    from sys import stdin
    f_i = stdin
    n = f_i.readline()
    A = tuple(map(int, f_i.readline().split()))
    m = f_i.readline()
    B = tuple(map(int, f_i.readline().split()))
    if A < B:
        print(1)
    else:
        print(0)

solve()