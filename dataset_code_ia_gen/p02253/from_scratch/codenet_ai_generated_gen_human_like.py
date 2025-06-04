n = int(input())
activities = [tuple(map(int, input().split())) for _ in range(n)]
activities.sort(key=lambda x: x[1])

count = 0
last_finish = 0

for start, finish in activities:
    if start >= last_finish:
        count += 1
        last_finish = finish

print(count)