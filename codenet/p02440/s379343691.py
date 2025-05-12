def solve():
    from sys import stdin
    f_i = stdin
    
    n = f_i.readline()
    A = list(map(int, f_i.readline().split()))
    
    q = int(f_i.readline())
    ans = []
    for i in range(q):
        com, b, e = map(int, f_i.readline().split())
        if com == 0:
            ans.append(str(min(A[b:e])))
        else:
            ans.append(str(max(A[b:e])))
    print('\n'.join(ans))

solve()