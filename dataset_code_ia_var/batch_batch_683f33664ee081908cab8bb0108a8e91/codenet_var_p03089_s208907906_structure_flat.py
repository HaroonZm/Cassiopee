a = int(input())
ar = list(map(int, input().split(" ")))
br = []
while True:
    b = len(ar)
    s = "N"
    i = b - 1
    while i >= 0:
        if ar[i] == i + 1:
            s = "Y"
            br.append(ar[i])
            del ar[i]
            break
        i -= 1
    if s == "N":
        print(-1)
        exit()
    if len(ar) == 0:
        break
i = a - 1
while i >= 0:
    print(br[i])
    i -= 1