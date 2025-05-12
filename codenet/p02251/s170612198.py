n = int(input())
n_calc = n

C = [1, 5, 10, 25]

cnt = 0

for c in C[::-1]:
    q, n_calc = divmod(n_calc, c)
    cnt += q

    if int(n_calc) == 0:
        break

print(cnt)