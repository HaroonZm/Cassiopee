while True:
    line = raw_input()
    n, k = map(int, line.split())
    if k == 0:
        break

    if n % 2 == 1 or len(bin(k - 1)[2:].zfill(n // 2)) > n // 2:
        print "No"
        print
        continue

    A = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append('.')
        A.append(row)

    bin_k = bin(k - 1)[2:]
    while len(bin_k) < n // 2:
        bin_k = '0' + bin_k

    for i in range(n // 2):
        if bin_k[i] == '1':
            A[0][i * 2] = 'E'
            A[0][i * 2 + 1] = 'E'

    print ''.join(A[0])

    for i in range(n - 1):
        for j in range(n):
            cnt = 0
            if i > 0:
                if A[i][j] == A[i - 1][j]:
                    cnt += 1
            if j > 0:
                if A[i][j] == A[i][j - 1]:
                    cnt += 1
            if j < n - 1:
                if A[i][j] == A[i][j + 1]:
                    cnt += 1

            if cnt == 1:
                A[i + 1][j] = A[i][j]
            elif A[i][j] == '.':
                A[i + 1][j] = 'E'
            else:
                A[i + 1][j] = '.'
        print ''.join(A[i + 1])
    print