T = int(raw_input())
i = 0
while i < T:
    N_D = raw_input().split()
    N = int(N_D[0])
    D = int(N_D[1])
    if N % 2 == 1:
        print 127 * (N - 1) + D
    else:
        print 127 * (N - 1) + (D ^ 127)
    i += 1