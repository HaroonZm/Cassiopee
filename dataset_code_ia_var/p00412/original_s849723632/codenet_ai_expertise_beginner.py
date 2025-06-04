n, m = input().split()
n = int(n)
m = int(m)

rane = []
for i in range(n):
    rane.append([])

def get_rane():
    index = 0
    min_len = 9999
    for i in range(n):
        if len(rane[i]) < min_len:
            min_len = len(rane[i])
            if min_len == 0:
                return i
            index = i
    return index

for i in range(m):
    inputs = input().split()
    c = int(inputs[0])
    num = int(inputs[1])
    if c == 0:
        num = num - 1
        print(rane[num][0])
        rane[num].pop(0)
    else:
        idx = get_rane()
        rane[idx].append(num)