x = int(input())
i = x
while i <= 100003:
    est_premier = True
    j = 2
    while j < i:
        if i % j == 0:
            est_premier = False
            break
        j = j + 1
    if est_premier:
        print(i)
        break
    i = i + 1