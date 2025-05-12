N = int(input())
A = [(int(input()), 0) for i in range(N)]
B = [(int(input()), 1) for i in range(N)]
mod = 10 ** 9 + 7

X = A + B
X.sort()

ans = 1
Ar, Br = 0, 0

for x, i in X:
    if i == 0:
        if Br > 0:
            ans *= Br
            ans %= mod
            Br -= 1
        else:
            Ar += 1

    else:
        if Ar > 0:
            ans *= Ar
            ans %= mod
            Ar -= 1
        else:
            Br += 1

print(ans)