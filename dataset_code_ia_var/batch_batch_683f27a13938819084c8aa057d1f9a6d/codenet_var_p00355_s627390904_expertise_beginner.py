def solve():
    a_b = input().split()
    a = int(a_b[0])
    b = int(a_b[1])
    N = int(input())
    found = False
    for i in range(N):
        s_f = input().split()
        s = int(s_f[0])
        f = int(s_f[1])
        if not (b <= s or f <= a):
            print(1)
            found = True
            break
    if not found:
        print(0)

solve()