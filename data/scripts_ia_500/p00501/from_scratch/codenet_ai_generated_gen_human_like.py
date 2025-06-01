N = int(input())
shop_name = input()
old_signs = [input() for _ in range(N)]

count = 0
length = len(shop_name)

for sign in old_signs:
    sign_len = len(sign)
    can_make = False

    # interval d must be at least 1 and at most such that last char fits
    for d in range(1, sign_len):
        if d * (length - 1) >= sign_len:
            break

        # try all possible start positions where the substring fits
        for start in range(sign_len - d * (length - 1)):
            # check if with start and interval d we can get shop_name
            matched = True
            for i in range(length):
                if sign[start + d * i] != shop_name[i]:
                    matched = False
                    break
            if matched:
                can_make = True
                break
        if can_make:
            break

    if can_make:
        count += 1

print(count)