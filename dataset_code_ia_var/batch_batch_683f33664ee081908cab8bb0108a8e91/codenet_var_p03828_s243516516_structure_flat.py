import math

x = int(input())
a = math.factorial(x)

sosu_list = []
for i in range(x+1):
    num = i
    is_p = True
    if num < 2:
        is_p = False
    elif num == 2 or num == 3 or num == 5:
        is_p = True
    elif num % 2 == 0 or num % 3 == 0 or num % 5 == 0:
        is_p = False
    else:
        prime = 7
        step = 4
        num_sqrt = math.sqrt(num)
        while prime <= num_sqrt:
            if num % prime == 0:
                is_p = False
                break
            prime += step
            step = 6 - step
    if is_p:
        sosu_list.append(i)

sosu_cnt = {}
for sosu in sosu_list:
    while a % sosu == 0:
        if sosu in sosu_cnt:
            sosu_cnt[sosu] += 1
        else:
            sosu_cnt[sosu] = 1
        a //= sosu

ans = 1
for key in sosu_cnt:
    sosu_cnt[key] += 1
    ans = (ans * sosu_cnt[key]) % (10 ** 9 + 7)
print(ans)