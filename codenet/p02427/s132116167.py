n = int(input())
for i in range(1 << n):
    rs = [str(i) + ":"]
    for j in range(n):
        if i & (1 << j) != 0:
           rs.append(j)
    print(*rs)