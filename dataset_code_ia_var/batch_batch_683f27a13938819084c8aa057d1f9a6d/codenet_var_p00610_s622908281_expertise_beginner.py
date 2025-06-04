def checkback(B, i, j):
    count = 0
    if B[i][j] == B[i][j-1]:
        count += 1
    if B[i][j] == B[i][j+1]:
        count += 1
    if B[i][j] == B[i-1][j]:
        count += 1
    if count == 2:
        return 1 - B[i][j]
    else:
        return B[i][j]

while True:
    inp = input().split()
    N = int(inp[0])
    K = int(inp[1])
    if N == 0:
        break
    if N % 2 == 1 or K > 2 ** (N // 2):
        print("No\n")
    else:
        n = N // 2
        A = [0] * N
        K = K - 1
        for i in range(1, n + 1):
            val = K // (2 ** (n - i))
            A[2 * (i - 1)] = val
            A[2 * (i - 1) + 1] = val
            K = K % (2 ** (n - i))
        B = []
        for i in range(N + 2):
            B.append([-1] * (N + 2))
        for i in range(N):
            B[1][i+1] = A[i]
        for i in range(2, N + 1):
            for j in range(1, N + 1):
                B[i][j] = checkback(B, i-1, j)
        for i in range(1, N + 1):
            row = ""
            for j in range(1, N + 1):
                if B[i][j] == 0:
                    row += "."
                else:
                    row += "E"
            print(row)
        print("\n")