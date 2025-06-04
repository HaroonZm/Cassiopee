n = int(input())
i = 0
while i < (1 << n):
    rs = [str(i) + ":"]
    j = 0
    while j < n:
        if i & (1 << j):
            rs.append(j)
        j += 1
    print(*rs)
    i += 1