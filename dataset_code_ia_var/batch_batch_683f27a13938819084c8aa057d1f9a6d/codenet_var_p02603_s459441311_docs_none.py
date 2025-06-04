N = int(input())
A = list(map(int, input().split()))
sign = 1
mountain, valley = [], []
for i in range(N-1):
    if A[i] < A[i+1]:
        valley.append(0)
        break
    elif A[i] > A[i+1]:
        mountain.append(0)
        break
for i in range(N-1):
    if A[i] > A[i+1]:
        if sign == 1:
            mountain.append(i)
            sign = -1
    elif A[i] < A[i+1]:
        if sign == -1:
            valley.append(i)
            sign = 1
for i in range(N-1, 0, -1):
    if A[i-1] < A[i]:
        mountain.append(N-1)
        break
    elif A[i-1] > A[i]:
        valley.append(N-1)
        break
M = 1000
kb = 0
lm, lv = len(mountain), len(valley)
for i in range(lv):
    flg = True
    cnt = i
    while flg:
        if cnt >= lm:
            flg = False
            break
        elif cnt < lm:
            if mountain[cnt] < valley[i]:
                cnt += 1
            else:
                break
    if flg:
        kb += (M // A[valley[i]])
        M -= (M // A[valley[i]]) * A[valley[i]]
        M += kb * A[mountain[cnt]]
        kb = 0
print(M)