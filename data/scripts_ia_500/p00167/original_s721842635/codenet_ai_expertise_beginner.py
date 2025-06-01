while True:
    N = input()
    if N == '':
        break
    N = int(N)
    M = []
    for i in range(N):
        M.append(input())
    C = 0
    for p in range(N-1, 0, -1):
        for i in range(p):
            if M[i] > M[i+1]:
                temp = M[i]
                M[i] = M[i+1]
                M[i+1] = temp
                C = C + 1
    print(C)