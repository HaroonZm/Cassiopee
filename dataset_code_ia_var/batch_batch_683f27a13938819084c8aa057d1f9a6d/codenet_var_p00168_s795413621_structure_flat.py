n_values = []
while True:
    n = int(raw_input())
    if n == 0:
        break
    n_values.append(n)
for n in n_values:
    goal = [0 for i in range(n)]
    if n > 0:
        goal[0] = 1
    if n > 1:
        goal[1] = 2
    if n > 2:
        goal[2] = 4
    i = 3
    while i < n:
        goal[i] = goal[i-1] + goal[i-2] + goal[i-3]
        i += 1
    print ((goal[-1] // 10 + 1) // 365 + 1)