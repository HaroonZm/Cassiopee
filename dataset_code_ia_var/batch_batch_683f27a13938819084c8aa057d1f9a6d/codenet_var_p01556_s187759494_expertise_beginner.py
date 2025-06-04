N = int(input())
lst = []

for i in range(N):
    X_Y = input().split()
    X = int(X_Y[0])
    Y = int(X_Y[1])
    lst.append((X, Y))

if N % 2 != 0:
    print("NA")
    exit()

ansx = lst[0][0] + lst[N // 2][0]
ansy = lst[0][1] + lst[N // 2][1]

i = 0
while i < (N // 2):
    x = lst[i][0] + lst[i + N // 2][0]
    y = lst[i][1] + lst[i + N // 2][1]
    if x != ansx or y != ansy:
        print("NA")
        exit()
    i = i + 1

print(str(ansx / 2.0) + " " + str(ansy / 2.0))