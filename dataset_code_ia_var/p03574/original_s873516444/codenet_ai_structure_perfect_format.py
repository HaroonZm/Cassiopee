h, w = map(int, input().split())
ms = []
for i in range(h):
    m = input()
    ms.append(list(m))

count = 0
for i in range(h):
    for j in range(w):
        if ms[i][j] == ".":
            if i > 0 and j > 0:
                if ms[i - 1][j - 1] == "#":
                    count += 1
            if i > 0:
                if ms[i - 1][j] == "#":
                    count += 1
            if i > 0 and j < w - 1:
                if ms[i - 1][j + 1] == "#":
                    count += 1
            if j > 0:
                if ms[i][j - 1] == "#":
                    count += 1
            if j < w - 1:
                if ms[i][j + 1] == "#":
                    count += 1
            if i < h - 1 and j > 0:
                if ms[i + 1][j - 1] == "#":
                    count += 1
            if i < h - 1:
                if ms[i + 1][j] == "#":
                    count += 1
            if i < h - 1 and j < w - 1:
                if ms[i + 1][j + 1] == "#":
                    count += 1
            ms[i][j] = str(count)
            count = 0

for i in range(h):
    temp = "".join([ms[i][j] for j in range(w)])
    print(temp)