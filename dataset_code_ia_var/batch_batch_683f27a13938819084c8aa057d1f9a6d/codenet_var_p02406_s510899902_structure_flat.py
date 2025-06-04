n = int(input())
i = 1
while i <= n:
    x = i
    if x % 3 == 0:
        print("", i, end="")
        i += 1
        continue
    flag = False
    while x > 0:
        if x % 10 == 3:
            print("", i, end="")
            flag = True
            break
        x //= 10
    i += 1
print("")