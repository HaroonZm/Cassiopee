h, w = map(int, input().split())
l = []
for i in range(h):
    l.append(list(map(str, input().split())))
i = 0
found = False
while i < h and not found:
    j = 0
    while j < w and not found:
        if l[i][j] == 'snuke':
            print(chr(65 + j) + str(i + 1))
            found = True
        j += 1
    i += 1