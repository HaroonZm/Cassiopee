while True:
    n_m = input().split()
    n = int(n_m[0])
    m = int(n_m[1])
    if n == 0 and m == 0:
        break

    a_list = input().split()
    a = []
    for num in a_list:
        a.append(int(num))

    ans = 0

    limit = m // n

    for num in a:
        if num < limit:
            ans += num
        else:
            ans += limit

    print(ans)