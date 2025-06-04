N_K = input().split()
N = int(N_K[0])
K = int(N_K[1])
if (N + 1) // K >= 2:
    print('YES')
else:
    print('NO')