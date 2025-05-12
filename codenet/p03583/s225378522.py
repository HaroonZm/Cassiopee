N = int(input())
for h in range(1,3501):
    for n in range(1,3501):
        p = 4*h*n - N*h - N*n
        if p <= 0:
            continue
        else:
            if (h*n) % p == 0:
                print(str(h) + " " + str(n) + " " + str((N*h*n)//p))
                exit()