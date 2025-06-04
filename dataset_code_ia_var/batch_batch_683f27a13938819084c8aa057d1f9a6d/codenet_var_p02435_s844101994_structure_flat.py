n_q = input().split(' ')
n = int(n_q[0])
q = int(n_q[1])
stacks = []
i = 0
while i < n:
    stacks.append([])
    i += 1
j = 0
while j < q:
    op = input().split(' ')
    if int(op[0]) == 0:
        stacks[int(op[1])].append(int(op[2]))
    elif int(op[0]) == 1:
        if len(stacks[int(op[1])]) != 0:
            print(stacks[int(op[1])][-1])
    elif int(op[0]) == 2:
        if len(stacks[int(op[1])]) != 0:
            stacks[int(op[1])].pop()
    j += 1