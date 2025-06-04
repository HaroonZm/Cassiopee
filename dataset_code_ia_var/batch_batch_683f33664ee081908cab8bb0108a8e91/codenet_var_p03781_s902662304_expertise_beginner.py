x = int(input())

i = 1
while i <= x:
    if (i * (i + 1)) // 2 >= x:
        print(i)
        break
    i = i + 1