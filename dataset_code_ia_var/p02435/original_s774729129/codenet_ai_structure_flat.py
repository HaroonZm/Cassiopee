n, r = input().split(' ')
n = int(n)
r = int(r)
stack = []
for _ in range(n):
    stack.append([])
i_r = 0
while i_r < r:
    row = input().split(' ')
    c = int(row[0])
    i = int(row[1])
    if c == 0:
        stack[i].append(int(row[2]))
    if len(stack[i]) > 0:
        if c == 1:
            print(stack[i][-1])
        if c == 2:
            stack[i].pop()
    i_r += 1