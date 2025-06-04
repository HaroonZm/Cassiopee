import sys

for line in sys.stdin:
    numbers = line.strip().split(",")
    values = []
    for num in numbers:
        values.append(int(num))
    k_list = []
    for i in range(len(values) - 1):
        s = 0
        for j in range(i):
            s += values[j]
        k_list.append(s)
    total = values[-2] + values[-1]
    if total != 0:
        l = (values[-2] / total) * k_list[-1]
    else:
        l = 0
    n_list = []
    for a in k_list:
        diff = a - l
        if diff >= 0:
            n_list.append(diff)
        else:
            n_list.append(10000000000.0)
    min_value = min(n_list)
    min_index = n_list.index(min_value)
    print(min_index)