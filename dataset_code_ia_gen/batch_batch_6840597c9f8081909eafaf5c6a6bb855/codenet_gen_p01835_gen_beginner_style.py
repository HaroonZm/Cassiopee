N, K = map(int, input().split())
T = int(input())
tasks = []
for _ in range(T):
    l, r, x = map(int, input().split())
    tasks.append((l, r, x))

done = [0] * (N + 2)
for l, r, x in tasks:
    if x == 1:
        for i in range(l, r + 1):
            done[i] = 1

for task_num in range(2, K + 1):
    new_done = [0] * (N + 2)
    # find consecutive segments where done[i] == task_num - 1
    i = 1
    while i <= N:
        if done[i] == task_num - 1:
            start = i
            while i <= N and done[i] == task_num - 1:
                i += 1
            end = i - 1
            # check if any task with task_num covers a subinterval of [start,end]
            for l, r, x in tasks:
                if x == task_num:
                    left = max(l, start)
                    right = min(r, end)
                    if left <= right:
                        for j in range(left, right + 1):
                            new_done[j] = task_num
        else:
            i += 1
    done = new_done

result = 0
for i in range(1, N + 1):
    if done[i] == K:
        result += 1

print(result)