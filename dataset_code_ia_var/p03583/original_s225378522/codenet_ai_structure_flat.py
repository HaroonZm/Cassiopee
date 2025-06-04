N = int(input())
h = 1
while h < 3501:
    n = 1
    while n < 3501:
        p = 4*h*n - N*h - N*n
        if p > 0:
            if (h*n) % p == 0:
                print(str(h) + " " + str(n) + " " + str((N*h*n)//p))
                exit()
        n += 1
    h += 1