while True:
    line = raw_input()
    n_m = line.split()
    n = int(n_m[0])
    m = int(n_m[1])
    if n == 0 and m == 0:
        break
    r = []
    for i in range(m):
        r.append(0)
    for i in range(n):
        numbers = raw_input().split()
        for j in range(m):
            r[j] = r[j] - int(numbers[j])
    temp = []
    for i in range(m):
        temp.append((r[i], i+1))
    temp_sorted = sorted(temp)
    result = []
    for item in temp_sorted:
        result.append(str(item[1]))
    print ' '.join(result)