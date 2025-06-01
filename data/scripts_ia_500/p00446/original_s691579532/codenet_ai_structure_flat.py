while True:
    n = int(input())
    if n == 0:
        exit()
    taro = []
    for _ in range(n):
        taro.append(int(input()))
    hanako = []
    for i in range(1, 2 * n + 1):
        if i not in taro:
            hanako.append(i)
    taro.sort()
    m = 0
    taro_flg = True
    while len(taro) > 0 and len(hanako) > 0:
        if taro_flg:
            i = 0
            while i < len(taro):
                if taro[i] > m:
                    m = taro[i]
                    taro.pop(i)
                    break
                if i == len(taro) - 1:
                    m = 0
                i += 1
            taro_flg = False
        else:
            i = 0
            while i < len(hanako):
                if hanako[i] > m:
                    m = hanako[i]
                    hanako.pop(i)
                    break
                if i == len(hanako) - 1:
                    m = 0
                i += 1
            taro_flg = True
    print(len(hanako))
    print(len(taro))