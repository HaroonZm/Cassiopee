N_K_Q = input().split()
N = int(N_K_Q[0])
K = int(N_K_Q[1])
Q = int(N_K_Q[2])
A = []
i = 0
while i < Q:
    A.append(int(input()))
    i += 1

point_list = []
i = 0
while i < N:
    point_list.append(0)
    i += 1

q = 0
while q < Q:
    point_list[A[q] - 1] += 1
    q += 1

n = 0
while n < N:
    if Q - point_list[n] >= K:
        print('No')
    else:
        print('Yes')
    n += 1