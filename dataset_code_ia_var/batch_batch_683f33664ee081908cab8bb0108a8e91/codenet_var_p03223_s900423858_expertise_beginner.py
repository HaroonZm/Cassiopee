N = int(input())
A = []
for i in range(N):
    A.append(int(input()))

A.sort()

right = A[0]
left = A[0]
index_l = 1
index_r = len(A) - 1
ans_l = 0
count = 1

while True:
    if count % 2 == 1:
        if index_r - index_l >= 1:
            diff1 = abs(left - A[index_r]) + abs(right - A[index_r - 1])
            diff2 = abs(right - A[index_r]) + abs(left - A[index_r - 1])
            if diff1 > diff2:
                ans_l += diff1
                left = A[index_r]
                right = A[index_r - 1]
            else:
                ans_l += diff2
                left = A[index_r - 1]
                right = A[index_r]
            index_r -= 2
        elif index_r - index_l == 0:
            if abs(left - A[index_r]) > abs(right - A[index_r]):
                ans_l += abs(left - A[index_r])
            else:
                ans_l += abs(right - A[index_r])
            index_r -= 1
        else:
            break
    else:
        if index_r - index_l >= 1:
            diff1 = abs(left - A[index_l]) + abs(right - A[index_l + 1])
            diff2 = abs(right - A[index_l]) + abs(left - A[index_l + 1])
            if diff1 > diff2:
                ans_l += diff1
                left = A[index_l]
                right = A[index_l + 1]
            else:
                ans_l += diff2
                left = A[index_l + 1]
                right = A[index_l]
            index_l += 2
        elif index_r - index_l == 0:
            if abs(left - A[index_r]) > abs(right - A[index_r]):
                ans_l += abs(left - A[index_r])
            else:
                ans_l += abs(right - A[index_r])
            index_l += 1
        else:
            break
    count += 1

A = A[::-1]

right = A[0]
left = A[0]
index_l = 1
index_r = len(A) - 1
ans_r = 0
count = 1

while True:
    if count % 2 == 1:
        if index_r - index_l >= 1:
            diff1 = abs(left - A[index_r]) + abs(right - A[index_r - 1])
            diff2 = abs(right - A[index_r]) + abs(left - A[index_r - 1])
            if diff1 > diff2:
                ans_r += diff1
                left = A[index_r]
                right = A[index_r - 1]
            else:
                ans_r += diff2
                left = A[index_r - 1]
                right = A[index_r]
            index_r -= 2
        elif index_r - index_l == 0:
            if abs(left - A[index_r]) > abs(right - A[index_r]):
                ans_r += abs(left - A[index_r])
            else:
                ans_r += abs(right - A[index_r])
            index_r -= 1
        else:
            break
    else:
        if index_r - index_l >= 1:
            diff1 = abs(left - A[index_l]) + abs(right - A[index_l + 1])
            diff2 = abs(right - A[index_l]) + abs(left - A[index_l + 1])
            if diff1 > diff2:
                ans_r += diff1
                left = A[index_l]
                right = A[index_l + 1]
            else:
                ans_r += diff2
                left = A[index_l + 1]
                right = A[index_l]
            index_l += 2
        elif index_r - index_l == 0:
            if abs(left - A[index_r]) > abs(right - A[index_r]):
                ans_r += abs(left - A[index_r])
            else:
                ans_r += abs(right - A[index_r])
            index_l += 1
        else:
            break
    count += 1

print(max(ans_l, ans_r))