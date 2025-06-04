case_num = 1
while True:
    N = int(input())
    if N == 0:
        break
    mat = [[0]*N for _ in range(N)]
    num = 1
    for s in range(2*N-1):
        if s % 2 == 0:
            start = max(0, s-(N-1))
            end = min(s, N-1)
            for i in range(end, start-1, -1):
                j = s - i
                mat[i][j] = num
                num += 1
        else:
            start = max(0, s-(N-1))
            end = min(s, N-1)
            for j in range(end, start-1, -1):
                i = s - j
                mat[i][j] = num
                num += 1
    print(f"Case {case_num}:")
    for row in mat:
        print(''.join(f"{x:3}" for x in row))
    case_num += 1