def puyo_one(A):
    ans = 0
    now = 1
    for i in range(1, 5):
        if A[i] == A[i - 1]:
            now += 1
        else:
            if now >= 3:
                ans += now * A[i - 1]
            now = 1
    return ans

def puyo(A):
    end = False
    total = 0
    while not end:
        made_change = False
        for i in range(len(A)):
            count = 1
            for j in range(1, 5):
                if A[i][j] == A[i][j - 1] and A[i][j] != 0:
                    count += 1
                else:
                    if count >= 3:
                        made_change = True
                        total += A[i][j - 1] * count
                        for k in range(j - count, j):
                            A[i][k] = 0
                    count = 1
            if count >= 3:
                made_change = True
                total += A[i][j - 1] * count
                for k in range(j - count + 1, j + 1):
                    A[i][k] = 0
        if not made_change:
            end = True
        N = len(A)
        for i in range(1, N + 1):
            for j in range(5):
                if A[N - i][j] == 0 and i != N:
                    shift = 1
                    while (N - i - shift) >= 0 and A[N - i - shift][j] == 0 and (shift + i < N):
                        shift += 1
                    if (N - i - shift) >= 0:
                        A[N - i][j] = A[N - i - shift][j]
                        A[N - i - shift][j] = 0
        while True:
            if [0, 0, 0, 0, 0] in A:
                A.pop(A.index([0, 0, 0, 0, 0]))
            else:
                break
    return total

while True:
    H = int(input())
    if H == 0:
        break
    else:
        A = []
        for _ in range(H):
            row = list(map(int, input().split()))
            A.append(row)
        print(puyo(A))