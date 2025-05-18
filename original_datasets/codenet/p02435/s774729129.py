n, r = input().split(' ')
stack = [[] for _ in range(int(n))]
for _ in range(int(r)):
    row = list(map(int, input().split(' ')))
    c = row[0]
    i = row[1]

    if c == 0:
        stack[i].append(row[2])
    if stack[i]:
        if c == 1:
            print(stack[i][-1])
        if c == 2:
            stack[i].pop()