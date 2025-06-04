while True:
    e = input()
    if e == '0 0':
        break
    r = int(e.split()[0])
    d = []
    rows = []
    for _ in range(r):
        row = input().split()
        rows.append(row)
    for i in range(len(rows[0])):
        bits = []
        for j in range(r):
            bits.append(rows[j][i])
        binary_str = ''.join(bits)
        d.append(int(binary_str, 2))
    max_score = 0
    for i in range(2**r):
        total = 0
        for j in d:
            c = bin(i ^ j).count('1')
            if c > r // 2:
                total += c
            else:
                total += r - c
        if total > max_score:
            max_score = total
    print(max_score)