d = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

while True:
    line = input()
    if not line:
        break
    line = line.strip()
    values = []
    for char in line:
        values.append(d[char])
    if len(values) == 1:
        print(values[0])
    else:
        total = sum(values)
        for i in range(len(values) -1):
            if values[i] < values[i+1]:
                total = total - 2 * values[i]
        print(total)