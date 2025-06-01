while True:
    line = raw_input()
    n, m = line.split()
    n = int(n)
    m = int(m)
    if n == 0 and m == 0:
        break
    r = []
    for i in range(m):
        r.append(0)
    for i in range(n):
        line = raw_input()
        numbers = line.split()
        for j in range(m):
            r[j] = r[j] - int(numbers[j])
    pairs = []
    for i in range(m):
        pairs.append((r[i], i+1))
    pairs.sort()
    result = []
    for pair in pairs:
        result.append(str(pair[1]))
    print ' '.join(result)