m, d = map(int, input().split())
count = 0
for month in range(1, m + 1):
    for i in range(2, 10):
        if month % i == 0:
            div = month // i
            if 1 < div < 10:
                if i * 10 + div <= d:
                    count += 1
print(count)