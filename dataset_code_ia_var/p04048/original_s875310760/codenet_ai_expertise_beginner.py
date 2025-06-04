N_X = input().split()
N = int(N_X[0])
X = int(N_X[1])
ans = N
a = X
b = N - X

if a > b:
    temp = a
    a = b
    b = temp

while a != 0:
    if b % a == 0:
        ans = ans + 2 * (b // a - 1) * a + a
        print(ans)
        break
    else:
        ans = ans + 2 * (b // a) * a
        temp = b % a
        b = a
        a = temp
        if a > b:
            temp = a
            a = b
            b = temp