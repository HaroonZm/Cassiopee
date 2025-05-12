while True:

    inp = int(input())

    if inp == 0:
        break

    times = int(inp / 4)

    sum = 0

    for i in range(times):
        sum += int(input())

    print(sum)