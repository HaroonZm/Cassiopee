while True:
    n = int(input())
    if n == 0:
        break

    data = [0 for i in range(10)]
    for i in range(n):
        data[int(input())] += 1

    for i in range(10):
        if data[i] == 0:
            print("-")
        else:
            print("*" * data[i])