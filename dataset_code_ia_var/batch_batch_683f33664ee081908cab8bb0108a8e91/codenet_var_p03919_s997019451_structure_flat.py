h, w = map(int, input().split())
l = []
for _ in range(h):
    l.append(list(input().split()))
i = 0
while i < h:
    j = 0
    while j < w:
        if l[i][j] == "snuke":
            print(chr(ord("A") + j) + str(i + 1))
            import sys; sys.exit()
        j += 1
    i += 1