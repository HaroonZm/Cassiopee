while True:
    N = int(input())
    if N == 0:
        break

    lines = []
    for i in range(N):
        lines.append(input())
    parts = input().split()
    P = int(parts[0])
    Q = int(parts[1])
    R = int(parts[2])
    C = int(parts[3])

    found = False
    for line in lines:
        data = line.split()
        s = int(data[0])
        p = int(data[1])
        q = int(data[2])
        r = int(data[3])
        if p <= P and q <= Q and r <= R and 4*p + 9*q + 4*r <= C:
            print(s)
            found = True
    if not found:
        print("NA")