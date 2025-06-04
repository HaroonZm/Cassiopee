n = int(input())

for i in range(n):
    numbers = input().split()
    x = int(numbers[0])
    y = int(numbers[1])
    b = int(numbers[2])
    p = int(numbers[3])

    total_normal = x * b + y * p

    if b < 5 and p < 2:
        promo = (x * 5 + y * 2) * 0.8
        if total_normal < promo:
            ans = total_normal
        else:
            ans = promo
    elif b >= 5 and p < 2:
        promo = (x * b + y * 2) * 0.8
        if total_normal < promo:
            ans = total_normal
        else:
            ans = promo
    elif b < 5 and p >= 2:
        promo = (x * 5 + y * p) * 0.8
        if total_normal < promo:
            ans = total_normal
        else:
            ans = promo
    else:
        ans = total_normal * 0.8

    print(int(ans))