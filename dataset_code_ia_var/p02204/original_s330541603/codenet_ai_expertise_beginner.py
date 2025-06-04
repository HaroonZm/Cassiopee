m_n = input().split()
M = int(m_n[0])
N = int(m_n[1])
A_line = input().split()
A = []
for x in A_line:
    A.append(int(x))

if M >= 3:
    now = A[0]
    ans = 0
    for k in range(1, N):
        if A[k] == now:
            now = -1
            ans = ans + 1
        else:
            now = A[k]
    print(ans)
else:
    now = A[0]
    ans1 = 0
    for k in range(1, N):
        if A[k] == now:
            if now == 1:
                now = 2
            else:
                now = 1
            ans1 = ans1 + 1
        else:
            now = A[k]

    if A[0] == 1:
        now = 2
    else:
        now = 1
    ans2 = 1
    for k in range(1, N):
        if A[k] == now:
            if now == 1:
                now = 2
            else:
                now = 1
            ans2 = ans2 + 1
        else:
            now = A[k]

    if ans1 < ans2:
        print(ans1)
    else:
        print(ans2)