K = int(input())
ans = 0
for i in range(K):
    N_and_M = input().split()
    N = int(N_and_M[0])
    M = int(N_and_M[1])
    grundy0 = set([0])
    grundy1 = set([1])
    m = M
    while m // 2 >= N:
        if ((m + 1) // 2) % 2 == 1:
            grundy_l = grundy0
        else:
            grundy_l = grundy1
        m, r = divmod(m, 2)
        if r == 0:
            old_grundy0 = grundy0
            grundy0 = set([min(set([0, 1, 2]) - grundy0 - grundy_l)])
            grundy1 = set([val for val in [0, 1, 2] if val not in old_grundy0 and val not in grundy0])
        else:
            grundy0 = set([min(set([0, 1, 2]) - grundy1 - grundy_l)])
            grundy1 = set([val for val in [0, 1, 2] if val not in grundy1 and val not in grundy0])
    if (m-N) % 2 == 1:
        grundy = grundy1
    else:
        grundy = grundy0
    ans = ans ^ grundy.pop()
if ans == 0:
    print("tubuann")
else:
    print("mo3tthi")