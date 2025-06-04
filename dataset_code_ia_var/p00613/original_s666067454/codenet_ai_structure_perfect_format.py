while True:
    k = input()
    if not k:
        break
    print(sum(map(int, raw_input().split())) / (k - 1))