N = int(input())

sum = 0

if N <= 2:
    print(N)
else:
    i = 1
    while i < N:
        sum += i
        if sum >= N:
            break
        i += 1
    j = 1
    while j <= i:
        if j == sum - N:
            j += 1
            continue
        print(j)
        j += 1