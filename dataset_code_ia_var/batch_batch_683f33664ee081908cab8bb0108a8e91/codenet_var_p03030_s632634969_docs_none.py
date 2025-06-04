n = int(input())
rs = []
for i in range(n):
    s, p = input().split()
    p = int(p)
    rs.append([[s, -p], i+1])
for r in sorted(rs):
    print(r[1])