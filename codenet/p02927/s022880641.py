M, D = map(int, input().split())
count = 0
for month in range(1,M+1):
    for day in range(10,D+1):
        d_10, d_1 = map(int, list(str(day)))
        if d_10*d_1 == month and d_1 > 1 and d_10 > 1:
            count += 1

print(count)