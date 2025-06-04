h, w = map(int, input().split())
l = [input().split() for _ in range(h)]
for i in range(h):
    for j in range(w):
        if l[i][j] == "snuke":
            print(chr(ord("A") + j) + str(i + 1))
            exit()