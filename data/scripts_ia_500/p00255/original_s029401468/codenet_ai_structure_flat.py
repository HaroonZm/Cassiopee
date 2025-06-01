while True:
    n = input()
    if n == '0':
        break
    p = input().strip().split(" ")
    j = input().strip().split(" ")
    p = [int(x) for x in p]
    j = [int(x) for x in j]
    j.sort(reverse=True)
    sum_p = 0
    for m in p:
        sum_p += m
    num = int(n)
    for i in range(num - 1):
        if (num - 1) * (sum_p + j[i]) < num * sum_p:
            break
        num -= 1
        sum_p += j[i]
    print(num * sum_p)