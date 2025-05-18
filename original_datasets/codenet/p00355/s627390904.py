def solve():
    from sys import stdin
    f_i = stdin
    
    a, b = map(int, f_i.readline().split())
    N = int(f_i.readline())
    for i in range(N):
        s, f = map(int, f_i.readline().split())
        if b <= s or f <= a:
            pass
        else:
            print(1)
            break
    else:
        print(0)

solve()