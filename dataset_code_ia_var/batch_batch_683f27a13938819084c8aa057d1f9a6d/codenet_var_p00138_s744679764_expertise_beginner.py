x = []
y = []
for i in range(3):
    temp = []
    for j in range(8):
        line = raw_input()
        parts = line.split()
        parts.reverse()
        temp.append(parts)
    temp.sort()
    x.append(temp[0])
    x.append(temp[1])
    y.append(temp[2])
    y.append(temp[3])
y_sorted = sorted(y)
x.append(y_sorted[0])
x.append(y_sorted[1])

for e in x:
    e.reverse()
    print " ".join(e)