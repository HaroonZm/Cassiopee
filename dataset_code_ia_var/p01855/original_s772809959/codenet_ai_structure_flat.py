t = int(input())
while t:
    t -= 1
    a, b = map(int, input().split())
    x = a
    y = b
    while x != 0:
        temp = x
        x = y % x
        y = temp
    c = y
    a = a // c
    b = b // c
    if a == b:
        ans1 = 1
        ans2 = 0
    elif a % 2 == 0 or b % 2 == 0:
        ans1 = 1
        ans2 = 1
    else:
        ans1 = a * b // 2 + 1
        ans2 = a * b // 2
    print(ans1, ans2)