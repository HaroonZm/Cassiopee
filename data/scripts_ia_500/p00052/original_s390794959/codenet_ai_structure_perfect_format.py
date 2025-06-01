def calc(n):
    cnt_2 = 0
    cnt_5 = 0
    while n % 2 == 0:
        n /= 2
        cnt_2 += 1
    while n % 5 == 0:
        n /= 5
        cnt_5 += 1
    return cnt_2, cnt_5

while True:
    N = input()
    if N == 0:
        quit()
    t2 = 0
    t5 = 0
    for i in range(N, 0, -1):
        x, y = calc(i)
        t2 += x
        t5 += y
    print(min(t2, t5))