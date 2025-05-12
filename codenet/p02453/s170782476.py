def solve():
    from sys import stdin
    f_i = stdin
    
    n = int(f_i.readline())
    A = list(map(int, f_i.readline().split()))
    q = int(f_i.readline())
    
    from bisect import bisect_left as bl
    print('\n'.join(str(bl(A, int(f_i.readline()))) for i in range(q)))

solve()