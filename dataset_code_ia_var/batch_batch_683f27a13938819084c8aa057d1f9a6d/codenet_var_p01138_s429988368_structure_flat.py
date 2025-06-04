while True:
    n = int(input())
    if n == 0:
        break

    cnt = [0] * (60 * 60 * 24 + 2)

    for _ in range(n):
        begin, end = input().split()
        h, m, s = map(int, begin.split(":"))
        begin_time = h * 60 * 60 + m * 60 + s
        h, m, s = map(int, end.split(":"))
        end_time = h * 60 * 60 + m * 60 + s

        cnt[begin_time] += 1
        cnt[end_time] -= 1

    for i in range(1, len(cnt)):
        cnt[i] += cnt[i - 1]

    mx = cnt[0]
    for x in cnt:
        if x > mx:
            mx = x

    print(mx)