inputs = []
for _ in range(2):
    inputs.append(input())
n = int(inputs[0])
a = []
for x in inputs[1].split(" "):
    a.append(int(x))
b = {}
for i in a:
    if i not in b:
        b[i] = 1
    else:
        b[i] += 1
count = 0
for k in b:
    tmp = k - b[k]
    if tmp > 0:
        count += b[k]
    else:
        count += -tmp
print(count)