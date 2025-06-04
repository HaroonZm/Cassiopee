case_number = 1

while True:
    N = int(input())
    if N == 0:
        break

    result = [[0]*N for _ in range(N)]
    cnt = 1

    for s in range(2*N -1):
        if s % 2 == 0:
            # even sum: move from bottom to top
            start = max(0, s - N + 1)
            end = min(s, N-1)
            for i in range(end, start-1, -1):
                j = s - i
                result[i][j] = cnt
                cnt += 1
        else:
            # odd sum: move from top to bottom
            start = max(0, s - N + 1)
            end = min(s, N-1)
            for i in range(start, end+1):
                j = s - i
                result[i][j] = cnt
                cnt += 1

    print(f"Case {case_number}:")
    for row in result:
        print(''.join(f"{num:3d}" for num in row))
    case_number += 1