while True:
    n = int(input())
    if n == 0:
        break
    numList = [0,0,0,0,0,0,0,0,0,0]
    i = 0
    while i < n:
        c = int(input())
        numList[c] = numList[c] + 1
        i = i + 1
    j = 0
    while j < 10:
        cnt = ''
        k = 0
        while k < numList[j]:
            cnt = cnt + '*'
            k = k + 1
        if len(cnt) == 0:
            print("-")
        else:
            print(cnt)
        j = j + 1