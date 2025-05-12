a = []
n = int(raw_input())
for _ in range(n):
    a.append(map(int, raw_input().split()))
for i in range(n):
    f = [1,1,1]
    for j in range(n):
        if i == j:
            continue
        for k in range(3):
            if a[i][k] == a[j][k]:
                f[k] = 0
    print a[i][0]*f[0] + a[i][1]*f[1] + a[i][2]*f[2]