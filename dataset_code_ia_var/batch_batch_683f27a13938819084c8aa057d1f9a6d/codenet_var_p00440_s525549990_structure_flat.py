while True:
    tmp = input().split()
    n = int(tmp[0])
    k = int(tmp[1])
    if n == 0:
        break
    cards = []
    for _ in range(k):
        cards.append(int(input()))
    cards.sort(reverse=True)
    white = False
    if cards and cards[-1] == 0:
        white = True
        cards.pop()
    if not cards:
        print(1)
        continue
    prev = cards.pop()
    cnt = 1
    precnt = 0
    ans = 1
    while cards:
        cur = cards.pop()
        diff = cur - prev
        if diff == 1:
            cnt += 1
        else:
            if precnt + cnt > ans:
                ans = precnt + cnt
            if white and diff == 2:
                precnt = cnt + 1
            else:
                precnt = 0
            cnt = 1
        prev = cur
    if precnt + cnt > ans:
        ans = precnt + cnt
    print(ans)