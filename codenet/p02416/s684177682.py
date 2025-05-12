while True:
    x = input()
    if x == "0":
        break
    sum_s = 0
    for s in x:
        sum_s += int(s)
    print(sum_s)