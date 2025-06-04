X_Y = input().split()
X = int(X_Y[0])
Y = int(X_Y[1])
i = 0
while i <= X:
    kame = 2 * i
    ashi = Y - kame
    if ashi % 4 == 0:
        if ashi // 4 == X - i:
            print("Yes")
            exit()
    i += 1
print("No")