from collections import deque

number_list = [float("inf") for i in range(1000 + 1)]
number_list[1] = 0
que = deque([[1, [1], 0]])

while len(que) > 0:
    n, array, depth = que.popleft()
    if depth > 16:
        continue
    for i in array:
        if n + i <= 1000 and number_list[n + i] >= depth + 1:
            number_list[n + i] = depth + 1
            que.append([n + i, array + [n + i], depth + 1])

        if n - i > 0 and number_list[n - i] >= depth + 1:
            number_list[n - i] = depth + 1
            que.append([n - i, array + [n - i], depth + 1])

while True:
    N = int(input())
    if N == 0:
        break
    print(number_list[N])