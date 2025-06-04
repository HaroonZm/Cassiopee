import sys
n = int(sys.stdin.readline())
data = []
i = 0
while i < n:
    s = sys.stdin.readline().split()
    b = "*" + s[0]
    a = "*" + s[1]
    d = s[2]
    row = [b, a, d]
    data.append(row)
    i += 1

q = int(sys.stdin.readline())
j = 0
while j < q:
    parts = sys.stdin.readline().split()
    qb = parts[0]
    qa = parts[1]
    f = parts[2]
    t = parts[3]
    if t == "*":
        t = "9" + t
    k = 0
    while k < len(data):
        b = data[k][0]
        a = data[k][1]
        d = data[k][2]
        if qb in b and qa in a and f <= d <= t:
            print(b[1:])
        k += 1
    if j < q-1:
        print()
    j += 1