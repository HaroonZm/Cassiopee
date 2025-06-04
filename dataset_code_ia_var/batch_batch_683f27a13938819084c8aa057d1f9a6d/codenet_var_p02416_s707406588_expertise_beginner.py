x = input()
while x != "0":
    total = 0
    for c in x:
        total = total + int(c)
    print(total)
    x = input()