a = int(input())
ar = list(map(int,input().split(" ")))
br = []
while True:
    b = len(ar)
    s = "N"
    for i in range(b-1,-1,-1):
        if ar[i] == i+1:
            s = "Y"
            br.append(ar[i])
            del ar[i]
            break
    if s == "N":
        print(-1)
        exit()
    if len(ar) == 0:
        break
for i in range(a-1,-1,-1):
    print(br[i])