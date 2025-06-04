while True:
    x = input()
    if x == "0":
        break
    total = 0
    for number in x:
        total = total + int(number)
    print(total)