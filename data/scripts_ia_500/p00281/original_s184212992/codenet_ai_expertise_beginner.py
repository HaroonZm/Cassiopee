while True:
    try:
        n, m = map(int, input().split())
    except:
        break

    rs = []
    while True:
        line = input()
        if line == "0 0 0":
            break
        s, t, e = map(int, line.split())
        rs.append((s - 1, t - 1, e))
    
    l = int(input())
    b = []
    for _ in range(l):
        row = list(map(int, input().split()))
        b.append(row)
    
    c = []
    for i in range(l):
        c.append([0] * n)
    
    for s, t, e in rs:
        for i in range(l):
            c[i][s] += b[i][t] * e
    
    for i in range(l):
        line_out = ""
        for x in c[i]:
            line_out += str(x) + " "
        print(line_out.strip())