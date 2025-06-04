N = int(input())
shop_name = input()
old_signs = [input() for _ in range(N)]

count = 0
len_shop = len(shop_name)

for sign in old_signs:
    len_sign = len(sign)
    can_make = False
    for d in range(1, len_sign):
        for start in range(len_sign):
            if start + d * (len_shop - 1) >= len_sign:
                break
            formed = ''.join(sign[start + i * d] for i in range(len_shop))
            if formed == shop_name:
                can_make = True
                break
        if can_make:
            break
    if can_make:
        count += 1

print(count)