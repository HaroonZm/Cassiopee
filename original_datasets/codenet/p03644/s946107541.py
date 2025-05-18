N = int(input())

best = 1
best_count = 0
for n in range(1, N+1):
    i = n
    count = 0
    while True:
        q, mod = divmod(i, 2)
        if mod == 0:
            i = q
            count += 1
        else:
            break
    if count > best_count:
        best = n
        best_count = count

print(best)