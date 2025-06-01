n = int(input())
i = 0
while i < n:
    print("Case", str(i+1) + ":")
    tmp = input()
    j = 0
    while j < 10:
        tmp = str(int(tmp)**2).zfill(8)[2:6]
        print(int(tmp))
        j += 1
    i += 1