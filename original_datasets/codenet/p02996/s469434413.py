n = int(input())
task = [[int(i) for i in input().split()] for _ in range(n)]
task.sort(key=lambda x:x[1])
t = 0
for i in task:
    t += i[0]
    if t > i[1]:
        exit(print('No'))
print('Yes')