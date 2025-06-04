def f(x):
    a, c = x, 0
    while True:
        b = list(map(lambda e: a.count(e), a))
        if a == b:
            return c, " ".join(str(i) for i in a)
        else:
            a, c = b, c + 1

while True:
    user_input = input()
    if user_input == '0':
        break
    else:
        line = input()
        nums = list(map(int, line.split()))
        res_c, res_s = f(nums)
        print(res_c)
        print(res_s)