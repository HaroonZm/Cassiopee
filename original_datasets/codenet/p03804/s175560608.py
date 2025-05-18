def resolve():
    N, M = map(int, input().split())
    A = [list(input()) for _ in range(N)]
    B = [list(input()) for _ in range(M)]

    ans = 'No'
    for i in range(N):
        for j in range(N):
            if A[i][j] == B[0][0]:
                count = 0
                for k in range(M):
                    for l in range(M):
                        if i+k>= N or j+l>= N:
                            continue
                        if A[i+k][j+l] == B[k][l]:
                            count += 1
                    if count == M * M:
                        ans = 'Yes'
                        break
                if ans == 'Yes':
                    break
            if ans == 'Yes':
                break
        if ans == 'Yes':
            break
    
    print(ans)

resolve()