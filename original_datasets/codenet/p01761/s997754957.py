import sys
n = int(sys.stdin.readline())
data = [[None]*3 for i in range(n)]
for i in range(n):
    s = sys.stdin.readline().split()
    data[i][0] = "*"+s[0]
    data[i][1] = "*"+s[1]
    data[i][2] = s[2]

q = int(sys.stdin.readline())
for i in range(q):
    qb,qa,f,t = sys.stdin.readline().split()
    if t == "*":
        t = "9"+t
    for b,a,d in data:
        if qb in b and qa in a and f <= d <= t:
            print(b[1:])
    if i < q-1:
        print()