n, m = input().split()
n = int(n)
m = int(m)

table = []
for i in range(n):
    table.append([])

for l in range(m):
    cmd, num = input().split()
    cmd = int(cmd)
    num = int(num)
    if cmd == 0:
        print(table[num-1][0])
        del table[num-1][0]
    else:
        min_len = 10000
        min_idx = -1
        for i in range(n):
            if len(table[i]) < min_len:
                min_len = len(table[i])
                min_idx = i
        table[min_idx].append(num)