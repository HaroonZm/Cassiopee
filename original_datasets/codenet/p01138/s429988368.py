def cvtTime(s):
    h, m, s = map(int, s.split(":"))
    return h * 60 * 60 + m * 60 + s

while True:
    n = int(input())
    if n == 0:
        break

    cnt = [0] * (60 * 60 * 24 + 2)

    for i in range(n):
        begin, end = input().split()
        begin_time = cvtTime(begin)
        end_time = cvtTime(end)

        cnt[begin_time] += 1
        cnt[end_time] -= 1

    for i in range(1, len(cnt)):
        cnt[i] += cnt[i - 1]

    print(max(cnt))