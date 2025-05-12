def calc_start(mid):
    cnt = -1
    i = 1
    while 10 ** i < mid:
        cnt += i * (10 ** i - 10 ** (i - 1))
        fif = (10 ** i - 1) // 15 - (10 ** (i - 1) - 1) // 15
        three = (10 ** i - 1) // 3 - (10 ** (i - 1) - 1) // 3
        five = (10 ** i - 1) // 5 - (10 ** (i - 1) - 1) // 5
        cnt += (three + five) * 4 - (three + five - fif) * i
        i += 1
    cnt += i * (mid - 10 ** (i - 1))
    fif = (mid - 1) // 15 - (10 ** (i - 1) - 1) // 15
    three = (mid - 1) // 3 - (10 ** (i - 1) - 1) // 3
    five = (mid - 1) // 5 - (10 ** (i - 1) - 1) // 5
    cnt += (three + five) * 4 - (three + five - fif) * i
    return cnt + 1

N = int(input()) - 1
left, right = 1, 10 ** 18
while left + 1 < right:
    mid = (left + right) // 2
    start = calc_start(mid)
    if start <= N:
        left = mid
    else:
        right = mid
ans = ''
for i in range(left, left + 30):
    tmp = ''
    if i % 3 == 0:
        tmp += "Fizz"
    if i % 5 == 0:
        tmp += "Buzz"
    if not tmp:
        tmp = str(i)
    ans += tmp
start = calc_start(left)
print(ans[N - start:N - start + 20])