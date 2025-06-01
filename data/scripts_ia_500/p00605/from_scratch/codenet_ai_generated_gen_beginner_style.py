while True:
    line = input()
    if line == '':
        break
    N, K = map(int, line.split())
    if N == 0 and K == 0:
        break
    S = list(map(int, input().split()))
    B = []
    for _ in range(N):
        B.append(list(map(int, input().split())))
    # calculate total needed for each blood type
    total_needed = [0]*K
    for i in range(N):
        for j in range(K):
            total_needed[j] += B[i][j]
    possible = True
    for i in range(K):
        if total_needed[i] > S[i]:
            possible = False
            break
    if possible:
        print("Yes")
    else:
        print("No")