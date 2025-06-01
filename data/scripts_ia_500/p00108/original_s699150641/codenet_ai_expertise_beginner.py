f = [0] * 105

while True:
    n = int(input())
    if n == 0:
        break

    numbers = list(map(int, input().split()))
    current = numbers[:]
    count = 0

    while True:
        for num in current:
            f[num] += 1

        next_list = []
        for num in current:
            next_list.append(f[num])

        for num in current:
            f[num] = 0

        if next_list == current:
            break
        else:
            current = next_list
            count += 1

    print(count)
    print(*current)