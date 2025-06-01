while True:
    line = raw_input()
    a, b = line.split()
    a = int(a)
    b = int(b)
    if a == 0 and b == 0:
        break

    sums = [0] * b
    for i in range(a):
        codes = raw_input().split()
        for j in range(b):
            sums[j] += int(codes[j])

    pairs = []
    for i in range(b):
        pairs.append((i, sums[i]))

    pairs.sort(key=lambda x: x[1], reverse=True)

    for p in pairs:
        print p[0] + 1,
    print()