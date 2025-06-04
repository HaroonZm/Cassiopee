N = int(input())
s = list(map(int, list(input())))

def add_calc(numbers):
    if len(numbers) <= 1:
        return 0
    dp_left = [0] * len(numbers)
    dp_right = [0] * len(numbers)
    dp_center = [0] * len(numbers)
    for i in range(len(numbers)-1):
        if numbers[i] > 1:
            dp_left[i+1] = max(dp_left[i] + numbers[i] - 1, dp_center[i] + numbers[i])
        else:
            dp_left[i+1] = dp_center[i] + numbers[i]
        if numbers[i] > 1:
            dp_right[i+1] = max(dp_left[i] + numbers[i+1], dp_center[i] + numbers[i+1], dp_right[i] + numbers[i+1] - 1)
        else:
            dp_right[i+1] = dp_center[i] + numbers[i+1]
        dp_center[i+1] = max(dp_left[i], dp_right[i], dp_center[i])
    return max(dp_left[-1], dp_right[-1], dp_center[-1])

count_1 = 1
count_2 = 1
small_list = []
answer = 0

for i in range(N):
    if s[i] == 1:
        if count_1 == 1:
            small_list.append(1)
            count_1 = 0
            count_2 = 0
        else:
            small_list[-1] += 1
    else:
        if count_2 == 1:
            continue
        elif count_1 == 1:
            count_2 = 1
            answer += add_calc(small_list)
            small_list = []
        else:
            count_1 = 1
    if i == N - 1:
        answer += add_calc(small_list)

print(answer)