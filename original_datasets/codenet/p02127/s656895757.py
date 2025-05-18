s = input()
t = " " + input()
line = [1]
next = 1
t_size = len(t)
flag = False
for i in s:
    if t[next] == i:
        line[0] += 1
        next = line[0]
        line += [0]
        j = 0
        while line[j] == t_size:
            line[j] = 0
            next = line[j + 1] = line[j + 1] + 1
            j += 1
        if line[-1] == 0:
            line.pop()
print(len(line) - 1)