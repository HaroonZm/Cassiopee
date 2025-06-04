A, B, C = map(int, input().split())
sum = 0
i = 0
while True:
    sum += A
    i += 1
    if sum >= C:
        print(i)
        break
    if i % 7 == 0:
        sum += B
        if sum >= C:
            print(i)
            break