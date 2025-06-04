paper = []
for i in range(10):
    ligne = []
    for j in range(10):
        ligne.append(0)
    paper.append(ligne)

while True:
    try:
        entree = input()
        x, y, s = entree.split(',')
        x = int(x)
        y = int(y)
        s = int(s)
    except:
        break

    if s == 1:
        for i in range(10):
            for j in range(10):
                if abs(x - i) + abs(y - j) <= 1:
                    paper[i][j] = paper[i][j] + 1
    elif s == 2:
        for i in range(10):
            for j in range(10):
                if abs(x - i) <= 1 and abs(y - j) <= 1:
                    paper[i][j] = paper[i][j] + 1
    else:
        for i in range(10):
            for j in range(10):
                if abs(x - i) + abs(y - j) <= 2:
                    paper[i][j] = paper[i][j] + 1

ls = []
for i in range(10):
    for j in range(10):
        ls.append(paper[i][j])

zero_count = 0
for v in ls:
    if v == 0:
        zero_count = zero_count + 1
print(zero_count)

max_val = ls[0]
for v in ls:
    if v > max_val:
        max_val = v
print(max_val)