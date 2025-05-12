while True:
    a,b = input().split()
    if a == b == "0":
        break
    count = 0
    for i in range(4):
        if a[i] == b[i]:
            count += 1
    print(count,end = " ")
    newcount = 0
    for j in range(4):
        if a[j] == b[0] or a[j] == b[1] or a[j] == b[2] or a[j] == b[3]:
            newcount += 1
    print(newcount - count)