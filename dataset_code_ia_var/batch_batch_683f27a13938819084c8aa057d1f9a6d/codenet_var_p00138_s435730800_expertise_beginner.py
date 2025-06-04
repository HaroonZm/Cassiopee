data = []
temp = []
result = []

def add_to_result(d):
    for j in range(2):
        result.append((d[0][0], d[0][1]))
        d.pop(0)

for i in range(24):
    a, b = input().split()
    a = float(a)
    b = float(b)
    temp.append((a, b))
    if (i + 1) % 8 == 0:
        temp.sort(key=lambda x: x[1])
        add_to_result(temp)
        data += temp
        temp = []

data.sort(key=lambda x: x[1])
add_to_result(data)

for i in range(8):
    print(int(result[i][0]), result[i][1])